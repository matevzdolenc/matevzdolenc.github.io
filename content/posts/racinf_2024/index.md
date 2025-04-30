---
title: Računalništvo in informatika 2024/25
date: 2025-02-15
draft: false
showDate: true
showDateUpdated: true
tags: ["ulfgg", "2024", "racinf", "predavanje"]
showAuthor: false
---

{{< alert icon="comment">}}
Zgornja slika je bila ustvarjena z orodjem **Adobe Firefly 2**.
**Ukaz:** *a laptop on a desk; laptop screen displays python code; software development concept, construction site in the background*
{{< /alert >}}

## Splošne informacije

Študent pridobi osnovno teoretično in praktično znanje o računalništvu in informatiki ter je sposoben samostojno uporabljati računalniško tehnologijo pri študiju oz. običajnih inženirskih nalogah. Spozna sodobne računalniške in informacijske tehnologije ter pridobi temeljno znanje, ki mu omogoča nadaljnje samoizobraževanje oz. nadgradnjo pridobljenih znanj s področja računalniške tehnologije.

### Urnik

- predavanja - sreda, 14-16, J-I/1
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
    data: [70, 63, 56, 55, 39, 42, 19, 16, , , , , , , ],
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

### 1. teden - sreda, 19. 2. 2025

- Uvod:
	* [Uvod v predmet- vsebina, program, osnovne informacije](/files/racinf-2024.pdf)
	* [Posebnosti gradbeništva](/files/posebnosti-gradbenistva.pdf)

