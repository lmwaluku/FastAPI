from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

# Enumaration for Gender
class Gender(str, Enum):
    male = 'male'
    female = 'female'

# Basemodel for data entered by the user
class CreateProfileSchema(BaseModel):
	name: str
	surname: str
	nationalid: str
	sex: Gender = Gender.male

# data returned to user
class ProfileCreatedSchema(CreateProfileSchema):
	id: int
	nationalid: str
	
	class Config:
		orm_mode = True