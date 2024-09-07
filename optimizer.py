from dotenv import load_dotenv as loader
import os
import base64
from requests import post,get
import json
import auth, helper, artist_search, song

loader()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def main():
    token = auth.get_token(client_id, client_secret)
    header = auth.auth_header(token)
    
    print("\nWhat do you want to do?\n1.Search for Artists\n2.Search for Songs\n3.Exit.")

    console = input("> ")
    
    while console != '3':
        if console == "1":
            searchy = artist_search.a_search(header)
        elif console == "2":
            searchy = song.songsearch(header)
        else:
            print ("Invalid Input. Try Again.")
        print("\nWhat do you want to do?\n1.Search for Artists\n2.Search for Songs\n3.Exit.")
        console = input("> ")


if __name__ == "__main__":
    main()