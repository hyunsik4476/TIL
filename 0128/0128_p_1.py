import requests

# https://developers.themoviedb.org/3/movies/get-popular-movies
BASE_URL = 'https://api.themoviedb.org.3'
path = '/movie/now_playing'
params = {
    'api_key': '94408b8ba77aeba1e34e9ce31795cc76',
    'region': 'KR',
    'language': 'ko'
}
# https://api.themoviedb.org.3/movie/now_playing?api_key=94408b8ba77aeba1e34e9ce31795cc76&region=KR&language=ko

response = requests.get(BASE_URL+path, params = params)
print(response.status_code, response.url)
data = response.json()
