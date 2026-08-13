---
categories:
  - "Emails"
published: 2026-08-11
created: 2026-08-13
labels:
  - "wPraktyce"
relevance: wysoka
tags:
  - "strategia-AI"
  - "context-engineering"
  - "automatyzacja"
---

# Piotr, czym nakarmisz swoje AI

Autor newslettera (Patryk Łopot, wPraktyce.AI) opisuje rozmowę z firmą techniczną, która chciała nauczyć AI rozpoznawania awarii na podstawie kilkunastoletniego archiwum zgłoszeń serwisowych — dopóki nie okazało się, że archiwum zawiera tylko informację, że coś się zepsuło, a nie jak to naprawiono. Na tym przykładzie formułuje tezę, że najdroższym mitem wdrożeń AI w polskich firmach jest przekonanie "mamy dane", podczas gdy w rzeczywistości firmy mają zapis zdarzeń, a nie zapis rozwiązań i decyzji. Proponuje prosty test trzech pytań do zastosowania przed startem wdrożenia, żeby sprawdzić, czy archiwum faktycznie nadaje się do nauczenia AI. Konkluzja: jeśli wiedza żyje w głowach ludzi, a nie w dokumentacji, trzeba ją najpierw wydobyć i zapisać, a dopiero potem budować na niej AI — odwrócona kolejność kosztuje najwięcej.

## Frameworki i metody
- **Test trzech pytań przed wdrożeniem AI** — dla procesu, który ma przejąć AI: (1) czy zapisujecie CO się stało, czy JAK to rozwiązaliście — sprawdź 5 ostatnich wpisów pod kątem decyzji i efektu; (2) czy nowy pracownik nauczyłby się z tego roboty, patrząc na archiwum bez komentarza; (3) gdzie ta wiedza żyje naprawdę — jeśli w głowach ludzi, a nie w dokumentach, to punkt startu, a nie gotowe dane.
- **Kolejność wdrożenia** — najpierw budowa sposobu zapisywania wiedzy (decyzji i ich efektów), dopiero potem [[AI]] uczone na tej podstawie; odwrócenie tej kolejności ("zaciągniemy archiwum") jest najkosztowniejszym błędem.

## Wnioski
- Zasada "śmieci na wejściu, śmieci na wyjściu" dotyczy [[AI]] tak samo jak każdego innego systemu — firmy mylą posiadanie archiwum zdarzeń z posiadaniem wiedzy o rozwiązaniach, co prowadzi do wdrożeń bez pokrycia w danych.
- Test trzech pytań to gotowe narzędzie do szybkiej diagnozy gotowości danych klienta przed rozpoczęciem projektu wdrożenia AI — można go stosować jako pierwszy krok audytu w pracy konsultingowej.
- Jeśli wiedza żyje wyłącznie w głowach ludzi (typowe też w małych i średnich organizacjach społecznych), projekt wdrożenia AI powinien zacząć się od procesu wydobycia i ustrukturyzowania tej wiedzy, a nie od wyboru narzędzia.

## Cytat
> AI nie wyciągnie z Twojego archiwum wiedzy, której tam po prostu nie ma.

## Zastosowanie
Test trzech pytań to gotowy, prosty framework do wykorzystania na wstępnych rozmowach z organizacjami przed projektami wdrożenia AI — pomaga szybko zdiagnozować, czy dane klienta (np. archiwa zgłoszeń, dokumentacja projektów) realnie nadają się do nauczenia modelu, zanim padnie obietnica gotowego rozwiązania.
