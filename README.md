![Nouveau logo du HuffPost](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/HuffPost.svg/320px-HuffPost.svg.png "Nouveau logo du HuffPost")

# Étude sur le taux d'originalité de 16 éditions du *HuffPost*.

Un peu plus de 1,8 million d'*articles* (on ne parle pas des *blogues*) de 16 des 18 éditions du *HuffPost* ont été analysés avec [**pandas**](https://github.com/jhroy/tuto-pandas) pour voir qui signe ces articles. Chaque article a été placé dans trois catégories:

- `HP_oui` lorsque l'auteur est un employé ou un pigiste du *HuffPost*.
- `HP_non` lorsque l'auteur est une source externe (autre média ou agence de presse).
- `HP_inconnu` lorsque qu'il est impossible d'attribuer l'article.

Pour faire fonctionner les carnets Jupyter qui se trouvent dans ce répertoire, il faut d'abord aller chercher les données de base, un fichier de 656 Mo accessible ici: [**scraping-nettoye.csv**](https://drive.google.com/file/d/0B90qcYhVsMeYQ2FQbEt3YkFhTjg/view?usp=sharing) (sauf pour l'édition espagnole, dont les données sont incluses dans le fichier [**scraping-ES-2.csv**](https://github.com/jhroy/huffpost/blob/master/scraping-ES-2.csv).
