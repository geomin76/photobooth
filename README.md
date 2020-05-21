# photobooth

Creating a photo booth with Raspberry Pi 4 Model B + Python/Flask

### Setup
Here's how to setup and run photobooth
- `$ git clone https://github.com/geomin76/photobooth.git`
- `$ cd photobooth`

To set up the virtual environment
- `$ python3 -m venv venv`
- `$ virtualenv venv`
- `$ source venv/bin/activate`

To now install dependencies:
- `$ pip install requests`
- `$ pip install Flask`
- `$ sudo apt-get install libltdl-dev libusb-dev libusb-1.0 libexif-dev libpopt-dev`
- `$ sudo apt install gphoto2 libgphoto2-dev`
- `$ pip install gphoto2`
- `$ pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

Create a directory called `static`, this is where the photos taken will be stored
- `$ mkdir static`

Now Google Photos API setup:
- Check out this YouTube tutorial on how to get your client secret [here](https://youtu.be/dkxcd2Q3Qwo?t=393)
- Once you have downloaded the client secret, rename it to `client_secret.json` and move it to this directory

Now to run the application! Run `$ python main.py` and begin the authentication!

After you click the button "let's begin," check your terminal! You should see a `Please visit this URL to authorize this application:`. Visit this URL to get Google Photos authentication.

If authentication is successful, you should see a file called `token_photoslibrary_v1.pickle` in your directory. This is your "pickle" file that gives you Google Photos access! If you delete the pickle, you'll have to go through authentication again!

And after that, your app is ready to roll! You can create an album, take photos and they'll show up in your Google Photos album you created!

Cheers!

(Don't forget to set up your camera with the settings you want, in manual focus, and leave your camera "on" forever so it doesn't sleep)

<br/>
<br/>
<br/>
<br/>

If successful on gphoto2 installation, you can run `$ gphoto2 --auto-detect` and it should pull up this:
~~~
Model                          Port                                            
----------------------------------------------------------
~~~

You can plug in your camera to the Raspberry Pi and run `$ gphoto2 --auto-detect` and you will see your camera listed like this:
~~~
Model                          Port                                            
----------------------------------------------------------
Canon EOS 5D Mark II           usb:001,005   
~~~

You can check if your camera is compatible with gphoto2 [here](http://gphoto.org/doc/remote/)

You can check out the gphoto2 capabilities [here](http://gphoto.org/doc/manual/ref-gphoto2-cli.html)
