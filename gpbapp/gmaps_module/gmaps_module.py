#! /usr/bin/env python3
# coding: utf-8

import googlemaps


def make_request(list_words, gmaps):
	""" make a request to google maps api with googlemaps module"""
	query = ""
	for word in list_words:
		query += (word + " ")
	places_result = gmaps.places(
		query, location=(48, 2), radius=50000, language="fr")
	return places_result


def call_gmaps_api(list_words, GM_APP_ID):
	""" call google maps api with all words,
	if no result, try with less one,...
	and resturn the result"""
	gmaps = googlemaps.Client(key=GM_APP_ID)
	places_result = make_request(list_words, gmaps)

	if places_result["status"] == "OK": 
		return places_result
	elif places_result["status"] == 'ZERO_RESULTS':
		i = 1
		while i < len(list_words):
			ind = 0
			len_new_list = len(list_words) - i
			while (places_result["status"] == 'ZERO_RESULTS') and (
				ind <= i):
				new_list_words = list_words[ind:((len_new_list-1)+ind)]
				places_result = make_request(new_list_words, gmaps)
				ind += 1
			if places_result["status"] == "OK": 
				return places_result
			i +=1
		return places_result 
			
