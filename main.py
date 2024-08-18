from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel, EmailStr  
from typing import List,Annotated
import models
from database import SessionLocal, engine,sessionmaker
from sqlalchemy.orm import Session

app= FastAPI()
models.Base.metadata.create_all(bind=engine)

class ContactUs(BaseModel):
    name : str
    email : EmailStr
    message : str

def get_db():
    try:
        db = SessionLocal(bind=engine)
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/contact-us")
async def contact_us(contact_us : ContactUs, db : db_dependency):
    contact_request = models.ContactRequest(name=contact_us.name, email=contact_us.email, message=contact_us.message)
    db.add(contact_request)
    db.commit()
    db.refresh(contact_request)

    return {"message": "Thank you for contacting us","data":contact_request}
