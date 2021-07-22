from project_management_portal_auth.interactors.storages.storage_interface \
    import StorageInterface

class ValidateAdminInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def validate_admin_wrapper(self, user_id: int):
        return self.is_admin(user_id=user_id)

    def is_admin(self, user_id: int):
        is_admin_dto = self.storage.is_admin(user_id=user_id)
        return is_admin_dto
