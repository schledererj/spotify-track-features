"""
Use this file to generate an access token for use in Spotipy's `client` constructor's `auth` argument.
You'll need to log into Spotify's web API dashboard, create an application, replace the client ID on line 14 with your own,
and set the client secret in the SPOTIPY_CLIENT_SECRET environment variable (keep it out of the code to reduce
the chances of accidentally committing it to git). From there, make sure port 8000 is open locally, as the
library will automagically spin up a tiny web server to receive the OAuth callback on that port. This code
simply prints out the access token which you can then paste into the accompanying ipynb file.
"""

from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify

# Generate this in the Spotify API dashboard
sp_client_id = "ed87ed465cfd4ccb814aeb8af5deb9a5"
# sp_client_secret = "" # Use environment variable SPOTIPY_CLIENT_SECRET to store this securely

scopes = ["user-read-private", "user-library-read",
          "user-top-read", "user-read-recently-played"]
oauth = SpotifyOAuth(
    sp_client_id, redirect_uri="http://localhost:8000", scope=scopes)

sp = Spotify(auth_manager=oauth)
access_token = sp.auth_manager.get_access_token(as_dict=False)
print(f"Access token: {access_token}")
