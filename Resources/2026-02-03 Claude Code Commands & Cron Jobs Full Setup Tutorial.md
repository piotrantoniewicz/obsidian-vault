---
categories: Clippings
authors: ["[[Allie K Miller]]"]
url: https://www.youtube.com/watch?v=l6V0u3ZIgDI
source: "[[Archives/2026-02-03 Claude Code Commands & Cron Jobs Full Setup Tutorial|2026-02-03 Claude Code Commands & Cron Jobs Full Setup Tutorial]]"
published: 2026-02-03
created: 2026-04-06
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "context-engineering"
---

# Claude Code Commands & Cron Jobs Full Setup Tutorial

[[Allie K Miller]] pokazuje, jak zbudować własne polecenia slash (slash commands) w [[Claude Code]], połączyć je z zewnętrznymi systemami przez [[MCP]] (na przykładzie Google Workspace / Gmail) i uruchomić automatycznie na określonym harmonogramie za pomocą cron jobów. Centralnym przykładem jest polecenie `/UE` (urgent emails) — co piątek o 9:00 Claude Code sprawdza Gmail w poszukiwaniu pilnych e-maili bez odpowiedzi i wysyła użytkownikowi podsumowanie z bezpośrednimi linkami. Tutorial pokazuje też łączenie poleceń w łańcuchy (stacking) oraz generowanie listy przydatnych komend na podstawie kontekstu biznesowego. Autorka podkreśla, że choć konfiguracja (zwłaszcza MCP) zajmuje kilka godzin przy pierwszym podejściu, zwraca się w ciągu 1–2 tygodni dzięki oszczędności czasu.

## Frameworki i metody

- **Slash commands** — własne skróty zapisane jako pliki Markdown w [[Claude Code]]; uruchamiane przez wpisanie `/nazwa`; obsługują argumenty (np. `/UE 3days` dla ostatnich 3 dni) z wartościami domyślnymi
- **Cron jobs** — zadania uruchamiane automatycznie wg harmonogramu (np. co piątek o 9:00); konfigurowane przez [[Claude Code]] w tle, bez zajmowania ekranu; wymagają, by komputer był włączony lub by użyć dedykowanego serwera (np. VPS / Mac Mini)
- **Stacking commands** — łączenie poleceń w łańcuchy: jedno polecenie (np. `/daily-brief`) może automatycznie uruchamiać inne (np. `/client-prep` dla każdego klienta z kalendarza), przekazując argumenty dynamicznie
- **Context vault** — dokument opisujący działalność, projekty, narzędzia i kontekst właściciela; podany do [[Claude Code]] pozwala wygenerować spersonalizowaną listę przydatnych komend
- **Konfiguracja Google Workspace [[MCP]]** — integracja z Gmail / Google Calendar przez protokół [[MCP]]; wymaga ustawienia OAuth i przyznania uprawnień; wersja [[Anthropic]] zalecana ze względów bezpieczeństwa

## Kluczowe dane

- Szacowany czas konfiguracji od zera (pierwsza komenda + MCP): 2–3 godziny
- Szacowany zwrot z inwestycji czasu: 1–2 tygodnie
- Komenda `/UE` sprawdza e-maile za ostatnie 7 dni domyślnie; obsługuje argumenty: 3 days, 1 week, 1 month

## Wnioski

- Własne slash commands z [[MCP]] (Gmail, [[Slack]], [[Notion]]) pozwalają zautomatyzować powtarzalne zadania biurowe raz, a korzystać z nich wielokrotnie — szczególnie wartościowe dla osób pracujących z wieloma klientami lub projektami jednocześnie.
- Cron joby eliminują potrzebę pamiętania o regularnych zadaniach (przegląd e-maili, raporty cotygodniowe, podsumowania Slacka) — narzędzie pracuje w tle bez angażowania uwagi użytkownika.
- Stacking commands to jakościowy skok w automatyzacji: zamiast wielu niezależnych kroków, jeden wyzwalacz może uruchomić kompleksowy workflow łączący dane z Gmail, [[Slack]], [[Notion]] i sieci — co bezpośrednio przekłada się na modele automatyzacji z [[Make.com]] czy [[Langflow]].

## Cytat

> Jeśli używasz tego narzędzia tylko do wykonywania zadań, nie nauczysz się niczego — i prawdopodobnie wpadniesz w kłopoty z bezpieczeństwem. Pytaj w trakcie, nie tylko na końcu.

## Zastosowanie

Slash commands z cron jobami mogą obsłużyć powtarzalne zadania w pracy z NGO — przegląd korespondencji, przygotowanie do spotkań z klientami, tygodniowe podsumowania projektów. Konfiguracja `/client-prep` integrująca Gmail, [[Slack]] i [[Notion]] może być bezpośrednim wzorcem dla narzędzia wspierającego przygotowanie do konsultacji z organizacjami. Technika context vault + generowanie listy komend to gotowy format do prowadzenia warsztatu "jak zautomatyzować swoją pracę z AI" w ramach dobryai.pl.
