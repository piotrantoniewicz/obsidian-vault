---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/how-to-run-cold-email-without-destroying-your-domain.-and-what-to-build-before-the-window-closes?utm_medium=email&_hsenc=p2ANqtz-8tEQHjH0O0u-Q8RLH0-1bF6RqyphmGOlcghqGZgC8t4Nj0N80uhoPz7dvXfkCN0ZsUl2oYPRc8ggGbfxUPJscXE1d-OVtlTroYciAb9TgC538k_7w&_hsmi=144226179&utm_content=144165921&utm_source=hs_email"
source: "[[Archives/2026-08-25 How to run cold email without destroying your deliverability|2026-08-25 How to run cold email without destroying your deliverability]]"
published: 2026-08-25
created: 2026-08-28
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
---

# How to run cold email without destroying your deliverability

Artykuł [[Beth O'Malley]] argumentuje, że cold email jako kanał kończy się nie z powodów etycznych, lecz technicznych — infrastruktura pocztowa (Microsoft, Gmail) zaostrzyła wymagania autentykacji i przestała tolerować niski engagement charakterystyczny dla zimnych maili. Autorka pokazuje, jak "kwarantannować" ryzyko dla firm, które nadal muszą prowadzić outbound: osobna domena, pełna autentykacja SPF/DKIM/DMARC, powolne warm-upy, niskie stałe wolumeny i agresywna higiena danych. Kluczowa teza — reputacja domeny to "cały majątek" nadawcy: zła kampania cold email może zniszczyć zdolność wysyłki maili transakcyjnych i marketingowych z tej samej domeny. Tekst kończy się rekomendacją budowania mniejszej, wysokiej jakości audiencji przychodzącej (inbound) zamiast dalszego skalowania outboundu, bo okno na skuteczny cold email się zamyka.

## Frameworki i metody

- **9 zasad defensywnego setupu cold email** — (1) nigdy nie wysyłaj z domeny głównej, (2) trzymaj całkowicie osobno domenę/platformę/skrzynki, (3) pełna autentykacja SPF/DKIM/DMARC w trybie enforcement, (4) powolny warm-up przez realną wysyłkę, (5) unikaj automatycznych narzędzi do warm-upu, (6) niski i stały wolumen na skrzynkę, (7) nie buduj rotacji domen do omijania limitów, (8) zawsze dołącz działający opt-out, (9) monitoruj codziennie (Postmaster Tools, complaint rate, bounce rate, reply rate).
- **Zasady jakości danych** — weryfikuj listę tuż przed wysyłką, nie w momencie zakupu; re-weryfikuj dane starsze niż kilka tygodni; usuwaj adresy rolowe (info@, sales@, admin@); traktuj domeny catch-all jako ryzyko, nie jako sukces weryfikacji; permanentnie suspenduj twarde odbicia w całej organizacji.
- **Zasady operacyjne wysyłki** — małe wolumeny i wysoka trafność zamiast masowości, research zamiast merge fields, reply rate jako jedyna wiarygodna metryka, maksymalnie 2–3 kontakty w sekwencji, jeden ask na maila, agresywna i trwała supresja.
- **Przejście "outbound to inbound"** — publikowanie odpowiedzi na pytania, które faktycznie zadają klienci, budowanie treści dla kupujących "nie w rynku" i raportowanie na pipeline influenced zamiast liczby wysłanych maili.

## Kluczowe dane

- Prognoza autorki: cold email jako kanał "skończy się" do 2030 roku.
- Rekomendowana liczba kontaktów w sekwencji: maksymalnie 2–3 (zamiast typowych ośmiu).
- 50 dobrze zresearchowanych maili przebija skutecznością 5000 generowanych automatycznie.

## Wnioski

- Reputacja domeny stała się głównym sygnałem zaufania dla dostawców poczty (wyprzedzając reputację IP) — dlatego cold email nigdy nie powinien iść z domeny używanej do maili transakcyjnych i marketingowych.
- Największym zagrożeniem nie jest złe copy, lecz zła jakość danych (weryfikacja, domeny catch-all, adresy rolowe) — problem deliverability wygląda jak problem copywritingu, ale rzadko nim jest.
- Autorka rekomenduje traktować outbound jako rozwiązanie tymczasowe i równolegle budować inbound (treści odpowiadające na realne pytania kupujących, świadomy opt-in) — to zmiana strategiczna, nie tylko taktyczna poprawka deliverability.

## Cytat
> Zły kwartał cold email nie kosztuje cię kampanii. Kosztuje cię możliwość wysyłania maili do obecnych klientów.

## Zastosowanie
Bezpośrednio przydatne przy doradztwie klientom NGO w kwestii deliverability mailingów fundraisingowych — zasady autentykacji domeny (SPF/DKIM/DMARC), warm-up i higieny danych stosują się wprost do kampanii e-mailowych organizacji społecznych, nie tylko cold outboundu B2B. Dobry materiał źródłowy do modułu o deliverability w kursie mailowym "Fundraising z AI".
