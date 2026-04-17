---
categories:
  - "Emails"
published: 2025-10-28
created: 2026-03-06
labels:
  - Alice
relevance: niska
tags:
  - narzędzia-AI
  - prompt-engineering
  - szkolenia-AI
---
# Calling Assistants to a conversation in Alice

[[Alice]] umożliwia przywoływanie różnych asystentów w trakcie jednej rozmowy za pomocą @wzmianki — np. asystent sprzedażowy tworzy ofertę, a asystent compliance @wywoływany sprawdza ją przed wysłaniem, bez żadnego przełączania kontekstu. To wzorzec orkiestracji wielu wyspecjalizowanych agentów w jednym wątku. Autor podkreśla zasadę „lean assistant": każdy asystent powinien mieć jak najmniej integracji [[MCP]] — wąska specjalizacja eliminuje konflikty i poprawia jakość wyników. Kombinacja specjalizacji + Skills + @wywołanie to architektura multi-agent workflow bez kodu.

## Wnioski

- Wzorzec @wywołania wyspecjalizowanych asystentów to implementacja multi-agent orchestration dostępna bez żadnego kodu — to ważny koncept dla NGO chcących budować bardziej złożone AI workflow (np. asystent fundraisingowy + asystent redakcyjny + asystent publikacyjny).
- Zasada „lean assistant" (mało [[MCP]]ów, wąska specjalizacja) to dobra praktyka projektowania agentów AI niezależnie od narzędzia — warto ją stosować przy budowaniu własnych asystentów w [[Claude]] Projects czy podobnych systemach.
- Specjalizacja roli zamiast jednego wszechwiedzącego asystenta to zmiana myślenia o AI — kluczowa przy wdrożeniach organizacyjnych, gdzie różne osoby / procesy potrzebują różnych „trybów" AI.

## Cytat

> Prawdziwa magia? Wyspecjalizowani asystenci, każdy skupiony na jednej supermocy, wspierany przez Skills — @wywołujesz ich dokładnie wtedy, kiedy potrzebujesz.

## Zastosowanie

Przy projektowaniu AI workflow dla NGO warto zaproponować model kilku wąskich asystentów (@fundraising, @komunikacja, @dane) zamiast jednego ogólnego — wzorzec z [[Alice]] dobrze ilustruje tę architekturę na szkoleniach i warsztatach wdrożeniowych.
