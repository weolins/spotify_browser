from requests import post,get
import json
import helper

def songsearch(token_h):
    name = input("Name a song: ")
    url = "https://api.spotify.com/v1/search"
    query = f"q={name}&type=track&limit=5"
    qurl = url+"?"+query
    result = get(qurl, headers = token_h)
    output = result.json()

    surls = []

    n = 1
    for i in output['tracks']['items']:
        print(f"{n}.{i['name']} by {i['artists'][0]['name']} ({helper.timer(i['duration_ms'])}) with {i['popularity']}% popularity.")
        n+=1
        surls.append(i['external_urls']['spotify'])
        
    helper.asker(surls, "S")
    
    return
