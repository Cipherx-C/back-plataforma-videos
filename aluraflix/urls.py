# aluraflix/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', include('videos.urls')),  # Inclui as URLs do app `videos`
    path('', include('videos.urls')),  # Inclui as URLs do app videos diretamente na raiz
]
