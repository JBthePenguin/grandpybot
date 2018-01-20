#! /usr/bin/env python3
# coding: utf-8

"""Tests of all app's functions """

# pylint: disable=unused-argument

import googlemaps
import wikipedia
from .. import gpb_module, gmaps_module, wiki_module
from .. import views


class TestGpb:
    """Test for gpb_module"""
    @staticmethod
    def test_recovery_key_word():
        """Test str -> list of words without stop words
        and non alphanumeric characters"""
        assert gpb_module.recovery_key_word(
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
            ) == ["salut", "grandpy", "connais", "adresse", "openclassrooms"]

    @staticmethod
    def test_handle_gmaps_return():
        """ Test gmap's api result -> response for client """
        # example of gmaps'api result
        gmaps_response = {
            "html_attributions": [],
            "results": [{
                "formatted_address": "Paris",
                "geometry": {
                    "location": {
                        "lat": 48.51,
                        "lng": 2.51
                    },
                    "viewport": {
                        "northweast": {
                            "lat": 58.51,
                            "lng": 3.25
                        },
                        "southweast": {
                            "lat": 51,
                            "lng": 1.6
                        }
                    }
                },
                "name": "OpenClassrooms"
            }],
            "status": "OK"
        }
        # example of response for client
        result = {
            "found" : "YES",
            "response": {
                "name": "OpenClassrooms",
                "address" : "Paris",
                "location" : {
                    "lat": 48.51,
                    "lng": 2.51
                }
            }
        }
        # assert that gmap's result -> response
        assert gpb_module.handle_gmaps_return(
            gmaps_response) == result

        # Test if zero result from gmap's api
        gmaps_response = {
            "html_attributions": [],
            "results": [],
            "status": "ZERO_RESULTS"
        }
        result = {
            "found" : "NO",
            "response": "Bizarre, je ne connais pas ou je n'ai pas compris"
        }
        # assert that gmap's result -> response
        assert gpb_module.handle_gmaps_return(
            gmaps_response) == result


class TestGmaps:
    """Test for gmaps_module"""
    # google maps api key valide needed
    GM_API_ID = views.APP.config["GM_WEB_APP_ID"]
    def test_make_gmaps_request(self, monkeypatch):
        """Test return the result Google Maps API"""
        # set the result for the request
        result = {
            "html_attributions": [],
            "results": [{"formatted_address": 'Paris', "name": "OpenClassrooms"}],
            "status": "OK"
        }

        def mockreturn(query, *args, **kwargs):
            """ mock the result """
            return result

        monkeypatch.setattr(googlemaps.Client, "places", mockreturn)
        # assert that make_gmaps_request return the result
        assert gmaps_module.make_gmaps_request(
            ["adresse", "openclassrooms"],
            googlemaps.Client(key=self.GM_API_ID)
            ) == result

    def test_call_gmaps_api(self, monkeypatch):
        """Test return the result Google Maps API after one or more calls"""
        # set this result for the request
        result = {
            "html_attributions": [],
            "results": [],
            "status": "ZERO_RESULTS"
        }

        def mockreturn(query, *args, **kwargs):
            """ mock the result """
            return result

        monkeypatch.setattr(googlemaps.Client, "places", mockreturn)
        # assert that call_gmaps_api return the result
        assert gmaps_module.call_gmaps_api(
            ["grandpy"], self.GM_API_ID
            ) == result


class TestWiki:
    """Test for wiki_module
    wiki's api result -> response for client"""
    # example of handle_gmaps_return result
    handle_gmaps_return_result = {
        "found" : "YES",
        "response": {
            "name": "OpenClassrooms",
            "address" : "7 Cité Paradis, 75010 Paris, France",
            "location" : {
                "lat": 48.51,
                "lng": 2.51
            }
        }
    }
    new_response = handle_gmaps_return_result["response"]
    response = handle_gmaps_return_result

    def test_call_wiki_api_result_ok(self, monkeypatch):
        """ Test with a wiki's api result """
        # mset this result for the first request -> list of titles
        wiki_search_result = ['Cité Paradis', 'Paradis', 'Paris', 'Vanessa Paradis']

        def mocksearchreturn(request):
            """ mock the result """
            return wiki_search_result

        monkeypatch.setattr(wikipedia, "search", mocksearchreturn)
        # mock this result for the second request -> summary
        wiki_summary_result = "La cité Paradis est une voie publique."

        def mocksummaryreturn(request, *args, **kwargs):
            """ mock the result """
            return wiki_summary_result

        monkeypatch.setattr(wikipedia, "summary", mocksummaryreturn)
        # example of response for client
        self.new_response["text"] = "La cité Paradis est une voie publique."
        self.response["response"] = self.new_response
        # assert text add to response
        assert wiki_module.call_wiki_api(
            self.handle_gmaps_return_result) == self.response

    def test_call_wiki_api_no_result(self, monkeypatch):
        """ Test if zero result from wiki's api """
        # mock this result for the first request -> list of titles
        wiki_search_result = []

        def mocksearchreturn(request):
            """ mock the result """
            return wiki_search_result

        monkeypatch.setattr(wikipedia, "search", mocksearchreturn)
        # example of response for client
        self.new_response["text"] = "Etrange, je ne me rappelle plus."
        self.response["response"] = self.new_response
        # assert text add to response
        assert wiki_module.call_wiki_api(
            self.handle_gmaps_return_result) == self.response
