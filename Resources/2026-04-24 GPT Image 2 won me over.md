---
categories:
  - "Emails"
published: 2026-04-24
created: 2026-04-29
labels:
  - "Ryan Carr"
relevance: średnia
tags:
  - "narzędzia-AI"
  - "content-marketing"
  - "automatyzacja"
---

# GPT Image 2 won me over 🤷‍♂️

Ryan Carr przetestował GPT Image 2 od OpenAI w kontekście generowania brandowanych grafik do postów LinkedIn i ocenia go jako realną alternatywę dla dotychczas używanego Nano Banana Pro. Newsletter opisuje gotowy workflow oparty na [[Flora]], który przekształca dowolny długi materiał (transkrypt, notatka głosowa, newsletter) w gotowy post LinkedIn z trzema wariantami graficznymi dopasowanymi do marki. Kluczową innowacją jest zastosowanie referencyjnych grafik brandingowych użytkownika jako wizualnych kotew dla GPT Image 2, co zapewnia spójność wizualną bez ręcznego promptowania stylu. Workflow jest dostępny jako klonowany szablon w [[Flora]].

## Frameworki i metody

- **Content-to-LinkedIn Pipeline** — node-based workflow w [[Flora]] przekształcający długi materiał w post LinkedIn + 3 obrazy; kroki: (1) wrzuć treść do pierwszego node'a, (2) [[Claude]] Opus 4.7 tworzy 4 wersje posta pod różne kąty emocjonalne (funny, insightful, impressive, frustrating), (3) scoring wg rubryki „corniness", (4) wybór zwycięskiej wersji, (5) budowanie promptu obrazowego z kluczowym cytatem/statystyką, (6) GPT Image 2 generuje 3 równoległe rendery z referencjami brandingowymi
- **Brand Reference Anchoring** — zamiast opisywać styl w prompcie, wgrywa się własne grafiki brandingowe (logo, paleta, przykładowe grafiki) jako wizualne kotwice dla modelu generującego obrazy — kluczowy krok konfiguracji workflow

## Kluczowe dane

- 3 równoległe rendery obrazów generowane przez GPT Image 2 w jednym uruchomieniu
- 2–3 minuty na pełny output (post + 3 warianty graficzne)

## Wnioski

- [[GPT Image 2]] jest konkurencyjny z [[Nano Banana Pro]] pod względem brandingu i dokładności — warto przetestować go jako domyślne narzędzie do grafik contentowych, szczególnie gdy zależy nam na spójności wizualnej
- [[Flora]] jako narzędzie do łączenia modeli AI w node-based workflows jest użyteczna przy produkcji treści wymagającej spójności wizualnej — potencjalnie przydatna do tworzenia materiałów dla klientów z NGO
- Separacja thinking (model językowy drafts post) od building (model obrazowy renders) to skuteczny pattern do automatyzacji [[content-marketing]]u z zachowaniem jakości — wart omówienia w szkoleniu Fundraising z AI

## Cytat

> „GPT Image 2 używa twoich uploadów jako wizualnych kotew dla każdego renderu — dlatego zamiana referencji na własne materiały brandingowe to prawdopodobnie najważniejszy krok konfiguracji."

## Zastosowanie

Workflow można zaadaptować do tworzenia postów LinkedIn dla Piotra lub klientów z sektora NGO — zamiast pliku brandingowego Tailwind, wgrywa się materiały wizualne organizacji. Automatyzacja typu „długi tekst → gotowy post + grafika" mogłaby wejść do kursu Fundraising z AI jako przykład content marketingu z AI. Warto przetestować [[Flora]] jako narzędzie uzupełniające [[Make.com]] w automatyzacji treści.
