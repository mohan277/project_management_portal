from abc import ABC
from abc import abstractmethod
from typing import List
from project_management_portal.interactors.storages.dtos import (
    ListOfProjectsDto,
    ProjectDto,
    ListOfTasksDto,
    TaskDto
)


class TaskStorageInterface:

    @abstractmethod
    def create_task(self,
                    title: str,
                    user_id: int,
                    description: str,
                    project: int,
                    state: int,
                    issue_type: str) -> TaskDto:
        pass


    @abstractmethod
    def get_list_of_tasks(self, project_id: int) -> ListOfTasksDto:
        pass


    @abstractmethod
    def is_valid_project_id(self, project: int) -> bool:
        pass


    @abstractmethod
    def is_valid_state_id(self, state: int) -> bool:
        pass


    @abstractmethod
    def is_valid_user_id(self, user_id: int) -> bool:
        pass
