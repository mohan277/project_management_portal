from formaster.exceptions.exceptions import FormClosedException
from formaster.interactors.storages.storage_interface import StorageInterface


class FormValidationMixin:
    def validate_form_is_live(self, form_id: int):
        form_dto = self.storage.get_form_dto(form_id=form_id)
        is_not_live = not form_dto.is_live
        if is_not_live:
            raise FormClosedException(form_id)
