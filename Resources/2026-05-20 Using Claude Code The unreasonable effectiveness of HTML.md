---
categories: Clippings
authors:
  - "[[Thariq Shihipar]]"
url: https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
source: "[[Archives/2000-05-20 Using Claude Code The unreasonable effectiveness of HTML|2000-05-20 Using Claude Code The unreasonable effectiveness of HTML]]"
published: 2026-05-20
created: 2026-05-21
relevance: średnia
tags:
  - narzędzia-AI
  - strategia-AI
---

# Using Claude Code: The unreasonable effectiveness of HTML

[[Thariq Shihipar]] z [[Anthropic]] argumentuje, że HTML jest lepszym formatem wyjściowym niż Markdown w pracy z [[Claude Code]] — szczególnie dla specyfikacji, raportów, przeglądów kodu i interaktywnych edytorów. HTML pozwala na większą gęstość informacji (tabele, SVG, CSS, interakcje), jest łatwiejszy do czytania i udostępniania, a Claude może go generować bez specjalnych instrukcji. Kluczowa teza: Markdown ogranicza potencjał agentów AI, bo ludziom przestaje się chcieć czytać długie pliki tekstowe, podczas gdy HTML utrzymuje ich zaangażowanie w pętlę decyzyjną.

## Frameworki i metody

- **Pliki HTML jako specyfikacje i kanwa eksploracyjna** — zamiast jednego planu Markdown autor tworzy sieć plików HTML dla różnych etapów: eksploracja opcji → mockupy UI → plan implementacji. Pliki przekazywane są jako kontekst do kolejnych sesji Claude.
- **Jednorazowe interfejsy edycji** — [[Claude Code]] buduje dedykowany edytor HTML (np. drag-and-drop kart Kanban, edytor flag funkcji) z przyciskiem "skopiuj jako JSON/prompt", który eksportuje wynik z powrotem do Claude Code.
- **Przypadki użycia HTML zamiast Markdown**: przeglądy kodu (diffy, adnotacje, wykresy przepływu), projektowanie (prototypy z suwakami/przyciskami), raporty tygodniowe, dokumenty wyjaśniające, eksploracja wielu opcji projektowych jednocześnie.

## Wnioski

- HTML radykalnie zwiększa prawdopodobieństwo, że człowiek faktycznie przeczyta output [[Claude Code]] — to nie tylko estetyka, ale mechanizm utrzymania kontroli nad AI w pętli.
- Interaktywność HTML (suwaki, eksport jako prompt) tworzy ścisłe pętle sprzężenia zwrotnego między człowiekiem a modelem, przyspieszając iteracje.
- Podejście wymaga zmiany mentalności: pliki HTML traktować jak żywe dokumenty robocze, nie ostateczne raporty — autor przyznaje, że prawie całkowicie porzucił Markdown.

## Zastosowanie

Przy budowaniu pluginów [[Claude Code]] i skill files warto rozważyć generowanie outputów w HTML zamiast Markdown — szczególnie dla złożonych raportów dla NGO, analiz kampanii fundraisingowych czy dokumentacji wdrożeń [[Make.com]]. Technika jednorazowego edytora HTML może uprościć ręczny review wyników AI w projektach outreach lub szkoleniowych.
