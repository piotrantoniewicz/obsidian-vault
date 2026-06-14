---
categories:
  - Clippings
authors: ["[[Marcin Wilkowski]]"]
url: "https://blog.humanistyka.dev/2026/03/stylometryczne-cechy-tekstow-generowanych-maszynowo"
source: "[[Archives/2026-03-21 Stylometryczne cechy tekstów generowanych maszynowo|2026-03-21 Stylometryczne cechy tekstów generowanych maszynowo]]"
published: 2026-03-21
created: 2026-06-14
relevance: niska
tags:
  - "LLM"
  - "trendy-AI"
---

# Stylometryczne cechy tekstów generowanych maszynowo

Wilkowski omawia badanie naukowców z Uniwersytetu Jagiellońskiego (*Stylometry recognizes human and LLM-generated texts in short samples*, 2026), które pokazuje, że stylometria — tradycyjnie służąca do ustalania autorstwa tekstów — może skutecznie wykrywać wytwory [[LLM|dużych modeli językowych]], nawet w krótkich próbkach i po automatycznym parafrazowaniu. Kluczowe wskaźniki to: bogactwo leksykalne (TTR), zróżnicowanie spójników i przyimków, częstotliwość stopniowania przymiotników oraz obecność inwersji składniowej. Ważne ograniczenie: parametry detekcji muszą być każdorazowo dostosowywane do gatunku tekstu i języka — wyniki z Wikipedii (angielskiej) nie uogólniają się automatycznie na inne typy treści. Badanie stanowi kolejny argument przeciwko skuteczności generycznych, komercyjnych detektorów AI.

## Frameworki i metody

**4 główne cechy stylometryczne tekstów maszynowych (drzewa decyzyjne):**

1. **TTR (Type-Token Ratio)** — stosunek unikalnych słów do wszystkich słów; teksty AI mają zazwyczaj niższe zróżnicowanie leksykalne
2. **Częstotliwość przymiotników w stopniu wyższym** — teksty maszynowe rzadziej stosują stopniowanie
3. **Słabe zróżnicowanie słów funkcyjnych** — przyimki i spójniki powtarzają się monotonnie zamiast być wymieniane
4. **Brak inwersji składniowej** — AI rzadziej przesuwa elementy zdania dla podkreślenia znaczenia

**Narzędzia zastosowane w badaniu:**
- [[StyloMetrix]] (NASK) — do ekstrakcji 195 cech stylometrycznych
- Analiza n-gramów — własny schemat badaczy
- Modele testowane: GPT-3.5, GPT-4, LLaMa 2/3, Orca, Falcon

## Wnioski
- Stylometria dostosowana do konkretnego gatunku tekstu może być znacznie skuteczniejsza niż generyczne detektory AI, bo szuka specyficznych wzorców językowych, a nie „AI fingerprints" ogólnego rodzaju.
- Teksty pisane przez ludzi są bardziej nasycone faktami, datami i nazwami własnymi niż wytwory [[LLM]] — nawet w tym samym gatunku.
- Automatyczne parafrazy (DIPPER, Parrot) utrudniają detekcję, ale nie eliminują stylometrycznych sygnałów — część cech przeżywa parafrazowanie.

## Zastosowanie
Dla Piotra temat ma niskie znaczenie operacyjne. Może być przydatny jako przykład podczas szkoleń o rozpoznawaniu treści AI: badanie UJ dostarcza konkretnych, zrozumiałych kryteriów (TTR, spójniki, inwersja), które można przetłumaczyć na praktyczne wskazówki dla uczestników warsztatów bez technicznego zaplecza.
