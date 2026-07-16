---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/email-tracking-pixels-now-require-consent-in-france-and-italy"
source: "[[Archives/2026-07-15 Email Tracking Pixels Now Require Consent in France and Italy — Your Action Plan|2026-07-15 Email Tracking Pixels Now Require Consent in France and Italy — Your Action Plan]]"
published: 2026-07-15
created: 2026-07-16
relevance: wysoka
tags:
  - "digital-campaigning"
  - "framing"
  - "narzędzia-AI"
---

# Email Tracking Pixels Now Require Consent in France and Italy — Your Action Plan

CNIL (Francja) i Garante (Włochy) uznały, że piksel śledzący w mailach prawnie działa jak cookie i wymaga zgody na podstawie art. 5(3) dyrektywy ePrivacy — a nie tylko zgody na wysyłkę maili. Francuski termin dla istniejących kontaktów minął 14 lipca 2026, włoski upływa 28 października 2026. Dotyczy każdego nadawcy wysyłającego maile do odbiorców we Francji lub Włoszech, niezależnie od siedziby organizacji czy używanej platformy. Autorka argumentuje, że open rate i tak od lat traci wiarygodność (Apple MPP, Gmail Gemini auto-open), więc regulacja tylko wymusza to, co i tak było już rozsądne: przejście na click rate, odpowiedzi i konwersje jako miary zaangażowania. Artykuł daje konkretny plan działania krok po kroku oraz status wsparcia w głównych platformach (HubSpot, Klaviyo, Mailchimp, Braze).

## Frameworki i metody

**6-krokowy plan wdrożenia zgodności:**

1. **Segmentacja kontaktów francuskich i włoskich** — po polach kraju w CRM oraz dopasowaniu domen dostawców (np. @orange.fr, @libero.it).
2. **Wyłączenie trackingu otwarć dla tego segmentu** — najprościej przez wersje maili bez piksela wysyłane osobno do tego segmentu.
3. **Audyt automatyzacji opartych na otwarciach** — re-engagement, lead scoring, alerty sprzedażowe — zbudowanie fallbacków opartych na kliknięciach, wizytach na stronie czy zakupach.
4. **Aktualizacja formularzy zapisu** — Francja wymaga osobnej, jawnej zgody na tracking (nie może być połączona ze zgodą na maile); Włochy dopuszczają zgodę łączoną, jeśli jest neutralna i jasno opisana.
5. **Dodanie osobnego mechanizmu rezygnacji z trackingu** w stopce maila — niezależnego od wypisania się z listy.
6. **Wysyłka maila z prośbą o zgodę bez aktywnego piksela** — otwarcie tego maila nie może być traktowane jako dowód zgody.

## Kluczowe dane
- Ok. 68% wysyłanych dziś maili zawiera przynajmniej jeden piksel śledzący, w większości bez zgody.
- Francuski termin (kontakty istniejące): 14 lipca 2026. Włoski termin: 28 października 2026.
- Google zapłacił 325 mln euro (wrzesień 2025) za praktyki reklamowe, przed którymi ostrzegał CNIL.

## Wnioski
- Zgoda na e-mail i zgoda na tracking to dwie różne zgody — traktowanie ich łącznie (typowe w Mailchimpie, HubSpocie, Klaviyo domyślnie) przestaje być wystarczające dla kontaktów francuskich i włoskich.
- To nie problem lokalny — ta sama logika prawna (dyrektywa ePrivacy, wytyczne EDPB z 2024) jest dostępna dla każdego regulatora w UE, więc warto budować infrastrukturę zgody od razu globalnie, a nie kraj po kraju.
- Regulacja przyspiesza zmianę, która i tak była potrzebna: przejście z open rate na click rate, odpowiedzi, wizyty na stronie i konwersje jako realne sygnały zaangażowania.

## Zastosowanie
Przydatne przy prowadzeniu kampanii mailowych dla organizacji z kontaktami w UE — warto sprawdzić, czy klienci NGO mają segmenty francuskie/włoskie na liście i czy ich ESP (Mailchimp, HubSpot) obsłużył już zgodność. Materiał nadaje się też jako punkt wyjścia do warsztatu o rzetelnych metrykach e-mail marketingu zamiast opierania się na open rate.
