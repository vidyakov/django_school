from django.urls import path

from .views import LessonInfoViewSet


app_name = 'courseapp'

urlpatterns = [
    path('info/', LessonInfoViewSet.as_view({'get': 'list'}), name='lesson_info'),
    # path('interactive/', LessonInfoViewSet.as_view({'get': 'list'}), name='lesson_interactive'),
    # path('materials/', LessonInfoViewSet.as_view({'get': 'list'}), name='lessons_materials'),
]

