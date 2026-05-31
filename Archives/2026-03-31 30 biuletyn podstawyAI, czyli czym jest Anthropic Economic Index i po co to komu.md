---
type: "Web"
authors: "[[Przemek Jurgiel-Zyla]]"
url: "https://www.linkedin.com/pulse/czym-jest-anthropic-economic-index-i-po-co-komu-przemek-jurgiel-zyla-hjmbf/"
published: 2026-03-31
created: 2026-05-31
tags:
  - "trendy-AI"
  - "szkolenia-AI"
  - "strategia-AI"
---


### Kontekst, bo to ważne. Na rynku jest mnóstwo raportów o AI. McKinsey publikuje co kwartał, Gartner rysuje swoje krzywe, Stanford robi AI Index. Większość opiera się na ankietach, wywiadach z CEO albo analizie patentów.

Anthropic Economic Index jest inny. Korzysta z systemu Clio, narzędzia, które analizuje zanonimizowane konwersacje użytkowników Claude'a (z claude\_ai i z API). Każda konwersacja jest klasyfikowana według zadań z bazy O\*NET (amerykański system opisu kompetencji zawodowych), mapowana na zawody i stawki godzinowe. **Efekt: widzimy co ludzie faktycznie robią z AI.**

Piąta edycja obejmuje dane z 5–12 lutego 2026, próba to milion konwersacji z [claude.ai](http://claude.ai/) plus milion z API (Claude Code, integracje). Czwarta edycja była z listopada 2025, więc mamy trzymiesięczny interwał do porównania.

### I tu clue, to nie jest snapshot. To seria pomiarowa, piąta z rzędu. Trendy widoczne w danych zaczynają mieć statystyczną wagę.

Link do raportu: [https://www.anthropic.com/research/economic-index-march-2026-report](https://www.anthropic.com/research/economic-index-march-2026-report)

\---

## AI się demokratyzuje, i to widać w liczbach

Pierwszy wniosek z raportu to coś, co czuliśmy intuicyjnie, ale teraz mamy dane: zastosowania AI się rozpraszają.

Koncentracja użycia (top 10 zadań O\*NET jako % całego ruchu na [claude.ai](http://claude.ai/)) spadła z 24% w listopadzie 2025 do 19% w lutym 2026. Najniższy poziom w historii pomiarów. Ludzie używają AI do coraz bardziej różnorodnych rzeczy. Nie tylko kodowanie i pisanie esejów, coraz więcej niszowych, specjalistycznych zadań.

Co ciekawe, na API (Claude Code, integracje developerskie) trend jest odwrotny, koncentracja na top 10 zadaniach wzrosła do 33%. Profesjonalni programiści przenoszą się z [claude.ai](http://claude.ai/) na API, gdzie Claude Code rozbija złożone zadania na wiele mniejszych wywołań. Na [claude.ai](http://claude.ai/) zostaje coraz więcej „zwykłych" użytkowników z coraz bardziej różnorodnymi potrzebami.

## A jak to wygląda u nas (w Polsce)?

Programowanie i debugowanie to 17,9% konwersacji, wsparcie techniczne IT to 11,3%, łącznie prawie 30% ruchu to stricte technikalia. Ale zaraz za nimi mamy tłumaczenia i redakcję tekstów (8,9%), marketing i treści kreatywne (7,5%), pomoc w codziennym życiu (6,2%), edukację i STEM (łącznie ponad 11%).

*(patrz: wykres - kategorie zapytań, poziom wysoki)*

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQEmQ0N9j8U-7Q/article-inline_image-shrink_1000_1488/B4DZ05FnJsJoAU-/0/1774779266810?e=1781740800&v=beta&t=zGjaTogSZjbnFKL16BBOD3lkq7JRMStep9G0pQTXVLo)

Jedna rzecz mnie tu szczególnie zainteresowała: kategoria „treści marketingowe, kampanie reklamowe i SEO" plus „tworzenie i optymalizacja treści w mediach społecznościowych" dają łącznie prawie 5% polskiego ruchu. AI wchodzi do polskiego marketingu cyfrowego szybciej, niż wielu marketerów by przyznało. (Tak, pewnie część z Was czyta ten post napisany przy pomocy... no dobra, nie będę kończył tego zdania:P)

\---

## Wartość zadań spada na claude\_ai, rośnie na API

Średnia wartość zadania (mierzona stawką godzinową powiązanego zawodu w USA) spadła na claude\_ai z $49,3 do $47,9/h. Na API wzrosła z $50,4 do $50,7/h.

Na pierwszy rzut oka nic dramatycznego. Ale mechanizm pod spodem jest ciekawy.

Na claude\_ai przybywa „casual users", ludzie, którzy pytają o pogodę, porównują produkty, szukają prostych informacji. Wzrost użycia osobistego z 35% do 42% konwersacji to efekt rosnącej popularności (reklamy Super Bowl, organic growth). Jednocześnie wysokowartościowe zadania, głównie kodowanie, migrują na API. Programista, który wcześniej debugował w chacie, teraz robi to przez Claude Code.

Efekt netto: claude\_ai staje się bardziej „dla wszystkich", API bardziej „dla profesjonalistów". Ale nawet po spadku, średnia $47,9/h to wciąż wyraźnie powyżej mediany stawki w USA ($37,3/h). AI obsługuje głównie zadania wymagające wyższych kwalifikacji.

W naszych polskich danych podział personal vs. work jest prawie idealnie pół na pół, 46,6% osobiste, 45,1% zawodowe, 8,3% nauka i studia. Claude\_ai w Polsce to uniwersalny asystent, nie narzędzie wyłącznie dla devów. Moim zdaniem to jest kluczowa informacja dla każdego, kto buduje produkty AI na polski rynek, bo rynek nie jest tak techniczny, jak się wydaje z bańki twitterowej.

\---

## Augmentacja wygrywa z automatyzacją

Tu muszę się zatrzymać na chwilę, bo ten wniosek jest naprawdę ważny.

Wbrew narracji „AI zastąpi ludzi", dane pokazują coś odwrotnego. Na claude\_ai proporcja augmentacji (człowiek + AI współpracują) wzrosła do 53%, automatyzacji (AI robi samo) spadła do 44%. I co ciekawsze, im bardziej doświadczony użytkownik, tym WIĘCEJ augmentacji, nie automatyzacji.

Doświadczeni użytkownicy (konto starsze niż 6 miesięcy) w porównaniu z nowymi: mniej delegują dyrektywnie (29,4% vs. 38,1%, spadek o 8,7 pp), więcej iterują (28,2% vs. 24,5%), więcej się uczą (24,7% vs. 21,3%). I mają wyższy success rate: 73,1% vs. 66,7%.

Powtórzę, bo to jest ważne: ludzie, którzy naprawdę umieją korzystać z AI, nie outsourcują do niego więcej. Współpracują z nim lepiej. I osiągają lepsze wyniki.

U nas dominujące wzorce współpracy to dyrektywna (27,8%), uczenie się (26,6%) i iteracja zadania (23,1%). Pętla zwrotna 12,8%, walidacja 7,1%.

*(patrz: wykres - wzorce współpracy człowiek–AI)*

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQFRgTxD2ndAWw/article-inline_image-shrink_1000_1488/B4DZ05GsdkKMAQ-/0/1774779550543?e=1781740800&v=beta&t=Ne8RXAsvPtq1KFvHFqm5Ub8Snr0C7unm52hX8bgLnAk)

Prawie jedna czwarta konwersacji ma charakter iteracyjny, to nie jest „zrób mi prezentację", tylko wieloetapowa praca nad czymś. A ponad jedna czwarta to uczenie się. Polacy pytają AI „jak to działa?" częściej niż „zrób to za mnie". Widzę ten wzorzec też na warsztatach PodstawyAI, gdzie uczymy ludzi promptowania, więc dane mnie nie dziwią, ale fajnie mieć twarde potwierdzenie.

\---

## Learning curves, czyli najciekawsza część raportu

Piąta edycja ma jeden zupełnie nowy element, którego wcześniejsze raporty nie miały: analizę krzywych uczenia się. Moim zdaniem to jest najciekawsza część całego dokumentu, więc pozwolę sobie rozwinąć.

Anthropic zbadał, jak zmienia się skuteczność i wzorce użycia w zależności od stażu użytkownika. Podział: „high tenure" (konto starsze niż 6 miesięcy) vs. „low tenure" (reszta).

### Co wyszło?

Success rate: 73,1% vs. 66,7% u nowych. Różnica 6,4 pp. Co ważne, po kontroli regresyjnej (ten sam typ zadania, ten sam kraj, ten sam model) efekt nadal wynosi +4 pp. To nie jest kwestia tego, że „starzy wyjadacze" przynoszą łatwiejsze zadania. Nawet robiąc dokładnie to samo, osiągają lepsze wyniki.

Co więcej, przynoszą trudniejsze zadania (wymagane wykształcenie: 12,3 lat vs. 11,5 lat u nowych) i jednocześnie mają wyższy sukces. Paradoks tylko pozorny, kompetencja promptowania rośnie z doświadczeniem i kompensuje wyższy poziom trudności.

Używają Claude częściej do pracy (48,9% vs. 41,6%), mniej do celów osobistych. Zakres zastosowań bardziej rozproszony (top 10 zadań: 20,7% vs. 22,2%), z biegiem czasu odkrywają coraz więcej sposobów użycia. I co mnie szczególnie ciekawi: świadomie dobierają model do zadania. 55% zadań z kategorii Computer & Mathematical ląduje na modelu Opus (vs. 51% średnio). Każde dodatkowe $10/h wartości zadania zwiększa udział Opusa o 1,5 pp na claude\_ai i aż 2,8 pp na API.

Anthropic de facto udowodnił, że umiejętność pracy z AI jest mierzalną kompetencją, która rośnie z praktyką. Kompetencja, którą można trenować, nie jakieś wrodzone „wyczucie".

Dla mnie jako inwestora w Movens Capital to jest podwójnie interesujące. Widzę rosnący rynek szkoleń i narzędzi wspierających AI literacy. Ale widzę też ryzyko, firmy, które nie inwestują w upskilling swoich ludzi, będą tracić na efektywności nie dlatego, że AI jest słabe, ale dlatego, że ich ludzie nie umieją z niego korzystać. Dlatego sam prowadzę warsztaty PodstawyAI, bo widzę, jak ludzie po jednym dniu praktyki zaczynają inaczej formułować prompty i osiągać inne wyniki.

\---

## Nowe wektory automatyzacji w API

Raport identyfikuje dwa workflow, które co najmniej podwoiły swój udział w API między listopadem a lutym:

Automatyzacja sprzedaży i outreachu: generowanie materiałów sales enablement, kwalifikacja leadów B2B, wzbogacanie danych klientów, draftowanie cold maili. Oraz zautomatyzowany trading i operacje rynkowe: monitorowanie pozycji, proponowanie inwestycji, informowanie o warunkach rynkowych.

To nie jest „kiedyś AI będzie używane w sprzedaży". To jest „już jest i podwoiło się w trzy miesiące". Dla nas w Movens to bezpośredni sygnał dealflow: spółki budujące narzędzia AI dla sales/outreach i fintech/trading mają rosnący, empirycznie potwierdzony rynek.

\---

## Polska mapa adopcji AI wg województw

OK, to jest moja ulubiona część, bo tego nie znajdziecie w żadnym polskim raporcie o AI.

Dane Anthropic pozwoliły mi rozbić polskie konwersacje na województwa. Obraz jest ekstremalnie skoncentrowany.

*(patrz: wykres 04a — użycie Claude\_ai wg województw)*

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQHmUUH5v_sWSg/article-inline_image-shrink_1000_1488/B4DZ05HGDdGoAQ-/0/1774779655229?e=1781740800&v=beta&t=G1bh7ArDK3PLLSP8WM0SHJdxfywUYDOX8-S0pUFtynQ)

Mazowieckie: 55,5%. Ponad połowa wszystkich konwersacji z Polski. 5 167 rozmów w jednym tygodniu, ponad siedem razy więcej niż drugie w kolejności Wielkopolskie (684, 7,3%).

Piątka „big five" — Wielkopolskie, Śląskie, Pomorskie, Dolnośląskie, Małopolskie - tworzy drugą grupę, każde z mniej więcej 500–700 konwersacji. Poznań, Katowice/Gliwice, Gdańsk/Gdynia, Wrocław, Kraków. Dokładnie mapa polskiego IT.

Na drugim biegunie: Warmińsko-mazurskie (53), Opolskie (46), Lubuskie (18 konwersacji w całym tygodniu). Osiemnaście. Tyle co nic. // należy pamiętać, że Claude nie jest tak popularne w PL jak OpenAI (ChatGPT) oraz, że nie zawsze udaje się uzyskać precyzyjną lokalizację użytkownika.

To dane z jednej platformy (Claude\_ai), więc użytkownicy ChatGPT, Gemini i innych nie są tu widoczni. Ale proporcje między województwami prawdopodobnie odzwierciedlają ogólny pattern adopcji AI w Polsce, korelacja z mapą sektora IT i ośrodków akademickich jest niemal idealna.

**A teraz zaskoczenie:**

*(patrz: wykres - heatmapa kategorii zapytań wg województw)*

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQEa8GiZgloPKQ/article-inline_image-shrink_1000_1488/B4DZ05HcEGJ4AQ-/0/1774779745682?e=1781740800&v=beta&t=RT3PIpql2jB6tCunBG_9ASRGdmEToWhFGgWSs7-yFQ0)

Województwo lubelskie ma wysoki udział kategorii STEM/matematycznych, dużo więcej niż średnia krajowa (5,75%). Przy 339 konwersacjach to kilkadziesiąt rozmów o matematyce i fizyce. Może to efekt UMCS-u i Politechniki Lubelskiej? Może jest tam jakaś grupa studentów, która masowo używa Claude'a do zadań? Nie wiem. **Chętnie bym to lepiej zrozumiał, więc jeśli ktoś jest z Lublina i ma teorię, piszcie w komentarzach.**

\---

## Do czego Polacy konkretnie używają Claude'a?

Schodząc głębiej w dane, na poziomie konkretnych zadań zawodowych (klasyfikacja O\*NET) obraz jest jednoznaczny.

*(patrz: wykres - top 20 zadań zawodowych O* NET)\*

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQFmlgbylvYVgw/article-inline_image-shrink_1000_1488/B4DZ05IBTCKAAQ-/0/1774779898190?e=1781740800&v=beta&t=jJeEeanIrz1lMeO2DgR6hPsC7EWjU0PDMEmSLMjGbLc)

