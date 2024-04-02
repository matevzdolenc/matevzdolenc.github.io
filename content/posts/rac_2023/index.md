---
title: Računalništvo 2023/24
date: 2024-02-21
draft: false
showDate: true
showDateUpdated: true
tags: ["ulfgg", "2023", "rac", "predavanje"]
showAuthor: false
---

{{< alert icon="comment">}}
Zgornja slika je bila ustvarjena z orodjem **Adobe Firefly 2**.
**Ukaz:** *a laptop on a desk with plans and paper in the background, laptop screen shows spreadsheet of numbers and charts*
{{< /alert >}}

## Splošne informacije

Cilj predmeta je pridobiti osnovna računalniška znanja, ki so potrebna v nadaljevanju študija ter kasneje pri samostojnem inženirskem delu. Predmetnospecifične kompetence, ki jih študent pridobi pri tem predmetu, so:
- poznavanje in razumevanje sodobne računalniške in informacijske tehnologije,
- poznavanje in razumevanje osnovnih konceptov sodobnega razvoja inženirske programske opreme,
- poznavanje in razumevanje temeljnega znanja, ki mu omogoča nadaljnje samoizobraževanje oz. nadgradnjo pridobljenih znanj s področja računalniške tehnologije.
        
### Urnik
- predavanja - ponedeljek, 10-12, P II/6
- seminar - ponedeljek, 12-13, P II/6
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
    data: [39, 30, 26, 22, 20, , , , , , , , , , ],
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

## Seminar

### 1. naloga

Pripravite načrt za spletno stran (vsebina, izgled, ...) - spletno stran boste izdelali v okviru 2. seminarske naloge. Načrt pripravite v dveh oblikah: (1) s programom MS Word in (2) v obliki LaTeX ali Markdown dokumenta.

MS Word dokument in ZIP datoteko LaTeX ali Markdown zapisa oddate v spletni učilnici najkasneje do 25.3.2024.

### 2. naloga

Samostojno izdelajte spletno stran, ki ste jo predlagali v 1. seminarski nalogi. Spletno stran oz. blog izdelajte na enem izmed brezplačnih servisov za gostovanje spletnih strani ali blogov ([Google Sites](http://sites.google.com/), [WordPress](http://wordpress.com/), [Wix](https://www.wix.com), ...)

Spletno stran pripravite najkasneje do 22.4.2024. Obvestilo o spletnem naslovu izdelane spletne strani oddate v spletni učilnici.

Povezave:
- the balance, [8 Popular Types of Web Hosting Services](https://www.thebalance.com/types-of-web-hosting-services-2532072)
- website.com, [Web Hosting](https://www.website.com/beginnerguide/webhosting/6/2/types-of-web-hosting-services.ws)

{{< figure src="/img/og-rac-2016-spletne-strani.png" caption="Nekaj primerov spletnih strani študentov OG.">}}

## Predavanja

### 1. teden - ponedeljek, 26. 2. 2024

- Uvod:
	* [Uvod v predmet- vsebina, program, osnovne informacije](/files/og-rac-2023.pdf)
	* [Posebnosti gradbeništva](/files/posebnosti-gradbenistva.pdf)
- Uvod v gradbeno informatiko:
	* [Splošno o gradbeni informatiki - značilnosti in posledice le-teh](/files/gradbena-informatika.pdf)
	* [Informacije, podatki, znanje](/files/informacije-podatki-znanje.pdf)
	
{{< figure src="/img/posebnosti-gradbenistva.png" caption="Posebnosti gradbeništva določajo uporabo in uvajanje informacijsko-komunikacijskih tehnologij v gradbenem sektorju." >}}

### 2. teden - ponedeljek, 4. 3. 2024

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

- Digitalni dokumenti:
	* [Digitalni dokumenti](href="http://media.matevzdolenc.com/ul-fgg/2022-2023/digitalni-dokumenti.pdf) - prednosti in slabosti, standardi, itd.
	* Excel - naslavljanje celic: absolutno/relativno, delo s formulami: pisanje/kopiranje, ...

{{< figure src="/img/md-latex-preview.png" caption="Markdown (levo) in LaTeX (desno) predogled." >}}

### 3. teden - ponedeljek, 11. 3. 2024

- Internet in splet:
	* [Uvod v Internet](/files/internet.pdf) - zgodovina, protokoli, ...
	* [Uvod v splet](/files/splet.pdf) - zgotovina, protokoli, uporaba, 1.0/2.0/3.0, ...

{{< figure src="/img/web2.png" caption="" >}}

### 4. teden - ponedeljek, 18. 3. 2024

- Internet in splet:
    * [Uvod v splet 2.0](/files/splet-2.0-rk.pdf)
    * [Osnove inženirske komunikacije](/files/komunikacija.pdf)

- Knjiga David Weinberger, “Everything is Miscellaneous: The Power of the New Digital Disorder”
	* [Vse je različno](/files/vse-je-razlicno.pdf)
    * [Everything is Miscellaneous](http://www.youtube.com/watch?v=x3wOhXsjPYM) - video
    * [Information R/evolution](http://www.youtube.com/watch?v=-4CV05HyAbM) - video

{{< figure src="/img/everything_is_miscellaneous.png" caption="" >}}

### 5. teden - ponedeljek, 25. 3. 2024

Spletna predstavitev je zagotovo ena izmed pomembnih odločitev, je rešitev, saj je pomemben in prodoren element komunikacije in (samo)predstavitve. Ne glede na to, ali želite predstaviti le sebe oz. imate že izdelano idejo in posel, morate biti v vsakem primeru prisotni in vidni tudi na spletu, saj ponuja veliko možnosti, kako se predstaviti in oblikovati svojo blagovno znamko na spletu.

Predstavitev:
- [Osebna spletna stran](http://media.matevzdolenc.com/ul-fgg/2022-2023/osebna-spletna-stran.pdf)

{{< figure src="/img/osebna-spletna-stran.png" >}}
