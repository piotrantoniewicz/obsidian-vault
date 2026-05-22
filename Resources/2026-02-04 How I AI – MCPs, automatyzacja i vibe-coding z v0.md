---
categories: Clippings
authors: ["[[Lenny Rachitsky]]"]
url: "https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-automate-the"
source: "[[Archives/2026-02-04 How I AI – MCPs, automatyzacja i vibe-coding z v0|2026-02-04 How I AI – MCPs, automatyzacja i vibe-coding z v0]]"
published: 2026-02-04
created: 2026-05-12
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "vibe-coding"
---

# How I AI – MCPs, automatyzacja i vibe-coding z v0

Dwa odcinki podcastu w jednym: Reid Robinson z [[Zapier]] pokazuje, jak [[MCP]] w połączeniu z [[Claude Projects]] zamienia Claude w stale działającego asystenta do automatyzacji CRM, przygotowania spotkań i syntezy feedbacku klientów — bez aktywnej obecności użytkownika. Guillermo Rauch (CEO [[Vercel]]) demonstruje, jak [[v0]] ewoluował z narzędzia do prototypowania w środowisko produkcyjne z pełnym Git workflow: branche, preview, pull requesty — dostępne dla każdego, nie tylko deweloperów. Oba odcinki łączy wspólna teza: AI przestaje być narzędziem "na żądanie" i staje się infrastrukturą działającą w tle.

## Frameworki i metody

**Workflow Reida Robinsona (Zapier):**
- **MCP jako "app connector dla AI"** — zamiast myśleć o MCP technicznie, traktuj je jako wtyczki dające modelowi dostęp do aplikacji (pobieranie danych lub wykonywanie akcji)
- **Claude Projects jako warstwa instrukcji** — persistent system prompt definiuje kolejność działań, sposób obsługi narzędzi i format danych; to rozwiązuje problem niespójnego zachowania Claude przy złożonych workflowach
- **Automatyczny CRM update** — po spotkaniu Claude odczytuje notatki, uzupełnia rekordy w CRM i utrzymuje historię klienta bez ręcznego wpisu
- **"If you could run ChatGPT in your sleep, what would you do?"** — pytanie heurystyczne do odkrywania wartościowych przypadków automatyzacji

**Workflow Guillermo Raucha (Vercel):**
- **Vibe-coding do produkcji z [[v0]]** — trzy zdania prompta wystarczyły do dodania systemu ocen z rate-limitingiem do skills.sh; v0 samodzielnie zadbał o zabezpieczenia przed nadużyciem
- **Git workflow w v0** — branche, commity, preview deployments i pull requesty są dostępne bez lokalnego setupu środowiska

## Kluczowe dane

- skills.sh (marketplace AI skills zbudowany w v0) zebrał 34 000+ zgłoszeń społecznościowych
- Eliminacja lokalnego setupu (Homebrew, dependencies) to według [[Guillermo Rauch|Raucha]] główna bariera wejścia do developmentu, którą v0 usuwa

## Wnioski

- [[MCP]] + [[Claude Projects]] to dziś najskuteczniejsza kombinacja do budowania autonomicznych workflowów — [[Claude Projects]] rozwiązuje problem braku pamięci i niespójności między sesjami
- Automatyzacja CRM to "universally hated task" — organizacje społeczne mają ten sam problem z logowaniem kontaktów i aktualizacją baz darczyńców
- [[v0]] demokratyzuje development nie przez uproszczenie kodu, lecz przez usunięcie setup friction — analogia do tego, co [[Make.com]] zrobił dla automatyzacji

## Cytat

> Przestań "używać" AI i zacznij budować systemy, które działają w tle.

## Zastosowanie

Workflow Reida Robinsona z [[Zapier]] + [[MCP]] jest bezpośrednio przenośny na pracę z NGO: automatyczne logowanie kontaktów po rozmowach, synthesis feedbacku z kampanii, przygotowanie briefingu przed spotkaniem z darczyńcą. To konkretny materiał do uwzględnienia w kursie "Fundraising z AI" jako przykład systemu, który działa bez aktywnej obsługi.
