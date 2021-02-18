from sh import Command
from flask import Flask, request, send_file
from tempfile import NamedTemporaryFile

app = Flask(__name__)
flite = Command("/app/flite").bake("-voice", "rms")
ffmpeg = Command("ffmpeg").bake("-y")
SUFFIX = ".ogg"
TEMPR_DIR = "/tmp"

def synthesise_speech(text: str, tempfile):
  with NamedTemporaryFile(suffix=SUFFIX, dir=TEMPR_DIR) as temp_intermediate:
    tempfile_intermediate = temp_intermediate.name
    flite(text, tempfile_intermediate)
    ffmpeg(tempfile, i=tempfile_intermediate)

@app.route('/', methods=['POST'])
def get_speech():
  text = request.json['text']
  with NamedTemporaryFile(suffix=SUFFIX, dir=TEMPR_DIR) as temp:
    tempfile = temp.name
    synthesise_speech(text, tempfile)
    return send_file(tempfile)
