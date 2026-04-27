---
categories:
  - Emails
published: '2026-04-27'
created: '2026-04-27'
labels:
  - Send It Right
relevance: średnia
tags:
  - digital-campaigning
  - content-marketing
  - fundraising
---
# Why Your Deliverability Rate is Wrong

Newsletter Lauren Meyer (Send It Right) obala powszechne przekonanie, że wysoki "deliverability rate" oznacza, że emaile trafiają do skrzynki odbiorczej. Problem polega na fundamentalnym rozróżnieniu: delivery rate (czy serwer przyjął wiadomość) to dane dokładne, natomiast deliverability rate (czy wiadomość trafiła do inboxu) to z definicji szacunek — dostawcy skrzynek pocztowych nie informują nadawców o tym, co dzieje się z emailem po jego akceptacji. Wiele platform podaje "deliverability rate" jako pewną metrykę, choć opiera się ona zaledwie na kilku danych wejściowych. Zamiast ufać jednej liczbie, autorka zaleca monitorowanie szerokiego zestawu sygnałów i traktowanie wskaźników reputacji kierunkowo, nie jako wyrocznię.

## Frameworki i metody

- **Delivery rate vs. Deliverability rate** — delivery rate mierzy, czy wiadomość została zaakceptowana lub odrzucona przez serwer odbiorcy (dokładny, bo mailbox providers dają feedback); deliverability rate próbuje oszacować placement w inboxie (niedokładny, bo mailbox providers nie ujawniają, dokąd trafiła wiadomość po akceptacji — inbox, spam, czy "podłoga")
- **Sender Score** (Validity) — narzędzie do oceny reputacji nadawcy na skali 0–100; wymaga podania IP lub domeny wysyłkowej; daje wgląd w kilka aspektów reputacji, ale nadal jest szacunkiem
- **StreamScore** (Socketlabs) — score uwzględniający 25 data points: delivery i engagement metrics, bounce responses, spam trap hits, seed testing, mailbox provider feedback (np. [[Google Postmaster Tools]]), [[DMARC]] i inne; mimo zaawansowania nadal pozostaje przybliżeniem
- **Wielowskaźnikowe monitorowanie reputacji** — zamiast jednej metryki, śledzenie kombinacji: delivery rate, bounce rate, open rate, CTR, unsubscribes, spam complaints, odpowiedzi, dane od mailbox providers — razem dają bardziej wiarygodny obraz kondycji wysyłki

## Wnioski

- Wskaźnik dostarczalności w dashboardach [[ESP]] jest z definicji niedokładny — mailbox providers nie udostępniają nadawcom danych o placemencie wiadomości, więc każda "deliverability rate" to szacunek oparty na niepełnych danych
- Narzędzia jak [[Sender Score]] czy StreamScore mogą pomóc w ocenie reputacji nadawcy, ale należy je traktować jako wskazówkę kierunkową — false positives i false negatives są nieuniknione, co może prowadzić do ignorowania realnych problemów lub paniki bez powodu
- W kampaniach [[digital-campaigning]] i [[fundraising]] przez email kluczowe jest budowanie zaangażowania subskrybentów (otwieralność, kliknięcia, brak skarg spam) — silna reputacja nadawcy to efekt uboczny dobrego contentu, nie odwrotnie

## Cytat

> "Utrzymuj zadowolenie subskrybentów, a twoja dostarczalność zadba o siebie sama."

## Zastosowanie

Przy prowadzeniu kampanii emailowych dla NGO — zarówno fundraisingowych, jak i advocacy — warto rozumieć różnicę między delivery rate (mierzalnym) a deliverability rate (szacunkowym), żeby nie wyciągać błędnych wniosków ze statystyk platformy. Wiedza ta jest bezpośrednio zastosowalna w kursie "Fundraising z AI" przy omawianiu metryk skuteczności email campaigns oraz w pracy z klientami NGO korzystającymi z narzędzi jak [[Impact Stack]] czy [[Engaging Networks]]. Zamiast polegać na jednej "deliverability rate", lepiej śledzić kombinację wskaźników i budować zdrową bazę przez dostarczanie wartościowego contentu.
