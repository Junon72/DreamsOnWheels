from django.urls import path
from . import views

app_name = 'highlight'

urlpatterns = [
    path('highlight/', views.get_highlight, name="get_highlight"),
    path('vote/<id>/', views.up_vote, name="up_vote"),
]
