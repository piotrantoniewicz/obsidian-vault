---
categories:
  - Clippings
authors: ["[[Lenny Rachitsky]]"]
url: "https://www.lennysnewsletter.com/p/how-i-ai-how-this-pm-uses-claude?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
source: "[[Archives/2026-08-31 🎙️ How I AI How this PM uses Claude to handle 70% to 80% of his workday|2026-08-31 🎙️ How I AI How this PM uses Claude to handle 70% to 80% of his workday]]"
published: 2026-08-31
created: 2026-09-01
relevance: wysoka
tags:
  - "context-engineering"
  - "automatyzacja"
  - "narzędzia-AI"
---

# 🎙️ How I AI How this PM uses Claude to handle 70% to 80% of his workday

Podcast „How I AI" opisuje, jak Daniel Blum, product manager w Melio, zbudował samodoskonalący się system oparty na [[Claude]] i [[Cowork]], który przejął 70-80% jego codziennej pracy. System zarządza jego tablicą w Notion, przygotowuje go do tygodnia, skanuje Slack i maila pod kątem ważnego kontekstu i uczy się z jego edycji bez czekania na wyraźny feedback. Kluczowa teza: architektura systemu (pliki kontekstowe, pętle aktualizacji, telemetria feedbacku) liczy się bardziej niż wybór konkretnego narzędzia AI. Blum przekształcił swój setup w 15-minutowy onboarding dla innych pracowników Melio, pokazując drogę od osobistego workflow do produktu firmowego.

## Frameworki i metody

**Elementy samodoskonalącego się systemu AI:**

1. **Architektura ważniejsza niż narzędzie** — system staje się użyteczny, gdy potrafi aktualizować własne pliki bazowe i łączyć się z narzędziami, których ktoś już używa (Notion, Slack, mail), niezależnie czy działa w Cowork, Codex czy ChatGPT.
2. **Kontekst jako ciągły proces, nie jednorazowy setup** — miesiące budowania plików kontekstowych (notatki głosowe, linki, decki) dla każdego obszaru pracy, z cyklicznymi aktualizacjami co kilka tygodni, żeby luka między wiedzą AI a rzeczywistością firmy była jak najmniejsza.
3. **Poranny brief, który zna swoje luki** — codzienny przegląd Slacka, maila i notatek pod kątem nieznanych terminów czy celów, z zadawaniem celnych pytań, żeby uzupełnić brakujący kontekst (np. dopytanie o znaczenie firmowego żargonu, zamiast zgadywania).
4. **Pętla uczenia się z różnic** — cotygodniowy skill porównujący szkice AI z finalnymi wersjami wysłanymi przez człowieka, uczący się na podstawie drobnych, instynktownych edycji, a nie jawnego feedbacku.
5. **Telemetria feedbacku jako produkt** — każdy sygnał tarcia („to nie działa", prośba o korektę) jest logowany; cotygodniowa pętla poprawcza identyfikuje najczęstsze problemy i rekomenduje aktualizacje — de facto analityka dla własnych narzędzi AI.
6. **Onboarding personalizacji (Workstation plugin)** — 15-minutowy proces, który podłącza narzędzia danej osoby, mapuje jej współpracowników i uczy się jej głosu, zamiast zaczynać od generycznego systemu zbudowanego pod kogoś innego.

## Wnioski

- Wartość spersonalizowanego systemu AI buduje się powoli — pierwsze tygodnie są frustrujące (system nie wie wystarczająco dużo, praca wymaga poprawek), ale po przełamaniu tego etapu praca tygodnia mieści się w jednym dniu.
- Największym ograniczeniem dzisiejszych systemów AI jest brak ciągłości działania (system nie pracuje, gdy komputer jest wyłączony), a nie brak inteligencji — to sugeruje kierunek rozwoju narzędzi typu [[Cowork]] w stronę pracy autonomicznej w chmurze.
- Model „architektura + ciągły kontekst + pętla feedbacku" jest bezpośrednio przenośny na budowę własnego Second Brain (Obsidian + Cowork) — to właściwie opis tego samego typu systemu, tylko wdrożonego przez PM-a w firmie.

## Zastosowanie

Bezpośrednia inspiracja dla własnego projektu budowy Second Brain w strukturze EPARAX (Obsidian + Claude Cowork) — szczególnie warte przetestowania: cykliczne odświeżanie plików kontekstowych, poranny brief identyfikujący luki wiedzy oraz pętla porównująca szkice z finalnymi wersjami tekstów (przydatne przy ghostwritingu). Materiał nadaje się też jako case study do szkoleń z wdrażania AI w organizacjach — pokazuje ścieżkę od osobistego workflow do zespołowego onboardingu.
