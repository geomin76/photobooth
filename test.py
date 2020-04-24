import os
from Google import Create_Service
import requests
import pickle

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary','https://www.googleapis.com/auth/photoslibrary.sharing']
service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))
print(token.token)

# body = {
#     "album": {"title": "poop"}
# }

# response_album_poop = service.albums().create(body=body).execute() 

# print(response_album_poop)

# response = service.albums().list(
#     pageSize = 50
# ).execute()

# print(response)

# print(dir(service))

url = "https://photoslibrary.googleapis.com/v1/albums"
myobj = {"album": {
    "title": "fopoker"
}}
x = requests.post(url, json=myobj, headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer " + token.token
    })
print(x)