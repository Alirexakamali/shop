from django.urls import path

from .views import LoginView, RegisterView, VerifyRegistrationView

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
    path("register/", RegisterView.as_view(), name="register"),
    path("register/verify/", VerifyRegistrationView.as_view(), name="verify-registration"),
]
