from project_management_portal.interactors.storages. \
    task_storage_interface import TaskStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetTasksInteractor:
    def __init__(self,
                 storage: TaskStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter


    def get_list_of_tasks(self, project_id: int):

        is_project_id_valid = self.storage.is_valid_project_id(
            project=project_id
        )

        is_project_id_invalid = not is_project_id_valid

        if is_project_id_invalid:
            self.presenter.raise_invalid_project_id_exception()
            return

        list_of_tasks_dto = self.storage.get_list_of_tasks(
            project_id=project_id)

        response = self.presenter.get_list_of_tasks_response(
            list_of_tasks_dto=list_of_tasks_dto
        )

        return response
