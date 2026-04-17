---
categories:
  - "Emails"

published: 2026-01-09
created: 2026-03-06
labels:
  - "Kodożercy"
relevance: średnia
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "prompt-engineering"
---

# Jak wygląda dojrzała praca z AI. Przykład setupu Borisa Cherny'ego

[[Boris Cherny]], twórca [[Claude Code]], opisał na X swój codzienny workflow z AI — bez marketingu, jako opis realnej praktyki. Kluczowe elementy jego setupu to: praca na kilku równoległych instancjach [[Claude]], plik `CLAUDE.md` jako trwała pamięć projektu (aktualizowana po każdym błędzie), planowanie zakresu przed generowaniem kodu oraz weryfikacja wyników przez samego agenta. Podejście to pokazuje AI zintegrowane w proces, a nie używane okazjonalnie — liczy się nie czas jednej odpowiedzi, lecz minimalna liczba iteracji potrzebnych do dowiezienia wyniku. Dla większości zastosowań autor sugeruje stopniowe wdrożenie: najpierw reguły współpracy, potem plan przed działaniem, na końcu równoległość.

## Wnioski
- Plik `CLAUDE.md` (lub odpowiednik w dowolnym projekcie) to najprostsza zmiana o najwyższym zwrocie: kilka reguł zapisanych raz eliminuje powtarzające się błędy w każdej sesji z [[AI]]
- Planowanie zakresu przed uruchomieniem agenta to zasada, którą można przenieść bezpośrednio do automatyzacji dla NGO — im lepiej opisany kontekst na wejściu, tym mniej ręcznych korekt na wyjściu
- Weryfikacja przez samego agenta (testy, przejście po interfejsie) to element często pomijany przy wdrożeniach, a decydujący o jakości — powinien stać się standardem w automatyzacjach budowanych dla organizacji

## Cytat
> [[AI]] zaczyna działać sensownie dopiero wtedy, gdy ma proces, pamięć i możliwość sprawdzenia swojej pracy.

## Zastosowanie
Setup [[Boris Cherny|Borisa Cherny'ego]] to gotowy szablon do przekazania podczas szkoleń i wdrożeń AI w NGO — szczególnie koncepcja pliku z regułami współpracy nadaje się natychmiast do zastosowania nawet przez osoby bez doświadczenia technicznego.
