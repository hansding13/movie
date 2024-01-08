import requests

url = 'https://mysterious-springs-10746.herokuapp.com/admin/movies/movie/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data:
        print(item)
else:
    print('Error:', response.status_code)