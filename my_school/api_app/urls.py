from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api_app.views import Students, Courses


app_name = 'api_app'

urlpatterns = [
    path('students/', Students.as_view(), name='students'),
    path('courses/', Courses.as_view(), name='courses'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
