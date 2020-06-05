from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.storages.transition_storage_implementation \
    import TransitionStorageImplementation
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation
from project_management_portal.interactors.get_transition_details_interactor import \
    GetTransitionDetailsInteractor
from raven.utils import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = TransitionStorageImplementation()
    presenter = PresenterImplementation()

    request_data = kwargs['request_data']
    task_id = kwargs['task_id']
    to_state = request_data['to_state']

    interactor = GetTransitionDetailsInteractor(storage=storage, presenter=presenter)

    list_of_checklists_dict = interactor. \
        get_transition_details_between_two_states(task_id=task_id,
                                                  to_state=to_state)

    response_data = json.dumps(list_of_checklists_dict)
    print(response_data)
    return HttpResponse(response_data, status=200)


    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from project_management_portal.views.transition_details.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from project_management_portal.views.transition_details.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from project_management_portal.views.transition_details.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="project_management_portal", test_case=test_case,
    #     operation_name="transition_details",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]