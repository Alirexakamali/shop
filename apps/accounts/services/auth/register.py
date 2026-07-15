from attrs import define, field


@define(frozen=True, slots=True)
class RegisterData:
    first_name: str
    last_name: str
    email: str = field(converter=str.lower)
    password: str


class RegisterService:
    
    def register(self,data: RegisterData) -> None: ...
