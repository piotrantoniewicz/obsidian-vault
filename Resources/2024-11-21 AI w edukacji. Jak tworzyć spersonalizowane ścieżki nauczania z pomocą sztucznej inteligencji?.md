---
categories: Clippings
authors: ["[[Bartłomiej Polakowski]]"]
url: https://sektor3-0.pl/blog/ai-w-edukacji-jak-tworzyc-spersonalizowane-sciezki-nauczania-z-pomoca-sztucznej-inteligencji/
source: "[[Archives/2024-11-21 AI w edukacji. Jak tworzyć spersonalizowane ścieżki nauczania z pomocą sztucznej inteligencji?|2024-11-21 AI w edukacji. Jak tworzyć spersonalizowane ścieżki nauczania z pomocą sztucznej inteligencji?]]"
published: 2024-11-21
created: 2026-03-24
relevance: wysoka
tags:
  - "szkolenia-AI"
  - "prompt-engineering"
  - "narzędzia-AI"
---

# AI w edukacji. Jak tworzyć spersonalizowane ścieżki nauczania z pomocą sztucznej inteligencji?

Artykuł [[Bartłomiej Polakowski|Bartłomieja Polakowskiego]] pokazuje krok po kroku, jak przy użyciu [[ChatGPT]] lub [[Claude]] zbudować spersonalizowany program szkoleniowy z indywidualnymi ścieżkami edukacyjnymi — bez drogich platform LMS. Proces składa się z dwóch etapów: (1) stworzenie struktury szkolenia przez prompting — definicja kompetencji, modułów, ankiety wstępnej i przypisania uczestników do ścieżek (Beginner/Intermediate/Advanced); (2) stworzenie interaktywnego chatbota-trenera (jako GPTs lub Project w Claude), który prowadzi uczestnika przez symulacje i role-play, monitoruje postępy i daje feedback. Artykuł zawiera pełne, gotowe do użycia prompty w języku angielskim (z polskim tłumaczeniem) i live demo chatbota do ćwiczenia Instructional Design.

## Frameworki i metody
- Trzystopniowy proces budowania spersonalizowanych ścieżek nauczania z AI:
  1. **Etap 1 — Struktura programu**: prompt generuje moduły, cele, sekwencję, szacowany czas trwania i kryteria ewaluacji; ważna instrukcja: `Don't use learning styles` (brak naukowych dowodów na skuteczność dopasowania do stylów uczenia)
  2. **Etap 2 — Diagnostyka uczestników**: ankieta + test wiedzy wstępnej → analiza wyników przez AI → automatyczne przypisanie do ścieżek (score 0-40%: Beginner, 41-70%: Intermediate, 71-100%: Advanced)
  3. **Etap 3 — Chatbot-trener**: konfiguracja GPTs/Project [[Claude]] jako wirtualny mentor prowadzący symulacje i role-play; struktura: persona → narracja → scenariusz → feedback → podbicie trudności
- Wzorzec prompta dla chatbota szkoleniowego: PERSONA + NARRATIVE + OBJECTIVES (lista sprawdzanych kompetencji) + steps (sekwencja kroków) + feedback structure

## Kluczowe dane
- Badania wskazują: studenci uczą się ponad 2x więcej w krótszym czasie z AI tutorem vs. aktywna nauka w klasie (Research Square, 2024)
- Narzędzia AI mogą zmniejszyć lukę w wynikach dla słabiej radzących sobie uczniów o 20% (McKinsey & Company)

## Wnioski
- Spersonalizowane ścieżki szkoleniowe można zbudować bez platformy LMS — wystarczy [[ChatGPT]] lub [[Claude]] Pro i seria dobrze zaplanowanych promptów; bariera wejścia jest bardzo niska dla osób znających prompt engineering
- Kluczowy insight: instrukcja `Don't use learning styles` w prompcie — [[LLM]] są wytrenowane na publikacjach propagujących style uczenia, więc bez tej instrukcji chatbot będzie je aplikować mimo braku dowodów na ich skuteczność
- Chatbot-trener z role-play jest efektywniejszy niż statyczne materiały — pozwala uczestnikowi ćwiczyć trudne sytuacje (spotkanie z klientem, negocjacje) w bezpiecznym środowisku z natychmiastowym feedbackiem

## Cytat
> Niezależnie od ilości detali, osoby korzystające z Waszych chatbotów dostaną inne odpowiedzi. Nie unikniecie również typowych dla GenAI halucynacji. Dobrze skonstruowany prompt pozwoli jednak nawigować dyskusją we właściwym kierunku i pozwoli zachować jej strukturę.

## Zastosowanie
Artykuł jest bezpośrednio użyteczny przy projektowaniu kursu mailowego „Fundraising z AI" — wzorzec ankieta diagnostyczna → ścieżki → chatbot-trener można zaadaptować na potrzeby szkolenia NGO z różnym poziomem zaawansowania. Prompt chatbota-trenera (role-play spotkanie z klientem) da się przerobić na symulację rozmowy z darczyńcą lub fundatorem. Materiał przydatny też w szkoleniach dla organizacji, gdzie trener chce dać uczestnikom narzędzie do ćwiczenia po szkoleniu.
