import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from project_management_portal.interactors.get_transition_details_interactor import \
    GetTransitionDetailsInteractor
from project_management_portal.interactors.storages. \
    transition_storage_interface import TransitionStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_get_transition_details_with_invalid_task_id_returns_exception():

    # Arrange
    task_id = 1
    to_state = 1

    storage = create_autospec(TransitionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetTransitionDetailsInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_task_id.return_value = False
    presenter.raise_invalid_task_id_exception.side_effect = NotFound

    interactor = GetTransitionDetailsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.get_transition_details_between_two_states(
            task_id=task_id,
            to_state=to_state)

    # Assert
    storage.is_valid_task_id.assert_called_once_with(
        task_id=task_id
    )
    presenter.raise_invalid_task_id_exception.assert_called_once()


def test_get_transition_details_with_invalid_to_state_id_returns_exception():

    # Arrange
    task_id = 1
    to_state = 1

    storage = create_autospec(TransitionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetTransitionDetailsInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_to_state_id.return_value = False
    presenter.raise_invalid_to_state_id_exception.side_effect = NotFound

    interactor = GetTransitionDetailsInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.get_transition_details_between_two_states(
            task_id=task_id,
            to_state=to_state)

    # Assert
    storage.is_valid_to_state_id.assert_called_once_with(
        to_state=to_state
    )
    presenter.raise_invalid_to_state_id_exception.assert_called_once()


def test_get_transition_details_returns_list_of_to_checklists(
    list_of_checklists_dto, get_transition_details_expected_output):

    # Arrange
    task_id = 1
    to_state = 1

    storage = create_autospec(TransitionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetTransitionDetailsInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_task_id.return_value = True
    storage.is_valid_to_state_id.return_value = True

    storage.get_transition_details_between_two_states.return_value = list_of_checklists_dto

    presenter.get_to_states_based_on_current_state_response.return_value = get_transition_details_expected_output

    # Act
    response = interactor.get_transition_details_between_two_states(
        task_id=task_id,
        to_state=to_state
    )

    # Assert
    # assert response == get_transition_details_expected_output

    storage.is_valid_task_id.assert_called_once_with(
        task_id=task_id
    )

    storage.is_valid_to_state_id.assert_called_once_with(
        to_state=to_state
    )

    storage.get_transition_details_between_two_states.assert_called_once_with(
        task_id=task_id,
        to_state=to_state
    )

    presenter.get_transition_details_between_two_states_response. \
        assert_called_once_with(list_of_checklists_dto=list_of_checklists_dto)

