from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.storages \
    .user_admin_login_storage_implementation import \
        LoginStorageImplementation
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation
from project_management_portal.interactors.user_admin_login_interactor \
    import LoginInteractor
from project_management_portal.common.oauth2_storage import OAuth2SQLStorage
from raven.utils import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = LoginStorageImplementation()
    presenter = PresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()

    interactor = LoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    request_data = kwargs['request_data']

    response = interactor.login(
        username=request_data['username'],
        password=request_data['password'])

    response_data = json.dumps(response)

    return HttpResponse(response_data, status=200)

    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from project_management_portal.views.user_login.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from project_management_portal.views.user_login.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from project_management_portal.views.user_login.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="project_management_portal", test_case=test_case,
    #     operation_name="user_login",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]