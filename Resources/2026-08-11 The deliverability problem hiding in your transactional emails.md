---
categories:
  - "Emails"
published: 2026-08-11
created: 2026-08-13
labels:
  - "Civic Shout"
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
  - "organizacje-społeczne"
---

# The deliverability problem hiding in your transactional emails

Case study opisuje, jak Statue of Liberty & Ellis Island Foundation odkryła, że jej problemy z reputacją nadawcy brały się nie z kampanii fundraisingowych, lecz z maili transakcyjnych (potwierdzenia kont, potwierdzenia zakupu) wysyłanych przez Office 365 — platformę, która nie śledzi odbić i wypisów. Fundacja pozyskiwała 4-5 tys. nowych leadów miesięcznie z bazy rekordów historycznych, więc niewidoczne złe dane szybko się kumulowały i zaniżały reputację całej domeny. Tekst pokazuje praktyczny, czteroetapowy plan naprawy infrastruktury mailowej oraz przypomina, że maile fundraisingowe i transakcyjne dzielące domenę wzajemnie się „zarażają" problemami z dostarczalnością.

## Frameworki i metody
- **Czteroetapowa naprawa dostarczalności** — 1) walidacja całej bazy maili przez [[Bouncer]] w celu usunięcia niedostarczalnych adresów; 2) wydzielenie subdomeny dla maili fundraisingowych, by chronić reputację domeny głównej i izolować problemy wg typu maila; 3) migracja maili transakcyjnych z Office 365 do [[Postmark]] — platformy dedykowanej do wysyłki transakcyjnej, śledzącej odbicia i wypisy z synchronizacją do CRM; 4) rozgrzewanie listy fundraisingowej w CRM — start od małych wolumenów na listach ostatnio otwierających i subskrybentów, ze wzrostem opartym o treści kultywacyjne
- **Diagnoza problemu we własnym programie** — sprawdź, jak wysyłane są maile transakcyjne i czy platforma w ogóle śledzi ich dane; sprawdź, czy maile fundraisingowe i transakcyjne dzielą tę samą domenę

## Kluczowe dane
- Fundacja pozyskiwała 4 000–5 000 nowych leadów miesięcznie wyłącznie z bazy rekordów (Arrival Records Collection)
- Po wdrożeniu zmian reputacja IP i domeny wróciła do wysokiego poziomu
- Nowy standard: walidacja adresów e-mail 2-4 razy w roku

## Wnioski
- Maile transakcyjne wysyłane przez platformy nieprzeznaczone do marketingu (jak Office 365) mogą ukrywać odbicia i wypisy, które psują reputację nadawcy bez śladu w danych
- Wydzielenie osobnej subdomeny dla maili fundraisingowych to jedna z najprostszych zmian infrastrukturalnych, chroniąca resztę komunikacji przed skutkami problemów po jednej stronie
- Powrót do wysokich wolumenów wysyłki po naprawie dostarczalności nie zawsze jest celem — mniejsza, ale bardziej zaangażowana lista bywa efektywniejsza

## Cytat
> To jeden z tych problemów, o które wiele zespołów nigdy nie pyta, dopóki nie zaczyna ich to kosztować.

## Zastosowanie
Warto sprawdzić u klientów NGO, jaką platformą wysyłane są maile transakcyjne (potwierdzenia darowizn, formularzy) i czy dzielą domenę z kampaniami fundraisingowymi — to gotowa checklista audytowa do wykorzystania przy wdrożeniach digital campaigning. Framework czterech etapów można zaadaptować jako punkt wyjścia do doradztwa w zakresie dostarczalności e-maili dla organizacji społecznych.
