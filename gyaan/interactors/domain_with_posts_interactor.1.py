from gyaan.interactors.presenters.dtos import DomainDetailsWithPosts
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import \
    PresenterInterface
from gyaan.exceptions.exceptions import DomainDoesNotExist, \
    UserNotDomainMember
from gyaan.interactors.domain_details import DomainDetailsInteractor
from gyaan.interactors.domain_posts import DomainPostsInteractor


class DomainWithPostsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_with_posts_wrapper(self, user_id: int, domain_id: int,
                                      offset: int, limit: int,
                                      presenter: PresenterInterface):
        try:
            return self._get_domain_with_posts_response(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset,
                limit=limit,
                presenter=presenter
            )
        except DomainDoesNotExist as err:
            presenter.raise_domain_id_does_not_exist_exception(err)
            return
        except UserNotDomainMember as err:
            presenter.raise_user_not_domain_member_exception(err)
            return

    def _get_domain_with_posts_response(self, user_id: int, domain_id: int,
                                        offset: int, limit: int,
                                        presenter: PresenterInterface):
        domain_with_posts_dto = self.get_domain_with_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        response = presenter.get_domain_posts_response(
            domain_with_posts_dto=domain_with_posts_dto
        )
        return response

    def get_domain_with_posts(self, user_id: int, domain_id: int,
                              offset: int, limit: int):

        domain_details_interactor = DomainDetailsInteractor(
            storage=self.storage
        )

        domain_details = domain_details_interactor.get_domain_details(
            user_id=user_id,
            domain_id=domain_id
        )

        domain_posts_interactor = DomainPostsInteractor(
            storage=self.storage
        )

        domain_posts = domain_posts_interactor.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )

        return DomainDetailsWithPosts(
            post_details=domain_posts,
            domain_details=domain_details
        )
