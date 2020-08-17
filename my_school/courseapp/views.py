from pprint import pprint

from django.views.generic import TemplateView


class CoursePageView(TemplateView):
    template_name = 'courseapp/course.html'

    def get(self, request, *args, **kwargs):
        pprint(kwargs)
        return super().get(request, *args, **kwargs)
