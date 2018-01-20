#! /usr/bin/env python3
# coding: utf-8

""" All app's routes """

from flask import Flask, render_template, jsonify, request

from .gpb_module import recovery_key_word, handle_gmaps_return
from .gmaps_module import call_gmaps_api
from .wiki_module import call_wiki_api

APP = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
APP.config.from_object('config')
# To get one variable, tape APP.config['MY_VARIABLE']


@APP.route('/')
def index():
    """ return the main page """
    return render_template(
        "index.html", GM_JS_APP_ID=APP.config["GM_JS_APP_ID"])


@APP.route('/api/')
def api():
    """ Vérify if the request's key is OK
    Call Google Maps and MediaWiki APIs
    Return a result """
    # Recovery the client request
    input_user = request.args.get('a', 0, type=str)
    if input_user == 0:
        # if key is incorrect
        response = {
            "found" : "NO",
            "response": "Ce n'est pas sympa de vouloir profiter des faiblesses d'un vieillard !!!"
        }
    else:
        # Recovery the key words
        input_user = recovery_key_word(input_user)
        # AJAX request with GoogleMap API
        response = call_gmaps_api(input_user, APP.config["GM_WEB_APP_ID"])
        # Handle the google's return
        response = handle_gmaps_return(response)
        # If there is a return:
        if response["found"] == "YES":
            # AJAX request with Wikipedia API
            # and handle the wiki's return
            response = call_wiki_api(response)
    # send the response for client -> json
    return jsonify(response)


if __name__ == "__main__":
    APP.run()
