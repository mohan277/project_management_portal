import pytest
from unittest.mock import Mock
from unittest .mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from project_management_portal.interactors.storages. \
    user_admin_login_storage_interface import LoginStorageInterface
from project_management_portal.interactors.user_admin_login_interactor \
    import LoginInteractor
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.exceptions import \
    InvalidUsernameException, InvalidPasswordException
from project_management_portal.interactors.storages.dtos import AccessTokenDto


def test_user_login_with_invalid_username():

    # Arrange
    username = "mohana"
    password = "krisna"

    storage = create_autospec(LoginStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)


    interactor = LoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    storage.validate_username.side_effect = InvalidUsernameException
    presenter.raise_invalid_username.side_effect =  NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
        )

    # Assert
    storage.validate_username.assert_called_once_with(
        username=username
    )
    presenter.raise_invalid_username.assert_called_once()


def test_user_login_with_invalid_password():

    # Arrange
    username = "mohana"
    password = "krisna"

    storage = create_autospec(LoginStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuth2SQLStorage)


    interactor = LoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    storage.validate_password.side_effect = InvalidPasswordException
    presenter.raise_invalid_password.side_effect =  NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.login(
            username=username,
            password=password
        )

    # Assert
    storage.validate_password.assert_called_once_with(
        username=username,
        password=password
    )
    presenter.raise_invalid_password.assert_called_once()
