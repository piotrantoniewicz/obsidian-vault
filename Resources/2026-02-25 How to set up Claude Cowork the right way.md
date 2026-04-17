---
categories: Clippings
authors: "[[Nav Toor]]"
url: https://x.com/heynavtoor/status/2026717574776631556
source: "[[2026-02-25 How to set up Claude Cowork the right way(so it actually does your work while you step away)]]"
published: 2026-02-25
created: 2026-03-07
relevance: wysoka
tags:
  - narzędzia-AI
  - automatyzacja
  - prompt-engineering
---

# How to set up Claude Cowork the right way

Nav Toor — freelancer budujący systemy AI od trzech lat — opisuje kompleksowo pięć kluczowych funkcji Claude Cowork i jak poprawnie skonfigurować każdą z nich. Centralny wniosek: Cowork to nie chatbot, lecz agent działający w folderach na komputerze użytkownika; zmiana myślenia z "lepsze prompty" na "lepsza kontekst w plikach" jest kluczowym przeskokiem. Artykuł zawiera konkretne pierwsze prompty dla każdej funkcji i uczciwy przegląd ograniczeń narzędzia.

## Frameworki i metody

**5 kluczowych funkcji Claude Cowork (w kolejności priorytetu)**
1. **File System Access** — Claude czyta i pisze do rzeczywistych folderów na komputerze; eliminuje ręczne kopiowanie/wklejanie plików między narzędziami
2. **AskUserQuestion** — zamiast zgadywać przy nieprecyzyjnym zadaniu, Claude generuje formularz z pytaniami precyzującymi kierunek; kończy erę "cleverych promptów" na rzecz "dobrego kontekstu"
3. **Plugins** — gotowe zestawy narzędzi dla konkretnych funkcji zawodowych (marketing, sprzedaż, analiza danych, prawo itd.)
4. **Instructions (Global & Folder)** — stałe instrukcje ładowane automatycznie na początku każdej sesji; eliminują potrzebę ponownego tłumaczenia kim jesteś i jak chcesz pracować
5. **Connectors** — integracje live z [[Slack]], [[Google Drive]], [[Notion]] i 50+ narzędziami; brak kopiowania/wklejania z zewnętrznych systemów

**Strategia plików kontekstowych (Context Files Strategy)**
- `about-me.md` — kim jesteś, co robisz, co sukces oznacza w twojej pracy
- `brand-voice.md` — jak komunikujesz, przykłady pisania, frazy, co brzmi źle
- `working-style.md` — jak chcesz żeby Claude się zachowywał, preferowane formaty wyjściowe

**Prompt do onboardingu kontekstowego:**
_"Read all the files in this folder. Then give me a summary of what you know about me, how I work, and what context you have access to."_

## Wnioski
- [[Claude Code]] (i [[Cowork]]) zmienia fundamentalny model pracy z AI: od "wyjdź do chatbota" do "AI działa w twoim środowisku" — różnica w jakości outputów jest jakościowa, nie kosmetyczna
- Dobry kontekst w plikach się kumuluje — każdy tydzień refinementu plików kontekstowych sprawia, że AI lepiej odpowiada twoim potrzebom
- Najważniejsza zasada onboardingu nowego użytkownika Cowork: 30 minut konfiguracji (pliki kontekstowe + global instructions + jeden plugin + jeden connector) przed pierwszym prawdziwym zadaniem

## Zastosowanie
Setup opisany w artykule można bezpośrednio zastosować we własnej pracy i jako materiał do szkoleń z AI dla organizacji — szczególnie strategia plików kontekstowych i podejście "context over prompts" jest natychmiast użyteczne.
