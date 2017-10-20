![HuffPost logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/HuffPost.svg/320px-HuffPost.svg.png "HuffPost logo")

# Original reporting at the *HuffPost* (2011-2016)
### Study on the "originality rate" of the *HuffPost* and 15 of its international editions
<hr>

The bylines of more than 1.8 million *articles* (**_blogs_** were excluded) published by 16 of the _HuffPost_'s 18 versions were scraped.<br>Each byline was categorized thus:


- `HP_yes` when the byline includes *"HuffPost"* or the name of an employee or freelancer, even if another media organization is mentioned.
- `HP_no` when the byline attributes authorship exclusively to another media organization (press agency, website, newspaper, etc.).
- `HP_unknown` when authorship cannot be established.


The table below gives the rates per edition.<br>
Links are to Jupyter notebooks in French.<br>
One can access the raw data by downloading this csv file: [**scraping-nettoye.csv**](https://drive.google.com/file/d/0B90qcYhVsMeYQ2FQbEt3YkFhTjg/view?usp=sharing) (apart from the Spanish edition, whose data is included in this file: [**scraping-ES-2.csv**](https://github.com/jhroy/huffpost/blob/master/scraping-ES-2.csv)).

| **version**        | **launch date**   |**articles**|**`HP_yes`**|**`HP_no`**|**`HP_unknown`**| **originality rate** |
| ------------- |-------------| -----:|-----:|-----:|-----:|-----:|
|[US](HuffPost-usa.ipynb)<sup>1</sup>, [site](http://www.huffingtonpost.com/)|2005-05-09|550&nbsp;955|250&nbsp;528|210&nbsp;226|90&nbsp;201|45.5%|
|[Canada](HuffPost-can.ipynb), [site](http://www.huffingtonpost.ca/)|2011-05-26|265&nbsp;153|40&nbsp;809|222&nbsp;950|1&nbsp;394|15.4%|
|[United Kingdom](HuffPost-uk.ipynb), [site](http://www.huffingtonpost.co.uk/)|2011-07-06|161&nbsp;263|118&nbsp;317|42&nbsp;757|189|73.4%|
|[France](HuffPost-fr.ipynb), [site](http://www.huffingtonpost.fr/)|2012-01-23|54&nbsp;156|49&nbsp;815|4&nbsp;088|253|92.0%|
|[Québec](HuffPost-qc.ipynb), [site](http://quebec.huffingtonpost.ca/)|2012-02-08|390&nbsp;231|44&nbsp;282|344&nbsp;510|1&nbsp;439|11.3%|
|[Spain](HuffPost-es.ipynb), [site](http://www.huffingtonpost.es/)|2012-06-07|56&nbsp;348|48&nbsp;879|7&nbsp;381|88|86.7%|
|[Italy](HuffPost-it.ipynb), [site](http://www.huffingtonpost.it/)|2012-09-24|64&nbsp;880|53&nbsp;820|9&nbsp;944|1&nbsp;116|83.0%|
|[Japan](HuffPost-jp.ipynb), [site](http://www.huffingtonpost.jp/)|2013-05-06|23&nbsp;708|16&nbsp;490|6&nbsp;865|353|69.6%|
|[Maghreb](HuffPost-mag.ipynb), [site](http://www.huffpostmaghreb.com/)|2013-06-25|28&nbsp;653|25&nbsp;200|3&nbsp;337|116|87.9%|
|[Germany](HuffPost-all.ipynb), [site](http://www.huffingtonpost.de/)|2013-10-01|68&nbsp;733|31&nbsp;831|33&nbsp;445|3&nbsp;457|46.3%|
|[Brazil](HuffPost-bra.ipynb), 	[site](http://www.huffpostbrasil.com/)|2014-01-29|20&nbsp;831|14&nbsp;543|5&nbsp;745|543|69.8%|
|[South Korea](HuffPost-kr.ipynb), [site](http://www.huffingtonpost.kr/)|2014-02-26|51&nbsp;890|25&nbsp;945|25&nbsp;476|469|50.0%|
|[Greece](HuffPost-grece.ipynb), [site](http://www.huffingtonpost.gr/)|2014-11-20|55&nbsp;433|55&nbsp;004|279|150|99.2%|
|[India](HuffPost-inde.ipynb), [site](http://www.huffingtonpost.in/)|2014-12-08|14&nbsp;618|8&nbsp;613|3&nbsp;154|2&nbsp;851|58.9%|
|[Australia](HuffPost-aus.ipynb), [site](http://www.huffingtonpost.com.au/)|2015-08-18|17&nbsp;154|12&nbsp;335|3&nbsp;255|1&nbsp;564|71.9%|
|[Mexico](HuffPost-mex.ipynb), [site](http://www.huffingtonpost.com.mx/)|2016-09-01|2&nbsp;168|1&nbsp;916|102|150|88.4%|
|*All* | |*1&nbsp;826&nbsp;174*|*798&nbsp;327*|*923&nbsp;514*|*104&nbsp;333*|*43.7%*|

###### 1 : All articles available and findable online published between the launch date and Dec. 31, 2016, were included in this study, apart from the US edition where articles were included starting Jan. 1, 2011.
