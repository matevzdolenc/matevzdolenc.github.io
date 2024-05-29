---
title: Računalništvo in informatika 2023/24
date: 2024-02-21
draft: false
showDate: true
showDateUpdated: true
tags: ["ulfgg", "2023", "racinf", "predavanje"]
showAuthor: false
---

{{< alert icon="comment">}}
Zgornja slika je bila ustvarjena z orodjem **Adobe Firefly 2**.
**Ukaz:** *a laptop on a desk; laptop screen displays python code; software development concept, construction site in the background*
{{< /alert >}}

## Splošne informacije

Študent pridobi osnovno teoretično in praktično znanje o računalništvu in informatiki ter je sposoben samostojno uporabljati računalniško tehnologijo pri študiju oz. običajnih inženirskih nalogah. Spozna sodobne računalniške in informacijske tehnologije ter pridobi temeljno znanje, ki mu omogoča nadaljnje samoizobraževanje oz. nadgradnjo pridobljenih znanj s področja računalniške tehnologije.

### Urnik

- predavanja - sreda, 12-14, P I/1
- vaje - po skupinah

### Kontakt

- govorilne ure - ponedeljek 9-10, soba 035
- email - [mdolenc@fgg.uni-lj.si](mailto:mdolenc@fgg.uni-lj.si)

### Prisotnost

{{< chart >}}
type: 'bar',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'],
  datasets: [{
    label: 'prisotnost na predavanjih',
    data: [76, 67, 59, 58, 55, 58, 36, 46, 21, 30, 20, , , , ],
  }],
},
options: {
	plugins: {
		tooltip: {
			enabled: false
		},
		title: {
			display: true,
			text: 'Prisotnost na predavanjih'
		},
		legend: {
			display: false
		},
	},
	scales: {
		x: {
			title: {
          		display: true,
          		text: 'teden'
	        },
		},
		y: {
			title: {
          		display: true,
          		text: 'število študentov'
	        },
		}
	}
}
{{< /chart >}}

## Predavanja

### 1. teden - sreda, 28. 2. 2024

- Uvod:
	* [Uvod v predmet- vsebina, program, osnovne informacije](/files/racinf-2023.pdf)
	* [Posebnosti gradbeništva](/files/posebnosti-gradbenistva.pdf)
- Razvoj programske opreme:
	* [Agilni manifest](/files/agilni-manifest.pdf)
	* [Agilne metodologije](/files/agilne-metodologije.pdf)
