import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.constants.enums import ProjectType, IssueType
from project_management_portal.interactors.storages.dtos import (
    ProjectDto,
    WorkflowTypeDto,
    ListOfProjectsDto,
    WorkflowDto,
    ListOfWorkflowsDto,
    TaskDto,
    ListOfTasksDto,
    FinalUserDTO,
    FinalProjectDTO
)


###################create project ####################
@pytest.fixture()
@freeze_time("2020-05-20")
def user_details_dtos():
    user_details_dtos = [
        FinalUserDTO(
            name='user1',
            user_id=1,
            is_admin=True,
            profile_pic_url='profile_pic_url1'
        ),
        FinalUserDTO(
            name='user2',
            user_id=2,
            is_admin=False,
            profile_pic_url='profile_pic_url2'
        )
    ]
    return user_details_dtos


@pytest.fixture()
@freeze_time("2020-05-20")
def project_details_dto():
    project_details_dto = ProjectDto(
        project_id=1,
        name='project_1',
        description='description_1',
        workflow_type='workflow_type_1',
        project_type=ProjectType.CRM.value,
        created_by_id=1,
        created_at=datetime.datetime(2020, 5, 20, 0, 0)
    )
    return project_details_dto


@pytest.fixture()
@freeze_time("2020-05-20")
def final_project_details_dto(project_details_dto, user_details_dtos):
    final_project_details_dto = FinalProjectDTO(
        user_details_dtos=user_details_dtos,
        project_details_dto=project_details_dto
    )
    return final_project_details_dto



@pytest.fixture()
def create_project_expected_output_response():
    create_project_expected_output_response = {
        "name": "project_1",
        "project_id": 1,
        "description": "description_1",
        "workflow_type": "workflow_type_1",
        "project_type": "CRM",
        "created_by_id": 1,
        "created_at": '2020-05-20 00:00:00',
        "developers": [
            {
                "name": 'user1',
                "user_id": 1,
                "is_admin": True,
                "profile_pic_url": 'profile_pic_url1'
            },
            {
                "name": 'user2',
                "user_id": 2,
                "is_admin": False,
                "profile_pic_url": 'profile_pic_url2'
            }
        ]
    }
    return create_project_expected_output_response

##################### get list of projects ########################

@pytest.fixture()
@freeze_time("2020-05-20")
def list_of_project_dtos():
    list_of_project_dtos = [
        ProjectDto(
            project_id=1,
            name='project_1',
            description='description_1',
            workflow_type='workflow_type_1',
            project_type=ProjectType.CRM.value,
            created_by_id=1,
            created_at=datetime.datetime(2020, 5, 20, 0, 0)
        )
    ]
    return list_of_project_dtos


@pytest.fixture()
def get_admin_projects_expected_output_response():
    get_projects_expected_output = {
        "projects": [
            {
                "name": "project_1",
                "project_id": 1,
                "description": "description_1",
                "workflow_type": "workflow_type_1",
                "project_type": ProjectType.CRM.value,
                "created_at": '2020-05-20 00:00:00',
                "created_by_id": 1
            }
        ],
        "total_count_of_projects": 1
    }
    return get_projects_expected_output


@pytest.fixture()
def list_of_projects_dto(list_of_project_dtos):
    list_of_projects_dto = ListOfProjectsDto(
        list_of_project_dtos=list_of_project_dtos,
        total_count_of_projects=1
    )

    return list_of_projects_dto


################### create task ####################


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
        created_by_id=1
    )
    return task_details_dto


@pytest.fixture()
def create_task_expected_output():
    response = {
        "title": "title_1",
        "task_id": 1,
        "description": "description_1",
        "project": "project_1",
        "state": "state_1",
        "issue_type": IssueType.BUG.value,
        "created_at": '2020-05-20 00:00:00',
        "created_by_id": 1
    }
    return response


##################### get list of tasks ########################


@pytest.fixture()
@freeze_time("2020-05-20")
def list_of_task_dtos():
    list_of_task_dtos = [
        TaskDto(
            title="title_1",
            task_id=1,
            description="description_1",
            project="project_1",
            state="state_1",
            issue_type=IssueType.BUG.value,
            created_at=datetime.datetime(2020, 5, 20, 0, 0),
            created_by_id=1
        )
    ]
    return list_of_task_dtos


@pytest.fixture()
def get_tasks_expected_output():
    response = {
        "tasks": [
            {
                "title": "title_1",
                "task_id": 1,
                "description": "description_1",
                "project": "project_1",
                "state": "state_1",
                "issue_type": IssueType.BUG.value,
                "created_at": '2020-05-20 00:00:00',
                "created_by_id": 1
            }
        ],
        "total_count_of_tasks": 1
    }

    return response


@pytest.fixture()
def list_of_tasks_dto(list_of_task_dtos):
    list_of_tasks_dto = ListOfTasksDto(
        list_of_task_dtos=list_of_task_dtos,
        total_count_of_tasks=1
    )

    return list_of_tasks_dto


##################### get list of workflows ########################



@pytest.fixture()
def list_of_workflow_dtos():
    list_of_workflow_dtos = [
        WorkflowDto(
            name='workflow_type_1',
            workflow_id=1
        ),
        WorkflowDto(
            name='workflow_type_2',
            workflow_id=2
        ),
        WorkflowDto(
            name='workflow_type_3',
            workflow_id=3
        )
    ]
    return list_of_workflow_dtos


@pytest.fixture()
def list_of_workflows_dto(list_of_workflow_dtos):
    response = ListOfWorkflowsDto(
        list_of_workflow_dtos=list_of_workflow_dtos,
        total_count_of_workflows=3
    )
    return response


@pytest.fixture()
def get_workflows_expected_output_response():
    get_workflows_expected_output = {
        "workflows": [
            {
                "name": "workflow_type_1",
                "workflow_id": 1,
            },
            {
                "name": "workflow_type_2",
                "workflow_id": 2,
            },
            {
                "name": "workflow_type_3",
                "workflow_id": 3,
            }
        ],
        "total_count_of_workflows": 3
    }
    return get_workflows_expected_output
