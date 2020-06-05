import pytest
from unittest .mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.storages. \
    transition_storage_interface import TransitionStorageInterface
from project_management_portal.interactors.create_transition_interactor \
    import CreateTransitionInteractor
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_create_transition_with_invalid_from_state_id_raises_exception():

    # Arrange
    name = "transition_1"
    description = "description_1"
    from_state = 1
    to_state = 1

    storage = create_autospec(TransitionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateTransitionInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_from_state_id.return_value = False
    presenter.raise_invalid_from_state_id_exception.side_effect = NotFound

    interactor = CreateTransitionInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_transition(
            name=name,
            description=description,
            from_state=from_state,
            to_state=to_state
        )

    # Assert
    storage.is_valid_from_state_id.assert_called_once_with(
        from_state=from_state
    )
    presenter.raise_invalid_from_state_id_exception.assert_called_once()


def test_create_transition_with_invalid_to_state_id_raises_exception():

    # Arrange
    name = "transition_1"
    description = "description_1"
    from_state = 1
    to_state = 1

    storage = create_autospec(TransitionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateTransitionInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_to_state_id.return_value = False
    presenter.raise_invalid_to_state_id_exception.side_effect = NotFound

    interactor = CreateTransitionInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_transition(
            name=name,
            description=description,
            from_state=from_state,
            to_state=to_state
        )

    # Assert
    storage.is_valid_to_state_id.assert_called_once_with(
        to_state=to_state
    )
    presenter.raise_invalid_to_state_id_exception.assert_called_once()


def test_create_transition_with_valid_details_returns_transition_details(
    transition_details_dto, create_transition_expected_output):

    # Arrange
    name = "transition_1"
    description = "description_1"
    from_state = 1
    to_state = 1

    storage = create_autospec(TransitionStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateTransitionInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_from_state_id.return_value = True
    storage.is_valid_to_state_id.return_value = True
    storage.create_transition.return_value = transition_details_dto
    presenter.get_create_transition_response. \
        return_value = create_transition_expected_output

    # Act
    response = interactor.create_transition(
        name=name,
        description=description,
        from_state=from_state,
        to_state=to_state
    )

    # Assert
    storage.create_transition.assert_called_once_with(
        name=name,
        description=description,
        from_state=from_state,
        to_state=to_state
    )

    presenter.get_create_transition_response.assert_called_once_with(
        transition_details_dto=transition_details_dto
    )

    assert response == create_transition_expected_output
