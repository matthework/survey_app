from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    full_name: str | None = None


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
