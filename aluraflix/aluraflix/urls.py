from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', include('videos.urls')),  # Inclui as URLs do app `videos`
    path('', RedirectView.as_view(url='/videos/', permanent=True)),  # Redireciona a raiz para o app `videos`
]