---
categories: Clippings
authors: ["[[Alexander Embiricos]]"]
url: "https://www.youtube.com/watch?v=xeZDHGjG5zM"
source: "[[Archives/2026-01-12 The power user s guide to Codex  Alexander Embiricos (product lead)|2026-01-12 The power user s guide to Codex  Alexander Embiricos (product lead)]]"
published: 2026-01-12
created: 2026-05-12
relevance: średnia
tags:
  - "narzędzia-AI"
  - "vibe-coding"
  - "prompt-engineering"
---

# The power user's guide to Codex — Alexander Embiricos (product lead)

[[Alexander Embiricos]], product lead [[Codex]] w [[OpenAI]], pokazuje praktyczne przepływy pracy z tym agentem kodowania — zarówno dla osób technicznych, jak i nieeksperckich. Główny argument: Codex sprawdza się najlepiej jako "thoroughness-first" agent do złożonych zadań kodowania, a jego skuteczność zależy przede wszystkim od jakości kontekstu dostarczonego w promptcie. Odcinek pokazuje konkretne workflow: równoległe sesje z Git worktrees, technikę PLANS.md do architektonowania złożonych projektów oraz zautomatyzowany code review.

## Frameworki i metody

- **PLANS.md** — technika tworzenia szczegółowego planu implementacji jako osobnego pliku (PLANS.md) przed uruchomieniem Codexa na złożonym projekcie. Plan opisuje cel, kroki, zależności i oczekiwane rezultaty — model ma go "w głowie" przez całą sesję. Szczególnie przydatna dla projektów wymagających wielu zmian w różnych miejscach kodu.

- **Git worktrees + równoległe sesje** — uruchamianie wielu instancji [[Codex]] jednocześnie na osobnych gałęziach Git (worktrees), by unikać konfliktów. Każda instancja pracuje nad innym zadaniem niezależnie — wyniki scalane są po zakończeniu. Pozwala znacząco przyspieszyć pracę.

- **Vibe coding vs. produkcja** — rozróżnienie: vibe coding (szybkie prototypowanie bez planowania) vs. produkcyjne aplikacje (wymagają planowania, testów, code review). [[Codex]] sprawdza się w obu, ale wymaga innego podejścia promptowego.

- **Zautomatyzowany code review** — integracja [[Codex]] z [[GitHub]] do automatycznej recenzji pull requestów. [[OpenAI]] używa tego wewnętrznie — review uruchamiane automatycznie przy każdym PR.

## Kluczowe dane

- [[OpenAI]] zbudowało aplikację [[Sora]] na Android w 28 dni przy użyciu [[Codex]] — natychmiast stała się #1 w App Store.
- [[Codex]] dostępny w planach Plus, Pro, Business, Team i EDU [[ChatGPT]].

## Wnioski

- Jakość outputu [[Codex]] jest wprost proporcjonalna do jakości kontekstu — im więcej agent wie o projekcie, tym lepsze rezultaty.
- Równoległość (git worktrees + kilka instancji) to jeden z najważniejszych "power moves" przy pracy z agentami kodowania.
- Granica między "vibe coding" a produkcyjnym rozwojem wymaga świadomego wyboru — nie każdy projekt potrzebuje planowania, ale złożone zadania bez planu kończą się chaosem.

## Zastosowanie

Dla Piotra najbardziej użyteczna jest technika PLANS.md — analogicznie można ją stosować przy promptowaniu [[Claude]] do złożonych zadań automatyzacyjnych lub pisaniu skryptów [[Make.com]]. Workflow równoległych sesji jest inspiracją dla budowania własnych pluginów i narzędzi AI. Rozróżnienie vibe coding vs. produkcja pomaga decydować, kiedy warto poświęcić czas na planowanie przed wdrożeniem.
