---
categories:
  - Clippings
authors:
  - '[[Beth O''Malley]]'
url: >-
  https://weareastral.co.uk/thevault/what-is-bimi-how-to-get-it-what-it-costs-and-does-it-help-email-deliverability
source: >-
  [[Archives/2026-07-22 What is BIMI, How to Get It, What It Costs, and Does it
  Help Email Deliverability-|2026-07-22 What is BIMI, How to Get It, What It
  Costs, and Does it Help Email Deliverability-]]
published: '2026-07-22'
created: '2026-07-24'
relevance: średnia
tags:
  - digital-campaigning
  - fundraising
---
# What is BIMI, How to Get It, What It Costs, and Does it Help Email Deliverability?

Artykuł Beth O'Malley wyjaśnia czym jest BIMI (Brand Indicators for Message Identification) — standard pozwalający wyświetlić zweryfikowane logo marki obok nadawcy w skrzynce odbiorczej, wymagający wcześniej wdrożonego DMARC na poziomie egzekwowania (p=quarantine lub p=reject) oraz działających SPF i DKIM. Autorka rozróżnia dwa typy certyfikatów: VMC (wymaga zarejestrowanego znaku towarowego, wyświetla niebieski znacznik w Gmail) i CMC (bez znaku towarowego, tańszy, ale bez wsparcia Apple Mail). Kluczowy wniosek: BIMI nie poprawia bezpośrednio deliverability — to efekt uboczny uporządkowania autentykacji, a cytowane dane o wzroście open rate (np. 38%) pochodzą z niekontrolowanych, jednostkowych wdrożeń i wymagają sceptycyzmu. Najsilniejszym, najbardziej jednoznacznym argumentem za BIMI jest ochrona przed phishingiem, nie marketing.

## Frameworki i metody

**6 kroków wdrożenia BIMI:**
1. Uporządkuj autentykację — DMARC na poziomie egzekwowania, działające SPF i DKIM na wszystkich domenach i platformach wysyłkowych.
2. Zdecyduj VMC czy CMC — zależnie od posiadania zarejestrowanego znaku towarowego.
3. Przygotuj logo w formacie SVG Tiny 1.2 Portable/Secure (PNG nie działa).
4. Kup certyfikat u autoryzowanego Certificate Authority (np. [[DigiCert]], [[GlobalSign]]).
5. Opublikuj rekord DNS BIMI wskazujący na plik logo i certyfikat.
6. Przetestuj wyświetlanie w Gmail, Yahoo i Apple Mail i monitoruj.

**Kiedy BIMI ma sens, a kiedy może poczekać:** ma sens przy DMARC już na poziomie egzekwowania, zarejestrowanym znaku towarowym i solidnych fundamentach programu e-mail; może poczekać, jeśli autentykacja nie jest jeszcze na poziomie egzekwowania lub lista i deliverability wymagają pracy w pierwszej kolejności.

## Kluczowe dane
- VMC: ok. £1 100–1 400 rocznie
- CMC: ok. £770–990 rocznie
- Zarządzane wdrożenie BIMI+DMARC (np. Red Sift OnDMARC): od ok. £200/miesiąc

## Wnioski
- BIMI wymaga [[DMARC]] na poziomie egzekwowania jako warunku wstępnego — bez uporządkowanej autentykacji nie ma sensu w ogóle o nim myśleć.
- Deklarowane wzrosty engagement po wdrożeniu BIMI są mylące, bo współwystępują z porządkowaniem autentykacji i reputacji domeny, więc trudno je przypisać samemu logo.
- Najmocniejszy, najmniej dyskusyjny argument za BIMI to ochrona marki przed phishingiem — istotne dla organizacji z dużą bazą darczyńców i wysokim zaufaniem odbiorców.

## Cytat
> Wdrażanie BIMI, gdy deliverability kuleje, lista jest niezaangażowana, a autentykacja niekompletna, jest jak malowanie elewacji domu, który ma problemy konstrukcyjne.

## Zastosowanie
Przydatne jako punkt odniesienia, gdy klient pyta o BIMI: najpierw sprawdzić, czy DMARC jest na poziomie egzekwowania, zanim rozważy się koszt certyfikatu. Materiał do checklisty audytu deliverability przed rekomendacją inwestycji w BIMI dla organizacji z rozpoznawalną marką i dużym wolumenem wysyłki.
