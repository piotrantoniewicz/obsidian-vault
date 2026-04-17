---
categories:
  - Emails
published: 2026-02-13
created: 2026-03-18
labels:
  - Robert Szewczyk
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - prompt-engineering
---

# 🤖 3 komendy, które robią research za mnie

Autor pokazuje trzy własne komendy Claude Code zbudowane na bazie open-source'owego scrapera [[Crawl4AI]], podłączonego przez serwer MCP do agenta. Komendy `/blog-scan`, `/trend-scan` i `/competitor-scan` wykonują w ciągu kilku minut research, który wcześniej zajmował godziny. Całość działa na własnym VPS bez dodatkowych kosztów. Dane MIT/Forbes przypominają, że tylko firmy skupione na 3–4 konkretnych zastosowaniach AI widzą realny zwrot.

## Wnioski

- Komenda `/blog-scan [temat]` skanuje 6 blogów i generuje 5 pomysłów na wpisy w ~2 minuty, łącząc [[Crawl4AI]] z [[Claude Code]] przez protokół [[MCP]] — zero kosztów ponad istniejący serwer.
- Według danych MIT i Forbes 56% firm nie widzi zwrotu z [[AI]], a mniej niż 1% osiąga ponad 20% zwrotu; wygrywa ten, kto wybiera 3–4 konkretne zastosowania zamiast eksperymentować wszędzie.
- Funkcja [[Agent Teams]] w [[Claude Code]] (eksperymentalna) pozwala sub-agentom dzielić wspólną listę zadań i wzajemnie kwestionować swoje wnioski, co zbliża pracę AI do prawdziwej weryfikacji.

## Cytat

> „Crawl4AI to open-source'owy scraper, który możesz hostować na własnym VPS i podłączyć jako serwer MCP do Claude Code — koszt dodatkowy: 0 zł."

## Zastosowanie

Wdrożyć `/competitor-scan` na stronach konkurencji przed przygotowaniem oferty lub nowej usługi, żeby w kilka minut zebrać FAQ, ceny i recenzje bez ręcznego przeglądania stron.
