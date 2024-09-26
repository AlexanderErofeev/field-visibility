from graphene_django.utils.testing import GraphQLTestCase
from django.contrib.auth.models import User, Permission
from core.schema import create_schema


class UsersTestCase(GraphQLTestCase):
    def setUp(self):
        permission = Permission.objects.get(codename='view_user')
        self.user_with_permission = User.objects.create_user(username="user1", password="pass")
        self.user_with_permission.user_permissions.add(permission)

        self.user_without_permission = User.objects.create_user(username="user2", password="pass")

        self.user_query = '''
        query UserQuery {
          user(id: 1) {
            username
            email
          }
        }
        '''

        self.query_introspection = '''
        query QueryIntrospection {
          type: __type(name: "Query") {
            fields {
              name
              description
            }
          }
        }
        '''

    def test_user_query_with_permission(self):
        schema = create_schema(self.user_with_permission)
        result = schema.execute(self.user_query)
        assert not result.errors
        assert result.data == {'user': {'username': 'user1', 'email': ''}}

    def test_user_query_without_permission(self):
        schema = create_schema(self.user_without_permission)
        result = schema.execute(self.user_query)
        assert len(result.errors) == 1
        assert result.errors[0].message == '''Cannot query field 'user' on type 'Query'.'''

    def test_introspection_with_permission(self):
        schema = create_schema(self.user_with_permission)
        result = schema.execute(self.query_introspection)
        assert not result.errors
        assert {'name': 'user', 'description': 'Gets single User by ID'} in result.data['type']['fields']

    def test_introspection_without_permission(self):
        schema = create_schema(self.user_without_permission)
        result = schema.execute(self.query_introspection)
        assert not result.errors
        assert not any(field['name'] == 'user' for field in result.data['type']['fields'])
