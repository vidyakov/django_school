from django.conf import settings
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, FormView

from .forms import ContactForm
from .models import Course


class AllCoursesListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'mainapp/contact_form.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        user_name = form.cleaned_data.get('name')
        user_message = form.cleaned_data.get('message')
        user_email = form.cleaned_data.get('email')

        send_mail(user_name, user_message, settings.EMAIL_HOST_USER, [settings.ADMINISTRATORS_EMAILS])
        send_mail(user_name, user_message, settings.EMAIL_HOST_USER, [user_email])

        return super().form_valid(form)
