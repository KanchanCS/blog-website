from django.urls import path
from .import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("single/<int:id>/", views.single, name="single"),
    path("like-<int:post_id>/", views.like, name="like"),
    path("unlike-<int:post_id>/", views.unlike, name="unlike"),
]