---
categories: Clippings
authors: ["[[Anthropic]]"]
url: https://www.youtube.com/watch?v=ysPbXH0LpIE
source: "[[Archives/2025-07-31 Prompting 101 Code w Claude|2025-07-31 Prompting 101 Code w Claude]]"
published: 2025-07-31
created: 2026-03-23
relevance: wysoka
tags:
  - "prompt-engineering"
  - "narzędzia-AI"
  - "strategia-AI"
---

# Prompting 101: Code w Claude

Hannah i Christian z zespołu Applied AI [[Anthropic]] prowadzą praktyczny webinar o prompt engineeringu na przykładzie systemu oceny roszczeń ubezpieczeniowych (formularz wypadku samochodowego w języku szwedzkim). Prezentacja przeprowadza przez 10 elementów dobrze zbudowanego promptu — od task context i tonu, przez background detail i przykłady, aż po reminders i formatowanie outputu. Kluczowy wniosek: prompt engineering to nauka empiryczna — iteracyjna, oparta na testowaniu konkretnych przypadków i stopniowym wzbogacaniu kontekstu. Dodatkowym narzędziem do debugowania promptów jest extended thinking w [[Claude]] 3.7/4, które pozwala zobaczyć jak model przetwarza dane przed udzieleniem odpowiedzi.

## Frameworki i metody

**10-elementowa struktura promptu wg [[Anthropic]]:**

1. **Task context** — opisz rolę modelu i cel zadania; bez tego model będzie zgadywał kontekst (np. pomylił wypadek samochodowy z narciarskim)
2. **Tone context** — określ pożądany ton i zachowanie (np. pewny, faktyczny, bez zgadywania gdy brak danych)
3. **Background detail / dokumenty / obrazy** — statyczne informacje o domenie, które nie zmieniają się między zapytaniami; idealne do system prompt i [[prompt caching]]
4. **Szczegółowe instrukcje** — lista kroków, w jakiej kolejności model ma analizować dane; kolejność ma znaczenie (najpierw formularz, potem szkic)
5. **Przykłady (few-shot)** — konkretne przypadki z trudnych, granicznych sytuacji z oznaczonym poprawnym outputem; najskuteczniejsze narzędzie poprawy jakości
6. **Historia konwersacji** — kontekst poprzednich wiadomości, szczególnie ważny w aplikacjach user-facing
7. **Dynamiczny content** — dane zmienne między zapytaniami (np. konkretny formularz do analizy)
8. **Przypomnienie zadania (reminder)** — ponowne podkreślenie kluczowych wytycznych na końcu promptu, m.in. zakaz halucynacji i zasady pewności odpowiedzi
9. **Formatowanie outputu** — struktura odpowiedzi (XML tags, JSON) dopasowana do potrzeb aplikacji downstream
10. **Pre-filled response (prefill)** — wskazanie jak model ma zacząć odpowiedź, eliminuje zbędny wstęp i wymusza pożądany format

**Organizacja informacji w prompcie:**
- Używaj tagów XML do oznaczania sekcji (np. `<user_preferences>`, `<final_verdict>`) — [[Claude]] był fine-tunowany na taką strukturę
- Markdown jest przydatny, ale XML daje większą kontrolę semantyczną
- Wszystkie stałe elementy (opisy formularzy, instrukcje domenowe) umieszczaj w system prompt

## Wnioski

- Kolejność analizy danych w instrukcjach ma kluczowe znaczenie — Claude powinien przetworzyć kontekst strukturalny (formularz) przed interpretacją niejednoznacznych danych (szkic odręczny); ta zasada przekłada się na każdy pipeline przetwarzania danych.
- Few-shot examples z trudnymi, granicznymi przypadkami są najskuteczniejszym narzędziem poprawy jakości outputu — szczególnie gdy dysponujemy ludzkimi labelami dla przypadków, które model regularnie myli.
- Extended thinking w [[Claude]] 3.7/4 pozwala zobaczyć tok rozumowania modelu — to cenne narzędzie diagnostyczne do identyfikowania gdzie prompt wymaga uzupełnienia i jak model interpretuje dostarczone dane.

## Zastosowanie

Struktura 10-elementowego promptu to gotowy szablon do zastosowania przy budowaniu narzędzi AI dla NGO — np. systemu klasyfikacji maili od darczyńców, automatycznego przetwarzania raportów czy asystenta do oceny wniosków grantowych. Techniki few-shot examples i output formatting (XML/JSON) są bezpośrednio przydatne przy rozwijaniu własnych pluginów [[Claude Code]] i automatyzacji w [[Make.com]]. Podejście iteracyjne opisane przez [[Anthropic]] — testuj, identyfikuj błąd, dodaj przykład do systemu — to dobra ramka metodyczna do przekazania uczestnikom szkoleń z AI dla organizacji.
