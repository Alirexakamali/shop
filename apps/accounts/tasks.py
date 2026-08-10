from celery import shared_task 

from .services.email.sender import EmailService


@shared_task
def send_register_otp(email: str, otp: str) -> None:
    EmailService.send_verification_code(
        email=email,
        otp=otp,
    )

