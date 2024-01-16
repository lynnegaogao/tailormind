from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,    
    allow_origins= "http://localhost:5173/",    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)

@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    dirs = 'uploads'
    # 判断uploads目录是否存在，否则新建uploads目录
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    # 保存上传文件到uploads目录
    file_location = f"{dirs}/{file.filename}"
    with open(file_location, "wb") as file_object:
        file_object.write(file.file.read())
    return {"filename": file.filename}