- Uvod v programski jezik Python:
	* [Zakaj Python?](/files/zakaj-python.pdf)
	* Namestitev: [python.org](http://python.org), [Continuum Analytics - Anaconda](https://www.anaconda.com/download)
	* Urejevalniki teksta: [Notepad++](https://notepad-plus-plus.org), [Visual Studio Code](https://code.visualstudio.com)

- Naloga:
	* Namestitev programskega sistema Python na domačem računalniku (Python + urejevalnik teksta).
	
{{< figure src="/img/agilne-metodologije.png" caption="Agilne metodologije predstavljajo nabor vrednot." >}}

### 2. teden - sreda, 26. 2. 2025

- Razvoj programske opreme:
	* [Agilni manifest](/files/agilni-manifest.pdf)
	* [Agilne metodologije](/files/agilne-metodologije.pdf)

- Uvod v Python:
	* Izvedba in zagon enostavnega Python programa/skripte (Spyder, iPython)
	* Uporabljeni ukazi: input(), print(), float(), import, math.pi

- Izvorna koda:
	* Python: [krog-1.py](/src/python/krog-1.py)

{{< figure src="/img/py-ploscina-kroga-spyder.png" caption="Python program krog.py v programskem okolju Spyder." >}}

### 3. teden - sreda, 5. 3. 2025

- Uvod v Python:
	- Zagon Python skript iz ukazne vrstice
	- Program za izračun plošline kroga
    - Seznami: for in while zanka

- Izvorna koda:
	* [krog-1.py](/src/python/krog-1.py")
	* [krog-seznam.py](/src/python/krog-seznam.py")
	* [krog-range.py](/src/python/krog-range.py")

{{< figure src="/img/py-izpis-tabele-krogov.png" caption="Izpis preproste tabele v konzolnem oknu." >}}

### 4. teden - sreda, 12. 3. 2025

- Uvod v Python:
	- while zanka
    - izpis v datoteko
	- Uvoz tekstovnih podatkov v Excel in risanje razpršenih grafov.

- Izvorna koda:
    - Izračun ničle funkcije - bisekcija, [bisekcija-1.py](/src/python/bisekcija-1.py), [bisekcija-2.py](/src/python/bisekcija-2.py)

{{< figure src="/img/py-bisekcija-graf.png" caption="" >}}

### 5./6. teden - sreda, 19./26. 3. 2025

- Uvod v Python:
	- začetek daljšega primera
	- vnos več podatkov v vrstici
	- seznami

- Primer: [Izračun geometrijskih karakteristik](/files/geokar-formule.pdf)

- Izvorna koda: 
	- Podatki v programu, [geokar-1.py](/src/python/geokar-1.py)
	- Branje podatkov s tipkovnico (vsak podatek v svoji vrstici), [geokar-2.py](/src/python/geokar-2.py)
    - Branje podatkov s tipkovnico (x in y koordinati v isti vrstici), [geokar-3.py](/src/python/geokar-3.py)
    - Branje podatkov iz datoteke, [geokar-4.py](/src/python/geokar-4.py)
    - Testni podatki, [geokar-podatki.txt](/src/python/geokar-podatki.txt)
    - Izračun ploščine s funkcijo, [geokar-5.py](/src/python/geokar-5.py)
	- Vse geometrijske karakteristike, [geokar-6.py](/src/python/geokar-6.py)
	- Uporaba modulov, [geokar-7.py](/src/python/geokar-7.py), [geometrijske_karakteristike.py](/src/python/geometrijske_karakteristike.py)

{{< figure src="/img/py-geokar-sublimetext.png" >}}

### 7. teden - sreda, 2. 4. 2025

Podatkovni standardi:
- XML - Extended Markup Language
- JSON - JavaScript Object Notation
- IFC - Industry Foundation Classes

Primeri:
- Izdelajte XML/JSON dokument za shranjevanje poljubnega poligonalnega prereza. Točke prereza so podane z oznako in dvema koordinatama: x in y. Rešitve: [xml](/src/python/primer.xml) | [json](/src/python/primer.json)
- Izdelajte XML dokument, ki vsebuje podatke o dveh geografskih točkah (ime/naslov, koordinate, nadmorska višina)
- Povezave:
	- [uvod-v-xml-zacasno.pdf](/files/uvod-v-xml-zacasno.pdf)
    - [XML standard](https://www.w3.org/standards/xml/)
    - [W3C](https://www.w3.org)
    - [JSON](https://www.json.org)
    - [IFC](https://www.buildingsmart.org/standards/ifc)
    - [KML](https://developers.google.com/kml/?hl=en)

{{< figure src="https://imgs.xkcd.com/comics/standards.png" >}}

### 8./9. teden - sreda, 9./16. 4. 2025

- Uvod v Python: zapisovanje in branje XML datotek

- Izvorna koda:
	- Zapis podatkov o prerezu v XML datoteko, [geokar-8-1.py](/src/python/geokar-8-1.py)
	- Zapis podatkov o prerezu v XML datoteko z uporabo Python XML knjižnice, [geokar-8-2.py](/src/python/geokar-8-2.py)
	- Branje podatkov o prerezu iz XML datoteke, [geokar-9-1.py](/src/python/geokar-9-1.py)
    - Podajanje imena vhodne datoteke s podatko o prerezu v ukazni vrstici, [geokar-9-2.py](/src/python/geokar-9-2.py)
    - Podajanje imena vhodne datoteke s podatko o prerezu v ukazni vrstici, [geokar-9-3.py](/src/python/geokar-9-3.py)
    - Ostale potrebne datoteke ... [geometrijske_karakteristike.py](/src/python/geometrijske_karakteristike.py), [geokar-podatki.txt](/src/python/geokar-podatki.txt), [geokar-podatki.xml](/src/python/geokar-podatki.xml)

{{< figure src="/img/py-geokar-xml.png" >}}

### 10. teden - sreda, 23. 4. 2025
Knjižnice: [NumPy](https://www.numpy.org), [SciPy](https://scipy.org), [matplotlib](https://matplotlib.org)

Python in SQL:
- Baze podatkov: [SQLite](http://www.sqlite.org), [MySQL](http://www.mysql.com), ...
- [Uporaba Python/SQL](http://www.python-course.eu/sql_python.php)
- Zapis podatkov v bazo SQLite: [geokar-xml2db.py](/src/python/geokar-xml2db.py), [geokar-podatki.xml](/src/python/geokar-podatki.xml)
- Iskanje podatkov v bazi SQLite: [geokar-10-1.py](/src/python/geokar-10-1.py), [geometrijske_karakteristike.py](/src/python/geometrijske_karakteristike.py)

Python in Excel: 
-  Uporaba knjižnice [openpyxl](https://openpyxl.readthedocs.io/en/stable/#): [mb_primer-1.py](/src/python/mb_primer-1.py), [mb_primer-1.xlsx](/src/python/mb_primer-1.xlsx)
- Uporaba knjižnice [Pandas](http://pandas.pydata.org): [mb_primer-2.py](/src/python/mb_primer-2.py), [mb_primer-2.xlsx](/src/python/mb_primer-2.xlsx)

Python in numerične analize:
- Preprost primer izračuna sistema linearnih enačb, [linalg-1.py](/src/python/linalg-1.py)
- Izračun sistema linearnih enačb:
	- Program: [linalg-2.py](/src/python/linalg-2.py)
	- Podatki - [Matrix Market](https://math.nist.gov/MatrixMarket/): [info](http://math.nist.gov/MatrixMarket/data/SPARSKIT/fidap/fidapm37.html), [fidapm37.mtx](/src/python/fidapm37.mtx), [fidapm37_rhs1.mtx](/src/python/fidapm37_rhs1.mtx)

Uporaba knjižnice PyPlot:
- Program za izris prereza: [geokar-plot.py](/src/python/geokar-plot.py)
- Podatki: [geokar-podatki-1.txt](/src/python/geokar-podatki-1.txt), [geokar-podatki-2.txt](/src/python/geokar-podatki-2.txt)

Datoteke: [numpy-matplotlib-sqlite.zip](/src/python/numpy-matplotlib-sqlite.zip)

{{< figure src="/img/fidapm37_lg_city.gif" >}}
{{< figure src="/img/py-geokar-pyplot.png" >}}

### 11. teden - sreda, 30. 4. 2025

Samostojno delo. Naloga objavljena v spletni učilnici.

### 12. teden - sreda, 7. 5. 2025

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

