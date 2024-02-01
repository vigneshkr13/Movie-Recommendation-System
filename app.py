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
app.secret_key = 'Vk'

@app.route('/', methods=['GET']) 
def index(): 

    # This code section is to get the request the movie list directly from notebook.
    # top_movies = request.args.getlist('top_movies')
    # top_movies = session.get('top_movies', [])
    # print("Top Movies: ",top_movies)

    # url = "https://api.themoviedb.org/3/search/movie?query=spiderman"

    # headers = {
    #     "accept": "application/json",
    #     "Authorization": f"Bearer {bearer_token}"   
    # }

    # response = requests.get(url, headers=headers)
    
    # res = json.loads(response.text)
    # print("RES: ", res['results'][0])

    # top_movies = request.args.getlist('top_movies')
    # print("Top Movies: ",top_movies)


    # Popular Movies
    popular_movie_file_path = "./top_movies_list.txt"

    with open(popular_movie_file_path, 'r') as f:
        pop_movies = [line.strip() for line in f]

    # print("Top Movies: ",pop_movies)
    pop_movie_details = []

    for movie_title in pop_movies:
        
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {bearer_token}"   
        }
        
        
        response = requests.get(url, headers=headers)
        
        
        res = json.loads(response.text)
        
        
        if res.get('results'):
            pop_movie_details.append({
                'title': res['results'][0]['title'],
                'poster_path': res['results'][0]['poster_path']
            })
        
        
    # print(pop_movie_details)

    # Recommended Movies - User Item Recommendation
    recommended_movie_file_path = './user_recommendations.txt'

    with open(recommended_movie_file_path, 'r') as f:
        rec_movies = f.readlines()[1]

    rec_movies = rec_movies.split('|')
    for i in range(len(rec_movies)):
        rec_movies[i] = rec_movies[i][:-6]

    print("Recommended Movies: ",rec_movies)
    rec_movie_details = []

    for movie_title in rec_movies:
        
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {bearer_token}"   
        }
        
        
        response = requests.get(url, headers=headers)
        
        
        res_rec_mov = json.loads(response.text)
        
        # print(res_rec_mov)
        if res_rec_mov.get('results'):
            rec_movie_details.append({
                'title': res_rec_mov['results'][0]['title'],
                'poster_path': res_rec_mov['results'][0]['poster_path']
            })
        
        

    print(rec_movie_details)


     # Recommended Movies - Item Item Recommendation
    item_rec_movie_file_path = './item_item_recommendations.txt'

    with open(item_rec_movie_file_path, 'r') as f:
        item_rec_movies = f.readlines()[1]

    item_rec_movies = item_rec_movies.split('|')
    for i in range(len(item_rec_movies)):
        item_rec_movies[i] = item_rec_movies[i][:-6]

    print("Recommended Movies: ",item_rec_movies)
    rec_item_item_movie_details = []

    for movie_title in item_rec_movies:
        
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {bearer_token}"   
        }
        
        
        response = requests.get(url, headers=headers)
        
        
        res_item_mov = json.loads(response.text)
        
        # print(res_rec_mov)
        if res_item_mov.get('results'):
            rec_item_item_movie_details.append({
                'title': res_item_mov['results'][0]['title'],
                'poster_path': res_item_mov['results'][0]['poster_path']
            })
        
        

    print(rec_item_item_movie_details)


    return render_template('index.html', movie_details=pop_movie_details, rec_movie_details = rec_movie_details, rec_item_item_movie_details = rec_item_item_movie_details)

@app.route('/mylist') 
def mylist(): 
    return render_template('test1.html')


@app.route("/random")
def random():
    return  "Something"


@app.route('/movie_detail')
def movie_detail():
  
    return render_template('movie_detail.html')


