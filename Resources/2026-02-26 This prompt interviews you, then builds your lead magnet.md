---
categories:
  - Emails
published: 2026-02-26
created: 2026-03-18
labels:
  - Ryan Carr
relevance: wysoka
tags:
  - produkty-cyfrowe
  - prompt-engineering
  - digital-campaigning
---

# This prompt interviews you, then builds your lead magnet

Ryan Carr udostępnia 3500-słowowy wizard prompt, który w 10–15 minut przeprowadza przez trzy fazy: wywiad (2–3 wymiany zamiast 20-punktowego formularza, Claude sam analizuje stronę www i dobiera kolory/fonty), prezentację 3 różnych konceptów lead magnetu (z 10 archetypów: scorecard, kalkulator ROI, assessment diagnostyczny, quiz, benchmark, silnik rekomendacji), i finalny build jako samodzielny plik HTML gotowy do hostowania. Output to w pełni interaktywny lead magnet z bramką emailową — bez backendu, jeden plik. Prompt działa w Claude (conversation lub Claude Code) i używa modelu Opus 4.6.

## Wnioski
- Wizard prompt jako framework redukuje „slop factor" AI: zamiast generowania od razu, najpierw zbiera kontekst przez ustrukturyzowany wywiad, co daje dużo bardziej dopasowany output niż zwykły prompt.
- Technika „zawsze proś o opcje" — prompt prezentuje 3 różne koncepty lead magnetu przed buildem, co pozwala wybrać najlepszy kierunek zamiast przyjmować pierwszą propozycję.
- Plik HTML bez backendu można hostować wszędzie (GitHub Pages, Netlify, Beehiiv custom page); jedyne co trzeba podpiąć ręcznie to URL formularza email provider.

## Cytat
> „Zamiast trafiać na 20-punktowy formularz, AI zaczyna od jednego otwartego pytania i wnioskuje resztę z twoich odpowiedzi."

## Zastosowanie
Użyć wizard prompta do zbudowania lead magnetu dla [[dobryai.pl]] — np. interaktywnego quizu „Gotowość Twojej NGO na AI" zbierającego maile i dającego spersonalizowany raport z rekomendacjami narzędzi.
