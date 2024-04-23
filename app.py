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

@app.route('/get_movie', methods=["GET"])
def get_movies():
    title = request.args.get("title")
    year = request.args.get("year")
    movies = requests.get(f'http://www.omdbapi.com/?apikey='+API_KEY+'&t={title}&y={year}').json()
    return movies