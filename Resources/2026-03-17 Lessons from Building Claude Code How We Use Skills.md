---
categories: Clippings
authors:
  - '[[Thariq Shihipar]]'
url: 'https://x.com/trq212/status/2033949937936085378'
source: >-
  "[[Archives/2026-03-17 Lessons from Building Claude Code How We Use
  Skills|2026-03-17 Lessons from Building Claude Code How We Use Skills]]"
published: '2026-03-17'
created: '2026-05-01'
relevance: wysoka
tags:
  - narzędzia-AI
  - automatyzacja
  - prompt-engineering
---
# Lessons from Building Claude Code How We Use Skills

Thariq Shihipar z [[Anthropic]] opisuje wewnętrzne doświadczenia firmy z budowaniem i używaniem skills w [[Claude Code]] — narzędziu, które Piotr aktywnie stosuje w swojej pracy. Artykuł proponuje taksonomię 9 typów skills, dzieli się konkretną wiedzą o tym, co sprawia, że skill jest dobry, i jak dystrybuować skills w zespole przez marketplace pluginów. Najważniejsze przesunięcie perspektywy: skill to nie plik markdown, lecz folder z plikami, skryptami i kontekstem — to całkowicie zmienia podejście do projektowania. Artykuł pochodzi bezpośrednio od twórców narzędzia i zawiera nieoczywiste wskazówki, których nie ma w dokumentacji.

## Frameworki i metody

9 typów skills w [[Claude Code]] według Anthropic:

1. **Library & API Reference** — wyjaśnianie, jak poprawnie używać biblioteki, CLI, SDK; zawiera snippety i listę gotchas
2. **Product Verification** — testowanie i weryfikacja outputu Claude'a (Playwright, tmux); warto inwestować tydzień inżyniera w doskonałe skills weryfikacyjne
3. **Data Fetching & Analysis** — połączenie z danymi i monitoringiem; zawiera credentiale, ID dashboardów, instrukcje typowych zapytań
4. **Business Process & Team Automation** — automatyzacja powtarzalnych przepływów w jednym komendzie; warto zapisywać poprzednie wyniki w logach
5. **Code Scaffolding & Templates** — generowanie boilerplate dla konkretnej funkcji w codebase
6. **Code Quality & Review** — wymuszanie standardów; można uruchamiać przez hooki lub GitHub Actions; adversarial review jako osobny subagent
7. **CI/CD & Deployment** — fetchowanie, push, deploy; może referencować inne skills
8. **Runbooks** — symptom jako wejście, ustrukturyzowany raport jako wyjście; diagnoza przez multi-tool investigation
9. **Infrastructure Operations** — rutynowe operacje z guardrailami; zwłaszcza destruktywne akcje powinny mieć potwierdzenie użytkownika

Najważniejsze zasady budowania skills:
- **Gotchas section** — najważniejsza sekcja skill; buduj z rzeczywistych błędów Claude'a, aktualizuj na bieżąco
- **Progressive disclosure** — wskazuj na podpliki (references/, assets/, scripts/), które Claude odczyta kiedy będą potrzebne; cały filesystem to forma [[context-engineering]]
- **Description field** — to wyzwalacz dla modelu, nie opis dla człowieka; opisuje KIEDY użyć skill, nie CO robi
- **Unikaj railroadingu** — daj Claude'owi informację, nie sztywny przepis; elastyczność skills = reużywalność
- **Memory w skill** — log pliki lub JSON do przechowywania historii wykonań; np. standup-post czyta własne poprzednie posty i widzi, co się zmieniło

## Wnioski
- Taksonomia 9 typów pozwala zaudytować istniejące skills Piotra i zobaczyć, których kategorii brakuje — szczególnie Product Verification i Runbooks są niedoceniane poza środowiskami inżynierskimi, ale mają zastosowanie w automatyzacji procesów NGO.
- Wskazówka o gotchas i progressive disclosure to konkretna poprawa do wdrożenia w istniejących pluginach — zamiast ładować wszystko do SKILL.md, rozbić na podpliki referencyjne.
- Artykuł można pokazać klientom NGO jako dowód, że skills to oficjalny, produkcyjny wzorzec stosowany wewnątrz [[Anthropic]] — nie eksperyment, lecz sprawdzona metoda pracy z agentami AI.

## Cytat
> „Skill to folder, nie plik markdown — i właśnie ta różnica zmienia wszystko."

## Zastosowanie
Artykuł bezpośrednio wspiera pracę Piotra nad własnymi pluginami [[Claude Code]] — taksonomia 9 typów jest gotowym narzędziem do audytu i planowania nowych skills. Zasada "description field jest dla modelu" to szybka poprawa, którą można wdrożyć natychmiast w istniejących skill descriptions. Wskazówka o on-demand hooks (np. /careful blokujący rm -rf) to wzorzec wartościowy przy projektowaniu skills dla mniej technicznych użytkowników NGO.
