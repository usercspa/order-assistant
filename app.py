import os 
from flask import Flask, request, redirect, render_template 

import speech recognition as sr 

app = Flask(__name__)

@app.route("/", methods=[]"GET")

def index():
  retuen render_template('index.html')

  if __name__ == "__main__" :
    app.run(debug=True, threaded=True)  