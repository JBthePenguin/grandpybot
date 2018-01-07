#! /usr/bin/env python3
# coding: utf-8

import wikipedia

def call_wiki_api(gmaps_result):
	"""search the title of wiki page
	and found the summary if there is a result""" 
	response = gmaps_result["response"]
	address = response["address"]
	"""remove number"""
	wiki_search =  ''.join([i for i in address if not i.isdigit()])
	wikipedia.set_lang("fr")
	list_results = wikipedia.search(wiki_search)
	if list_results == []:
		text = "Etrange, je ne me rappelle plus."
	else:
		title_page = list_results[0]
		text = wikipedia.summary(title_page, sentences=1)

	response["text"] = text
	final_result = gmaps_result
	final_result["response"] = response
	return final_result 