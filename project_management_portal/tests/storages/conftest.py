import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.constants.enums import ProjectType, IssueType
from project_management_portal.interactors.storages.dtos import (
    ProjectDto,
    UserDto,
    WorkflowTypeDto,
    ListOfProjectsDto,
    TaskDto,
    StateDto,
    TaskProjectDto,
    WorkflowDto,
    ListOfWorkflowsDto,
    ToStateDto,
    ListOfToStatesDto,
    ListOfTasksDto
)
from project_management_portal.models import (
    User,
    Project,
    State,
    Transition,
    Workflow,
    Task
)


@pytest.fixture
def create_users():
    user_objs = User.objects.bulk_create([
        User(username='mohan', name='user_1', is_admin=True, profile_pic='profile_pic_1'),
        User(username='krishna', name='user_2', is_admin=False, profile_pic='profile_pic_2')
    ])
    return user_objs


@pytest.fixture
@freeze_time("2020-05-20")
def create_state():
    state_objs = State.objects.bulk_create([
        State(name='TODO'),
        State(name='In Progress'),
        State(name='To be reviewed')
    ])
    return state_objs


@pytest.fixture
@freeze_time("2020-05-20")
def create_transition(create_state):
    state_obj_1 = State.objects.get(id=1)
    state_obj_2 = State.objects.get(id=2)
    state_obj_3 = State.objects.get(id=3)
    transition_objs = Transition.objects.bulk_create([
        Transition(name='transition_1',
                   description='description_1',
                   from_state=state_obj_1,
                   to_state=state_obj_2
        ),
        Transition(name='transition_2',
                   description='description_2',
                   from_state=state_obj_1,
                   to_state=state_obj_3
        ),
        Transition(name='transition_3',
                   description='description_3',
                   from_state=state_obj_2,
                   to_state=state_obj_3
        )
    ])
    return transition_objs


@pytest.fixture
@freeze_time("2020-05-20")
def create_workflow(create_state, create_transition):
    state_obj_1 = State.objects.get(id=1)
    state_obj_2 = State.objects.get(id=2)
    state_obj_3 = State.objects.get(id=3)

    transition_obj_1 = Transition.objects.get(id=1)
    transition_obj_2 = Transition.objects.get(id=2)
    transition_obj_3 = Transition.objects.get(id=3)

    workflow_obj_1 = Workflow.objects.create(name='workflow_type_1')
    workflow_obj_2 = Workflow.objects.create(name='workflow_type_2')
    workflow_obj_3 = Workflow.objects.create(name='workflow_type_3')

    workflow_obj_1.states.add(state_obj_1)
    workflow_obj_2.states.add(state_obj_2)
    workflow_obj_3.states.add(state_obj_3)

    workflow_obj_1.transitions.add(transition_obj_1)
    workflow_obj_2.transitions.add(transition_obj_2)
    workflow_obj_3.transitions.add(transition_obj_3)

    workflow_objs = [workflow_obj_1, workflow_obj_2, workflow_obj_3]

    return workflow_objs


@pytest.fixture
@freeze_time("2020-05-20")
def create_project(create_users, create_workflow):

    user_obj = User.objects.get(id=2)

    project_objs = Project.objects.bulk_create(
        [
            Project(id=1,
                    name='project_1',
                    created_by_id=1,
                    description='description_1',
                    workflow_type_id=1,
                    project_type='CRM'
                ),
            Project(id=2,
                    name='project_2',
                    created_by_id=1,
                    description='description_2',
                    workflow_type_id=1,
                    project_type='Financial'
                )
            ]
        )
    project_obj_1 = project_objs[0]
    project_obj_1.assigned_to.add(user_obj)
    return project_objs


@pytest.fixture()
@freeze_time("2020-05-20")
def create_task(create_state, create_project):

    task_objs = Task.objects.bulk_create([
        Task(title="title_1",
             description="description_1",
             project_id=1,
             issue_type="Task",
             created_by_id=1,
             state_id=1
        ),
        Task(title="title_2",
             description="description_2",
             project_id=2,
             issue_type="Bug",
             created_by_id=1,
             state_id=2
        ),
        Task(title="title_3",
             description="description_3",
             project_id=2,
             issue_type="Enhancement",
             created_by_id=1,
             state_id=3
        )
    ])
    return task_objs




######################### create project ######################

