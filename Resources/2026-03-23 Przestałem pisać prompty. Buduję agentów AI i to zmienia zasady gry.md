---
categories:
  - "Emails"
published: 2026-03-23
created: 2026-04-25
labels:
  - "Creative Sparks"
relevance: wysoka
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "automatyzacja"
---

# Przestałem pisać prompty. Buduję agentów AI i to zmienia zasady gry.

Tomasz Maciąg opisuje ewolucję swojej pracy z AI: od pojedynczych promptów przez systemy promptów do agentów AI — narzędzi, które prowadzą przez cały proces end-to-end, przenosząc kontekst między etapami bez angażowania użytkownika jako "project managera własnego procesu". Agent, w przeciwieństwie do promptu, ma wiedzę ekspercką, zna procesy właściciela i prowadzi krok po kroku, prezentując checkpointy i trade-offy decyzyjne. Jako przykład podaje własnego UX Designer agenta, który skrócił kilkudniowe planowanie strony do kilku godzin weekendowej pracy, produkując realne pliki: copy, sitemap i wireframe. Autor zapowiada przedsprzedaż tego agenta w trzech wariantach licencji.

## Frameworki i metody
- **Ewolucja promptowania** — trzy poziomy dojrzałości pracy z AI:
  1. Pojedynczy prompt — pytanie o konkretne rzeczy, fragmentaryczne efekty, brak kontekstu projektu
  2. System promptów — uporządkowane etapy i sekwencje, ale użytkownik musi pilnować kolejności i przenosić informacje między etapami
  3. [[Agent AI]] — wiedza ekspercka + znajomość procesów + automatyczne przenoszenie kontekstu + checkpointy decyzyjne
- **Architektura agenta** — agent ma: wiedzę ekspercką w danym obszarze, znajomość procesów właściciela, prowadzi przez ustrukturyzowany proces krok po kroku, na każdym etapie checkpointy z opcjami i trade-offami
- **Agent UX Designer** — pełen cykl projektu webowego: discovery → strategia → architektura informacji → szablon strony → wireframe → review; wyjście: prawdziwy copy, sitemap, wireframe

## Kluczowe dane
- ~3h pracy z agentem nad makietą i tekstami (vs kilka dni planowania tradycyjnie)
- ~2h eksperymenty z kierunkiem designu w Google Stitch
- Drugi dzień: kodowanie w [[Claude Code]]

## Wnioski
- Przejście na agentów AI eliminuje konieczność bycia "project managerem własnego procesu AI" — kontekst przenosi się między etapami automatycznie, co jest kluczowym argumentem przy wdrażaniu [[automatyzacja]] złożonych procesów w organizacjach
- Agent działa wydajnie dopiero gdy jest wyposażony w wiedzę ekspercką i znajomość metodyki pracy danej organizacji — to podpowiada jak myśleć o wdrożeniach AI w NGO: najpierw zakodować wiedzę ekspercką organizacji, potem budować agenta
- Podejście agentowe redukuje czas na zadania planistyczne z dni do godzin — potencjał dla [[Langflow]] i [[Make.com]] przy automatyzacji pracy organizacji pozarządowych

## Cytat
> "Agent nie czeka na moje pytania — prowadzi mnie przez ustrukturyzowany proces krok po kroku, a kontekst przenosi się między etapami automatycznie."

## Zastosowanie
Podejście agentowe jest bezpośrednio użyteczne przy budowaniu własnych narzędzi AI dla dobryai.pl — zamiast gotowych promptów warto tworzyć agentów wyposażonych w wiedzę ekspercką z zakresu fundraisingu i digital campaigningu dla NGO. Architektura "agent z checkpointami decyzyjnymi" to wzorzec wart wdrożenia w automatyzacjach procesowych dla klientów z sektora organizacji społecznych. Własny UX Designer agent Tomasza to inspiracja do zbudowania analogicznego "Fundraising Strategist" agenta dla organizacji.
