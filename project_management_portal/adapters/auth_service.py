from typing import List
from project_management_portal.interactors.storages.dtos import FinalUserDTO


class AuthService:

    @property
    def interface(self):
        from project_management_portal_auth.interfaces.service_interface \
            import ServiceInterface
        return ServiceInterface()

    def get_user_dtos(self, user_ids: List[int]):
        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)

        # TODO: Convert to DTO in this app
        user_details_dtos = [
            FinalUserDTO(
                name=user_dto.name,
                user_id=user_dto.user_id,
                is_admin=user_dto.is_admin,
                profile_pic_url=user_dto.profile_pic_url
            )
            for user_dto in user_dtos
        ]
        return user_details_dtos