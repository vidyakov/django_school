from rest_framework.viewsets import ModelViewSet

from .models import LessonInfo
from .serializers import (
    LessonInfoSerializer,
)


class LessonInfoViewSet(ModelViewSet):
    queryset = LessonInfo.objects.all()
    serializer_class = LessonInfoSerializer
