from abc import ABC
from abc import abstractmethod

class StorageInterface:

    @abstractmethod
    def validation_of_username(self, username: str):
        pass


    def validation_of_password(self, username: str, password: str):
        pass
