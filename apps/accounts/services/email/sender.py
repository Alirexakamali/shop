from django.conf import settings
from django.core.mail import send_mail


class EmailService:
    @staticmethod
    def send_verification_code(*, email: str, otp: str) -> None:
        send_mail(
            subject="Email Verification",
            message=f"Your verification code is: {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )