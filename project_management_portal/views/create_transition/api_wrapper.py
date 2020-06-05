from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.storages.transition_storage_implementation \
    import TransitionStorageImplementation
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation
from project_management_portal.interactors.create_transition_interactor import \
    CreateTransitionInteractor
from raven.utils import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = TransitionStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateTransitionInteractor(
        storage=storage,
        presenter=presenter
    )

    request_data = kwargs['request_data']

    transition_details_dict = interactor.create_transition(
        name=request_data['name'],
        description=request_data['description'],
        from_state=request_data['from_state'],
        to_state=request_data['to_state'])

    response_data = json.dumps(transition_details_dict)

    return HttpResponse(response_data, status=200)
    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from project_management_portal.views.create_transition.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from project_management_portal.views.create_transition.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from project_management_portal.views.create_transition.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="project_management_portal", test_case=test_case,
    #     operation_name="create_transition",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]