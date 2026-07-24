---
categories: Concept
tags:
  - digital-campaigning
  - fundraising
  - automatyzacja
created: 2026-06-14
updated: 2026-07-24
relevance: wysoka
sources:
  - "[[2024-07-25 Email deliverability guide]]"
  - "[[2026-03-04 What Email Deliverability Actually Is (and the 3 Metrics That you Should be Tracking)]]"
  - "[[2024-07-05 Why Your Email Needs Sunscreen]]"
  - "[[2026-04-21 Email Deliverability for Infrequent and Seasonal Senders How to Land in the Inbox When It Actually Matters]]"
  - "[[2024-11-13 How to Catch and Lower Email Deliverability Red Flags]]"
  - "[[2025-04-09 Boost Your Nonprofit s Email Reach A Beginner s Guide to SPF, DKIM, DMARC, and BIMI]]"
  - "[[2024-09-12 Why Your Emails Aren't Reaching The Inbox]]"
  - "[[2026-06-16 Send It Right - What to Do When You Have a Deliverability Issue]]"
  - "[[2026-06-18 Your email program is carrying more weight than ever]]"
  - "[[2026-03-14 Inbox Placement Rates Aren t What You Think]]"
  - "[[2026-02-24 Email Deliverability Trends 2026 Expert Insights and Predictions]]"
  - "[[2026-07-22 Not Sending Enough Email Is a Deliverability Problem Too]]"
  - "[[2026-07-22 What is BIMI, How to Get It, What It Costs, and Does it Help Email Deliverability-]]"
---

# Email deliverability (dostarczalność maili)

Email deliverability to realna zdolność wiadomości do trafienia **do głównej skrzynki odbiorczej**, a nie tylko na serwer odbiorcy. Trzeba ją ostro odróżnić od **delivery rate**: delivery (97–99%) oznacza tylko, że serwer przyjął maila — i jest liczbą mylącą, bo wiadomość może wylądować w spamie albo w karcie "Oferty" i wciąż figurować jako "Delivered" w panelu ESP. Deliverability to placement: inbox / promotions / spam. O tym placemencie decyduje **reputacja domeny nadawcy**, budowana z wzorców zachowań i oceniana **osobno i niejawnie** przez Gmail, Microsoft i Yahoo — żaden z nich nie ujawnia pełnych kryteriów, a nowoczesne filtry opierają się na modelowaniu behawioralnym, nie na analizie słów kluczowych. Dla organizacji emailowej oznacza to fundamentalną zmianę perspektywy: można optymalizować tematy maili przez cały dzień, ale jeśli lądują w spamie — to nie ma znaczenia.

---

## Kluczowe mechanizmy

**1. Trzy filary inbox placement: uwierzytelnianie, reputacja, zaangażowanie**
Od 2024 roku Gmail i Yahoo egzekwują obowiązkowo dla nadawców masowych: SPF, DKIM, DMARC oraz one-click unsubscribe; w 2025 dołączył Microsoft (Outlook) z analogicznymi wymaganiami. To dziś praktyczny standard, nie dobra praktyka. Na tym fundamencie reputacja nadawcy zależy od historii domeny, spójności wolumenu i — przede wszystkim — sygnałów zaangażowania per odbiorca.

**2. Uwierzytelnianie — techniczny warunek wstępny**
Trzy protokoły grają różne role: **SPF** (Sender Policy Framework) wskazuje, które IP mogą wysyłać w imieniu domeny; **DKIM** podpisuje wiadomość kryptograficznie, by odbiorca sprawdził, że treść nie została zmieniona; **DMARC** spina oba i mówi serwerowi, co robić z mailem, który nie przeszedł weryfikacji. DMARC wdraża się fazowo: `p=none` (monitorowanie, zbieranie raportów) → `p=quarantine` (do spamu) → `p=reject` (odrzucenie). Kluczowe: reputacja jest powiązana z **domeną, nie z IP** — zmiana ESP nie naprawi złych praktyk wysyłkowych. Rekordy wymagają też okresowej konserwacji, bo migracje IT czy nowe integracje potrafią je niezauważenie uszkodzić.

