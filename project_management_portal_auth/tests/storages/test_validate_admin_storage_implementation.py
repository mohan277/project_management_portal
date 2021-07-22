import pytest
from project_management_portal_auth.dtos.user_dto import IsAdminDTO
from project_management_portal_auth.models.user import User
from project_management_portal_auth.storages.storage_implementation import \
    StorageImplementation


class TestStorageImplementation:

    @pytest.mark.django_db
    def test_given_user_id_is_admin_return_is_admin_valid_dto(
            self, is_admin_valid_dto):

        # Arrange
        expected_dto = is_admin_valid_dto
        user_id = 1
        storage = StorageImplementation()

        # Act
        actual_dto = storage.is_admin(user_id=user_id)

        #Assert
        assert actual_dto == expected_dto

    @pytest.fixture
    def create_user(self):
        user_obj = User.objects.create(
            name='user1',
            is_admin=False,
            profile_pic_url='profile_pic_1'
        )
        return user_obj

    @pytest.fixture
    def is_admin_valid_dto(self, create_user):
        is_admin_valid_dto = IsAdminDTO(is_admin=False)
        return is_admin_valid_dto
