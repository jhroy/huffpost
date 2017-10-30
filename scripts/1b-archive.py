# coding: utf-8
# 2017 Jean-Hugues Roy, GNU GPL v3.

import csv
import requests
import datetime
from time import sleep
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

cle = "CLÉ APIs GOOGLE"
cse = "CODE GOOGLE CUSTOM SEARCH"

def goo(url):

	req = requests.get(url)
	r = req.json()

	if "items" in r:

		items = r["items"]

		for item in items:
			lien = item["link"]
			if "_n_" in lien:
				genre = "Nouvelles"
				p1 = lien.find("_n_")
				p2 = lien.find(".htm")
				iD = lien[p1+3:p2]
			elif "_b_" in lien:
				genre = "Blogue"
			else:
				genre = "Inconnu"
				iD = "Inconnu"
			if genre != "Blogue":

				article = []
				article.append(iD)
				article.append(edition[0])
				article.append(an)
				article.append(mois)
				article.append(jour)

				article.append(lien)
				if "og:title" in item["pagemap"]["metatags"][0]:
					article.append(item["pagemap"]["metatags"][0]["og:title"])
				else:
					article.append(item["title"])
				if "article:tag" in item["pagemap"]["metatags"][0]:
					article.append(item["pagemap"]["metatags"][0]["article:tag"])
				else:
					article.append("")

				print(article,"\n")

				yo = open(fichier,"a")
				yolo = csv.writer(yo)
				yolo.writerow(article)

e = "editions.csv"

f1 = open(e)
editions = csv.reader(f1)
next(editions) # pour ignorer les entêtes

for edition in editions:

	fichier = "hp-{}.csv".format(edition[0].casefold())

	date_debut = edition[2]
	date_fin = "01-01-2017"

	debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
	fin = datetime.datetime.strptime(date_fin, "%d-%m-%Y")
	dates = [debut + datetime.timedelta(days=j) for j in range(0, (fin-debut).days)]
	print("L'édition {} du HP compte {} jours".format(edition[0],len(dates)))

	for date in dates:
		an = date.year
		mois = str(date.strftime("%m"))
		jour = str(date.strftime("%d"))
		terme = "site:http://www.{0}/{1}/{2}/{3}".format(edition[3],an,mois,jour) ### À CHANGER
		print("\n"+"*"*50)
		# print("{}".format(terme))

		url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}".format(cle,cse,terme)
		print(url)

		req = requests.get(url)
		r = req.json()
		nbResultats = r["queries"]["request"][0]["totalResults"]
		print("{} résultats ce jour-là\n".format(nbResultats))
		nbResultats = float(nbResultats)

		goo(url)

		if nbResultats > 10:
			nbPages = int((nbResultats-1)/10)
			# print(nbPages)
			for n in range(1,nbPages+1):
				index = (n*10)+1
				url2 = "{}&start={}".format(url,index)
				print("Page {}\n{}\n".format(n+1,url2))
				goo(url2)
