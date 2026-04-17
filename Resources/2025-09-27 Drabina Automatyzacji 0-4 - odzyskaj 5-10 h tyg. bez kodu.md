---
categories:
  - "Emails"
published: 2025-09-27
created: 2026-03-06
labels:
  - Tomasz Woliński
relevance: wysoka
tags:
  - automatyzacja
  - strategia-AI
---
# Drabina Automatyzacji 0→4: odzyskaj 5–10 h/tyg. bez kodu

Tomasz Woliński przedstawia framework "Drabina Automatyzacji 0→4" — ewolucję od pracy ręcznej przez dokumentację i procedury (SOP), mikro-automaty, aż po pełną automatyzację z opcjonalnym Human-in-the-Loop (HITL). Kluczowa teza: nie każdy proces warto automatyzować do poziomu 4 — zatrzymanie na poziomie 2–3 jest racjonalne i nadal przynosi realną oszczędność czasu. Na przykładzie obsługi maili autor pokazuje, że porządek w danych (filtry Gmail) powinien poprzedzać automatyzację z [[LLM]], a agent w [[n8n]] z HITL pozwala oszczędzać czas bez utraty kontroli nad komunikacją.

## Wnioski
- Automatyzacja powinna zaczynać się od mapowania: najpierw ręcznie → notatki → SOP → mikro-automaty → full-auto; nie każdy proces trafia do poziomu 4 i to jest w porządku — i tak oszczędza to dużo czasu.
- Przed przekazaniem maili do [[LLM]] warto najpierw przefiltrować strumień filtrami [[Gmail]] (newslettery, faktury, VIP-y) — automatyzuj czyste dane, nie chaos skrzynki wejściowej.
- [[n8n]] z trybem HITL (Human-in-the-Loop) pozwala agentowi przygotowywać szkice odpowiedzi na bazie bazy wiedzy, a człowiek weryfikuje — realna oszczędność bez oddawania kontroli nad komunikacją.

## Cytat
> Nie ma sensu automatyzować rzeczy na siłę. Wiele procesów zostaje na poziomie 2 albo 3. I to jest ok — i tak oszczędza to bardzo dużo czasu.

## Zastosowanie
Framework 0→4 to gotowe narzędzie do priorytetyzowania, które procesy w NGO warto zautomatyzować i na jakim poziomie zatrzymać — zanim zainwestujesz czas klienta we wdrożenie [[Make.com]] lub [[n8n]].
