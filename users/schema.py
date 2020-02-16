import graphene
from .types import UserType
from .queries import resolve_user
from .mutations import CreateAccountMutation


class Query(object):

    user = graphene.Field(
        UserType, id=graphene.Int(required=True), resolver=resolve_user
    )


class Mutation(object):

    create_account = CreateAccountMutation.Field()
