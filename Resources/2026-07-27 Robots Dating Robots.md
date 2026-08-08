---
categories:
  - Clippings
authors: ["[[Kevin Barenblat]]"]
url: "https://aiforhumanity.ffwd.org/p/robots-dating-robots?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
source: "[[Archives/2026-07-27 Robots Dating Robots|2026-07-27 Robots Dating Robots]]"
published: 2026-07-27
created: 2026-08-02
relevance: wysoka
tags:
  - "fundraising"
  - "strategia-AI"
  - "prompt-engineering"
---

# Robots Dating Robots

Kevin Barenblat i Scott J. Kleper (Fast Forward) opisują, jak zaprojektowali narzędzia AI do oceny wniosków grantowych (AI Proposal Assessment Tool, AI Grant Writing Coach) tak, by uniknąć scenariusza „robotów randkujących z robotami" — sytuacji, w której AI piszące wnioski i AI je oceniające zaczynają grać w system, a ludzie tylko udają, że czytają i piszą. Kluczowy wniosek z ich iteracji: dążenie do zgodności ocen między modelami (Claude, Gemini, ChatGPT) było błędem — modele różniły się w werdyktach, ale zgadzały się w rozumowaniu i argumentach. Zamiast wymuszać jednoznaczną ocenę „tak/nie", przeprojektowali narzędzie tak, by AI podsuwało pytania do dyskusji między funderem a wnioskodawcą, nie wydawało wyroku.

## Frameworki i metody

**Zasada „Nudge, Don't Judge" przy projektowaniu promptów oceniających:**
- Nie proś AI o werdykt (czerwony/żółty/zielony) — poproś o wskazanie konkretnych obszarów do omówienia, np. zamiast oceniać czy zespół jest „adekwatny", AI sugeruje: „warto omówić relację z kontraktorami i czy tę kompetencję rozwijać wewnętrznie".
- Rozbieżność ocen między modelami LLM to błąd, jeśli oczekujesz werdyktu, ale zaleta, jeśli oczekujesz pokrycia tematu (coverage) — różne modele wychwytują różne aspekty.
- Pętla weryfikacyjna promptu: uruchamiaj wielokrotnie na różnych LLM-ach i oceniaj wynik wg trzech kryteriów: (1) czy stwierdzenia są trafne, (2) czy feedback jest użyteczny i konkretny, (3) czy prompt unika wydawania jednoznacznej oceny tak/nie.
- AI ma prowadzić do refleksji człowieka, nie zastępować jego osąd — szczególnie przy decyzjach wpływających na finansowanie organizacji społecznych.

## Wnioski
- Przy projektowaniu narzędzi AI wspierających ocenę wniosków grantowych — czy to po stronie fundera, czy organizacji piszącej wniosek — lepiej celować w jakość pytań generowanych przez AI niż w zgodność ocen między modelami.
- Zasada „nudge, don't judge" przekłada się wprost na [[prompt-engineering|prompt engineering]] narzędzi wspierających decyzje: prompty proszące o otwarte pytania i obserwacje są bardziej użyteczne niż te proszące o skalę ocen.
- Ryzyko „robotów randkujących z robotami" (AI piszące wniosek vs. AI oceniające wniosek) to realny problem przy skalowaniu grant writing z AI po obu stronach procesu — wart uwzględnienia przy doradztwie dla organizacji społecznych wdrażających AI w fundraisingu.

## Zastosowanie
Bezpośrednio przydatne przy projektowaniu własnych promptów/narzędzi AI do wspierania klientów NGO w pisaniu i ocenie wniosków grantowych — zasada „nudge, don't judge" i trzykryterialna pętla weryfikacyjna to gotowy wzorzec do zastosowania. Warto też przywołać koncept „robots dating robots" jako ostrzeżenie w rozmowach z funderami o granicach automatyzacji oceny wniosków.
