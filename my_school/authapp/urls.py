from django.urls import path

from .views import SchoolUserCreateView, SchoolUserLoginView, SchoolUserLogoutView, AuthChoice

app_name = 'authapp'

urlpatterns = [
    path('choice/', AuthChoice.as_view(), name='choice'),

    path('register/', SchoolUserCreateView.as_view(), name='create'),
    path('login/', SchoolUserLoginView.as_view(), name='session-auth'),
    path('logout/', SchoolUserLogoutView.as_view(), name='logout'),
]
