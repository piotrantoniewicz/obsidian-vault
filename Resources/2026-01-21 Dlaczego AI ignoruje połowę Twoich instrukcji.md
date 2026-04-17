---
categories:
  - "Emails"
published: 2026-01-21
created: 2026-03-06
labels:
  - AI Ninjas
relevance: niska
tags:
  - prompt-engineering
  - LLM
  - narzędzia-AI
---
# Dlaczego AI ignoruje połowę Twoich instrukcji

Newsletter AI Ninjas opisuje zjawisko „Lost in the Middle" — efekt udokumentowany badaniami, polegający na tym, że modele [[LLM]] (w tym [[GPT-4]] i [[Claude]]) pomijają nawet 40% instrukcji ukrytych w środku długiej konwersacji. Problem dotyka wszystkich modeli i nie jest błędem użytkownika, lecz architektoniczną cechą mechanizmu uwagi. Autor prezentuje praktyczne rozwiązanie w postaci pliku `CLAUDE.md` — „kotwicy kontekstu" ładowanej na początku każdej sesji agenta. Koncepcja **Context Engineering** zakłada rozdzielenie krytycznych zasad (max 300 linii) od szczegółów technicznych linkowanych w plikach pomocniczych.

## Wnioski
- Efekt „Lost in the Middle" to nie kwestia jakości promptu, lecz struktury kontekstu — warto budować świadomość tej cechy [[LLM]] w szkoleniach, by uczestnicy nie frustrowano się „głupiejącym" modelem.
- Plik `CLAUDE.md` jako stała kotwica kontekstu to wzorzec przenoszalny poza kodowanie: organizacja pracy z [[Claude Code]] w projektach NGO (np. automatyzacja raportowania) może korzystać z tego samego mechanizmu.
- [[Prompt engineering]] ewoluuje w stronę **Context Engineering** — projektowania tego, co i kiedy trafia do kontekstu, co jest ważniejsze niż sam styl pisania promptów.

## Cytat
> Model potrafi pominąć nawet 40% instrukcji ukrytych w głębi długiej konwersacji — to nie jest zła wola modelu, a efekt „Lost in the Middle" udokumentowany badaniami na wszystkich [[LLM]] od [[GPT-4]] po [[Claude]].

## Zastosowanie
Przy projektowaniu szkoleń AI dla NGO warto wprowadzić ćwiczenie z budowania `CLAUDE.md` lub analogicznego pliku kontekstowego — uczy strukturyzowania wiedzy projektowej i znacząco poprawia jakość pracy z agentami.
