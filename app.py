# flask --app app.py --debug run
import os

from flask import Flask, render_template,request, redirect,url_for,session
import requests

import json
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')

if not bearer_token:
    raise ValueError("Bearer Token not found in the .env file.")




app = Flask(__name__)


@app.route('/') 
def index(): 
    
    url = "https://api.themoviedb.org/3/search/movie?query=spiderman"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    response = requests.get(url, headers=headers)

    res = json.loads(response.text)
    print("RES: ", res['results'])
    return render_template('index.html')

@app.route('/mylist') 
def mylist(): 
    return render_template('test1.html')


@app.route("/random")
def random():
    return  "Something"



