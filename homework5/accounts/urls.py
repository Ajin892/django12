from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup_view, name="signup"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("counter/", views.counter_view, name="counter"),
    path("logout/", views.logout_view, name="logout"),
]
