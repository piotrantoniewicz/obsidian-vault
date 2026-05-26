---
categories: Clippings
authors: ["[[Claire Vo]]"]
url: https://www.lennysnewsletter.com/p/openclaw-the-complete-guide-to-building
source: "[[Archives/2026-03-31 OpenClaw The complete guide to building, training, and living with your personal AI agent|2026-03-31 OpenClaw The complete guide to building, training, and living with your personal AI agent]]"
published: 2026-03-31
created: 2026-05-12
relevance: średnia
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "strategia-AI"
---

# OpenClaw The complete guide to building, training, and living with your personal AI agent

[[Claire Vo]] opisuje, jak zbudowała zespół 9 specjalistycznych agentów AI opartych na platformie [[OpenClaw]] — open-source'owym frameworku do osobistej automatyzacji, działającym lokalnie lub na VPS i komunikującym się przez Telegram, WhatsApp czy Slack. Kluczowy insight to specjalizacja: zamiast jednego agenta „do wszystkiego", lepiej tworzyć wąsko wyspecjalizowane boty z oddzielnymi narzędziami, harmonogramami cron i tożsamościami. Architektura OpenClaw opiera się na plikach Markdown (SOUL.md, AGENTS.md, TOOLS.md) definiujących granice, uprawnienia i pamięć każdego agenta. Cały setup można zintegrować z [[Obsidian]] jako wspólną bazą wiedzy dla człowieka i agenta. Koszty wahają się od ~100 USD/mies. (subskrypcja ChatGPT) do nawet 1000 USD/mies. przy bezpośrednich kosztach API.

## Frameworki i metody

- **Multi-agent setup** — zamiast jednego, rozbudowanego agenta lepiej tworzyć wąsko wyspecjalizowane boty: Polly (asystent osobisty), Finn (rodzina i logistyka), Max (marketing), Sam (sprzedaż), Holly (helpdesk), Sage (kursy), Howie (podcast), Kelly (developer), Q (edukacja dzieci)
- **Pliki tożsamości agenta** — każdy agent OpenClaw ma swój zestaw plików Markdown w workspace:
  - `AGENTS.md` — bazowe instrukcje i pamięć
  - `SOUL.md` — persona, ton głosu, granice działania
  - `IDENTITY.md` — nazwa, charakter, emoji
  - `TOOLS.md` — notatki o dostępnych narzędziach
  - `USER.md` — profil właściciela/managera agenta
- **Bezpieczeństwo** — zasada minimalnych uprawnień: zaczynaj od read-only tokenów, dopiero potem dawaj write access; SOUL.md jako guardrail przeciwko prompt injection; nie udostępniaj agenta w grupowych czatach publicznych

## Wnioski

- [[OpenClaw]] umożliwia budowanie trwałych, autonomicznych agentów z własnym harmonogramem i pamięcią — to jakościowo inny poziom automatyzacji niż jednorazowe prompty
- Obsidian jako wspólna przestrzeń pracy człowieka i agenta to konkretny, działający wzorzec — warto go zbadać w kontekście własnego vaultu
- Koszty osobistej automatyzacji AI mogą być porównywalne z częściowym etatem pracownika, ale wymagają czasu na konfigurację i utrzymanie

## Zastosowanie

Piotr mógłby wdrożyć agenta zarządzającego outreachem NGO — przeszukującego nowych kandydatów, uzupełniającego dane w Notion i wysyłającego pierwsze wiadomości według ustalonego playbooka. Integracja z [[Obsidian]] opisana w artykule bezpośrednio pasuje do obecnego setupu. OpenClaw jako rozszerzenie obecnych przepływów w [[Make.com]] i MCP warto rozważyć w kontekście kursów szkoleniowych z AI dla organizacji — to gotowy case study.
