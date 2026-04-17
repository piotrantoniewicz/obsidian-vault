---
categories:
  - "Emails"
published: 2025-10-29
created: 2026-03-06
labels:
  - Alice
relevance: niska
tags:
  - narzędzia-AI
  - prompt-engineering
  - automatyzacja
---
# Copy, transform, paste with 1-click

[[LLM]]y są wyjątkowo skuteczne w transformacji tekstu (tłumaczenia, korekta, przepisywanie, reformatowanie) — to bezpośredni efekt ich architektury opartej na przewidywaniu kolejnego tokenu. Newsletter opisuje workflow oparty na Skills do transformacji tekstu w [[Alice]]: Skills z włączoną opcją „Copy to clipboard" wysyłają gotowy wynik wprost do schowka bez klikania, a tryb „Single-turn mode" wysyła tylko ostatnią wiadomość zamiast całej historii — oszczędza tokeny i przyspiesza działanie. Razem tworzą wzorzec micro-automatyzacji tekstu: zaznacz → skrót → wklej.

## Wnioski

- Transformacja tekstu to „sweet spot" [[LLM]] — korekta, tłumaczenie, przepisywanie w stylu, reformatowanie na post/notatkę/raport — NGO powinny budować bibliotekę takich Skills jako pierwszy krok wdrożenia AI.
- Tryb Single-turn dla operacji tekstowych to ważna optymalizacja kosztów: większość transformacji nie potrzebuje historii rozmowy, wystarczy ostatnia wiadomość — warto ten wzorzec stosować przy projektowaniu własnych AI workflows.
- Automatyczne kopiowanie odpowiedzi do schowka + skrót klawiaturowy to kompletna eliminacja friction przy powtarzalnych zadaniach tekstowych — model wart pokazania pracownikom NGO jako natychmiastowy quick win.

## Cytat

> [[LLM]]y działają przez przewidywanie kolejnego tokenu — dlatego tekst to ich mocna strona, a obliczenia i złożone rozumowanie wymagają osobnych narzędzi.

## Zastosowanie

Na szkoleniach AI dla NGO warto zacząć od budowania biblioteki 5 Skills do transformacji tekstu (tłumaczenie na angielski, korekta, przepisanie na post, streszczenie, formatowanie raportu) — to natychmiastowy quick win, który pokazuje wartość AI bez żadnej integracji ani konfiguracji.
