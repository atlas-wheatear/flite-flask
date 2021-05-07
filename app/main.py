from sh import Command
from flask import Flask, request, jsonify
from tempfile import NamedTemporaryFile
import requests
import os
from json import loads

app = Flask(__name__)
flite = Command("/app/flite").bake("-voice", "rms").bake("-t")
ffmpeg = Command("ffmpeg").bake("-y")
SUFFIX = ".ogg"
TEMP_DIR = "/tmp"
upload_url = "http://" + os.environ["UPLOAD_SERVER"] + ":" + os.environ["UPLOAD_PORT"]


def synthesise_speech(text: str, tempfile: str):
  with NamedTemporaryFile(suffix=SUFFIX, dir=TEMP_DIR) as temp_intermediate:
    tempfile_intermediate = temp_intermediate.name
    flite(text, tempfile_intermediate)
    ffmpeg(tempfile, i=tempfile_intermediate)

def upload_ogg(tempfile: str) -> str:
    files = {'ogg': open(tempfile, 'rb')}
    response = requests.post(upload_url, files=files)
    print(response.text)
    return loads(response.text)

@app.route('/', methods=['POST'])
def get_speech():
  text = request.json['text']
  with NamedTemporaryFile(suffix=SUFFIX, dir=TEMP_DIR) as temp:
    tempfile = temp.name
    synthesise_speech(text, tempfile)
    response = upload_ogg(tempfile)
  return jsonify(response)
