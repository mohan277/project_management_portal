import pytest
from freezegun import freeze_time
from project_management_portal.models import (
    User,
    Project,
    State,
    Transition,
    Workflow
)


@pytest.fixture
def create_users():
    user_objs = User.objects.bulk_create([
        User(username='mohana', name='user_1', is_admin=True, profile_pic='profile_pic_1'),
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
def create_transition():
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

    workflow_obj_1 = Workflow.objects.create(name='workflow_1')
    workflow_obj_2 = Workflow.objects.create(name='workflow_2')
    workflow_obj_3 = Workflow.objects.create(name='workflow_3')

    workflow_obj_1.add(state_obj_1)
    workflow_obj_2.add(state_obj_2)
    workflow_obj_3.add(state_obj_3)

    workflow_obj_1.add(transition_obj_1)
    workflow_obj_2.add(transition_obj_2)
    workflow_obj_3.add(transition_obj_3)

    workflow_objs = [workflow_obj_1, workflow_obj_2, workflow_obj_3]

    return workflow_objs





@pytest.fixture
@freeze_time("2020-05-20")
def create_project(create_users):
    project_objs = Project.objects.bulk_create(
        [
            Project(name='project_1',
                    user_id=1,
                    description='description_1',
                    workflow_type_id=1,
                    project_type='CRM'
                ),
            Project(name='project_2',
                    user_id=1,
                    description='description_2',
                    workflow_type_id=2, project_type='Financial'
                )
            ]
        )
    return project_objs





























            # project_type=ProjectType.FINANCIAL.value,