from rest_framework.viewsets import ModelViewSet

from .models import AdditionalMaterial, LessonInfo, InteractiveLesson
from .serializers import (
    AdditionalMaterialSerializer,
    LessonInfoSerializer,
    InteractiveLessonSerializer,
)


# class AdditionalMaterialViewSet(ModelViewSet):
#     queryset = AdditionalMaterial.objects.all()
#     serializer_class = AdditionalMaterialSerializer
#
#
class LessonInfoViewSet(ModelViewSet):
    queryset = LessonInfo.objects.all()
    serializer_class = LessonInfoSerializer

#
# class InteractiveLessonViewSet(ModelViewSet):
#     queryset = InteractiveLesson.objects.all()
#     serializer_class = InteractiveLessonSerializer
