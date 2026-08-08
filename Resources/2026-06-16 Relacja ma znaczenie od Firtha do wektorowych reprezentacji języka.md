---
categories:
  - Clippings
authors: ["[[Marcin Wilkowski]]"]
url: "https://blog.humanistyka.dev/2026/06/relacja-ma-znaczenie-od-firtha-do-wektorowych-reprezentacji-jezyka?utm_source=newsletter"
source: "[[Archives/2026-06-16 Relacja ma znaczenie od Firtha do wektorowych reprezentacji języka|2026-06-16 Relacja ma znaczenie od Firtha do wektorowych reprezentacji języka]]"
published: 2026-06-16
created: 2026-08-05
relevance: niska
tags:
  - "LLM"
  - "narzędzia-AI"
  - "prompt-engineering"
---

# Relacja ma znaczenie: od Firtha do wektorowych reprezentacji języka

Artykuł broni semantyki dystrybucyjnej (idei, że znaczenie słowa wynika z jego sąsiedztwa, ukutej w 1957 r. przez [[John Rupert Firth|Johna Ruperta Firtha]]) jako solidnej podstawy modeli językowych — zamiast dyskutować, czy AI "myśli", proponuje traktować reprezentacje wektorowe jako narzędzie badawcze do analizy zmian znaczeń słów w czasie (*lexical semantic change*, LSC). Omawia dwa badania: analizę zmian semantycznych w starogreckim za pomocą [[word2vec]] oraz porównanie BERT i ChatGPT 3.5 w zadaniach wykrywania zmiany znaczenia słów. W obu przypadkach generowanie tekstu jest tylko jednym z zastosowań modeli językowych — autor podkreśla wartość traktowania ich jako reprezentacji języka do badań lingwistycznych.

## Frameworki i metody
- **Semantyka dystrybucyjna (distributional semantics)** — wyznaczanie znaczenia słowa na podstawie kontekstu (sąsiedztwa), w którym występuje; podstawa reprezentacji wektorowych w modelach językowych.
- **Lexical semantic change detection (LSC)** — metoda badania, jak zmienia się znaczenie słów w czasie, poprzez porównywanie wektorów tego samego słowa w różnych okresach (np. odległość kosinusowa).

## Kluczowe dane
- Korpus Diorisis Ancient Greek Corpus: ponad 820 tekstów literackich, ok. 10 mln tokenów, pięć okresów historycznych
- Słowo δείκνυμι (*deiknymi*) wystąpiło w korpusie ponad 4,5 tys. razy i posłużyło jako przykład zmiany znaczenia (od percepcji wzrokowej, przez język filozoficzny, do znaczenia ogólnego)
- W zadaniach wykrywania zmiany semantycznej [[BERT]] konsekwentnie osiągał lepsze wyniki niż ChatGPT 3.5

## Wnioski
- Modele językowe można wykorzystywać nie tylko do generowania tekstu, ale jako reprezentacje języka do badania jego historycznych przemian — to inny sposób myślenia o ich przydatności niż wyłącznie jako "maszyn do pisania".
- Mniejszy, wyspecjalizowany model ([[BERT]]) może przewyższać większy, ogólny model (ChatGPT) w wąsko zdefiniowanym zadaniu — nie zawsze większy model oznacza lepszy wynik.
- Analiza wektorowa wspiera, ale nie zastępuje klasycznych metod interpretacyjnych (close reading) — bez wiedzy kontekstowej wyniki matematyczne trudno sensownie zinterpretować.

## Cytat
> Poznasz słowo po towarzystwie, w jakim przebywa.

## Zastosowanie
Materiał ma charakter głównie edukacyjny i teoretyczny — buduje intuicję, jak działają reprezentacje wektorowe i czym różnią się modele typu BERT od generatywnych LLM. Może się przydać jako tło do tłumaczenia klientom mechaniki działania AI albo przy ocenie, czy do konkretnego wąskiego zadania nie lepiej sprawdzi się mniejszy, sprofilowany model zamiast dużego LLM.
