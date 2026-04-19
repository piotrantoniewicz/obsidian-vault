---
categories: Clippings
authors: ["[[Roman Kozłowski]]"]
url: https://messageflow.com/pl/blog/przewodnik-dostarczalnosc-email/
source: "[[Archives/2024-07-25 Email deliverability guide|2024-07-25 Email deliverability guide]]"
published: 2024-07-25
created: 2026-04-18
relevance: wysoka
tags:
  - "fundraising"
  - "digital-campaigning"
  - "content-marketing"
---

# Email deliverability guide

Dostarczalność emaili to nie to samo co delivery rate — to realna zdolność wiadomości do trafienia do głównej skrzynki odbiorczej, a nie tylko do serwera. W 2026 roku o inbox placement decydują przede wszystkim: uwierzytelnianie (SPF/DKIM/DMARC), reputacja domeny i sygnały zaangażowania odbiorców, a nowoczesne filtry antyspamowe opierają się w dużej mierze na modelowaniu behawioralnym, nie analizie słów kluczowych. Przewodnik [[MessageFlow]] stanowi kompleksowy materiał operacyjny wyjaśniający zarówno mechanizmy filtrowania, jak i konkretne praktyki utrzymania stabilnego inbox placement — w tym segmentację według dostawców skrzynek i specyfikę europejskich, w tym polskich, providerów.

## Frameworki i metody

- **7-krokowy proces poprawy deliverability** — (1) audyt SPF/DKIM/DMARC z alignment → (2) analiza skarg i bounce'ów per provider → (3) czyszczenie i wyciszanie nieaktywnych → (4) segmentacja według zaangażowania → (5) ujednolicenie częstotliwości → (6) stopniowy warm-up nowych domen → (7) rozdzielenie strumieni marketingowych i transakcyjnych
- **Segmentacja per mailbox provider** — monitorowanie inbox placement oddzielnie dla Gmail, Outlook i regionalnych providerów (Onet, Wirtualna Polska, Orange) jako osobna metryka, nie zagregowany wynik globalny
- **Checklista operacyjna (10 punktów)** — uwierzytelnianie z alignment, one-click unsubscribe, skargi na spam <0,1%, hard bounce <2%, brak kupowanych list, stopniowy warm-up, segmentacja zaangażowania, wyciszanie nieaktywnych, stała częstotliwość, monitoring per provider

## Kluczowe dane

- Zdrowy program email: delivery rate 98–99%, inbox placement 95%+, skargi na spam <0,1%, hard bounce <2%
- Gmail i Yahoo od 2024 roku egzekwują obowiązkowo SPF, DKIM, DMARC i one-click unsubscribe dla nadawców masowych
- Reputacja domeny buduje się wolno — traci szybko; i jest dziś często ważniejsza niż reputacja IP

## Wnioski

- Wysoki delivery rate nie oznacza wysokiej dostarczalności — organizacje mogą mieć 99% delivery rate i jednocześnie trafiać do spamu, jeśli reputacja domeny lub zaangażowanie są słabe
- Polska specyfika: Onet, Wirtualna Polska i Orange mają własne systemy filtrowania odmienne od Gmail — kampanie do polskich darczyńców wymagają monitorowania inbox placement per provider, nie tylko globalnie
- Nieaktywni subskrybenci aktywnie szkodzą reputacji domeny — regularne wyciszanie to nie opcjonalna higiena, to konieczność strategiczna

## Cytat

> "Dostarczalność to nie jedna metryka — to długoterminowy efekt odpowiedzialnych praktyk wysyłkowych."

## Zastosowanie

Przewodnik jest bezpośrednio użyteczny jako materiał źródłowy do kursu mailowego dla organizacji społecznych — szczególnie do bloku o dostarczalności i technikach list hygiene. Polska specyfika emailowa (Onet, WP, Orange jako lokalni providerzy) czyni ten materiał bardziej relewantnym dla polskich NGO niż anglojęzyczne przewodniki skupione wyłącznie na Gmail. Checklista operacyjna może posłużyć jako framework audytu email dla organizacji klienckich przed wdrożeniem nowej kampanii fundraisingowej.
