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
    def is_valid_user_ids_list(self, assigned_to: List[int]) -> bool:
        pass


    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass


    @abstractmethod
    def create_project(self,
                       name: str,
                       user_id: int,
                       description: str,
                       workflow_type: int,
                       project_type: str,
                       assigned_to: List[int]) -> ProjectDto:
        pass


    @abstractmethod
    def is_valid_limit(self, limit: int) -> bool:
        pass


    @abstractmethod
    def is_valid_offset(self, offset: int) -> bool:
        pass


    @abstractmethod
    def get_list_of_admin_projects(
        self, limit: int, offset: int, user_id: int) -> ListOfProjectsDto:
        pass


    @abstractmethod
    def get_list_of_member_projects(
        self, limit: int, offset: int, user_id: int) -> ListOfProjectsDto:
        pass
