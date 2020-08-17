from django.urls import path

from .views import CoursePageView


app_name = 'courseapp'

urlpatterns = [
    path('', CoursePageView.as_view(), name='page'),
]

