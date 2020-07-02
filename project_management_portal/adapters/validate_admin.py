class ValidateAdmin:
    @property
    def interface(self):
        from project_management_portal_auth.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_is_admin_valid_dto(self, user_id: int):
        is_admin_valid_dto = self.interface.get_is_admin_valid_dto(user_id=user_id)
        return is_admin_valid_dto
