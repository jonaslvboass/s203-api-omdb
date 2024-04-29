import json
import os

from dotenv import load_dotenv
from flask import Flask, request
import requests

load_dotenv()

API_KEY = os.environ.get('OMDB_API_KEY')

app = Flask(__name__)

@app.route('/')
def hello():
    return json.dumps({"msg":"Everything's fine!"})

@app.route('/get_movies', methods=["GET"])
def get_movies():
    query = 'http://www.omdbapi.com/?apikey='+API_KEY
    if 'title' in request.args:
        title = request.args.get("title")
        query += '&t='+title
    else:
        return json.dumps({"msg":"Need type something..."})
    if 'year' in request.args:
        year = request.args.get("year")
        query += '&y='+year
    if 'page' in request.args:
        page = request.args.get("page")
        query += '&page='+page
    movies = requests.get(query).json()
    movies["msg"] = "OK"
    return movies