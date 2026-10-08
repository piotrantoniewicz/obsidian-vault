---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/how-to-build-an-email-early-warning-system-so-you-find-out-before-it-costs-you"
source: "[[Archives/2026-10-01 How to build an email deliverability early warning system|2026-10-01 How to build an email deliverability early warning system]]"
published: 2026-10-01
created: 2026-10-08
relevance: wysoka
tags:
  - "digital-campaigning"
---

# How to build an email deliverability early warning system

[[Beth O'Malley]] pokazuje, że problemy z dostarczalnością maili prawie nigdy nie pojawiają się nagle – narastają tygodniami, a sygnały są widoczne, tylko nikt ich nie obserwuje. Firmy patrzą na wskaźniki opóźnione (open rate, kliknięcia, przychód), które potwierdzają szkodę, zamiast na wyprzedzające (skargi na spam, bounce'y, odroczenia, uwierzytelnianie, umiejscowienie w skrzynkach). Proponuje tani system wczesnego ostrzegania: kilka liczb z progami zielony/bursztynowy/czerwony/stop, jeden arkusz i osoba, która 15 minut tygodniowo to sprawdza. Dla organizacji społecznych wysyłających apele i newslettery to praktyczna ochrona zasięgu bez kupowania narzędzi.

## Frameworki i metody

**Wskaźniki wyprzedzające (poruszają się pierwsze):** wskaźnik i liczba skarg na spam (per wysyłka i per provider), hard bounce'y i nagłe zmiany, soft bounce'y i odroczenia, odsetek przechodzących uwierzytelnień, umiejscowienie w skrzynkach per provider, zaangażowanie w pierwszym mailu u nowych subskrybentów.

**Wskaźniki opóźnione (potwierdzają):** open rate, click rate, przychód i konwersje.

**Progi:**
- Skargi na spam: <0,02% w porządku; 0,02–0,1% bursztynowy; 0,1–0,3% czerwony (wstrzymaj szerokie wysyłki); >0,3% stop.
- Hard bounce: liczy się stabilność; każdy nagły wzrost to bursztyn, utrzymujący się podwyższony poziom to czerwony.
- Umiejscowienie w spamie: do ok. 15% normalnie; 15–25% bursztyn; 26–50% czerwony; >50% stop.
- Uwierzytelnianie poniżej 100% to bursztyn od razu; wyrzucenia z listy porównuj tylko w obrębie tego samego typu maila.

**Budowa bez kupowania narzędzi:**
1. Skonfiguruj [[Google Postmaster Tools]] i zweryfikuj domenę.
2. Skonfiguruj Microsoft SNDS.
3. Co tydzień eksportuj te same metryki z ESP (w tym samym dniu).
4. Trzymaj je w jednym arkuszu z formatowaniem warunkowym.
5. Dodaj regularny pomiar umiejscowienia (seed testing).
6. Wskaż osobę odpowiedzialną i termin w kalendarzu.
7. Zrób punkt odniesienia (baseline) w zwykłym miesiącu, zanim coś się zepsuje.

**Plan reakcji:** bursztyn – zrozum (segment, wysyłka, provider, co się zmieniło w 2 tygodnie); czerwony – wstrzymaj szerokie wysyłki, zaostrz wykluczenia, zmniejsz wolumen, sprawdź uwierzytelnianie i blocklisty; stop – wstrzymaj wszystko poza transakcyjnymi, decyzja wyznaczonej osoby, spodziewaj się tygodni.

**Czego nie traktować jako alarmu:** pojedynczego punktu danych, sezonowości, szumu procentowego przy małych wolumenach, celowego czyszczenia listy, ruchu u jednego providera.

## Wnioski
- Progi autorki są ostrzejsze niż publikowane limity, bo limity to moment kary, a nie moment niepokoju – dobra zasada przy konfiguracji alertów dla list organizacji społecznych.
- Przy małych listach liczy się bezwzględna liczba skarg, nie procent – trzy niezadowolone osoby mogą przekroczyć próg.
- Darmowy zestaw (Postmaster Tools, SNDS, arkusz, 15 minut tygodniowo) wystarcza, by wychwycić większość problemów; kluczowe są baseline i wskazana odpowiedzialna osoba.

## Zastosowanie
Gotowa checklista do audytów dostarczalności u klientów oraz szablon arkusza monitoringu (progi zielony/bursztyn/czerwony/stop) do wdrożenia w organizacjach społecznych prowadzących e-mail fundraising. Można go włączyć do kursu „Fundraising z AI" jako moduł o utrzymaniu zasięgu listy.
