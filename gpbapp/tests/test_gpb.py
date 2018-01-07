#! /usr/bin/env python3
# coding: utf-8

import random, string

import googlemaps, wikipedia

from .. import gpb_module, gmaps_module, wiki_module

from .. import views

class TestGpb:
	"""Test for gpb_module"""
	def test_recovery_key_word(self):
		assert gpb_module.recovery_key_word(
			"Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
			) == ["salut", "grandpy", "connais", "adresse", "openclassrooms"]

	def test_handle_gmaps_return(self):
		gmaps_response = {
			"html_attributions": [],
			"results": [{
				"formatted_address": "Paris",
				"geometry": {
					"location": {
						"lat": 48,
						"lng": 2
					},
					"viewport": {
						"northweast": {
							"lat": 58,
							"lng": 3
						},
						"southweast": {
							"lat": 51,
							"lng": 1
						}
					}
				},
				"name": "OpenClassrooms"
			}],
			"status": "OK"
		}
		result = {
			"found" : "YES",
			"response": {
				"name": "OpenClassrooms",
				"address" : "Paris",
				"location" : {
					"lat": 48,
					"lng": 2
				}
			}
		}
		assert gpb_module.handle_gmaps_return(
			gmaps_response) == result
		
		gmaps_response = {
			"html_attributions": [],
			"results": [],
			"status": "ZERO_RESULTS"
		}
		result = {
			"found" : "NO",
			"response": "Bizarre, je ne connais pas ou je n'ai pas compris"
		}
		assert gpb_module.handle_gmaps_return(
			gmaps_response) == result


class TestGmaps:
	"""Test for gmaps_module"""
	def test_make_gmaps_request(self, monkeypatch):
		"""google maps api key valide needed"""
		GM_APP_ID = views.app.config["GM_WEB_APP_ID"]
		results = {"html_attributions": [],
			"results": [{"formatted_address": 'Paris',
				"name": "OpenClassrooms"}],
			"status": "OK"}
		
		def mockreturn(request, *args, **kwargs):
			return results

		monkeypatch.setattr(googlemaps.Client, "places", mockreturn)
		assert gmaps_module.make_gmaps_request(
			["adresse", "openclassrooms"],
			googlemaps.Client(key=GM_APP_ID)
			) == results

	def test_call_gmaps_api(self, monkeypatch):
		"""google maps api key valide needed"""
		GM_APP_ID = views.app.config["GM_WEB_APP_ID"]
		results = {
			"html_attributions": [],
			"results": [],
			"status": "ZERO_RESULTS"
		}
		
		def mockreturn(request, *args, **kwargs):
			return results

		monkeypatch.setattr(googlemaps.Client, "places", mockreturn)
		assert gmaps_module.call_gmaps_api(
			["grandpy"], GM_APP_ID
			) == results


class TestWiki:
	"""Test for wiki_module"""
	def test_call_wiki_api(self, monkeypatch):
		gmaps_result = {
			"found" : "YES",
			"response": {
				"name": "OpenClassrooms",
				"address" : "7 Cité Paradis, 75010 Paris, France",
				"location" : {
					"lat": 48,
					"lng": 2
				} 
			}
		}

		wiki_search_result = ['Cité Paradis', 'Paradis', 'Paris', 'Vanessa Paradis']	
		
		def mocksearchreturn(request):
			return wiki_search_result

		monkeypatch.setattr(wikipedia, "search", mocksearchreturn)

		wiki_summary_result = "La cité Paradis est une voie publique."

		def mocksummaryreturn(request, *args, **kwargs):
			return wiki_summary_result

		monkeypatch.setattr(wikipedia, "summary", mocksummaryreturn)

		response = {
			"found" : "YES",
			"response": {
				"name": "OpenClassrooms",
				"address" : "7 Cité Paradis, 75010 Paris, France",
				"location" : {
					"lat": 48,
					"lng": 2
				},
				"text" : "La cité Paradis est une voie publique."
			}
		}
		
		assert wiki_module.call_wiki_api(gmaps_result) == response

		wiki_search_result = []

		def mocksearchreturn(request):
			return wiki_search_result

		monkeypatch.setattr(wikipedia, "search", mocksearchreturn)

		response = {
			"found" : "YES",
			"response": {
				"name": "OpenClassrooms",
				"address" : "7 Cité Paradis, 75010 Paris, France",
				"location" : {
					"lat": 48,
					"lng": 2
				},
				"text" : "Etrange, je ne me rappelle plus."
			}
		}

		assert wiki_module.call_wiki_api(gmaps_result) == response


		