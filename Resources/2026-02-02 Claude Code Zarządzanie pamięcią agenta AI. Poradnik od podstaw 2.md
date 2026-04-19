---
categories: Clippings
authors: ["[[Krzysztof Bohaczyk]]"]
url: https://www.youtube.com/watch?v=PIvJnLkquVc
source: "[[Archives/2026-02-02 Claude Code Zarządzanie pamięcią agenta AI. Poradnik od podstaw 2|2026-02-02 Claude Code Zarządzanie pamięcią agenta AI. Poradnik od podstaw 2]]"
published: 2026-02-02
created: 2026-04-19
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "szkolenia-AI"
  - "strategia-AI"
---

# Claude Code: Zarządzanie pamięcią agenta AI. Poradnik od podstaw 2

[[Krzysztof Bohaczyk]] wyjaśnia w praktyczny sposób, jak działa system pamięci [[Claude Code]] oparty na plikach `CLAUDE.md`. Bez tego pliku każda sesja zaczyna się od zera — agent nie pamięta struktury projektu ani preferencji użytkownika. `CLAUDE.md` pełni rolę briefingu dla nowego stażysty: kontekst projektu, zasady pracy i styl komunikacji dołączane są automatycznie do system promptu każdej sesji. Odcinek pokazuje też hierarchię trzech poziomów pamięci (globalny, projektowy, lokalny) oraz komendy `/init`, `/memory` i skrót `#` do szybkiego aktualizowania reguł w trakcie rozmowy. Materiał skierowany jest do użytkowników nietech­nicznych — przykładowy projekt to system zarządzania contentem bez linii kodu.

## Frameworki i metody

- **Hierarchia pamięci w [[Claude Code]]** — trzy poziomy plików konfiguracyjnych:
  - **Globalny** (`~/CLAUDE.md`) — dotyczy wszystkich projektów; miejsce na preferencje użytkownika, ulubione narzędzia, styl pisania, język
  - **Projektowy** (`CLAUDE.md` w katalogu projektu) — kontekst konkretnego repozytorium; może być commitowany do [[GitHub]] i współdzielony z zespołem
  - **Lokalny** (`CLAUDE.local.md`) — prywatne ustawienia dla projektu, nie trafia do repozytorium; dobre miejsce na narzędzia, schematy i klucze specyficzne dla danego użytkownika

- **Kluczowe komendy do zarządzania pamięcią**:
  - `/init` — automatyczna analiza projektu i wygenerowanie szkieletu `CLAUDE.md` na podstawie struktury katalogów; punkt startowy dla nowego projektu
  - `/memory` — podgląd wszystkich aktywnych plików pamięci (globalny, projektowy, lokalny) w bieżącej sesji
  - `# <reguła>` — szybkie dodanie reguły bezpośrednio z czatu; [[Claude Code]] automatycznie aktualizuje odpowiedni plik `CLAUDE.md`

- **Wskazówki do pisania skutecznego `CLAUDE.md`**:
  - Objętość: do 300–500 linijek — plik ma być zwięzłym briefingiem, nie encyklopedią
  - Zawartość dla projektów nietech­nicznych: opis projektu, workflow, struktura katalogów, język i ton treści, persona
  - Zawartość dla projektów technicznych: opis aplikacji, stack technologiczny, instrukcja uruchamiania projektu
  - Plik powinien być aktualizowany wraz z rozwojem projektu

## Wnioski

- Brak `CLAUDE.md` = agent bez pamięci — każda sesja zaczyna od zera i wymaga ponownego opisywania kontekstu; plik eliminuje tę stratę czasu i obniża barierę wejścia dla nietech­nicznych użytkowników
- Mechanizm pamięci jest wspólny dla wielu narzędzi AI (Codex używa `agents.md`, Gemini — `gemini.md`) — wiedza z konfiguracji [[Claude Code]] transferuje się na inne agentic tools
- Skrót `#` pozwala na bieżące "uczenie" agenta w trakcie pracy — gdy Claude robi coś niepoprawnie, można od razu zaktualizować regułę bez przerywania sesji

## Zastosowanie

Materiał jest bezpośrednio przydatny przy konfigurowaniu własnych projektów w [[Claude Code|Claude Cowork]] — szczególnie hierarchia globalny/projektowy/lokalny jako wzorzec do wdrożenia w dobryai.pl i projektach NGO. Schemat projektowego `CLAUDE.md` dla systemu zarządzania contentem (Content OS pokazany w odcinku) można zaadaptować do workflow ghostwritingowego lub zarządzania treściami kampanii fundraisingowych. W szkoleniach z AI dla organizacji ten materiał dobrze ilustruje mechanizm "briefingu agenta" bez konieczności znajomości kodu.
