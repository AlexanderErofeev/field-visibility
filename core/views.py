from graphene_django.views import GraphQLView


class DynamicSchemaGraphQLView(GraphQLView):
    create_schema = None

    def __init__(self, create_schema, *args, **kwargs):
        self.create_schema = create_schema
        super(DynamicSchemaGraphQLView, self).__init__(create_schema(), *args, **kwargs)

    def get_response(self, request, *args, **kwargs):
        self.schema = self.create_schema(request.user)
        return super(DynamicSchemaGraphQLView, self).get_response(request, *args, **kwargs)
