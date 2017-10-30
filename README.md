![Nouveau logo du HuffPost](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/HuffPost.svg/320px-HuffPost.svg.png "Nouveau logo du HuffPost")

# Étude sur le taux d'originalité de 16 éditions du *HuffPost* (2011-2016).
[English version](README-en.md)
<hr>


Un peu plus de 1,8 million d'**_articles_**  (on ne parle pas des *blogues*) de 16 des 18 éditions du *HuffPost* ont été analysés avec [**pandas**](https://github.com/jhroy/tuto-pandas) pour voir qui signe ces articles. Chaque article a été placé dans trois catégories:

- `HP_oui` lorsque l'auteur est un employé ou un pigiste du *HuffPost*.
- `HP_non` lorsque l'auteur est une source externe (autre média ou agence de presse).
- `HP_inconnu` lorsque qu'il est impossible d'attribuer l'article.

Pour faire fonctionner les carnets Jupyter qui se trouvent dans ce répertoire, il faut d'abord aller chercher les données de base, un fichier de 656 Mo accessible ici: [**scraping-nettoye.csv**](https://drive.google.com/file/d/0B90qcYhVsMeYQ2FQbEt3YkFhTjg/view?usp=sharing) (sauf pour l'édition espagnole, dont les données sont incluses dans le fichier [**scraping-ES-2.csv**](https://github.com/jhroy/huffpost/blob/master/scraping-ES-2.csv).

Il y a un carnet par pays. Le tableau ci-dessous présente les résultats complets par pays, classés par date de fondation.

| **édition**        | **date de fondation**   |**articles**|**`HP_oui`**|**`HP_non`**|**`HP_inconnu`**| **taux d'originalité** |
| ------------- |-------------| -----:|-----:|-----:|-----:|-----:|
|[États-Unis](HuffPost-usa.ipynb)<sup>1</sup>, [site](http://www.huffingtonpost.com/)|2005-05-09|550&nbsp;955|250&nbsp;528|210&nbsp;226|90&nbsp;201|45,5%|
|[Canada](HuffPost-can.ipynb), [site](http://www.huffingtonpost.ca/)|2011-05-26|265&nbsp;153|40&nbsp;809|222&nbsp;950|1&nbsp;394|15,4%|
|[Royaume-Uni](HuffPost-uk.ipynb), [site](http://www.huffingtonpost.co.uk/)|2011-07-06|161&nbsp;263|118&nbsp;317|42&nbsp;757|189|73,4%|
|[France](HuffPost-fr.ipynb), [site](http://www.huffingtonpost.fr/)|2012-01-23|54&nbsp;156|49&nbsp;815|4&nbsp;088|253|92,0%|
|[Québec](HuffPost-qc.ipynb), [site](http://quebec.huffingtonpost.ca/)|2012-02-08|390&nbsp;231|44&nbsp;282|344&nbsp;510|1&nbsp;439|11,3%|
|[Espagne](HuffPost-esp.ipynb), [site](http://www.huffingtonpost.es/)|2012-06-07|56&nbsp;348|48&nbsp;879|7&nbsp;381|88|86,7%|
|[Italie](HuffPost-ita.ipynb), [site](http://www.huffingtonpost.it/)|2012-09-24|64&nbsp;880|53&nbsp;820|9&nbsp;944|1&nbsp;116|83,0%|
|[Japon](HuffPost-jap.ipynb), [site](http://www.huffingtonpost.jp/)|2013-05-06|23&nbsp;708|16&nbsp;490|6&nbsp;865|353|69,6%|
|[Maghreb](HuffPost-mag.ipynb), [site](http://www.huffpostmaghreb.com/)|2013-06-25|28&nbsp;653|25&nbsp;200|3&nbsp;337|116|87,9%|
|[Allemagne](HuffPost-all.ipynb), [site](http://www.huffingtonpost.de/)|2013-10-01|68&nbsp;733|31&nbsp;831|33&nbsp;445|3&nbsp;457|46,3%|
|[Brésil](HuffPost-bra.ipynb), 	[site](http://www.huffpostbrasil.com/)|2014-01-29|20&nbsp;831|14&nbsp;543|5&nbsp;745|543|69,8%|
|[Corée du Sud](HuffPost-kr.ipynb), [site](http://www.huffingtonpost.kr/)|2014-02-26|51&nbsp;890|25&nbsp;945|25&nbsp;476|469|50,0%|
|[Grèce](HuffPost-grece.ipynb), [site](http://www.huffingtonpost.gr/)|2014-11-20|55&nbsp;433|55&nbsp;004|279|150|99,2%|
|[Inde](HuffPost-inde.ipynb), [site](http://www.huffingtonpost.in/)|2014-12-08|14&nbsp;618|8&nbsp;613|3&nbsp;154|2&nbsp;851|58,9%|
|[Australie](HuffPost-aus.ipynb), [site](http://www.huffingtonpost.com.au/)|2015-08-18|17&nbsp;154|12&nbsp;335|3&nbsp;255|1&nbsp;564|71,9%|
|[Mexique](HuffPost-mex.ipynb), [site](http://www.huffingtonpost.com.mx/)|2016-09-01|2&nbsp;168|1&nbsp;916|102|150|88,4%|
|*Ensemble* | |*1&nbsp;826&nbsp;174*|*798&nbsp;327*|*923&nbsp;514*|*104&nbsp;333*|*43,7%*|

###### 1 : Tous les articles accessibles et publiés entre la date de fondation et le 31 décembre 2016 ont été inclus dans cette étude, sauf dans le cas de l'édition américaine où la cueillette a commencé le 1<sup>er</sup> janvier 2011.
<hr>

[Quelques exemples des scripts python utilisés pour réaliser ce projet](/scripts).
