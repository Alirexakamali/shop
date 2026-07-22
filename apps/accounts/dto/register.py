from attrs import define, field


@define(frozen=True, slots=True)
class RegisterDTO:
    first_name: str
    last_name: str
    email: str = field(converter=lambda value: value.strip().lower())
    password: str
    
@define(frozen=True, slots=True)
class VerifyRegistrationDTO:
    email: str = field(converter=str.lower)
    otp: str