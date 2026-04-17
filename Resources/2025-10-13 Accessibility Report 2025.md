---
categories: Clippings
authors: ["[[Email Markup Consortium]]"]
url: https://emailmarkup.org/en/reports/accessibility/2025/
source: "[[Archives/2025-10-13 Accessibility Report 2025|2025-10-13 Accessibility Report 2025]]"
published: 2025-10-13
created: 2026-03-23
relevance: niska
tags:
  - "digital-campaigning"
---

# Accessibility Report 2025

[[Email Markup Consortium]] publikuje coroczny raport o dostępności emaili HTML, analizując 443 585 wiadomości z okresu maj 2024 – maj 2025. Wyniki są alarmujące: 99,89% emaili zawiera błędy dostępności kategorii "Serious" lub "Critical", a tylko 21 wiadomości przeszło wszystkie automatyczne testy — i to od zaledwie dwóch marek. Raport rozszerzono o ocenę klientów pocztowych: tylko jeden (SFR Desktop) obsługuje wszystkie 20 testowanych funkcji HTML/CSS niezbędnych do budowania dostępnych emaili. Autorzy wskazują na systemowe przyczyny: brak wiedzy emailo-specyficznej nawet wśród doświadczonych developerów, generowanie niedostępnego kodu przez drag-and-drop buildery oraz słabe wsparcie w klientach pocztowych.

## Kluczowe dane

- 99,89% emaili zawiera błędy "Serious" lub "Critical" (60,66% Critical, 39,23% Serious)
- Najczęstszy problem: brak atrybutu `dir` w body (98,14% emaili), brak `lang` (96,67%), tabele layoutu bez `role="presentation"` (86,24%)
- Tylko 1 z 44 testowanych klientów pocztowych (SFR Desktop) obsługuje wszystkie funkcje dostępności

## Wnioski

- Dostępność emaili to obszar, w którym nawet duże marki i organizacje rządowe (100% failure rate) mają ogromne zaległości — argument przydatny przy rozmowach o jakości komunikacji emailowej z klientami NGO
- Drag-and-drop buildery (np. w platformach typu [[Mailchimp]], [[MailerLite]]) generują strukturalnie niedostępny kod — organizacje używające tych narzędzi powinny wiedzieć, że ich emaile najprawdopodobniej mają błędy dostępności bez dodatkowego audytu
- [[Outlook]] dla Windows obsługuje tylko 7/20 testowanych funkcji dostępności, co oznacza, że nawet poprawnie zakodowany email może być niedostępny dla dużej grupy odbiorców

## Zastosowanie

Temat dostępności emaili jest marginalnie związany z codzienną pracą Piotra, ale może być użyteczny jako argument dodatkowy w szkoleniach o jakości komunikacji emailowej — szczególnie dla organizacji pracujących z osobami z niepełnosprawnościami lub dbającymi o standardy dostępności cyfrowej. Warto mieć w rezerwie przy rozmowach o audytach emailowych z klientami NGO.