Top 5 to programowanie w różnych wariantach: naprawianie bugów (4,67%), pisanie nowych programów (2,95%), diagnostyka systemowa (2,28%), poprawa interfejsów i wydajności (2,00%), administracja systemami (1,89%). Pięć z sześciu najczęstszych zadań to IT.

Na szóstym miejscu redakcja i edycja tekstów (1,53%). Dalej pomoc studentom (1,08%), omawianie materiału w formie dyskusji (0,97%).

Na najniższym poziomie szczegółowości kategorii liderem jest weryfikacja poprawności, informacji, dokumentów, kodu, danych (1,86%). Polacy używają AI jako narzędzia kontroli jakości. Nie „zrób za mnie", ale „sprawdź, czy zrobiłem dobrze". To dojrzały wzorzec użycia.

Dalej: tłumaczenia z wytycznymi stylistycznymi (0,85%), dostosowywanie tonu postów w social media (0,64%), debugowanie gier wideo (0,59%). Tak, debugowanie gier. Ktoś w Polsce intensywnie robi gamedev na Claude'u:)

\---

## Nierówność geograficzna: dwa bieguny

Raport globalny identyfikuje niepokojący trend, który warto zestawić z polskimi danymi.

W USA konwergencja trwa, nierówność adopcji między stanami maleje. Współczynnik Gini dla stanów spadł z 0,37 (sierpień 2025) do 0,29 (luty 2026). Przy obecnym tempie wyrównanie nastąpi za 5–9 lat.

