---
categories:
  - "Emails"
published: 2026-02-13
created: 2026-03-06
labels:
  - AI Ninjas
relevance: niska
tags:
  - narzędzia-AI
  - szkolenia-AI
  - strategia-AI
---
# Zbuduj swoje skills w Claude Code

Newsletter AI Ninjas opisuje mechanizm **Skills** w [[Claude Code]] — plików instrukcji przechowywanych w `.claude/skills/`, które agent ładuje selektywnie, tylko gdy zadanie pasuje do opisu skilla. W odróżnieniu od `CLAUDE.md`, który ładuje się w całości przy każdej sesji, skills są aktywowane na żądanie — nagłówki skanowane są zawsze, pełna treść tylko przy dopasowaniu. To podejście oszczędza tokeny i pozwala utrzymać dużą bibliotekę wyspecjalizowanych instrukcji bez spowalniania modelu. Autor pokazuje, że skill to zaledwie jeden plik `SKILL.md` z sekcją YAML (kiedy aktywować) i treścią (co robić). [[Anthropic]] udostępniło już oficjalny skill `frontend-design` instalowany przez `/install-plugin`.

## Wnioski
- Skills to architektura wiedzy dla agenta — zamiast jednego przepełnionego pliku `CLAUDE.md`, tworzymy modułową bibliotekę: osobny skill do code review, osobny do pisania postów, osobny do analizy danych.
- Mechanizm selektywnego ładowania skilli jest bezpośrednio przenoszalny na własne workflow w [[Claude Code]]: skill `fundraising-copy` z instrukcjami stylu komunikacji dla NGO, skill `campaign-brief` z formatem brief kampanii cyfrowej.
- Oficjalny sklep skillów od [[Anthropic]] (instalacja przez `/install-plugin`) sugeruje rosnący ekosystem — warto śledzić dostępne pluginy jako gotowe rozwiązania do wdrożeń AI w organizacjach.

## Cytat
> Skills działają sprytniej — Claude ładuje pełne instrukcje tylko wtedy, kiedy dostaje zadanie pasujące do opisu skilla. Nie zużywasz tokenów na rzeczy, których akurat nie potrzebujesz.

## Zastosowanie
Przy budowaniu własnych narzędzi AI dla NGO warto wdrożyć skills jako sposób na skodyfikowanie wiedzy organizacyjnej — każdy powtarzalny proces (raport, brief, mail do darczyńcy) może mieć swój skill, który utrzymuje spójność stylu i standardów.
