---
categories: Clippings
authors: ["[[Caitlin Sullivan]]"]
url: https://www.lennysnewsletter.com/p/how-to-do-ai-analysis-you-can-actually
source: "[[Archives/2026-02-17 How to do AI analysis you can actually trust|2026-02-17 How to do AI analysis you can actually trust]]"
published: 2026-02-17
created: 2026-05-12
relevance: średnia
tags:
  - "prompt-engineering"
  - "LLM"
  - "narzędzia-AI"
---

# How to do AI analysis you can actually trust

Caitlin Sullivan, ekspertka od badań użytkowników, opisuje cztery tryby błędów w analizie danych z pomocą AI oraz konkretne techniki promptowania, które je eliminują. Kluczowy problem: AI zawsze brzmi pewnie, nawet gdy kłamie — wymyślone cytaty, fałszywe insighty i błędne wnioski są niewidoczne, dopóki ktoś nie zada trudnego pytania lub decyzja nie obróci się w katastrofę. Artykuł jest praktycznym przewodnikiem dla każdego, kto używa [[LLM]] do analizy jakościowej — wywiadów, ankiet, feedbacku. Choć pisany z perspektywy product managerów, wszystkie techniki są w pełni transferowalne do analizy danych NGO: ewaluacji programów, badania darczyńców, feedbacku od beneficjentów.

## Frameworki i metody

**4 tryby błędów w analizie AI i jak je naprawić:**

1. **Wymyślone dowody** — [[LLM]] generuje cytaty statystycznie prawdopodobne, nie dosłowne. Naprawa: zasady wyboru cytatów w prompcie ("zacznij gdzie zaczyna się myśl, zachowaj zastrzeżenia i emocje, nie łącz wypowiedzi z różnych miejsc") + weryfikacja: poproś model o potwierdzenie każdego cytatu jako VERIFIED / PARAPHRASE / NOT FOUND

2. **Fałszywe lub ogólne insighty** — AI szuka konsensusu i łatwych wzorców. Naprawa: załaduj 4 warstwy kontekstu: (a) cel projektu, (b) cel biznesowy/decyzja do podjęcia, (c) kontekst produktu/programu, (d) opis grupy uczestników badania

3. **"Sygnał" bez wartości decyzyjnej** — AI podaje liczby bez interpretacji decyzyjnej ("22 osoby wspomniały X"). Naprawa: few-shot calibration — pokaż AI przykłady dla każdego poziomu własnej skali z wyjaśnieniem, dlaczego dana odpowiedź należy do danego bucketu

4. **Sprzeczne insighty** — AI nie robi drugiego przeglądu własnej pracy. Naprawa: weryfikacja końcowa — poproś LLM o audyt: sprawdź cytaty, znajdź sprzeczności w wypowiedziach uczestników, oceń pewność twierdzeń

**Porównanie modeli do analizy jakościowej:**
- [[Claude]] — najlepszy do dogłębnej analizy z szerokim pokryciem danych; mniej hallucynacji
- [[Gemini]]/NotebookLM — najlepszy do dobrze ugruntowanych, dobrze udokumentowanych motywów; mocniejsze cytowanie
- [[ChatGPT]] — najlepszy do finalnego framowania dla odbiorców; najmniej wiarygodny w dosłownych cytatach

## Wnioski
- Błędy AI w analizie są niewidoczne z definicji — dlatego wymagają aktywnej weryfikacji, nie pasywnego "ufania outputowi"
- Jakość analizy [[LLM]] zależy głównie od jakości kontekstu w prompcie — ogólny prompt = ogólny wynik; precyzyjny kontekst decyzyjny = precyzyjne insighty
- [[Claude]] jest rekomendowany jako najlepsza baza do analizy jakościowej — szersze pokrycie danych i mniej hallucynacji niż [[ChatGPT]]

## Zastosowanie
Piotr może wykorzystać te techniki do analizy feedbacku darczyńców, wyników ankiet ewaluacyjnych i treści wywiadów z beneficjentami NGO. Technika few-shot calibration i weryfikacja cytatów to konkretne elementy gotowe do włączenia w moduł [[prompt-engineering|prompt engineeringu]] w szkoleniach dla organizacji społecznych — jako przykład jak robić rzetelną analizę jakościową z AI.
