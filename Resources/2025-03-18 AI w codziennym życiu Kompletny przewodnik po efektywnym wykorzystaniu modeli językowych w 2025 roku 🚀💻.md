---
categories: Clippings
authors: ["[[Przemek Jurgiel-Zyla]]"]
url: "https://www.linkedin.com/pulse/ai-w-codziennym-%C5%BCyciu-kompletny-przewodnik-po-modeli-jurgiel-%C5%BCy%C5%82a-kdiuf/"
source: "[[Archives/2025-03-18 AI w codziennym życiu Kompletny przewodnik po efektywnym wykorzystaniu modeli językowych w 2025 roku 🚀💻|2025-03-18 AI w codziennym życiu Kompletny przewodnik po efektywnym wykorzystaniu modeli językowych w 2025 roku 🚀💻]]"
published: 2025-03-18
created: 2026-05-31
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "LLM"
  - "prompt-engineering"
---

# AI w codziennym życiu Kompletny przewodnik po efektywnym wykorzystaniu modeli językowych w 2025 roku 🚀💻

Artykuł to obszerne podsumowanie wykładu [[Andrej Karpathy]] o praktycznym użyciu LLM, traktujące modele jako "skompresowany internet" o rozmiarze ~1 TB i bilion parametrów. Karpathy proponuje strategiczne używanie różnych modeli do różnych zadań: flagowe (GPT-4o, Claude 3.7, Gemini 2.0) do złożonych analiz i dokumentów, modele z funkcją thinking (o1 Pro, Claude extended thinking) do wieloetapowych problemów, Perplexity/ChatGPT z wyszukiwaniem do aktualnych informacji. Ważnym wątkiem jest tzw. "rada LLM" — pytanie kilku modeli o to samo dla ważnych decyzji, co minimalizuje ryzyko błędów. Artykuł omawia też vibe coding w edytorach z AI ([[Cursor]]) jako zmianę roli programisty z autora kodu w architekta, oraz multimodalność (głos, obraz, wideo, NotebookLM).

## Frameworki i metody
- Hierarchia modeli (Tier-1 flagowe / Tier-2 darmowe) — dobór modelu do zadania jako samodzielna kompetencja
- Strategia multi-model: szybkie zapytania → modele bez thinking; złożone problemy → thinking (o1, Claude extended); dokumenty → Claude; deep research → ChatGPT Pro / Perplexity; aktualne info → modele z web search
- Rada LLM — to samo pytanie do kilku modeli i porównanie odpowiedzi dla ważnych decyzji
- Custom GPTs / Custom Instructions — few-shot prompting jako technika budowania wyspecjalizowanych asystentów do powtarzalnych zadań
- Vibe coding w [[Cursor]] — polecenia w języku naturalnym zamiast ręcznego pisania kodu; deweloper skupia się na logice wysokiego poziomu

## Kluczowe dane
- ~50% interakcji Karpathego z komputerem przechodzi przez LLM
- Wzrost produktywności w programowaniu szacowany na 30–40%
- ~90% książek czytanych z asystą LLM (lepsza retencja)
- Modele thinking: od 30 sek. do kilku minut na analizę, generują znacząco więcej tokenów (wyższy koszt API)

## Wnioski
- Wybór odpowiedniego modelu do zadania mierzalnie wpływa na jakość wyników — to kompetencja, nie oczywistość
- [[Vibe coding]] w edytorach jak [[Cursor]] redukuje czas prototypowania i obniża barierę wejścia do budowania narzędzi cyfrowych
- Personalizacja (custom instructions, memory, custom GPTs) to niedoceniana dźwignia produktywności — warto inwestować czas raz, żeby zyskiwać potem przy każdej sesji

## Zastosowanie
Przy szkoleniach AI dla NGO warto rekomendować strategię multi-model i custom instructions jako techniki zaawansowanego użycia — konkretne, uczące się narzędzia zamiast jednorazowych promptów. Framework "rady LLM" jest łatwy do wytłumaczenia i daje natychmiastowy, zauważalny rezultat. Vibe coding może zainteresować organizacje chcące budować proste narzędzia bez zatrudniania zewnętrznych programistów.
