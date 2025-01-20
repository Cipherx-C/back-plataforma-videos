from django.urls import path
from .views import RegisterView, LoginView, VideoListCreateView, VideoDetailView, CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('videos/', VideoListCreateView.as_view(), name='video_list_create'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]