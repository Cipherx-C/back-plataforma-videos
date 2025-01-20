from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Supondo que você tenha um app chamado `api`
    path('', RedirectView.as_view(url='/api/', permanent=True)),  # Redireciona a raiz para o app `api`
]