from typing import List
from project_management_portal.exceptions import InvalidListOfUserIdsException
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class CreateProjectInteractor:
    def __init__(self,
                 storage: ProjectStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter

    def create_project(self,
                       name: str,
                       user_id: int,
                       description: str,
                       workflow_type: int,
                       project_type: str,
                       assigned_to: List[int]):


        is_workflow_type_id_valid = self.storage.is_valid_workflow_type_id(
            workflow_type=workflow_type
        )

        is_workflow_type_id_invalid = not is_workflow_type_id_valid

        if is_workflow_type_id_invalid:
            self.presenter.raise_invalid_workflow_type_id_exception()
            return

        is_valid_user_ids_list = self.storage.is_valid_user_ids_list(
            assigned_to=assigned_to)

        is_invalid_user_ids_list = not is_valid_user_ids_list

        if is_invalid_user_ids_list:
            self.presenter.raise_invalid_list_of_user_ids_exception()
            return

        is_admin = self.storage.is_admin(user_id=user_id)

        is_not_admin = not is_admin

        if is_not_admin:
            self.presenter.raise_invalid_admin_exception()
            return


        project_details_dto = self.storage.create_project(
            name=name,
            user_id=user_id,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type,
            assigned_to=assigned_to
        )

        response = self.presenter.get_create_project_response(
            project_details_dto=project_details_dto
        )

        return response
