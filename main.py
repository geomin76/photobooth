from flask import Flask
from flask import render_template, redirect, request
from service import *

app = Flask(__name__)

@app.route("/")
def main():
    listAndDeleteImgs()
    return render_template("intro.html")

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

@app.route("/test")
def test():
    return googlePhotosAuth()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


