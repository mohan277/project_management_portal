from typing import List

from project_management_portal_auth.dtos.user_dto import UserDTO, IsAdminDTO
from project_management_portal_auth.interactors.storages.storage_interface \
    import StorageInterface
from project_management_portal_auth.models import User


class StorageImplementation(StorageInterface):

    def get_user_details_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        users = list(User.objects.filter(id__in=user_ids))
        user_dtos = []
        for user in users:
            user_dto = self._convert_user_object_to_dto(user=user)
            user_dtos.append(user_dto)
        return user_dtos

    @staticmethod
    def _convert_user_object_to_dto(user):
        return UserDTO(user_id=user.id,
                       name=user.name,
                       is_admin=user.is_admin,
                       profile_pic_url=user.profile_pic_url)


    def is_admin(self, user_id: int):
        is_admin = User.objects.get(id=user_id).is_admin
        is_admin_dto = IsAdminDTO(is_admin=is_admin)
        return is_admin_dto
