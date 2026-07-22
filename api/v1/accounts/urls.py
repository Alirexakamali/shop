from django.urls import path

from .views import (
    LoginView,
    RegisterView,
    VerifyRegistrationView,
    ForgotPasswordView,
    VerifyPasswordResetView,
)

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
        name="register",
    ),
    path(
        "register/verify/",
        VerifyRegistrationView.as_view(),
        name="verify-registration",
    ),
    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot-password",
    ),
    path(
        "forgot-password/verify/",
        VerifyPasswordResetView.as_view(),
        name="verify-password-reset",
    ),
]
