---
categories: Clippings
authors: ["[[WenHao Yu]]"]
url: https://yu-wenhao.com/en/blog/lyt-framework-guide/
source: "[[Archives/2026-03-03 Obsidian PKM Guide How I Use AI to Build a LYT Note-Taking System|2026-03-03 Obsidian PKM Guide How I Use AI to Build a LYT Note-Taking System]]"
published: 2026-03-03
created: 2026-04-19
relevance: wysoka
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "context-engineering"
---

# Obsidian PKM Guide: How I Use AI to Build a LYT Note-Taking System

[[WenHao Yu]] opisuje, jak framework [[LYT]] (Linking Your Thinking) stworzony przez [[Nick Milo|Nicka Milo]] stał się najlepszą podstawą dla systemu zarządzania wiedzą zintegrowanego z AI. Autor przetestował PARA, Zettelkasten i LYT — i pokazuje, dlaczego struktura MOC (Maps of Content) daje AI natychmiastowy kontekst tematyczny, czego nie oferuje żaden z konkurencyjnych frameworków. Przy wsparciu [[Claude Code]] system produkuje 5+ notatek dziennie zamiast jednej tygodniowo. Kluczowa teza: wartość PKM polega nie na liczbie notatek, lecz na gęstości połączeń — a AI przyspiesza ten efekt kumulacji wykładniczo.

## Frameworki i metody

- **LYT (Linking Your Thinking)** — framework PKM oparty na trzech elementach:
  - **MOC (Maps of Content)** — notatka-mapa zawierająca linki do innych notatek danego tematu; zastępuje foldery, pozwala jednej notatce należeć do wielu MOC jednocześnie; daje AI natychmiastowy kontekst tematyczny bez przeskakiwania po kartach
  - **Framework ACE** — struktura folderów najwyższego poziomu: *Atlas* (wiedza — co to jest?), *Calendar* (czas — kiedy?), *Efforts* (działanie — nad czym pracuję?); rozdziela tryby myślenia: uczenie się / refleksja / egzekucja
  - **Pięć typów notatek** — Things (pojęcia), Statements (własne opinie i insighty), Questions (otwarte pytania), Quotes (cytaty), People (osoby); Statements są najcenniejsze — to Twoje własne myślenie, nie Wikipedia

- **Porównanie frameworków PKM z perspektywy kompatybilności z AI**:
  - PARA — wiedza grzęźnie w Archive po zakończeniu projektu; AI nie wie, gdzie szukać
  - Zettelkasten — brak struktury nadrzędnej; AI musi przeskakiwać karta po karcie
  - LYT — MOC to indeks tematyczny; AI otwiera MOC i natychmiast widzi cały krajobraz tematu

- **Workflow AI + LYT z [[Claude Code]]**: AI czyta istniejące MOC przed każdą sesją, dopisuje nowe notatki do właściwych map, identyfikuje luki i uzupełnia je badaniem webowym — całość bez ręcznego przenoszenia plików

## Kluczowe dane

- 70 000+ pobrań Ideaverse (starter kitu LYT) — najpopularniejszy zestaw startowy do notatek z linkowaniem na świecie
- Przyrost notatek: z 1 karty tygodniowo (Zettelkasten bez AI) do 5+ kart dziennie + MOC (LYT + AI)

## Wnioski

- [[LYT]] jest lepiej kompatybilny z AI niż PARA i [[Zettelkasten]], bo MOC pełni rolę indeksu tematycznego — AI może natychmiast zorientować się w danym obszarze wiedzy bez eksplorowania setek plików
- Warto pisać notatki typu Statement (własne opinie, analogie, insighty) — to one, a nie definicje pojęć, tworzą rzeczywistą wartość drugiego mózgu i mogą bezpośrednio zasilać content
- LYT zarządza wiedzą, nie działaniem — żeby domknąć pętlę codziennej produktywności, trzeba go uzupełnić frameworkiem egzekucji (autor używa [[12 Week Year]])

## Zastosowanie

Artykuł bezpośrednio dotyczy projektu budowania Second Brain Piotra w strukturze [[EPARAX]] połączonej z [[Obsidian]] i [[Claude Code|Claude Cowork]]. Trójelementowy model LYT (MOC + ACE + typy notatek) warto sprawdzić pod kątem zgodności lub konfliktów z aktualną strukturą EPARAX. Mechanizm MOC jako kontekstu dla AI jest kluczowy: jeśli Claude ma sprawnie poruszać się po vaulcie, musi mieć gotowe mapy tematyczne — to argument za priorytetowym tworzeniem MOC dla aktywnych obszarów (fundraising, AI dla NGO, automatyzacja).
