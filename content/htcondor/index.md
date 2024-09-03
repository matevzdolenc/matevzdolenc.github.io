---
title: "HTCondor za inženirje"
description: "Naučite se osnovne uporabe visoko propustnega računskega okolja HTCondor."
showWordCount: false
showReadingTime: false
showDate: false
---

{{< lead >}}
{{< param "description">}}
{{< /lead >}}

[HTCondor](https://research.cs.wisc.edu/htcondor/index.html) je odprto-koden distribuiran sistem za upravljanje z računskimi viri (DRMS - Distributed Resource Management System). Sistem omogoča predvsem vzpostavitev visoko-propustni računskih okolij (HTC - high-througput computing), ki so primerna za analizo najrazličnejših parametričnih študij.

Video posnetki so v prvi vrsti namenjeni inženirjem in študentom gradbeništva, geodezije, strojništva, ki si želijo poenostaviti izvajanje različnih parametričnih študij ali pa le uporabiti računske vire, ki so prosti in dostopni.

Prepričan sem, da vam bodo video posnetki olajšali spoznavanje sistema HTCondor ter omogočili razvoj in izvedbo različnih, računsko zahtevnih analiz.

## 01 Uvod

Uvod v serijo izobraževalnih video posnetkov z naslovom HTCondor za inženirje.

{{< youtubeLite id="WJ4FH9tG6Po" label="HTCondor za inženirje | 01 Uvod" >}}
[Prezentacija](/htcondor/slides/uvod.pdf)

## 02 Računska okolja in parametrične študije

Za računsko analizo lahko uporabimo različna računska okolja. V gradbeništvu so zanimive predvsem parametrične študije. Za analizo le-teh pa so posebej primerna visoko-propusna računska okolja.

{{< youtubeLite id="ss3REGt96dI" label="HTCondor za inženirje | 02 Računska okolja in parametrične študije" >}}
[Prezentacija](/htcondor/slides/parametricne-studije.pdf)

## 03 Namestitev sistema HTCondor

Na osebni računalnik z operacijskim sistemom Windows 10 bomo namestili zadnjo verzijo sistema HTCondor ter uporabili dva osnovna ukaza: condor_status in condor_q. Namestitev na drugih operacijskih sistemih (Mac OS X, Linux) poteka zelo podobno.

{{< youtubeLite id="7m85UaS0wFA" label="HTCondor za inženirje | 03 Namestitev sistema HTCondor" >}}
[Prezentacija](/htcondor/slides/namestitev.pdf)

## 04 Prvi primer

V prejšnjem koraku smo na računalnik namestili osebni HTCondor. Sedaj je seveda potrebno preiskusiti ali nameščen sistem deluje. Izdelali bomo preprost program (BAT proceduro) ter napisali vhodno datoteko za sistem HTCondor s katero določimo način izvajanja našega programa.

{{< youtubeLite id="BHDVZ9fSSnQ" label="HTCondor za inženirje | 04 Prvi primer" >}}
[Prezentacija](/htcondor/slides/prvi_primer.pdf)

## 05 Več nalog

Zagon enega programa v sistemu HTCondor je lahko seveda primerno - če npr. želimo uporabiti oddaljen računalnik in ne obremenjevati našega. Vseeno pa je HTCondor v prvi vrsti namenjen zagonu več programov. Tokrat se bomo z našim primerom približali splošni parametrični analizi.

{{< youtubeLite id="j5eLFAcRoMg" label="HTCondor za inženirje | 05 Več nalog" >}}
[Prezentacija](/htcondor/slides/vec_nalog.pdf)

## 06 Več nalog in rezultatov

V prejšnjem koraku smo videli, da smo na koncu dobili, kot rezultat, le rezultat primera, ki se je izvedel zadnji. Tokrat bomo primer popravili tako, da bomo dobili vse rezultate. To bomo naredili z uporabo makra $(Process), ki nam omogoča, da uporabimo zaporedno številko procesa (naloge) za označevanje datotek.

{{< youtubeLite id="yJQ-JttpHvQ" label="HTCondor za inženirje | 06 Več nalog in rezultatov" >}}
[Prezentacija](/htcondor/slides/vec_nalog_in_rezultatov.pdf)



