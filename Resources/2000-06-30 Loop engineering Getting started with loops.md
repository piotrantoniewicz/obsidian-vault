---
categories:
  - Clippings
authors: ["[[Anthropic]]"]
url: "https://claude.com/blog/getting-started-with-loops"
source: "[[Archives/2000-06-30 Loop engineering Getting started with loops|2000-06-30 Loop engineering Getting started with loops]]"
published: 2000-06-30
created: 2026-08-25
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "context-engineering"
---

# Loop engineering Getting started with loops

Zespół Claude Code definiuje "loop engineering" jako projektowanie cykli, w których agent powtarza pracę do spełnienia warunku stopu, zamiast pojedynczego promptu. Artykuł porządkuje cztery typy pętli — turn-based, goal-based, time-based i proaktywne — według sposobu wyzwalania, kryterium zakończenia i typu zadania, do którego pasują. Kluczowa teza: nie każde zadanie wymaga złożonej pętli — warto zaczynać od najprostszego rozwiązania i sięgać po bardziej złożone wzorce selektywnie. Tekst daje też praktyczne wskazówki dot. utrzymania jakości kodu (skille jako sposób na samoweryfikację, druga agentowa recenzja) i zarządzania zużyciem tokenów (dobór modelu, jasne kryteria stopu, piloty przed dużym uruchomieniem).

## Frameworki i metody

**Cztery typy pętli w Claude Code:**

1. **Turn-based** — wyzwalane promptem użytkownika; Claude sam ocenia, że zadanie jest skończone lub potrzebuje więcej kontekstu. Najlepsze do krótkich, jednorazowych zadań. Jakość weryfikacji poprawia się przez zapisanie kroków sprawdzających jako [[SKILL.md]].

2. **Goal-based (`/goal`)** — wyzwalane ręcznie, kończy się po osiągnięciu zdefiniowanego celu lub limitu liczby prób. Najlepsze do zadań z mierzalnymi kryteriami sukcesu (np. konkretny wynik testu, próg punktowy).

3. **Time-based (`/loop`, `/schedule`)** — wyzwalane interwałem czasowym; kończy się, gdy użytkownik je anuluje lub praca się zakończy (np. PR zostaje zmergowany). Najlepsze do pracy cyklicznej lub interakcji z systemami zewnętrznymi. `/loop` działa lokalnie na komputerze użytkownika, `/schedule` przenosi pętlę do chmury.

4. **Proaktywne** — wyzwalane zdarzeniem lub harmonogramem bez udziału człowieka w czasie rzeczywistym; cała rutyna działa, dopóki nie zostanie wyłączona. Najlepsze do powtarzalnych, dobrze zdefiniowanych strumieni pracy (triage zgłoszeń, migracje, aktualizacje zależności). Łączy pozostałe prymitywy z auto mode i dynamic workflows.

## Wnioski

- Dobór typu pętli zależy od trzech pytań: kto/co wyzwala pracę, jakie jest kryterium stopu i czy zadanie ma weryfikowalne kryteria sukcesu — to praktyczna checklista przy projektowaniu własnych automatyzacji w [[Claude Code]].
- Jakość wyniku pętli zależy od systemu wokół niej: czysty kodebase, możliwość samoweryfikacji (skille), dostępna dokumentacja i druga, niezależna recenzja agentowa.
- Zarządzanie kosztem pętli to nie tylko dobór modelu — to też jasne kryteria stopu, pilotaż na małej próbce przed dużym uruchomieniem i dopasowanie częstotliwości sprawdzania do tego, jak szybko zmienia się obserwowany system.

## Cytat
> Pętle, które piszą kod, potrzebują pętli, które ten kod sprawdzają.

## Zastosowanie
Bezpośrednio przydatne przy rozwijaniu własnych pluginów Claude Code — pomaga świadomie dobrać prymityw (turn-based / `/goal` / `/loop` / `/schedule`) zamiast domyślnie sięgać po najbardziej złożony wariant. Warto rozważyć zaszycie kroków weryfikacji jako SKILL.md w istniejących pluginach (np. clippings-to-notes, dowod-troski), zamiast polegać na ręcznym sprawdzaniu. Framework pytań (wyzwalacz / kryterium stopu / weryfikowalność) można też wykorzystać przy projektowaniu automatyzacji dla klientów NGO korzystających z Make.com czy Langflow.
