from dataclasses import dataclass


@dataclass(slots=True)
class RegisterDTO:
    email: str
    first_name: str
    last_name: str
    password: str