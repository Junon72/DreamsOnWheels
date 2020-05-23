from django.urls import path
from . import views
from posts.views import CommentUpdateView

app_name = 'posts'
urlpatterns = [
    path('blogs/', views.get_posts, name='get_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('update/<int:pk>', views.CommentUpdateView.as_view(), name='update_comment'),
]