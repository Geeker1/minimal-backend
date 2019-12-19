import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from product import schema


class Query(schema.Query,ObjectType):
    pass


class Mutation(schema.Mutation,ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
