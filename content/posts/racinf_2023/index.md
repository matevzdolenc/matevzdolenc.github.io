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
    data: [76, 67, 59, 58, 55, 58, 36, 46, 21, , , , , , ],
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

- Izvorna koda: -
          <!-- <ul>
            <li>19.4.2023: 
              <a href="http://media.matevzdolenc.com/python/src/geokar-20230419.py">geokar-20230419.py</a>, 
              <a href="http://media.matevzdolenc.com/python/src/geokar-podatki-20230419.txt">geokar-podatki-20230419.txt</a></li>
          </ul>
            <li>Zapis podatkov o prerezu v XML datoteko z uporabo Python XML knjižnice,
              <a href="http://media.matevzdolenc.com/python/src/geokar-8-2.py">geokar-8-2.py</a> </li>
            <li>Branje podatkov o prerezu iz XML datoteke,
              <a href="http://media.matevzdolenc.com/python/src/geokar-9-1.py">geokar-9-1.py</a></li>
            <li>Podajanje imena vhodne datoteke s podatko o prerezu v ukazni vrstici,
              <a href="http://media.matevzdolenc.com/python/src/geokar-9-2.py">geokar-9-2.py</a></li>
            <li>Podajanje imena vhodne datoteke s podatko o prerezu v ukazni vrstici,
              <a href="http://media.matevzdolenc.com/python/src/geokar-9-3.py">geokar-9-3.py</a></li>
            <li>Ostale potrebne datoteke ...
              <a href="http://media.matevzdolenc.com/python/src/geometrijske_karakteristike.py">geometrijske_karakteristike.py</a>,
              <a href="http://media.matevzdolenc.com/python/src/geokar-podatki.txt">geokar-podatki.txt</a>,
              <a href="http://media.matevzdolenc.com/python/src/geokar-podatki.xml">geokar-podatki.xml</a></li>
          </ul>
        </div> -->

{{< figure src="/img/py-geokar-xml.png" >}}

