from flask import Flask
from flask import render_template, redirect, request, session, url_for
from service import *

app = Flask(__name__)

app.secret_key = "helloworld"


@app.route("/")
def main():
    listAndDeleteImgs()
    return render_template("intro.html")


@app.route("/album", methods=['GET','POST'])
def album():
    name = request.form['name']
    url = "https://photoslibrary.googleapis.com/v1/albums"
    myobj = {"album": {
        "title": name
    }}
    x = requests.post(url, json=myobj, headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + session['tokens'].get('access_token')
        })
    session['username'] = (x.json()['id'])
    return render_template("prePhoto.html", name=name)


# Make sure camera is on!
@app.route("/takePhoto")
def takePhoto():
    killGPhoto2()
    listAndDeleteImgs()
    captureImages()
    files = getImgs()
    return render_template("index.html", files=files)



@app.route("/googleAuth")
def test():
    token = googlePhotosAuth()
    session['tokens'] = {
        'access_token': token
    }
    return render_template("album.html")

@app.route("/prePhotoWithAlbum")
def prePhotoWithAlbum():
    return render_template("prePhotoWithAlbum.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    uploadHelper(session['tokens'].get('access_token'), session['username'])
    return render_template("uploaded.html")


@app.route("/newUser", methods=['GET', 'POST'])
def newUser():
    os.remove('token_photoslibrary_v1.pickle')
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


