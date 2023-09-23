from django.urls import path
from .import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("single/<int:id>/", views.single, name="single"),
]