from rest_framework.generics import ListAPIView

from authapp.models import SchoolUser
from .serializers import CourseSerializer, SchoolUserSerializer
from mainapp.models import Course


class Courses(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class Students(ListAPIView):
    queryset = SchoolUser.objects.all()
    serializer_class = SchoolUserSerializer
