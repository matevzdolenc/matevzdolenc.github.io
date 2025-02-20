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
    data: [70, , , , , , , , , , , , , , ],
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


