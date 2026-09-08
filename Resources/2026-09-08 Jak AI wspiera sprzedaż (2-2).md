---
categories:
  - "Emails"
published: 2026-09-08
created: 2026-09-08
labels:
  - "wPraktyce"
relevance: średnia
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "context-engineering"
---

# Jak AI wspiera sprzedaż? (2/2)

Autor opisuje drugą część swojego systemu sprzedażowego opartego na AI — tym razem etap po zakończeniu rozmowy handlowej. Każda rozmowa (Fireflies dla wideocalli, dyktafon Plaud dla spotkań na żywo) trafia jako transkrypt do [[Claude Code]], który automatycznie generuje podsumowanie do CRM, listę zadań i draft follow-upu. System buduje też samoistnie rosnącą bazę obiekcji i odpowiedzi z realnych rozmów klientów, zamiast szablonowego playbooku. Tekst kończy się wezwaniem do bezpłatnej konsultacji, ale sama treść ma wartość jako opis konkretnego workflow automatyzacji.

## Frameworki i metody

- **Pętla posprzedażowa** — po każdej rozmowie: (1) nagranie trafia do [[Claude Code]] jako transkrypt, (2) podsumowanie ląduje automatycznie w CRM (Asana), (3) z ustaleń powstają konkretne zadania z przypisaniem i terminem, (4) AI przygotowuje draft follow-upu do akceptacji przez handlowca.
- **Samorosnąca baza wiedzy** — AI wyciąga z transkryptu nietypowe obiekcje klientów i tego samego dnia dopisuje je do wspólnej bazy zespołu razem z odpowiedzią; jeśli obiekcji nie udało się zaadresować, system flaguje potrzebę uzupełnienia założeń na przyszłość.
- **Przekazanie leada bez utraty kontekstu** — przy zmianie osoby prowadzącej temat AI składa podsumowanie całej historii rozmów, wnioski dla zespołu i draft kolejnego maila w głosie osoby przejmującej kontakt; każdy członek zespołu dostaje też briefing o kliencie przed swoją rozmową.

## Kluczowe dane

- Po 20–50–100 rozmowach powstaje playbook oparty na realnych klientach, a nie na szablonie od konsultantów.
- Przekazanie prowadzenia leada (podsumowanie + briefing + draft maila) zajęło ok. 2 „maszyno-godziny", w większości wykonane automatycznie.

## Wnioski

- Automatyzacja pętli nagranie → transkrypt → CRM → zadania → follow-up eliminuje typową stratę wiedzy z rozmów handlowych — wzorzec przenaszalny na spotkania z darczyńcami czy partnerami NGO.
- Samorosnąca baza obiekcji i odpowiedzi z transkryptów to praktyczny przykład [[context engineering]] — budowanie kontekstu dla AI z rzeczywistych rozmów zamiast z gotowych szablonów.
- Płynne przekazywanie prowadzenia relacji (podsumowanie + briefing zamiast godzinnego spotkania) pokazuje, jak AI może ograniczać ryzyko utraty wiedzy przy rotacji osób w zespole.

## Cytat

> System pamięta za wszystkich - i z każdą rozmową jest mądrzejszy.

## Zastosowanie

Wzorzec pętli posprzedażowej i samorosnącej bazy wiedzy można przenieść na pracę z organizacjami pozarządowymi — automatyzację notatek ze spotkań z darczyńcami czy partnerami oraz budowanie wspólnej bazy argumentów i obiekcji zespołu. Przydatne też jako inspiracja przy wdrożeniach AI u klientów Piotra pracujących nad procesami sprzedaży/fundraisingu.
