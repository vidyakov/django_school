from rest_framework import serializers

from .models import AdditionalMaterial, LessonInfo, InteractiveLesson


class AdditionalMaterialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AdditionalMaterial
        fields = 'name', 'link', 'file'


class LessonInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LessonInfo
        fields = 'name', 'course'


class InteractiveLessonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = InteractiveLesson
        fields = 'materials', 'second_limit', 'error_limit'
