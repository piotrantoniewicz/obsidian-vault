---
categories:
  - "Emails"
published: 2026-09-04
created: 2026-09-10
labels:
  - "The Batch"
relevance: średnia
tags:
  - "narzędzia-AI"
  - "trendy-AI"
  - "strategia-AI"
---

# Comparing OpenAI and Anthropic's Data Retention Policies

The Batch porównuje nowe polityki retencji danych OpenAI i Anthropic dla klientów biznesowych — obie firmy ogłosiły zmiany niemal jednocześnie, ale różnią się podejściem: Anthropic łagodzi swoją wcześniejszą zasadę 30-dniowego przechowywania danych, OpenAI potwierdza zero data retention (ZDR) jako standard. Kluczowy problem: obie firmy twierdzą, że mogą wykrywać nadużycia "bez czytania danych klienta", ale nie ujawniają, jak technicznie to działa — a systemy monitorujące i tak muszą odszyfrować dane, by je przeskanować. Dla organizacji przetwarzających wrażliwe dane (w tym NGO pracujące z danymi darczyńców czy beneficjentów) to rozróżnienie między "nie szkolimy na twoich danych" a "nie mamy twoich danych" ma realne znaczenie prawne i bezpieczeństwa.

## Frameworki i metody
- **Cztery poziomy prywatności AI w chmurze** — framework z 2024 roku przywołany przez [[DeepLearning.AI]]: najsilniejszy poziom to taki, gdzie dostawca w ogóle nie ma dostępu do danych klienta — to poziom kluczowy dla pracy z wrażliwymi danymi

## Kluczowe dane
- Anthropic od czerwca wymaga 30-dniowego przechowywania rozmów z Claude Fable 5 na wszystkich platformach; treści oznaczone przez firmę mogą być przechowywane do 2 lat
- Nowy program Anthropic (Enterprise Frontier Safeguards, EFS) ma być dostępny jesienią 2026
- GLM-5.3-Flash: 320 mld parametrów (18 mld aktywnych), kontekst do ok. 1 mln tokenów

## Wnioski
- Zapowiedź [[Enterprise Frontier Safeguards]] (Anthropic) i [[Private Safety Processing]] (OpenAI) pokazuje, że oba systemy nadal wymagają zdalnego "odszyfrowania i przeskanowania" danych — deklaracja "pracownicy tego nie widzą" nie jest tym samym co "system tego nie widzi"
- Dla organizacji obsługujących dane wrażliwe (prawnicze, medyczne, ale też fundraisingowe) różnica między brakiem treningu na danych a faktycznym brakiem dostępu do danych powinna być elementem oceny ryzyka przy wyborze dostawcy AI
- Żadna z firm nie opublikowała niezależnego audytu swojego systemu monitorowania — obietnice pozostają na razie mapą drogową, nie gwarancją

## Cytat
> "We won't train on your data" i "we don't have your data" to różne obietnice.

## Zastosowanie
Przydatne jako punkt odniesienia przy doradzaniu organizacjom społecznym w wyborze narzędzi AI do pracy z danymi darczyńców lub beneficjentów — framework czterech poziomów prywatności można wykorzystać w materiałach szkoleniowych o bezpiecznym wdrażaniu AI w NGO.
