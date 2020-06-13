from project_management_portal.models import (
    User,
    Task,
    State,
    Project,
    Workflow,
    Checklist,
    Transition,
)



# # Create users with roles
# # Assigning users to projects
# # Create Workflows, States, Transitions, Checklists in transitions
# p


# # user
def create_users():

    users = [
        {
            'username': 'Ganesh',
            "name": "ganesh",
            "is_admin": True,
            "profile_pic": "profile_pic_1",
            "password": "ganesh"
        },
        {
            'username': 'mohan',
            "name": "mohan",
            "is_admin": False,
            "profile_pic": "profile_pic_2",
            "password": "mohan"
        },
        {
            'username': 'krishna',
            "name": "krishna",
            "is_admin": False,
            "profile_pic": "profile_pic_3",
            "password": "krishna"
        }
    ]

    for user in users:
        user_obj = User.objects.create(
            name=user['name'],
            is_admin=user['is_admin'],
            username=user['username'],
            profile_pic=user['profile_pic'])

        user_obj.set_password(user['password'])
        user_obj.save()



# # state
def create_states():

    states = [
        {
            "name": "TODO"
        },
        {
            "name": "Planning ELP"
        },
        {
            "name": "In Progress"
        },
        {
            "name": "Testing Completed"
        },
        {
            "name": "Self review Completed"
        },
        {
            "name": "To be reviewed"
        },
        {
            "name": "Completed"
        }
    ]

    for state in states:
        State.objects.create(name=state['name'])



# checklist
def create_checklists():

    checklists = [
        {
            "name": "I have followed all the objectives in this task by following ELP.",
            "is_mandatory": True
        },
        {
            "name": "I have maintained the clean code practices.",
            "is_mandatory": True
        },
        {
            "name": "I have completed the objectives as per the state.",
            "is_mandatory": True
        },
        {
            "name": "I agree above transition changes are done by me.",
            "is_mandatory": False
        }
    ]

    for checklist in checklists:
        Checklist.objects.create(name=checklist['name'],
                                 is_mandatory=checklist['is_mandatory'])




# transition
def create_transitions():

    checklist_obj_1 = Checklist.objects.get(id=1)
    checklist_obj_2 = Checklist.objects.get(id=2)
    checklist_obj_3 = Checklist.objects.get(id=3)
    checklist_obj_4 = Checklist.objects.get(id=4)

    list_of_checklist_objs = [
        checklist_obj_1,
        checklist_obj_2,
        checklist_obj_3,
        checklist_obj_4
    ]

    transitions = [
        {
            "name": "transition_1",
            "description": "description_1",
            "from_state": 1,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_2",
            "description": "description_2",
            "from_state": 6,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 1,
            "to_state": 4,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 4,
            "to_state": 5,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 5,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 6,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 1,
            "to_state": 2,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 2,
            "to_state": 3,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_2",
            "description": "description_2",
            "from_state": 3,
            "to_state": 6,
            "checklist": list_of_checklist_objs
        },
        {
            "name": "transition_3",
            "description": "description_3",
            "from_state": 6,
            "to_state": 7,
            "checklist": list_of_checklist_objs
        }
    ]

    for transition in transitions:
        transition_obj = Transition.objects.create(
            name=transition['name'],
            description=transition['description'],
            from_state_id=transition['from_state'],
            to_state_id=transition['to_state']
        )

        transition_obj.checklist.set(transition['checklist'])


