---
categories:
  - "Emails"
published: 2026-02-12
created: 2026-03-06
labels:
  - AI Ninjas
relevance: niska
tags:
  - narzędzia-AI
  - automatyzacja
  - szkolenia-AI
---
# Jak działa Agent Teams w Claude Code

Newsletter AI Ninjas przedstawia ewolucję od subagentów do **Agent Teams** w [[Claude Code]] — nowego trybu pracy, w którym kilka pełnoprawnych agentów koordynuje się nawzajem zamiast być zarządzanych przez centralny węzeł. W modelu subagentowym całą koordynację musiał wykonywać główny agent z ograniczonym oknem kontekstu. Agent teams przełamują to wąskie gardło: agenci komunikują się bezpośrednio, dzielą wspólną kolejkę zadań i samodzielnie pobierają kolejne taski po zakończeniu poprzednich. Synchronizacja stanu odbywa się przez pliki dyskowe i mechanizm `SendMessage`; file locking zapobiega konfliktom. Funkcja jest aktualnie w fazie beta.

## Wnioski
- Główną wartością agent teams jest eliminacja wąskiego gardła koordynacji — [[Claude Code]] nie musi „pilnować" wszystkiego sam, co pozwala na głębsze, wieloperspektywiczne zadania (np. code review z pozycji security + performance + testy jednocześnie).
- Podział subagenci/teams to zasada efektywności kosztowej: proste, atomowe zadania (sprawdź test, wygeneruj plik) = subagenci; złożone zadania wymagające dyskusji i wzajemnej krytyki = agent teams.
- Wzorzec team lead + samoorganizacja jest przenoszalny poza kodowanie — przy projektowaniu automatyzacji procesów w NGO (np. [[Make.com]], [[Langflow]]) warto myśleć o tym, kiedy potrzebna jest hierarchia, a kiedy siatka współpracy.

## Cytat
> Agent teams działają inaczej — agenci piszą do siebie nawzajem, sami biorą kolejne taski z wspólnej listy i kwestionują nawzajem swoje rozwiązania. Zamiast jednego agenta ogarniającego wszystko jest team lead i samoorganizacja zespołu.

## Zastosowanie
Przy budowaniu własnych pluginów i narzędzi AI w [[Claude Code]] warto przetestować tryb agent teams do zadań wymagających kilku perspektyw — np. przygotowania materiałów szkoleniowych z podziałem na role: badacz treści, projektant struktury, krytyk.
