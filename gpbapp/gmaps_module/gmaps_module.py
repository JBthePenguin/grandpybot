#! /usr/bin/env python3
# coding: utf-8

""" this module is using to call GoogleMaps API """

import googlemaps


def make_gmaps_request(list_words, gmaps):
    """ make a request to google maps api with googlemaps module"""
    query = ""
    # Transform list_words(list) in query(str)
    for word in list_words:
        query += (word + " ")
    # make request
    places_result = gmaps.places(
        query, location=(48, 2), radius=50000, language="fr")
    return places_result


def call_gmaps_api(list_words, gm_web_app_id):
    """ call google maps api with all words,
    if no result, try with less one,...
    and resturn the result"""
    gmaps = googlemaps.Client(key=gm_web_app_id)
    # 1st request
    places_result = make_gmaps_request(list_words, gmaps)
    if places_result["status"] == 'ZERO_RESULTS':
        # if no result
        i = 1
        while i < len(list_words):
            # try with one less word...
            ind = 0
            len_new_list = len(list_words) - i
            while (places_result["status"] == 'ZERO_RESULTS') and (ind <= i):
                # try again with a new list
                new_list_words = list_words[ind:((len_new_list)+ind)]
                places_result = make_gmaps_request(new_list_words, gmaps)
                ind += 1
            if places_result["status"] == "OK":
                return places_result
            i += 1
    return places_result
