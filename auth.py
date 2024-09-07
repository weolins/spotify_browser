import base64
from requests import post,get


def get_token(client_id, client_secret):
    #Gets the access token from Spotify.
    
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")
    #Encoding the Client ID and Secret in Base 64 to get the token.

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials"}
    result = post(url, headers = headers, data = data)
    #Sending header data to spotify to request a token.

    json_result = result.json()
    token = json_result["access_token"]
    #Converting the token from JSON to dictionary.
    
    return token


def auth_header(token):
    #Makes a header token for searching.
    return {"Authorization": "Bearer "+token}

