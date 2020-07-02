from typing import List
from abc import ABC
from abc import abstractmethod
from project_management_portal.interactors.storages.dtos import (
    ListOfProjectsDto,
    ProjectDto
)


class ProjectStorageInterface:

    @abstractmethod
    def is_valid_workflow_type_id(self, workflow_type: int) -> bool:
        pass

    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def create_project(self,
                       name: str,
                       user_id: int,
                       description: str,
                       project_type: str,
                       workflow_type: int,
                       developers: List[int]) -> ProjectDto:
        pass

    @abstractmethod
    def get_user_ids(self, project_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_list_of_admin_projects(
        self, limit: int, offset: int, user_id: int) -> ListOfProjectsDto:
        pass

    @abstractmethod
    def get_list_of_member_projects(
        self, limit: int, offset: int, user_id: int) -> ListOfProjectsDto:
        pass
