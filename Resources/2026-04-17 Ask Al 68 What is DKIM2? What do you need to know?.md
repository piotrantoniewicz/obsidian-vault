---
categories: Clippings
authors: ["[[Al Iverson]]"]
url: https://www.youtube.com/watch?v=K7z_62tUXkQ
source: "[[Archives/2026-04-17 Ask Al 68 What is DKIM2? What do you need to know?|2026-04-17 Ask Al 68 What is DKIM2? What do you need to know?]]"
published: 2026-04-17
created: 2026-05-07
relevance: niska
tags:
  - "digital-campaigning"
---

# Ask Al 68: What is DKIM2? What do you need to know?

Odcinek podcastu wideo [[Al Iverson]] z [[Valimail]] wyjaśnia, czym jest DKIM2 — propozycja aktualizacji protokołu uwierzytelniania emaili [[DKIM]] (DomainKeys Identified Mail), który w niezmienionej formie działa od ponad 20 lat. Nowa wersja ma rozwiązać trzy problemy: replay attack (ponowne użycie legalnie podpisanej wiadomości przez złośliwy podmiot), backscatter (bouncy od wiadomości, których nigdy nie wysłałeś) oraz zrywanie uwierzytelnienia przy przekazywaniu wiadomości przez listy mailingowe i rewriting linków. DKIM2 jest nadal w fazie rozwoju przez grupę roboczą IETF. Dla nadawców korzystających z platform jak Amazon SES czy SendGrid — praktycznie żadnych działań nie będzie wymagać.

## Kluczowe dane
- DKIM w obecnej formie ma ponad 20 lat i jest powszechnie stosowany
- DKIM2 rozwiązuje 3 problemy: replay attacks, backscatter, zrywanie podpisów przy forwarding/rewriting
- Protokół jest nadal w fazie opracowywania przez grupę roboczą IETF — szczegóły mogą się zmienić

## Wnioski
- Dla organizacji korzystających z platform emailowych (ESP) wdrożenie DKIM2 będzie praktycznie transparentne — platformy obsłużą aktualizacje automatycznie
- Protokół DMARC pozostaje niezagrożony przez DKIM2 — jego raportowanie jest zbyt wartościowe, żeby z niego rezygnować
- Warto śledzić grupę roboczą IETF DKIM, jeśli zarządzasz własną infrastrukturą email lub pracujesz z organizacjami które ją posiadają

## Zastosowanie
Temat dotyczy niskopoziomowej technikaliów email authentication — w praktyce pracy z [[NGO]] nie wymaga bezpośrednich działań. Może być przydatny jako tło przy szkoleniach z dostarczalności, gdy pojawi się pytanie o przyszłość protokołów uwierzytelniania.
