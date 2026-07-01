from django.urls import path

from .views.login import LoginView
from .views.password import PasswordLoginView

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path(
        "password-login/",
        PasswordLoginView.as_view(),
        name="password-login",
    ),
]
