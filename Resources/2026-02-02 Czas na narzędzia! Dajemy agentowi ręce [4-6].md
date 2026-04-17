---
categories:
  - Emails
published: 2026-02-02
created: 2026-03-18
labels:
  - Robert Szewczyk
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - prompt-engineering
---
# Czas na narzędzia! Dajemy agentowi ręce 🛠️ [4/6]

Czwarta lekcja kursu budowania agentów AI w [[n8n]] dodaje "ręce" — narzędzia (tools) umożliwiające agentowi połączenie z zewnętrznymi aplikacjami przez API. Jako pierwsze narzędzie użyta jest Wikipedia (bez konfiguracji klucza API). Kluczowym elementem lekcji jest System Prompt — "DNA agenta": odgórna instrukcja działająca w tle rozmowy, definiująca rolę, osobowość i reguły korzystania z narzędzi. Przykładowy system prompt: "Jesteś asystentem AI; korzystaj z Wikipedii gdy szukasz odpowiedzi w internecie; odpowiadaj krótko i zawsze po polsku." Agent automatycznie decyduje, kiedy skorzystać z narzędzia, co można zweryfikować w zakładce "Executions". Lekcja zapowiada też możliwość delegowania zadań do sub-agentów (multi-agent architecture) i integracji z Google Calendar oraz Gmail w kolejnym kroku.

## Wnioski
- System Prompt jako "DNA agenta" to concept o fundamentalnym znaczeniu dla każdego wdrożenia AI w NGO — jasna definicja roli, języka, stylu i zasad korzystania z narzędzi zastępuje każdorazowe instrukcje użytkownika i zapewnia spójność odpowiedzi agenta dla wszystkich pracowników organizacji.
- Mechanizm "agent sam decyduje o użyciu narzędzia na podstawie System Promptu" eliminuje konieczność ręcznego sterowania i otwiera drogę do agentów pracujących autonomicznie — np. agent FAQ dla darczyńców, który sam sięga po aktualną bazę wiedzy NGO.
- [[n8n]] Executions jako logi debugowania pozwalają na monitoring zachowania agenta w organizacji (kiedy korzystał z jakiego narzędzia, co poszło nie tak) — to element transparentności i kontroli AI ważny przy wdrożeniach w NGO odpowiedzialnych przed donorami.

## Cytat
> "Narzędzia (tools) to dla agenta drzwi do zewnętrznego świata — dzięki nim może łączyć się z Twoimi ulubionymi aplikacjami i wykonywać w nich konkretne zadania."

## Zastosowanie
Piotr może zbudować agenta z System Promptem definiującym go jako "eksperta fundraisingowego NGO" i wyposażyć go w narzędzia dostępu do bazy wiedzy organizacji — gotowy asystent odpowiadający na pytania darczyńców spójnie i po polsku.
