from pydantic import BaseModel, EmailStr, field_validator


class CreateUserDTO(BaseModel):
    name: str
    email: EmailStr

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        parts = value.strip().split()
        if len(parts) < 2:
            raise ValueError("Name must include at least a first and last name.")
        elif len(parts[0]) < 2 or len(parts[-1]) < 2:
            raise ValueError("First name and last name must have at least 2 characters.")
        return value