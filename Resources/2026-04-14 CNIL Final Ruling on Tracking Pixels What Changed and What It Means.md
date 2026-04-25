---
categories: Clippings
authors: ["[[Bram Van Daele]]"]
url: https://www.engagor.ai/resources/blog/cnil-tracking-pixel-final-recommendation-2026
source: "[[Archives/2026-04-14 CNIL Final Ruling on Tracking Pixels What Changed and What It Means|2026-04-14 CNIL Final Ruling on Tracking Pixels What Changed and What It Means]]"
published: 2026-04-14
created: 2026-04-24
relevance: średnia
tags:
  - "digital-campaigning"
  - "content-marketing"
---

# CNIL Final Ruling on Tracking Pixels: What Changed and What It Means

Francuska [[CNIL]] opublikowała 14 kwietnia 2026 ostateczną rekomendację dotyczącą tracking pixels w emailach — potwierdzając, że piksele śledzące otwieranie wiadomości podlegają tym samym wymogom co cookies i wymagają wyraźnej, odrębnej zgody odbiorcy. Kluczową nowością względem projektu jest wprowadzenie wyjątku dla celów dostarczalności: nadawcy mogą używać danych o otwarciach bez zgody wyłącznie w celu identyfikacji nieaktywnych subskrybentów i ich usunięcia z listy wysyłkowej. Artykuł precyzyjnie wyjaśnia, co wyjątek obejmuje, a czego nie — i dlaczego większość systemów emailowych nie jest na to przygotowana. Autor wskazuje, że kierunek regulacji w całej Europie jest jasny: indywidualny tracking otwarć jako bezpłatny sygnał marketingowy jest w strukturalnym odwrocie.

## Frameworki i metody

- **Podwójna zgoda CNIL** — dwie osobne zgody wymagane od odbiorcy: (1) na otrzymywanie emaili marketingowych, (2) osobno na tracking pixel. Nie można ich łączyć w jeden checkbox.
- **Wyjątek dostarczalności** — tracking bez zgody jest dozwolony wyłącznie, gdy:
  1. Dane ograniczone są do absolutnego minimum
  2. Celem jest wyłącznie identyfikacja nieaktywnych odbiorców i ich usunięcie z listy
  3. Dane nie trafiają do żadnego innego systemu (scoring, segmentacja, personalizacja, A/B testy)
- **Harmonogram przejścia** — dla istniejących list: 3 miesiące na poinformowanie odbiorców o pikselu i danie im możliwości sprzeciwu. Dla nowych adresów zebranych po 14 kwietnia 2026: pełny wymóg zgody od razu.

## Kluczowe dane

- Termin dostosowania istniejących list do nowych wymogów: 3 miesiące od 14 kwietnia 2026
- Tracking otwarć bez zgody: dopuszczalny tylko dla celów dostarczalności — nie dla marketingu
- Kliknięcia, konwersje i odpowiedzi na emaile: **nie są objęte** regulacją (nie wymagają piksela)

## Wnioski

- Organizacje prowadzące kampanie emailowe do odbiorców z Francji muszą od teraz zbierać oddzielną zgodę na tracking — segment listy z taką zgodą będzie mniejszy i nie będzie reprezentatywny dla całej bazy, co zniekształca analizę skuteczności kampanii
- Metryki oparte na kliknięciach, konwersjach i odpowiedziach stają się ważniejsze niż open rate — warto już teraz przestawić pomiar efektywności kampanii NGO na te sygnały
- Choć rekomendacja dotyczy formalnie prawa francuskiego, [[CNIL]] historycznie wyznacza kierunek dla całej UE — należy ją traktować jako zapowiedź szerszych zmian regulacyjnych w Polsce i reszcie Europy

## Zastosowanie

Przy projektowaniu kampanii emailowych dla polskich NGO warto zacząć zbierać oddzielną zgodę na tracking już na etapie zapisu — to łatwiejsze niż retroaktywna zbiórka zgód. W kursie "Fundraising z AI" temat może posłużyć jako przykład konieczności budowania strategii emailowej na sygnałach odpornych na zmiany regulacyjne (kliknięcia, konwersje). Organizacje korzystające z [[Make.com]] do automatyzacji kampanii emailowych powinny sprawdzić, czy ich flow nie łączy danych dostarczalności z danymi segmentacyjnymi.
