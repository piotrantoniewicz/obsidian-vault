---
categories:
  - Emails
published: '2026-07-10'
created: '2026-07-10'
labels:
  - The Batch
relevance: średnia
tags:
  - vibe-coding
  - automatyzacja
  - context-engineering
---
# Restoration of Claude Fable 5, Gemini's Video Dev Engine, DeepSeek Speeds Up Speculative Decoding

Andrew Ng opisuje swoją metodę szybkiego budowania prototypów 0-to-1 za pomocą agentów kodujących pracujących w pętli aż do spełnienia specyfikacji produktu. Kluczowa zasada: tokeny AI są tanie, tokeny ludzkie są cenne — zamiast długo dopracowywać spec przed startem, lepiej szybko wygenerować pierwszą wersję, ocenić jej błędy i dopiero wtedy doprecyzować specyfikację. Podkreśla też znaczenie zapisywania kluczowych decyzji w pliku SPEC.md, żeby agent nie "zapominał" ustaleń po kompaktowaniu pamięci.

## Frameworki i metody

- **Pętla kodowania agentowego (agentic coding loop)** — agent pracuje iteracyjnie aż spełni zadaną specyfikację; najtrudniejszym elementem jest sformułowanie samej specyfikacji, evali i testów, bo to tam wnosi się wiedzę ekspercką człowieka
- **Zasada „AI tokeny są tanie, ludzkie tokeny są złotem"** — zamiast spędzać godzinę na dopracowaniu specyfikacji, lepiej poświęcić 10 minut na wstępny opis, dać agentowi 20 minut na zbudowanie prototypu, a potem poprawiać spec na podstawie tego, co faktycznie powstało
- **SPEC.md jako pamięć projektu** — kluczowe decyzje warto zapisywać w osobnym pliku, żeby agent kodujący nie musiał ich odkrywać ponownie ani ich nie zapominał w trakcie długiej pracy nad projektem

## Wnioski

- Przy szybkich prototypach warto celowo rezygnować z długiego planowania architektury na rzecz szybkich iteracji z agentem kodującym — błędy w UI czy założeniach łatwiej wychwycić na gotowym prototypie niż przewidzieć na etapie spisywania specyfikacji
- Dokumentowanie decyzji w plikach typu SPEC.md to praktyczny sposób na ograniczenie kosztu "zapominania" przez agenta w dłuższych projektach — przydatne przy pracy z [[Claude Code]] nad własnymi pluginami
- Podejście "spec-driven development" nie musi być procesem waterfallowym — spec może ewoluować równolegle z kodem, napędzana obserwacją tego, co agent faktycznie zbudował

## Cytat

> AI tokeny są tanie; ludzkie tokeny są złotem.

## Zastosowanie

Zasadę szybkiego prototypowania z agentem i dopiero późniejszego dopracowywania specyfikacji można zastosować przy rozwijaniu własnych pluginów Claude Code oraz przy budowie Second Brain w Obsidianie — zamiast długo planować strukturę, warto zbudować pierwszą wersję i iterować na podstawie realnych błędów.
