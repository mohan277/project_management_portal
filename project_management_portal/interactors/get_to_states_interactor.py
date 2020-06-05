from project_management_portal.interactors.storages. \
    state_storage_interface import StateStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetToStatesInteractor:
    def __init__(self,
                 storage: StateStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter


    def get_to_states_based_on_current_state(self, task_id: int):

        is_valid_task_id = self.storage.is_valid_task_id(task_id=task_id)
        is_invalid_task_id = not is_valid_task_id

        if is_invalid_task_id:
            self.presenter.raise_invalid_task_id_exception()
            return

        list_of_to_states_dto = self.storage. \
            get_to_states_based_on_current_state(task_id=task_id)

        response = self.presenter. \
        get_to_states_based_on_current_state_response(
            list_of_to_states_dto=list_of_to_states_dto)

        return response
