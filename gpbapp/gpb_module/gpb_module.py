#! /usr/bin/env python3
# coding: utf-8

import json, re


def recovery_key_word(input_user):
	""" make a list of words without stop words"""
	# remove  all non alphanumeric characters before listing
	input_user = re.sub(r"\W+", " ", input_user).lower()
	input_user = input_user.split(" ")
	if '' in input_user:
		input_user.remove('')
	# remove stop words
	with open("gpbapp/static/json/stop_words_fr.json") as stop_words:
		stop_words_dict = json.load(stop_words)
	for word in stop_words_dict:
		if word in input_user:
			input_user.remove(word)
	return input_user
	