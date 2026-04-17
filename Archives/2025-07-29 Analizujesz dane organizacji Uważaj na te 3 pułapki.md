---
type: Web
authors: '[[Klaudia Stano]]'
url: >-
  https://sektor3-0.pl/blog/analiza-danych-ngo-3-pulapki/?utm_source=newsletter&utm_medium=email&utm_term=2026-03-24&utm_campaign=6+pyta%C5%84+zanim+w%C5%82%C4%85czysz+AI+w+organizacji+
published: 2025-07-29T00:00:00.000Z
created: 2026-03-24T00:00:00.000Z
tags:
  - fundraising
  - strategia-organizacji
  - digital-campaigning
---


Ułatwienia dostępu

- Skalowanie treści 100%
- Czcionka 100%
- Wysokość linii 100%
- Odstęp liter 100%

![Analizujesz dane organizacji? Uważaj na te 3 pułapki ](https://sektor3-0.pl/wp-content/uploads/elementor/thumbs/Analizujesz-dane-organizacji-Uwazaj-na-te-3-pulapki-blog-r9dss6px5fb80ovy2zeau137jl8ynqtsp3s6v1771y.jpg "Analizujesz dane organizacji? Uważaj na te 3 pułapki blog")

Otwierasz arkusz z danymi. Zaczynasz robić wyliczenia i wykresy, a następnie przeklejasz wyniki do raportu lub prezentacji. Co może pójść nie tak? W tym artykule opiszę trzy pułapki, w które możesz wpaść, analizując dane i podzielę się wskazówkami, jak ich unikać.

**Otwierasz arkusz z danymi. Zaczynasz robić wyliczenia i wykresy, a następnie przeklejasz wyniki do raportu lub prezentacji. Co może pójść nie tak? W tym artykule opiszę trzy pułapki, w które możesz wpaść, analizując dane i podzielę się wskazówkami, jak ich unikać.**

W dalszej części wpisu będziemy bazować na danych o darowiznach fikcyjnej Fundacji ABC. Arkusz i obliczenia znajdziesz [tutaj](https://docs.google.com/spreadsheets/d/1uNf3KPdrWOWvLV45X9o7WwCDiKATl1DhCszotmuqCkE/edit?usp=sharing).

## Pułapka nr 1: Suma i średnia to tylko część historii

Wyobraź sobie, że pracujesz w Fundacji ABC i robisz [przegląd darowizn](https://docs.google.com/spreadsheets/d/1uNf3KPdrWOWvLV45X9o7WwCDiKATl1DhCszotmuqCkE/edit?gid=1385489244#gid=1385489244) indywidualnych z 2024 r.:

<table><colgroup><col> <col></colgroup><tbody><tr><td colspan="1" rowspan="1"><strong>Liczba darowizn</strong></td><td colspan="1" rowspan="1"><strong>853</strong></td></tr><tr><td colspan="1" rowspan="1"><strong>Suma darowizn</strong></td><td colspan="1" rowspan="1"><strong>801 500 zł</strong></td></tr><tr><td colspan="1" rowspan="1"><strong>Średnia kwota darowizny</strong></td><td colspan="1" rowspan="1"><strong>940 zł</strong></td></tr></tbody></table>

Wydaje się, że darczyńcy byli bardzo hojni – średnia kwota darowizny wyniosła prawie 1000 zł! Już prawie idziesz otwierać szampana z zespołem, ale… zaraz, zaraz… **czy średnia arytmetyczna na pewno jest dobrą miarą przeciętności?** Niekoniecznie.

Sprawdzasz dodatkowe statystyki i wyglądają one tak:

<table><colgroup><col> <col></colgroup><tbody><tr><td colspan="1" rowspan="1"><strong>Minimalna darowizna</strong></td><td colspan="1" rowspan="1"><strong>10 zł</strong></td></tr><tr><td colspan="1" rowspan="1"><strong>Maksymalna darowizna</strong></td><td colspan="1" rowspan="1"><strong>56 000 zł</strong></td></tr></tbody></table>

Zakres darowizn był bardzo zróżnicowany (a nawet: *ogromnie* zróżnicowany): od wpłat o równowartości espresso w kawiarni do przelewów rzędu kilkudziesięciu tysięcy złotych.

Gdy przyjrzymy się wpłatom jeszcze dokładniej, zauważymy, że fundacja otrzymała:

- 21 przelewów o wysokości powyżej 10 tys. zł,
- 832 darowizny o wysokości od 10 do 200 zł.

Mówiąc inaczej: 21 darowizn (stanowiących **2,5% wszystkich darowizn**) wygenerowało aż **89% wpływów**.

Czy zatem wyliczanie średniej arytmetycznej z tak rozproszonego rozkładu ma sens? Niestety, nie do końca. W takim wypadku lepiej sprawdzi się mediana:

<table><colgroup><col> <col></colgroup><tbody><tr><td colspan="1" rowspan="1"><strong>Mediana darowizn</strong></td><td colspan="1" rowspan="1"><strong>100 zł</strong></td></tr></tbody></table>

**Mediana wynosi „tylko” 100 zł i informuje o tym, że połowa darowizn była mniejsza, a połowa większa od tej kwoty.**

Skąd zatem taka wysoka średnia arytmetyczna (940 zł)? **Średnia ma to do siebie, że jest podatna na tzw. „wartości odstające”. Już kilka bardzo wysokich wpłat może ją mocno zawyżyć.** I tak właśnie jest w tym przypadku.

Mediana, w przeciwieństwie do średniej arytmetycznej, nie reaguje na wartości odstające i dlatego często jest lepszą miarą przeciętności.

Użyteczną miarą w przypadku takiej analizy może być również **dominanta**, która wskazuje, jaka wysokość wpłaty była najczęstsza w 2024 r.:

<table><colgroup><col> <col></colgroup><tbody><tr><td colspan="1" rowspan="1"><strong>Najczęstsza darowizna (dominanta)</strong></td><td colspan="1" rowspan="1"><strong>50 zł</strong></td></tr></tbody></table>

Podsumowując – warto przeanalizować więcej statystyk opisowych niż średnia arytmetyczna i suma, a także przyjrzeć się danym z kilku różnych stron.

## Pułapka nr 2: Więcej nie znaczy lepiej – potrzebny jest punkt odniesienia

Przejdźmy do analizy [darczyńców](https://docs.google.com/spreadsheets/d/1uNf3KPdrWOWvLV45X9o7WwCDiKATl1DhCszotmuqCkE/edit?gid=1288013472#gid=1288013472). W 2024 r. w sumie 450 osób indywidualnych wpłaciło środki na rzecz Fundacji ABC. Gdzie mieszkają darczyńcy? Jak wygląda ich rozkład geograficzny według województw? Ponieważ Fundacja prowadzi działania na terenie całej Polski, chcemy sprawdzić, gdzie udało nam się pozyskać największą liczbę darczyńców.

Analiza pokazuje, że aż 38% darczyńców pochodzi z trzech województw – śląskiego, wielkopolskiego i mazowieckiego:  [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20882%20898'%3E%3C/svg%3E)](https://sektor3-0.pl/wp-content/uploads/2025/07/Tabela1.png)Czy to oznacza, że w tych województwach działania marketingowo-fundraisingowe Fundacji były najskuteczniejsze? Niekoniecznie – pamiętasz pewnie z lekcji geografii, że **te trzy regiony są jednocześnie regionami o największej populacji** (tylko w innej kolejności: mazowieckie, śląskie, wielkopolskie). Fakt, że te trzy województwa znalazły się na podium, może wynikać po prostu z faktu, że mieszka tam najwięcej osób, a nie z efektywności naszych działań.

To, co warto zrobić, to **porównać geograficzny rozkład darczyńców Fundacji z rozkładem populacji Polski w wieku produkcyjnym** (zakładając, że to ta grupa wiekowa zwykle przekazuje darowizny). W ten sposób dowiemy się, czy są regiony, z których mamy więcej lub mniej wspierających niż wskazywałaby na to demografia.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201470%20896'%3E%3C/svg%3E) Z zestawienia wynika, że szczególnie **w województwach śląskim i pomorskim mamy więcej darczyńców, niż moglibyśmy się spodziewać (bazując na rozmieszczeniu populacji)**. Z kolei w województwach mazowieckim i małopolskim jest odwrotnie.

*Uwaga: oczywiście należy do takiej analizy podchodzić z ostrożnością, ponieważ liczba darczyńców w niektórych województwach jest dość niska i może się wahać z roku na rok – warto sprawdzić, czy podobne zależności występowały we wcześniejszych latach działania Fundacji.*

To, co chcę przekazać, to wskazówka, że **warto osadzać dane w kontekście** – może nam to pomóc dostrzec zależności, które nie są widoczne na pierwszy rzut oka.

Inny przykład: gdybyśmy chcieli sprawdzić, które województwa w Polsce są najbardziej zmotoryzowane, zamiast podawać całkowitą liczbę zarejestrowanych samochodów w danym regionie, lepiej obliczyć, **ile samochodów przypada na każde 1000 osób** – wszak populacja mazowieckiego prawie sześciokrotnie przewyższa populację województwa opolskiego.

## Pułapka nr 3: Próba to nie (zawsze) populacja

Wyobraź sobie taką sytuację: z ankiety, którą przesłałeś/przesłałaś w zeszłym miesiącu mailowo do wszystkich 450 osób wspierających finansowo Fundację ABC wynika, że **darczyńcy oceniają efektywność działań organizacji na 4.9/5**.

Czy jednak zdanie, które napisałam powyżej, jest poprawnie sformułowane?

Jeśli nie wszyscy darczyńcy wypełnili ankietę (a to się raczej nigdy nie zdarza), to powinniśmy powiedzieć: *„* ***Darczyńcy, którzy wypełnili ankietę****, oceniają efektywność działań Fundacji ABC na 4.9/5”.*

Wysyłając ankietę, otrzymujemy odpowiedzi od pewnej podgrupy – co gorsza **nielosowej**. Dobrowolne formularze wypełniają nieprzypadkowe osoby: na przykład takie, które są bardzo przywiązane do Fundacji i zadowolone z jej działań. Lub odwrotnie – osoby, które coś zdenerwowało i chcą wyrazić swoje niezadowolenie. Albo… osoby, które lubią wypełniać ankiety (poniższa grafika trafnie oddaje ten problem ).

![Źródło: sketchplanations.com/sampling-bias Tłumaczenie grafiki: „Otrzymaliśmy 500 odpowiedzi w ankiecie i dowiedzieliśmy się, że ludzie uwielbiają wypełniać ankiety!”. Widzisz pułapkę?](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202048%201736'%3E%3C/svg%3E)

Źródło: sketchplanations.com/sampling-bias. Tłumaczenie grafiki: „Otrzymaliśmy 500 odpowiedzi w ankiecie i dowiedzieliśmy się, że ludzie uwielbiają wypełniać ankiety!”. Widzisz pułapkę?

Oczywiście to nie znaczy, że nie warto robić ankiet. Ankiety mają ogromny sens! Na podstawie odpowiedzi respondentów (nawet nielosowych) możesz:

- wytropić potencjalne problemy,
- zauważyć mocne strony działań organizacji,
- postawić hipotezy badawcze,
- poznać język, którym posługują się darczyńcy.

**Ważne jest to, aby na podstawie niereprezentatywnej próby nie wyciągać wniosków dotyczących całej populacji.** Opisując dane i wyniki z ankiet/badań, zadbajmy o precyzję języka i uważajmy, aby nie wyciągać zbyt pochopnych wniosków.

## I jeszcze dwie pułapki

W praktyce obserwuję jeszcze dwa błędy – opiszę je bardzo krótko:

### Mylenie procentów i punktów procentowych

Przykład: jeśli odsetek darczyńców jednorazowych w 2023 r. wynosił 42%, a rok później 33%, to znaczy, że **obniżył się o 9 punktów procentowych** (a nie o 9%). Gdybyśmy chcieli wyrazić tę zmianę w procentach, powiedzielibyśmy, że **odsetek darczyńców jednorazowych spadł o 21%** (21% = efekt dzielenia 9%/42%).

### Mylenie korelacji z przyczynowością

Przykład: Jeśli zauważymy dodatnią korelację między wiekiem darczyńców a kwotą przekazywanych darowizn, nie oznacza to jeszcze, że starszy wiek powoduje hojniejsze darowizny. Taka zależność może wynikać z wielu innych czynników, np. większych dochodów. **Korelacja nie daje dowodów na przyczynowość** – **pokazuje jedynie powiązanie**.

[![Wizualizacja danych – narzędzia do opowiadania historii opartych o dane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201100%201100'%3E%3C/svg%3E)](https://elearning.sektor3-0.pl/obszary/wizualizacja-danych-narzedzia-do-opowiadania-historii-opartych-o-dane/)

Mam nadzieję, że wskazówki, które zebrałam w tym artykule, pomogą Ci uniknąć błędów i wyciągania pochopnych wniosków z danych, a jednocześnie zainspirują Cię do wzbogacenia i poszerzenia Twoich analiz.

Życzę Ci owocnej pracy z danymi!

## Na deser: BI\_NGO

Jeśli Twoja organizacji potrzebuje wsparcia w analizie i wizualizacji danych, sprawdź projekt BI\_NGO, który łączy NGO-sy z wolontariuszami – miłośnikami liczb. O efektach I edycji wolontariatu dla Fundacji Gajusz przeczytasz [w tym artykule](https://sektor3-0.pl/blog/jak-wizualizacja-danych-wspiera-komunikacje-organizacji-spolecznej-sprawdz-na-przykladzie-fundacji-gajusz/).

**Inne teksty, które Cię zainteresują:**

- [Dlaczego dane są ważne dla organizacji społecznej?](https://sektor3-0.pl/blog/dane-w-organizacji-spolecznej/)
- [Jak prezentować dane w organizacji społecznej? 11 praktycznych wskazówek](https://sektor3-0.pl/blog/dane-w-organizacji-spolecznej-jak-prezentowac/)
- [Bezpłatne narzędzia do tworzenia wykresów i map w NGO](https://sektor3-0.pl/blog/dane-w-organizacji-spolecznej-bezplatne-narzedzia/)

Newsletter

Dołącz do grona ponad 10 000 zaangażowanych subskrybentów i dwa razy w miesiącu otrzymuj nieodpłatnie nową dawkę wiedzy, inspiracji oraz technologicznych recenzji i porad od ekspertów i ekspertek programu Sektor 3.0.
