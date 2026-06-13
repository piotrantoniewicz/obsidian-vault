---
categories:
  - "Emails"
published: 2026-06-13
created: 2026-06-13
labels:
  - "Tomasz Woliński"
relevance: wysoka
tags:
  - "narzędzia-AI"
  - "context-engineering"
  - "strategia-AI"
---

# Agent się nie uczy — uczą się jego wspomnienia

Tomasz Woliński (stormit.pl) stawia tezę, którą trudno odeprzeć: kolejna premiera modelu nie sprawi, że agent zacznie pamiętać Twój kontekst — bo model z definicji zaczyna każdą sesję od zera. Mądrzeją tylko wspomnienia, nie model. Kluczowym problemem jest jednak nie brak pamięci, lecz jej jakość: badanie Chroma na 18 modelach pokazało, że każdy z nich traci jakość wraz ze wzrostem kontekstu. Rozwiązaniem nie jest więcej wspomnień, ale ich regularna konsolidacja — analogia do ludzkiego snu, którą wdrożyły już Anthropic i OpenAI. OpenAI podaje konkret: skuteczność przypominania faktów wzrosła z 41,5% do 82,8% po wdrożeniu procesu porządkowania pamięci.

## Frameworki i metody

- **Pętla Kontekstu (5 kroków)** — system pracy z pamięcią agenta na zwykłych plikach markdown:
  1. **Działaj** — sesja robi swoją robotę, nic nie zmieniasz
  2. **Przechwyć** — na koniec sesji agent dopisuje lekcje do pliku (wymusza to mechanizm, nie ludzka pamięć)
  3. **Routuj** — lekcja trafia do właściwego pliku (reguła ogólna → instrukcje; procedura → osobny plik; jeden wielki plik pamięci = chaos)
  4. **Konsoliduj** — raz w tygodniu: duplikaty out, nieaktualne out, reszta skrócona (krok, który wszyscy pomijają)
  5. **Załaduj** — następna sesja startuje z czystą, krótką pamięcią

- **Quick Win — plik lekcji** — minimalna działająca wersja pętli:
  - Utwórz plik `lekcje.md`
  - Dodaj do instrukcji AI: *"Na koniec dłuższej rozmowy zaproponuj 1-2 lekcje warte zapamiętania — jeden punkt na lekcję, bez narracji"*
  - W [[Claude Code]] agent dopisuje lekcje sam do pliku; w ChatGPT wklejasz propozycję do notatki
  - Raz w tygodniu wytnij połowę: duplikaty, oczywistości, nieaktualne (~5 min start, 30 min tygodniowo)

- **"Śnienie" (memory consolidation)** — proces wdrożony przez [[Anthropic]] i [[OpenAI]]: w tle czyta zebrane wspomnienia, scala duplikaty, wyrzuca nieaktualne, zapisuje czystą wersję. Kopia procesu konsolidacji pamięci z fazy REM u ludzi.

## Kluczowe dane

- 18 modeli zbadanych przez Chroma: wszystkie tracą jakość wraz ze wzrostem kontekstu
- OpenAI: skuteczność przypominania faktów wzrosła z **41,5% do 82,8%** po wdrożeniu konsolidacji wspomnień
- Cursor wdrożył w pełni automatyczną pamięć — i wycofał ją po kilku miesiącach (miliony użytkowników, ten sam wniosek)

## Wnioski

- Budowanie na najnowszym modelu to ryzyko operacyjne — jak pokazał przypadek Claude Fable 5 wyłączonego przez rząd USA po 3 dniach; system oparty na plikach i pętli kontekstu pozwala zmienić jedną linijkę i pracować dalej na poprzednim modelu
- Automatyczny zapis wspomnień bez regularnego przeglądu i cięcia degraduje jakość agenta — "zatruty plik pamięci" działa gorzej niż żadna pamięć
- Kto ma prawo pisać do pamięci agenta to pytanie bezpieczeństwa, nie filozofii: zatruta treść zapisana jako "lekcja" (z maila, strony WWW, CV) odpala się tydzień później w innej sesji — udokumentowany wektor ataku

## Cytat

> *Inteligencja bez pamięci wciąż budzi się każdego ranka jako ta sama, czysta kartka.*

## Zastosowanie

Pętla Kontekstu to gotowy system do wdrożenia w [[Claude Code]] już dziś — szczególnie przydatny przy budowie Second Brain i automatyzacji pracy z [[Obsidian]]. Konsolidacja wspomnień (krok 4) jest bezpośrednią inspiracją dla pluginu `/anthropic-skills:consolidate-memory`. Argument o bezpieczeństwie pamięci agenta warto uwzględnić przy projektowaniu wdrożeń AI dla NGO — zwłaszcza gdy agent czyta zewnętrzne dokumenty (maile, strony, formularze).
