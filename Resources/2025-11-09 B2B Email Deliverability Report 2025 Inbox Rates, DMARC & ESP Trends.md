---
categories: Clippings
authors: ["[[Vlad Kuryatnik]]"]
url: https://thedigitalbloom.com/learn/b2b-email-deliverability-benchmarks-2025/
source: "[[Archives/2025-11-09 B2B Email Deliverability Report 2025 Inbox Rates, DMARC & ESP Trends|2025-11-09 B2B Email Deliverability Report 2025 Inbox Rates, DMARC & ESP Trends]]"
published: 2025-11-09
created: 2026-04-18
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
  - "organizacje-społeczne"
---

# B2B Email Deliverability Report 2025: Inbox Rates, DMARC & ESP Trends

Raport z 2025 roku dokumentuje katastrofalny spadek dostarczalności emaili B2B — szczególnie na platformach Microsoft (Office365 spadł o 26,7 pp, Outlook/Hotmail o 22,6 pp rok do roku). Główne przyczyny to brak wdrożenia uwierzytelniania (tylko 7,6% domen egzekwuje DMARC), kary za wysyłki powyżej 1 mln/miesiąc oraz nieufność systemów filtrowania wobec nowych domen. Organizacje z pełnym zestawem SPF+DKIM+DMARC i dojrzałymi domenami osiągają 85–95% inbox placement — 2,7 razy lepiej niż senderzy bez uwierzytelniania. Raport zawiera kompletną listę kontrolną naprawy dostarczalności z szacowanym wpływem każdego kroku.

## Frameworki i metody

**Checklist naprawy dostarczalności emaili — priorytety według wpływu:**

1. **DMARC z p=quarantine lub p=reject** — nie wystarczy p=none (monitoring); egzekucja to +17,4 pp inbox placement
2. **DKIM signing** — klucze 2048-bit, rotacja co 3-6 miesięcy — +12,9 pp
3. **SPF skonfigurowany** — uwzględnij wszystkie IP wysyłające, limit 10 DNS lookup — +8,3 pp
4. **Domain aging** — rejestruj domeny 6-12 miesięcy przed ważną kampanią; nowe domeny (0-3 mies.) mają tylko 55% inbox placement vs 85% dla dojrzałych
5. **IP warmup** — stopniowe zwiększanie wolumenu przez 30-60 dni; faza 1 (dni 1-14): 60-65%, faza 4 (dni 46-60): 78-85%
6. **List hygiene** — weryfikuj listę przed każdą kampanią (robi to tylko 23,6% marketerów); usuń bounces i nieaktywnych po 6-12 miesiącach
7. **Monitoring** — Google Postmaster Tools (tygodniowo), Microsoft SNDS, raporty DMARC aggregate

**Segmentacja wolumenu:**
- 1-10k/miesiąc: stabilne ~50% inbox (brak kar)
- 200k-1M/miesiąc: najlepszy wynik ~61% (legalni senderzy z full auth)
- 1M+/miesiąc: tylko 27,6% inbox — konieczna rotacja domen

## Kluczowe dane

- Office365 inbox placement: 50,7% (↓26,7 pp YoY) — wysyłka do firm na Outlook to ryzyko
- Tylko 7,6% domen egzekwuje DMARC — 92,4% jest podatnych na agresywne filtrowanie
- Full auth (SPF+DKIM+DMARC): 83,75% inbox vs brak auth: 44,99% — różnica 38,76 pp
- Non-Profit bounce rate: 0,40% — dobry wynik branżowy (benchmark dla NGO)
- Europa: 91% inbox placement (GDPR = permission-based listy = wyższy engagement)

## Wnioski

- Brak wdrożonego DMARC (egzekwowanego, nie tylko monitorującego) to dziś największe ryzyko dla email campaigns NGO — kampanie fundraisingowe mogą trafiać do spamu większości odbiorców bez żadnego alertu.
- Wysyłki do odbiorców korporacyjnych na Microsoft (Office365, Outlook) wymagają szczególnej uwagi: inbox placement poniżej 51% oznacza, że połowa wiadomości nie dociera do celu.
- Budowanie list permission-based zgodnie z RODO (europejski standard) to przewaga strategiczna — Europa osiąga 91% inbox placement właśnie dlatego, że liste są z natury zaangażowane.

## Zastosowanie

Przed uruchomieniem kampanii emailowych dla klientów NGO warto przeprowadzić audyt infrastruktury: sprawdzić SPF, DKIM i DMARC — checklist z artykułu nadaje się bezpośrednio jako narzędzie diagnostyczne. Dane o bounce rate dla Non-Profit (0,40%) i sektora Politics (0,28%) to przydatne benchmarki do oceny jakości bazy darczyńców. W kursie "Fundraising z AI" temat dostarczalności powinien pojawić się jako element "higieny emailowej" — bez technicznej infrastruktury nawet najlepsza treść nie dotrze do odbiorcy.
