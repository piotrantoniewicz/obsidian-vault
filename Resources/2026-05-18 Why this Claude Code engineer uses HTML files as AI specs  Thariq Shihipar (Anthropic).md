---
categories: Clippings
authors: ["[[Thariq Shihipar]]"]
url: https://www.youtube.com/watch?v=Qrpm7E80wQ0
source: "[[Archives/2026-05-18 Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic)|2026-05-18 Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic)]]"
published: 2026-05-18
created: 2026-05-18
relevance: średnia
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "prompt-engineering"
---

# Why this Claude Code engineer uses HTML files as AI specs  Thariq Shihipar (Anthropic)

[[Thariq Shihipar]] z zespołu [[Claude Code]] / [[Anthropic]] opisuje zmianę paradygmatu w pracy z agentami AI: HTML zamiast Markdown jako medium tworzenia specyfikacji, planów i artefaktów. HTML jest bogatszy wizualnie, łatwiejszy do czytania i przewijania, przez co angażuje człowieka do pozostania "in the loop" — w przeciwieństwie do tysiąclinijkowych plików Markdown, których nikt nie czyta. Kluczowa teza: "product manager 2026 to alokator zasobów obliczeniowych" — kiedy mówisz "Claude może działać 8 godzin", mówisz "Claude może wydać 500 dolarów" i musisz zdecydować, co jest tego warte. Filozofia "mentalności obfitości": 99% generowanych tokenów to nie kod produkcyjny, ale interaktywne artefakty pomagające zrozumieć, co chcesz zbudować.

## Frameworki i metody

- **HTML workflow z [[Claude Code]]** — czterostopniowy proces tworzenia oprogramowania:
  1. **Brainstorm w HTML** — "brainstorm some ideas in HTML" → Claude generuje wizualne propozycje z mockupami i uzasadnieniami
  2. **Plan w HTML** — "create an HTML file as a plan, include excerpts, mockups, code, whatever is needed for maximum context" → kompletny spec z wizualizacjami
  3. **Micro-app do edycji** — dla trudnych sekcji planu: "create an editable HTML artifact, design the ideal interface for this problem" → jednorazowy UI do interaktywnej edycji konkretnego fragmentu
  4. **Wdrożenie z artefaktem** — wyczyść kontekst, "here's a plan, implement it" → HTML plan jako artifact weryfikacyjny

- **Dokumentacja just-in-time** — specyfikacje nie muszą być w centralnym repozytorium w zunifikowanym formacie; [[Claude]] znajdzie je narzędziami. Ważna jest jakość treści, nie miejsce przechowywania

- **Filozofia promowania** — daj Claude wystarczający kontekst (typ interfejsów, struktura danych), ale nie przekonstruowuj promptu; dodaj "whatever is needed to give me maximum context" jako sygnał zaufania zamiast sztywnej specyfikacji każdego elementu

## Wnioski

- Mentalność alokatora zasobów to nowy sposób myślenia o pracy z AI — zanim zlecisz długie zadanie [[Claude Code]], warto zainwestować czas w dobry HTML spec, który "jest wart wydania tych 500 dolarów"
- HTML jako "żywy system projektowy" (design.html zamiast design.md) może być przekazywany jako kontekst do nowych projektów bez potrzeby przebudowywania wiedzy o designie
- Wyniki pracy z Claude mają wyższą jakość gdy człowiek jest "in the loop" — HTML spec angażuje autora do prawdziwego czytania i edytowania, zamiast ślepego akceptowania Markdown

## Zastosowanie

Piotr mógłby używać HTML zamiast Markdown do tworzenia briefów i specyfikacji dla Claude przy budowaniu nowych pluginów Cowork lub automatyzacji w [[Make.com]] — efekt angażujący do czytania oznacza lepszą kontrolę nad tym, co agent faktycznie zrobi. Technika "micro-app do edycji sekcji" jest szczególnie przydatna przy definiowaniu reguł filtrowania NGO w projekcie outreach — zamiast edytować listę kryteriów ICP w surowym tekście, można zbudować interaktywny formularz. Filozofia "compute allocator" bezpośrednio przekłada się na kursy szkoleniowe z AI — to gotowy frame dla uczestników, który zmienia sposób myślenia o delegowaniu zadań do AI.
