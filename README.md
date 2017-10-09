![Nouveau logo du HuffPost](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/HuffPost.svg/320px-HuffPost.svg.png "Nouveau logo du HuffPost")

# Étude sur le taux d'originalité de 16 éditions du *HuffPost*.

Un peu plus de 1,8 million d'*articles* (on ne parle pas des *blogues*) de 16 des 18 éditions du *HuffPost* ont été analysés avec [**pandas**](https://github.com/jhroy/tuto-pandas) pour voir qui signe ces articles. Chaque article a été placé dans trois catégories:

- `HP_oui` lorsque l'auteur est un employé ou un pigiste du *HuffPost*.
- `HP_non` lorsque l'auteur est une source externe (autre média ou agence de presse).
- `HP_inconnu` lorsque qu'il est impossible d'attribuer l'article.

Pour faire fonctionner les carnets Jupyter qui se trouvent dans ce répertoire, il faut d'abord aller chercher les données de base, un fichier de 656 Mo accessible ici: [**scraping-nettoye.csv**](https://drive.google.com/file/d/0B90qcYhVsMeYQ2FQbEt3YkFhTjg/view?usp=sharing) (sauf pour l'édition espagnole, dont les données sont incluses dans le fichier [**scraping-ES-2.csv**](https://github.com/jhroy/huffpost/blob/master/scraping-ES-2.csv).

Il y a un carnet par pays. Le tableau ci-dessous présente les résultats complets par pays, classés par date de fondation.

| **édition**        | **date de fondation**           | **url**  |**articles**|**`HP_oui`**|**`HP_non`**|**`HP_inconnu`**| **taux d'originalité** |
| ------------- |-------------|-----| -----:|-----:|-----:|-----:|-----:|
|[États-Unis](HuffPost-usa.ipynb)|	2005-05-09	|	[huffingtonpost.com](http://www.huffingtonpost.com/)|550 955|250 528|210 226|90 201|45,5 %|
|[Canada](HuffPost-can.ipynb)|	2011-05-26	|	[huffingtonpost.ca](http://www.huffingtonpost.ca/)|265 153|40 809|222 950|1 394|15,4 %|
|[Royaume-Uni](HuffPost-uk.ipynb)|	2011-07-06	|	[huffingtonpost.co.uk](http://www.huffingtonpost.co.uk/)|161 263|118 317|42 757|189|73,4 %|
|[France](HuffPost-fr.ipynb)|	2012-01-23	|	[huffingtonpost.fr](http://www.huffingtonpost.fr/)|54 156|49 815|4 088|253|92 %|
|[Québec](HuffPost-qc.ipynb)|	2012-02-08	|	[quebec.huffingtonpost.ca](http://quebec.huffingtonpost.ca/)|390 231|44 282|344 510|1 439|11,3 %|
|[Espagne](HuffPost-es.ipynb)|	2012-06-07	|	[huffingtonpost.es](http://www.huffingtonpost.es/)|56 348|48 879|7 381|88|86,7 %|
|[Italie](HuffPost-it.ipynb)|	2012-09-24	|	[huffingtonpost.it](http://www.huffingtonpost.it/)|64 880|53 820|9 944|1 116|83 %|
|[Japon](HuffPost-jp.ipynb)|	2013-05-06	|	[huffingtonpost.jp](http://www.huffingtonpost.jp/)|23 708|16 490|6 865|353|69,6 %|
|[Maghreb](HuffPost-mag.ipynb)|	2013-06-25	|	[huffpostmaghreb.com](http://www.huffpostmaghreb.com/)|28 653|25 200|3 337|116|87,9 %|
|[Allemagne](HuffPost-all.ipynb)|	2013-10-01	|	[huffingtonpost.de](http://www.huffingtonpost.de/)|68 733|31 831|33 445|3 457|46,3 %|
|[Brésil](HuffPost-bra.ipynb)|	2014-01-29	|	[brasilpost.com.br](http://www.huffpostbrasil.com/)|20 831|14 543|5 745|543|69,8 %|
|[Corée du Sud](HuffPost-kr.ipynb)|	2014-02-26	| [huffingtonpost.kr](http://www.huffingtonpost.kr/)|51 890|25 945|25 476|469|50,0 %|
|[Grèce](HuffPost-grece.ipynb)|	2014-11-20	|	[huffingtonpost.gr](http://www.huffingtonpost.gr/)|55 433|55 004|279|150|99,2 %|
|[Inde](HuffPost-inde.ipynb)|	2014-12-08	|	[huffingtonpost.in](http://www.huffingtonpost.in/)|14 618|8 613|3 154|2 851|58,9 %|
|[Australie](HuffPost-aus.ipynb)|	2015-08-18	|	[huffingtonpost.com.au](http://www.huffingtonpost.com.au/)|17 154|12 335|3 255|1 564|71,9 %|
|[Mexique](HuffPost-mex.ipynb)|	2016-09-01	|	[huffingtonpost.com.mx](http://www.huffingtonpost.com.mx/)|2 168|1 916|102|150|88,4 %|
|*Ensemble* | | |1 826 174 | 798 327|923 514 | 104 333|*43,7 %*|
