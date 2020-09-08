from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'main_app/index.html'

