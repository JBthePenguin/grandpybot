#! /usr/bin/env python3
# coding: utf-8

from flask import Flask, render_template, jsonify, request

# MAIN_DIR = path_dirname(__file__)

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
def index():
    return render_template(
        "index.html",)

@app.route('/api/')
def api():
	# Recovery the client request
	input_user = request.args.get('a', 0, type=str)
	response = "I have received this message : " + input_user
	# Recovery the key words
	input_user = gpb_module.recovery_key_word(input_user)
	# AJAX request with GoogleMap API
	gmaps_module.call_gmaps_api(input_user, app.config["GM_APP_ID"])
	# AJAX request with Wikipedia API
	# Handle the google's return
	# Handle the wiki's return
	# Prepare and send the response for client -> json
	return jsonify(response)


if __name__ == "__main__":
    app.run()
