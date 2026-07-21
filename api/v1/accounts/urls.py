from django.urls import path

from .views import LoginView , RegisterView

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    # path(
    #     "password-login/",
    #     PasswordLoginView.as_view(),
    #     name="password-login",
    # ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),
    # path(
    #     "verify-email/",
    # ),
]
