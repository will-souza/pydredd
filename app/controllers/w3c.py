from requests_html import HTMLSession
session = HTMLSession()
import time


def w3c(all_url):
	links_erros = {}
	for link in all_url:
	  w3cLink = f"https://validator.w3.org/nu/?doc={link}"
	  r = session.get(w3cLink)
	  erros = r.html.find('#results strong')
	  if erros:
	    links_erros[link] = []
	    for erro in erros:
	      links_erros[link].append(erro.text)
	  time.sleep(1)
	return(links_erros)
