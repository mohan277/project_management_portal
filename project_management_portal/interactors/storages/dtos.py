from dataclasses import dataclass
from project_management_portal.constants.enums import ProjectType, IssueType
from typing import List, Optional
from datetime import datetime


@dataclass
class AccessTokenDto:
    access_token: str
    refresh_token: str
    expires_in: int
    is_admin: bool


@dataclass
class WorkflowTypeDto:
    name: str
    workflow_type_id: int


@dataclass
class UserDto:
    name: str
    user_id: str


@dataclass
class FinalUserDTO:
    name: str
    user_id: int
    is_admin: bool
    profile_pic_url: str


@dataclass
class IsAdminDTO:
    is_admin: bool


@dataclass
class ProjectDto:
    name: str
    project_id: int
    description: str
    workflow_type: str
    project_type: ProjectType
    created_by_id: int
    created_at: datetime


@dataclass
class FinalProjectDTO:
    project_details_dto: ProjectDto
    user_details_dtos: List[FinalUserDTO]


@dataclass
class ProjectDetailsDto:
    user_dto: UserDto
    project_dto: ProjectDto
    workflow_type_dto: WorkflowTypeDto


@dataclass
class ListOfProjectsDto:
    list_of_project_dtos: List[FinalProjectDTO]
    total_count_of_projects: int


@dataclass
class TaskProjectDto:
    name: str
    project_id: int

@dataclass
class StateDto:
    name: str
    state_id: int


@dataclass
class TaskDto:
    task_id: int
    title: str
    description: str
    project: int
    state: str
    issue_type: IssueType
    created_by_id: str
    created_at: datetime


@dataclass
class ListOfTasksDto:
    list_of_task_dtos: List[TaskDto]
    total_count_of_tasks: int


@dataclass
class WorkflowDto:
    name: str
    workflow_id: int


@dataclass
class ListOfWorkflowsDto:
    list_of_workflow_dtos: List[WorkflowDto]
    total_count_of_workflows: int


@dataclass
class ToStateDto:
    name: str
    to_state_id: int


@dataclass
class ListOfToStatesDto:
    list_of_to_state_dtos: List[ToStateDto]
    total_count_of_to_states: int


@dataclass
class FromStateDto:
    name: str
    from_state_id: int


@dataclass
class TransitionDto:
    name: str
    transition_id: int
    description: str
    from_state: FromStateDto
    to_state: ToStateDto


@dataclass
class ChecklistDto:
    name: str
    checklist_id: int
    is_mandatory: bool


@dataclass
class ListOfChecklistsDto:
    list_of_checklist_dtos: List[ChecklistDto]
