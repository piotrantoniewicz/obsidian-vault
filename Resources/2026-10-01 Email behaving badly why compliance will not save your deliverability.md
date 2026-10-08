---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/email-behaving-badly-why-compliance-will-not-save-your-deliverability?utm_medium=email&_hsenc=p2ANqtz-9CB7S7Ma4HLy3iMIkP1bSK8Qdtl-nWa-a3Yq-K4e2gKoyiIwV6JPIJKQfHFqVQMP8f3R32nz2uKwvxachDFGE9qMIWkET35dil0E_cwC2VpRCLmrY&_hsmi=147661112&utm_content=147658469&utm_source=hs_email"
source: "[[Archives/2026-10-01 Email behaving badly why compliance will not save your deliverability|2026-10-01 Email behaving badly why compliance will not save your deliverability]]"
published: 2026-10-01
created: 2026-10-08
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
---

# Email behaving badly why compliance will not save your deliverability

[[Beth O'Malley]] twierdzi, że w 2026 roku dostawcy skrzynek ([[Gmail]], [[Microsoft]]) przesunęli nacisk z technicznej zgodności (uwierzytelnianie, jednoklikowa rezygnacja, niski odsetek skarg) na zachowanie nadawcy. Skoro prawie wszyscy poważni nadawcy spełniają wymagania, zgodność przestała być sygnałem – jest jedynie „biletem wstępu", a o dostarczalności decyduje to, jak odbiorcy reagują na wysyłki. Dlatego program mailowy może przejść każdy audyt i mimo to tracić zasięg. Dla organizacji społecznych wniosek jest praktyczny: o dostarczalności decydują jakość listy, częstotliwość i wartość każdego maila, a nie konfiguracja.

## Frameworki i metody

**Podłoga zgodności (warunek konieczny):**
- [[SPF]], [[DKIM]] i [[DMARC]] w pełni dopasowane i na poziomie egzekwowania (DMARC p=none to tylko monitoring).
- Jednoklikowa rezygnacja (list-unsubscribe) w nagłówkach.
- Odsetek skarg poniżej 0,3% (to limit, nie cel; autorka dąży do poniżej 0,05%).
- Czysta obsługa odbić i wiarygodne dane (twarde odbicia usuwane na stałe).

**Zachowania zgodne z przepisami, które i tak niszczą dostarczalność:**
1. Wysyłka do osób, które wyraziły zgodę, ale już nie chcą maili.
2. Wysoka częstotliwość bez konsekwencji (treści, które nic nie wnoszą).
3. Wybudzanie uśpionej bazy tylko dlatego, że jest na liście.
4. Skoki wolumenu łamiące dotychczasowy wzorzec (np. z 2 000 do 10 000 adresów).
5. Formalnie istniejąca, ale ukryta rezygnacja.
6. Zgoda powiązana z pobraniem, zakupem, konkursem lub logowaniem do wifi.
7. Marketing udający maile transakcyjne.
8. Sztuczna pilność i mylące tematy („Re:" bez odpowiedzi, wiecznie przesuwany termin).
9. Zakup danych z deklaracją zgody.

**Jak dostawcy oceniają zachowanie:** zaangażowanie dodatnie i ujemne (otwarcia, kliknięcia, odpowiedzi vs. usunięcia bez otwarcia i skargi), klastry skarg, spójność wzorca (wolumen, rytm, skład odbiorców), historia na poziomie odbiorcy oraz zagregowana ocena całej listy.

**Test jednego pytania:** czy odbiorca byłby w porządku z tym mailem, gdyby dokładnie wiedział, dlaczego go dostaje i jak zdobyliśmy jego adres? Pytania pomocnicze: czy potrafisz powiedzieć to na głos odbiorcy, i czy rozsądna osoba byłaby *zadowolona* (nie tylko tolerowała) z maila dziś, w tej częstotliwości?

**7 zasad dobrego zachowania:**
1. Wysyłaj do osób, które chcą, i przestań wysyłać do tych, które nie chcą (wykluczenia na poziomie systemu).
2. Bądź spójny: wolumen, rytm i tożsamość nadawcy.
3. Regularnie wysyłaj coś, co ma znaczenie.
4. Spraw, by rezygnacja była oczywista i natychmiastowa.
5. Pozyskuj kontakty właściwie – sposób zapisu najlepiej przewiduje wyniki.
6. Rozdziel strumienie (transakcyjne, marketingowe, wychodzące).
7. Dotrzymuj obietnic z momentu zapisu (częstotliwość, tematy).

## Wnioski
- Audyt zgodności (SPF/DKIM/DMARC, rezygnacja, skargi) to dopiero próg wejścia; dostarczalność to „stan zdrowia" reputacji kształtowany zachowaniem w czasie, nie konfiguracja.
- Największa dźwignia dla większości programów to wykluczanie osób nieangażujących się i dbałość o to, by każdy mail miał znaczenie – szczególnie ważne przy kampaniach końca roku, gdy rośnie wolumen.
- Skok wolumenu przy kampanii (np. apel końca roku do całej bazy) wygląda z zewnątrz jak zakup listy; trzeba go planować stopniowo i kierować do aktywnej części bazy.

## Cytat
> Konfiguracją możesz wprowadzić się na boisko, ale nie możesz skonfigurować sobie zwycięstwa.

## Zastosowanie
Przydatne jako lista kontrolna w audytach mailingu organizacji społecznych i w kursie „Fundraising z AI" (moduł o dostarczalności i planowaniu wolumenu kampanii). Test „czy odbiorca byłby zadowolony" można wprost włączyć do szkoleń z digital campaigningu i do polityki wykluczeń w [[CRM]] klienta.