@pytest.fixture()
@freeze_time("2020-05-20")
def project_details_dto():
    project_details_dto = ProjectDto(
        project_id=3,
        name='project_management_portal',
        description='The name of the project is project_management_portal',
        workflow_type='workflow_type_1',
        project_type=ProjectType.CRM.value,
        created_by='mohan',
        created_at=datetime.datetime(2020, 5, 20, 0, 0)
    )
    return project_details_dto


######################### get projects ######################

@pytest.fixture()
@freeze_time("2020-05-20")
def list_of_admin_projects_dtos():
    list_of_project_dtos = [
        ProjectDto(
            name='project_1',
            project_id=1,
            description='description_1',
            workflow_type='workflow_type_1',
            project_type='CRM',
            created_by='mohan',
            created_at=datetime.datetime(2020, 5, 20, 0, 0)
        ),
        ProjectDto(
            name='project_2',
            project_id=2,
            description='description_2',
            workflow_type='workflow_type_1',
            project_type='Financial',
            created_by='mohan',
            created_at=datetime.datetime(2020, 5, 20, 0, 0)
        )
    ]
    return list_of_project_dtos


@pytest.fixture()
@freeze_time("2020-05-20")
def get_admin_projects_expected_output(list_of_admin_projects_dtos):
    response = ListOfProjectsDto(
        list_of_project_dtos=list_of_admin_projects_dtos,
        total_count_of_projects=2
    )
    return response


@pytest.fixture()
@freeze_time("2020-05-20")
def list_of_member_projects_dtos():
    list_of_project_dtos = [
        ProjectDto(
            name='project_1',
            project_id=1,
            description='description_1',
            workflow_type='workflow_type_1',
            project_type='CRM',
            created_by='mohan',
            created_at=datetime.datetime(2020, 5, 20, 0, 0)
        )
    ]
    return list_of_project_dtos

@pytest.fixture()
@freeze_time("2020-05-20")
def get_member_projects_expected_output(list_of_member_projects_dtos):
    response = ListOfProjectsDto(
        list_of_project_dtos=list_of_member_projects_dtos,
        total_count_of_projects=1
    )
    return response

######################### create task ######################

@pytest.fixture()
@freeze_time("2020-05-20")
def task_details_dto():
    task_details_dto = TaskDto(
        task_id=1,
        title="title_1",
        description="description_1",
        project="project_1",
        state="In Progress",
        created_by="mohan",
        created_at=datetime.datetime(2020, 5, 20, 0, 0),
        issue_type="Bug"
)
    return task_details_dto


######################### get tasks ######################


@pytest.fixture()
@freeze_time("2020-05-20")
def list_of_task_dtos():
    list_of_task_dtos = [
        TaskDto(
            title="title_1",
            task_id=1,
            description="description_1",
            project="project_1",
            state="TODO",
            issue_type=IssueType.TASK.value,
            created_by='mohan',
            created_at=datetime.datetime(2020, 5, 20, 0, 0)
        )
    ]
    return list_of_task_dtos


@pytest.fixture()
@freeze_time("2020-05-20")
def get_tasks_expected_output(list_of_task_dtos):
    response = ListOfTasksDto(
        list_of_task_dtos=list_of_task_dtos,
        total_count_of_tasks=1
    )
    return response


@pytest.fixture()
@freeze_time("2020-05-20")
def no_tasks_expected_output():
    response = ListOfTasksDto(
        list_of_task_dtos=[],
        total_count_of_tasks=0
    )
    return response


######################### get workflows ######################

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
def get_workflows_expected_output(list_of_workflow_dtos):
    response = ListOfWorkflowsDto(
        list_of_workflow_dtos=list_of_workflow_dtos,
        total_count_of_workflows=3
    )
    return response


@pytest.fixture()
@freeze_time("2020-05-20")
def no_workflows_expected_output():
    response = ListOfWorkflowsDto(
        list_of_workflow_dtos=[],
        total_count_of_workflows=0
    )
    return response


#################### get to states based on current  state ###############


@pytest.fixture()
def list_of_to_state_dtos():
    list_of_to_state_dtos = [
        ToStateDto(
            name="In Progress",
            to_state_id=2
        )
    ]
    return list_of_to_state_dtos


@pytest.fixture()
def details_of_to_states_based_on_current_state(list_of_to_state_dtos):
    details_of_to_states_based_on_current_state = ListOfToStatesDto(
        list_of_to_state_dtos=list_of_to_state_dtos,
        total_count_of_to_states=1
        )
    return details_of_to_states_based_on_current_state


