---
categories:
  - Clippings
authors: ["[[Marek Staniszewski]]"]
url: "https://www.linkedin.com/pulse/jak-robi%C4%87-badania-marketingowe-z-ai-%C5%BCeby-mia%C5%82o-r%C4%99ce-i-staniszewski-sbczf/"
source: "[[Archives/2026-08-19 Jak robić badania marketingowe z AI żeby to miało ręce i nogi – albo o tym dlaczego LLM nie potrafią nie mieć jakiegoś zdania na temat|2026-08-19 Jak robić badania marketingowe z AI żeby to miało ręce i nogi – albo o tym dlaczego LLM nie potrafią nie mieć jakiegoś zdania na temat]]"
published: 2026-08-19
created: 2026-08-26
relevance: wysoka
tags:
  - "LLM"
  - "prompt-engineering"
  - "strategia-AI"
---

# Jak robić badania marketingowe z AI żeby to miało ręce i nogi – albo o tym dlaczego LLM nie potrafią nie mieć jakiegoś zdania na temat

Marek Staniszewski analizuje trzy sposoby wykorzystania LLM do prognozowania wyników badań marketingowych na przykładzie wyboru wariantu opakowania kawy: proste zapytanie w oknie czatu, „silicon sampling” (symulacja stu respondentów) oraz „predykcję rozkładu” (poproszenie modelu o oszacowanie procentowego rozkładu odpowiedzi). Pokazuje eksperymentalnie, że modele typu instruction-tuned nie próbkują z rozkładu, tylko zapadają się do jednej dominującej odpowiedzi (distributional collapse), przez co „sto symulowanych respondentów” to w praktyce jeden respondent powtórzony sto razy — a wynik silnie zależy od tego, jak sformułowano prompt, a nie od realnych preferencji konsumentów. Autor przywołuje badania naukowe pokazujące, że LLM dobrze radzi sobie z ustalaniem kierunków i rankingów (korelacja do 0,85–0,90 wg badania w „Nature”), ale zawodzi przy przewidywaniu konkretnych wartości procentowych na poziomie segmentów czy pojedynczych osób (korelacja rzędu 0,20). Wniosek praktyczny: LLM nadaje się do zawężania listy pomysłów i pretestów, ale nie do podejmowania decyzji progowych czy segmentacyjnych, gdzie liczy się dokładna wielkość efektu.

## Frameworki i metody

- **Metoda 1: zapytanie w oknie konwersacji** — pytanie modelu wprost „który wariant wybrać” daje jedną rekomendację eksperta, nie prognozę zachowań rynku; podatne na efekt kompromisu (wybór środkowej opcji) i niepowtarzalne między sesjami.
- **Metoda 2: [[silicon sampling]]** — wielokrotne zadawanie tego samego pytania przez API (bez pamięci konwersacji) jako symulacja pojedynczych respondentów; bez person model daje „distributional collapse” (100% tej samej odpowiedzi), z personami demograficznymi przesuwa się jedynie punkt zapadania (np. 93% na innym wariancie), nie tworząc realnego zróżnicowania.
- **Metoda 3: predykcja rozkładu (direct distributional prediction)** — zamiast symulować pojedynczych respondentów, model raz proszony jest o oszacowanie procentowego rozkładu odpowiedzi w całej próbie i segmentach; błąd względem danych ludzkich spada o ponad połowę względem agregacji person, ale wyniki w podgrupach pozostają niestabilne między powtórzeniami.
- **Test kontrolny „15 minut”** — przed zaufaniem predykcji AI warto poprosić 3 doświadczone osoby z zespołu o wypełnienie tej samej tabeli z przewidywaniami na kartce, żeby sprawdzić, czy AI rzeczywiście przewiduje lepiej niż eksperci.

## Kluczowe dane

- Korelacja predykcji LLM z realnymi wynikami badań społecznych: 0,85 (dla badań nieopublikowanych przed cutoffem modelu: 0,90) — badanie w „Nature” na 70 eksperymentach i ponad 119 tys. uczestników.
- Korelacja „cyfrowych bliźniaków” z odpowiedziami pojedynczych osób: tylko 0,20 (Columbia Business School, ponad 500 pytań na osobę).
- Eksperyment własny autora (Brazylia/Kolumbia): trafność kierunkowa modeli 80–85%, ale konkretne wartości procentowe różniły się od realnych nawet kilkukrotnie (np. rozpoznawalność Polski jako dostawcy: prognoza 10–18%, realnie 1–6%).

## Wnioski

- LLM dobrze radzi sobie z ustalaniem kierunku i rankingu (co jest ważniejsze, co wygra), ale systematycznie zawyża wielkość efektów i nie potrafi odwzorować obojętności respondentów — realne „nie mam zdania” model zawsze zamienia w jakąś opinię.
- [[Silicon sampling]] i symulacja person nadają się najwyżej do pretestów i weryfikacji zrozumiałości pytań ankietowych — nie do podejmowania decyzji progowych ani do wnioskowania o konkretnych segmentach, bo wyniki segmentowe są niestabilne między powtórzeniami.
- Zanim zaufa się predykcji AI w badaniu, warto porównać ją z szybką prognozą 2–3 doświadczonych osób z zespołu — często wypadają podobnie dobrze, co relatywizuje przewagę modelu.

## Cytat

> Model systematycznie przecenia to, jak bardzo ludzie coś zauważają i jak bardzo im na czymś zależy.

## Zastosowanie

Przy pracy z NGO i badaniach na potrzeby kampanii czy fundraisingu warto stosować metodę predykcji rozkładu do wstępnego zawężania pomysłów (np. warianty apeli fundraisingowych) i testowania zrozumiałości ankiet, ale nie traktować wyników jako substytutu realnych badań na darczyńcach, zwłaszcza przy decyzjach progowych. To dobry materiał do szkoleń z AI dla organizacji — pokazuje konkretne pułapki (distributional collapse, brak neutralności) i prosty test kontrolny do zastosowania przed zaufaniem prognozom AI.
