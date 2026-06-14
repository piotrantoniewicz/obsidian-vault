---
categories:
  - Clippings
authors: ["[[Marcin Wilkowski]]"]
url: "https://blog.humanistyka.dev/2025/07/nasi-chlopcy-i-niemozliwosc-historii-maszynowej"
source: "[[Archives/2025-07-27 \"Nasi chłopcy\" i niemożliwość historii maszynowej|2025-07-27 \"Nasi chłopcy\" i niemożliwość historii maszynowej]]"
published: 2025-07-27
created: 2026-06-14
relevance: średnia
tags:
  - "strategia-AI"
  - "LLM"
  - "trendy-AI"
---

# "Nasi chłopcy" i niemożliwość historii maszynowej

Marcin Wilkowski analizuje ograniczenia [[LLM|dużych modeli językowych]] w praktyce historycznej, inspirując się kontrowersyjną wystawą Muzeum Gdańska o Polakach wcielonych do Wehrmacht. Kluczowy argument: [[LLM]]y są strukturalnie niezdolne do pisania wbrew dominującym narracjom w danych treningowych – mogą powielać popularne wizje historii, ale nie są w stanie wygenerować przeciwhistorii wymagającej sięgnięcia po marginalne, nieortodoksyjne źródła. Modele nie posiadają „pamięci wertykalnej" – nie wiedzą, z jakiego źródła pochodzi dany token, co czyni ich wypowiedzi „kategorycznie niemożliwymi do śledzenia". Nawet jeśli technicznie można zmusić model do napisania alternatywnej narracji, reprodukuje on statystyczny mainstream, a nie krytyczne myślenie historyczne.

## Frameworki i metody

**3 strukturalne ograniczenia LLM w historiografii (wg Kansteinera i Hughes-Warrington):**

1. **Brak zdolności do contra-narracji** — modele są strukturalnie niezdolne do pisania wbrew własnemu zestawowi treningowemu; efekt zawężonego wyszukiwania wzmacnia dominujące narracje zamiast je kwestionować.

2. **Brak pamięci wertykalnej** — modele nie przechowują informacji o źródle tokenów; wypowiedzi są „kategorycznie niemożliwe do śledzenia", co eliminuje możliwość przypisów i weryfikacji w naukowym sensie. Narzędzia [[RAG]] mogą częściowo to naprawić, wymagają jednak udostępnienia specyficznych, wysokiej jakości źródeł.

3. **Niemożność doświadczenia i sprawczości społecznej** — historia to nie tylko tekst i fakty, ale też przestrzeń muzeum, spotkanie ludzi, debata publiczna. Interfejs ekranu nie zastąpi tych wymiarów.

## Wnioski

- [[LLM]]y reprodukują statystyczny mainstream danych treningowych – nie nadają się do tworzenia historii kontrnarracyjnej bez ręcznie dobranego korpusu [[RAG]] i precyzyjnych promptów uwzględniających złożoność historyczną.
- Brak „pamięci wertykalnej" w modelach jest fundamentalnym problemem dla każdej dziedziny wymagającej weryfikowalnych referencji – nie tylko historii, ale też dziennikarstwa, nauki i edukacji.
- Artykuł (z 2022 roku, przed premierą ChatGPT) wciąż aktualnie diagnozuje ograniczenia – i przypomina, że krytyczna zdolność do pisania „wbrew" jest domeną człowieka, nie maszyny.

## Zastosowanie

Przy szkoleniach z AI dla NGO – przydatny jako case study pokazujący, że LLM reprodukuje mainstream i nie zastąpi krytycznego myślenia eksperckiego. Przy pracy z organizacjami nad strategią AI: argument, że modele bez odpowiednio dobranej bazy wiedzy (RAG) będą powielać ogólne, uproszczone narracje – istotne przy wdrożeniach dla organizacji z unikalną misją lub kontrnarracyjnym głosem.
