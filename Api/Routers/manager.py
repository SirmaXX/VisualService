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
  


@managerroute.put("/img/update/{id}/{img_name}")
async def update_image(req: Request,id:int,img_name:str,db: Session = Depends(get_db)):
     file_location = f"../Img/" 
     image = db.query(İmage).filter_by(id=id).first()
     if image != None:
        if os.path.isfile( file_location+img_name):
          print("The file already exists")
        else:
         os.rename( file_location+image.img_name,file_location+img_name)
         db.query(İmage).filter_by(id=id).update(dict(img_name=img_name))
         db.commit()        
     else :
        return False    



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




@managerroute.post("/video/add")
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






@managerroute.put("/video/update/{id}/{video_name}")
async def update_video(req: Request,id:int,video_name:str,db: Session = Depends(get_db)):
     file_location = f"../Videos/" 
     video = db.query(Video).filter_by(id=id).first()
     if video != None:
        if os.path.isfile( file_location+video_name):
          print("The file already exists")
        else:
         os.rename( file_location+video.video_name,file_location+video_name)
         db.query(Video).filter_by(id=id).update(dict(video_name=video_name))
         db.commit()        
     else :
        return False    





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

