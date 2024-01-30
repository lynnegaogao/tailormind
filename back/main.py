#from fastapi import FastAPI, File, UploadFile
#from fastapi.responses import FileResponse
#from fastapi.middleware.cors import CORSMiddleware
#import os
#from dotenv import load_dotenv
 
#load_dotenv()
#app = FastAPI()
#app.add_middleware(
#    CORSMiddleware,    
#    allow_origins= "http://localhost:5173/",    
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],    
#)


#@app.post("/uploadfile")
#async def create_upload_file(file: UploadFile = File(...)):
#    dirs = 'uploads'
#    # 判断uploads目录是否存在，否则新建uploads目录
#    if not os.path.exists(dirs):
#        os.makedirs(dirs)
#    # 保存上传文件到uploads目录
#    file_location = f"{dirs}/{file.filename}"
#    with open(file_location, "wb") as file_object:
#        file_object.write(file.file.read())
#    return {"filename": file.filename}




import json
import os
import time
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask,request
#import simplejson

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}},supports_credentials=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 允许最大16MB



UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
filename=''

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    print("backend gets file!")
    if 'file' not in request.files:
        return {"error": "No file part"}, 400

    file = request.files['file']
    if file.filename == '':
        return {"error": "No selected file"}, 400

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return {"filename": filename}

if __name__ == '__main__':
    app.run(debug=True)