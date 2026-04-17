---
categories:
  - "Emails"
published: 2025-06-19
created: 2026-03-25
labels:
  - "ECF"
relevance: wysoka
tags:
  - "digital-campaigning"
  - "organizacje-społeczne"
  - "strategia-organizacji"
---

# Emails to MPs not getting through

Bogaty wątek ECF (18 wiadomości) zainicjowany przez Jamesa Blaira z Kinship, który odkrył, że masowe maile do posłów przez [[Engaging Networks]] nagle przestały docierać — potwierdzał to brak standardowych automatycznych odpowiedzi. Diagnoza okazała się systemowa: Parliamentary Digital Service (PDS) zmieniło konfigurację filtrów bezpieczeństwa i zaczęło kwarantannować zewnętrzne maile do skrzynek parliament.uk. Engaging Networks podjął bezpośredni kontakt z PDS i pracował nad rozwiązaniem technicznym, jednocześnie przygotowując plan awaryjny fizycznego wysyłania listów. Wątek wywołał szerszą dyskusję o strategii komunikacji z decydentami — z silnym przekazem, że masowe maile to zła taktyka.

## Frameworki i metody

- **Diagnostyka dostarczalności emaili** — gdy maile nie docierają: sprawdź ustawienia DMARC (p=none nie zapewnia egzekwowania), DKIM (czy podpisywanie włączone w portalu admina) i SPF. Zbadaj jakość domeny narzędziami Google Workspace / Microsoft 365. Obecność tracking pixela może powodować kwarantannę.
- **Broadcast vs. Email-to-Target** — dwa różne mechanizmy w [[Engaging Networks]]: broadcast (masowy mailing z konta organizacji do posłów) vs. email-to-target (akcja, gdzie to wspierający wysyłają maile z własnych adresów). Mają inną techniczną specyfikę i inne podatności.
- **Multi-channel fallback** — gdy email jest zablokowany, plan awaryjny to: (a) fizyczne listy do parlamentarzystów (EN oferowało druk i wysyłkę), (b) telefony do biur poselskich, (c) wizyty w biurach, (d) postcard/craftivism. [[PostBug]] (Duane Raymond / FairSay) jako narzędzie do wysyłki fizycznych wiadomości od wspierających do decydentów.
- **Strategia personalizowana vs. masowa** — Nancy Platts (była radca ministrów): skuteczniejsze niż masowe maile jest (a) wybór MPs na podstawie ich roli i zainteresowań, (b) spersonalizowany email z nawiązaniem do ich aktywności w parlamencie, (c) telefoniczny follow-up po kilku dniach. Podejście „najpierw o nich, potem o sprawie".
- **Weekly status report** — alternatywna forma komunikacji z MP: zamiast tysięcy pojedynczych maili — cotygodniowy raport z liczbą wiadomości i wybranymi cytatami od wspierających. Bardziej czytelne i angażujące dla zapracowanych posłów.

## Kluczowe dane

- Jeden MP w UK otrzymuje worki poczty i tysiące maili tygodniowo, dysponując nielicznym personelem
- Jedna petycja z platformy Care2 zebrała prawie 20 000 podpisów w 2 dni
- EN zebrało potwierdzenia dostarczenia auto-reply po technicznym obejściu w ciągu 24h od diagnozy

## Wnioski

- Zmiany po stronie filtrów bezpieczeństwa parlamentu lub instytucji docelowej mogą z dnia na dzień uniemożliwić dostarczanie maili — kampaniści muszą mieć zawsze gotowe alternatywne kanały komunikacji z decydentami, szczególnie w czasie wrażliwych politycznie kampanii.
- Masowe emaile do posłów są nieskuteczne nie tylko technicznie (ryzyko blokady), ale też strategicznie — spersonalizowane, ukierunkowane wiadomości dają znacząco lepsze wyniki niż kampanie broadcast; warto przenosić tę wiedzę do polskich NGO pracujących z posłami czy radnymi.
- [[Engaging Networks]] i [[Impact Stack]] mają różną infrastrukturę — w momencie kryzysu warto wiedzieć, który z dostawców ma aktywne relacje z PDS i potrafi szybko reagować na systemowe blokady.

## Cytat

> „Email zawsze będzie podatny na blokowanie lub utknięcie w algorytmach — każdy kampanista powinien mieć gotowe plany awaryjne: telefon, wizyta osobista, list, pocztówka." — Duane Raymond, [[FairSay]] / PostBug

## Zastosowanie

Dla Piotra doradzającego polskim NGO w kampaniach digital, temat dostarczalności emaili do instytucji publicznych (ministerstwa, urzędy, Sejm) jest bardzo realny — warto zbudować checklistę techniczną (DMARC/DKIM/SPF) i strategiczną (kanały zastępcze) jako standard przy projektowaniu kampanii. Filozofia Nancy Platts o spersonalizowanej komunikacji z politykami to dobry framework do zastosowania przy kampaniach rzeczniczych prowadzonych przez organizacje społeczne w Polsce.
