---
categories: Clippings
authors: ["[[Validity]]"]
url: https://www.validity.com/e-mail-marketing/sender-reputation/
source: "[[Archives/2021-08-06 Email Sender Reputation|2021-08-06 Email Sender Reputation]]"
published: 2021-08-06
created: 2026-04-18
relevance: wysoka
tags:
  - "fundraising"
  - "digital-campaigning"
  - "content-marketing"
---

# Email Sender Reputation

Reputacja nadawcy to kluczowy czynnik decydujący o tym, czy wiadomości email trafiają do skrzynki odbiorczej — działa jak scoring kredytowy, oceniając wiarygodność nadawcy w oczach dostawców skrzynek pocztowych (MBP). Każdy nadawca posiada indywidualny wynik reputacji, który MBP takie jak Gmail czy Microsoft wykorzystują jako pierwszą warstwę filtrowania. Reputacja opiera się na dwóch wymiarach: reputacji domeny (kto wysyła) i reputacji IP (skąd wysyła), a każdy MBP stosuje własny algorytm oceny. Artykuł omawia narzędzie Sender Score od [[Validity]] jako metodę pomiaru reputacji IP oraz konkretne działania naprawcze w zależności od uzyskanego wyniku.

## Frameworki i metody

- **Sender Score** — skala 0–100 oceniająca reputację IP nadawcy; poniżej 70 = wymaga poprawy, 70–80 = solidna podstawa, powyżej 80 = doskonała reputacja
- **Feedback Loops (FBL)** — mechanizm monitorowania skarg odbiorców; nadawcy powinni zarejestrować swoje IP/domeny we wszystkich dostępnych FBL
- **Subdomena dla strumieni wiadomości** — oddzielenie emaili transakcyjnych od marketingowych chroni reputację kluczowych komunikatów

## Kluczowe dane

- Hard bounce szkodzi reputacji bardziej niż soft bounce — twardy zwrot sugeruje nieistniejące adresy, co sygnalizuje złe praktyki budowania listy
- Spam traps wykrywają nadawców kupujących lub scrapujących listy adresów — trafienie w spam trap natychmiast obniża reputację
- Gmail i Microsoft stosują odrębne algorytmy oceny reputacji — dobry wynik u jednego nie gwarantuje dostarczalności u drugiego

## Wnioski

- Reputacja domeny i reputacja IP to dwa niezależne wymiary — dobry wynik w Gmail nie gwarantuje inbox placement w Outlook i odwrotnie
- Zaangażowanie odbiorców (odczyty, kliknięcia, odpowiedzi) jest aktywnym sygnałem reputacyjnym — niska interakcja bezpośrednio obniża inbox placement nawet przy technicznie poprawnej konfiguracji
- Higiena listy (double opt-in, usuwanie nieaktywnych, analiza bounce'ów) to podstawa utrzymania dobrej reputacji, a nie tylko opcjonalna praktyka

## Zastosowanie

W kampaniach emailowych dla organizacji NGO reputacja nadawcy decyduje o tym, czy apele fundraisingowe docierają do skrzynek darczyńców — warto wdrożyć monitorowanie Sender Score przed każdą większą kampanią. Przy kursach mailowych dla organizacji społecznych ten materiał stanowi solidną podstawę do bloku o dostarczalności i technikach list hygiene. Segment dotyczący subdomen jest praktycznie użyteczny przy rozdzielaniu wysyłek newslettera i apeli zbiórkowych w systemach CRM.
