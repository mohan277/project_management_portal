import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from project_management_portal.interactors.get_workflows_interactor import \
    GetWorkflowsInteractor
from project_management_portal.interactors.storages. \
    workflow_storage_interface import WorkflowStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.interactors.storages.dtos import \
    ListOfWorkflowsDto


def test_get_workflows_returns_list_of_workflows(list_of_workflow_dtos,
                                                 get_workflows_expected_output):

    # Arrange
    total_count_of_workflows = 1
    storage = create_autospec(WorkflowStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetWorkflowsInteractor(
        storage=storage,
        presenter=presenter
    )

    list_of_workflows_dto = ListOfWorkflowsDto(
        list_of_workflow_dtos=list_of_workflow_dtos,
        total_count_of_workflows=total_count_of_workflows
    )

    storage.get_list_of_workflows.return_value = list_of_workflows_dto
    presenter.get_list_of_workflows_response. \
        return_value = get_workflows_expected_output

    # Act
    response = interactor.get_list_of_workflows()

    # Assert
    storage.get_list_of_workflows.assert_called_once()

    presenter.get_list_of_workflows_response.assert_called_once_with(
        list_of_workflows_dto=list_of_workflows_dto
    )

    assert response == get_workflows_expected_output
