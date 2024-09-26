import graphene
import ingredients.schema
import users.schema


class Query(
    ingredients.schema.Query,
    users.schema.Query,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
