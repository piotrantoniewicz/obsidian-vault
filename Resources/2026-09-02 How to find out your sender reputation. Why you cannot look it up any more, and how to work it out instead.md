---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/how-to-know-your-sender-reputation.-why-you-cannot-look-it-up-any-more-and-how-to-work-it-out-instead?utm_medium=email&_hsenc=p2ANqtz-9xWT80QQ3JBJozT73QxNkFY8opjPRIhrH9NdZFNZ2cXu9LnyNc_6v1H52AmJsTI9kYoK0MFnXG5B6D_6WEPYMvDU6gZk7AcjpnZXmXpwdNGgIQYwQ&_hsmi=144797544&utm_content=144791947&utm_source=hs_email"
source: "[[Archives/2026-09-02 How to find out your sender reputation. Why you cannot look it up any more, and how to work it out instead|2026-09-02 How to find out your sender reputation. Why you cannot look it up any more, and how to work it out instead]]"
published: 2026-09-02
created: 2026-09-03
relevance: wysoka
tags:
  - "digital-campaigning"
  - "fundraising"
---

# How to find out your sender reputation. Why you cannot look it up any more, and how to work it out instead.

Beth O'Malley wyjaśnia, że nie istnieje jeden globalny wskaźnik reputacji nadawcy — nawet przybliżony dashboard Google Postmaster Tools został wycofany, więc reputację trzeba wywnioskować z wielu sygnałów naraz. Reputacja to w istocie dwie osobne oceny (domeny i IP), budowane niezależnie przez każdego dostawcę skrzynek na podstawie trzech czynników: sposobu wysyłki, odbiorców i ich reakcji. Autorka proponuje metodę opartą na śledzeniu wskaźników umieszczenia w skrzynce (IPR/SPR/OPR) przez co najmniej 30 dni oraz na rozróżnieniu reputacji „reaktywnej" (chwilowe wahania, które same wracają do normy) od „skonsolidowanej" (trwała degradacja wymagająca realnej interwencji). Tekst jest ważny, bo — jak pisze autorka na podstawie własnych badań wśród ponad pięciu tysięcy specjalistów — deliverability to najsłabiej rozumiany obszar w branży e-mail marketingu.

## Frameworki i metody

**Sześć kroków audytu reputacji nadawcy:**

1. Analiza sytuacyjna — skąd pochodzi lista, kto ją wysyła, skąd biorą się sygnały negatywne.
2. Kontrole techniczne — weryfikacja [[SPF]], [[DKIM]] i [[DMARC]] oraz sprawdzenie blacklist.
3. Reputacja i infrastruktura — budowanie hipotezy reputacji per dostawca, mapowanie domen i systemów wysyłkowych.
4. Higiena danych i wysyłki — jakość bazy, walidacja list, odbicia, skargi, źródła pozyskania, ryzyko spam-trapów.
5. Testowanie umieszczenia w skrzynce — 30-dniowy test z wieloma narzędziami i rotującymi seedami, dający IPR, SPR i OPR per dostawca oraz trend.
6. Interpretacja i plan działania — wybór jednego z trzech trybów: ochrona i monitoring (zdrowy nadawca), transformacja i optymalizacja (na granicy), lub odbudowa (poważny problem).

**Sygnały a zdarzenia:** pojedynczy sygnał negatywny (jedno odbicie, jedna skarga) jest niemal nieszkodliwy — dopiero skupienie wielu negatywnych sygnałów w krótkim czasie („zdarzenie negatywne") realnie szkodzi reputacji. Ta sama logika działa w drugą stronę dla sygnałów pozytywnych.

## Kluczowe dane

- Spam Placement Rate: 0–15% to norma, 15–25% wymaga obserwacji, 26–50% to realny wpływ na zasięg, powyżej 50% to sytuacja poważna.
- Brak wysyłki przez ok. 4 tygodnie powoduje, że Gmail zaczyna „zapominać" nadawcę — zbyt rzadka wysyłka szkodzi reputacji tak samo jak zbyt częsta.
- Według badań autorki wśród ponad 5000 specjalistów na świecie, deliverability to największa luka kompetencyjna w zawodzie.

## Wnioski
- Nie ma jednego wskaźnika reputacji nadawcy — trzeba budować hipotezę z wielu sygnałów osobno dla każdego dostawcy skrzynek ([[Gmail]], [[Microsoft]], [[Yahoo]]).
- Rozróżnienie reputacji reaktywnej od skonsolidowanej decyduje o tym, czy wystarczy korekta, czy potrzebna jest pełna transformacja programu mailowego.
- Jednorazowy test placementu wprowadza w błąd — wiarygodny obraz daje dopiero trend z minimum 30 dni i wielu narzędzi.

## Cytat
> Deliverability to numer jeden luka kompetencyjna w naszym zawodzie — nie dlatego, że to trudne, ale dlatego, że nikt nigdy nie wyjaśnił, że liczba, której ludzie szukają, nigdy nie miała powstać.

## Zastosowanie
Przy audytach programów mailingowych klientów NGO warto wdrożyć 30-dniowy test placementu zamiast jednorazowych sprawdzeń i rozróżniać spadek wynikający z pojedynczej kampanii od trwałej degradacji reputacji. Przydatne jako materiał referencyjny przy diagnozowaniu problemów z dostarczalnością w kampaniach fundraisingowych i digital campaigning.
