from sh import Command
from flask import Flask, request, send_file
from tempfile import NamedTemporaryFile

app = Flask(__name__)
flite = Command("/flite/flite")

@app.route('/', methods=['POST'])
def get_speech():
  text = request.json['text']
  with NamedTemporaryFile(suffix='.wav', dir="/tmp") as temp:
    tempfile = temp.name
    flite(text, tempfile)
    return send_file(tempfile)
