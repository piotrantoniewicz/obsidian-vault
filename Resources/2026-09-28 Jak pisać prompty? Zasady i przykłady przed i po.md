---
categories:
  - Clippings
authors: ["[[Mateusz Wojdalski]]"]
url: "https://devstockacademy.pl/blog/narzedzia-i-automatyzacja/jak-pisac-prompty-przyklady/?utm_source=newsletter&utm_medium=email&utm_term=2026-09-29&utm_campaign=KSeF+od+stycznia+dla+ka%C5%BCdej+JDG+Kary+dopiero+w+2028"
source: "[[Archives/2026-09-28 Jak pisać prompty? Zasady i przykłady przed i po|2026-09-28 Jak pisać prompty? Zasady i przykłady przed i po]]"
published: 2026-09-28
created: 2026-09-29
relevance: wysoka
tags:
  - "prompt-engineering"
  - "szkolenia-AI"
  - "narzędzia-AI"
---

# Jak pisać prompty? Zasady i przykłady przed i po

Artykuł DevstockAcademy zbiera siedem zasad promptowania wspólnych dla oficjalnych przewodników [[Anthropic]], [[Google]] i [[OpenAI]] i pokazuje je na polskich przykładach z codziennej pracy (mail do klienta, streszczenie umowy, plan tygodnia). Główna myśl: model zna świat, ale nie zna użytkownika, więc każdą lukę w kontekście wypełni czymś przeciętnym — trzeba mu dać kontekst i powód, przykład oczekiwanego wyniku oraz jasno opisany format. Druga część dotyczy ograniczania halucynacji (cytaty, „nie wiem”, weryfikacja u źródła), a trzecia obala mity o formułkach typu „jesteś najlepszym ekspertem”. To gotowy, dobrze uporządkowany materiał szkoleniowy.

## Frameworki i metody

**Siedem zasad promptowania:**
1. Pisz konkretnie: co ma powstać, dla kogo, jak długie, w jakim tonie.
2. Dodaj kontekst i powód (np. zakaz wielokropków z wyjaśnieniem, że tekst przeczyta syntezator mowy).
3. Pokaż przykład (Google: zawsze; Anthropic: 3–5) — zwykle daje najwięcej.
4. Opisz format odpowiedzi: tabela, lista, liczba zdań, mail z tematem.
5. Zamieniaj ogólniki na liczby („3–5 zdań” zamiast „dość krótko”).
6. Mów, co zrobić, zamiast czego unikać.
7. Dziel duże zadania na numerowane kroki.

**Długie materiały:** dokument na początku, pytanie na końcu; instrukcję oddzielić od materiału.

**Ograniczanie halucynacji:**
- Pozwól napisać „nie wiem” lub „brak w dokumencie”.
- Poproś najpierw o dosłowne cytaty, potem o analizę.
- Każ do każdego twierdzenia znaleźć cytat i usunąć te bez potwierdzenia.
- Ogranicz model do wklejonego materiału.
- Zadaj to samo pytanie kilka razy i porównaj fakty.

**Szablon promptu (sześć pól):** Kontekst, Zadanie, Materiał, Format, Zasady, Przykład.

**Test:** pokaż prompt koledze, który nie zna zadania — jeśli nie wiedziałby, co zrobić, model też nie będzie wiedział.

## Kluczowe dane
- Wklejenie długiego dokumentu na początku, a pytania na końcu poprawia jakość odpowiedzi nawet o 30% (testy [[Anthropic]]).
- Przykłady w prompcie: 3–5 według Anthropic.

## Wnioski
- Przewodniki [[Anthropic]], [[Google]] i [[OpenAI]] zgadzają się w najważniejszych punktach, więc jeden, spójny zestaw zasad wystarcza na szkoleniach dla zespołów niezależnie od używanego modelu.
- Zestaw „przed i po” jest skutecznym formatem dydaktycznym: pokazuje, że różnicę robi kontekst, format i liczby, a nie „magiczne formułki”; rola ma sens tylko wtedy, gdy zawiera zadanie.
- Halucynacje ogranicza się procesem (cytaty, „nie wiem”, weryfikacja), a nie prośbą o procent pewności; żadna technika ich nie eliminuje, więc ważne informacje trzeba sprawdzać u źródła.

## Zastosowanie
Gotowa struktura do warsztatu „Prompty dla organizacji społecznych”: siedem zasad, szablon sześciu pól i ćwiczenie przed/po na przykładach z sektora (mail do darczyńcy, streszczenie umowy grantowej, plan kampanii). Warto też zaadaptować sekcję o halucynacjach do checklisty weryfikacji w kursie „Fundraising z AI”.
