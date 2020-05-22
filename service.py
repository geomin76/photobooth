import gphoto2 as gp
import signal, os, subprocess, sys
from time import sleep
import requests
from Google import Create_Service
import pickle



# Kill the gphoto2 process whenever we turn on the camera or reboot the Raspberry Pi
def killGPhoto2():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()

    #find the "gvfsd-gphoto2" process to kill
    for line in out.splitlines():
        if b'gvfsd-gphoto2' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)
            print("Killed process " + str(pid) + " gvfsd-gphoto2")

def captureImages():
    camera = gp.Camera()
    camera.init()
    print('Capturing Image')
    for x in range(0, 3):
        file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
        # print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join('./static', file_path.name)
        camera_file = camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
        camera_file.save(target)
        print("Taken and saved img " + file_path.name)

    # this opens up the img in a photoviewer
    # subprocess.call(['xdg-open', target])
    camera.exit()

def getImgs():
    files = os.listdir("./static")
    filesList = []
    for content in files:
        filesList.append("/static/" + str(content))
    return filesList


def listAndDeleteImgs():
    files = os.listdir("./static")
    for content in files:
        os.remove("./static/" + str(content))
        print("deleted " + str(content))


def cameraInfo():
    camera = gp.Camera()
    camera.init()
    text = camera.get_summary()
    print('Summary')
    print(str(text))
    camera.exit()

def googlePhotosAuth():
    API_NAME = 'photoslibrary'
    API_VERSION = 'v1'
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/photoslibrary','https://www.googleapis.com/auth/photoslibrary.sharing']
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    token = pickle.load(open('token_photoslibrary_v1.pickle', 'rb'))
    return token.token


def upload_image(image_path, upload_file_name, token):
    upload_url = 'https://photoslibrary.googleapis.com/v1/uploads'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-type': 'application/octet-stream',
        'X-Goog-Upload-Protocol': 'raw',
        'X-Goog-File-Name': upload_file_name
    }

    img = open(image_path, 'rb').read()
    response = requests.post(upload_url, data=img, headers=headers)
    return response


def uploadHelper(token):
    files = os.listdir("./static")
    tokens = []
    image_dir = os.path.join(os.getcwd(), 'static')
    for content in files:
        print(content) 
        image_file = os.path.join(image_dir, content)
        response = upload_image(image_file, content, token)
        tokens.append(response.content.decode('utf-8'))
    new_media_items = [{'simpleMediaItem': {'uploadToken': tok}}for tok in tokens]
    request_body = {
        'newMediaItems': new_media_items
    }


    API_NAME = 'photoslibrary'
    API_VERSION = 'v1'
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/photoslibrary','https://www.googleapis.com/auth/photoslibrary.sharing']
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

    upload_response = service.mediaItems().batchCreate(body=request_body).execute()


def getAlbums():
    API_NAME = 'photoslibrary'
    API_VERSION = 'v1'
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/photoslibrary','https://www.googleapis.com/auth/photoslibrary.sharing']
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

    album_response = service.albums().list(pageSize=50, excludeNonAppCreatedData=False).execute()

    listAlbums = album_response.get('albums')
    # print(len(listAlbums))
    # print(listAlbums[len(listAlbums) - 1])
    new_list = []
    nextPageToken = album_response.get('nextPageToken')
    while nextPageToken:
        response = service.albums().list(pageSize=50, excludeNonAppCreatedData=False, pageToken=nextPageToken).execute()
        new_list.append(response.get('albums'))
        nextPageToken = response.get('nextPageToken')
