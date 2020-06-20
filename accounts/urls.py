from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('password-reset/', include('accounts.urls_reset')),
    path('profile/', views.user_profile, name="user_profile"),
    path('update-profile/', views.update_profile, name="update_profile"),
]
