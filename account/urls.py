from django.urls import path

from . import views 

app_name = "account"

urlpatterns = [
    path("register", views.sign_up, name="signup"),
    path("logout", views.Logout, name="logout"),
    path("login", views.Login, name="login")]