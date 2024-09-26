import graphene
import ingredients.schema
import users.schema


def create_schema(user=None):
    query = type('Query', (
        ingredients.schema.Query,
        users.schema.Query,
        graphene.ObjectType
    ), {})
    return graphene.Schema(query=query)
