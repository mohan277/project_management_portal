from unittest.mock import create_autospec

from project_management_portal_auth.dtos.user_dto import IsAdminDTO
from project_management_portal_auth.interactors.validate_admin_interactor \
    import ValidateAdminInteractor
from project_management_portal_auth.interactors.storages.storage_interface \
    import StorageInterface


class TestValidateAdminInteractor:

    def test_given_user_id_is_admin_return_boolean_value(self):

        #Arrange
        user_id = 1
        expected_admin_dto = IsAdminDTO(
            is_admin=True
        )
        storage = create_autospec(StorageInterface)
        storage.is_admin.return_value = expected_admin_dto
        interactor = ValidateAdminInteractor(storage=storage)

        # Act
        actual_admin_dto = interactor.is_admin(
            user_id=user_id)

        # Assert
        assert actual_admin_dto == expected_admin_dto
        storage.is_admin.assert_called_once_with(
            user_id=user_id)
