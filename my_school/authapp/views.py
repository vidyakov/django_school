from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SchoolUserCreationForm
from .models import SchoolUser


class SchoolUserCreateView(FormView):
    model = SchoolUser
    form_class = SchoolUserCreationForm
    success_url = reverse_lazy('main:index')
    template_name = 'authapp/schooluser_form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SchoolUserLoginView(LoginView):
    template_name = 'authapp/login.html'
    redirect_authenticated_user = reverse_lazy('main:index')


class SchoolUserLogoutView(LogoutView):
    next_page = reverse_lazy('main:index')

