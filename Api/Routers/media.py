from fastapi import APIRouter,Depends, Request,HTTPException, FastAPI,UploadFile,File
from flask import jsonify
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from Lib.models import SessionLocal
import os
import shutil

#gün kontrolü için eklediğim tarihler
Now = datetime.today() 
Future=datetime.today() + timedelta(days=2)


mediaroute = APIRouter(responses={404: {"description": "Not found"}})

# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()



mediaroute.post("/")
async def root(uploaded_file: UploadFile = File(...)):
      filextensions = ['image/png', 'image/jpg', 'image/jpeg']
      if uploaded_file.content_type in filextensions :
        file_location = f"Img/{uploaded_file.filename}"
        with open(file_location, "wb+") as file_object:
          shutil.copyfileobj(uploaded_file.file,file_object)
        return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
      else :
        return {"file_name":"imaj değil"}
  


mediaroute.delete("/img/{imgname}")
async def remove_image(imgname:str):
  if os.path.isfile("Img/" +imgname):
     os.remove("Img/" +imgname)
  else:    ## Show an error ##
    print("Error: %s file not found" % imgname)
  return {"file_name":"dosya silindi"}



mediaroute.post("/video")
async def video_upload(file:UploadFile=File(...)):
  filextensions = ['video/mp4', 'video/avi', 'video/mpeg', 'video/3gp']
  if file.content_type in filextensions :
    file_location = f"Videos/{file.filename}"
    with open(file_location, "wb+") as file_object:
          shutil.copyfileobj(file.file,file_object)
    return {"info": f"file '{file.filename}' saved at '{file_location}'"}
  else :
      return {"file_name":"video  değil"}


mediaroute.delete("/video/{videoname}")
async def remove_video(videoname:str):
  if os.path.isfile("Videos/" +videoname):
     os.remove("Videos/" +videoname)
  else:    ## Show an error ##
    print("Error: %s file not found" % videoname)
  return {"file_name":"dosya silindi"}



