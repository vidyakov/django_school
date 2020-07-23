from django.urls import path

from .views import SchoolUserCreateView, SchoolUserLoginView, SchoolUserLogoutView


app_name = 'authapp'

urlpatterns = [
    path('register/', SchoolUserCreateView.as_view(), name='create'),
    path('login/', SchoolUserLoginView.as_view(), name='login'),
    path('logout/', SchoolUserLogoutView.as_view(), name='logout'),
]
