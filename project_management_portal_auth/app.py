from django.apps import AppConfig


class FbPostAuthAppConfig(AppConfig):
    name = "project_management_portal_auth"

    def ready(self):
        from project_management_portal_auth import signals # pylint: disable=unused-variable
