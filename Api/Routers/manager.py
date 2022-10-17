from fastapi import APIRouter,Depends, Request,HTTPException,FastAPI,UploadFile,File
from flask import jsonify
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from Lib.models import SessionLocal,İmage,Video
import json
import shutil
import pathlib
import os
from typing import List


#gün kontrolü için eklediğim tarihler
Now = datetime.today() 
Future=datetime.today() + timedelta(days=2)


managerroute = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()





@managerroute.get("/img")
async def home(req: Request, db: Session = Depends(get_db)):
    """ bütün kullanıcıların sıralandığı fonksiyon"""
    images = db.query(İmage).all()
    if not  images:
        raise HTTPException(status_code=404,detail="Resim bulunamadı")
    else :
        return  images



@managerroute.get("/img/{id}")
async def get_user(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    image = db.query(İmage).filter_by(id=id).first()
    if image != None:
        return image
    else :
        raise HTTPException(status_code=404,detail="Aranan Kullanıcı yoktur")



@managerroute.post("/img/add")
async def upload_image(req: Request,db: Session = Depends(get_db),uploaded_file: UploadFile = File(...)):
      filextensions = ['image/png', 'image/jpg', 'image/jpeg']
      if uploaded_file.content_type in filextensions :
        file_location = f"../Img/{uploaded_file.filename}"
        with open(file_location, "wb+") as file_object:
          shutil.copyfileobj(uploaded_file.file,file_object)
          new_image=İmage(img_name=uploaded_file.filename)
          db.add(new_image)
          db.commit()
        return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
      else :
        return {"file_name":"imaj değil"}
  
@managerroute.delete("/img/delete/{id}")
async def remove_image(req: Request,id:int,db: Session = Depends(get_db)):
   image = db.query(İmage).filter_by(id=id).first()
   if image != None:
        if os.path.isfile("../Img/" +image.img_name):
            os.remove("Img/" +image.img_name)
            db.delete(image)
            db.commit()
        else:    ## Show an error ##
            db.delete(image)
            db.commit()
   else:    ## Show an error ##
      return {"file_name":"dosya silindi"}
  
""" 
@managerroute.delete("/img/delete/{id}")
async def remove_image(req: Request,id:int,db: Session = Depends(get_db)):
   image = db.query(İmage).filter_by(id=id).first()
   if image != None:
    if os.path.isfile("../Img/" +image.img_name):
      os.remove("../Img/" +image.img_name)
      db.delete(image)
      db.commit()
    else:    ## Show an error ##
        print("dosya yoktur")
    return {"file_name":"dosya silindi"}
   else :
        raise HTTPException(status_code=404,detail="resim yoktur")
     
   """



@managerroute.get("/video")
async def home(req: Request, db: Session = Depends(get_db)):
    """ bütün kullanıcıların sıralandığı fonksiyon"""
    images = db.query(Video).all()
    if not  images:
        raise HTTPException(status_code=404,detail="Resim bulunamadı")
    else :
        return  images



@managerroute.get("/video/{id}")
async def get_user(req: Request,id:int, db: Session = Depends(get_db)):
    """ istenilen kullanıcının bilgilerini veren fonksiyon"""
    image = db.query(Video).filter_by(id=id).first()
    if image != None:
        return image
    else :
        raise HTTPException(status_code=404,detail="Aranan Kullanıcı yoktur")




@managerroute.post("/video")
async def video_upload(req: Request,db: Session = Depends(get_db),file:UploadFile=File(...)):
  filextensions = ['video/mp4', 'video/avi', 'video/mpeg', 'video/3gp']
  if file.content_type in filextensions :
    file_location = f"../Videos/{file.filename}"
    with open(file_location, "wb+") as file_object:
          shutil.copyfileobj(file.file,file_object)
          new_video=Video(video_name=file.filename)
          db.add(new_video)
          db.commit()
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}
  else :
      return {"file_name":"video  değil"}






@managerroute.delete("/video/delete/{id}")
async def remove_video(req: Request,id:int,db: Session = Depends(get_db)):
   video = db.query(İmage).filter_by(id=id).first()
   if video != None:
        if os.path.isfile("../Videos/" +video.video_name):
            os.remove("../Videos/" +video.video_name)
            db.delete(video)
            db.commit()
        else:    ## Show an error ##
            db.delete(video)
            db.commit()
   else:    ## Show an error ##
      return {"file_name":"dosya silindi"}

