from django.urls import path
from . import views


urlpatterns = [
    path('blogs/', views.get_posts, name='get_posts'),
    path('post/<pk>/', views.post_detail, name='post_detail')
]