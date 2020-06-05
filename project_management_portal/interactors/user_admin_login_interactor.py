from project_management_portal.interactors.storages. \
    user_admin_login_storage_interface import LoginStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from project_management_portal.exceptions import \
    InvalidUsernameException, InvalidPasswordException


class LoginInteractor:
    def __init__(self,
                 storage: LoginStorageInterface,
                 presenter: PresenterInterface,
                 oauth2_storage: OAuth2SQLStorage):

            self.storage = storage
            self.presenter = presenter
            self.oauth2_storage = oauth2_storage

    def login(self, username: str, password: str):

        try:
            user_id = self.storage.validate_username(username=username)
        except InvalidUsernameException:
            return self.presenter.raise_invalid_username()

        try:
            self.storage.validate_password(username=username,
                                           password=password)
        except InvalidPasswordException:
            self.presenter.raise_invalid_password()

        is_admin = self.storage.is_admin(username=username)

        service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
        )

        token_storage_dto = service.create_user_auth_tokens(user_id=user_id)

        response = self.presenter.get_access_token(
            is_admin=is_admin, access_token=token_storage_dto.access_token)

        return response
