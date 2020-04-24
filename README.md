# photobooth

Creating a photo booth with Raspberry Pi 4 Model B + Python/Flask

### Setup
Installing Flask
- $ `pip install Flask`

Installing and setting up gphoto2 for Python
- `$ sudo pip install -v gphoto2`

Installing and setting up Google Photos API
- `$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

Installing and setting up gphoto2 + libgphoto2 for terminal
- `$ sudo apt-get install libltdl-dev libusb-dev libusb-1.0 libexif-dev libpopt-dev`
- `$ wget http://downloads.sourceforge.net/project/gphoto/libgphoto/2.5.7/libgphoto2-2.5.7.tar.gz`
- `$ wget http://downloads.sourceforge.net/project/gphoto/gphoto/2.5.6/gphoto2-2.5.6.tar.gz`

Installing libgphoto2

- `$ tar -xvzf libgphoto2-2.5.7.tar.gz`
- `$ cd libgphoto2-2.5.7`
- `$ ./configure`
- `$ make` (this may take a while)
- `$ sudo make install`

Installing gphoto2

- `$ tar -xvzf gphoto2-2.5.6.tar.gz`
- `$ cd gphoto2-2.5.6`
- `$ ./configure`
- `$ make`
- `$ sudo make install`

If successful, you can run `$ gphoto2 --auto-detect` and it should pull up this:
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
