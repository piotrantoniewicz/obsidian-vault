---
categories:
  - "Emails"
published: 2025-10-31
created: 2026-03-06
labels:
  - Alice
relevance: niska
tags:
  - automatyzacja
  - narzędzia-AI
  - prompt-engineering
---
# Connecting Alice to tools and automations

Remote Actions w [[Alice]] to mechanizm wysyłania danych do zewnętrznych narzędzi przez webhook — bez pisania kodu. Schemat jest prosty: definiujesz Skill z promptem opisującym oczekiwaną strukturę JSON, [[Alice]] przetwarza wiadomość użytkownika i wysyła JSON do webhooka [[Make]] lub [[Zapier]], automatyzacja wykonuje resztę w docelowej aplikacji. Przykład: „Dodaj spotkanie z Markiem jutro o 14" → [[Alice]] zwraca `{"due-date": "...", "task": "..."}` → webhook tworzy zadanie w [[Todoist]] lub wydarzenie w kalendarzu. To no-code bridge między AI a całym ekosystemem narzędzi.

## Wnioski

- Remote Actions to wzorzec integracji AI z narzędziami pracy dostępny bez programowania — kluczowy dla NGO, gdzie nikt nie pisze kodu, ale organizacja używa [[Make]], [[Zapier]] czy [[n8n]] do automatyzacji procesów.
- JSON jako lingua franca między [[Alice]] a automatyzacją to prosty, ale potężny wzorzec — warto go pokazać na warsztatach: prompt definiuje strukturę danych, a [[Make]]/[[Zapier]] obsługuje resztę.
- Projektowanie AI jako „asystenta który nie tylko rozmawia, ale naprawdę wykonuje akcje" to zmiana narracyjna ważna przy sprzedaży idei AI wewnątrz organizacji — różnica między chatbotem a agentem.

## Cytat

> Pomyśl o tym jak o nauce [[Alice]], by być Twoim osobistym asystentem — który nie tylko rozmawia z Tobą, ale naprawdę załatwia sprawy w Twoim cyfrowym świecie.

## Zastosowanie

Remote Actions + [[Make]]/[[Zapier]] to gotowy przepis na wdrożenie AI w procesach NGO bez IT — warto mieć przygotowane demo „powiedz coś, a AI to wykona" jako kulminacyjny moment szkolenia z automatyzacji dla organizacji.
