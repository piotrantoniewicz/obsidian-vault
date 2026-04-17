---
categories: Clippings
authors:
  - '[[Marzena Kacprowicz]]'
url: >-
  https://sektor3-0.pl/blog/recykling-tresci-jak-zautomatyzowac-tworzenie-transkrypcji/
source: >-
  [[Archives/2025-02-05 Recykling treści Jak zautomatyzować tworzenie
  transkrypcji postów do mediów społecznościowych i wpisów na bloga|2025-02-05
  Recykling treści Jak zautomatyzować tworzenie transkrypcji postów do mediów
  społecznościowych i wpisów na bloga]]
published: '2025-02-05'
created: '2026-03-24'
relevance: wysoka
tags:
  - automatyzacja
  - content-marketing
  - narzędzia-AI
---
# Recykling treści — jak zautomatyzować tworzenie transkrypcji, postów do mediów społecznościowych i wpisów na bloga

Artykuł [[Marzena Kacprowicz|Marzeny Kacprowicz]] opisuje krok po kroku budowę automatyzacji w [[Make.com]], która z pliku wideo nagrywanego webinaru generuje: transkrypcję, serię postów na Facebooka i wpis na blog — wszystko zapisywane automatycznie na Dysku Google i odsyłane e-mailem. Wyzwalaczem jest wiadomość na specjalny adres mailhook; transkrypcję tworzy [[OpenAI]] Whisper, a posty i wpis bloga kolejne moduły OpenAI z promptami. Artykuł zawiera szczegółowe zrzuty ekranu i videotutoriale dla każdego kroku. Autorka podkreśla, że wyniki AI należy traktować jako szkic do doszlifowania przed publikacją.

## Frameworki i metody
- **Schemat automatyzacji recyklingu treści (Make.com):**
  1. Trigger: Webhooks → Custom mailhook (specjalny adres e-mail) — wysłanie wiadomości z wideo w załączniku uruchamia scenariusz.
  2. Moduł OpenAI → Create a Transcription — transkrypcja nagrania (plik max 25 MB).
  3. Router — rozdzielenie procesu na równoległe ścieżki.
  4. Ścieżka 1: Google Docs → Create a Document (transkrypcja) + Google Drive → Download + Gmail → Send (odesłanie pliku nadawcy).
  5. Ścieżka 2: OpenAI → Create a Completion (posty na Facebook) → Google Docs → Create a Document.
  6. Ścieżka 3: OpenAI → Create a Completion (wpis na blog) → Google Docs → Create a Document.
- **Wymagane narzędzia:** [[Make.com]], Gmail, Dysk Google, OpenAI Platform (klucz API, kredyty ~5$).
- **Parametr Temperature w OpenAI:** im niższy (np. 0.2), tym bardziej dosłowna odpowiedź; wyższy = bardziej kreatywna i zróżnicowana.

## Kluczowe dane
- Koszt startowy: jednorazowy pakiet kredytów OpenAI za 5$ (6$ z podatkiem) — wystarczy na długi czas, bo każde zapytanie kosztuje ułamek centa.
- Limit rozmiaru pliku wideo: max 25 MB przy wysyłaniu przez mailhook.

## Wnioski
- Recykling treści przez [[Make.com]] + [[OpenAI]] pozwala jednym nagraniem webinaru zasilić kilka kanałów komunikacji jednocześnie — bez ręcznego przepisywania.
- Schemat jest modularny: możliwe rozszerzenie o kolejne ścieżki (np. post na LinkedIn, streszczenie e-mailowe dla subskrybentów).
- Treści AI należy traktować jako szkic — wymagają ludzkiej korekty stylu i dostosowania do głosu organizacji przed publikacją.

## Zastosowanie
To gotowy przepis do wdrożenia dla organizacji prowadzących webinary lub nagrywające treści edukacyjne — szczególnie przydatny jako ćwiczenie na warsztatach z automatyzacji dla NGO. Można też zaadaptować ten schemat dla własnych szkoleń i kursów mailowych: nagranie sesji → transkrypcja → automatyczny post i notatka. Warto rozbudować scenariusz o integrację z [[Notion]] lub [[Obsidian]] jako docelowym miejscem przechowywania wiedzy.
