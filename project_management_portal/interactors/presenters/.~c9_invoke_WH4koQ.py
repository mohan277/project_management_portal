from abc import ABC
from abc import abstractmethod
from typing import List
from project_management_portal.interactors.storages.dtos import (
    ListOfProjectsDto,
    ProjectDto,
    ListOfTasksDto,
    TaskDto,
    TransitionDto,
    ListOfWorkflowsDto,
    ListOfToStatesDto,
    ListOfChecklistsDto
)


class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_username(self):
        pass

    @abstractmethod
    def raise_invalid_password(self):
        pass

    @abstractmethod
    def get_access_token(self, access_token: str):
        pass

    @abstractmethod
    def raise_invalid_workflow_type_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_admin_exception(self):
        pass

    @abstractmethod
    def get_create_project_response(
        self, final_project_details_dto: FinalProjectDTO):
        pass

    @abstractmethod
    def get_list_of_projects_response(
        self, list_of_projects_dto: ListOfProjectsDto):
        pass

    @abstractmethod
    def raise_invalid_project_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_state_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_user_id_exception(self):
        pass

    @abstractmethod
    def get_create_task_response(self,
                                    task_details_dto: TaskDto):
        pass

    @abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass

    @abstractmethod
    def get_list_of_tasks_response(self, list_of_tasks_dto: ListOfTasksDto):
        pass

    @abstractmethod
    def get_create_transition_response(self,
                                    transition_details_dto: TransitionDto):
        pass

    @abstractmethod
    def raise_invalid_from_state_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_to_state_id_exception(self):
        pass

    @abstractmethod
    def get_list_of_workflows_response(self, list_of_workflows_dto: ListOfWorkflowsDto):
        pass

    @abstractmethod
    def get_to_states_based_on_current_state_response(
        self, list_of_to_states_dto: ListOfToStatesDto):
        pass

    @abstractmethod
    def raise_invalid_task_id_exception(self):
        pass

    @abstractmethod
    def get_transition_details_between_two_states_response(
        self, list_of_checklists_dto: ListOfChecklistsDto):
        pass
