import datetime
import factory, factory.django
from django.utils import timezone
from project_management_portal.models import Checklist, State, \
    Workflow, Transition, Project, Task


# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User
#     name  = factory.Sequence(lambda n: 'user_%d' %n)
#     profile_pic = factory.Sequence(lambda n: 'profile_pic_%d' %n)
#     is_admin = factory.Faker('pybool')


class StateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = State
    name  = factory.Sequence(lambda n: 'state_%d' %n)


class ChecklistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Checklist
    name  = factory.Sequence(lambda n: 'checklist_%d' %n)
    is_mandatory = factory.Faker('pybool')


class TransitionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transition

    name  = factory.Sequence(lambda n: 'transition_%d' %n)
    description = factory.Sequence(lambda n: 'description_%d' %n)
    from_state = factory.SubFactory(StateFactory)
    to_state = factory.SubFactory(StateFactory)


    @factory.post_generation
    def checklist(self, create, extracted, **kwargs):
        if not create:
            # checklist = ChecklistFactory()
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for checklist in extracted:
                self.checklists.add(checklist)


class WorkflowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Workflow

    name  = factory.Sequence(lambda n: 'workflow_type_%d' %n)
    created_at = factory.LazyFunction(timezone.now)

    @classmethod
    def _prepare(cls, create, **kwargs):
        state = StateFactory()
        workflow = super(WorkflowFactory, cls)._prepare(create, **kwargs)
        workflow.states.add(state)

    @factory.post_generation
    def transition(self, create, extracted, **kwargs):
        if not create:
            # checklist = ChecklistFactory()
            # Simple build, do nothing.
            return
        if extracted:
            # A list of groups were passed in, use them
            for transition in extracted:
                self.transitions.add(transition)

class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: 'project_%d' %n)
    description = factory.Sequence(lambda n: 'description_%d' %n)
    workflow_type = factory.SubFactory(WorkflowFactory)
    created_at = factory.LazyFunction(timezone.now)
    project_type = factory.Iterator(['Classic Software', 'Financial', 'CRM'])
    created_by_id = 1

    # @factory.post_generation
    # def developers(self, create, extracted, **kwargs):
    #     if not create:
    #         return
    #     if extracted:
    #         for user in extracted:
    #             self.assigned_to.add(user)


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = Task

    title = factory.Sequence(lambda n: 'title_%d' %n)
    description = factory.Sequence(lambda n: 'description_%d' %n)
    issue_type = factory.Iterator(['Task', 'Bug', 'Developer story', 'User story', 'Enhancement'])
    project = factory.SubFactory(ProjectFactory)
    state = factory.SubFactory(StateFactory)
    created_by_id = 1
    created_at = factory.LazyFunction(timezone.now)
