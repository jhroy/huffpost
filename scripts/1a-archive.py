# coding: utf-8
# 2017 Jean-Hugues Roy, GNU GPL v3.

import csv
import requests
import datetime
from time import sleep
from bs4 import BeautifulSoup

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
		url = "http://www.{}/archive/{}-{}-{}".format(edition[3],date.year,date.month,date.day)
		print(url)
		entete = {
			"User-Agent":"Jean-Hugues Roy, Universite du Quebec a Montreal (UQAM)",
			"From":"r***s@uqam.ca"
			}
		x = requests.get(url,headers=entete,timeout=300)
		page = BeautifulSoup(x.text,"html.parser")
		articles = page.find("div", class_="archive").find_all("li")

		for article in articles:
			url = article.a["href"]
			if "_n_" in url:
				genre = "Nouvelles"
				p1 = url.find("_n_")
				p2 = url.find(".htm")
				iD = url[p1+3:p2]
			elif "_b_" in url:
				genre = "Blogue"
			else:
				genre = "Inconnu"
				iD = "Inconnu"
				
			#Si l'élément archivé n'est pas un blogue, on l'enregistre
			if genre != "Blogue":
				art = []
				art.append(iD)
				art.append(edition[0])
				art.append(date.year)
				art.append(date.month)
				art.append(date.day)
				art.append(url)
				art.append(article.a.text.strip())
				art.append(genre)
				print(art)

				yo = open(fichier,"a")
				yolo = csv.writer(yo)
				yolo.writerow(art)
