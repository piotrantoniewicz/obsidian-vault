---
categories:
  - Clippings
authors: ["[[Anshu Chimala]]"]
url: "https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
source: "[[Archives/2026-09-01 How to turn your AI into a world-class designer|2026-09-01 How to turn your AI into a world-class designer]]"
published: 2026-09-01
created: 2026-09-10
relevance: średnia
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "prompt-engineering"
---

# How to turn your AI into a world-class designer

Anshu Chimala (12 lat w Apple, projektowanie i prototypowanie produktów AI) pokazuje, dlaczego modele AI domyślnie tworzą przewidywalne, „sloppy" projekty — bo jako predyktory kolejnego tokenu wybierają rozwiązania najbardziej prawdopodobne, a nie najbardziej odważne. Proponuje trójetapowy proces (Discover → Define → Deliver), inspirowany metodą Double Diamond, dostosowany do pracy z agentami AI zamiast ludzkich projektantów. Kluczowa teza: żeby wydobyć z modelu prawdziwie oryginalny design, trzeba świadomie wypychać go poza domyślne, „bezpieczne" wybory — losowość, ambitne odniesienia inspiracyjne i pętle krytyki z osobnym „agentem-krytykiem". Artykuł jest praktycznym zbiorem technik promptowania, nie tylko teorią.

## Frameworki i metody

**Proces Discover → Define → Deliver (dla zespołu agentów AI):**
1. **Discover** — szerokie eksplorowanie kierunków, odważne, ambitne briefy projektowe, zamiast domyślnych, przewidywalnych wyborów modelu.
2. **Define** — nadanie indywidualnej tożsamości projektowej przez łączenie modeli i pchanie AI poza znane wzorce.
3. **Deliver** — dopracowanie efektu końcowego przez usuwanie zbędnych elementów i skupienie na kluczowych detalach.

**8 konkretnych technik w ramach tego procesu:**
1. **String Seed of Thought** — model generuje losowy ciąg alfanumeryczny i na jego podstawie buduje kierunek kreatywny (kolor, layout, typografia), zamiast domyślnych wzorców.
2. **Ambitne, konkretne prompty** — inspiracja z zewnątrz (gra wideo, styl architektoniczny, instalacja artystyczna) zamiast proszenia modelu o „coś unikalnego" wprost.
3. **Pętle sprzężenia zwrotnego z subagentami** — osobny „agent-krytyk" (np. mocniejszy model) ocenia zrzuty ekranu projektu wg jasnych, obiektywnych kryteriów i przyznaje ocenę do momentu osiągnięcia progu jakości.
4. **Generowanie obrazów** wzbogacające projekt (shadery, efekty 3D) zamiast domyślnych gradientów i kształtów kodowych.
5. **Generowanie wideo** do bardziej zaawansowanego ruchu — pętle animacji i płynne przejścia między stanami interfejsu.
6. **Wycinanie zbędnych elementów** — AI dodaje chętnie, rzadko odejmuje; ograniczanie liczby elementów podnosi odbiór jako premium.
7. **Usuwanie „AI tells"** — rozpoznawanie powtarzalnych wzorców typowych dla projektów AI i świadome unikanie ich.
8. **Ręczne przepisywanie treści (copy)** — tekst wygenerowany przez AI traktować jak „lorem ipsum": placeholder do przepisania ludzkim głosem.

## Wnioski
- Domyślne wyjścia modeli są przewidywalne, bo trening nagradza wybory bezpieczne i akceptowalne dla wszystkich — świadome „wypychanie" modelu poza tę strefę wymaga zewnętrznego źródła losowości lub bardzo konkretnego kierunku, nie samego proszenia o „coś unikalnego".
- Oddzielenie roli wykonawcy (tani, szybki model) od roli krytyka (droższy, mocniejszy model oceniający tylko zrzuty ekranu, bez kontekstu implementacji) daje bardziej obiektywną pętlę poprawy jakości niż samoocena tego samego agenta.
- Największym sygnałem projektu „AI slop" jest nadmiar — zbędne elementy, gradienty, przegadany tekst; polerowanie polega głównie na odejmowaniu, nie dodawaniu.

## Zastosowanie
Przydatne przy pracy nad własnymi narzędziami AI i przy szkoleniach z promptowania — konkretne techniki (seed strings, agent-krytyk, redukcja „AI tells") można pokazywać uczestnikom jako praktyczny warsztat podnoszenia jakości wyjść AI, nie tylko w kontekście designu wizualnego, ale ogólnie promptowania i pracy z subagentami.
