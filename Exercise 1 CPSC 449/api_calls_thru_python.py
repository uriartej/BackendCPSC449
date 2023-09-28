import requests

BASE_URL = "http://localhost:8000/api"
GRAPHQL_URL = "http://localhost:4000/graphql"

# ================ Rest API Calls ======================
def get_artist_id(artist_name): # Albums by red hot chili peppers
    endpoint = f"/tables/artists/rows?_search={artist_name.replace(' ', '%20')}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()  
     
    if response.status_code == 200:
        return data['data'][0]['ArtistId']
    return response.status_code

artist_id = get_artist_id("Red Hot Chili Peppers")

def get_albums_by_artist(artist_id):
    endpoint = f"/tables/albums/rows?_filters=ArtistId:{artist_id}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()
    
    album_list = []
    if response.status_code == 200:
        parse = data['data']
        for albums in parse:
            album_list.append(albums['Title'])
        return album_list    
    else:
        return response.status_code       

print(f"Albums by Red Hot Chili Pepper(REST):")
albums = get_albums_by_artist(artist_id)
for album in albums:
    print(album)

def get_artist_id(artist_name): # U2 Genres
    endpoint = f"/tables/artists/rows?_search={artist_name.replace(' ', '%20')}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()  

    if response.status_code == 200 and data['data']:
        return data['data'][0]['ArtistId']
    else:
        return response.status_code

def get_albums_by_artist(artist_id):
    endpoint = f"/tables/albums/rows?_filters=ArtistId:{artist_id}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()
    if response.status_code == 200:
        return data['data']
    else:
        return response.status_code

def get_tracks_by_album(album_id):
    endpoint = f"/tables/tracks/rows?_filters=AlbumId:{album_id}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()
    if response.status_code == 200:
        return data['data']
    else:
        return response.status_code

def get_genre_by_id(genre_id):
    endpoint = f"/tables/genres/rows?_filters=GenreId:{genre_id}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()
    if response.status_code == 200 and data['data']:
        return data['data'][0]['Name']
    else:
        return response.status_code

def get_genres_by_album(album_id):
    tracks = get_tracks_by_album(album_id)
    genre_ids = set([track['GenreId'] for track in tracks if track['GenreId'] is not None])
    genres = [get_genre_by_id(genre_id) for genre_id in genre_ids]
    return genres

def get_all_genres_for_artist(artist_id):
    albums = get_albums_by_artist(artist_id)
    all_genres = []
    for album in albums:
        album_id = album['AlbumId']
        genres = get_genres_by_album(album_id)
        all_genres.extend(genres)
    return set(all_genres)

artist_name = "U2"
artist_id = get_artist_id(artist_name)
albums = get_albums_by_artist(artist_id)

if artist_id:
    unique_genres = get_all_genres_for_artist(artist_id)
    print(f"\nGenres by {artist_name}(REST):")
    for genre in unique_genres:
        print(genre)

def get_playlist_id(playlist_name): # tracks on playlist Grunge and artist/album names
    endpoint = f"/tables/playlists/rows?_search={playlist_name}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()

    if response.status_code == 200:
        return data['data'][0]['PlaylistId']
    else:
        return response.status_code

playlist_id = get_playlist_id("Grunge")

def get_track_ids(playlist_id):
    endpoint = f"/tables/playlist_track/rows?_page=1&_limit=15&_schema=TrackId&_filters=PlaylistId:{playlist_id}"
    response = requests.get(BASE_URL + endpoint)
    data = response.json()

    if response.status_code == 200:
        return data['data']
    else:
        return response.status_code

tracks_id = get_track_ids(playlist_id)

def get_track_titles(tracks_id):
    
    track_title_list = []  
    for track_info in tracks_id:
        endpoint = f"/tables/tracks/rows?_schema=Name,AlbumId&_filters=TrackId:{track_info['TrackId']}"
        response = requests.get(BASE_URL + endpoint)
        data = response.json()

        if response.status_code == 200:
            track_title_list.append(data['data'])        
        else:
            return response.status_code
    return track_title_list

track_info = get_track_titles(tracks_id)

def get_track_info(track_title_list):
    result_list = []
    for track_info in track_title_list:
        album_id = track_info[0]['AlbumId']
        endpoint = f"/tables/albums/rows?_page=1&_limit=10&_schema=Title,ArtistId&_extend=ArtistId&_filters=AlbumId:{album_id}"
        response = requests.get(BASE_URL + endpoint)
        data = response.json()

        if response.status_code == 200:
            list_tuples = [(track_info[0]['Name']), (data['data'][0]['Title']), (data['data'][0]['ArtistId_data']['Name'])]
            result_list.append(list_tuples)    
        else:
            return response.status_code
    return result_list

track_info = get_track_info(track_info)

print('\nNames of tracks on the playlist “Grunge” and their associated artists and albums (REST):')

for tracks in track_info:
    print(f"Track Name: {tracks[0]} Album Name: {tracks[1]} Artist Name: {tracks[2]}")

# ============ GraphQL Queries ================
def get_albums_graphql(artist_name): # albums by red  hot chili peppers
    query = f"""
    {{
      artists(where: {{name: "{artist_name}"}}) {{
        albums {{
          title
        }}
      }}
    }}
    """
    response = requests.post(GRAPHQL_URL, json={'query': query})
    if response.status_code == 200:
        data = response.json()
        return [album['title'] for album in data['data']['artists'][0]['albums']]
    return response.status_code

print(f"\nAlbums by Red Hot Chili Pepper(GraphQL):")

albums_graphql = get_albums_graphql("Red Hot Chili Peppers")
print('\n'.join(albums_graphql))

def get_genres_for_artist(artist_name): # Genres associated with U2
    query = f"""
    query {{
        artist(where: {{name: "{artist_name}"}}) {{
            albums{{
                tracks {{
                    genre {{
                        name
                    }}
                }}
            }}
        }}
    }}
    """
    response = requests.post(GRAPHQL_URL, json={'query': query})
    if response.status_code == 200:
        data = response.json()
        genres = []
        for album in data['data']['artist']['albums']:
            for track in album['tracks']:
                if track['genre']['name'] not in genres:
                    genres.append(track['genre']['name'])
        return genres
    return response.status_code

print("\nGenres associated with U2(GraphQL):")

genres = get_genres_for_artist("U2")
print('\n'.join(genres))

def get_tracks_on_playlist(playlist_name): #Names of tracks on the playlist Grunge and their associated artist and albums
    query = f"""
    query {{
        playlist(where: {{name: "{playlist_name}"}}) {{
            tracks{{
                name
                album {{
                    title
                    artist {{
                        name
                    }}
                }}
            }}
        }}
    }}
    """
    response = requests.post(GRAPHQL_URL, json={'query': query})
    
    if response.status_code == 200:
        data = response.json()
        tracks = []
        for track in data['data']['playlist']['tracks']:
            track_name = track['name']
            album_title = track['album']['title']
            artist_name = track['album']['artist']['name']
            tracks.append((track_name, album_title, artist_name))
        return tracks
    return response.status_code

tracks_info = get_tracks_on_playlist("Grunge")

print("\nNames of tracks on the playlist Grunge and their associated artist and albums(GraphQL):")

for track_name, album_title, artist_name in tracks_info:
    print(f"Track: {track_name}, Album: {album_title}, Artist: {artist_name}")