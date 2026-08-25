---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/the-state-of-email-deliverability-in-2026.-and-what-i-think-happens-in-2027?utm_medium=email&_hsenc=p2ANqtz--wIRfjPy3QZWbgllExeVevFfGxX9BVhRNtEQVbGUKDuUbyfwDeHzJRYONhEkzaxjCc7gWivNmx29LBnTvjd5YLOOGk9KrcWR-tc9QpsshNgO9IHq8&_hsmi=143645329&utm_content=143639175&utm_source=hs_email"
source: "[[Archives/2026-08-19 The state of email deliverability in 2026. And what I think happens in 2027|2026-08-19 The state of email deliverability in 2026. And what I think happens in 2027]]"
published: 2026-08-19
created: 2026-08-25
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
  - "trendy-AI"
---

# The state of email deliverability in 2026. And what I think happens in 2027.

Beth O'Malley (Astral) argumentuje, że ok. 15% każdej wysyłki mailowej ląduje w spamie i to jest nowy, niewidoczny w standardowym raportowaniu baseline 2026 roku — dostawcy poczty (Gmail, Microsoft) przestali tolerować niedbałą autentykację i masowe wysyłki bez zgody, więc praktyki uchodzące płazem jeszcze w 2022 dziś kończą się twardym odrzuceniem. Autorka twierdzi, że deliverability to nie ustawienie ani jednorazowy problem do naprawienia, lecz stan zależny od zachowania w czasie — a mimo to ponad 85% z ok. 3000 przebadanych marketerów przyznaje, że się na tym nie zna. Tekst opisuje też zjawisko „deliverability washing" (mylące metryki dostawców ESP prezentowane jako wskaźniki dostarczalności) oraz stawia siedem konkretnych prognoz na 2027 rok, w tym dalszy wzrost baseline'u spamu, spadek skuteczności maili pisanych bez udziału człowieka i powolną śmierć cold email w B2B.

## Frameworki i metody

**Plan działania na najbliższe 6 miesięcy (7 kroków):**

1. Zmierz, gdzie realnie lądują maile — placement liczony osobno od delivery, wg dostawcy, jako trend, nie pojedynczy odczyt.
2. Popraw autentykację i doprowadź DMARC do poziomu enforcement — polityka `p=none` to tylko monitoring, nie ochrona.
3. Rozdziel strumienie wysyłek — transakcyjne od promocyjnych, różne subdomeny dla różnych celów, żeby jeden zły miesiąc nie zepsuł potwierdzeń zamówień/wpłat.
4. Zajmij się grupą nieaktywnych odbiorców — brak reakcji (w mailu i poza nim) obniża reputację wysyłki dla wszystkich pozostałych.
5. Wróć z człowiekiem do treści — jeśli program komunikacji przeszedł na zautomatyzowane pisanie, spadek zaangażowania i tak nadejdzie.
6. Naucz się oceniać porady dostawców i agencji na tyle, by rozpoznać, co jest prawdą, a co „deliverability washingiem".
7. Buduj mniejszą, lepszą listę — szczególnie w B2B, gdzie pipeline oparty na wolumenie ma coraz krótszy „runway".

## Kluczowe dane
- Ok. 15% typowej wysyłki nie dociera do skrzynki odbiorczej — to nowy baseline 2026 (dane m.in. Validity).
- Ponad 85% z ok. 3000 przebadanych marketerów przyznaje, że nie zna się wystarczająco na deliverability.
- Prognoza autorki na 2027: baseline spamu wzrośnie do 17-21% wysyłek.

## Wnioski
- Tolerancja dostawców poczty się skończyła — dawne zaniedbania (słaba autentykacja, brak segmentacji, wysyłka do wszystkich) dziś kończą się mechanicznym odrzuceniem, nie cichym trafieniem do spamu.
- Spadek dostarczalności maili pisanych głównie przez AI nie wynika z wykrywania AI przez filtry, lecz z tego, że ludzie rozpoznają wzorce nudnego, zautomatyzowanego tekstu i przestają się angażować — a filtry reagują na spadek zaangażowania.
- Cold email (zwłaszcza w B2B) traci skuteczność strukturalnie, nie chwilowo — potrzebna jest mniejsza, bardziej zaangażowana lista zamiast dalszego skalowania wolumenu wysyłek.

## Cytat
> Deliverability to nie ustawienie, które konfigurujesz, ani wynik, który sprawdzasz — to stan, który zależy od twojego zachowania w czasie, a nie od tego, co zrobiłeś dziś rano.

## Zastosowanie

Bezpośrednio przydatne przy audytach dostarczalności dla klientów NGO i przy kursie mailowym „Fundraising z AI" — zwłaszcza ostrzeżenie przed automatyzowaniem treści maili bez udziału człowieka (spadek zaangażowania odbiorców) i 7-krokowy plan jako gotowa checklista audytowa. Dobry materiał do budowania świadomości klientów, że DMARC na `p=none` i wysyłka bez segmentacji to dziś realne ryzyko utraty kanału, nie tylko techniczny detal.
