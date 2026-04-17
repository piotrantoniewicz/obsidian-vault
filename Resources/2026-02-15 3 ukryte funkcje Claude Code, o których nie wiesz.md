---
categories:
  - "Emails"
published: 2026-02-15
created: 2026-03-06
labels:
  - AI Ninjas
relevance: niska
tags:
  - narzędzia-AI
  - szkolenia-AI
  - strategia-AI
---
# 3 ukryte funkcje Claude Code, o których nie wiesz

Newsletter AI Ninjas prezentuje trzy mniej znane funkcje [[Claude Code]], które znacząco zmieniają sposób pracy z agentem. **Pipe mode** (`claude -p`) umożliwia odpytywanie modelu jednym poleceniem z terminala — bez otwierania sesji interaktywnej — i pozwala wpiąć Claude Code w dowolny pipeline (CI/CD, pre-commit hooks, skrypty bash wysyłające raporty na [[Slack]]). **Fast mode** (`/fast`) przyspiesza generowanie 2,5× kosztem wyższych opłat za token, przydatny przy krótkich iteracjach i debugowaniu na żywo. **Auto memory** (`MEMORY.md`) daje agentowi pamięć między sesjami — Claude sam zapisuje wzorce projektu i preferencje użytkownika, a każdy projekt ma oddzielny katalog pamięci.

## Wnioski
- Pipe mode odblokuje [[Claude Code]] jako komponent automatyzacji — zamiast narzędzia do interaktywnej pracy staje się elementem pipeline'u: poranne podsumowanie logów, analiza błędów w CI, generowanie raportów na [[Slack]] lub e-mail.
- Auto memory (`MEMORY.md`) to mechanizm uczenia się kontekstu projektu bez pracy użytkownika — szczególnie wartościowy przy długich projektach (np. kampanie cyfrowe, strategie NGO), gdzie Claude po kilku sesjach zna specyfikę organizacji.
- Fast mode (`/fast`) sugeruje, że architektura [[Claude Code]] zakłada świadome zarządzanie kosztami i prędkością — warto budować tę świadomość w szkoleniach, by uczestnicy wiedzieli, kiedy optymalizować pod szybkość, a kiedy pod jakość.

## Cytat
> Prawdziwa moc polega na łączeniu z innymi narzędziami — możesz wpiąć [[Claude Code]] w dowolny pipeline: CI/CD, pre-commit hooks, joby. Nie jest zamknięty w interaktywnej sesji.

## Zastosowanie
Pipe mode otwiera możliwość zbudowania automatyzacji raportowania dla NGO: skrypt zbierający dane z kampanii fundraisingowej i wysyłający co rano podsumowanie do zespołu przez [[Make.com]] lub bezpośrednio na [[Slack]].
