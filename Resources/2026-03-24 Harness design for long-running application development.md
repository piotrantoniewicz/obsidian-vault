---
categories: Clippings
authors: "[[Anthropic]]"
url: https://www.anthropic.com/engineering/harness-design-long-running-apps
source: "[[Archives/2026-03-24 Harness design for long-running application development|2026-03-24 Harness design for long-running application development]]"
published: 2026-03-24
created: 2026-03-25
relevance: średnia
tags:
  - narzędzia-AI
  - strategia-AI
  - automatyzacja
---

# Harness design for long-running application development

[[Prithvi Rajasekaran]] z zespołu [[Anthropic]] opisuje, jak przełamał limity wydajności długo działających agentów kodujących, stosując architekturę inspirowaną [[GAN]] (Generative Adversarial Networks): oddzielny agent-generator i agent-evaluator, które iteracyjnie doskonalą wynik. Kluczowym odkryciem jest to, że modele językowe systematycznie zawyżają ocenę własnej pracy — oddzielenie oceniania od generowania i skalibrowanie ewaluatora na "sceptyczny" tryb dramatycznie podnosi jakość finalnych produktów. Na przestrzeni eksperymentów z frontendem i pełnym stackiem, architektura trzech agentów (planner, generator, evaluator) z negocjowanymi kontraktami sprintowymi wyprodukowała aplikacje znacznie bogatsze niż podejście jednoagentowe — choć 20× droższe.

## Frameworki i metody

- **Architektura Generator-Evaluator** — agent generujący i osobny agent oceniający tworzą pętlę feedbackową; ewaluator jest kalibrowany na sceptycyzm poprzez few-shot przykłady z rozpisanymi ocenami
- **Cztery kryteria oceny designu frontendu:**
  - *Design quality* — spójność kolorów, typografii, layoutu jako całości
  - *Originality* — dowody oryginalnych decyzji projektowych (penalizacja "AI slop": fioletowe gradienty, szablonowe layouty)
  - *Craft* — precyzja techniczna: hierarchia typografii, spójność odstępów, kontrast
  - *Functionality* — użyteczność niezależna od estetyki
- **Trzyagentowy system dla full-stack:**
  - *Planner* — rozbudowuje 1-4 zdaniowy prompt do pełnej specyfikacji produktu
  - *Generator* — buduje feature po feature, używa git, na koniec każdego sprintu samoewaluuje
  - *Evaluator* — testuje live aplikację przez [[Playwright MCP]], negocjuje kontrakt sprintu przed startem każdego cyklu
- **Sprint contracts** — generator i ewaluator uzgadniają przed startem sprintu co zostanie zbudowane i jakie testy potwierdzą ukończenie; komunikacja przez pliki
- **Context resets vs compaction** — reset kontekstu daje modelowi "czyste pole" i eliminuje "context anxiety" (przedwczesne kończenie zadań przy zapełnionym oknie); compaction zachowuje ciągłość, ale nie likwiduje problemu

## Kluczowe dane

- Solo run (Opus 4.5): 20 min, $9 vs Full harness: 6 hr, $200 (20× drożej, ale jakość nieporównywalna)
- Build DAW w przeglądarce (V2 Harness, Opus 4.6): 3 godz. 50 min, $124,70
- Opus 4.6 wyeliminował potrzebę context resets dzięki lepszemu długookontekstowemu wyszukiwaniu i mniejszej "context anxiety"

## Wnioski

- Modele LLM są słabymi ewaluatorami własnej pracy — zewnętrzny, sceptycznie skalibrowany ewaluator to kluczowy lever jakości w każdym agentowym systemie.
- Każdy komponent harnessu koduje założenie o tym, czego model nie umie zrobić sam; te założenia szybko się starzeją — każdy nowy model wymaga ponownej weryfikacji, które elementy scaffoldu są wciąż potrzebne.
- [[Claude Agent SDK]] upraszcza orkiestrację multi-agentową — warto go uwzględnić przy budowaniu własnych narzędzi automatyzacyjnych opartych na Claude.

## Zastosowanie

Piotr buduje własne pluginy do [[Claude Code]] i narzędzia AI — ta architektura generator-evaluator jest bezpośrednio inspirującym wzorcem dla pluginów wymagających wysokiej jakości outputu (np. generowanie raportów, notatek, treści). Zasada "sceptycznego ewaluatora" można też zastosować do walidacji jakości notatek generowanych przez obecne skille (clippings-to-notes, emails-to-notes).
