from typing import List
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.exceptions import InvalidLimitValueException, \
    InvalidOffsetValueException
from project_management_portal.adapters.service_adapter import \
    get_service_adapter
from project_management_portal.interactors.storages.dtos import \
    FinalProjectDTO, ListOfProjectsDto, ProjectDto


class GetProjectsInteractor:
    def __init__(self, storage: ProjectStorageInterface):
        self.storage = storage

    def get_list_of_projects_wrapper(self,
                                     limit: int,
                                     offset: int,
                                     user_id: int,
                                     presenter: PresenterInterface):
        try:
            response = self._get_list_of_projects_response(
                limit=limit,
                offset=offset,
                user_id=user_id,
                presenter=presenter
            )
            return response

        except InvalidLimitValueException:
            presenter.raise_invalid_limit_value_exception()
        except InvalidOffsetValueException:
            presenter.raise_invalid_offset_value_exception()

    def _get_list_of_projects_response(self,
                                       limit: int,
                                       offset: int,
                                       user_id: int,
                                       presenter: PresenterInterface):

        list_of_projects_dto = self.get_list_of_projects(limit=limit,
                                                         offset=offset,
                                                         user_id=user_id)

        response = presenter.get_list_of_projects_response(
            list_of_projects_dto=list_of_projects_dto
        )
        return response

    def get_list_of_projects(self, limit: int, offset: int, user_id: int):

        is_limit_value_valid = limit>=0
        is_limit_value_invalid = not is_limit_value_valid
        if is_limit_value_invalid:
            raise InvalidLimitValueException

        is_offset_value_valid = offset>=0
        is_offset_value_invalid = not is_offset_value_valid
        if is_offset_value_invalid:
            raise InvalidOffsetValueException

        service_adapter = get_service_adapter()
        is_admin_valid_dto = service_adapter.validate_admin. \
            get_is_admin_valid_dto(user_id=user_id)
        is_admin = is_admin_valid_dto.is_admin

        if is_admin:
            list_of_projects_dto = self.storage.get_list_of_admin_projects(
                limit=limit,
                offset=offset,
                user_id=user_id
            )
        else:
            list_of_projects_dto = self.storage.get_list_of_member_projects(
                limit=limit,
                offset=offset,
                user_id=user_id
            )
        final_list_of_project_details_dtos = self. \
            get_final_list_of_project_details_dtos(
                list_of_project_dtos=list_of_projects_dto.list_of_project_dtos
            )

        final_list_of_projects_details_dto = ListOfProjectsDto(
            list_of_project_dtos=final_list_of_project_details_dtos,
            total_count_of_projects=list_of_projects_dto.total_count_of_projects)
        return final_list_of_projects_details_dto


    def get_final_list_of_project_details_dtos(
        self, list_of_project_dtos: List[ProjectDto]):

        final_list_of_project_details_dtos = []
        service_adapter = get_service_adapter()
        for project_dto in list_of_project_dtos:
            user_ids = self.storage.get_user_ids(
                project_id=project_dto.project_id
            )
            user_details_dtos = service_adapter.auth_service.get_user_dtos(
                user_ids=user_ids
            )

            final_project_details_dto = FinalProjectDTO(
                user_details_dtos=user_details_dtos,
                project_details_dto=project_dto
            )
            final_list_of_project_details_dtos.append(
                final_project_details_dto
            )
        return final_list_of_project_details_dtos
