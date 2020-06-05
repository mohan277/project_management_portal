from project_management_portal.interactors.storages. \
    workflow_storage_interface import WorkflowStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


class GetWorkflowsInteractor:
    def __init__(self,
                 storage: WorkflowStorageInterface,
                 presenter: PresenterInterface):

            self.storage = storage
            self.presenter = presenter


    def get_list_of_workflows(self):

        list_of_workflows_dto = self.storage.get_list_of_workflows()

        response = self.presenter.get_list_of_workflows_response(
            list_of_workflows_dto=list_of_workflows_dto
        )

        return response
