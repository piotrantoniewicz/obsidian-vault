---
categories: Clippings
authors: ["[[Hamel Husain]]"]
url: https://www.lennysnewsletter.com/p/building-eval-systems-that-improve
source: "[[Archives/2025-09-09 Building eval systems that improve your AI product|2025-09-09 Building eval systems that improve your AI product]]"
published: 2025-09-09
created: 2026-05-11
relevance: wysoka
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "prompt-engineering"
---

# Building eval systems that improve your AI product

Artykuł [[Hamel Husain|Hamela Husaina]] to kompletny przewodnik po budowaniu systemów ewaluacji produktów AI — nie po to, żeby tworzyć ładne dashboardy, lecz żeby napędzać realne ulepszenia. Autorzy argumentują, że gotowe metryki (halucynacje, toksyczność) są pułapką: oderwane od rzeczywistych problemów użytkowników, generują liczby, które nikt nie czyta. Zamiast tego proponują trójetapowy proces: error analysis → budowa zestawu ewaluatorów → ciągłe doskonalenie.

## Frameworki i metody

**Faza 1 — Error Analysis (analiza błędów)**
- **Open coding** — ekspert domenowy przegląda ~100 interakcji użytkownika z AI i swobodnie opisuje wszystko, co wydaje się błędne; każda interakcja dostaje ocenę pass/fail z uzasadnieniem
- **Axial coding** — grupowanie swobodnych obserwacji w taksonomię błędów (max ~10 kategorii); zliczenie kategorii wskazuje gdzie skupić zasoby
- Punkt wyjścia to zawsze losowa próba interakcji, nie metryki off-the-shelf

**Faza 2 — Budowa zestawu ewaluatorów**
- **Code-based evaluators** — dla obiektywnych kryteriów (np. czy output zawiera wymagane pole JSON); szybkie, tanie, deterministyczne
- **LLM-as-a-judge** — dla subiektywnych kryteriów (ton, trafność, jakość rozumowania); wymaga walidacji na zbiorze oznaczonym przez eksperta
- Podział danych do budowy sędziego: train (10–20%) → dev (40–45%) → test (40–45%)
- Zamiast accuracy używać **TPR/TNR** — oddzielna miara dla poprawnych "pass" i poprawnych "fail"

**Faza 3 — Ewaluacja złożonych systemów**
- **RAG**: osobna ewaluacja retrievera (recall@k) i generatora (faithfulness + answer relevance); najpierw napraw retriever
- **Agenty**: transition failure matrix — mapa kroków workflow, gdzie agent najczęściej się załamuje
- **Multi-turn**: najpierw weryfikuj czy błąd reprodukuje się w pojedynczej turze, zanim zaczniesz analizować konwersację

## Wnioski
- Ewaluacja zaczyna się od obserwacji, nie od metryk — błędy trzeba odkryć empirycznie, zanim zbudujesz miernik
- Pojedynczy ekspert domenowy z ocenami binarny (pass/fail) + uzasadnienie to skuteczniejsza baza niż skale Likerta i wiele anotatorów
- [[LLM]]-as-a-judge jest użyteczny tylko jeśli walidowany na danych ludzkich — bez tego daje fałszywe poczucie kontroli jakości

## Zastosowanie
Ten framework można zastosować bezpośrednio przy budowaniu pluginów [[Claude Code]] i narzędzi w ramach dobryai.pl — każdy nowy agent lub automatyzacja potrzebuje własnej listy failure modes zanim trafi do użytkowników. Error analysis (100 interakcji → open coding → axial coding) to metoda, którą można wdrożyć w szkoleniach dla NGO pokazujących jak sprawdzać jakość własnych wdrożeń AI.
