from typing import List
from abc import ABC
from abc import abstractmethod
from project_management_portal.interactors.storages.dtos import \
    ListOfToStatesDto

class StateStorageInterface:

    @abstractmethod
    def get_to_states_based_on_current_state(self, task_id: int) -> \
        ListOfToStatesDto:
        pass


    @abstractmethod
    def is_valid_task_id(self, task_id: int) -> bool:
        pass

