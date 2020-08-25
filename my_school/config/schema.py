from graphene import ObjectType, Schema

from mainapp.schema import Query as MainAppQuery
from authapp.schema import Query as AuthAppQuery


class Query(AuthAppQuery, MainAppQuery, ObjectType):
    pass


schema = Schema(query=Query)
