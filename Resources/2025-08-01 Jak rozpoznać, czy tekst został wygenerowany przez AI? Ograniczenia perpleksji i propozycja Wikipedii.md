---
categories:
  - Clippings
authors: ["[[Marcin Wilkowski]]"]
url: "https://blog.humanistyka.dev/2025/08/jak-rozpoznac-czy-tekst-zostal-wygenerowany-przez-ai-ograniczenia-perpleksji-i-propozycja-wikipedii"
source: "[[Archives/2025-08-01 Jak rozpoznać, czy tekst został wygenerowany przez AI? Ograniczenia perpleksji i propozycja Wikipedii|2025-08-01 Jak rozpoznać, czy tekst został wygenerowany przez AI? Ograniczenia perpleksji i propozycja Wikipedii]]"
published: 2025-08-01
created: 2026-06-14
relevance: niska
tags:
  - "LLM"
  - "narzędzia-AI"
  - "ghostwriting"
---

# Jak rozpoznać, czy tekst został wygenerowany przez AI? Ograniczenia perpleksji i propozycja Wikipedii

[[Marcin Wilkowski]] pokazuje, dlaczego automatyczne detektory tekstów AI oparte na perpleksji są zawodne i dyskryminujące — faworyzują native speakerów kosztem osób piszących w nieojczystym języku. Nawet [[OpenAI]] wycofało swój własny detektor po kilku miesiącach z powodu niskiej skuteczności. W zamian społeczność Wikipedii zaproponowała tabelę pięciu kategorii ręcznych sygnałów, które pozwalają odróżnić tekst maszynowy od ludzkiego bez algorytmów. Artykuł jest przestrogą przed ślepym zaufaniem do narzędzi i wezwaniem do wypracowania własnych heurystyk.

## Frameworki i metody

**5 kategorii sygnałów AI według społeczności Wikipedii:**

1. **Język i ton** — nadmierne podkreślanie wagi zjawisk, styl promocyjny, niepotrzebne opinie, generalizacje typu *większość badaczy uważa, że…*
2. **Styl i formatowanie** — niepotrzebne pogrubienia, nadmiar list punktowanych, emoji, nadużywanie półpauz, niespójne cudzysłowy
3. **Zwroty i ujawnienia** — frazy wynikające z interakcji z modelem (*Zgodnie z poleceniem…*), wzmianki o ograniczeniach wiedzy, wzorce z pustymi miejscami
4. **Formatowanie i cytowania** — błędne odnośniki, halucynowana bibliografia (błędy w tytułach, datach, miejscach wydania)
5. **Treść merytoryczna** — ogólniki, brak pogłębionej analizy, powtarzanie pomysłów, niespójność stylu

## Wnioski

- Detektory AI oparte na perpleksji są zawodne i mogą dyskryminować osoby piszące w języku nieojczystym — [[OpenAI]] samo wycofało swój detektor po kilku miesiącach
- Ręczna analiza według kategorii sygnałów Wikipedii jest skuteczniejsza niż automatyczne narzędzia i nie wymaga specjalistycznego oprogramowania
- Nawet ręczne metody przestają działać, gdy autor świadomie steruje stylem w [[prompt engineering|prompcie]] — prosi o język akademicki lub podaje przykłady dobrego pisania

## Zastosowanie

Artykuł może być przydatny w szkoleniach z AI dla NGO jako materiał do modułu o ograniczeniach i weryfikacji treści generowanych maszynowo. W pracy ghostwritera tabela Wikipedii to użyteczna lista kontrolna przy redakcji tekstów pisanych z pomocą AI. Klientom pytającym o wykrywanie AI w tekstach warto wskazać tę tabelę zamiast polecać zawodne detektory komercyjne.
