from project_management_portal.interactors.storages. \
    transition_storage_interface import TransitionStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class CreateTransitionInteractor:
    def __init__(self,
                 storage: TransitionStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter


    def create_transition(self,
                    name: str,
                    description: str,
                    from_state: int,
                    to_state: int):

        is_from_state_id_valid = self.storage.is_valid_from_state_id(
            from_state=from_state
        )

        is_from_state_id_invalid = not is_from_state_id_valid

        if is_from_state_id_invalid:
            self.presenter.raise_invalid_from_state_id_exception()
            return

        is_to_state_id_valid = self.storage.is_valid_to_state_id(
            to_state=to_state
        )

        is_to_state_id_invalid = not is_to_state_id_valid

        if is_to_state_id_invalid:
            self.presenter.raise_invalid_to_state_id_exception()
            return

        transition_details_dto = self.storage.create_transition(
            name=name,
            description=description,
            from_state=from_state,
            to_state=to_state)

        response = self.presenter.get_create_transition_response(
            transition_details_dto=transition_details_dto
        )
        return response
