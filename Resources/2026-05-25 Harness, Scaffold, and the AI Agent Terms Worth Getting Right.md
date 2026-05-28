---
categories: Clippings
authors: ["[[Sergio Paniego]]", "[[Aritra Roy Gosthipaty]]"]
url: https://huggingface.co/blog/agent-glossary
source: "[[Archives/2026-05-25 Harness, Scaffold, and the AI Agent Terms Worth Getting Right|2026-05-25 Harness, Scaffold, and the AI Agent Terms Worth Getting Right]]"
published: 2026-05-25
created: 2026-05-28
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "LLM"
  - "context-engineering"
---

# Harness, Scaffold, and the AI Agent Terms Worth Getting Right

[[HuggingFace]] opublikował glosariusz terminologii agentów AI, który precyzuje pojęcia używane zamiennie lub błędnie w całej branży. Autorzy rozróżniają między modelem (samo [[LLM]]), scaffoldingiem (warstwa definiująca zachowanie: system prompt, opisy narzędzi, zarządzanie kontekstem) i harnesem (warstwa wykonawcza: pętla wywołań modelu, obsługa narzędzi, decyzja o zatrzymaniu). Artykuł jest szczególnie przydatny dla kogoś, kto buduje własne narzędzia AI i rozmawia z klientami o wdrożeniach agentów.

## Frameworki i metody

Słownik kluczowych pojęć ekosystemu agentów AI:

- **Model** — samo [[LLM]]: przyjmuje tekst, generuje tekst (np. [[Claude]], Qwen, GPT). Bez scaffoldingu i harnesa nie ma pętli ani pamięci między wywołaniami.

- **Scaffolding** — warstwa definiująca zachowanie modelu: system prompt, opisy narzędzi, sposób parsowania odpowiedzi, zarządzanie kontekstem między krokami. To scaffolding kształtuje, jak model „widzi świat" i działa w nim.

- **Harness** — warstwa wykonawcza: wywołuje model, obsługuje wywołania narzędzi, decyduje o zatrzymaniu. Wzór: `Agent = Model + Harness`. Produkty jak [[Claude Code]] lub Codex to harness zbudowany wokół konkretnego modelu. Harness engineering to dyscyplina projektowania tej warstwy.

- **Agent** — model + wszystko wokół niego, co pozwala mu działać w pętli: przyjmować informacje, decydować i działać na podstawie wyników. Pochodzi z RL, gdzie agent = funkcja: obserwacja → akcja.

- **Context Engineering** — projektowanie tego, co trafia do okna kontekstowego agenta: system prompt, opisy narzędzi, historia rozmowy, pobrana wiedza. Obejmuje pamięć krótkoterminową (w oknie kontekstowym) i długoterminową (zewnętrzna, pobierana na żądanie).

- **Policy** — zdefiniowane zachowanie agenta: jakie akcje podejmuje w danej sytuacji. Część policy jest w wagach modelu, część w scaffoldingu i harnesie.

- **Tool Use** — jak agenty sięgają na zewnątrz: API, interpretery kodu, bazy danych, web search, systemy plików.

- **Skills** — wielokrotne użycie: paczki wiedzy umożliwiające zadania wieloetapowe. Gdzie tool to akcja, skill łączy wszystko potrzebne do realizacji celu.

- **Sub-agents** — agent wywołany przez inny agent do obsługi konkretnego podzadania. Ma własny model i scaffold, rozumuje niezależnie, zwraca wynik. Agent wywołujący to orchestrator.

- **Eval harness** — zamiast zbierania danych treningowych, uruchamia zestaw scenariuszy przy checkpoincie modelu i rejestruje metryki.

## Kluczowe dane

- Agent = Model + Harness (popularny wzór w społeczności)
- Scaffolding = co model widzi; Harness = jak agent działa
- Sub-agent ≠ tool (ma własny model i scaffold, może sam używać narzędzi i wywoływać sub-agenty)

## Wnioski

- Rozróżnienie harness/scaffold jest kluczowe przy rozmowie o wdrożeniach agentów — te dwa pojęcia nie są synonimami, choć wiele produktów używa ich zamiennie
- [[Claude Code]] jest harnesem wokół [[Claude]] — scaffolding to CLAUDE.md, opisy narzędzi i system prompt; harness to pętla wywołań i obsługa narzędzi
- [[MCP]] (Model Context Protocol) to standaryzacja połączenia Tool Use → Harness — robi tę warstwę interoperacyjną między różnymi dostawcami i implementacjami

## Zastosowanie

Dla Piotra budującego pluginy do [[Claude Code]] i wdrażającego AI w NGO, ten słownik to niezbędna baza terminologiczna. Przy rozmowach z klientami o „agentach AI" warto używać precyzyjnej nomenklatury: czym jest harness, czym scaffold, i dlaczego ten sam model (np. [[Claude]]) może zachowywać się zupełnie inaczej w różnych harnesach. Przy budowaniu własnych narzędzi AI (np. automatyzacje w [[Make.com]] lub pluginy) zrozumienie warstwy harnesa i scaffoldingu pomaga projektować bardziej niezawodne systemy.
