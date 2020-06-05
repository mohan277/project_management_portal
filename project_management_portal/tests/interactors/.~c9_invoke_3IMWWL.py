import datetime
from freezegun import freeze_time
import pytest
from project_management_portal.constants.enums import ProjectType, IssueType
from project_management_portal.interactors.storages.dtos import (
    UserDto,
    ProjectDto,
    WorkflowTypeDto,
    StateDto,
    TaskProjectDto,
    TaskDto,
    FromStateDto,
    ToStateDto,
    TransitionDto,
    WorkflowDto
)


######################### create_project ####################################

@pytest.fixture()
@freeze_time("2020-05-20")
def project_details_dto():
    project_details_dto = ProjectDto(
        project_id=1,
        name='project_management_portal',
        description='The name of the project is project_management_portal',
        workflow_type='workflow_type_1',
        project_type=ProjectType.CRM.value,
        created_by='user_1',
        created_at=datetime.datetime(2020, 5, 20, 0, 0)
    )
    return project_details_dto


@pytest.fixture()
@freeze_time("2020-05-20")
def create_project_expected_output():
    response = {
        "name": "project_1",
        "project_id": 1,
        "description": "description_1",
        "workflow_type": "workflow_type_1",
        "project_type": ProjectType.CRM.value,
        "created_at": datetime.datetime(2020, 5, 20, 0, 0),
        "created_by": "user_1"
    }
    return response


######################### get projects ####################################

@pytest.fixture()
@freeze_time("2020-05-20")
def get_projects_expected_output():
    get_projects_expected_output = {
        "projects": [
            {
                "name": "project_1",
                "project_id": 1,
                "description": "description_1",
                "workflow_type": "workflow_type_1",
                "project_type": ProjectType.CRM.value,
                "created_at": datetime.datetime(2020, 5, 20, 0, 0),
                "created_by": "user_1"
            }
        ],
        "total_count_of_projects": 1
    }
    return get_projects_expected_output

######################### create task ####################################


@pytest.fixture()
@freeze_time("2020-05-20")
def task_details_dto():
    task_details_dto = TaskDto(
        title="title_1",
        task_id=1,
        description="description_1",
        project="project_1",
        state="state_1",
        issue_type=IssueType.BUG.value,
        created_at=datetime.datetime(2020, 5, 20, 0, 0),
        created_by="user_1"
    )
    return task_details_dto

@pytest.fixture()
@freeze_time("2020-05-20")
def task_details_dto():
    task_details_dto = TaskDto(
        title="title_1",
        task_id=1,
        description="description_1",
        project="project_1",
        state="state_1",
        issue_type=IssueType.BUG.value,
        created_at=datetime.datetime(2020, 5, 20, 0, 0),
        created_by="user_1"
    )
    return task_details_dto

@pytest.fixture()
@freeze_time("2020-05-20")
def create_task_expected_output():
    response = {
        "title": "title_1",
        "task_id": 1,
        "description": "description_1",
def list_of_task__dtos():
        "state": "state_1",
        "issue_type": IssueType.BUG.value,
        "created_at": datetime.datetime(2020, 5, 20, 0, 0),
        "created_by": "user_1",
        "user_id": 1
    }
    return response


######################### get tasks ####################################

@pytest.fixture()
def get_tasks_expected_output():
    get_tasks_expected_output = [
        {
            "title": "title_1",
            "description": "description_1",
            "project": {
                "name": "project_1",
                "project_id": 1
            },
            "state": {
                "name": "state_1",
                "user_id": 1
            }
        }
    ]
    return get_tasks_expected_output


######################### create transition ####################################

@pytest.fixture()
def from_state_dto():
    from_state_dto = FromStateDto(
        name="state_1",
        from_state_id=1
    )
    return from_state_dto


@pytest.fixture()
def to_state_dto():
    to_state_dto = ToStateDto(
        name="state_1",
        to_state_id=1
    )
    return to_state_dto


@pytest.fixture()
def transition_details_dto(from_state_dto, to_state_dto):
    transition_details_dto = TransitionDto(
        name="transition_1",
        transition_id=1,
        description="description_1",
        from_state=from_state_dto,
        to_state=to_state_dto
    )
    return transition_details_dto


@pytest.fixture()
def create_transition_expected_output():
    response = {
        "name": "transition_1",
        "transition_id": 1,
        "description": "description_1",
        "from_state": {
            "name": "state_1",
            "from_state_id": 1
        },
        "to_state": {
            "name": "state_1",
            "to_state_id": 1
        }
    }
    return response


###################### get workflows ######################

@pytest.fixture()
def list_of_workflow_dtos():
    list_of_workflow_dtos = [
        WorkflowDto(
            name='workflow_1',
            workflow_id=1
        )
    ]
    return list_of_workflow_dtos


@pytest.fixture()
def get_workflows_expected_output():
    get_workflows_expected_output = {
        "workflows": [
            {
                "name": "workflow_1",
                "workflow_id": 1
            }
        ],
        "total_count_of_workflows": 1
    }
    return get_workflows_expected_output


###################### get to_states ######################

@pytest.fixture()
def list_of_to_state_dtos():
    list_of_to_state_dtos = [
        ToStateDto(
            name='state_1',
            to_state_id=1
        )
    ]
    return list_of_to_state_dtos


@pytest.fixture()
@freeze_time("2020-05-20")
def get_to_states_expected_output():
    get_to_states_expected_output = {
        "to_states": [
            {
                "name": "state_1",
                "to_state_id": 1
            }
        ],
        "total_count_of_to_states": 1
    }
    return get_to_states_expected_output
