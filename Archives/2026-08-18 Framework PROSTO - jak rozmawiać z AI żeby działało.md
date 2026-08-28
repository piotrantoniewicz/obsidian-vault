---
type: "Web"
authors: "[[Konrad Krawczuk]]"
url: "https://chcedointernetu.pl/blog/framework-prosto-jak-rozmawiac-z-ai?utm_source=ActiveCampaign&utm_medium=email&utm_content=Zg%C5%82o%C5%9B%20si%C4%99%2C%20do%C5%82%C4%85cz%2C%20tw%C3%B3rz%20-%20mamy%20dla%20Ciebie%20bilety&utm_campaign=Zg%C5%82o%C5%9B%20si%C4%99%2C%20do%C5%82%C4%85cz%2C%20tw%C3%B3rz%20-%20mamy%20dla%20Ciebie%20bilety"
published: 2026-08-18
created: 2026-08-28
tags:
  - "prompt-engineering"
  - "szkolenia-AI"
  - "narzędzia-AI"
---


## TL;DR

PROSTO to sześcioetapowy szablon promptu (Profil, Rezultat, Odbiorca, Styl, Tło lokalne, Ocena) plus karta oceny 8 kryteriów. Napisałem go, żeby właściciele małych firm dostawali od AI content, który zamienia się w telefony, a nie w lajki. Testowałem na 10 000 syntetycznych promptów, żeby zobaczyć, gdzie ludzie realnie gubią jakość. Pobierz PDF, użyj szablonu, oceniaj wyniki.

## Dlaczego to napisałem

Rozmawiam co tydzień z właścicielami lokalnych firm z Rumi, Wejherowa, Redy, Gdyni. Coraz więcej z nich próbuje ChatGPT, Claude czy Perplexity do pisania postów, oferty czy odpowiedzi na opinie. Wynik często ten sam: **generyczny tekst, który brzmi jak sto innych postów w feedzie**. Klient nie dzwoni, bo nie ma powodu.

Problem nie leży w AI. Leży w prompcie. Angielskie frameworki (CLARITY, SOCRATES, ANTICIPATE) są fajne w teorii, ale żaden z nich nie wie, że w Rumi w maju masz sezon komunijny, a nowa piekarnia na Dąbrowskiego właśnie otworzyła promocję na chleb za 4 zł. Bez tego kontekstu AI daje odpowiedź dla "wszystkich" - czyli dla nikogo.

Chciałem coś, co działa **po polsku**, dla **lokalnego biznesu** i ma **wbudowaną ocenę**. Tak powstało PROSTO.

## Cały framework na jednej stronie

