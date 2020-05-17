from django.urls import path
from . import views


urlpatterns = [
	path('highlight/', views.get_highlight, name="get_highlight")
]