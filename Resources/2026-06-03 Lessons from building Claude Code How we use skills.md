---
categories:
  - Clippings
authors:
  - "[[Anthropic]]"
url: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
source: "[[Archives/2026-06-03 Lessons from building Claude Code How we use skills|2026-06-03 Lessons from building Claude Code How we use skills]]"
published: 2026-06-03
created: 2026-07-08
relevance: wysoka
tags:
  - vibe-coding
  - narzędzia-AI
  - context-engineering
---

# Lessons from building Claude Code How we use skills

Anthropic dzieli się doświadczeniami z wewnętrznego używania Skills w Claude Code — narzędzia, którego autorzy skatalogowali setki własnych skilli i pogrupowali je w dziewięć kategorii funkcjonalnych. Kluczowa teza: skill to nie plik markdown, tylko cały folder ze skryptami, zasobami i strukturą, który agent eksploruje progresywnie — a najlepsze skille robią jedną rzecz dobrze, zamiast próbować ogarnąć wszystko naraz. Artykuł zawiera konkretne, praktyczne wskazówki pisania i dystrybuowania skilli, które mają bezpośrednie zastosowanie przy budowie własnych pluginów Claude Code.

## Frameworki i metody

**Dziewięć kategorii skilli zidentyfikowanych w Anthropic:**
1. Library and API reference — jak poprawnie używać biblioteki/CLI/SDK, z gotowcami błędów do unikania.
2. Product verification — testowanie i weryfikacja działania kodu (np. z Playwright, tmux); ma największy mierzalny wpływ na jakość wyników.
3. Data fetching and analysis — łączenie się z danymi i monitoringiem.
4. Business process and team automation — automatyzacja powtarzalnych workflow w jedną komendę.
5. Code scaffolding and templates — generowanie boilerplate'u dla konkretnej funkcji w kodzie.
6. Code quality and review — egzekwowanie jakości kodu i code review.
7. CI/CD and deployment — pobieranie, wypychanie i wdrażanie kodu.
8. Runbooks — od symptomu (alert, wątek Slack) przez wieloetapowe dochodzenie do ustrukturyzowanego raportu.
9. Infrastructure operations — rutynowe operacje utrzymaniowe, część z guardrailami przed destrukcyjnymi akcjami.

**Wskazówki pisania skilli:**
- **Nie pisz oczywistości** — Claude już umie kodować; skill ma dodawać wiedzę wypychającą model poza domyślny sposób myślenia, nie powtarzać to, co i tak by zrobił.
- **Buduj sekcję Gotchas** — najwyższej wartości treść w skillu to lista konkretnych pułapek, na które model wcześniej wpadał (np. "tabela X jest append-only, bierz wiersz z najwyższą wersją, nie najnowszym created_at").
- **Wykorzystuj system plików i progresywne ujawnianie** — SKILL.md wskazuje na dodatkowe pliki (`references/`, `assets/`), które model czyta dopiero w odpowiednim momencie, zamiast ładować wszystko naraz.
- **Nie "railroaduj" modelu** — daj wystarczające informacje, ale zostaw elastyczność dopasowania do sytuacji, zamiast sztywnych instrukcji krok po kroku.
- **Przemyśl setup** — skill może przechowywać dane konfiguracyjne (np. `config.json`) i pytać użytkownika o brakujące informacje (np. przez AskUserQuestion), gdy konfiguracji brak.
- **Pisz opisy dla modelu, nie dla ludzi** — pole `description` to nie streszczenie, tylko definicja triggerów, kiedy dany skill ma się aktywować.
- **Pomóż modelowi pamiętać** — skill może przechowywać własną pamięć (append-only log, JSON, nawet SQLite), którą czyta przy kolejnym uruchomieniu, żeby wiedzieć, co się zmieniło.
- **Przechowuj skrypty, generuj kod** — dając modelowi gotowe funkcje/biblioteki, oszczędzasz jego "tury" na kompozycję zamiast odtwarzania boilerplate'u za każdym razem.
- **Używaj hooków on-demand** — hooki aktywowane tylko przy wywołaniu konkretnego skilla (np. blokada `rm -rf` czy `DROP TABLE` tylko podczas pracy na produkcji), zamiast trzymać je włączone stale.

## Wnioski

- Dobra struktura pluginu Claude Code to nie jeden plik SKILL.md, tylko folder z progresywnym ujawnianiem treści — warto to zastosować przy rozwijaniu własnych [[narzędzia-AI|narzędzi AI]] i pluginów do pracy z organizacjami społecznymi.
- Sekcja Gotchas budowana iteracyjnie z realnych błędów modelu to najwyższej wartości element skilla — dobra praktyka do wdrożenia przy tworzeniu własnych skilli produkcyjnych, nie tylko eksperymentalnych.
- Opis skilla (`description`) trzeba pisać jako definicję triggera dla modelu, a nie streszczenie funkcji — częsty błąd przy tworzeniu własnych pluginów, który obniża trafność automatycznego wywoływania.

## Zastosowanie

Bezpośrednio przydatne przy rozwijaniu własnych pluginów Claude Code (projekt "Pluginy Claude Code — własne narzędzia AI do pracy") — dziewięć kategorii skilli to gotowy framework do audytu własnej biblioteki skilli, a wskazówki o sekcji Gotchas i progresywnym ujawnianiu można od razu zastosować przy refaktoryzacji istniejących pluginów typu `clippings-to-notes` czy `emails-to-notes`.
</content>
