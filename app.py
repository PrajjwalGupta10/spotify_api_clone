from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Spotify API credentials
CLIENT_ID = '4983fc79946145399da8526d084d437d'
CLIENT_SECRET = 'a914949f612c4cf1accaeea5ff65f920'

# Function to get Spotify access token
def get_access_token():
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET}
    response = requests.post(url, headers=headers, data=data)
    return response.json()['access_token']

# Function to search for songs
def search_songs(query):
    token = get_access_token()
    url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'q': query, 'type': 'track', 'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    return response.json()['tracks']['items']

@app.route('/', methods=['GET', 'POST'])
def index():
    songs = []
    query = ""
    if request.method == 'POST':
        query = request.form.get('query')
        songs = search_songs(query)
    return render_template('index.html', songs=songs, query=query)

if __name__ == '__main__':
    app.run(debug=True)


# 44.226.145.213
# 54.187.200.255
# 34.213.214.55
# 35.164.95.156
# 44.230.95.183
# 44.229.200.200