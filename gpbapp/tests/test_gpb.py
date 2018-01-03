#! /usr/bin/env python3
# coding: utf-8

import random, string

import googlemaps

from .. import gpb_module, gmaps_module

from .. import views

class TestGpb:
	"""Test for gpb_module"""
	def test_recovery_key_word(self):
		assert gpb_module.recovery_key_word(
			"Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
			) == ["salut", "grandpy", "connais", "adresse", "openclassrooms"]


class TestGmaps:
	"""Test for gmaps_module"""
	def test_call_gmaps_api(self, monkeypatch):
		"""google maps api key valide needed"""
		GM_APP_ID = views.app.config["GM_APP_ID"]
		results = {"html_attributions": [],
			"results": [{"formated_address": 'Paris',
				"name": "OpenClassrooms"}],
			"status": "OK"}
		
		def mockreturn(request, *args, **kwargs):
			return results

		monkeypatch.setattr(googlemaps.Client, "places", mockreturn)
		assert gmaps_module.call_gmaps_api(
			["adresse", "openclassrooms"], GM_APP_ID) == results

		results = {"html_attributions": [],
			"results": [],
			"status": "ZERO_RESULTS"}
		monkeypatch.setattr(googlemaps.Client, "places", mockreturn)
		assert gmaps_module.call_gmaps_api(
			["grandpy"], GM_APP_ID) == results
