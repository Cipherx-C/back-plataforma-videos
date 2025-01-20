from django.urls import path
from .views import RegisterView, LoginView, VideoListCreateView, VideoDetailView, CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', VideoListCreateView.as_view(), name='video_list_create'),  # Página de lista de vídeos
    path('<int:pk>/', VideoDetailView.as_view(), name='video_detail'),  # Detalhe de vídeo
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
