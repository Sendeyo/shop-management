
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", include("website.urls")),
    path('admin/', admin.site.urls),
    path("login", auth_views.LoginView.as_view(template_name="website/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="website/logout.html"), name="logout")
]
