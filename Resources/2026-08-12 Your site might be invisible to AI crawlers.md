---
categories:
  - "Emails"
published: 2026-08-12
created: 2026-08-12
labels:
  - "Matt Diggity"
relevance: średnia
tags:
  - "narzędzia-AI"
  - "content-marketing"
  - "trendy-AI"
---

# Your site might be invisible to AI crawlers

Newsletter techniczny o SEO ostrzega, że boty AI (GPTBot, ClaudeBot, PerplexityBot) mogą być domyślnie blokowane przez CMS-y, wtyczki bezpieczeństwa lub firewalle — bez wiedzy właściciela strony — co czyni treść niewidoczną dla asystentów AI, zanim w ogóle zostanie oceniona jej jakość. Autor przedstawia czteroetapowy audyt: sprawdzenie `robots.txt`, rozdzielenie strategii widoczności w AI od strategii Google, kontrolę ustawień CDN/firewalla oraz cykliczne powtarzanie audytu po aktualizacjach platformy. Treść ma wartość praktyczną dla każdego, kto zależy na tym, by jego content był cytowany przez narzędzia AI (tzw. GEO — Generative Engine Optimization), choć mail kończy się linkiem do płatnego audytu, co obniża jego neutralność.

## Frameworki i metody
- **Audyt widoczności AI (4 kroki)**:
  1. Audyt `robots.txt` pod kątem blokad specyficznych dla botów AI (`GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`) — sprawdzić, czy reguła nie pochodzi z domyślnej konfiguracji wtyczki
  2. Rozdzielić decyzję o treningu modeli od decyzji o cytowaniu w wyszukiwaniu — zablokowanie `Google-Extended` zatrzymuje trening przyszłych modeli Gemini, ale nie blokuje cytowań w AI Overviews (te korzystają z aktywnego indeksu)
  3. Sprawdzić ustawienia CDN i firewalla (np. [[Cloudflare]], Sucuri) pod kątem reguł blokujących user-agenty botów AI oraz wyzwań JavaScript/CAPTCHA, które uniemożliwiają botom renderowanie strony
  4. Powtarzać kontrolę cyklicznie (co kwartał) i po każdej większej aktualizacji platformy, porównując plik `robots.txt` z zapisanym punktem odniesienia

## Wnioski
- Plik `robots.txt` bywa modyfikowany bez wiedzy właściciela strony przez aktualizacje wtyczek CMS — warto traktować dostęp botów AI jako stały punkt kontrolny SEO, a nie jednorazową konfigurację
- Widoczność dla botów AI i widoczność dla [[Google]] to dwa osobne przełączniki decyzyjne — można świadomie zezwolić na cytowanie treści bez zgody na jej wykorzystanie do treningu modeli
- Same reguły w `robots.txt` to za mało — realne blokady mogą wynikać z ustawień firewalla (WAF) lub CDN, które nie są widoczne w standardowym audycie SEO

## Cytat
> Jeśli narzędzia AI nie widzą Twojej treści, nie mogą jej polecić — bez względu na to, jak dobra jest.

## Zastosowanie
Warto sprawdzić `robots.txt` i ustawienia firewalla na dobryai.pl oraz stronach klientów NGO, żeby upewnić się, że treści merytoryczne (poradniki, artykuły o fundraisingu) są dostępne dla botów AI i mogą być cytowane przez asystentów typu ChatGPT czy Claude. To praktyczny element strategii content marketingu i widoczności organizacji w wynikach generowanych przez AI.
