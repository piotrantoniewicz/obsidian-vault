---
categories:
  - Emails
created: '2026-08-13'
labels:
  - AI Product Heroes
published: '2026-08-12'
relevance: wysoka
tags:
  - narzędzia-AI
  - automatyzacja
  - context-engineering
---
# Podsumowanie webinaru "Second Brain 2.0 i skille w Claude Code: AI, które zna Twój projekt"

Mail podsumowuje webinar AI Product Heroes o budowie Second Braina — systemu wiedzy opartego na plikach markdown, [[Obsidian]] i agencie AI (Claude Code lub Codex), który sam pełni rolę bibliotekarza. Zawiera 11-krokową instrukcję wdrożenia: od pobrania repozytorium i struktury folderów, przez personalizację i pierwsze projekty, po integracje przez MCP, budowę własnych skilli i pracę zespołową na gicie. Całość kończy się case study absolwenta programu oraz ofertą sprzedażową trzeciej edycji kohortowego programu AI Product Heroes. Treść jest bezpośrednio zbieżna z własnym projektem Piotra budowania Second Braina w strukturze EPARAX i łączenia Obsidiana z Claude Cowork.

## Frameworki i metody
- **11 kroków budowy Second Braina** — krok 1: pobierz repozytorium [Super Brain](https://github.com/superhero-tech/super-brain) z gotową strukturą folderów (daily, inbox, knowledge, projects, raw, templates, skills, system); krok 2: wskaż agentowi (np. [[Claude Code]]) folder projektu; krok 3: otwórz ten sam folder jako vault w [[Obsidian]]; krok 4: uruchom skill personalizujący, który buduje plik About; krok 5: załóż pierwszy projekt skillem project start; krok 6: dokładaj wiedzę przez wrzucenie pliku, skill ingest lub Obsidian Web Clipper; krok 7: porządkuj inbox skillem ingest, opcjonalnie jako cykliczna rutyna; krok 8: odpytuj bazę skillem query, który odpowiada na podstawie wiki, nie internetu; krok 9: podłącz zewnętrzne narzędzia przez konektory [[MCP]]; krok 10: zamień powtarzalne prośby w nowego skilla — zasady w skillu są najważniejsze, bo zapobiegają zmyślaniu; krok 11: rozszerz na zespół przez pracę na gicie (submoduły, osobne repozytorium na wspólny projekt)
- **Metafora biblioteki** — pliki to księgozbiór, AI to bibliotekarz, [[Obsidian]] to czytelnia, a instrukcje i skille to regulamin; bez bibliotekarza biblioteka staje się tylko magazynem

## Kluczowe dane
- Nagranie z webinaru ma już ponad 3400 wyświetleń
- Program AI Product Heroes 3 trwa 6 tygodni, start 19 października
- Cena w przedsprzedaży do 3 września: 2490 zł netto, później 3490 zł netto

## Wnioski
- Wiedza trzymana w plikach markdown na dysku (a nie w modelu) zostaje z użytkownikiem niezależnie od zmiany modelu, narzędzia czy pracodawcy — to argument za dalszym rozwijaniem własnego Second Braina zamiast polegania na pamięci pojedynczego narzędzia AI
- Kluczowe operacje bazy wiedzy warto trzymać w [[skille|skillach]], nie w luźnych instrukcjach, bo model bywa niekonsekwentny w czytaniu plików sterujących (tzw. dryf modelu) — to bezpośrednio dotyczy pracy Piotra nad własnymi pluginami [[Claude Code]]
- [[MCP]] (Model Context Protocol) pozwala podłączyć Second Brain do zewnętrznych narzędzi przez konektory, co otwiera drogę do dalszej automatyzacji poza samym Obsidianem

## Cytat
> Pamięć mieszka w plikach, nie w modelu.

## Zastosowanie
Instrukcja krok po kroku (struktura repozytorium, kolejność wdrożenia, rola skilli) to gotowy checklist do porównania z własnym setupem Second Braina w EPARAX i pluginami Claude Code. Warto rozważyć wdrożenie cyklicznej rutyny porządkującej inbox oraz jaśniejszy podział ról plików sterujących (system/skills), żeby ograniczyć dryf modelu we własnej bazie.
