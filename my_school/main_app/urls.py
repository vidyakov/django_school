from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import IndexPage


app_name = 'main_app'

urlpatterns = [
    path('', IndexPage.as_view(), name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
