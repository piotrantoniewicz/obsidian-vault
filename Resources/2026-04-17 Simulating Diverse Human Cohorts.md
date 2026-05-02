---
categories:
  - Emails
published: '2026-04-17'
created: '2026-05-01'
labels:
  - The Batch
relevance: wysoka
tags:
  - LLM
  - prompt-engineering
  - digital-campaigning
---
# Simulating Diverse Human Cohorts

Badacze z Google (Davide Paglieri, Logan Cross i zespół) zaproponowali metodę "Persona Generators" — podejście do symulowania zróżnicowanych kohort ludzkich z użyciem [[LLM]]. Kluczowy problem polega na tym, że standardowe podpowiedzi dla modeli językowych generują uśrednione odpowiedzi, nieodzwierciedlające pełnego zakresu opinii w ludzkiej populacji. Rozwiązaniem jest optymalizacja kodu generującego persony (nie samych person) za pomocą algorytmu ewolucyjnego [[AlphaEvolve]], który maksymalizuje różnorodność postaw na zdefiniowanych osiach. Wyniki pokazują 82% pokrycia możliwych odpowiedzi — wyraźnie powyżej dotychczasowych metod (Nemotron Personas: 76%, Concordia memory generator: 46%). Metoda otwiera praktyczną ścieżkę do badania opinii publicznej bez kosztownych badań fokusowych.

## Frameworki i metody

- **Definicja kontekstu i osi różnorodności (diversity axes)** — np. zaufanie do instytucji, tolerancja ryzyka, nastawienie do teorii spiskowych; określają zakres postaw, które mają pokrywać persony
- **Generowanie kwestionariuszy przez [[Gemini]] 2.5 Pro** — 30 kwestionariuszy na różne tematy (ochrona zdrowia, edukacja finansowa, teorie spiskowe); każdy zawiera kontekst, osie różnorodności i pytania w skali 1–5
- **Optymalizacja kodu przez [[AlphaEvolve]]** — algorytm ewolucyjny iteruje 500 razy na 10 wersjach kodu, maksymalizując 6 metryk różnorodności (m.in. średnia odległość wektorów odpowiedzi); wynikiem jest kod generujący 25 zróżnicowanych person
- **Symulacja odpowiedzi przez [[Concordia]] + [[Gemma]] 3-27B-IT** — biblioteka Concordia zarządza agentami; każda persona "odpowiada" na kwestionariusz jako wektor wartości 1–5
- **Ewaluacja różnorodności** — 6 metryk, m.in. stopień pokrycia możliwych odpowiedzi i średnia odległość między wektorami person; wybrany kod maksymalizuje ich średnią

## Kluczowe dane

- 82% pokrycia możliwych odpowiedzi przez Persona Generators (vs. 76% Nemotron Personas, 46% Concordia memory generator)
- 25 person generowanych na jeden kwestionariusz
- 500 iteracji [[AlphaEvolve]] potrzebnych do pełnej optymalizacji

## Wnioski

- Standardowe [[prompt-engineering|prompty]] persona dla [[LLM]] dają uśrednione, mało zróżnicowane odpowiedzi — optymalizacja kodu generującego persony zamiast samych person to kluczowa zmiana podejścia dająca rzeczywistą różnorodność
- [[AlphaEvolve]] jako metoda ewolucyjna do optymalizacji kodu otwiera nową klasę narzędzi do badań syntetycznych — szczególnie użytecznych w [[digital-campaigning|digital campaigningu]], gdzie testowanie komunikatów na realnych fokusach jest kosztowne
- Syntetyczne persony pokrywające pełne spektrum postaw mogą zastąpić wstępne badania odbiorców w kampaniach NGO — zarówno dla fundraisingu, jak i advocacy

## Cytat

> "Syntetyczne persony oferują intrygującą możliwość nawigacji przez wąskie gardło zarządzania produktem — trudność decydowania, co budować, gdy budowanie jest łatwe dzięki [[LLM]]."

## Zastosowanie

Metoda bezpośrednio przydatna do testowania komunikatów fundraisingowych i kampanijnych dla NGO bez kosztownych badań fokusowych — można wygenerować 25 zróżnicowanych person odzwierciedlających pełne spektrum postaw potencjalnych darczyńców lub wyborców. Przy tworzeniu strategii dla klientów NGO warto rozważyć [[Concordia]] jako szkielet do szybkich symulacji reakcji odbiorców przed wdrożeniem kampanii. Eksperyment z [[AlphaEvolve]] do optymalizacji promptów persona to też wartościowy kierunek dla własnego pipeline'u w dobryai.pl.
