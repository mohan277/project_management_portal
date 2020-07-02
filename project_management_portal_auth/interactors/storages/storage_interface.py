from abc import abstractmethod
from typing import List

from project_management_portal_auth.dtos.user_dto import UserDTO


class StorageInterface:

    @abstractmethod
    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        pass

    @abstractmethod
    def is_admin(self, user_id: int) -> bool:
        pass
