from tmdb_client import get_movie_images,get_poster_url,get_single_movie,get_movies_list,get_single_movie_cast
from unittest.mock import Mock
def test_get_poster_url_uses_default_size():
    poster_api_path="some-poster-path"
    expected_default_size='w342'
    poster_url=get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_movies_list(monkeypatch):
   # Список, який поверне прихований "запит до API".
   mock_movies_list = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   # Результат запиту до API
   response = requests_mock.return_value
   # Ми перевизначаємо результат виклику методу json().
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_list = get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
   mock_movie = {'adult': False, 
                 'backdrop_path': '/jr8tSoJGj33XLgFBy6lmZhpGQNu.jpg',
                 'belongs_to_collection': {'id': 94602,'name': 'Puss in Boots Collection','poster_path': '/anHwj9IupRoRZZ98WTBvHpTiE6A.jpg','backdrop_path': '/feU1DWV5zMWxXUHJyAIk3dHRQ9c.jpg'},
                 'budget': 90000000, 
                 'genres': [{'id': 16, 'name': 'Animation'}, {'id': 12, 'name': 'Adventure'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}],
                 'homepage': 'https://www.dreamworks.com/movies/puss-in-boots-the-last-wish',
                 'id': 315162, 'imdb_id': 'tt3915174', 'original_language': 'en', 
                 'original_title': 'Puss in Boots: The Last Wish', 
                 'overview': 'Puss in Boots discovers that his passion for adventure has taken its toll: He has burned through eight of his nine lives, leaving him with only one life left. Puss sets out on an epic journey to find the mythical Last Wish and restore his nine lives.', 
                 'popularity': 3180.495, 
                 'poster_path': '/kuf6dutpsT0vSVehic3EZIqkOBt.jpg', 
                 'production_companies': [{'id': 521, 'logo_path': '/kP7t6RwGz2AvvTkvnI1uteEwHet.png', 'name': 'DreamWorks Animation', 'origin_country': 'US'}, {'id': 33, 'logo_path': '/8lvHyhjr8oUKOOy2dKXoALWKdp0.png', 'name': 'Universal Pictures', 'origin_country': 'US'}], 
                 'production_countries': [{'iso_3166_1': 'US', 'name': 'United States of America'}], 
                 'release_date': '2022-12-07', 'revenue': 461000000, 
                 'runtime': 103, 'spoken_languages': [{'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}, {'english_name': 'Spanish', 'iso_639_1': 'es', 'name': 'Español'}], 
                 'status': 'Released', 
                 'tagline': 'Say hola to his little friends.', 
                 'title': 'Puss in Boots: The Last Wish', 
                 'video': False, 
                 'vote_average': 8.4, 'vote_count': 4531}

   requests_mock = Mock()
   # Результат запиту до API
   response = requests_mock.return_value
   # Ми перевизначаємо результат виклику методу json().
   response.json.return_value = mock_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie = get_single_movie(315162)
   assert movie == mock_movie

def test_get_movie_images(monkeypatch):
   mock_movie_id=6
   mock_image_path = f"https://api.themoviedb.org/3/movie/{mock_movie_id}/images"
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_image_path
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_image = get_movie_images(movie_id=mock_movie_id)
   assert mock_image_path in movie_image

def test_get_single_movie_cast(monkeypatch):
   # Підготовка даних
   mock_movie_id=315162
   mock_movie_cast={'adult': False, 'gender': 2, 'id': 3131, 'known_for_department': 'Acting', 'name': 'Antonio Banderas', 'original_name': 'Antonio Banderas', 'popularity': 42.428, 'profile_path': '/n8YlGookYzgD3cmpMP45BYRNIoh.jpg', 'cast_id': 2, 'character': 'Puss in Boots (voice)', 'credit_id': '6052480e197de4006bb47b9a', 'order': 0}
   
   requests_mock = Mock()
   # Результат запиту до API
   response = requests_mock.return_value
   # Ми перевизначаємо результат виклику методу json().
   response.json.return_value = mock_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   # Виклик коду, який ми те
   movie_cast = get_single_movie_cast(movie_id=mock_movie_id)
   assert movie_cast == mock_movie_cast
   

