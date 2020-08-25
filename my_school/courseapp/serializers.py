from rest_framework import serializers

from .models import InteractiveLesson


class InteractiveLessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InteractiveLesson
        fields = 'materials', 'second_limit', 'error_limit'
