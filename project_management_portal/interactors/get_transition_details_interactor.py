from project_management_portal.interactors.storages. \
    transition_storage_interface import TransitionStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetTransitionDetailsInteractor:
    def __init__(self,
                 storage: TransitionStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter


    def get_transition_details_between_two_states(self,
                                                  task_id: int,
                                                  to_state: int):


        is_to_state_id_valid = self.storage.is_valid_to_state_id(
            to_state=to_state
        )

        is_to_state_id_invalid = not is_to_state_id_valid

        if is_to_state_id_invalid:
            self.presenter.raise_invalid_to_state_id_exception()
            return

        is_valid_task_id = self.storage.is_valid_task_id(task_id=task_id)
        is_invalid_task_id = not is_valid_task_id

        if is_invalid_task_id:
            self.presenter.raise_invalid_task_id_exception()
            return

        list_of_checklists_dto = self.storage. \
            get_transition_details_between_two_states(task_id=task_id,
                                                      to_state=to_state)

        response = self.presenter. \
            get_transition_details_between_two_states_response(
                list_of_checklists_dto=list_of_checklists_dto)

        return response
