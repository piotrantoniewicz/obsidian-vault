---
categories: Clippings
authors: ["[[Louise Linehan]]", "[[Xibeijia Guan]]"]
url: https://ahrefs.com/blog/why-chatgpt-cites-pages/
source: "[[Archives/2026-04-15 Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)|2026-04-15 Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)]]"
published: 2026-04-15
created: 2026-05-29
relevance: średnia
tags:
  - "LLM"
  - "narzędzia-AI"
  - "content-marketing"
---

# Why ChatGPT Cites One Page Over Another (Study of 1.4M Prompts)

Badanie [[Ahrefs]] analizujące 1,4 miliona promptów [[ChatGPT]] pokazuje, że cytowanie stron przez AI zależy przede wszystkim od semantycznej trafności tytułu względem wewnętrznych "fanout queries" — podzapytań generowanych przez model w odpowiedzi na prompt użytkownika. ChatGPT intensywnie korzysta z Reddita do budowania kontekstu tematycznego, ale prawie nigdy go nie cytuje (1.93%) — "uczy się od tłumu, cytuje instytucje". Artykuł odkrywa też pułapkę metodologiczną: porównania "cytowane vs. niecytowane" URL bez uwzględnienia źródła pobrania mogą prowadzić do błędnych wniosków o roli snippetów i dat publikacji.

## Kluczowe dane

- 88.46% cytowanych URL pochodzi z ogólnego indeksu search; Reddit (osobny API feed): tylko 1.93% cytowania przy 67.8% udziale w non-cited pool
- Cosine similarity tytułów: cytowane 0.602 vs. niecytowane 0.484 (względem promptu); 0.656 dla fanout queries — im lepszy match tytułu z podpytaniami AI, tym wyższe cytowanie
- Strony z natural language URL slugs: 89.78% citation rate vs. 81.11% dla opaque URLs

## Wnioski

- Optymalizacja pod AI-search to przede wszystkim optymalizacja tytułów pod konkretne pytania, które AI zadaje sobie wewnętrznie (fanout queries) — nie pod ogólne słowa kluczowe; SEO tytułów staje się ważniejsze niż kiedykolwiek
- Obecność w standardowym indeksie search jest warunkiem koniecznym cytowania przez [[ChatGPT]] — bez rankingu w wyszukiwarce nie ma cytowania przez AI, co potwierdza, że SEO i AI-search to naczynia połączone
- Reddit jest "szarą eminencją" AI search — [[ChatGPT]] czyta go masowo (16M data points), ale niemal nigdy nie cytuje; treści brandowe powinny być obecne zarówno na własnych stronach, jak i w community discussions dla budowania kontekstu

## Zastosowanie

Dla treści contentowych dobryai.pl — warto optymalizować tytuły artykułów pod konkretne pytania-scenariusze ("Jak NGO może wdrożyć AI?"), nie pod słowa kluczowe. Przy tworzeniu contentu dla organizacji, które chcą być widoczne w AI search — czytelne URL-e i semantycznie precyzyjne tytuły mają mierzalny wpływ na citation rate. Metodologiczne ostrzeżenie z artykułu (uważaj na artifacts w danych) jest użyteczne przy interpretowaniu jakichkolwiek badań porównawczych dotyczących AI.
