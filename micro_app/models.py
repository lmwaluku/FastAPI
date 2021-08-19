from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from database import Base
from schemas import Gender
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Database Model for the User Profile
class CreateProfileDBModel(Base):
	__tablename__ = "profiles"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(100))
	surname = Column(String(100))
	nationalid = Column(String(100), unique=True, index=True)
	sex = Column(Enum(Gender))