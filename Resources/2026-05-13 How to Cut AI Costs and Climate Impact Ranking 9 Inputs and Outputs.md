---
categories: Clippings
authors: ["[[Andy Crestodina]]"]
url: https://www.orbitmedia.com/blog/ai-costs-climate-file-formats/
source: "[[Archives/2026-05-13 How to Cut AI Costs and Climate Impact Ranking 9 Inputs and Outputs|2026-05-13 How to Cut AI Costs and Climate Impact Ranking 9 Inputs and Outputs]]"
published: 2026-05-13
created: 2026-05-14
relevance: średnia
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "prompt-engineering"
---

# How to Cut AI Costs and Climate Impact: Ranking 9 Inputs and Outputs

Każdy prompt do AI ma dwie ceny — finansową i środowiskową — a wybór formatu pliku może zmienić rachunek nawet 10-krotnie. Artykuł rankinguje 9 popularnych formatów wejściowych i wyjściowych pod kątem kosztu tokenów, zużycia energii i emisji CO₂: najlżejsze to TXT i [[Markdown|MD]], najcięższe — PPTX i DOCX. Kluczowa zasada: iteruj w lekkich formatach tekstowych, generuj ciężki plik tylko raz, na samym końcu procesu. Autor pokazuje też perspektywę środowiskową: koszt trenowania modeli (40 000 ton CO₂) jest nieporównywalnie wyższy niż koszt promptowania, a nasz rzeczywisty wpływ na klimat bardziej zależy od lotów i mięsa niż od liczby zapytań do AI.

## Frameworki i metody

Zasady efektywnego promptowania z ciężkimi formatami plików:
- **Brainstorm bez generowania pliku** — najpierw ustal treść w czacie, poleć AI żeby nie generowało DOCX/PPTX dopóki nie poprosisz
- **Lekkie podglądy** — podczas pracy nad treścią proś o wersję w [[Markdown]]
- **Iteracja w tekście** — prowadź rozmowę i poprawki w MD lub bezpośrednio w czacie, gdzie koszty są niskie
- **Batch zmian** — jeśli masz 5 poprawek, wyślij je w jednym prompcie (5 osobnych promptów = 5x koszt)
- **Finalna generacja raz** — dopiero gdy treść jest gotowa, generuj ciężki format
- **Drobne poprawki po eksporcie** — ostatnie tweaks rób poza AI, bezpośrednio w gotowym pliku

## Kluczowe dane
- Trening modeli AI to ~40 000 ton CO₂; jeden prompt ChatGPT to ~3 g CO₂
- 54% marketerów prosi AI o output w formacie DOCX — najdroższym z popularnych formatów
- Format PPTX jest najdroższy spośród wszystkich — wymaga osobnego modelu do obrazów i pełnej rekompilacji przy każdej edycji

## Wnioski
- [[Markdown]] to najlepszy format do pracy z AI — lekki, czytelny dla człowieka i dla modelu, tani w iteracji
- Każda edycja pliku DOCX lub PPTX w AI kosztuje tyle samo co generowanie od zera — dlatego nie poprawiaj, generuj ciężki plik tylko raz na końcu
- Dobry workflow AI to: praca w MD → iteracja w czacie → finalna generacja ciężkiego formatu tylko raz

## Cytat
> „Zmiany są finalne. Teraz wygeneruj plik DOCX. Użyj tych stylów…" — generuj ciężki format tylko raz, gdy wszystko jest gotowe.

## Zastosowanie
Piotr regularnie tworzy materiały szkoleniowe i dokumenty przez Claude — wiedza o kosztach formatów pozwala mu pracować wydajniej: iterować w MD, generować DOCX lub PPTX tylko raz na końcu. W szkoleniach z AI dla NGO może włączyć te zasady jako element świadomego, ekonomicznego korzystania z narzędzi AI — praktyczna wskazówka, którą uczestnicy od razu wdrożą.
