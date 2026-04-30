---
categories:
  - Emails
published: '2026-03-26'
created: '2026-04-30'
labels:
  - Mateusz Chrobok
relevance: średnia
tags:
  - trendy-AI
  - narzędzia-AI
  - strategia-AI
---
# Trochę ryzykuję z tym zdjęciem, ale...

Newsletter analizuje dwa duże tematy: wojnę o chipy AI (gdzie sankcje USA vs Chiny tworzą czarny rynek wart miliardy) oraz rosnące zagrożenie vishingiem wspomaganym deepfake'ami, zilustrowane atakiem na firmę ochrony danych Aura. Historia przemytu chipów Supermicro — zmiana etykiet suszarką do włosów, wartość 2,5 mld USD — ujawnia paradoks: im silniejszy zakaz eksportowy, tym bardziej kreatywni przemytnicy, a chipy AI to dziś najcenniejszy towar technologiczny. Atak na Aurę przez vishing pokazuje, że cała warstwa techniczna (VPN, monitoring, menedżer haseł) nie chroni przed jednym telefonem od sprawnego socjotechnika; [[Langflow]] miał krytyczną lukę RCE, od CVE do pierwszych ataków minęło zaledwie 20 godzin. W short newsach: [[GPT-4]] 5.4 przekroczył próg ludzki w obsłudze komputera na benchmarku OSWorld-V.

## Kluczowe dane

- Supermicro przemycił chipy Nvidii o wartości **2,5 mld USD** od 2022 roku
- Wzrost ataków vishingowych: **442%** w 2H 2024; **1265%** od uruchomienia ChatGPT
- Klonowanie głosu deepfake możliwe z **3 sekund** nagrania
- GPT-5.4 osiągnął **75%** na OSWorld-V, bijąc ludzki wynik 72,4%
- Deloitte szacuje straty z vishingu na **40 mld USD rocznie** do 2027

## Wnioski

- Krytyczna luka w [[Langflow]] — narzędziu używanym do automatyzacji — pokazuje, że okno między ujawnieniem CVE a pierwszym atakiem skurczyło się do godzin: aktualizacja narzędzi AI powinna być traktowana jako priorytet operacyjny, nie rutyna.
- Vishing wspomagany AI (deepfake głosu, perfekcyjne e-maile na podstawie LinkedIn) stanowi realne zagrożenie dla NGO przetwarzających dane darczyńców — warto wbudować ten temat do szkoleń z bezpieczeństwa cyfrowego.
- Koncentracja 40% globalnej produkcji DRAM w jednym kontrakcie [[OpenAI]]–Samsung/SK Hynix ilustruje ryzyko monopolizacji infrastruktury AI — użyteczny argument przy rozmowach z klientami o dywersyfikacji narzędzi.

## Cytat

> "Kto kontroluje chipy, kontroluje AI. Kto kontroluje AI, kontroluje następną dekadę."

## Zastosowanie

Luka w Langflow to bezpośredni sygnał do sprawdzenia wersji narzędzi używanych w automatyzacji procesów (Make.com, [[Langflow]], MCP). Temat vishingu i klonowania głosu jest użyteczny jako case study w szkoleniach z bezpieczeństwa cyfrowego dla NGO. Geopolityczna analiza rynku chipów dostarcza tła do rozmów z organizacjami o ryzyku uzależnienia od narzędzi AI jednego dostawcy.
