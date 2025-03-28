---
title: Programiranje in obdelava podatkov 2024/25
date: 2025-02-15
draft: false
showDate: true
showDateUpdated: true
tags: ["ulfgg", "2024", "pop", "predavanje"]
showAuthor: false
---

{{< alert icon="comment">}}
Zgornja slika je bila ustvarjena z orodjem **Adobe Firefly 2**.
**Ukaz:** *a laptop on a desk with, laptop screen displays SQL, GIS and database design, google maps in the background*
{{< /alert >}}

## Splošne informacije

Podatkovni standard XML, uporaba standarda xml v geodeziji (GML in SVG), ontologije, objektno programiranje (programiranje razredov in objektov, knjižnice razredov, izdelava okenskih programov z grafiko, baze podatkov, jezik sql, načrtovanje in programiranje podatkovnih baz), izdelava porazdeljenih informacijskih sistemov (varnost podatkov, elektronski digitalni podpis, avtentikacija, šifriranje podatkov, standardi za varno izmenjavo podatkov, zlorabe podatkov), spletni in storitveni programi (xml spletne storitve, wsdl - jezik za zapis spletnih storitev, soa - servisno orientirana arhitektura, uporaba spletnih storitev v geodeziji), uporaba metod umetne inteligence v geodeziji, strojno učenje z nevronskimi mrežami.

### Urnik

- predavanja/vaje - ponedeljek, 10-13, J-III/6 RU
- predavanja/vaje - torek, 8-11, J-IV/8 RU

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
    data: [13, 14, 14, 13, 12, 11, , , , , , , , , ],
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

### 1. teden - ponedeljek, 17. 2. 2025

- Uvod:
	* [Uvod v predmet- vsebina, program, osnovne informacije](/files/pop-2024.pdf)
	* [Posebnosti gradbeništva](/files/posebnosti-gradbenistva.pdf)
- Razvoj programske opreme:
	* [Agilni manifest](/files/agilni-manifest.pdf)
	* [Agilne metodologije](/files/agilne-metodologije.pdf)
- Uvod v programski jezik Python:
	* [Zakaj Python?](/files/zakaj-python.pdf)
	* Namestitev: [python.org](http://python.org), [Continuum Analytics - Anaconda](https://www.anaconda.com/download)
- Naloga:
	* Namestitev programskega sistema Python na domačem računalniku.
		
{{< figure src="/img/agilne-metodologije.png" caption="Agilne metodologije predstavljajo nabor vrednot." >}}

### 2. teden - ponedeljek, 24. 2. 2025

- Uvod v Python:
	* Izvedba in zagon enostavnega Python programa/skripte (Spyder, iPython)
	* Seznami v Pythonu - for in while zanka
	* Uporabljeni ukazi: input(), print(), float(), import, math.pi

- Izvorna koda:
	* Python: [krog-1.py](/src/python/krog-1.py)

{{< figure src="/img/py-ploscina-kroga-spyder.png" caption="Python program krog.py v programskem okolju Spyder." >}}

### 3. teden - torek, 4. 3. 2025

- Uvod v Python:
	- Zagon Python skript iz ukazne vrstice
	- Seznami: for in while zanka

- Izvorna koda:
	* [krog-1.py](/src/python/krog-1.py")
	* [krog-seznam.py](/src/python/krog-seznam.py")
	* [krog-range.py](/src/python/krog-range.py")

{{< figure src="/img/py-izpis-tabele-krogov.png" caption="Izpis preproste tabele v konzolnem oknu." >}}

### 4. teden - ponedeljek, 10. 3. 2025

- Naloga: V programskem jeziku Python izdelajte program za izračun nekaterih vrednosti v poljubnem pravokotniku naslednjimi zahtevami:
	- Interaktivni vnos podatkov pravokotnika (stranici a in b).
	- Izračun in izpis ploščine, obsega ter dolžine diagonale podanega pravokotnika.
	- Izračun in izpis kota med diagonalo in osnovno stranico pravokotnika.
	- Rešiteve: 
		- Vnos podatkov v več korakih - [pravokotnik-1.py](/src/python/pravokotnik-1.py)
		- Vnos podatkov v eni vrstici - [pravokotnik-2.py](/src/python/pravokotnik-2.py)
		- Vnos podatkov ob zagonu programa - [pravokotnik-3.py](/src/python/pravokotnik-3.py)

- Uvod v Python:
	- while zanka
    - izpis v datoteko
	- Uvoz tekstovnih podatkov v Excel in risanje razpršenih grafov.
	- Izvorna koda:
    	- Izračun ničle funkcije - bisekcija, [bisekcija-1.py](/src/python/bisekcija-1.py), [bisekcija-2.py](/src/python/bisekcija-2.py)

{{< figure src="/img/py-bisekcija-graf.png" caption="" >}}

### 5./6. teden - ponedeljek, 17./24. 3. 2025

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

### 7. teden - ponedeljek, 31. 3. 2025

- Uvod v Python: zapisovanje XML datotek

- Izvorna koda:
	- Zapis podatkov o prerezu v XML datoteko, [geokar-8-1.py](/src/python/geokar-8-1.py)
	- Zapis podatkov o prerezu v XML datoteko z uporabo Python XML knjižnice, [geokar-8-2.py](/src/python/geokar-8-2.py)

{{< figure src="/img/py-geokar-xml.png" >}}
