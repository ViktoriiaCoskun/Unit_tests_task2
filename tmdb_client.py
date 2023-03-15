import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNDUxMzkzOGI0YTQwYjI5ZGZmODEzYTE2NThlM2E0OCIsInN1YiI6IjYzZTVhZTJlZjQ4YjM0MDBiYzk3OTkwZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Z3TGNx4Or6naLpetl6HWkLVuzEj_nlb0zlNzJP0kx7Q"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
   # api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNDUxMzkzOGI0YTQwYjI5ZGZmODEzYTE2NThlM2E0OCIsInN1YiI6IjYzZTVhZTJlZjQ4YjM0MDBiYzk3OTkwZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Z3TGNx4Or6naLpetl6HWkLVuzEj_nlb0zlNzJP0kx7Q"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies(how_many,list_type):
    list_types=["popular","top_rated","upcoming","now_playing"]
    if list_type not in list_types:
      list_type = "popular"
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def search(search_query):
   base_url = "https://api.themoviedb.org/3/"
   api_token = API_TOKEN
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   endpoint = f"{base_url}search/movie/?query={search_query}"

   response = requests.get(endpoint, headers=headers)
   print(response)
   response = response.json()
   return response['results']

def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']

def call_tmdb_api(endpoint):
    full_url=f"https://api.themoviedb.org/3/{endpoint}"
    headers={"Authorization":f"Bearer{API_TOKEN}"}
    response=requests.get(full_url,headers=headers)
    response.raise_for_status()
    return response.json()