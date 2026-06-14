---
categories:
  - Clippings
authors: ["[[Marcin Wilkowski]]"]
url: "https://blog.humanistyka.dev/2025/12/jak-rozpoznawac-slopy-ai-w-tekstach-na-pewno-nie-maszynowo"
source: "[[Archives/2025-12-08 Jak rozpoznawać slopy AI w tekstach? Na pewno nie maszynowo|2025-12-08 Jak rozpoznawać slopy AI w tekstach? Na pewno nie maszynowo]]"
published: 2025-12-08
created: 2026-06-14
relevance: średnia
tags:
  - "LLM"
  - "content-marketing"
  - "szkolenia-AI"
---

# Jak rozpoznawać slopy AI w tekstach? Na pewno nie maszynowo

Wilkowski omawia dwa badania definiujące i operacjonalizujące pojęcie „slopu AI" – masowych, monotonnych, niskiej jakości wytworów generatywnych w formie tekstowej. Pierwsze badanie (*The 7Vs of AI Slop*) proponuje typologię opartą na siedmiu cechach: objętość, prędkość, zróżnicowanie, brak wartości, brak weryfikowalności, widoczność algorytmiczna i wirusowość – pokazując, że slop to systemowa cecha kapitalizmu platformowego, a nie zwykły spam. Drugie (*Measuring AI „Slop" in Text*) buduje taksonomię 7 kategorii cech tekstowego slopu (jakość informacji, gęstość, precyzja, powtarzalność itp.) możliwą do użycia jako prompt dla LLM. Kluczowy wniosek: automatyczne wykrywanie slopu maszynowego jest jeszcze zbyt mało zgodne z oceną ludzką, by działać w praktyce.

## Frameworki i metody

**7Vs AI Slop — typologia cech slopu (Bender et al., 2025):**

1. **Volume (objętość)** — masowe generowanie treści wypierających ludzką twórczość z wyszukiwarek, platform i playlist
2. **Velocity (prędkość)** — generowanie na tyle szybkie, że wymyka się moderacji i weryfikacji (fake newsy, meme churn)
3. **Variety (zróżnicowanie)** — wiele form (tekst, grafika, audio, kod), ale stylistycznie homogeniczny
4. **Value (brak wartości)** — „nutritionally empty": hollow essays, workslop, generyczny branding
5. **Verification (brak weryfikowalności)** — nieistniejące cytaty, zmyślone wizerunki, halucynacje
6. **Visibility (widoczność)** — algorytmiczne wzmacnianie: platformy premiują częste, nowe, angażujące treści
7. **Virality (wirusowość)** — popularność przez dziwaczność lub humor; normalizacja slopu

**Taksonomia cech tekstowego slopu do użycia jako prompt (Measuring AI Slop, 2025):**

| Kategoria | Opis |
|---|---|
| Faktualność | Nieprawidłowe lub zmyślone informacje |
| Stronniczość | Pozorna obiektywność ukrywająca punkt widzenia |
| Gęstość informacyjna | Dużo słów, mało treści |
| Adekwatność | Treść nie odpowiada na pytanie / nie spełnia celu |
| Precyzja | Ogólnikowe stwierdzenia bez danych |
| Powtarzalność | Parafrazowanie bez dodania wartości |
| Formatowanie | Nadmierne nagłówki, pogrubienia, podpunkty |
| Spójność | Niespójne przejścia, dygresje |
| Obszerność | Rozwlekłość bez wartości informacyjnej |
| Złożoność słownictwa | Nieadekwatny żargon lub modne słowa |
| Ton | Generyczny głos bez charakteru i perspektywy |

## Wnioski

- Slop nie jest nową wersją spamu – jest zróżnicowany, angażujący i wirusowy, więc nie da się go blokować tak jak niechciane maile; wymaga świadomości odbiorcy, nie filtru technicznego.
- Taksonomia cech tekstowego slopu nadaje się jako baza do promptu dla [[LLM]] do oceny jakości tekstu – ale zgodność maszynowej i ludzkiej oceny jest wciąż zbyt niska, by ufać automatycznej detekcji.
- Granica „wolnej od slopu" treści rysowana jest przez projekt Slop Evader na dacie 22 listopada 2022 (premiera ChatGPT) – co samo w sobie jest symptomatycznym skrótem myślowym.

## Zastosowanie

Przy szkoleniach z AI: taksonomia slopu to gotowy materiał dydaktyczny do ćwiczenia oceny jakości tekstów generowanych przez AI – można ją podać studentom jako checklistę. Dla własnej pracy z klientami: świadomość cech slopu pomaga formułować lepsze briefy i prompty, które minimalizują ryzyko generowania „workslop" w projektach ghostwriterskich i content marketingowych.
