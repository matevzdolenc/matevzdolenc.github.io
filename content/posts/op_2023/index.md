---
title: Obdelava podatkov 2023/24
date: 2024-02-21
draft: false
showDate: true
showDateUpdated: true
tags: ["ulfgg", "2023", "op", "predavanje"]
showAuthor: false
---

{{< alert icon="comment">}}
Zgornja slika je bila ustvarjena z orodjem **Adobe Firefly 2**.
**Ukaz:** *a laptop on a desk with, laptop screen displays SQL, GIS and database design, google maps in the background*
{{< /alert >}}

## Splošne informacije

Podatkovni standard XML, uporaba standarda xml v geodeziji (GML in SVG), ontologije, objektno programiranje (programiranje razredov in objektov, knjižnice razredov, izdelava okenskih programov z grafiko, baze podatkov, jezik sql, načrtovanje in programiranje podatkovnih baz), izdelava porazdeljenih informacijskih sistemov (varnost podatkov, elektronski digitalni podpis, avtentikacija, šifriranje podatkov, standardi za varno izmenjavo podatkov, zlorabe podatkov), spletni in storitveni programi (xml spletne storitve, wsdl - jezik za zapis spletnih storitev, soa - servisno orientirana arhitektura, uporaba spletnih storitev v geodeziji), uporaba metod umetne inteligence v geodeziji, strojno učenje z nevronskimi mrežami.

### Urnik

- predavanja/vaje - ponedeljek, 10-13, soba 305
- predavanja/vaje - torek, 11-14, RU II/3

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
    data: [10, 9, 8, 8, 8, , , , , , , , , , ],
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

### 1. teden - torek, 27. 2. 2024

- Uvod:
	* [Uvod v predmet- vsebina, program, osnovne informacije](/files/op-2023.pdf)
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

### 2. teden - torek, 5. 3. 2024

- Uvod v Python:
	* Izvedba in zagon enostavnega Python programa/skripte (Spyder, iPython)
	* Seznami v Pythonu - for in while zanka
	* Uporabljeni ukazi: input(), print(), float(), import, math.pi

- Izvorna koda:
	* Python: [krog-1.py](http://media.matevzdolenc.com/python/src/krog-1.py")

{{< figure src="/img/py-ploscina-kroga-spyder.png" caption="Python program krog.py v programskem okolju Spyder." >}}

### 3. teden - torek, 12. 3. 2024

- Naloga: V programskem jeziku Python izdelajte program za izračun nekaterih vrednosti v poljubnem pravokotniku naslednjimi zahtevami:
	- Interaktivni vnos podatkov pravokotnika (stranici a in b).
    - Izračun in izpis ploščine, obsega ter dolžine diagonale podanega pravokotnika.
    - Izračun in izpis kota med diagonalo in osnovno stranico pravokotnika.
	- Rešiteve: 
    	- Vnos podatkov v več korakih - [pravokotnik-1.py](http://media.matevzdolenc.com/python/src/pravokotnik-1.py)
        - Vnos podatkov v eni vrstici - [pravokotnik-2.py]("http://media.matevzdolenc.com/python/src/pravokotnik-2.py)
		- Vnos podatkov ob zagonu programa - [pravokotnik-3.py](http://media.matevzdolenc.com/python/src/pravokotnik-3.py)

- Uvod v Python:
	- Zagon Python skript iz ukazne vrstice
    - Seznami: for in while zanka

- Izvorna koda:
	* [krog-1.py](http://media.matevzdolenc.com/python/src/krog-1.py")
	* [krog-seznam.py](http://media.matevzdolenc.com/python/src/krog-seznam.py")
	* [krog-range.py](http://media.matevzdolenc.com/python/src/krog-range.py")

{{< figure src="/img/py-izpis-tabele-krogov.png" caption="Izpis preproste tabele v konzolnem oknu." >}}

### 4. teden - torek, 19. 3. 2024

- Naloga: V programskem jeziku Python izdelajte program za izpis indeksov elementov poljube matrike:
	- Interaktivni vnos podatkov o velikosti matrike.
	- Izpis elementov matrike v obliki [i,j].
	- Rešitve: -
		<!-- - [matrika-1.py](http://media.matevzdolenc.com/python/src/matrika-1.py)
		- [matrika-2.py](http://media.matevzdolenc.com/python/src/matrika-2.py)
		- [matrika-3.py](http://media.matevzdolenc.com/python/src/matrika-3.py) -->

- Uvod v Python:
	- while zanka
    - izpis v datoteko
	- Uvoz tekstovnih podatkov v Excel in risanje razpršenih grafov.
	- Izvorna koda: - 
    	<!-- - Izračun ničle funkcije - bisekcija, [bisekcija-1.py](http://media.matevzdolenc.com/python/src/bisekcija-1.py), [bisekcija-2.py](http://media.matevzdolenc.com/python/src/bisekcija-2.py) -->

{{< figure src="/img/py-bisekcija-graf.png" caption="" >}}

### 5. - 6. teden - torek, 26. 3. 2024 in 2. 4. 2024

- Uvod v Python:
	- branje in zapisovanje tekstovnih datotek
	- vnos več podatkov v vrstici

- Primer: [Izračun geometrijskih karakteristik](/files/geokar-formule.pdf)

- Izvorna koda: 
	- Podatki v programu, [geokar-1.py](http://media.matevzdolenc.com/python/src/geokar-1.py)
	<!-- - Branje podatkov s tipkovnico (vsak podatek v svoji vrstici), [geokar-2.py](http://media.matevzdolenc.com/python/src/geokar-2.py)
    - Branje podatkov s tipkovnico (x in y koordinati v isti vrstici), [geokar-3.py](http://media.matevzdolenc.com/python/src/geokar-3.py)
    - Branje podatkov iz datoteke, [geokar-4.py](http://media.matevzdolenc.com/python/src/geokar-4.py)
    - Izračun ploščine s funkcijo, [geokar-5.py](http://media.matevzdolenc.com/python/src/geokar-5.py)
	- Vse geometrijske karakteristike, [geokar-6.py](http://media.matevzdolenc.com/python/src/geokar-6.py)
    - Testni podatki, [geokar-podatki.txt](http://media.matevzdolenc.com/python/src/geokar-podatki.txt) -->

{{< figure src="/img/py-geokar-sublimetext.png" >}}
