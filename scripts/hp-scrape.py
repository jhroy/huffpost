# coding: utf-8
# 2017 Jean-Hugues Roy, GNU GPL v3.

import csv
import requests
import re
from bs4 import BeautifulSoup

e = "editions.csv"
f1 = open(e)
editions = csv.reader(f1)
next(editions) # pour ignorer les entêtes

for edition in editions:

	fichier1 = "hp-{}.csv".format(edition[0].casefold())
	fichier2 = "scraping-{}.csv".format(edition[0].casefold())

	f1 = open(fichier1)
	source = csv.reader(f1)
	next(source)

	for article in source:
		url = article[5]

		entete = {
			"User-Agent":"Jean-Hugues Roy, Universite du Quebec a Montreal (UQAM)",
			"From":"r***s@uqam.ca"
		}

		try:

			c = requests.get(url,stream=True,headers=entete)
			# print(c.status_code,url)

			page = BeautifulSoup(c.text,"html.parser")

			try:
				by = page.find("div", class_="author-card")
				byline = page.find("div", class_="author-card").text.strip()
				byline = byline.replace("\n"," ")
				byline = byline.replace("  "," ")

				if by.find("img"):
					alt = by.find("img")["alt"]
					byline = byline + alt

			except:
				try:
					by = page.find("div", class_="author-card")
					byline = page.find("li", class_="author-card").text.strip()
					byline = byline.replace("\n"," ")
					byline = byline.replace("  "," ")

					if by.find("img"):
						alt = by.find("img")["alt"]
						byline = byline + alt

				except:
					try:
						if page.find("div", class_="wire-partner-component"):
							wire = page.find("div", class_="wire-partner-component")
							agence = wire.img["class"][0]
							auteur = wire.text.strip()
							byline = agence + " " + auteur
					except:
						byline = "?"

			try:
				tags = page.find("meta", attrs={"name":"keywords"})["content"]
			except:
				tags = "?"

			try:
				site = page.find("meta", property="og:site_name")["content"]
			except:
				site = "?"

			try:
				titre = page.title.text
			except:
				titre = "?"

			article2 = []
			article2.append(article[0])
			article2.append(article[1])
			article2.append(article[2])
			article2.append(article[3])
			article2.append(article[4])
			article2.append(article[5])
			article2.append(article[6])
			article2.append(titre)
			if titre == article[6]:
				titrepareil = "O"
			else:
				titrepareil = "N"
			article2.append(titrepareil)
			article2.append(site)
			article2.append(byline)
			article2.append(tags)

			print(article2)
			print("#"*50)

			spirou = open(fichier2,"a")
			gaston = csv.writer(spirou)
			gaston.writerow(article2)

		except:
			print("#"*50)
			print("Problème quelconque... on saute cette page.")
			print("#"*50)
			print("\n")