Globalnie odwrotnie, nierówność rośnie. Gini dla krajów wzrósł z 0,46 do 0,50 od sierpnia 2025. Top 20 krajów odpowiada za 48% per-capita usage (wzrost z 45%). Kraje o niskiej adopcji zostają coraz dalej w tyle.

Polska z 9 310 konwersacjami to 0,93% globalnego ruchu Claude'a. Mało czy dużo? **Mniej niż nasz udział w globalnym PKB z parytetem siły nabywczej (bliżej 1,2%), ale jesteśmy w grze, mamy aktywną społeczność techniczną i rosnący sektor AI.**

Natomiast patrząc na nasze wewnętrzne dane, 55,5% konwersacji z jednego województwa, 18 z innego, mamy u siebie dokładnie ten sam problem nierówności, który widać globalnie. Tyle że na mikroskali.

\---

## Czy AI jest niezbędne?

Jedno z ciekawszych pytań w badaniu dotyczyło tego, czy użytkownik mógłby wykonać zadanie samodzielnie, bez AI.

### W Polsce: 88,4% tak. Tylko 11,6% zadań wymaga AI w sensie, że człowiek nie poradziłby sobie sam.

Globalnie odsetek jest zbliżony (12,24%, wzrost z 12,09% w listopadzie).

Ważna interpretacja: to nie znaczy, że AI jest niepotrzebne. AI działa przede wszystkim jako akcelerator, przyspiesza rzeczy, które umiemy, ale które zajęłyby nam dłużej. Średni czas wykonania zadania przez człowieka solo: 184 minuty. Z pomocą AI: 14 minut. Ponad 13x przyspieszenie. To zmienia rachunek ekonomiczny pracy.

