from typing import List
from project_management_portal.exceptions import InvalidWorkflowIdException, \
    InvalidAdminException
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.adapters.service_adapter import \
    get_service_adapter


class CreateProjectInteractor:
    def __init__(self, storage: ProjectStorageInterface):
            self.storage = storage

    def create_project_wrapper(self,
                               name: str,
                               user_id: int,
                               description: str,
                               project_type: str,
                               workflow_type: int,
                               a
                               presenter: PresenterInterface):

        try:
            response = self._get_create_project_response(
                name=name,
                user_id=user_id,
                presenter=presenter,
                description=description,
                project_type=project_type,
                workflow_type=workflow_type
            )
            return response
        except InvalidWorkflowIdException:
            presenter.raise_invalid_workflow_type_id_exception()
        except InvalidAdminException:
            presenter.raise_invalid_admin_exception()


    def _get_create_project_response(self,
                                     name: str,
                                     user_id: int,
                                     description: str,
                                     project_type: str,
                                     workflow_type: int,
                                     presenter: PresenterInterface):

        project_details_dto = self.create_project(
            name=name,
            user_id=user_id,
            description=description,
            project_type=project_type,
            workflow_type=workflow_type
        )
        response = presenter.get_create_project_response(
            project_details_dto=project_details_dto
        )
        return response

    def create_project(self,
                       name: str,
                       user_id: int,
                       description: str,
                       project_type: str,
                       workflow_type: int):

        is_workflow_type_id_valid = self.storage.is_valid_workflow_type_id(
            workflow_type=workflow_type
        )

        is_workflow_type_id_invalid = not is_workflow_type_id_valid

        if is_workflow_type_id_invalid:
            raise InvalidWorkflowIdException

        service_adapter = get_service_adapter()
        is_admin_valid_dto = service_adapter.validate_admin. \
            get_is_admin_valid_dto(user_id=user_id)

        is_admin = is_admin_valid_dto.is_admin

        is_not_admin = not is_admin

        if is_not_admin:
            raise InvalidAdminException

        project_details_dto = self.storage.create_project(
            name=name,
            user_id=user_id,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type
        )
        return project_details_dto
