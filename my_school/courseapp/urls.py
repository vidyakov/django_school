from django.urls import path

from .views import LessonPageView


app_name = 'courseapp'

urlpatterns = [
    path('<int:pk>/', LessonPageView.as_view(), name='page'),
]

