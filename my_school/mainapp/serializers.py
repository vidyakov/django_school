from rest_framework.serializers import ModelSerializer

from authapp.models import SchoolUser
from mainapp.models import Course


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = 'name', 'description', 'price'


class SchoolUserSerializer(ModelSerializer):

    class Meta:
        model = SchoolUser
        fields = 'first_name', 'last_name'
