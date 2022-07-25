from main import app
from unittest.mock import Mock
import tmdb_client

def test_get_movies_images():
    expected_default_size = 'w342'
    poster_api_path=""
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url

movie_id=666
def test_get_single_movie():
   movie= tmdb_client.get_single_movie(movie_id=movie_id)
   assert movie

def test_get_single_movie_cast(monkeypatch):
    cast_mock=Mock()
    cast_mock.return_value={'aspect_ratio': 1.778, 'height': 1040, 'iso_639_1': None, 'file_path': '/rL3VEvszvN2hVUjNU2bxa49rbQ4.jpg', 'vote_average': 5.312, 'vote_count': 1, 'width': 1849 , 'cast': 'brad pit'}
    monkeypatch.setattr("tmdb_client.get_single_movie_cast",cast_mock)
    assert "cast" in tmdb_client.get_single_movie_cast(2)
    
def test_get_movies_list(monkeypatch):
    mock_movies_list=['Movie 1', 'Movie 2']
    requests_mock=Mock()
    response=requests_mock.return_value
    response.json.return_value=mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list

def test_random_get_backdrop(monkeypatch):
   back_mock=Mock()
   back_mock.return_value= {'aspect_ratio': 1.778, 'height': 1040, 'iso_639_1': None, 'file_path': '/rL3VEvszvN2hVUjNU2bxa49rbQ4.jpg', 'vote_average': 5.312, 'vote_count': 1, 'width': 1849}
   monkeypatch.setattr("tmdb_client.random_get_backdrop", back_mock)
   assert "file_path" in tmdb_client.random_get_backdrop(movie_id)



