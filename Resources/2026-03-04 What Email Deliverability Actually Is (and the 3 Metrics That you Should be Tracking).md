---
categories: Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/what-email-deliverability-actually-is-and-the-3-metrics-that-really-matter"
source: "[[Archives/2026-03-04 What Email Deliverability Actually Is (and the 3 Metrics That you Should be Tracking)|2026-03-04 What Email Deliverability Actually Is (and the 3 Metrics That you Should be Tracking)]]"
published: 2026-03-04
created: 2026-06-10
relevance: wysoka
tags:
  - digital-campaigning
  - fundraising
---

# What Email Deliverability Actually Is (and the 3 Metrics That you Should be Tracking)

Artykuł obala powszechne błędne przekonanie, że wysoki wskaźnik „delivered" w panelu ESP oznacza dobrą dostarczalność — delivery i deliverability to dwie różne rzeczy. Dostarczalność (deliverability) to reputacja domeny nadawcy budowana przez wzorce zachowań i oceniana niezależnie przez Gmail, Microsoft i Yahoo — żaden z nich nie ujawnia pełnych kryteriów oceny. Autorka przedstawia 3 metryki, które faktycznie mówią o tym, czy maile trafiają do skrzynki odbiorczej, a nie do spamu, i argumentuje, że optymalizowanie tematów maili jest bezcelowe, jeśli wiadomości lądują w spamie. Szczególnie ważne w środowiskach B2B, gdzie korporacyjne filtry mogą quarantainować wiadomości zanim dotrą do odbiorcy — a ESP i tak wykaże „Delivered".

## Frameworki i metody

- **3 kluczowe metryki dostarczalności:**
  - *Inbox Placement Rate (IPR %)* — odsetek maili trafiających do skrzynki głównej; jedyna metryka pokazująca rzeczywistą widoczność; wymaga zewnętrznych narzędzi (seed testing), niedostępna w panelu ESP
  - *Spam Placement Rate (SPR %)* — odsetek maili trafiających do spamu; rośnie odwrotnie do IPR; open rate jest zawodny jako zastępnik (szczególnie w B2B przez image blocking i privacy features)
  - *Spam Complaint Count (SCC #)* — ważna jest liczba bezwzględna i wzorzec czasowy (velocity), nie sam procent; klastry skarg z konkretnej kampanii lub dostawcy to silniejszy sygnał niż statyczny próg 0,1%

- **Czynniki wpływające na reputację nadawcy:** uwierzytelnianie (SPF, DKIM, DMARC), historyczna reputacja domeny, sygnały zaangażowania per odbiorca, skargi na spam, spójność wolumenu, jakość danych (bounces, spam traps), analiza treści i linków, zmiany infrastruktury

## Kluczowe dane

- Gmail może początkowo testować nowych nadawców w spamie zanim przeniesie ich do skrzynki głównej po poprawie sygnałów zaangażowania
- W środowiskach B2B jeden pracownik oznaczający mail jako spam może wpłynąć na filtrowanie na poziomie całej organizacji
- Dane o skargach wewnątrz ESP są często niepełne (szczególnie dla Gmail) — rzeczywisty zasięg skarg bywa niedoszacowany

## Wnioski

- Panel ESP pokazuje wyłącznie czy serwer przyjął wiadomość — nie mówi nic o tym, czy trafiła do skrzynki odbiorczej
- Dostarczalność jest oparta na wzorcach, nie na sztywnych regułach procentowych — wzrost skarg w krótkim czasie liczy się bardziej niż stabilny niski procent
- Bez monitorowania IPR, SPR i SCC można optymalizować kampanie wewnątrz systemu, który już filtruje wiadomości do spamu

## Cytat

> Możesz ulepszać tematy wiadomości przez cały dzień, ale jeśli lądują w spamie — to nie ma znaczenia.

## Zastosowanie

Dla kampanii fundraisingowych i digital campaigningu prowadzonych emailem — wiedza o dostarczalności jest fundamentalna: niska IPR może wyjaśniać słabe wyniki kampanii, które wyglądają dobrze w panelu. Warto wdrożyć zewnętrzne narzędzia do seed testingu przed dużymi wysyłkami do bazy darczyńców. Koncepcja reputacji opartej na wzorcach (nie procentach) przekłada się na zasadę regularnych, angażujących wysyłek zamiast sporadycznych dużych kampanii.
