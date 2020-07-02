# from ib_common.service_adapter_utils.base_adapter_class import BaseAdapterClass


# class ServiceAdapter(BaseAdapterClass):
#     def __init__(self, *args, **kwargs):
#         from django.conf import settings
#         source = settings.IB_MINIPROJECTS_BACKEND_SOURCE
#         kwargs['source'] = source
#         super(ServiceAdapter, self).__init__(*args, **kwargs)

    # ******* sample service adapter property ********
    # @property
    # def ib_users(self):
    #     from sample_app.adapters.ib_users_service_adapter import \
    #         IBUsersServiceAdapter
    #     return IBUsersServiceAdapter(access_token=self.access_token,
    #                                  user=self.user, source=self.source)


class ServiceAdapter:

    @property
    def auth_service(self):
        from .auth_service import AuthService
        return AuthService()

    @property
    def validate_admin(self):
        from .validate_admin import ValidateAdmin
        return ValidateAdmin()


def get_service_adapter():
    return ServiceAdapter()
