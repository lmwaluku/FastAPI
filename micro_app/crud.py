from sqlalchemy.orm import Session
import models, schemas 

# verify the nationalid number submitted by user that it doesn't exist already in the database
def verify_id(db: Session, nationalid: str):
    return db.query(models.CreateProfileDBModel).filter(models.CreateProfileDBModel.nationalid == nationalid).first()

# insert the captured data into the database
def create_profile(db: Session, profiled: schemas.CreateProfileSchema):
    insert_profile = models.CreateProfileDBModel(
		name = profiled.name,
		surname = profiled.surname,
		nationalid = profiled.nationalid,
		sex = profiled.sex,
	)
    db.add(insert_profile)
    db.commit()
    db.refresh(insert_profile)
    return insert_profile
