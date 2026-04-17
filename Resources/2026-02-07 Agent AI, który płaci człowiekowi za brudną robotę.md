---
categories:
  - "Emails"
published: 2026-02-07
created: 2026-03-06
labels:
  - Tomasz Woliński
relevance: średnia
tags:
  - automatyzacja
  - narzędzia-AI
  - LLM
---
# Agent AI, który płaci człowiekowi za brudną robotę

Woliński opisuje odwrócenie ról w relacji człowiek–maszyna: platforma RentAHuman.ai pozwala agentom AI zlecać ludziom zadania fizyczne i płacić natychmiast w stablecoinach — AI jako pracodawca staje się faktem. Równolegle [[Claude Opus 4.6]] rozszerzył kontekst do 1 mln tokenów przy niezmienionych cenach, co otwiera nowe możliwości pracy z dużymi dokumentami i kodebazami. Kluczowy insight tygodnia to prompt "Dopytaj zanim odpowiesz" — nakazujący modelowi zadawanie pytań przed odpowiedzią — który redukuje liczbę iteracji do dobrego outputu nawet 3-krotnie. W tle: case study automatyzacji analizy 250 000 działek, gdzie latami trwający proces ręczny zastąpiono agentem AI.

## Wnioski
- Prompt "Dopytaj zanim odpowiesz" — model zadaje pytania o niejednoznaczności, brakujący kontekst i definicję sukcesu przed działaniem — drastycznie redukuje liczbę iteracji; szczególnie przydatny przy złożonych zadaniach strategicznych i procesowych.
- [[Claude Opus 4.6]] z 1 mln tokenów kontekstu (bez zmiany cen) otwiera możliwość pracy z całymi dokumentami strategicznymi, raportami NGO, archiwami korespondencji w jednym oknie — bez dzielenia na fragmenty.
- System AI "budujący kontekst" przez automatyczną transkrypcję głosówek, wyciąganie wniosków i zadawanie pytań uszczegóławiających — to gotowy wzorzec dla osobistego systemu wiedzy opartego na [[n8n]] + [[LLM]].

## Cytat
> Najlepsza automatyzacja to nie ta, która zastępuje myślenie. To ta, która pomaga myśleć lepiej.

## Zastosowanie
Prompt "Dopytaj zanim odpowiesz" oraz system głosówka → transkrypt → pytania kontekstowe mogą posłużyć Piotrowi jako gotowy workflow do budowania kontekstu organizacyjnego dla NGO, które korzystają z AI w pracy strategicznej.
