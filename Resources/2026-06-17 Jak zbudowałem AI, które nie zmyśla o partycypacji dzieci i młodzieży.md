---
categories:
  - Clippings
authors: ["[[Rafał Szymański]]"]
url: "https://rafalszymanski.pl/blog/ai-rag-ktore-nie-zmysla-partycypacja/"
source: "[[Archives/2026-06-17 Jak zbudowałem AI, które nie zmyśla o partycypacji dzieci i młodzieży|2026-06-17 Jak zbudowałem AI, które nie zmyśla o partycypacji dzieci i młodzieży]]"
created: 2026-06-17
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "LLM"
  - "organizacje-społeczne"
---

# Jak zbudowałem AI, które nie zmyśla o partycypacji dzieci i młodzieży

[[Rafał Szymański]] opisuje budowę PIA (Partycypacyjny Inteligentny Asystent) — prywatnej bazy wiedzy z asystentem AI opartym na architekturze [[RAG]], zbudowanej dla zespołu doradczego przy Rzeczniczce Praw Dziecka. W odróżnieniu od ogólnych modeli językowych, PIA odpowiada wyłącznie na podstawie dokumentów załadowanych do bazy i cytuje źródła zamiast zmyślać — co jest fundamentalną zmianą dla badaczy i aktywistów potrzebujących wiarygodnych odpowiedzi. Artykuł tłumaczy bez żargonu mechanizmy stojące za tym rozwiązaniem: embedding (zamiana tekstu na wektor liczb), chunking (hierarchiczny podział dokumentów na fragmenty-dziecko i fragmenty-rodzic) oraz specyficzne koszty tokenizacji języka polskiego. To przewodnik dla nieinżynierów z organizacji społecznych, którzy chcą zrozumieć jak i dlaczego działa AI oparta na własnej bazie wiedzy.

## Frameworki i metody

**Architektura RAG — 5 kroków od pytania do odpowiedzi:**

1. **Rozumienie pytania** — szybki, tani model przepisuje pytanie konwersacyjne (np. „a co z gminami?") na samodzielne zapytanie w kontekście rozmowy
2. **Wyszukiwanie semantyczne** — system szuka pasujących fragmentów po znaczeniu (embedding), nie po słowach kluczowych; działa również między językami
3. **Budowanie „ściągi"** — znalezione fragmenty są numerowane i wklejane do polecenia jako ponumerowane cytaty `[1]`, `[2]`…
4. **Generowanie odpowiedzi** — mocny model (w PIA: [[Claude AI|Claude]] Opus 4.8) pisze odpowiedź wyłącznie na podstawie ściągi, wstawiając numery cytowań przy każdym zdaniu
5. **Klikalne cytaty** — `[1]` staje się linkiem do konkretnego źródła, które użytkownik może otworzyć i zweryfikować

**Dwupoziomowy chunking dokumentów:**
- **Fragment-dziecko** (~1000 znaków, z zakładem) — po nim szukamy; mały i precyzyjny, wskazuje konkretny akapit
- **Fragment-rodzic** (~5000 znaków) — szerszy kontekst podawany modelowi do pisania odpowiedzi; analogia: szukasz po fiszkach, czytasz cały rozdział

**Decyzja dla języka polskiego:** limit 14 000 znaków na fragment (vs ~24 000 dla angielskiego) — wynika z wyższego kosztu tokenizacji polszczyzny (~2–3 znaki/token wobec ~4 dla angielskiego).

## Kluczowe dane

- Embedding w PIA: wektor 3072 liczb na fragment tekstu (model text-embedding-3-large)
- Polski tekst kosztuje 1,5–2× więcej tokenów niż angielski przy embedowaniu
- Limit fragmentu: 14 000 znaków (bezpieczny margines dla polskiego w granicach modelu)

## Wnioski

- [[RAG]] eliminuje problem halucynacji przez architekturalne ograniczenie: model może odpowiadać wyłącznie na podstawie zaindeksowanych dokumentów — gdy brakuje danych, mówi „brak danych" zamiast zmyślać.
- Każde zdanie w odpowiedzi ma klikalny przypis — to zmienia AI z „wyroczni" w narzędzie weryfikowalne, co jest kluczowe w kontekście pracy badawczej i advocacy.
- System można zbudować dla dowolnej domeny wiedzy: ten sam wzorzec (RAG + prywatna baza + klikalny cytaty) działa dla fundraisingu, polityk NGO, prawa czy diagnoz społecznych — wystarczy podmienić dokumenty w bazie.

## Zastosowanie

Dla organizacji społecznych chcących wdrożyć AI do pracy z dużą ilością dokumentów (raporty, analizy, polityki, transkrypty) — artykuł daje język i ramy do oceny RAG jako alternatywy dla prostego czatu z AI. Dla szkoleń z AI w NGO: konkretny case study z sektora społecznego (partycypacja dzieci) pokazuje zastosowanie w praktyce — łatwiejszy do przyswojenia niż abstrakcyjne wyjaśnienia techniczne. Warto rozważyć podobne rozwiązanie dla klientów budujących wewnętrzne bazy wiedzy (polityki fundraisingowe, standardy kampanii, materiały szkoleniowe).
