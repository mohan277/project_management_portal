import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from project_management_portal.interactors.get_to_states_interactor import \
    GetToStatesInteractor
from project_management_portal.interactors.storages. \
    state_storage_interface import StateStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.interactors.storages.dtos import \
    ListOfToStatesDto


def test_get_to_states_with_invalid_task_id_returns_exception():

    # Arrange
    task_id = 1

    storage = create_autospec(StateStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetToStatesInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_task_id.return_value = False
    presenter.raise_invalid_task_id_exception.side_effect = NotFound

    interactor = GetToStatesInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.get_to_states_based_on_current_state(task_id=task_id)

    # Assert
    storage.is_valid_task_id.assert_called_once_with(
        task_id=task_id
    )
    presenter.raise_invalid_task_id_exception.assert_called_once()


def test_get_to_states_returns_list_of_to_states(
    list_of_to_state_dtos, get_to_states_expected_output):

    # Arrange
    task_id = 1
    total_count_of_to_states = 1
    storage = create_autospec(StateStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetToStatesInteractor(
        storage=storage,
        presenter=presenter
    )

    list_of_to_states_dto = ListOfToStatesDto(
        list_of_to_state_dtos=list_of_to_state_dtos,
        total_count_of_to_states=total_count_of_to_states
    )

    storage.is_valid_task_id.return_value = True
    storage.get_to_states_based_on_current_state. \
        return_value = list_of_to_states_dto

    presenter.get_to_states_based_on_current_state_response. \
        return_value = get_to_states_expected_output

    # Act
    response = interactor.get_to_states_based_on_current_state(
        task_id=task_id
    )

    # Assert
    storage.is_valid_task_id.assert_called_once_with(
        task_id=task_id
    )

    storage.get_to_states_based_on_current_state.assert_called_once_with(
        task_id=task_id
    )

    presenter.get_to_states_based_on_current_state_response. \
        assert_called_once_with(list_of_to_states_dto=list_of_to_states_dto)

    assert response == get_to_states_expected_output
