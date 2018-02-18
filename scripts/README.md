# Scripts

### Quelques scripts utilisés pour le [projet sur le *Huffington Post*](../README.md).
<hr>

#### Scripts pour la première étape du moissonnage

* [**1a-archive.py**](1a-archive.py)&nbsp;: exemple de script qui a servi dans le cas où une version du *HuffPost* disposait d'une section d'archives, ce dont de moins en moins d'éditions disposent ([voici celles du *HuffPost* France, archivées sur la *Wayback Machine*](https://web.archive.org/web/20160806214824/http://www.huffingtonpost.fr/archive/2015-12)).

*  [**1b-archive.py**](1b-archive.py)&nbsp;: exemple de script qui a servi dans le cas où une version du *HuffPost* **ne disposait pas** d'une section d'archives, ce qui me forçait à avoir recours à l'[API Custom Search de Google](https://developers.google.com/custom-search/json-api/v1/overview).

#### Script pour la seconde étape du moissonnage

* [**2-scrape.py**](2-scrape.py)&nbsp;: une fois la première étape réalisée, on repasse à travers tous les URLs moissonnés pour, tout d'abord, vérifier s'il y a bel et bien un article au bout, puis pour recueillir le nom du ou des auteur(s) de cet article.

#### Tableau des éditions du *HuffPost*

* [**editions.csv**](editions.csv)
