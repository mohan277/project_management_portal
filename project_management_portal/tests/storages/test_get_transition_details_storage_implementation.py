import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.models import Transition, State
from project_management_portal.storages.transition_storage_implementation \
    import TransitionStorageImplementation


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_create_transition_with_valid_details_return_transition_details_dto(
    create_workflow, create_project, task_details_dto):

    # Arrange
    name = "transition_1"
    description = "description_1"
    from_state = 1
    to_state = 3

    storage = TransitionStorageImplementation()

    # Act
    response = storage.create_transition(name=name,
                                         description=description,
                                         from_state=from_state,
                                         to_state=to_state)

    # Assert
    # from_state_obj = State.objects.get(id=from_state)
    # to_state_obj = State.objects.get(id=to_state)
    # transition_obj = Transition.objects.get(name=name,
    #                                   description=description,
    #                                   from_state=from_state,
    #                                   to_state=to_state)

    # assert transition_obj.name == name
    # assert transition_obj.description == description
    # assert transition_obj.from_state_id == from_state
    # assert transition_obj.to_state_id == to_state
    # assert from_state_obj.id == from_state
    # assert to_state_obj.id == to_state
