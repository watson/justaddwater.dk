---
title: "[DK] Danske Netbank Usability Problem"
date: "2011-04-10T23:19:55"
slug: "dk-danske-netbank-usability-problem"
url: "/2011/04/10/dk-danske-netbank-usability-problem/"
wp_id: 1454
categories: ["In Danish", "Usability"]
tags: []
---

\[English: From time to time, I will post stories in Danish, when I consider it to be specifically relevent to Danish usage, (or simply easier for me). Therefore, find the below story in Danish (and here is a translate article link, in case you want to read it in Englsh)\]

Da Danske netbank for et halvt års tid siden opdaterede brugergrænsefladen, var det for at gøre banken mere brugervenlig.\
En ting er dog blevet værre: Udbakke-metaforen. Nu er den gemt mere af vejen end nogensinde før.

Se fx her hvor jeg netop har lagt en regning i "udbakke" til betaling. Hvor lang tid var du om at finde den?\
[](/wp-content/uploads/2011/04/danske-netbank-udbakke-skjult.png)

[![](/wp-content/uploads/2011/04/danske-netbank-udbakke-skjult-300x271.png "danske-netbank-udbakke-skjult")](/wp-content/uploads/2011/04/danske-netbank-udbakke-skjult.png)

Lad os lige  spole noget tid tilbage. Danske bank proklamerede at man ville investere op mod 1.000.000.000 danske kroner i at gøre netbanken mere brugervenlig. De kalder initiativet "Bedre bank" ([link til "bedre bank" info](http://www.danskebank.dk/da-dk/bedrebank/Documents/bedrebank.html?page=posts&category_id=1&post_id=18 "Danske Bank: Bedre Bank")). Her er et screenshot med teksten "Vi investerer massivt i brugervenlighed".

[![](/wp-content/uploads/2011/04/danskebank-vi-investerer-massivt-i-brugervenlighed-tiltag_pic.jpg "danskebank-vi-investerer-massivt-i-brugervenlighed-tiltag_pic")](/wp-content/uploads/2011/04/danskebank-vi-investerer-massivt-i-brugervenlighed-tiltag_pic.jpg)

Jeg benytter mest netbanken til betaling af regninger. Udbakken er en feature, som opvejer en væsentlig ulempe ved Nem-Id sikkerheden: Jeg slipper for den irriterende Nem-Id kode ved hver transaktion. I stedet kan jeg bruge udbakken, og betale alle regninger i een samlet transaktion, så jeg kun skal bruge Nem-Id koden en gang for alle betalinger.

Som ofte før, sættes sikkerhed i modsætning til brugervenlighed: Der er den ulempe ved udbakken at brugeren selv skal huske at tømme den. Og i tilfældet med Danske Bank, er udbakken vildt let at overse.

## Problem: Udbakke let at overse

Hvor lang tid var du om at lokalisere udbakken på øverste screenshot. 1 sekund? 10 sekunder? Har du ikke fundet den endnu? Måske vidste du hvor du skulle kigge på forhånd. Jeg gjorde ikke. Og hvor pinligt det end måtte lyde, har jeg faktisk også lagt i udbakken, og glemt at tømme den. (Det er vel sket 3-4 gange det sidste år).

Lad os lige vende tilbage til screenshottet øverst. Jeg har netop lagt en regning til betaling i udbakke. Sådan her ser skærmen ud:

[![Udbakke er gemt af vejen i venstremenuen, og statusbeskeden står helt nederst i skærmen](/wp-content/uploads/2011/04/danske-netbank-udbakke-skjult-highlight-arrow.png "danske-netbank-udbakke-skjult-highlight-arrow")](/wp-content/uploads/2011/04/danske-netbank-udbakke-skjult-highlight-arrow.png)

Netbanken på billedet giver korrekt to vigtige informationer:

1\) Udbakken er ikke tom, og\
2\) Statusbeskeden viser at informationer jeg netop har indtastet, er gemt.

Hver af disse informationer er vildt vigtige. For **regningerne bliver ikke betalt før udbakken er tømt**, hvilket i sig selv er en vigtig information, Danske Bank udelader at skrive direkte. Disse informationer skal have 100% opmærksomhed i brugerens bevidsthed, men fylder kun 5% af skærmen.

Og statusbeskeden står endda nederst, hvor vi læser oppefra og ned.

Det meste af pladsen bliver faktisk brugt på indtastningsfelterne til en "ny transaktion" ("kontooverførsel" på skærmbilledet ovenfor). Dette er sikkert med tanke på, at folk somme tider vil indtaste flere overførsler, når de nu er i gang. Men vægtningen burde være omvendt, så man ikke overser at man har lagt i udbakken, og at udbakken kræver opmærksomhed.

## Mit forslag: Tydelig status, med link til handling

**Når udbakken er i brug er den vigtigst,** ellers betales regningerne ikke. Derfor SKAL udbakken fremhæves når den er i brug. Et par enkelte midler til at fremhæve beskeden er:

1\. Flyt vigtige beskeder til toppen.

2\. giv status større visuel vægtning (jeg har tilføjet lidt farve)

3\. Lav link til handling (jeg har skrevet "vis udbakke" som link i statusbeskeden)

## Det kunne eksempelvis gøres sådan her:

[![Mit forslag til en bedre anbefaling: Mere tydelig. Visuel vægt. Placeret så den ses først.](/wp-content/uploads/2011/04/danske-netbank-udbakke-better-confirmation-300x171.png "danske-netbank-udbakke-better-confirmation")](/wp-content/uploads/2011/04/danske-netbank-udbakke-better-confirmation.png)

## Bonustip: Advarsel hvis banken forlades med fyldt udbakke

Som en sidste krølle på halen ville jeg nok lige tilføje en skræddersyet meddelelse til en bruger som ved et uheld forlader netbanken:

"Din udbakke indeholder transaktioner, som ikke er betalt. Tryk OK for at forlade netbanken. Tryk annuller for at gå til udbakke".

Eller noget i den stil. Tilføj beskeden både ved log-af, timeout, og hvis brugeren forlader siden ved at bruge browserens "tilbage"-knap, lukker browser vinduet, eller skriver ny adresse i adresselinien.

Bemærk: For god ordens skyld bør jeg nævne at  jeg pt. arbejder for en kunde (Nordea) der er konkurrent til Danske Bank.
