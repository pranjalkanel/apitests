from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from core.views import TestView, home

urlpatterns = [
    path('', home),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('apilink/', TestView.as_view(), name='test')
]