# # workflow
def create_workflows():
    state_obj_1 = State.objects.get(id=1)
    state_obj_2 = State.objects.get(id=2)
    state_obj_3 = State.objects.get(id=3)
    state_obj_4 = State.objects.get(id=4)
    state_obj_5 = State.objects.get(id=5)
    state_obj_6 = State.objects.get(id=6)
    state_obj_7 = State.objects.get(id=7)
    transition_obj_1 = Transition.objects.get(id=1)
    transition_obj_2 = Transition.objects.get(id=2)
    transition_obj_3 = Transition.objects.get(id=3)
    transition_obj_4 = Transition.objects.get(id=4)
    transition_obj_5 = Transition.objects.get(id=5)
    transition_obj_6 = Transition.objects.get(id=6)
    transition_obj_7 = Transition.objects.get(id=7)
    transition_obj_8 = Transition.objects.get(id=8)
    transition_obj_9 = Transition.objects.get(id=9)
    transition_obj_10 = Transition.objects.get(id=10)


    workflows = [
        {
            "name": "Agile",
            "states": [state_obj_1, state_obj_6, state_obj_7],
            "transitions": [transition_obj_1, transition_obj_2]
        },
        {
            "name" : "Adhoc",
            "states": [state_obj_1, state_obj_4, state_obj_5, state_obj_6, state_obj_7],
            "transitions": [transition_obj_3, transition_obj_4, transition_obj_5, transition_obj_6]
        },
        {
            "name" : "PMP",
            "states": [state_obj_1, state_obj_2, state_obj_3, state_obj_6, state_obj_7],
            "transitions": [transition_obj_7, transition_obj_8, transition_obj_9, transition_obj_10]
        }
    ]

    for workflow in workflows:

        workflow_obj = Workflow.objects.create(
            name=workflow['name']
        )

        workflow_obj.states.set(workflow['states'])
        workflow_obj.transitions.set(workflow['transitions'])



# # project
def create_projects():

    projects = [
        {
            "name": "Covid 19 Dashboard",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 1,
            "project_type": "CRM",
            "assigned_to": [2]
        },
        {
            "name": "Project Management Platform (PMP)",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 1,
            "project_type": "Classic Software",
            "assigned_to": [2]
        },
        {
            "name": "Content Management Portal",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 1,
            "project_type": "Financial",
            "assigned_to": [2]
        },
        {
            "name": "Resource Management Dashboard",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 1,
            "project_type": "Financial",
            "assigned_to": [2]
        },
        {
            "name": "Let's Ride",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 2,
            "project_type": "Classic Software",
            "assigned_to": [2]
        },
        {
            "name": "Slot Booking",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 2,
            "project_type": "Financial",
            "assigned_to": [2]
        },
        {
            "name": "Smart Food Management",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 2,
            "project_type":  "CRM",
            "assigned_to": [3]
        },
        {
            "name": "Reporting Portal",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 2,
            "project_type": "Classic Software",
            "assigned_to": [3]
        },
        {
            "name": "Formaster",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 3,
            "project_type": "Financial",
            "assigned_to": [3]
        },
        {
            "name": "Gyaan",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 3,
            "project_type": "Classic Software",
            "assigned_to": [3]
        },
        {
            "name": "Essentials Kit Management",
            "created_by_id": 1,
            "description": "This is the project description",
            "workflow_type_id": 3,
            "project_type":  "CRM",
            "assigned_to": [3]
        }
    ]

    for project in projects:
        project_obj = Project.objects.create(
            name=project['name'],
            created_by_id=project['created_by_id'],
            description=project['description'],
            workflow_type_id=project['workflow_type_id'],
            project_type=project['project_type'],
            assigned_to =project['assigned_to']
        )


# task
def create_tasks():

    tasks = [
        {
            "title": "task_1",
            "description": "This is the project description",
            "project_id": 1,
            "issue_type": "Bug",
            "state_id": ""
        },
        {
            "title": "task_1",
            "description": "This is the project description",
            "project_id": 1,
            "issue_type": "Task",
            "state_id": ""
        },
        {
            "title": "task_1",
            "description": "This is the project description",
            "project_id": 2,
            "issue_type": "Developer story",
            "state_id": ""
        },
        {
            "title": "task_1",
            "description": "This is the project description",
            "project_id": 2,
            "issue_type": "User story",
            "state_id": ""
        },
        {
            "title": "task_1",
            "description": "This is the project description",
            "project_id": 3,
            "issue_type": "Enhancement",
            "state_id": ""
        }
    ]

    for task in tasks:
        task_obj = Task.objects.create(
            title=task['title'],
            description=task['description'],
            project_id=task['project_id'],
            issue_type=task['issue_type'],
            state_id=task['state_id'],
        )
