import subprocess
from flask import Flask, request, send_file
from tempfile import NamedTemporaryFile

app = Flask(__name__)

def build_speech(text, tempfile):
  # build the wav
  command = '/flite/flite "%s" %s' % (text, tempfile)
  subprocess.call(command, shell=True)

@app.route('/', methods=['POST'])
def get_speech():
  text = request.json['text']
  with NamedTemporaryFile(suffix='.wav', dir="/tmp") as temp:
    tempfile = temp.name
    build_speech(text, tempfile)
    return send_file(tempfile)
