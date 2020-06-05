import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.storages.state_storage_implementation \
    import StateStorageImplementation


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_get_to_states_based_on_current_state(
        create_task, details_of_to_states_based_on_current_state):

    # Arrange
    task_id = 1
    storage = StateStorageImplementation()

    # Act
    response = storage.get_to_states_based_on_current_state(task_id=task_id)

    # Assert
    assert response == details_of_to_states_based_on_current_state
