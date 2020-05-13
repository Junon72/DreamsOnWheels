from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.user_profile, name="user_profile" ),
    path('password-reset/', include('accounts.url_reset'))
]