from django.urls import path
from posts import views
from .views import CommentUpdateView, CommentDeleteView

app_name = 'posts'
urlpatterns = [
    path('blogs/', views.get_posts, name='get_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('update/<int:pk>', CommentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
]