- Uvod v programski jezik Python:
	* [Zakaj Python?](http://media.matevzdolenc.com/ul-fgg/2022-2023/zakaj-python.pdf)
	* Namestitev: [python.org](http://python.org), [Continuum Analytics - Anaconda](https://www.anaconda.com/download)
- Naloga:
	* Namestitev programskega sistema Python na domačem računalniku.
	
{{< figure src="/img/agilne-metodologije.png" caption="Agilne metodologije predstavljajo nabor vrednot." >}}

### 2. teden - sreda, 6. 3. 2024

- Uvod v programski jezik Python:
	* [Zakaj Python?](http://media.matevzdolenc.com/ul-fgg/2022-2023/zakaj-python.pdf)
	* Namestitev: [python.org](http://python.org), [Continuum Analytics - Anaconda](https://www.anaconda.com/download)

- Uvod v Python:
	* Izvedba in zagon enostavnega Python programa/skripte (Spyder, iPython)
	* Uporabljeni ukazi: input(), print(), float(), import, math.pi

- Izvorna koda:
	* Python: [krog-1.py](http://media.matevzdolenc.com/python/src/krog-1.py")

{{< figure src="/img/py-ploscina-kroga-spyder.png" caption="Python program krog.py v programskem okolju Spyder." >}}

### 3. teden - sreda, 13. 3. 2024

- Uvod v Python:
	- Zagon Python skript iz ukazne vrstice
	- Program za izračun plošline kroga
    - Seznami: for in while zanka

- Izvorna koda:
	* [krog-1.py](http://media.matevzdolenc.com/python/src/krog-1.py")
	* [krog-seznam.py](http://media.matevzdolenc.com/python/src/krog-seznam.py")
	* [krog-range.py](http://media.matevzdolenc.com/python/src/krog-range.py")

{{< figure src="/img/py-izpis-tabele-krogov.png" caption="Izpis preproste tabele v konzolnem oknu." >}}

### 4. teden - sreda, 20. 3. 2024

- Uvod v Python:
	- while zanka
    - izpis v datoteko
	- Uvoz tekstovnih podatkov v Excel in risanje razpršenih grafov.

- Izvorna koda:
    - Izračun ničle funkcije - bisekcija, [bisekcija-1.py](http://media.matevzdolenc.com/python/src/bisekcija-1.py), [bisekcija-2.py](http://media.matevzdolenc.com/python/src/bisekcija-2.py)

{{< figure src="/img/py-bisekcija-graf.png" caption="" >}}

### 5. teden - sreda, 27. 3. 2024

- Uvod v Python:
	- branje in zapisovanje tekstovnih datotek

- Izvorna koda: -


### 6. - 7. teden - sreda, 3. 4. - 10. 4. 2024

- Uvod v Python:
	- branje in zapisovanje tekstovnih datotek
	- vnos več podatkov v vrstici
	- uporaba modulov

- Primer: [Izračun geometrijskih karakteristik](/files/geokar-formule.pdf)

- Izvorna koda: 
	- Podatki v programu, [geokar-1.py](http://media.matevzdolenc.com/python/src/geokar-1.py)
	- Branje podatkov s tipkovnico (vsak podatek v svoji vrstici), [geokar-2.py](http://media.matevzdolenc.com/python/src/geokar-2.py)
    - Branje podatkov s tipkovnico (x in y koordinati v isti vrstici), [geokar-3.py](http://media.matevzdolenc.com/python/src/geokar-3.py)
    - Branje podatkov iz datoteke, [geokar-4.py](http://media.matevzdolenc.com/python/src/geokar-4.py)
    - Testni podatki, [geokar-podatki.txt](http://media.matevzdolenc.com/python/src/geokar-podatki.txt)
    - Izračun ploščine s funkcijo, [geokar-5.py](http://media.matevzdolenc.com/python/src/geokar-5.py)
	- Vse geometrijske karakteristike, [geokar-6.py](http://media.matevzdolenc.com/python/src/geokar-6.py)
	- Uporaba modulov, [geokar-7.py](http://media.matevzdolenc.com/python/src/geokar-7.py), [geometrijske_karakteristike.py](http://media.matevzdolenc.com/python/src/geometrijske_karakteristike.py)

{{< figure src="/img/py-geokar-sublimetext.png" >}}

### 8. teden - sreda, 17. 4. 2024

Podatkovni standardi:
- XML - Extended Markup Language
- JSON - JavaScript Object Notation
- IFC - Industry Foundation Classes

Primeri:
- Izdelajte XML/JSON dokument za shranjevanje poljubnega poligonalnega prereza. Točke prereza so podane z oznako in dvema koordinatama: x in y. Rešitve: [xml](http://media.matevzdolenc.com/ul-fgg/2021-2022/primer.xml) | [json](http://media.matevzdolenc.com/ul-fgg/2021-2022/primer.json)
- Izdelajte XML dokument, ki vsebuje podatke o dveh geografskih točkah (ime/naslov, koordinate, nadmorska višina)
- Povezave:
	- [uvod-v-xml-zacasno.pdf](http://media.matevzdolenc.com/ul-fgg/2022-2023/uvod-v-xml-zacasno.pdf)
    - [XML standard](http://www.w3.org/standards/xml/)
    - [W3C](http://www.w3.org)
    - [JSON](http://www.json.org)
    - [IFC](http://www.buildingsmart.org/standards/ifc)
    - [KML](https://developers.google.com/kml/?hl=en)

{{< figure src="http://imgs.xkcd.com/comics/standards.png" >}}

### 9. teden - sreda, 24. 4. 2024

- Uvod v Python: branje in zapisovanje XML datotek

- Izvorna koda:
	- Zapis podatkov o prerezu v XML datoteko z uporabo Python XML knjižnice, [geokar-8-2.py](http://media.matevzdolenc.com/python/src/geokar-8-2.py)
    - Branje podatkov o prerezu iz XML datoteke, [geokar-9-1.py](http://media.matevzdolenc.com/python/src/geokar-9-1.py)
    - Podajanje imena vhodne datoteke s podatko o prerezu v ukazni vrstici, [geokar-9-2.py](http://media.matevzdolenc.com/python/src/geokar-9-2.py)
    - Podajanje imena vhodne datoteke s podatki o prerezu v ukazni vrstici, [geokar-9-3.py](http://media.matevzdolenc.com/python/src/geokar-9-3.py)
    - Ostale potrebne datoteke ... [geometrijske_karakteristike.py](http://media.matevzdolenc.com/python/src/geometrijske_karakteristike.py), [geokar-podatki.txt](http://media.matevzdolenc.com/python/src/geokar-podatki.txt), [geokar-podatki.xml](http://media.matevzdolenc.com/python/src/geokar-podatki.xml)

{{< figure src="/img/py-geokar-xml.png" >}}

### 10. teden - sreda, 8. 5. 2024
Knjižnice: [NumPy](https://www.numpy.org), [SciPy](https://scipy.org), [matplotlib](https://matplotlib.org)

Python in SQL:
- Baze podatkov: [SQLite](http://www.sqlite.org), [MySQL](http://www.mysql.com), ...
- [Uporaba Python/SQL](http://www.python-course.eu/sql_python.php)
- Zapis podatkov v bazo SQLite: [geokar-xml2db.py](http://media.matevzdolenc.com/python/src/geokar-xml2db.py), [geokar-podatki.xml](http://media.matevzdolenc.com/python/src/geokar-podatki.xml)
- Iskanje podatkov v bazi SQLite: [geokar-10-1.py](http://media.matevzdolenc.com/python/src/geokar-10-1.py), [geometrijske_karakteristike.py](http://media.matevzdolenc.com/python/src/geometrijske_karakteristike.py)

Python in Excel: 
-  Uporaba knjižnice [openpyxl](https://openpyxl.readthedocs.io/en/stable/#): [mb_primer-1.py](http://media.matevzdolenc.com/python/src/mb_primer-1.py), [mb_primer-1.xlsx](http://media.matevzdolenc.com/python/src/mb_primer-1.xlsx)
- Uporaba knjižnice [Pandas](http://pandas.pydata.org): [mb_primer-2.py](http://media.matevzdolenc.com/python/src/mb_primer-2.py), [mb_primer-2.xlsx](http://media.matevzdolenc.com/python/src/mb_primer-2.xlsx)

Python in numerične analize:
- Preprost primer izračuna sistema linearnih enačb, [linalg-1.py](http://media.matevzdolenc.com/python/src/linalg-1.py)
- Izračun sistema linearnih enačb:
	- Program: [linalg-2.py](http://media.matevzdolenc.com/python/src/linalg-2.py)
	- Podatki - [Matrix Market](https://math.nist.gov/MatrixMarket/): [info](http://math.nist.gov/MatrixMarket/data/SPARSKIT/fidap/fidapm37.html), [fidapm37.mtx](http://media.matevzdolenc.com/python/src/fidapm37.mtx), [fidapm37_rhs1.mtx](http://media.matevzdolenc.com/python/src/fidapm37_rhs1.mtx)

Uporaba knjižnice PyPlot:
- Program za izris prereza: [geokar-plot.py](http://media.matevzdolenc.com/python/src/geokar-plot.py)
- Podatki: [geokar-podatki-1.txt](http://media.matevzdolenc.com/python/src/geokar-podatki-1.txt), [geokar-podatki-2.txt](http://media.matevzdolenc.com/python/src/geokar-podatki-2.txt)

Datoteke: [numpy-matplotlib-sqlite.zip](http://media.matevzdolenc.com/python/src/numpy-matplotlib-sqlite.zip)

{{< figure src="/img/fidapm37_lg_city.gif" >}}
{{< figure src="/img/py-geokar-pyplot.png" >}}

### 11. teden - sreda, 15. 5. 2024

- Gradbena informatika:
	- [Posebnosti gradbeništva](/files/posebnosti-gradbenistva.pdf)
	- Uvod v gradbeno informatiko: [Splošno o gradbeni informatiki - značilnosti in posledice le-teh](/files/gradbena-informatika.pdf), [Informacije, podatki, znanje](/files/informacije-podatki-znanje.pdf)

- Digitalni dokumenti:
	* [Digitalni dokumenti](href="http://media.matevzdolenc.com/ul-fgg/2022-2023/digitalni-dokumenti.pdf) - prednosti in slabosti, standardi, itd.
	* Excel - naslavljanje celic: absolutno/relativno, delo s formulami: pisanje/kopiranje, ...

- LaTeX:
	* [LaTeX](http://www.latex-project.org)
 	* [MiKTeX, LaTeX za Windows](http://miktex.org)
	* [Ne najkrajši uvod v LaTeX](https://users.fmf.uni-lj.si/plestenjak/vaje/latex/lshort.pdf)
	* [LaTeX Base](https://latexbase.com/)
	* [Primer](/files/primer-latex.zip)
	
- Markdown:
	* [Markdown](http://daringfireball.net/projects/markdown/)
	* [Markdown Tutorial](http://markdowntutorial.com/)
	* [Markdown za Windows](http://www.maketecheasier.com/best-markdown-editor-for-windows/)
	* [Markdown hitra navodila](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
	* [Word to Markdown Converter](https://word-to-markdown.herokuapp.com)
	* [Markdown Live Preview](https://markdownlivepreview.com)
	* [Primer](/files/primer-md.zip)

{{< figure src="/img/md-latex-preview.png" caption="Markdown (levo) in LaTeX (desno) predogled." >}}

### 12. teden - 22. 5. 2024

- Internet in splet:
	* [Uvod v Internet](/files/internet.pdf) - zgodovina, protokoli, ...
	* [Uvod v splet](/files/splet.pdf) - zgotovina, protokoli, uporaba, 1.0/2.0/3.0, ...
    * [Uvod v splet 2.0](/files/splet-2.0-rk.pdf)
    * [Osnove inženirske komunikacije](/files/komunikacija.pdf)

{{< figure src="/img/web2.png" caption="" >}}

### 13. teden - 29. 5. 2024

Virtualizacija:
- [Virtualizacija - uporaba navideznih računalnikov](/files/virtualizacija.pdf)
- [Distro Watch](http://distrowatch.com/) - seznam Linux distribucij
- [Oracle VirtualBox](https://www.virtualbox.org) - okolje za virtualizacijo oeracijskih sistemov
- Linux distribucije: [Ubuntu](https://ubuntu.com), [Fedora](http://fedoraproject.org), [Redhat](http://www.redhat.com)
- Naloga: Namestitev VirtualBox in preiskus ene izmed Linux distribucij.

Odprta koda:
- [Odprta koda](/files/open-source-2017.pdf) - zgodovina in razvoj, kaj pomeni za končne upodarbnike

Knjiga David Weinberger, “Everything is Miscellaneous: The Power of the New Digital Disorder”:
- [Vse je različno](/files/vse-je-razlicno.pdf)
- [Everything is Miscellaneous](http://www.youtube.com/watch?v=x3wOhXsjPYM) - video
- [Information R/evolution](http://www.youtube.com/watch?v=-4CV05HyAbM) - video

{{< figure src="/img/virtualizacija-virtualbox.png" >}}

### 14. teden - 5. 6. 2024

Baze podatkov:
- [Uvod v podatkovne baze](/files/baze-podatkov-1920.pdf)
- [2019 Database Trends – SQL vs. NoSQL, Top Databases, Single vs. Multiple Database Use](https://scalegrid.io/blog/2019-database-trends-sql-vs-nosql-top-databases-single-vs-multiple-database-use/)

Podatkovni centri:
- [Google Datacenters](https://www.google.com/about/datacenters/)
- [AWS data centers](https://aws.amazon.com/compliance/data-center/data-centers/)
- [Facebook Engineering](https://engineering.fb.com)

Navidezna in razširjena resničnost:
- [Osnove in primeri](http://media.matevzdolenc.com/ul-fgg/2021-2022/vr-ar.pdf)
- DOLENC, Matevž. [Augmented reality in AEC industry](https://www.intechopen.com/online-first/1153616). V: BOULANGER, Pierre (ur.). Applications of Augmented Reality - Current State of the Art. London: IntechOpen Limited, 2023. Str. 1-14, ilustr. ISBN 978-1-83769-334-4., DOI: 10.5772/intechopen.1002371. [COBISS.SI-ID 164279299]
- DE HUGO SILVA, Angela Cristina, GABER, Metod, DOLENC, Matevž. [Using Augmented Reality in Different BIM Workflows](https://www.intechopen.com/online-first/77894). V: Augmented Reality. London: IntechOpen Limited, 2021. Str. 1-14, ilustr. DOI: 10.5772/intechopen.99336. [COBISS.SI-ID 94789635]
- Sebastjan Meža, [Razširjena resničnost kot infrastruktura za izboljšanje komunikacije v gradbenih projektih](https://repozitorij.uni-lj.si/IzpisGradiva.php?id=30946&lang=slv)
- Luka Gradišar, [Dan odprtih vrat: Digitalno modeliranje in navidzna resničnost](http://media.matevzdolenc.com/ul-fgg/2021-2022/Dan_odprtih_vrat_Digitalno_in_navidezna_resnicnost.pdf)
- Naloga: Namestite in preiskusite [BIMx](http://www.graphisoft.com/bimx/)

Internet stvari (angl. Internet of Things - IoT):
- [Osnove in primeri](http://media.matevzdolenc.com/ul-fgg/2021-2022/iot.pdf)
- [Internet of Things Infographic | What Is The "Internet of Things"?](https://www.postscapes.com/what-exactly-is-the-internet-of-things-infographic/)

{{< figure src="/img/vr-ar.jpeg" >}}

