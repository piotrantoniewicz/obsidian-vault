---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/how-to-prepare-for-black-friday-and-peak-season-the-deliverability-version?utm_medium=email&_hsenc=p2ANqtz--IRXlno-gK__FiXNa-ok090dyGuYZlg-h8KNHgUkueHXflJSSZtfmtbhu-L8qbbsRO58bCnfwI8JLj9Hw_yGNlGD676CbxEB-gowK0u3z7_muo3fA&_hsmi=143123921&utm_content=143130518&utm_source=hs_email"
source: "[[Archives/2026-08-12 How to prepare your email deliverability for Black Friday and peak season|2026-08-12 How to prepare your email deliverability for Black Friday and peak season]]"
published: 2026-08-12
created: 2026-08-13
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
---

# How to prepare your email deliverability for Black Friday and peak season

Beth O'Malley przekonuje, że skuteczność mailingu w sezonie Black Friday/Peak Season nie zależy od kreacji czy oferty, lecz od infrastruktury deliverability przygotowanej miesiące wcześniej — audytu autentykacji, reputacji nadawcy i segmentacji, zanim ruszy się z większym wolumenem wysyłek. Kluczowa teza: sezon szczytowy nie zawodzi w listopadzie, zawodzi w sierpniu — błędy popełnione na starcie sezonu ujawniają się dopiero w najważniejszym dla przychodów tygodniu. Autorka pokazuje, że skargi (complaints) rosną w sezonie szczytowym nieproporcjonalnie szybciej niż wolumen wysyłek, a wysyłka do całej bazy odbiorców jest najdroższym błędem, jaki można popełnić dla reputacji nadawcy. Tekst daje konkretny, 9-punktowy harmonogram odliczania (16 tygodni przed szczytem) oraz listę praktyk, które kiedyś były bezpieczne, a dziś aktywnie szkodzą deliverability.

## Frameworki i metody
- **Trzy rodzaje ryzyka w planowaniu peak season** — ryzyko dla deliverability (wolumen, skargi, reputacja nadawcy), ryzyko dla doświadczenia klienta (czy odbiorca czuje się obsłużony czy zasypany), ryzyko dla kolejnego kwartału (co dziedziczy się w styczniu po decyzjach z listopada).
- **Harmonogram odliczania do peak week** — 16 tygodni przed: audyt i baseline reputacji; 12–14 tygodni: autentykacja ([[SPF]]/[[DKIM]]/[[DMARC]]), rozdzielenie strumienia transakcyjnego od promocyjnego; 10–12 tygodni: suppresja nieaktywnych, testy wykluczeń, start warmupu nowej subdomeny; 8–10 tygodni: start rampy wolumenu od najbardziej zaangażowanych odbiorców; 6 tygodni: test wysyłki na pełnym wolumenie peak; 4 tygodnie: zamrożenie zmian infrastrukturalnych; 2 tygodnie: codzienny monitoring, potwierdzony „kill switch"; tydzień peak: tylko monitorowanie, żadnych zmian; tydzień po: nowi kupujący trafiają do osobnego flow orientacyjnego.
- **Audyt deliverability przed sezonem** — powinien obejmować: autentykację (SPF/DKIM/DMARC i status polityki DMARC), architekturę domen/subdomen (co dzieli reputację z czym), miejsce lądowania maili u poszczególnych dostawców (Gmail, Microsoft, Yahoo, Apple), wskaźniki skarg i odrzuceń w podziale na segmenty i źródła, kolizje automatyzacji z kampaniami kalendarzowymi oraz wielkość grupy odbiorców nieaktywnych.
- **Ramping (rozgrzewanie wolumenu)** — zwiększanie wysyłek stopniowo, nie skokowo, od września/października; obserwowanie skarg i odrzuceń na każdym etapie; kierowanie dodatkowego wolumenu najpierw do najbardziej zaangażowanych odbiorców; danie nowej subdomenie miesięcy, nie tygodni, na rozgrzanie.

## Kluczowe dane
- Wolumen skrzynek odbiorczych w okresie peak wzrósł ok. 93% (analiza Proton 2025), a wysyłki na Black Friday rosły ok. 30% rok do roku (Sinch)
- Blisko połowa kupujących oczekuje promocji już na miesiąc przed Black Friday (Sinch) — sezon rozciąga się z jednego weekendu na ok. 6 tygodni
- Ok. 3/4 spamu tematycznie związanego z Black Friday to czyste oszustwa, nie agresywny marketing (Bitdefender)

## Wnioski
- Deliverability trzeba traktować jako projekt zarządzania ryzykiem rozpoczynany kilkanaście tygodni przed szczytem sezonu, nie jako element kreacji kampanii dopinany na ostatnią chwilę — to bezpośrednio przekłada się na planowanie kampanii end-of-year giving w NGO.
- Wysyłka do całej, także nieaktywnej, bazy w szczycie sezonu szkodzi reputacji nadawcy bardziej niż przynosi korzyści — lepiej rozszerzać zasięg wcześniej i stopniowo, testując reakcję odbiorców.
- Rozdzielenie strumienia transakcyjnego (potwierdzenia, powiadomienia) od promocyjnego/fundraisingowego chroni najważniejszą komunikację operacyjną przed skutkami agresywnej kampanii sprzedażowej lub fundraisingowej.

## Cytat
> Sezon szczytowy nie zawodzi w listopadzie. Zawodzi w sierpniu, gdy wszyscy patrzą na kreację i spierają się o wysokość rabatu, a porażka staje się widoczna dopiero w jeden weekend, w którym widoczność liczy się najbardziej.

## Zastosowanie
Ramy z artykułu (audyt deliverability, ramping wolumenu, rozdzielenie strumieni, harmonogram odliczania) można wprost zaadaptować do planowania kampanii mailowych na koniec roku dla klientów NGO — zwłaszcza ostrzeżenie przed jednorazową wysyłką do całej, uśpionej bazy darczyńców. Dobry materiał do kursu mailowego „Fundraising z AI" jako case dotyczący technicznych podstaw skutecznego mailingu, niezależnie od treści kreacji.
