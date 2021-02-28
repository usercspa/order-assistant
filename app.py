import os 
from flask import Flask, request, redirect, render_template 

import speech recognition as sr 

app = Flask(__name__)

@app.route("/", methods=[]"GET")

def index():
  retuen "hi"

  if __name__ == "__main__" :
    app.run(debug=TRUE, threaded=TRUE)  