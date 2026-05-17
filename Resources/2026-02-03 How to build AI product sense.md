---
categories: Clippings
authors:
  - '[[Tal Raviv]]'
url: 'https://www.lennysnewsletter.com/p/how-to-build-ai-product-sense'
source: >-
  [[Archives/2026-02-03 How to build AI product sense|2026-02-03 How to build AI
  product sense]]
published: '2026-02-03'
created: '2026-05-12'
relevance: wysoka
tags:
  - narzędzia-AI
  - context-engineering
  - szkolenia-AI
---
# How to build AI product sense

[[Tal Raviv]] i Aman stawiają tezę, że najskuteczniejszy sposób na zbudowanie prawdziwej intuicji produktowej w świecie AI to codzienne używanie coding agentów ([[Cursor]], [[Claude Code]]) do pracy niemerytorycznej — strategii, priorytetyzacji, analizy danych. Coding agenty „pokazują pracę" w odróżnieniu od konsumenckich interfejsów (ChatGPT, Notion AI): widać reasoning modelu, wywołania narzędzi i zapełniający się context window. Dzięki temu naturalnymi metodami internalizuje się pojęcia, które inaczej pozostają abstrakcją: [[RAG]], pamięć agenta, context rot, subagenty, [[MCP]]. Artykuł prowadzi czytelnika przez 10 kroków — od instalacji Cursora, przez eksperymentowanie z modelami i narzędziami, po budowę lekkiego osobistego systemu produktywności.

## Frameworki i metody

- **RAG (Retrieval-Augmented Generation)** — przed odpowiedzią agent przeszukuje pliki i uzupełnia context window o trafne dokumenty; analogia: sprawdzenie notatek przed trudnym pytaniem
- **AGENTS.md / pamięć agenta** — plik Markdown automatycznie dołączany na początku każdej rozmowy; zawiera informacje o użytkowniku, styl pracy, wartości — ale zajmuje cenny context window
- **Context engineering** — świadome zarządzanie tym, co trafia do context window: narzędzia, RAG, pamięć, historia rozmowy; termin preferowany przez [[Andrej Karpathy]] nad "prompt engineering"
- **Context rot** — pogorszenie jakości odpowiedzi modelu wraz z zapełnianiem context window, widoczne szczególnie w zadaniach precyzyjnych (analiza danych, kod)
- **Subagenty** — otworzenie nowego wątku agenta do podzadania i zwrócenie tylko wyniku do wątku głównego; czyści context window
- **Personal OS w Cursor** — lekki system produktywności jako projekt: foldery Knowledge/, Tasks/, GOALS.md i AGENTS.md; każda sesja rozbudowuje bazę wiedzy zamiast żyć w historii czatu

## Wnioski
- Intuicja produktowa AI buduje się przez użytkowanie, nie przez czytanie — coding agenty dają wgląd w mechanikę niedostępny z poziomu ChatGPT
- [[MCP]] to standard analogiczny do USB: pozwala każdemu serwisowi (Notion, Linear, Amplitude) dostarczyć narzędzia do wszystkich agentów przez jeden konektor
- Dobór modelu to nie tylko "najinteligentniejszy wygrywa" — tool calling to osobna umiejętność modelu, niezależna od jakości pisania czy rozumowania

## Cytat
> Kiedy naprawdę rozumiesz produkty AI, zaczynasz „żyć w przyszłości".

## Zastosowanie
Artykuł ma bezpośrednie zastosowanie w szkoleniach Piotra z AI dla organizacji: framework "10 kroków z Cursorem" można zaadaptować jako ćwiczenie praktyczne dla uczestników, którzy chcą zrozumieć mechanikę agentów bez pisania kodu. Koncepcja personal OS (GOALS.md + Tasks/ + Knowledge/) to gotowy szablon lekkiego Second Brain dla uczestników kursów. Pojęcia context engineering i context rot warto wprowadzać w szkoleniach jako alternatywę dla ogólnikowego "prompt engineering".
