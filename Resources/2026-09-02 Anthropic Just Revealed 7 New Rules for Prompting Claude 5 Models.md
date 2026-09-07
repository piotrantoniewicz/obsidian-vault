---
categories:
  - Clippings
authors: ["[[Ben AI]]"]
url: "https://www.youtube.com/watch?v=HDmBwU5uvEE"
source: "[[Archives/2026-09-02 Anthropic Just Revealed 7 New Rules for Prompting Claude 5 Models|2026-09-02 Anthropic Just Revealed 7 New Rules for Prompting Claude 5 Models]]"
published: 2026-09-02
created: 2026-09-05
relevance: wysoka
tags:
  - "prompt-engineering"
  - "narzędzia-AI"
  - "context-engineering"
---

# Anthropic Just Revealed 7 New Rules for Prompting Claude 5 Models

Autor omawia siedem zasad promptowania modeli Claude 5 (Opus 5, Fable 5), oparte na oficjalnych wskazówkach Anthropic i wystąpieniu Borisa Cherny'ego na Y Combinator. Główna teza: nowsze, bardziej autonomiczne modele wymagają zmiany podejścia — zamiast szczegółowych instrukcji krok po kroku, lepiej podawać cały kontekst zadania naraz (cel, powód, ograniczenia, kryteria ukończenia) i pozwolić modelowi samodzielnie pracować dłużej. To istotna zmiana nawyków dla każdego, kto na co dzień koryguje prompty do automatyzacji i wdrożeń AI. Autor podkreśla też, że reguły zakazujące ("nigdy nie rób X") działają gorzej niż instrukcje z uzasadnieniem, a nadmierne dopytywanie o weryfikację jest już zbędne, bo modele robią to autonomicznie.

## Frameworki i metody

**7 zasad promptowania modeli Claude 5:**

1. **Podawaj całe zadanie naraz, nie krok po kroku** — opisz cel, powód (why), ograniczenia (guardrails) i kryteria ukończenia (definition of done), a następnie pozwól modelowi pracować samodzielnie przez dłuższy czas.
2. **Używaj skilla „interview me" przed złożonymi zadaniami** — pozwala on dopytać o brakujący kontekst i wygenerować gotowy brief/prompt przed uruchomieniem modelu na dużym zadaniu.
3. **Podawaj „dlaczego", nie tylko „co"** — model podejmuje lepsze mikrodecyzje, gdy rozumie szerszy kontekst i cel zadania, nie tylko literalne polecenie.
4. **Definiuj wyraźnie, jak wygląda „gotowe"** — modele Claude 5 mają tendencję do robienia zbyt dużo, nie zbyt mało; jasne kryteria zakończenia i styl outputu ograniczają zużycie tokenów.
5. **Zamieniaj twarde zakazy na uzasadnione instrukcje** — zamiast „nigdy nie rób X" lepiej działa „rób Y, ponieważ Z"; dotyczy to też plików takich jak [[Claude.md]] i skille.
6. **Nie każ modelowi podwójnie sprawdzać własnej pracy** — Opus 5 i Fable 5 są trenowane do autonomicznej weryfikacji i poprawiania błędów, więc dodatkowe instrukcje typu „sprawdź jeszcze raz" tylko zwiększają koszt bez poprawy jakości.
7. **Koryguj „głos" modelu raz, globalnie** — jeśli Opus 5 staje się zbyt żargonowy lub rozwlekły, warto to naprawić jednym promptem w instrukcjach systemowych (np. Claude desktop, [[Claude.md]]) zamiast poprawiać to za każdym razem.

## Wnioski

- Promptowanie modeli Claude 5 zbliża się do delegowania zadań człowiekowi — liczy się kontekst, powód i jasne kryteria sukcesu, a nie mikrozarządzanie krokami.
- Warto rozważyć wdrożenie własnego frameworku promptowania (cel – powód – ograniczenia – definicja gotowości) przy tworzeniu i aktualizowaniu skilli oraz pluginów [[Claude Code]] używanych w pracy z klientami NGO.
- Zamiana twardych zakazów na instrukcje z uzasadnieniem to konkretna, łatwa do wdrożenia zmiana w istniejących skillach i plikach [[Claude.md]].

## Zastosowanie
Warto przejrzeć istniejące skille i pliki `Claude.md` w projektach Piotra pod kątem zamiany twardych reguł na instrukcje z uzasadnieniem oraz uproszczenia nadmiernie szczegółowych promptów na rzecz opisu celu, kontekstu i kryteriów ukończenia. Framework „cel – dlaczego – ograniczenia – definicja gotowości" można wykorzystać przy szkoleniach z AI dla organizacji jako gotowy checklist promptowania.
