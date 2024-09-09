from requests import post,get
import json
import helper

def top_tracks (token_h, id):
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    result = get(url, headers = token_h)
    output = result.json()

    n = 1
    surls = []

    for i in output['tracks']:
        time = helper.timer(i['duration_ms'])
        print (f"{n}. {i['name']}: {time} from {i['album']['name']} with {i['popularity']}% popularity.")
        n = n+1
        surls.append(i['uri'])

    helper.asker(surls, "A")
    
    return


def a_search(token_h):
    name = input("Name an artist: ")
    url = "https://api.spotify.com/v1/search"
    query = f"q={name}&type=artist&limit=5"
    qurl = url+"?"+query
    result = get(qurl, headers = token_h)
    output = result.json()

    n = 1

    for i in output['artists']['items']:
        print (f"{n}. {i['name']}: {i['followers']['total']} followers.")
        n = n+1
        
    reply = input("Choose a Singer(1-5)\n(Enter 6 to go back): ")

    while reply != '6':
        if reply in ['1','2','3','4','5']:
            print(f"\nTop Tracks by {output['artists']['items'][int(reply)-1]['name']}:")
            id = output['artists']['items'][int(reply)-1]['id']
            top_tracks(token_h, id)
            return
        
        elif reply!= '6':
            print ("Invalid Input. Try Again.")
        reply = input("Choose a Singer(1-5)\n(Enter 6 to go back): ")
    
    return