Jednocześnie rośnie (wolno, ale rośnie) odsetek zadań, przy których człowiek sam by sobie nie poradził. 12,24% to niewiele, ale to zadania, które wcześniej po prostu by nie powstały. AI zaczyna umożliwiać nową pracę, nie tylko przyspieszać istniejącą.

\---

## Moja perspektywa

Siedzę w tych danych od kilku dni i kilka wniosków nie daje mi spokoju. Pozwolę sobie na chwilę opinii, nie analityki.

AI literacy to nowa kompetencja zawodowa i wreszcie mamy twarde dane na poparcie. +4 pp success rate po kontroli zmiennych, regresja na milionowej próbie. Firmy, które traktują szkolenia AI jako coś opcjonalnego, popełniają ten sam błąd co firmy, które w 2010 traktowały tak kompetencje cyfrowe. W [Movens Capital](https://www.linkedin.com/company/movenscapital/) patrzymy na ten temat dwutorowo: inwestujemy w spółki budujące narzędzia AI, ale szukamy też founderów, którzy rozumieją, że adopcja to nie feature, to kompetencja organizacyjna.

Augmentacja wygrywa z automatyzacją, przynajmniej na razie. Kontrnarratyw do „AI zabierze nam pracę". Najbardziej produktywni użytkownicy nie delegują więcej, współpracują lepiej. Traktowanie AI jak czarnej skrzynki daje gorsze wyniki, traktowanie jak partnera do iteracji daje lepsze. Proste? W teorii tak. W praktyce widzę, że większość ludzi cały czas jest bliżej trybu „zrób za mnie".

Druga rzecz, o której nie mogę przestać myśleć: **polska mapa adopcji AI jest lustrem polskiej mapy IT.** 55,5% konwersacji z Mazowieckiego, 18 z Lubuskiego. Ten cyfrowy podział będzie miał konsekwencje gospodarcze za 3–5 lat, a mało kto o tym mówi.

No i migracja kodowania na API. Programiści przenoszą się z chatu do Claude Code, z augmentacji do bardziej zautomatyzowanych workflow. Zawody z kategorii Computer & Mathematical są jednocześnie najbardziej wspomagane przez AI i najbardziej narażone na disruption. Im lepiej AI radzi sobie z twoim zawodem, tym więcej ci pomaga, ale tym większe ryzyko, że kiedyś cię zastąpi. Nie tyle paradoks, co logiczna konsekwencja.

Dane są publiczne. Anthropic udostępnił raw data na Hugging Face. Każdy może to przeanalizować. **Polską perspektywę, którą opisuję powyżej, wyciągnąłem sam z tych danych.** To standard, który chciałbym widzieć u innych dostawców AI. OpenAI, Google, Meta, pamięciowo nie widzę żebyście cokolwiek podobnego publikowali:)

