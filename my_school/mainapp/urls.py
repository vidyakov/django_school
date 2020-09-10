from django.urls import path

from .views import AllCoursesListView, CourseDetailView, ContactFormView

app_name = 'mainapp'

urlpatterns = [
    path('', AllCoursesListView.as_view(), name='index'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
