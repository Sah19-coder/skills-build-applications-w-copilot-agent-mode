from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import os

CODESPACE_NAME = os.getenv('CODESPACE_NAME', 'localhost')
BASE_URL = f'https://{CODESPACE_NAME}-8000.app.github.dev'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
]