from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import InteractiveLesson
from .serializers import InteractiveLessonSerializer


class LessonPageView(APIView):
    def get(self, request, pk):
        lesson = get_object_or_404(InteractiveLesson, pk=pk)
        lesson_serializer = InteractiveLessonSerializer(lesson)
        return Response(lesson_serializer.data)
