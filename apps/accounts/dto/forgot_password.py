from attrs import define, field


@define(frozen=True, slots=True)
class ForgotPasswordDTO:
    email: str


@define(frozen=True, slots=True)
class VerifyPasswordResetDTO:
    email: str
    otp: str
    new_password: str
