from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.storages.project_storage_implementation \
    import ProjectStorageImplementation
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation
from project_management_portal.interactors.get_projects_interactor import \
    GetProjectsInteractor
from raven.utils import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = ProjectStorageImplementation()
    presenter = PresenterImplementation()

    user = kwargs['user']
    query_parameters = kwargs['request_query_params']

    interactor = GetProjectsInteractor(storage=storage, presenter=presenter)

    list_of_projects_dict = interactor.get_list_of_projects(
        user_id=user.id,
        limit=query_parameters['limit'],
        offset=query_parameters['offset']
    )

    response_data = json.dumps(list_of_projects_dict)
    return HttpResponse(response_data, status=200)

   # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from project_management_portal.views.list_of_projects.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from project_management_portal.views.list_of_projects.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from project_management_portal.views.list_of_projects.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="project_management_portal", test_case=test_case,
    #     operation_name="list_of_projects",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]