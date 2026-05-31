---
categories: Clippings
authors: ["[[Przemek Jurgiel-Zyla]]"]
url: "https://www.linkedin.com/pulse/magia-vibe-codingu-jak-stworzy%C5%82em-w%C5%82asn%C4%85-stron%C4%99-z-cms-jurgiel-zyla-tuehf/"
source: "[[Archives/2025-04-22 Magia Vibe Codingu Jak stworzyłem własną stronę z Notion jako CMS|2025-04-22 Magia Vibe Codingu Jak stworzyłem własną stronę z Notion jako CMS]]"
published: 2025-04-22
created: 2026-05-31
relevance: średnia
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "automatyzacja"
---

# Magia Vibe Codingu Jak stworzyłem własną stronę z Notion jako CMS

Autor opisuje, jak przy pomocy [[Claude]] i podejścia "vibe coding" zbudował własną stronę internetową używającą [[Notion]] jako CMS — bez płatnych rozwiązań, w jeden weekend. Vibe coding oznacza skupienie się na efekcie końcowym zamiast na perfekcji kodu, z intensywnym wsparciem AI do generowania fragmentów. Kluczem było połączenie Notion API z hostingiem PHP oraz zabezpieczenie klucza API poza katalogiem publicznym. Projekt zajął kilka godzin i zaowocował działającą stroną z własną domeną i pełną kontrolą nad treścią.

## Frameworki i metody

- **Vibe coding** — podejście programistyczne skupione na szybkim osiągnięciu celu z pomocą AI zamiast pisania idealnego kodu; składa się z: użycia istniejącej platformy jako backendu, generowania kodu przez [[Claude]], skupienia na efekcie końcowym i iteracyjnego ulepszania
- **Notion jako CMS** — baza danych w [[Notion]] z polami (tytuł, treść, URL, cover photo) zasilająca stronę przez API; zmiany w Notion natychmiast synchronizują się ze stroną
- **Buforowanie odpowiedzi API** — prosty cache zapisujący dane z Notion API w pamięci podręcznej serwera, by uniknąć przekroczenia limitów przy większym ruchu

## Wnioski

- [[Claude]] potrafi wygenerować działający kod integracji z zewnętrznym API nawet dla osoby bez głębokiej wiedzy programistycznej — wystarczy dobrze opisać wymagania
- Vibe coding radykalnie obniża próg wejścia w tworzenie własnych narzędzi cyfrowych — weekend pracy zastępuje tygodnie nauki
- Bezpieczeństwo kluczy API wymaga świadomego podejścia od początku projektu — plik `.env` to minimum, ale nie wystarczy w każdym scenariuszu

## Zastosowanie

Podejście vibe coding z [[Claude]] można zastosować do budowania prostych narzędzi dla NGO — formularzy, stron kampanii, małych aplikacji — bez zatrudniania programisty. [[Notion]] jako CMS to gotowe rozwiązanie dla organizacji, które chcą łatwo aktualizować treści bez panelu administracyjnego. Dla Piotra to model, który można pokazywać na szkoleniach jako przykład dostępnej automatyzacji dla nietech-savvy zespołów.
