from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from project_management_portal.storages.task_storage_implementation \
    import TaskStorageImplementation
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation
from project_management_portal.interactors.create_task_interactor import \
    CreateTaskInteractor
from raven.utils import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    storage = TaskStorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )

    user = kwargs['user']
    request_data = kwargs['request_data']
    state = request_data.get('state')

    task_details_dict = interactor.create_task(
        user_id=user.id,
        title=request_data['title'],
        description=request_data['description'],
        project=request_data['project'],
        state=state,
        issue_type=request_data['issue_type']
    )

    response_data = json.dumps(task_details_dict)

    return HttpResponse(response_data, status=200)


    # ---------MOCK IMPLEMENTATION---------

    # try:
    #     from project_management_portal.views.create_task.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from project_management_portal.views.create_task.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from project_management_portal.views.create_task.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="project_management_portal", test_case=test_case,
    #     operation_name="create_task",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]