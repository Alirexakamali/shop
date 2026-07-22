from enum import StrEnum


class ForgotPasswordStatus(StrEnum):

    SUCCESS = "SUCCESS"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    OTP_SENT = "OTP_SENT"


class VerifyPasswordResetStatus(StrEnum):

    SUCCESS = "SUCCESS"
    INVALID_OTP = "INVALID_OTP"
    OTP_EXPIRED = "OTP_EXPIRED"
    TOO_MANY_ATTEMPTS = "TOO_MANY_ATTEMPTS"
    PASSWORD_RESET_NOT_FOUND = "PASSWORD_RESET_NOT_FOUND"
