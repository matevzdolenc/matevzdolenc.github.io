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
    data: [13, 14, 14, 13, 12, 11, 11, 9, 11, , , , , , ],
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

- Uvod v Python: zapisovanje in branje XML datotek

- Izvorna koda:
	- Zapis podatkov o prerezu v XML datoteko, [geokar-8-1.py](/src/python/geokar-8-1.py)
	- Zapis podatkov o prerezu v XML datoteko z uporabo Python XML knjižnice, [geokar-8-2.py](/src/python/geokar-8-2.py)
	- Branje podatkov o prerezu iz XML datoteke, [geokar-9-1.py](/src/python/geokar-9-1.py)
    - Podajanje imena vhodne datoteke s podatko o prerezu v ukazni vrstici, [geokar-9-2.py](/src/python/geokar-9-2.py)
    - Podajanje imena vhodne datoteke s podatko o prerezu v ukazni vrstici, [geokar-9-3.py](/src/python/geokar-9-3.py)
    - Ostale potrebne datoteke ... [geometrijske_karakteristike.py](/src/python/geometrijske_karakteristike.py), [geokar-podatki.txt](/src/python/geokar-podatki.txt), [geokar-podatki.xml](/src/python/geokar-podatki.xml)

{{< figure src="/img/py-geokar-xml.png" >}}

### 8. teden - ponedeljek, 7. 4. 2025

Naloga: Izdelaj program za menjalnico.

-  Programske zahteve:
	- program naj prebere trenutno tečajno listo iz XML datoteke
	- za podano vrednost v EUR naj program izpiše vrednosti v vseh ostali valutah
	- za podano vredno v izbrani valuti naj program izračuna ustrezno vrednost v EUR
- Pomoč:
	- Tečajno listo shranite na lokalni disk.
	- V XML datoteki lahko odstranite atribute korenskega XML elementa.
- Podatki:
	- [Banka Slovenije](http://www.bsi.si)
	- [Tečajna lista](http://www.bsi.si/_data/tecajnice/dtecbs.xml)
	- [Primer popravljena XML datoteke tečajne liste](/src/python/dtecbs.xml)
- Oddaja naloge:  
	- Vsebino izdelane naloge zapakirajte v paket .zip. Oddate vse uporabljene oz. ustvarjene datoteke (python program, podatki, ...).
	- Zip datoteko obvezno poimenujte takole: naloga-20250407-priimek-ime-vpisnaštevilka.zip
	- Nalogo oddate v spletni učilnici - naloga Menjalnica
- Rešitev:
	- Primer lokalno shranjene tečajne liste z odstranjenim imenskim prostorom, [dtecbs.xml](/src/python/dtecbs.xml)
	- Preprosta rešitev z lokalno datoteko in odstranjenim imenskim prostorom - implementiran samo prvi del naloge, ki za podan znesek v EUR izpiše vrednost v vseh ostalih valutah, [menjalnica-0.py](/src/python/menjalnica-0.py)
	- Preprosta rešitev z lokalno datoteko in odstranjenim imenskim prostorom, [menjalnica-1.py](/src/python/menjalnica-1.py)
	- Rešitev z branjem XML datoteke z Interneta, uporaba 2-D seznama, [menjalnica-2.py](/src/python/menjalnica-2.py)

{{< figure src="/img/py-menjalnica.png" >}}

### 9. teden - ponedeljek, 14. 4. 2025

Naloga: Izdelajte Python program, ki podane podatke v tekstovni datoteki pretvori v [KML](https://developers.google.com/kml/) zapis. KML datoteko poglejte v programu Google Earth.

Podatki (glej primer [KML-podatki.txt](/src/python/kml-podatki.txt)):
- 1 vrstica: center x-centra y-centra __# ime kraja in x in y koordinata kraja v decimalnih stopinjah__
- 2 vrstica: n __# število podanih krajev (celo število)__
- 3 + n vrstica: kraj x y __# kraj in x in y koordinata kraja v decimalnih stopinjah__

Navodila:
- Pripravite tekstovno datoteko s podatki oz. uporabite podatke v datoteki KML-podatki.txt. Za podatke si lahko npr. sestavite s podatki o koordinatah krajev od koder so študenti v letniku.
- V programu Google Earth pripravite preprost primer prikaza vaših izbranih podatkov. V programu shranite podatke v datoteko tipa KML (ne KMZ). V ustvarjeni datoteki preverite način zapisa uporabljenih podatkov. Natančno razlago zapisa KML datoteke lahko poiščete v [KML dokumentaciji](https://developers.google.com/kml/)
- Izdelajte program, ki ga zahteva naloga. Delovanje programa preverite na testnih podatkih.

Datoteke:
- [KML-podatki.txt](/src/python/KML-podatki.txt)
- [primer.kml](/src/python/primer.kml)

<!-- Rešitev: [kml-studenti.py](/src/python/kml-studenti.py) -->

{{< figure src="/img/kml-kraji.jpg" >}}

{{< figure src="/img/kml-kraji-crte.jpg" >}}

### 10. teden - ponedeljek, 28. 4. 2025

Samostojno delo. Naloga objavljena v spletni učilnici.

### 11. teden - ponedeljek, 5. 5. 2025

Naloga z Excelom.

Navodila:
1. V programu Excel pripravite tabelo s tremi stolpci. Vsak študent določi podatke za eno vrstico:
	- 1 stolpec: ime - ime študenta
	- 2 stolpec: število1 - poljubno realno število od -100 do 100
	- 3 stolpec: število2 - poljubno celo število od 0 do 100
2. Podatke iz programa Excel prenesite v tekstovno datoteko. Datoteko lahko dopolnite tako, da bo branje podatkov s programom, izdelanem v programskem jeziku Python, bolj preprosto.
V programskem jeziku Python izdelajte program, ki ...
	- prebere podatke iz datoteke, ki ste jo pripravili v točki 2 in prebrane podatke izpiše na zaslon v obliki tabele,
    - podatke izpiše v XML datoteko (oblika datoteke ni predpisana),
    - izračuna in izpiše na zaslon povprečno vrednost števil v 2. in 3. stolpcu tabele,
    - izračuna razliko med podanimi podatki v 2. in 3. stolpcu ter rezultate izpiše na zaslon in v izhodno tekstovno datoteko,
3. v datoteko, ki ste jo pripravili v 1. točki naloge, prenesite rezultate iz izhodne tekstovne datoteke in izdelajte graf teh rezultatov.
4. V programskem jeziku Python izdelajte program, ki prebere XML datoteko iz 3. točke naloge in podatke v obliki tabele izpiše na zaslon.
