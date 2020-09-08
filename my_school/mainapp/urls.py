from django.urls import path

from .views import AllCoursesListView, CourseDetailView, ContactFormView, Courses, Students

app_name = 'mainapp'

urlpatterns = [
    path('', AllCoursesListView.as_view(), name='index'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course'),
    path('contact/', ContactFormView.as_view(), name='contact'),

    path('api/courses/', Courses.as_view(), name='courses'),
    path('api/students/', Students.as_view(), name='students')
]
