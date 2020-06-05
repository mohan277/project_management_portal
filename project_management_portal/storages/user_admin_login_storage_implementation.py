from project_management_portal.models import User
from project_management_portal.interactors.storages. \
    user_admin_login_storage_interface import LoginStorageInterface
from project_management_portal.exceptions import (
    InvalidUsernameException,
    InvalidPasswordException
)


class LoginStorageImplementation(LoginStorageInterface):

    def validate_username(self, username: str) -> int:
        try:
            user = User.objects.get(username=username)
            return user.id

        except User.DoesNotExist:
            raise InvalidUsernameException


    def validate_password(self, username: str, password: str):

        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise InvalidPasswordException


    def is_admin(self, username: str) -> bool:

        try:
            user = User.objects.get(username=username)
            return user.is_admin

        except User.DoesNotExist:
            raise InvalidUsernameException
