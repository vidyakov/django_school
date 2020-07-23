from django.views.generic import ListView, DetailView

from .models import Course


class AllCoursesListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course
