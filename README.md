# grandpybot

## the grandpa robot

### How to run?

#### 1.Download the directory grandpybot

#### 2.Go inside:
`cd grandpybot`

#### 3.Create a virtual environment for python with virtualenv (!!!maybe you have to install virtualenv!!!)
`virtualenv -p python3 env`

#### 4.Use it
`source env/bin/activate`

#### 5.Install requirements with Pip (!!!maybe you have to install it!!!):
`pip install Flask googlemaps wikipedia` 
or
`pip install -r requirements.txt`
  
#### 6.a Run tests:
```
pip install pytest
pytest
```
#### 6.b Run app:
`python run.py`

### Now, with your favorite browser, go to this url:
127.0.0.1:5000

##### notes:
###### You need valide keys for GoogleMaps APIs("WEB" and "JS") and write them in config.py
###### This is command for Linux users, to adapt according to the used system.
