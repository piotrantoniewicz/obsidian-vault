---
categories: Clippings
authors: ["[[Thariq Shihipar]]", "[[Lenny Rachitsky]]"]
url: "https://www.lennysnewsletter.com/p/how-i-ai-html-is-the-new-markdown"
source: "[[Archives/2026-05-18 🎙️ How I AI HTML is the new Markdown How Anthropic engineers are building with Claude Code|2026-05-18 🎙️ How I AI HTML is the new Markdown How Anthropic engineers are building with Claude Code]]"
published: 2026-05-18
created: 2026-05-20
relevance: wysoka
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "prompt-engineering"
---

# HTML is the new Markdown: How Anthropic engineers are building with Claude Code

[[Thariq Shihipar]], inżynier z zespołu [[Claude Code]] w [[Anthropic]], pokazuje jak HTML artefakty zastępują Markdown w planowaniu i specyfikowaniu projektów AI. Kluczowa teza: inżynierowie przestają pisać kod — stają się „allocatorami compute", decydując co warto budować i ile zasobów przeznaczyć na zadanie. Interfejsy HTML czynią wyjście agentów AI czytelnym i angażującym, co sprawia, że człowiek pozostaje w pętli nawet gdy agent pracuje autonomicznie przez godziny.

## Frameworki i metody

**Workflow pracy z Claude Code + HTML artefakty:**
- Planowanie w HTML zamiast Markdown — interaktywne, wizualne plany z mockupami, tabelami i nawigacją umożliwiają rzeczywiste zaangażowanie z treścią, a nie tylko przeglądanie
- Living design system w HTML — jeden plik z kolorami, typografią, komponentami, który można przekazać do każdego projektu; czytelny zarówno dla człowieka, jak i dla AI
- Throwaway micro-apps — jednorazowe UI do edycji konkretnych sekcji planu (np. tabela reguł wizualizacji danych jako gamifikowany interfejs), porzucane po użyciu
- Prompt w stylu „HTML file, plan, visualize, include whatever is needed" — minimalny, z sygnałem zaufania na końcu (`whatever is needed`), co daje Claude przestrzeń do decyzji

**Zasada promptowania:** Proste, ufające instrukcje przewyższają rozbudowane system prompts z nadmiernymi ograniczeniami.

## Kluczowe dane
- Thariq szacuje, że ok. 1% generowanych tokenów trafia do kodu produkcyjnego; reszta to dashboardy, interfejsy i narzędzia do rozumienia co buduje
- Sesja Claude Code może trwać 8 godzin na jednym zadaniu — to decyzja o wydaniu ~$500 compute

## Wnioski
- HTML artefakty w [[Claude Code]] to praktyczne narzędzie budowania „living documents" — interaktywnych planów, spec'ów, systemów designu, które są jednocześnie maszynowo- i ludzko-czytelne, bez kompromisu między nimi.
- Rola dewelopera AI ewoluuje w kierunku „compute allocatora" — kluczową umiejętnością jest definiowanie granic, wartości i synchronizacja z agentem w fazie planowania, a nie pisanie kodu.
- Bycie uprzejmym wobec modelu AI to nie tylko etyka — Thariq sugeruje, że ton interakcji wpływa na jakość rozumowania modelu (przy agresywnym tonie model „wie, że zawodzi").

## Cytat
> „Kiedy tokeny są tanie, możesz pozwolić sobie na piękno w każdym etapie procesu — i mieć nadzieję, że to piękno przekłada się na lepszy finalny produkt."

## Zastosowanie
Wzorzec HTML artefaktów można bezpośrednio zastosować przy budowaniu pluginów [[Claude Code]] i narzędzi Cowork — zamiast Markdown-owych SKILL.md, warto eksperymentować z interaktywnymi HTML spec'ami. Zasada „compute allocatora" to dobry framing do szkoleń dla NGO z AI — zmiana narracji z „AI zabiera pracę" na „AI zmienia charakter decyzji". Techniki throwaway micro-apps są bezpośrednio użyteczne przy budowaniu własnych narzędzi pracy dla dobryai.pl.
