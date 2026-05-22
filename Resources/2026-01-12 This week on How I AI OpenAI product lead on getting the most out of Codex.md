---
categories: Clippings
authors: ["[[Lenny Rachitsky]]"]
url: "https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-the-power-users"
source: "[[Archives/2026-01-12 This week on How I AI OpenAI product lead on getting the most out of Codex|2026-01-12 This week on How I AI OpenAI product lead on getting the most out of Codex]]"
published: 2026-01-12
created: 2026-05-12
relevance: średnia
tags:
  - "narzędzia-AI"
  - "vibe-coding"
  - "strategia-AI"
---

# This week on How I AI: OpenAI product lead on getting the most out of Codex

Odcinek podcastu How I AI z Alexandrem Embiricem — product leadem [[OpenAI]] [[Codex]] — dokumentuje, jak agenci kodujący działają w środowiskach produkcyjnych: od prostych poprawek po pełne aplikacje. Kluczowy wniosek to, że kontekst jest ważniejszy niż sprytny prompt, a prawdziwym wąskim gardłem staje się ludzki osąd, nie generowanie kodu. [[OpenAI]] przetestowało te wzorce wewnętrznie, budując aplikację Sora na Androida w 28 dni, a użytkownicy [[Codex]] generowali o 70% więcej pull requestów niż nieużywający. Narzędzia AI ewoluują z oddzielnych destynacji w głęboko zintegrowanych "kolegów" żyjących bezpośrednio w środowisku deweloperskim.

## Frameworki i metody

- **Plans.md** — strukturalne planowanie złożonych zadań: przed rozpoczęciem implementacji agent tworzy plan z kamieniami milowymi; meta-szablon Plans.md pozwala Codexowi budować przemyślane, etapowe plany zamiast działać improwizacyjnie
- **Git worktrees** — równoległy rozwój z AI: jedna instancja Git śledząca wiele kopii kodebase'u jednocześnie, umożliwiająca uruchamianie wielu zadań agenta bez konfliktów zmian
- **Automated code review** — [[Codex]] recenzuje niemal wszystkie PRs we wszystkich repozytoriach [[OpenAI]]; wskazuje tylko błędy o wysokiej pewności, by chronić ludzką uwagę przed przeciążeniem

## Kluczowe dane

- Użytkownicy [[Codex]] generowali ~70% więcej pull requestów niż pracownicy [[OpenAI]] nieużywający narzędzia
- Aplikacja Sora na Androida zbudowana w 28 dni przy użyciu Plans.md i agentów kodujących

## Wnioski

- Kontekst instrukcji dla AI (cel zmiany, powód decyzji) jest ważniejszy niż sam prompt — dobrze sformułowany kontekst redukuje poprawki i przyspiesza pracę agenta
- Prawdziwe wąskie gardło to już nie generowanie kodu, lecz ludzki osąd: co budować, dla kogo, po co — to pytania, które AI jeszcze nie rozwiązuje
- Narzędzia AI ewoluują z oddzielnych destynacji w głęboko zintegrowanych "kolegów" żyjących w środowisku pracy — [[Codex]] w IDE, nie w przeglądarce

## Zastosowanie

Frameworki Plans.md i git worktrees mogą być zaadaptowane do pracy z agentem AI przy budowaniu automatyzacji w [[Make.com]] lub skryptach dla klientów NGO. Podejście "kontekst ważniejszy niż prompt" bezpośrednio wzmacnia efektywność materiałów szkoleniowych AI dla organizacji. Obserwacja, że ludzki osąd staje się głównym bottleneckiem, jest ważnym argumentem w rozmowach z NGO o roli człowieka przy wdrażaniu AI.
