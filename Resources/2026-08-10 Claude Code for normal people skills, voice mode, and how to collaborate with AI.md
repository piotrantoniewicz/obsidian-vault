---
categories:
  - Clippings
authors: ["[[How I AI]]"]
url: "https://www.youtube.com/watch?v=o_eg2TtXAO0"
source: "[[Archives/2026-08-10 Claude Code for normal people skills, voice mode, and how to collaborate with AI|2026-08-10 Claude Code for normal people skills, voice mode, and how to collaborate with AI]]"
published: 2026-08-10
created: 2026-08-10
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "vibe-coding"
---

# Claude Code for normal people skills, voice mode, and how to collaborate with AI

Grace Clarke, była konsultantka marketingowa, opowiada w podcaście How I AI, jak zbudowała całą infrastrukturę swojego jednoosobowego biznesu na Claude Code i Claude Cowork — bez tła technicznego. Kluczowa teza: „prompt engineering" umiera na rzecz „intent engineering" — zamiast pisać rozbudowane prompty, mówi do Claude przez 2-3 minuty na spacerze, opisując problem, i pozwala modelowi zaproponować rozwiązanie. Zbudowała pipeline operatora obsługującego klientów co godzinę, generator interaktywnych, spersonalizowanych propozycji HTML oraz własną zamienniczkę Gmaila. Największą barierą w adopcji AI nie jest brak korzyści, lecz brak nawyku otwierania narzędzia — dlatego uczy budowania „muscle memory" (np. przez zrzuty ekranu wysyłane do Claude) zamiast promptowania.

## Frameworki i metody

**Trzy filary jej systemu:**
1. **Voice guide (skill file)** — dokument opisujący jej sposób myślenia, słownictwo, czego unika (np. „AI slop"); dołączany automatycznie do niemal każdego zadania, żeby output brzmiał jak ona, nie jak AI.
2. **Proposal maker** — skill z change logiem, zasadami różnicującymi „teaching" od „consulting" i krokami budowy propozycji jako zaszyfrowanego, interaktywnego HTML zamiast tradycyjnego dokumentu.
3. **Pipeline operator** — uruchamiany co godzinę, przegląda maile i kontekst klientów, przesuwa ich przez kolejne etapy procesu, generuje kwestionariusze przed sesjami.

**Dwustopniowa „forcing function" dla osób nietechnicznych:**
1. Ustaw przypomnienie (Slack/kalendarz), które każe zrobić zrzut ekranu problemu i wkleić go do Claude z pytaniem „możesz mi z tym pomóc?" — buduje nawyk sięgania po narzędzie.
2. Zbuduj razem z Claude jeden skill (np. voice guide) — uczy podstaw technicznych (markdown, wersjonowanie) bez zniechęcania.

**Proces budowy skilla:** nie interview'ować użytkownika — Claude powinno samo studiować kontekst i wracać z gotową propozycją do reakcji, a nie zadawać pytania. Workflow: Claude Code do zadań ambitnych/niejednoznacznych (bo potrafi np. otworzyć przeglądarkę, gdy connector nie działa) → zapis sesji jako plik markdown → import do Claude Cowork do dalszej, bardziej wizualnej pracy.

## Wnioski

- „HTML to nowy markdown" — klienci wolą interaktywne, spersonalizowane dokumenty HTML (proposal, pre-work, workout tracker) niż suchy tekst; to działa też jako reklama umiejętności twórcy.
- Skille (voice guide, proposal maker) trzeba aktualizować na bieżąco — model dryfuje, pojawiają się nowe „tells" AI slopu przy każdej nowej wersji modelu, więc voice guide wymaga ciągłego doszlifowywania.
- Adopcja AI w zespołach/u klientów nie wynika z przekonywania o korzyściach, lecz z wymuszenia nawyku (forcing function) — ten sam mechanizm można zastosować przy szkoleniach organizacji społecznych z [[narzędzia-AI]].

## Zastosowanie

Model „voice guide + proposal maker + pipeline operator" można bezpośrednio przenieść na własną praktykę: skill opisujący styl komunikacji Piotra (już częściowo istnieje jako profil vaultu) oraz automatyzację propozycji dla klientów szkoleniowych/konsultingowych jako interaktywny HTML zamiast PDF. Dwustopniowa forcing function to gotowy element do warsztatów o adopcji AI w organizacjach społecznych — konkretna, przetestowana technika budowania nawyku zamiast samego przekonywania o korzyściach.