73,2% konwersacji polskich użytkowników kończy się sukcesem. Prawie trzy czwarte. Nie idealnie, ale wystarczająco, żeby ludzie wracali i coraz lepiej korzystali.

### Jak Wy korzystacie z AI w swojej pracy? Jesteście bliżej „zrób za mnie" czy bliżej „iterujmy razem"? Dajcie znać w komentarzach.

PS Wszystkie wykresy dotyczące Polski przygotowałem na podstawie surowych danych z Hugging Face, link do datasetu w komentarzu. Jeśli ktoś chce pogrzebać w danych swojego województwa, zachęcam:)

PS2 Raport ma ograniczenia, dane tylko z Claude'a, nie obejmują ChatGPT, Gemini i innych. Proporcje mogą być inne. Ale trendy współpracy człowiek–AI i krzywe uczenia się to moim zdaniem zjawiska uniwersalne, nie platform-specific.

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQFHoMUpswaQ6Q/article-inline_image-shrink_1000_1488/B4DZ05JI9UHcAQ-/0/1774780193614?e=1781740800&v=beta&t=gQzBr8gRstoBZ5UrZyU-azZI9KZXZnZrTIdg_nHhltA)

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQEYHVtSI41yZg/article-inline_image-shrink_1000_1488/B4DZ05JXFgHIAY-/0/1774780255766?e=1781740800&v=beta&t=P6YY1JLyLg4RETzo6IUv_DWysnmPVMpmDIMdbYGCW2g)

![Treść artykułu](https://media.licdn.com/dms/image/v2/D4D12AQE8YwGWDHuT0Q/article-inline_image-shrink_1000_1488/B4DZ05JfYGIcAQ-/0/1774780287769?e=1781740800&v=beta&t=d-b8tHAo5cCGSBLITi2IHh-t1vfDxNhJcCLqRS-tl9I)