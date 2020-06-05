from typing import List
from project_management_portal.exceptions import InvalidListOfUserIdsException
from project_management_portal.interactors.storages. \
    task_storage_interface import TaskStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class CreateTaskInteractor:
    def __init__(self,
                 storage: TaskStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter


    def create_task(self,
                    title: str,
                    user_id: int,
                    description: str,
                    project: int,
                    state: int,
                    issue_type: str):
        state_is_none = not state
        if state_is_none:
            state = 1

        is_project_id_valid = self.storage.is_valid_project_id(
            project=project
        )

        is_project_id_invalid = not is_project_id_valid

        if is_project_id_invalid:
            self.presenter.raise_invalid_project_id_exception()
            return

        is_state_id_valid = self.storage.is_valid_state_id(state=state)

        is_state_id_invalid = not is_state_id_valid

        if is_state_id_invalid:
            self.presenter.raise_invalid_state_id_exception()
            return

        is_user_id_valid = self.storage.is_valid_user_id(user_id=user_id)

        is_user_id_invalid = not is_user_id_valid

        if is_user_id_invalid:
            self.presenter.raise_invalid_user_id_exception()
            return


        task_details_dto = self.storage.create_task(title=title,
                                                    user_id=user_id,
                                                    description=description,
                                                    project=project,
                                                    state=state,
                                                    issue_type=issue_type)

        response = self.presenter.get_create_task_response(
            task_details_dto=task_details_dto
        )

        return response
