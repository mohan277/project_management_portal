from typing import List
from abc import ABC
from abc import abstractmethod
from project_management_portal.interactors.storages.dtos import (
    ListOfWorkflowsDto
)

class WorkflowStorageInterface:

    @abstractmethod
    def get_list_of_workflows(self) -> ListOfWorkflowsDto:
        pass
