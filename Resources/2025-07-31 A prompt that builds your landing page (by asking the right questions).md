---
categories: Clippings
authors: ["[[Ryan Carr]]"]
url: "https://moodboard.beehiiv.com/p/a-prompt-that-builds-your-landing-page-by-asking-the-right-questions"
source: "[[Archives/2025-07-31 A prompt that builds your landing page (by asking the right questions)|2025-07-31 A prompt that builds your landing page (by asking the right questions)]]"
published: 2025-07-31
created: 2026-05-08
relevance: średnia
tags:
  - "prompt-engineering"
  - "vibe-coding"
  - "produkty-cyfrowe"
---

# A prompt that builds your landing page (by asking the right questions)

Ryan Carr opisuje podejście do budowania stron sprzedażowych oparte na **meta-promptach procesowych** — zamiast wrzucać do AI jeden ogromny prompt z wszystkimi wymaganiami, pozwalamy modelowi najpierw przeprowadzić ustrukturyzowany wywiad z użytkownikiem. AI zadaje 5–6 pytań jedno po drugim, a dopiero na końcu generuje gotowy prompt dla buildera stron (np. [[Lovable]] lub [[Replit]]). Autor argumentuje, że taka sekwencja wymusza klarowność oferty i eliminuje generyczne copy, bo model pracuje na konkretnych danych, nie na domysłach. Podejście jest przenośne — ten sam meta-prompt działa dla dowolnego produktu lub klienta.

## Frameworki i metody

- **Process-Based Meta-Prompt** — prompt, który tworzy inne prompty poprzez sekwencję pytań:
  1. AI zadaje pytanie pierwsze (co sprzedajesz i dla kogo)
  2. Użytkownik odpowiada z detalami (zalecane: voice-to-text)
  3. AI zadaje kolejne pytanie (benefity, USP)
  4. Kolejne pytania obejmują: strukturę cenową, CTA i cele konwersji
  5. Po zebraniu odpowiedzi AI generuje gotowy prompt dla [[Lovable]]/[[Replit]] zaczynający się od "Build a..."
- **Specyfikacja wizualna w prompcie** — meta-prompt zawiera boilerplate preferencji designu: Inter font, gradienty SaaS, glass morphism, card-based layouts z hover animations — to zapewnia profesjonalny wygląd bez doprecyzowywania za każdym razem

## Wnioski

- Meta-prompt procesowy daje lepsze wyniki niż jeden duży prompt, bo wymusza zebranie konkretnych danych przed generowaniem treści — zasada ta działa poza stronami landing page
- Voice-to-text (np. [[Wispr Flow]]) znacznie przyspiesza odpowiadanie na pytania AI w trybie wywiadu — rozmowa jest naturalniejsza niż pisanie
- Podejście jest skalowalne: raz stworzony meta-prompt działa dla różnych klientów i produktów bez modyfikacji

## Zastosowanie

Meta-prompty procesowe można zastosować przy tworzeniu stron fundraisingowych lub kampanijnych dla NGO — wywiad z AI wymusi doprecyzowanie propozycji wartości i grupy docelowej przed budowaniem strony. To podejście warto uwzględnić w szkoleniach z [[prompt-engineering]] jako przykład, jak struktura dialogu z AI poprawia jakość outputu.
