from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetProjectsInteractor:
    def __init__(self,
                 storage: ProjectStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter


    def get_list_of_projects(self, limit: int, offset: int, user_id: int):

        is_admin = self.storage.is_admin(user_id=user_id)

        is_limit_value_valid = self.storage.is_valid_limit(limit=limit)

        is_limit_value_invalid = not is_limit_value_valid

        if is_limit_value_invalid:
            self.presenter.raise_invalid_limit_value_exception()
            return

        is_offset_value_valid = self.storage.is_valid_offset(offset=offset)

        is_offset_value_invalid = not is_offset_value_valid

        if is_offset_value_invalid:
            self.presenter.raise_invalid_offset_value_exception()
            return

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

        response = self.presenter.get_list_of_projects_response(
            list_of_projects_dto=list_of_projects_dto
        )

        return response
