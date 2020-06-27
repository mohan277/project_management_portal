from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_form_closed_exception(self, err):
        pass

    @abstractmethod
    def raise_invalid_form_id(self, err):
        pass

    @abstractmethod
    def raise_question_does_not_belong_to_form_exception(self, err):
        pass

    @abstractmethod
    def raise_invalid_user_response_submitted_exception(self, err):
        pass

    @abstractmethod
    def submit_form_response_details(self, user_response_id: int):
        pass