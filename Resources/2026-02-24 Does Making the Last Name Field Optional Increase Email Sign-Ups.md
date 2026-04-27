---
categories: Clippings
authors: ["[[NextAfter]]"]
url: https://www.nextafter.com/experiments/does-making-the-last-name-field-optional-increase-email-sign-ups/
source: "[[Archives/2026-02-24 Does Making the Last Name Field Optional Increase Email Sign-Ups|2026-02-24 Does Making the Last Name Field Optional Increase Email Sign-Ups]]"
published: 2026-02-24
created: 2026-04-27
relevance: wysoka
tags:
  - "fundraising"
  - "digital-campaigning"
  - "organizacje-społeczne"
---

# Does Making the "Last Name" Field Optional Increase Email Sign-Ups?

[[NextAfter]] przeprowadziło test A/B dla Luther Seminary sprawdzając, czy uczynienie pola "Nazwisko" opcjonalnym zwiększy liczbę zapisów email przy pobieraniu bezpłatnych treści biblijnych. Hipoteza była intuicyjna: mniej wymaganych pól redukuje tarcie i zwiększa konwersje. Wynik okazał się niejednoznaczny — wariant z opcjonalnym nazwiskiem osiągnął 24% konwersji wobec 27.5% w grupie kontrolnej, przy zaledwie 77.2% pewności statystycznej (próg ważności: 95%). Eksperyment nie zebrał wystarczającej próby (wymagane 1 144 obserwacji), więc wyniki są statystycznie nieważne. Kluczowy wniosek: dla tej grupy odbiorców pole "Nazwisko" może nie stanowić istotnej bariery — ale decyzja o zmianie formularza wymaga powtórzenia testu na wyższym ruchu.

## Frameworki i metody

- **Test A/B (split URL test)** — dwa warianty formularza testowane równolegle na podobnych grupach odbiorców:
  - Kontrola: imię wymagane, nazwisko **wymagane**, email wymagany
  - Wariant: imię wymagane, nazwisko **opcjonalne**, email wymagany
- Metryki pierwszorzędne: współczynnik konwersji formularza (email acquisition)
- Metryki drugorzędne: transakcje jednorazowe, darowizny cykliczne, przychód — monitorowane, by sprawdzić czy zmiany na górze lejka nie psują wyników poniżej

## Kluczowe dane

- Kontrola: 27.5% konwersji (119 konwersji z 432 odwiedzin)
- Wariant: 24.0% konwersji (104 konwersje z 434 odwiedzin)
- Pewność statystyczna: 77.2% — wymagane minimum to 95%; wynik nieważny

## Wnioski

- Intuicja "mniej wymaganych pól = więcej konwersji" nie znalazła potwierdzenia dla odbiorców zainteresowanych treściami religijno-edukacyjnymi — dla tej grupy nazwisko może nie być barierą psychologiczną
- [[NextAfter]] stosuje rygorystyczny próg 95% pewności statystycznej — wyniki poniżej tego progu traktują jako "brak wniosku", a nie "brak efektu"; to dobre podejście do unikania fałszywych optymalizacji
- Testowanie formularzy na stronach z niskim ruchem wymaga albo agregacji wielu stron w jeden test, albo wydłużenia czasu zbierania danych — małe NGO powinny planować testy A/B z wyprzedzeniem

## Cytat

> Jedynym właściwym wnioskiem jest to, że ten test nie dostarczył statystycznie ważnego odkrycia i powinien być powtórzony, zanim zostanie wprowadzona trwała zmiana.

## Zastosowanie

W pracy z NGO wdrażającymi formularze do budowania baz emailowych warto prowadzić testy A/B zanim zmienia się strukturę formularzy — nawet pozornie oczywiste zmiany (mniej pól) mogą nie dawać efektu dla konkretnej grupy odbiorców. Małe organizacje powinny albo agregować ruch z wielu stron akwizycyjnych do jednego testu, albo wydłużać czas zbierania próby. Kurs "Fundraising z AI" może zawierać ten case jako ilustrację tego, jak testować formularze zapisu do newslettera lub petycji.
