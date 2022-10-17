from flask_sqlalchemy import SQLAlchemy
from fastapi import FastAPI,UploadFile,File
from Routers.users import usersroute
from Routers.manager import managerroute
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import shutil
import pathlib

app = FastAPI()

app.include_router(usersroute, prefix="/users")
app.include_router(managerroute, prefix="/manager")



@app.get("/")
async def api_index():
    return {"Hello": "Worlsd"}



