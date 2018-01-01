#! /usr/bin/env python3
# coding: utf-8

from flask import Flask, render_template, jsonify, request


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
	input_user = request.args.get('a', 0, type=str)
	response = "I have received this message : " + input_user
	return jsonify(response)


if __name__ == "__main__":
    app.run()
