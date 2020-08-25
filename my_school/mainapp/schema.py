from graphene import List, Int
from graphene_django import DjangoObjectType

from .models import Tag, Course


class TagType(DjangoObjectType):

    class Meta:
        model = Tag


class CourseType(DjangoObjectType):

    class Meta:
        model = Course


class Query:
    all_courses = List(CourseType, limit=Int())
    all_tags = List(TagType, limit=Int())

    def resolve_all_courses(self, resolve_info, *, limit: int = None):
        return Course.objects.all()[:limit]

    def resolve_all_tags(self, resolve_info, *, limit: int = None):
        return Tag.objects.all()[:limit]
