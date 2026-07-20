---
categories:
  - "Emails"
published: 2026-07-17
created: 2026-07-20
labels:
  - "Robert Szewczyk"
relevance: wysoka
tags:
  - "vibe-coding"
  - "automatyzacja"
  - "narzędzia-AI"
---

# 6 dobrych praktyk tworzenia lepszych skills

Robert Szewczyk zebrał w Techletterze sześć zasad pisania skuteczniejszych skilli dla agentów AI (Claude Code, Codex i podobnych narzędzi), oparte na testach Anthropic, warsztacie z Krisem i własnych błędach. Kluczowy problem: przeciętny skill pisany "z palca" odpala się w ok. 20% przypadków, podczas gdy Anthropic celuje w 90% — różnicę robi jakość pola `description`, struktura pliku i kontrola nad tym, kto uruchamia skilla. Tekst dobrze uzupełnia praktykę budowania własnych pluginów Claude Code, którą Piotr już prowadzi.

## Frameworki i metody
- Description decyduje o wszystkim — pole `description` to jedyne, co agent widzi zanim zdecyduje, czy sięgnąć po skilla (limit ok. 1000 znaków); pisz w trzeciej osobie, dodaj wzorzec "use when" i konkretne trigger words.
- Progressive disclosure — skille ładują się na 3 poziomach jak pamięć RAM: nazwa + description (frontmatter) widoczne zawsze; body (reszta SKILL.md) czytane dopiero po wyborze skilla; podfoldery (przykłady, skrypty, szablony) dociągane tylko gdy potrzebne — body trzymaj krótkie, krytyczne instrukcje na górze.
- Skrypty zamiast tekstu — modele AI są niedeterministyczne, więc powtarzalne zadania warto zamykać w skryptach dołączonych do skilla zamiast opisywać słownie; [[Claude Code]] czy Codex mogą taki skrypt przygotować.
- Przykłady > reguły — modele lepiej reagują na konkretne przykłady (np. najlepsza prezentacja, dwa udane teksty na bloga) niż na suchą listę zasad; przykłady przemycają wiedzę domenową, której nie ma żaden gotowiec z sieci.
- Mniej znaczy lepiej — 20 dobrych skilli z własną ekspercką wiedzą działa lepiej niż 100 generycznych; nadmiar utrudnia agentowi wybór właściwego.
- Kontrola uruchamiania — slash-commands pozwalają wywołać skilla ręcznie zamiast liczyć na trafność opisu; dla akcji z realnymi konsekwencjami ustawienie `disable-model-invocation: true` blokuje autonomiczne odpalenie skilla przez model.

## Kluczowe dane
- Skill pisany "z palca" odpala się średnio w ok. 20% przypadków — cel Anthropic to 90%.
- Limit pola `description` to ok. 1000 znaków.

## Wnioski
- Format skilli w [[Claude Code]] wynagradza precyzyjny `description` i krótkie body bardziej niż rozbudowaną treść — warto zweryfikować pod tym kątem własne pluginy (np. artykuly-ngo, content-linkedin).
- `disable-model-invocation: true` to konkretny mechanizm do rozważenia przy skillach wykonujących nieodwracalne akcje (np. zapis do vaultu, wysyłka).
- Zasada "przykłady > reguły" pasuje do podejścia budowania skilli z własnymi wzorcami (np. przykładowe posty LinkedIn, artykuły ngo.pl) zamiast ogólnych instrukcji.

## Cytat
> To NIE agent jest problemem. Problem w tym, że nie dostał od Ciebie jasnej procedury.

## Zastosowanie
Bezpośrednio przydatne przy dopracowywaniu własnych pluginów Claude Code (np. `emails-to-notes`, `galaxy`, `artykuly-ngo`) — warto zrewidować `description` pod kątem trigger words i rozważyć `disable-model-invocation` przy skillach zapisujących do vaultu.
