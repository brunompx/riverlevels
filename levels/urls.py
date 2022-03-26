from django.urls import path
from . import views

urlpatterns = [
    path("", views.levelchart_index, name="levelchart"),
]