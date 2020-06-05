from abc import ABC
from abc import abstractmethod

class LoginStorageInterface:

    @abstractmethod
    def validate_username(self, username: str):
        pass

    @abstractmethod
    def validate_password(self, username: str, password: str) -> int:
        pass


    @abstractmethod
    def is_admin(self, username: str) -> bool:
        pass
