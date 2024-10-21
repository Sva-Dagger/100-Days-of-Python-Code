import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="e38d37a43e42460680c36827ed65d6ec",
                                               client_secret="7b24705566b644faaa14a2c9f20655e9",
                                               redirect_uri="http://spotify.com/signup/",
                                               scope="user-library-read"))

user_id = sp.current_user()["id"]
print(user_id)

year = input("Which year do you want to travel to? Type the year in this format YYYY: ")
song_names = ['Achacho - From "Aranmanai 4"', 'Takkunu Takkunu - From "Mr. Local"']

song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(song_uris)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")