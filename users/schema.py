from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType

User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


def create_query(user=None):
    fields = {}

    if user and user.has_perm('auth.view_user'):
        def resolve_user(*args, id: int):
            return User.objects.get(id=id)
        fields['user'] = graphene.Field(
            UserType,
            id=graphene.Int(required=True),
            description='Gets single User by ID',
            resolver=resolve_user
        )

    return type('Query', (graphene.ObjectType,), fields)
