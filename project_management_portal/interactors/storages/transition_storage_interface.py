from abc import ABC
from abc import abstractmethod
from project_management_portal.interactors.storages.dtos import (
    TransitionDto,
    ListOfChecklistsDto
)

class TransitionStorageInterface:

    @abstractmethod
    def create_transition(self,
                    name: str,
                    description: str,
                    from_state: int,
                    to_state: str) -> TransitionDto:
        pass


    @abstractmethod
    def is_valid_from_state_id(self, from_state: int) -> bool:
        pass


    @abstractmethod
    def is_valid_to_state_id(self, to_state: int) -> bool:
        pass


    @abstractmethod
    def is_valid_task_id(self, task_id: int) -> bool:
        pass


    @abstractmethod
    def get_transition_details_between_two_states(
        self,
        task_id: int,
        to_state: int) -> ListOfChecklistsDto:
        pass
