from flask import Flask
from flask import render_template, redirect, request, session, url_for
from service import *

app = Flask(__name__)

app.secret_key = "helloworld"

@app.route("/")
def main():
    listAndDeleteImgs()
    return render_template("intro.html")

@app.route("/album")
def album():
    url = "https://photoslibrary.googleapis.com/v1/albums"
    myobj = {"album": {
        "title": "test"
    }}
    x = requests.post(url, json=myobj, headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + session['tokens'].get('access_token')
        })
    return render_template("album.html")


# Make sure camera is on!
@app.route("/takePhoto")
def takePhoto():
    killGPhoto2()
    listAndDeleteImgs()
    captureImages()
    files = getImgs()
    return render_template("index.html", files=files)


@app.route("/emailPhoto", methods=['GET', 'POST'])
def emailPhoto():
    email = request.form['email'] 
    listAndDeleteImgs()
    return redirect("/")


@app.route("/googleAuth")
def test():
    token = googlePhotosAuth()
    session['tokens'] = {
        'access_token': token
    }
    return redirect(url_for('album'))


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


