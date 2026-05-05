---
type: Web
authors: '[[Mateusz Wojdalski]]'
url: >-
  https://devstockacademy.pl/blog/branza-it-i-nowe-technologie/anthropic-1-mln-rozmow-claude-porady-osobiste-2026/?ml_recipient=186619854031161036&ml_link=186619836852340451&utm_source=newsletter&utm_medium=email&utm_term=2026-05-05&utm_campaign=Anthropic+przeanalizowa%C5%82+milion+rozm%C3%B3w+z+Claude+em+Wynik+zaskakuje
published: 2026-05-01T00:00:00.000Z
created: 2026-05-05T00:00:00.000Z
tags:
  - trendy-AI
  - LLM
  - szkolenia-AI
---


Sześć procent rozmów z Claude’em to nie kod, dokumenty czy tłumaczenia. To pytania o rzeczy, które kiedyś zarezerwowane były dla zaufanego znajomego, terapeuty albo doradcy zawodowego. Czy zmienić pracę. Jak rozmawiać z partnerem o przeprowadzce. Co zrobić z narastającym długiem na karcie kredytowej.

Anthropic opublikował raport “How people ask Claude for personal guidance” 30 kwietnia 2026. Firma przefiltrowała milion rozmów z marca i kwietnia 2026 (po deduplikacji 639 tysięcy unikalnych). Następnie wyciągnęła z nich obraz tego, jak naprawdę używamy modelu językowego, kiedy nikt nas nie widzi. Wyniki rzucają nowe światło na rolę AI w codziennym życiu, a przy okazji pokazują niepokojący wzorzec. Podobny temat dotykaliśmy już przy okazji [paradoksu Gen Z, która używa AI codziennie a jednocześnie jej nie ufa](https://devstockacademy.pl/blog/branza-it-i-nowe-technologie/gen-z-nienawidzi-ai-paradoks-badanie-gallup-2026).

## Co dokładnie zbadał Anthropic

Anthropic ma narzędzie o nazwie Clio (Claude Insights and Observations), które potrafi analizować rozmowy bez czytania ich treści przez ludzi. Mechanizm wygląda tak. Najpierw każdą rozmowę podsumowuje osobny model językowy. Następnie podsumowania są grupowane w klastry tematyczne, a dopiero te klastry trafiają do raportów. Dzięki temu analityk Anthropic widzi “pięć tysięcy rozmów o długu na karcie”, a nie konkretne treści ze szczegółami z życia użytkowników.

Po filtrze zostało 38 tysięcy rozmów. Wyleciał kod, transkrypcje, tłumaczenia, faktografia i burze mózgów biznesowych. To, co zostało, to rozmowy, w których ktoś naprawdę szukał perspektywy na decyzję, a nie informacji do skopiowania. Raport skupia się przy tym wyłącznie na rozmowach pisanych po angielsku przez interfejs claude.ai, dlatego obraz nie obejmuje API ani aplikacji firmowych.

Dlaczego to ważne? Dotychczas spór o to, czy ludzie traktują AI “jak narzędzie”, czy “jak rozmówcę”, był zasadniczo światopoglądowy. Każdy obstawiał, co chciał. Tymczasem Anthropic dał na to twardą liczbę. Sześć na sto rozmów to coś więcej niż kod. W efekcie mamy dyskusję, w której Claude pełni rolę rozmówcy, a nie interfejsu do GitHuba.

## Top cztery tematy: zdrowie, kariera, relacje, finanse

Trzy czwarte porad osobistych skupia się w czterech obszarach. Najwięcej rozmów dotyczy zdrowia i dobrostanu (27 procent). Drugą pozycję zajmuje praca i kariera (26 procent). Dalej idą relacje (12 procent) i finanse osobiste (11 procent). Pozostałe 24 procent rozdziela się natomiast między dziesiątki mniejszych kategorii: prawo, religia, edukacja, hobby, decyzje zakupowe.

> Raport Anthropic pokazuje obraz, który łatwo przegapić w debacie o produktywności AI: dla wielu ludzi Claude jest pierwszym numerem, do którego dzwoni się o trzeciej w nocy z pytaniem “co teraz”.

Co konkretnie ludzie piszą? Jeśli ufamy raportowi, formuły pytań są zaskakująco proste. “Czy powinienem przyjąć tę ofertę pracy?”. “Jak pomóc mamie, która prawdopodobnie ma początki choroby Alzheimera?”. “Mój chłopak mówi, że nie chce mieć dzieci, ja chcę. Co robić?”. “Mam 47 tysięcy długu na karcie. Od czego zacząć?”. To nie są pytania, na które Google odpowiada listą artykułów. To są bowiem pytania, na które ludzie szukają jednej, konkretnej odpowiedzi z perspektywą, jakby ktoś przeczytał właśnie ich życie.

Drugą obserwacją wartą zatrzymania jest to, że ludzie nie używają Claude’a tylko jako “podpowiadacza informacji”. Co więcej, często traktują go jak partnera do wewnętrznej rozmowy, której nie chcą prowadzić sami ze sobą w głowie. Pytają, formułują obawy, dostają odpowiedź, polemizują z nią, prosząc o inne ujęcie. Dlatego pojedyncza rozmowa o decyzji życiowej ma średnio dłuższą długość niż rozmowa techniczna.

## Sycophancy: kiedy Claude mówi nam to, co chcemy usłyszeć

Najciekawsze i najbardziej niewygodne odkrycie raportu dotyczy sycophancy (z ang. lizusostwo modelu), czyli skłonności modelu do przytakiwania użytkownikowi nawet wtedy, gdy lepiej byłoby się nie zgodzić. Anthropic mierzy to, badając ile odpowiedzi jest “wyraźnie zorientowanych na potwierdzenie tego, co użytkownik już sobie pomyślał”. Średnio takie lizusowate odpowiedzi pojawiają się w 9 procentach rozmów doradczych. Z jednej strony to niedużo. Z drugiej strony liczba mocno waha się w zależności od domeny.

W poradach o relacjach przytakiwanie skacze do 25 procent. Innymi słowy co czwarta rozmowa romantyczna albo rodzinna kończy się tak, że Claude zgadza się z narracją użytkownika nawet wtedy, gdy z perspektywy zewnętrznej widać, że narracja jest jednostronna. W rozmowach o duchowości i sensie życia liczba ta wynosi aż 38 procent. Niemal cztery na dziesięć rozmów o sensie życia kończy się więc tym, że model utwierdza użytkownika w jego dotychczasowym przekonaniu.

Dlaczego to problem? Anthropic w raporcie powołuje się na konstytucję modelu, która brzmi mniej więcej tak: “rozmowa z Claude’em powinna przypominać rozmowę z mądrym przyjacielem, który mówi szczerze”. Lizusowaty model nie jest jednak mądrym przyjacielem. Jest komplementem za pieniądze. Co gorsza, właśnie w tych domenach (relacje, sens życia), w których ludzie najbardziej potrzebują kogoś, kto potrafi powiedzieć “być może mylisz się w tej sprawie”, AI najczęściej milknie i przytakuje.

> Przytakujące AI w rozmowie o relacjach to trochę jak kolega, który po Twoich pierwszych dziesięciu zdaniach zawsze odpowiada “no jasne, ona jest beznadziejna”. Może przyjemnie, ale rzadko prawdziwie.

Anthropic zauważa, że problem jest jednocześnie naprawialny. Dlatego zespół wziął wzorce z tych 38 tysięcy rozmów, wygenerował na ich bazie syntetyczne scenariusze treningowe i użył ich do douczenia nowych modeli, w tym [Claude Opus 4.7 oraz Mythos Preview](https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/project-glasswing-anthropic-claude-mythos-cybersecurity-2026). Według wewnętrznych testów udało się obniżyć skłonność do przytakiwania w tych modelach o połowę. To dobra wiadomość, ale pokazuje też nieoczywistą prawdę. Bezpieczne i szczere AI to nie jest “domyślne” zachowanie modelu językowego. To jest świadomy wybór designerski wynikający z tego, co lab postanawia kosztem doświadczenia użytkownika.

Pierwsza Misja AI · Kodożercy

### Używasz AI codziennie, a czy robisz to dobrze?

Kurs Pierwsza Misja AI pokaże Ci techniki promptowania, które naprawdę działają. 27 ćwiczeń z prawdziwym GPT-4, gamifikacja i certyfikat.

[Sprawdź program kursu →](https://kursy.kodozercy.pl/pierwsza-misja-ai/?utm_source=devstockacademy-blog&utm_medium=article-banner&utm_campaign=pierwsza-misja-ai&utm_content=anthropic-1-mln-rozmow-claude-porady-osobiste-2026)

![Pierwsza Misja AI - Kodożercy](https://devstockacademy.pl/wp-content/uploads/2026/04/pierwsza-misja-ai-pudelko-1.png)

## Co to znaczy dla nas, którzy używamy AI na co dzień

Pierwsza lekcja z tego raportu jest prosta. Jeśli korzystasz z Claude’a (albo dowolnego innego modelu) do podejmowania decyzji życiowych, jesteś w większej grupie, niż mogłoby się wydawać. To nie jest dziwactwo, ponieważ takie zachowanie wykazuje kilka procent populacji, która ma dostęp do narzędzia. Nie ma w tym nic złego, dopóki rozumiesz, jak takie narzędzie działa.

Druga lekcja jest mniej przyjemna. Domyślny model pisze tak, żeby Ci się podobało. W sprawach technicznych to zwykle nie szkodzi, ponieważ kompilator i tak prawdę wyłapie. W sprawach życiowych jednak nikt potem nie skompiluje Twojej decyzji o rozstaniu. Dlatego warto formułować pytania tak, żeby model miał miejsce na powiedzenie “być może patrzysz na to wąsko”. Pytania w stylu “Czy popełniam błąd, jeśli zrobię X?” albo “Jakich argumentów przeciwko mojej decyzji nie biorę pod uwagę?” wymuszają na modelu krytyczną perspektywę. Z kolei pytania w stylu “Czy to prawda, że X?” zostawiają go w trybie potwierdzania.

Trzecia lekcja dotyczy granic. AI nie jest ani terapeutą, ani lekarzem, ani doradcą finansowym. Może być pierwszym ekranem, na którym uporządkujesz myśli. Pomoże sformułować pytanie. Pokaże też, jakie są opcje. Jednak nie zastąpi specjalisty w sprawach, gdzie stawką jest zdrowie, prawo czy duże pieniądze. Co ciekawe, sam Claude w rozmowach na takie tematy zwykle to zaznacza. To jeden z mocniejszych elementów konstytucji modelu, której Anthropic nie usuwa nawet pod presją użytkowników. Pokazuje też, że [napięcie między bezpieczeństwem a dostępem do potężnych funkcji jest centralne dla strategii Anthropic w 2026](https://devstockacademy.pl/blog/branza-it-i-nowe-technologie/openai-cyber-ograniczony-dostep-altman-mythos-2026).

## Podsumowanie

Raport Anthropic z 30 kwietnia 2026 pokazuje obraz korzystania z AI, który łatwo było wcześniej tylko czuć, a teraz mamy go potwierdzony liczbami. Sześć procent rozmów z Claude’em to nie technika, tylko życie. Najczęściej zdrowie, kariera, relacje i finanse, czyli razem 76 procent. Niepokojąca jest jednak jedna liczba. Co czwarta rozmowa o relacjach kończy się tym, że Claude przytakuje, zamiast podać kontrargument. W rozmowach o duchowości problem dotyczy z kolei niemal czterech na dziesięć przypadków. Dlatego korzystając z AI w sprawach osobistych, warto pytać tak, żeby zostawić mu miejsce na niezgodzenie się z Twoją wersją. Anthropic obniżył przytakiwanie w Opus 4.7 i Mythos Preview o połowę, jednak dyscyplina pytania spada na nas.

Newsletter · DevstockAcademy & Kodożercy

### Bądź na bieżąco ze światem IT, AI i automatyzacji

Co wtorek: newsy z branży, praktyczne tipy i narzędzia które warto znać. Zero spamu.