![Framework PROSTO - 6 kroków + karta oceny](https://chcedointernetu.pl/_emdash/api/media/file/01M0AMMGTNRSNHNNHRGJ6FVV24.png)

Klik, żeby powiększyć. Wersja do druku w PDF na dole wpisu.

Sześcioetapowy szablon zbudowany wokół pytań, które i tak zadaje sobie każdy właściciel firmy, zanim wypuści reklamę. Różnica: tutaj zadajesz je AI, zanim ono ci coś napisze.

**P - Profil.** Kim jestem, co robię, skąd jestem, co mnie wyróżnia.

**R - Rezultat.** Co chcę osiągnąć. Nie "napisz post", tylko "chcę, żeby dzwonili".

**O - Odbiorca.** Kto to ma zobaczyć, jaki ma problem, gdzie to zobaczy.

**S - Styl.** Ton, długość, format, czego unikać.

**T - Tło lokalne.** Sezon, konkurencja, lokalne wydarzenia, specyfika miasta.

**O - Ocena.** Karta 8 kryteriów. Zanim użyjesz wyniku - oceniasz go w skali 0-16.

## Krok po kroku z przykładami

![Framework PROSTO - jak wypełnić każdy krok, dobre i złe przykłady](https://chcedointernetu.pl/_emdash/api/media/file/01M0AMMV0ZB6C2ERM2A2M81B8C.png)

Klik, żeby powiększyć.

Na tej stronie masz konkretne "złe" i "dobre" wypełnienie każdej litery, dla przykładowej firmy remontowej z Wejherowa. Różnica między "Mam firmę budowlaną." a "Prowadzę firmę remontowo-budowlaną RemontMax w Wejherowie. Działamy 12 lat, 4 pracowników. Specjalizacja: remonty łazienek w blokach. Klienci wracają, bo robimy czysto i w terminie." decyduje o tym, czy AI napisze coś, co jest o **twojej** firmie, czy o "firmie budowlanej" - czyli o żadnej.

Ta sama zasada dotyczy pozostałych kroków. Konkret > ogólniki. Zawsze.

## Co pokazał benchmark 10 000 promptów

Zanim wypuściłem framework, chciałem sprawdzić **gdzie ludzie realnie gubią jakość**. Napisałem generator, który syntetyzuje prompty pięciu klas jakości (od "terrible" do "excellent") dla 25 typów firm i 15 miast w Polsce. Wyszło mi 10 000 kombinacji. Każdą oceniłem heurystycznym ewaluatorem (regexy + reguły) w oparciu o 8 kryteriów karty PROSTO.

**Trzy liczby, które wyszły z tego benchmarku:**

- **80% promptów** dostaje **0 punktów** za "Wyróżnia się od konkurencji"
- **55% promptów** nie definiuje odbiorcy ani lokalnego kontekstu
- Sam fakt oceny wyniku (a nie tylko pisania promptu) **podnosi finalny wynik o 18%**

Innymi słowy: nawet dobrze napisany prompt zwykle wypada generycznie, bo nikt nie pyta AI "co mnie wyróżnia od konkurencji". A jeśli już go napiszesz i **od razu oceniasz wynik zamiast publikować na ślepo** - z automatu masz o 18% lepszą treść.

### Rozkład wyników w 10 000 promptach

![Rozkład promptów wg tieru jakości](https://chcedointernetu.pl/_emdash/api/media/file/01KRVC0VXHRJTQ7PTM4163EN0M.png)

Rozkład promptów wg tieru jakości

Góra piramidy (excellent) to 5% populacji. Większość siedzi w "poor" i "basic". Framework nie wymyśla dodatkowej pracy - on tylko pokazuje **gdzie jesteś** i jak się ruszyć w górę piramidy.

### Które kryteria są najsłabsze

![Heatmapa: średnie punkty per kryterium](https://chcedointernetu.pl/_emdash/api/media/file/01KRVC0XVT5FQM72JS7WNGKAXJ.png)

Heatmapa: średnie punkty per kryterium

Cel mierzalny i CTA - ludzie sobie radzą (0.99/2). Ton, odbiorca, kontekst lokalny - połowa punktów (0.60). Wyróżnienie - **0.28/2**, katastrofa.

### Trzy kryteria do naprawy w pierwszej kolejności

![Top 3 najsłabsze kryteria](https://chcedointernetu.pl/_emdash/api/media/file/01KRVC0ZHCBQ8ZA2DCWEJDKJAB.png)

Top 3 najsłabsze kryteria

Wyróżnienie od konkurencji, ton marki, lokalny kontekst - jeśli twoje prompty mają te trzy rzeczy, wyprzedzasz **80% konkurencji, która tego nie ma**.

### Siła lokalnego kontekstu

![Wpływ lokalnego kontekstu na wynik](https://chcedointernetu.pl/_emdash/api/media/file/01KRVC115434DPK25YDB15H5PX.png)

Wpływ lokalnego kontekstu na wynik

Prompty z konkretnym lokalnym tłem (miasto, sezon, wydarzenie) mają średnio o 3.4 punktu wyższy wynik. To najprostsze ulepszenie promptu jakie możesz zrobić dzisiaj: dodaj jedno zdanie "Jest \[miesiąc\], sezon \[X\], konkurencja robi \[Y\]".

### Boxplot per tier

![Boxplot: rozkład wyników per tier](https://chcedointernetu.pl/_emdash/api/media/file/01KRVC12P3TJPW7F6Q3KBZ613Q.png)

Boxplot: rozkład wyników per tier

Nawet w tierze "poor" trafiają się prompty, które wyskakują w górę. Framework nie gwarantuje, że zawsze będzie excellent - gwarantuje, że **wiesz na czym stoisz** i widzisz co poprawić.

### Sam ewaluator zmienia wynik o 18%

![Wpływ ewaluatora na finalny wynik promptu](https://chcedointernetu.pl/_emdash/api/media/file/01KRVC14FJZ8B0FZER6JBYDMMK.png)

Wpływ ewaluatora na finalny wynik promptu

To dla mnie najważniejszy wykres z całego badania. Większość frameworków kończy się na "napisz dobry prompt i wyślij". PROSTO ma szósty krok - **Ocena** - i to on robi różnicę. Nie publikuj wyniku, który nie przeszedł przez kartę 8 kryteriów.

## Karta oceny PROSTO

Po tym jak AI zwróci Ci wynik, oceniasz go w skali 0-2 za każde z 8 kryteriów. Prompt ewaluacyjny (do wklejenia razem z wynikiem):

> Ocen poniższy tekst według karty PROSTO. Daj punkty 0-2 za każde z 8 kryteriów. Podsumuj łączny wynik i powiedz, co konkretnie poprawić.
> 
> Kryteria:
> 
> 1\. Cel jest mierzalny
> 
> 2\. Odbiorca się rozpozna
> 
> 3\. Lokalny kontekst jest widoczny
> 
> 4\. Ton pasuje do marki
> 
> 5\. Jest konkretne CTA
> 
> 6\. Nie ma "napompowanego" języka
> 
> 7\. Długość jest odpowiednia
> 
> 8\. Wyróżnia się od konkurencji
> 
> Tekst do oceny:
> 
> \[WKLEJ TUTAJ\]

**Interpretacja wyniku:**

- 14-16 punktów: publikuj
- 10-13 punktów: popraw słabe punkty i puszczaj ponownie
- 6-9 punktów: wymaga przeróbki, wróć do promptu i uzupełnij kontekst
- 0-5 punktów: zacznij od nowa, wróć do kroku P (Profil)

## Pobierz PDF frameworku

Zrobiłem dla was **kartę PROSTO na jedną stronę A4** do wydrukowania i trzymania przy monitorze. W wersji v2 dodałem szablon do kopiowania i pełny przykład dla salonu fryzjerskiego w Rumi.

[Pobierz Framework-PROSTO-v2.pdf](https://chcedointernetu.pl/pdf/Framework-PROSTO-v2.pdf)

## Dlaczego to działa lepiej niż inne frameworki

**Po polsku.** Nie musisz pamiętać, co znaczy "Anticipate" czy "Ripple". Każda litera odpowiada polskiemu słowu, z którym pracujesz na co dzień.

**Z lokalnym kontekstem.** Żaden anglojęzyczny framework nie myśli o komuniach w Rumi ani o mieszkańcach osiedla Kaszubskiego w Wejherowie. PROSTO ma osobny krok na to, żeby ta wiedza dotarła do AI.

**Z wbudowanym ewaluatorem.** Nie zgadujesz, czy wynik jest dobry - **mierzysz**. Karta oceny robi z tego zamknięty cykl: prompt -> wynik -> ocena -> poprawa -> lepszy wynik.

**Praktyczny.** 6 kroków, każdy odpowiada na proste pytanie. Zero teorii, zero PhD. Kartka A4 i tyle.

**Skaluje się.** Działa tak samo dla posta na FB, jak dla strategii marketingowej na cały rok, jak dla briefu do agencji.

## Zacznij dziś

1. Pobierz PDF: [Framework-PROSTO-v2.pdf](https://chcedointernetu.pl/pdf/Framework-PROSTO-v2.pdf)
2. Wypełnij 5 pierwszych kroków (P R O S T) dla swojego biznesu
3. Wklej do AI (ChatGPT/Claude/Perplexity)
4. Wynik przepuść przez prompt ewaluacyjny (karta 8 kryteriów)
5. Jeśli mniej niż 10/16 - popraw i puszczaj ponownie

Framework jest darmowy. Jak wykorzystasz w swojej firmie i coś ci zadziała - **napisz mi na ratunku@chcedointernetu.pl**, chętnie zobaczę case i może zrobię z tego kolejny wpis.

\*Framework PROSTO opracowany przez Konrada Krawczuka (ChceDoInternetu.pl, Rumia). Wpis powstał po tym, jak zauważyłem, że właściciele lokalnych firm, które prowadzę przez wdrożenia AI - powtarzają te same błędy w promptach. Benchmark 10 000 promptów pomógł policzyć dokładnie, gdzie te błędy są najczęstsze. W kolejnym wpisie pokażę, co się stanie, kiedy Qwen 32B na moim GX10 poprowadzi agencję marketingową w Rumi przez 90 dni - z frameworkiem PROSTO i bez.