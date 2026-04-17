---
categories: Clippings
authors:
  - "[[Cat Wu]]"
url: https://claude.com/blog/product-management-on-the-ai-exponential
source: "[[Archives/2026-03-19 Product management on the AI exponential|2026-03-19 Product management on the AI exponential]]"
published: 2026-03-19
created: 2026-03-22
relevance: wysoka
tags:
  - strategia-AI
  - narzędzia-AI
  - automatyzacja
---

# Product Management on the AI Exponential

Cat Wu, Head of Product dla [[Claude Code]] w Anthropic, opisuje, jak praca product managera zmienia się w erze szybko poprawiających się modeli AI. Tradycyjny playbook PM zakładał, że możliwości technologiczne są stabilne przez cały czas trwania projektu — dziś każda kolejna wersja modelu może usunąć ograniczenia, wokół których właśnie projektowałeś. Wu proponuje cztery przesunięcia: krótkie sprinty zamiast długich roadmap, prototypy i evale zamiast dokumentów, rewizja funkcji przy każdym nowym modelu, i zasada „zrób prostą rzecz, która działa". Artykuł ilustruje te idee konkretnymi przykładami z historii [[Claude Code]] — w tym tym, jak [[AskUserQuestion]], todo listy i pluginy powstały jako „side questy" poza oficjalną roadmapą.

## Frameworki i metody

- **Side quest** — krótki, samodzielny eksperyment poza oficjalną roadmapą: popołudnie na prototyp idei, test możliwości, które wydawały się niedostępne; kilka kluczowych funkcji [[Claude Code]] (desktop, AskUserQuestion, todo listy) powstało właśnie tą drogą
- **Prototype-first thinking** — zamiast dokumentu PRD, najpierw prototyp; wewnętrzni użytkownicy testują, te z realnym zaangażowaniem są polerowane i szerzone; bo możesz zbudować prototyp w popołudnie, złe zakłady są tanie
- **Evale jako substytut dokumentacji** — konkretne zestawy ocen (evals) sprawiają, że abstrakcyjna funkcja staje się mierzalna; przykład: [[Claude Code]] agent teams — ręcznie przygotowane evale pomogły ustalić, kiedy feature działa, a kiedy nie
- **„Do the simple thing"** — im prostsze wdrożenie, tym łatwiej wymienić komponenty gdy przyjdzie nowy model; skomplikowane obejścia ograniczeń modelu stają się zbędnym długiem technicznym po kolejnym update'cie

## Kluczowe dane

- [[METR]]: [[Opus 4.6]] wykonuje zadania zajmujące człowiekowi ~12 godzin — w 16 miesięcy skok z 21 minut (Sonnet 3.5) do 12 godzin, czyli ~41x wzrost
- Nowy model [[Opus 4.6]] pozwolił skrócić system prompt o 20% — mniej promptingu potrzebnego do kompensowania ograniczeń modelu

## Wnioski

- Prawidłowość dotyczy nie tylko PM-ów: organizacje wdrażające [[AI]] powinny planować krótko i iteracyjnie, bo ograniczenia technologiczne, wokół których projektujemy, mogą zniknąć w połowie projektu — dotyczy to też NGO wdrażających automatyzacje
- „Zacznij od możliwości, nie od kosztów" — błędem jest zbyt wczesne cięcie użycia tokenów/narzędzi; najpierw sprawdź, czy feature jest w ogóle możliwy; dopiero potem optymalizuj koszty
- [[Claude Code]], [[Claude.ai]] i [[Cowork]] tworzą trójkę narzędzi o różnych rolach: myślenie strategiczne → budowanie i automatyzacja → praca z wiedzą i plikami; to naturalna architektura dla konsultanta pracującego z AI

## Zastosowanie

Artykuł jest bezpośrednio użyteczny do kształtowania własnego workflow z [[Claude Code]] i [[Cowork]] — szczególnie podejście do side questów i prototype-first. W szkoleniach z AI dla NGO warto adaptować tę zasadę: zamiast długiego planu wdrożenia, zacznij od krótkiego eksperymentu, który możesz pokazać w ciągu tygodnia. Wzorzec „zrób prostą rzecz" jest dobrą kontrą dla pokus nadmiernej automatyzacji na starcie.
