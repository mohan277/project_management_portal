import pytest
from unittest.mock import Mock
from unittest .mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.storages. \
    user_admin_login_storage_interface import LoginStorageInterface
from project_management_portal.interactors.user_admin_login_interactor \
    import LoginInteractor
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_user_admin_login_with_invalid_username():

    # Arrange
    username = "mohana"
    password = "krisna"

    storage = create_autospec(LoginStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = Mock()


    interactor = LoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    storage.validation_of_username.side_effect = NotFound
    presenter.raise_invalid_username.side_effect =  NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
        )

    # Assert
    storage.validation_of_username.assert_called_once_with(
        username=username
    )
    presenter.raise_invalid_username.assert_called_once_with(
        username=username
    )


def test_user_admin_login_with_invalid_password():

    # Arrange
    username = "mohana"
    password = "krisna"

    storage = create_autospec(LoginStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = Mock()


    interactor = LoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    storage.validation_of_password.side_effect = NotFound
    presenter.raise_invalid_password.side_effect =  NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
        )

    # Assert
    storage.validation_of_password.assert_called_once_with(
        username=username,
        password=password
    )
    presenter.raise_invalid_password.assert_called_once_with(
        username=username,
        password=password
    )


def test_user_admin_login_with_valid_username_and_password():

    # Arrange
    username = "mohana"
    password = "krisna"
    mock_presenter_response = {"access_token": "mohanakrishna"}

    storage = create_autospec(LoginStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = Mock()


    interactor = LoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    presenter.get_access_token.return_value = mock_presenter_response

    # Act
    response = interactor.login(
        username=username,
        password=password
    )

    # Assert
    assert response == mock_presenter_response
