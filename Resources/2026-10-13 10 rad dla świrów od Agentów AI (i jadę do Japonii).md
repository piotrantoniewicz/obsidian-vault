---
categories:
  - "Emails"
published: 2026-10-13
created: 2026-10-16
labels:
  - "Mirek Burnejko"
relevance: średnia
tags:
  - "narzędzia-AI"
  - "automatyzacja"
  - "strategia-AI"
---

# 10 rad dla świrów od Agentów AI (i jadę do Japonii)

Mirek Burnejko ([[AI Biznes Lab]]) zbiera dziesięć praktyk, dzięki którym [[Claude Code]] i [[Codex]] robią w firmie dużo więcej niż pojedyncze zadania. Wspólny mianownik: agent ma sam pilnować kosztów, bezpieczeństwa, powiadomień i procesów, a człowiek zostaje przy decyzjach i zatwierdzaniu. Notatka obejmuje wyłącznie część o 10 radach; pozostałe wątki maila (nagrania z meetupu, promocja warsztatu, notatki książkowe) pominięto.

## Frameworki i metody
- Chmura dla agentów — podłącz agentów do [[AWS]] (Lambda, S3, bazy danych, WAF, CloudWatch), zamiast samodzielnie kombinować z integracjami; przyspiesza budowanie i zdejmuje zarządzanie maszynami wirtualnymi.
- System CostSec (koszty + bezpieczeństwo) — jeden cel: cykliczne audyty, w których każde uruchomienie dodaje nowe testy bezpieczeństwa, a potem łata i testuje znalezione dziury.
- Asystent notyfikacji — wszystkie powiadomienia (maile, logi, zdarzenia systemowe, błędy chmury) w jednym miejscu; agent łączy kropki i sam rozbudowuje system, by łapać więcej logów, a wyciągać tylko to, co ważne.
- Skill `/end` — uruchamiany po sesji, daje maksymalnie 3 sugestie, jak ulepszyć system/[[harness]] przed następną sesją.
- Pytaj agenta — zamiast zgadywać, zapytaj Claude Code/Codex, co zrobić, by rzeczy robiły się same lub by nie powstawały błędy w analizie liczb.
- Strażnicy — małe programy sprawdzające pracę agenta, zanim zrobi coś nieodwracalnego; agent analizuje sesje i proponuje ich zestaw (u autora: 149).
- Czujka — skill, który analizuje kontekst, maile i powiadomienia, wyszukuje i opisuje procesy firmowe oraz proponuje automatyzacje; wersja solo darmowa, dane zostają lokalnie.
- [[Agent Team]] bez orkiestratora — silniejszy model (np. Opus 5.5) planuje zadania i uruchamia zespół agentów na słabszym modelu (np. Sonnet 5.5), który wykonuje pracę.
- Agent w chmurze — Claude Code/Codex na maszynie wirtualnej z dostępem SSH, wykonujący zadania cykliczne; cel to logować się tam jak najrzadziej.
- Analiza każdej ciekawej nowości — wrzucaj ją do asystenta (u autora „cto"), który ocenia przydatność nie w teorii, ale w konkretnym systemie firmy.

## Kluczowe dane
- 149 strażników działa w systemie autora.
- Czujka v0.1.6; w przykładzie z maila: 276 plików i 0% opisanych procesów end-to-end.
- Limit skilla `/end`: maks. 3 sugestie po sesji.

## Wnioski
- Największa dźwignia nie leży w pojedynczych promptach, lecz w warstwie nadzorczej wokół agenta: [[strażnicy]], audyty CostSec i skill `/end` zamieniają każdą sesję w ulepszenie systemu.
- Pytanie „co możemy zrobić, żeby to robiło się samo?" zadane [[Claude Code]] to tania metoda odkrywania automatyzacji, którą można stosować od ręki.
- Praca z [[Agent Team]] według schematu „droższy model planuje, tańszy wykonuje" pozwala kontrolować koszty bez budowania złożonej orkiestracji.

## Cytat
> Nie bądź czytelnikiem nagłówków — wrzuć każdą ciekawą rzecz do asystenta, który sprawdzi, jak użyć jej w naszym systemie, a nie w teorii.

## Zastosowanie
Rady 4, 6 i 8 (skill `/end`, strażnicy, Agent Team) można wprost przenieść na własne [[pluginy Claude Code]] i pracę w vaultcie. Rada 3 i Czujka są punktem wyjścia do ofert wdrożeniowych dla organizacji społecznych, które toną w powiadomieniach i nieopisanych procesach.
