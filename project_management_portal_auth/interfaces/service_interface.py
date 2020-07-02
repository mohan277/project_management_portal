from typing import List

from project_management_portal_auth.interactors.get_user_details_interactor \
    import GetUserDetailsInteractor
from project_management_portal_auth.interactors.validate_admin_interactor \
    import ValidateAdminInteractor
from project_management_portal_auth.storages.storage_implementation import \
    StorageImplementation


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]):
        storage = StorageImplementation()
        interactor = GetUserDetailsInteractor(storage=storage)
        user_dtos = interactor.get_user_details_dtos(user_ids=user_ids)
        return user_dtos

    @staticmethod
    def get_is_admin_valid_dto(user_id: int):
        storage = StorageImplementation()
        interactor = ValidateAdminInteractor(storage=storage)
        is_admin_dto = interactor.is_admin(user_id=user_id)
        return is_admin_dto
