from pydantic import BaseModel, ValidationError
from typing import Optional, List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine

#importing from the modulirised files
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# response_model give the user response sent to user or client
@app.post("/profiles/", response_model=schemas.ProfileCreatedSchema)
def create_new_profile(profile: schemas.CreateProfileSchema, db: Session = Depends(get_db)):

#since nationalid is unique, we need to validate it and ensure no other user enters information with same nationalid captured already in the system
	db_profile = crud.verify_id(db, nationalid = profile.nationalid)
	if db_profile:
		raise HTTPException(status_code=400, detail="National ID Already Registered")
#the response sent to user
	return crud.create_profile(db, profile)

#You can remove this if you prefer to use the default url and port
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)