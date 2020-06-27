class FormClosedException(Exception):
    def __init__(self, msg):
        self.msg = msg


class FormDoesNotExistException(Exception):
    def __init__(self, msg):
        self.msg = msg


class QuestionDoesNotBelongToForm(Exception):
    def __init__(self, msg):
        self.msg = msg


class InvalidUserResponseSubmitException(Exception):
    def __init__(self, msg):
        self.msg = msg