**3. Trzy metryki, które naprawdę coś mówią — ale rozróżnij sygnał bezpośredni od pochodnego**
Panel ESP pokazuje "delivered" — to za mało. Liczą się: **Inbox Placement Rate (IPR%)** — odsetek maili w skrzynce głównej, mierzalny tylko zewnętrznymi narzędziami (seed testing), niedostępny w ESP; **Spam Placement Rate (SPR%)** — rośnie odwrotnie do IPR (open rate jest tu zawodnym zamiennikiem, szczególnie w B2B przez image blocking); **Spam Complaint Count (SCC#)** — ważna jest liczba bezwzględna i *velocity* (nagły klaster skarg z jednej kampanii), nie sam statyczny próg. Paradoks: stałe 0,00% skarg to zły znak — maile lądują wprost w spamie, gdzie nikt nie klika "to spam". Część sygnałów reputacyjnych (skargi, bounce, reputacja domeny w oczach Gmaila) daje za darmo **[[Google Postmaster Tools]]** — minimalny obowiązkowy monitoring dla każdego nadawcy masowego.

Krytyczne dopowiedzenie (Meyer): IPR i SPR to **sygnały pochodne** ("prognoza pogody") — estymaty z seed-testów, nie odczyt rzeczywistości; adresy seed nie otwierają, nie klikają i nie zgłaszają spamu, więc estymata bywa fałszywie pozytywna lub negatywna, a Microsoft wręcz wrzuca część poczty do "czarnej dziury" bez sygnału. Wiarygodniejsze są **sygnały bezpośrednie** ("termometry"): bounce i kody odrzucenia, skargi przez feedback loops, reply/CTR/konwersje realnych odbiorców oraz darmowe dane reputacyjne z **[[Google Postmaster Tools]]** i **[[Microsoft SNDS]]**. Najmocniejsza tania diagnoza to **rozjazd open rate między dostawcami** (np. Gmail 32% vs Microsoft 4% przy tej samej kampanii = mail ląduje w spamie u Microsoftu) — czytelniejszy niż jakikolwiek seed-test. Zasada: żaden pojedynczy wskaźnik nie opowie całej historii — czytaj skargi, bounce, open-per-provider i reputację razem.

**4. Reputacja to infrastruktura roczna, nie przedwysyłkowy checklist**
Reputacji domeny nie da się zbudować w tydzień przed największą kampanią — buduje się przez cały rok. Sygnały pozytywne: otwarcia, kliknięcia, **odpowiedzi** (najsilniejszy), przeniesienie maila ze spamu do skrzynki. Negatywne: oznaczenie jako spam (najgroźniejsze), usuwanie bez otwierania, długotrwały brak zaangażowania. Stąd strategia dla **rzadkich/sezonowych nadawców** (NGO żyjące year-end appeals i GivingTuesday): (a) *inbox-first opt-in* — lead magnet dostarczany do skrzynki, nie na stronie, wymusza zaangażowany kontakt zaraz po zapisie; (b) *domain warming* uruchomiony min. 6 miesięcy przed szczytem; (c) wartościowy, niesprzedażowy content choćby raz w miesiącu, pod tym samym sender name. 20–100 zaangażowanych subskrybentów chroni reputację lepiej niż 5000 biernych kontaktów.

**5. Higiena listy i wczesne sygnały ostrzegawcze**
Nieaktywni subskrybenci aktywnie **szkodzą** reputacji — regularne wyciszanie to konieczność, nie opcja. Pięć czerwonych flag, które zaczynają się jako subtelne odchylenia, zanim staną się kryzysem: niskie delivery / wysokie bounce, spadające open rate, rosnące skargi spam, wzrost wypisów, niski CTR. Reakcja zaczyna się od diagnozy **per mailbox provider** (Gmail ≠ Microsoft ≠ Yahoo), nie od agregatu — bo problem z placementem u jednego dostawcy ginie w uśrednionym wyniku.

**6. Gdy problem już wystąpił — proces naprawczy**
Prewencja to jedno; gdy placement już spadł, Lauren Meyer proponuje trójstopniowy proces: (1) **zrozum skalę** — jak wykryto problem (spadek metryk, skargi odbiorców, alert ESP), czy dotyczy jednego providera czy wszystkich, czy to incydent izolowany; (2) **zdiagnozuj przyczynę** — ustal gdzie i kiedy się zaczął, przeanalizuj dane historyczne, sprawdź nagłówki i bounce'y (najlepiej z ESP/specjalistą); (3) **działaj** — napraw to, co w twojej mocy: autentykację, zbieranie listy, segmentację, treść. Większość przyczyn (niska jakość danych, źle zarządzana lista, ignorowane sygnały) leży po stronie nadawcy i jest w jego kontroli. Providerzy wybaczają jednorazowe błędy, ale długotrwałe zaniedbania wymagają **tygodni–miesięcy** naprawy. Budżet na naprawę argumentuj **w języku wpływu na wyniki finansowe**, nie technicznym — to działa na zarządy NGO.

**7. Trajektoria 2026 — skrzynka rankowana przez AI i kara za generyczny AI-content**
Prognoza 12 ekspertów (Bouncer, 2026) domyka kierunek: deliverability to **ciągła dyscyplina oparta na zaufaniu i zachowaniu**, nie jednorazowy setup. Trzy przesunięcia istotne operacyjnie: (a) **inbox rankowany przez AI** — o pozycji decydują trafność i czas, a tradycyjne metryki (open, CTR) tracą wartość jako sygnał jakości na rzecz głębszych wzorców (odpowiedzi, kliknięcia po przeczytaniu AI-streszczenia, długoterminowe zaangażowanie); (b) **„niewidzialny rozkład" listy** — baza starzeje się i eroduje reputację nawet przy zachowaniu wszystkich standardów technicznych i bez kupowania list, co czyni pruning i walidację obowiązkiem, nie opcją; (c) **kara za generyczny AI-messaging** — automatyzacja bez osądu produkuje treść generującą słabsze sygnały zaangażowania, więc *aktywnie szkodzi* reputacji. Wniosek dla NGO masowo wdrażających AI do pisania maili: generyczny output to nie tylko gorszy ton, ale realne ryzyko dostarczalności.

**8. Za rzadka wysyłka to też problem deliverability — deliverability jako balans, nie próg**
Kontrapunkt dla dominującego nurtu porad („wysyłaj mniej, czyść agresywniej", O'Malley): **brak wysyłki przechyla szalę tak samo jak nadmiar**. Gmail aktywnie proponuje nieaktywnym subskrybentom wypisanie się po ok. **30 dniach bez otwarć** (i usuwa nieaktywne konta osobiste po 2 latach), a nieregularny wzorzec wysyłki — długa cisza, potem nagły duży wolumen — przypomina filtrom zachowanie spamera. Stąd cztery reguły: (a) wysyłaj **konsekwentnie, nawet przy niskim wolumenie**; (b) **buduj flows** (welcome, lead nurture, post-donation) zanim staną się ratunkiem — automatyzacje wyzwalane działaniem odbiorcy generują silniejsze i wiarygodniejsze sygnały niż broadcasty; (c) **restart po przerwie traktuj jak warm-up** — zacznij od najbardziej zaangażowanych i buduj wolumen stopniowo; (d) mierz inbox placement ([[GlockApps]], [[Litmus]]), nie dashboard ESP. **Napięcie do rozstrzygnięcia:** mechanizm 5 i strona [[2026-06-29 Higiena listy|Higiena listy]] traktują wyciszanie nieaktywnych jako konieczność — O'Malley pokazuje drugą stronę: **wygaszanie oparte na samych otwarciach jest zawodne** (Apple MPP, integracja Gemini w Gmailu) i potrafi odciąć realnie zaangażowane kontakty. Rozstrzygnięcie kierunkowe: wygaszaj po *meaningful actions* (wpłaty, wizyty na stronie, kliknięcia), nie po open rate — narzędzia typu Klaviyo Deliverability Hub rekomendujące sunset po otwarciach mogą szkodzić.

**9. BIMI — efekt uboczny porządku, nie dźwignia deliverability**
BIMI (Brand Indicators for Message Identification) wyświetla zweryfikowane logo obok nadawcy w skrzynce; wymaga **DMARC na poziomie egzekwowania** (`p=quarantine` lub `p=reject`) plus działających SPF i DKIM, logo w formacie SVG Tiny 1.2 Portable/Secure (PNG nie zadziała), certyfikatu u autoryzowanego CA i rekordu DNS. Dwa typy certyfikatu: **VMC** (wymaga zarejestrowanego znaku towarowego, daje niebieski znacznik w Gmailu, ok. £1 100–1 400/rok) i **CMC** (bez znaku towarowego, taniej — ok. £770–990/rok — ale bez wsparcia Apple Mail). Kluczowe rozstrzygnięcie: **BIMI nie poprawia deliverability bezpośrednio**; cytowane wzrosty open rate (np. +38%) pochodzą z niekontrolowanych wdrożeń, w których jednocześnie porządkowano autentykację i reputację, więc efektu nie da się przypisać logo. Najsilniejszy, najmniej dyskusyjny argument to **ochrona marki przed phishingiem** — istotny dla organizacji z dużą bazą darczyńców. Reguła kolejności: BIMI ma sens dopiero po domknięciu autentykacji i higieny listy; wcześniej to „malowanie elewacji domu z problemami konstrukcyjnymi".

---

## Liczby-kotwice

- Zdrowy program: delivery 98–99%, **inbox placement 95%+**, skargi na spam <0,1%, hard bounce <2%
- Skargi spam: **>0,10%** = sygnał ostrzegawczy Google, **>0,30%** = poważny problem z placementem; cel stabilny ~0,03%
- Brak uwierzytelnienia potrafi zbić open rate z ~55% do ~5% (przykład Gmail); Yahoo szacuje, że ~95% przychodzącej poczty to spam/malware — autentykacja wyróżnia z reszty
- W B2B jeden pracownik klikający "spam" może wpłynąć na filtrowanie całej organizacji
- Od 2025 inbox placement to wynik **per-odbiorca, nie per-program**: ten sam mail trafia do skrzynki głównej u zaangażowanych i do spamu/promocji u niezaangażowanych (Gmail/Yahoo/Microsoft, engagement prediction)
- Przychody z e-maila NGO **+16% r/r w 2025** (M+R), ale wzrost w dużej mierze „awaryjny" — bez retencji darczyńcy jednorazowi odpadną; rosnąca liczba nadawców = agresywniejsze filtrowanie, więc higiena listy staje się czynnikiem różnicującym (CEP *State of Nonprofits 2026*)

---

## Powiązane pojęcia

- [[2026-06-13 Stewardship]] — "momenty pomiędzy" (kontakt bez prośby) to nie tylko taktyka relacyjna, ale i mechanizm deliverability: każda angażująca, niesprzedażowa wysyłka karmi reputację domeny.
- [[2026-06-12 Recurring giving]] — regularny, przewidywalny kontakt z darczyńcą cyklicznym to zarazem sygnał spójności wolumenu dla filtrów.
- [[2026-06-03 Tożsamość darczyńcy]] — zaangażowanie (odpowiedzi, kliknięcia) jako najsilniejszy sygnał reputacji łączy się z poczuciem przynależności: ludzie otwierają maile od nadawcy, z którym się utożsamiają.
- [[2026-06-29 Higiena listy]] — operacyjna warstwa pod deliverability: suppression-first, segmentacja zaangażowania, sunset, unsubscribe jako pokrętło i integralność danych na wejściu.
- [[2026-06-15 Newsletter jako kanał]] — deliverability to warstwa techniczna pod strategią newslettera: kanał własny (owned vs rented), billboard effect, rytm i wzrost bazy stoją na fundamencie dostarczalności.

---

## Zastosowanie w kontekście NGO

- **Audyt przed kampanią**: 10-punktowa checklista (autentykacja z alignment, one-click unsubscribe, skargi <0,1%, hard bounce <2%, brak kupowanych list, warm-up, segmentacja, wyciszanie nieaktywnych, stała częstotliwość, monitoring per provider) to gotowy framework przeglądu konta klienta przed nową kampanią fundraisingową.
- **Polska specyfika**: Onet, Wirtualna Polska i Orange mają własne systemy filtrowania, odmienne od Gmail — kampanie do polskich darczyńców wymagają monitorowania inbox placement *per provider*, nie tylko globalnie. To czyni anglojęzyczne przewodniki niepełnymi dla polskich NGO.
- **Year-end / GivingTuesday**: plan deliverability buduje się z 6-miesięcznym wyprzedzeniem — argument do rozmowy z organizacją, dlaczego warto emailować przez cały rok, nie tylko w grudniu.
- **Kurs "Fundraising z AI"**: deliverability jako moduł obok higieny listy i sekwencji onboardingowych; domain warming i walidacja list jako kroki do zautomatyzowania w workflow [[Make.com]].
- **Odpowiedź na pytanie klienta „czy warto w BIMI?"**: najpierw sprawdź, czy DMARC jest na poziomie egzekwowania i czy lista jest zaangażowana — jeśli nie, koszt certyfikatu (£770–1 400/rok) jest przedwczesny. Jeśli tak, sprzedawaj to jako ochronę przed phishingiem, nie jako wzrost open rate.
- **Argument „wysyłaj przez cały rok" wzmocniony**: organizacji, która maila tylko w grudniu, nie grozi tylko zimna reputacja — Gmail w międzyczasie sam zachęca jej subskrybentów do wypisania się. Restart po przerwie zaplanuj jako warm-up od najbardziej zaangażowanych.
- **DMARC `p=none`** to bezpieczny pierwszy krok dla organizacji, które nigdy nie uwierzytelniały poczty — zero ryzyka odrzucenia, pełna widoczność problemów.

---

## Otwarte pytania

- Jak praktycznie mierzyć IPR/SPR dla polskich providerów (Onet, WP, Orange), skoro większość narzędzi seed-testingowych celuje w Gmail/Outlook/Yahoo?
- Gdzie leży granica opłacalności *domain warming* dla małej organizacji — kiedy taniej i bezpieczniej jest zbudować zaangażowanie organicznie niż płacić za platformę symulującą zachowania?
- Jak AI zmieni filtrowanie po stronie odbiorcy (np. automatyczne kategoryzowanie i podsumowania w skrzynce) i co to znaczy dla "otwarcia" jako sygnału? Kierunek już widać (mechanizm 7): skrzynka rankowana przez AI degraduje open/CTR na rzecz trafności i interakcji po AI-streszczeniu — otwarte zostaje, jakie *zastępcze* sygnały zaangażowania staną się mierzalne dla nadawcy, skoro open rate się rozjeżdża, a IPR to tylko estymata.
