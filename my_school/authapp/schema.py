from graphene import List, Int
from graphene_django import DjangoObjectType

from .models import SchoolUser


class SchoolUserType(DjangoObjectType):

    class Meta:
        model = SchoolUser


class Query:
    all_users = List(SchoolUserType, limit=Int())

    def resolve_all_users(self, resolve_info, *, limit: int = None):
        return SchoolUser.objects.all()[:limit]
