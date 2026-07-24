---
categories: Concept
tags:
  - strategia-organizacji
  - strategia-AI
  - narzędzia-AI
created: 2026-07-07
updated: 2026-07-24
relevance: wysoka
sources:
  - "[[2026-06-16 Suwerenność na wynajem]]"
  - "[[2025-05-19 International Civil Society s Tech Stack is in Extreme Danger]]"
  - "[[2025-05-23 A worrying read!]]"
  - "[[2025-06-09 Sovereign AI is political branding—the reality is closer to digital colonialism]]"
  - "[[2026-06-10 Europejskie alternatywy dla amerykańskiego oprogramowania]]"
  - "[[2026-06-24 Oprogramowanie open source jako alternatywa. Czego nie wiecie o bezpłatnych narzędziach dla organizacji?]]"
  - "[[2026-06-23 Escola AI Weekly nr43]]"
  - "[[2025-03-19 Czy AI odbiera nam sprawczość Zachowaj kontrolę nad technologią]]"
  - "[[2025-04-21 We need dissident tech, now!]]"
  - "[[2025-05-15 Is your technology stack part of your theory of change]]"
  - "[[2026-07-24 Kimi K3 Redraws the Open Frontier, Muse Spark 1.1 Undercuts Competitors, Cloudflare Moves to Cut Off Crawlers]]"
  - "[[2026-07-23 The data center fight is going global]]"
  - "[[2026-07-21 Masowe zwolnienia przez AI już się zaczęły. -Wszyscy czytają Engelsa-]]"
---

# Suwerenność technologiczna (Technological Sovereignty)

**Suwerenność technologiczna** to zdolność organizacji (lub kraju) do kontrolowania własnej infrastruktury cyfrowej — narzędzi, danych, modeli AI i kanałów — tak, by żaden zewnętrzny podmiot nie mógł jednostronnie odebrać jej zdolności działania. Nie jest to stan zero-jedynkowy, lecz **suwak**: każda warstwa stosu (hosting, poczta, płatności, CRM, model AI) ma własny poziom zależności i własne ryzyko. Teza spinająca klaster pochodzi od Jemielniaka: **suwerenność, której się nie buduje, jest na wynajem — a każdy najem można wypowiedzieć w piątek po południu, bez ostrzeżenia**. Dla organizacji społecznych to nie abstrakcja geopolityczna, lecz ryzyko operacyjne: precedensy (odcięcie Międzynarodowego Trybunału Karnego od Microsoft 365, wyłączenie modelu Fable 5 decyzją eksportową USA) pokazują, że dostęp do infrastruktury stał się instrumentem polityki.

---

## Kluczowe mechanizmy

**1. „Suwerenność na wynajem" — dostęp jako przywilej, nie prawo**
Dwa precedensy z lat 2025–2026 zmieniły temat z teorii w plan ciągłości działania: (a) **Executive Order 14203** — sankcje na Międzynarodowy Trybunał Karny de facto odcięły mu Microsoft 365; firmy łamiące sankcje ryzykują kary do 20 lat więzienia za „material support", więc Microsoft nie miał wyboru, a amerykańskie organizacje przestały odpowiadać na maile MTK (efekt chłodzący); (b) **wyłączenie Fable 5** przez amerykańską kontrolę eksportową — model AI zniknął globalnie z dnia na dzień, nie przez awarię, lecz decyzję polityczną. Jemielniak osadza to w czterech analogiach: kryzys sueski (dźwignia finansowa zamiast wojska), sprawa PGP (kod jako „amunicja"), Minitel (pułapka zamkniętego narodowego systemu) i **Galileo — jedyny pozytywny wzorzec: Europa zamiast napisać regulację, zbudowała infrastrukturę**. Rządy traktują czołowe modele AI jak zasób strategiczny — „dostęp staje się przywilejem, nie prawem".

**2. Jurysdykcja bije geografię**
Lokalizacja serwera nie chroni: przez **CLOUD Act** serwer Microsoftu w Amsterdamie podlega prawu USA tak samo jak ten w Wirginii. Skala zależności: **AWS + Azure + Google Cloud = ~70% europejskiego rynku chmury; wszyscy europejscy dostawcy razem ~15%** — a na Wielkiej Trójce stoi większość platform sektora społecznego (e-mail, strony, VoIP). Osobna, pomijana luka to **infrastruktura płatnicza**: darowizny i składki płyną przez procesorów z USA (Stripe, PayPal) — odcięcie płatności zatrzymuje fundraising szybciej niż odcięcie poczty.

**3. Paradoks suwerennej AI — warstwy stosu (Benaich)**
„Suwerenna AI" na szczycie stosu to kosztowna iluzja: ZEA wydają $20 mld na Stargate — w całości na amerykańskich chipach; Mistral jest „europejskim przełomem" — wyprzedzanym przez chińskie modele open source. Realna kontrola wymaga wszystkich warstw: **chipy → dane treningowe → middleware → talenty**, nie tylko flagowego modelu. Wniosek dla strategii: celem nie jest „pobić Nvidię", lecz **mieć alternatywę wystarczająco dobrą** — dywersyfikacja, open source, lokalne kompetencje. Inaczej powstaje cyfrowy kolonializm: dostęp do technologii bez kontroli nad nią.

**4. Suwak, nie przełącznik — zarządzanie ryzykiem zamiast ideologii**
Tkaczyk: migracja to nie manifest, lecz redukcja pojedynczego punktu awarii — każde przesunięcie suwaka (mail w Szwajcarii, analityka z Wrocławia) zmniejsza ryzyko, nawet jeśli reklamy dalej idą przez platformy amerykańskie. Czterokrokowy plan: **(1) wyszukiwarka i przeglądarka** (5 minut, zero kosztów) → **(2) mail na własnej domenie** (~6 EUR/mies.; własna domena = przenośność) → **(3) pliki i dokumenty** (weekend; nowe projekty najpierw) → **(4) analityka, treści, AI** (miesiąc testów równolegle ze starym). Caraballo dodaje ubezpieczeniową ramę: organizacje ubezpieczają się od pożaru mimo niskiego prawdopodobieństwa — audyt i migracja stosu to ta sama logika. Bariera adopcji to inercja, nie jakość europejskich narzędzi (luka realna głównie w czołówce LLM i social media).

**5. Multi-model — dywersyfikacja AI jak multi-cloud (Wojewodzic)**
Po lekcji Fable 5: tak jak branża IT przeszła na multi-cloud, organizacje powinny przejść na **strategię multi-model** — warstwa abstrakcji (Open Router: jeden interfejs do wszystkich modeli), modele lokalne (Bielik, Mistral, Plum) do rutynowych zapytań, prywatna chmura dla procesów krytycznych. Kluczowa dyscyplina: **plan migracji przygotowany zanim nastąpi przymusowy przestój** — przegląd, które krytyczne procesy stoją na jednym modelu lub ekosystemie, i przetestowany zapasowy tor.

**6. Posiadanie i rozumienie technologii, nie sam dostęp**
Nagłowski (AI Social Lab): „najważniejsze jest posiadanie i rozumienie technologii, nie jedynie dostęp do niej" — otwarte modele z lokalnym przetwarzaniem ([[Bielik]] rozwijany społecznościowo przez [[SpeakLeash]]) pozwalają organizacjom przetwarzać dane osób w kryzysie bez oddawania ich korporacyjnemu dostawcy, który może zmienić warunki z dnia na dzień. Scholz radykalizuje: sektor potrzebuje **dissident tech** — infrastruktury budowanej celowo dla ruchów społecznych, bo „narzędzia pana nigdy nie rozmontują domu pana" (Audre Lorde); trzy systemowe problemy Big Tech to bezpieczeństwo danych wobec autorytarnych rządów, brak interoperacyjności i dane organizacji uwięzione w cudzych platformach. Wersja pragmatyczna (Schmeichel-Zarzeczna): **open source z matrycą decyzyjną** (aktywny rozwój? społeczność? dokumentacja? kompetencje w zespole? format czytelny dla partnerów?) i **podejście hybrydowe** — narzędzia komercyjne do codziennej pracy, otwarte tam, gdzie dane są wrażliwe; etapami, nie rewolucją.

**7. Stack jako część teorii zmiany**
Foale: jeśli misją organizacji jest dobro społeczne, a subskrypcje finansują firmy destabilizujące demokrację, to **wybór dostawcy jest decyzją polityczną i elementem teorii zmiany** — nie neutralnym zakupem. Analogia diagnostyczna: sektor jest z suwerennością tam, gdzie aktywizm klimatyczny 20 lat temu — problem znany, brakuje praktycznych ścieżek operacjonalizacji. Z tej samej dyskusji (ECF): „bezpłatne" znaczy „jesteś produktem", a problemy technologiczne organizacji to często problemy organizacyjne w przebraniu — audyt zależności warto łączyć z pytaniem o strategię, nie tylko o narzędzia.

---

**8. Odwrócenie argumentu „otwarte = niebezpieczne" ([[Andrew Ng]])**
Kontrapunkt dla domyślnej narracji bezpieczeństwa: w opisanym przez Ng incydencie to **model zamknięty** przypadkowo wywołał poważny atak na infrastrukturę Hugging Face, a **otwarty model GLM 5.2 pomógł go przeanalizować i się obronić** — bo komercyjny LLM odmówił analizy logów „ze względów bezpieczeństwa". Guardraile utrudniły obronę, otwartość ją umożliwiła. Trzy wnioski dla stosu organizacji: (a) otwarte modele wagowe (GLM 5.2, nadchodzący Kimi K3) domykają dystans do zamkniętych, co osłabia argument o ich rzekomej niebezpieczności; (b) nadmierne ograniczenia mają realny koszt operacyjny w sytuacji kryzysowej; (c) **możliwość analizy własnych danych bez wysyłania ich na zewnątrz to praktyczna przewaga bezpieczeństwa, nie postulat ideologiczny**. Ng nazywa też część dyskursu o AI safety próbą **regulatory capture** na korzyść dostawców modeli zamkniętych — teza mocna i sporna, ale warta znajomości, bo pojawia się w rozmowach o wyborze stosu.

**9. Warstwa fizyczna suwerenności — centra danych jako lokalny konflikt**
Suwerenność technologiczna ma wymiar, którego nie widać w warstwach stosu Benaicha: **infrastrukturę fizyczną i jej lokalny koszt**. Opór wobec centrów danych AI stał się zjawiskiem globalnym — od USA (moratoria w Nowym Jorku i Seattle, koalicja 500+ organizacji) przez Holandię, Irlandię, Chile i Urugwaj po Australię i Francję. Liczby, które nadają temu skalę: **71% Amerykanów sprzeciwia się budowie centrum danych w swojej okolicy** (48% zdecydowanie — więcej niż wobec elektrowni jądrowej: 53%); **centra danych zużyły 23% irlandzkiej energii elektrycznej w 2025 r.** (wzrost z 5% dekadę wcześniej, prognoza 31% do 2034). Trzykrokowy przepis organizowania: **dowiedz się, czego ci nie powiedzieli** (wnioski planistyczne, dostęp do informacji publicznej, dokumenty zoningowe — firmy zwykle ukrywają realną liczbę miejsc pracy, wpływ na ceny energii i zużycie wody) → **buduj najszerszą możliwą koalicję** (kościoły, lokalny biznes, kluby sportowe — trudniejsi do zdyskredytowania niż „zwykli podejrzani") → **zrozum, jak wygląda wygrana** (moratoria kupują czas, nie są rozwiązaniem docelowym). Uwaga dla filantropii: pieniądze zwykle przychodzą za późno, bo finansuje się organizacje, a nie ruchy — a nieformalne grupy bez osobowości prawnej działają najskuteczniej w najwcześniejszej fazie.

**10. Suwerenność a rynek pracy — ryzyko bycia dostawcą talentu bez własności technologii**
Trzecie rozszerzenie: konsekwencje makro. Prognozy dla Polski rozjeżdżają się mocno — **3,7 mln zagrożonych miejsc pracy (Polski Instytut Ekonomiczny) do 5,5 mln (MFW, horyzont 5–10 lat)** przy ok. 17 mln pracujących; Layoffs.fyi notuje **121 tys. zwolnień w branży technologicznej do połowy lipca 2026** (wobec 126 tys. w całym 2025). Bank Światowy widzi dla Polski zysk **1,3–12,1% PKB**, ale warunkowany przekwalifikowaniem i aktywną polityką rynku pracy. Kluczowy dla tej strony jest jednak inny wątek: ryzykiem nie jest tylko utrata miejsc pracy, lecz **przejęcie marż i klientów przez kraje, które wcześniej zbudują przewagę w modelach, danych i infrastrukturze** — scenariusz, w którym kraj zostaje dostawcą talentu bez własności technologii. To ten sam mechanizm co „suwerenność na wynajem", tylko na poziomie gospodarki, nie pojedynczej organizacji. Rozbieżność prognoz (PIE, MFW, NASK) sama w sobie jest argumentem za **planowaniem scenariuszowym**, nie jednoznacznym.

## Frameworki-kotwice

- **4 analogie historyczne (Jemielniak)** — Suez / PGP / Minitel / **Galileo**: buduj infrastrukturę zamiast pisać regulacje do cudzych maszyn.
- **Suwak, nie przełącznik + 4 kroki migracji (Tkaczyk)** — wyszukiwarka → mail na własnej domenie → pliki → analityka/AI; każdy krok samodzielnie zmniejsza ryzyko.
- **Warstwy stosu suwerenności (Benaich)** — chipy / dane / middleware / talenty; suwerenność tylko na szczycie = kosztowna iluzja (digital colonialism).
- **Strategia multi-model (Wojewodzic)** — warstwa abstrakcji + modele lokalne + prywatna chmura; plan B przed przymusowym przestojem.
- **Matryca decyzyjna open source + hybryda (ngo.pl)** — rozwój/społeczność/dokumentacja/kompetencje/format; komercyjne do codzienności, otwarte do danych wrażliwych.
- **3 problemy systemowe Big Tech (Scholz)** — bezpieczeństwo wobec autorytaryzmu / brak interoperacyjności / dane organizacji w cudzych rękach.
- **Audyt zależności (ECF/Caraballo)** — na czym stoi hosting? kto obsługuje e-mail? kto przetwarza płatności? które procesy stoją na jednym dostawcy AI?
- **Liczby-kotwice**: 70% europejskiej chmury = Wielka Trójka, europejscy dostawcy ~15%; kary do 20 lat za „material support"; Mistral Vibe 14,99 EUR/mies.; katalogi alternatyw: switching.software, privacyguides.org.

---

## Powiązane pojęcia

- [[2026-06-25 Owned vs rented audience|Owned vs rented audience]] — ta sama logika „najemca czy właściciel" na poziomie publiczności; suwerenność technologiczna to jej rozszerzenie z relacji z odbiorcami na całą infrastrukturę. Czerwony link stamtąd zrealizowany.
- [[2026-07-06 Context layer organizacji|Context layer organizacji]] — najcenniejsza warstwa do usuwerennienia: gdzie leży baza wiedzy organizacji, jest decyzją misyjną (Neider: data strategy = mission strategy, no-access mindset).
- [[2026-07-06 RODO i dane wrażliwe|RODO i dane wrażliwe]] — prawna strona tego samego medalu: modele lokalne, architektura „model vs wiedza" i DPA to techniczne realizacje suwerenności danych beneficjentów.
- [[2026-06-13 Wdrażanie AI w organizacji społecznej|Wdrażanie AI w organizacji społecznej]] — audyt zależności od dostawców powinien być filarem gotowości obok danych, ludzi i procesów.
- [[2026-06-15 AI governance|AI governance]] — miejsce, gdzie suwerenność staje się procedurą: polityka doboru narzędzi, vendor due diligence, plan ciągłości działania.
- [[2026-07-20 AI Act|AI Act]] — Europa reguluje maszyny, których nie buduje (Jemielniak): regulacja bez własnej infrastruktury daje suwerenność nominalną. Czerwony link zrealizowany 2026-07-20.
- [[Sprawczość organizacyjna]] — suwerenność to infrastrukturalny warunek sprawczości: organizacja, która nie kontroluje swoich narzędzi, nie kontroluje swojego działania (czerwony link — backlog, 2. incoming).

---

## Zastosowanie w kontekście organizacji społecznych

- **Audyt zależności jako moduł konsultacji strategicznej**: cztery pytania ECF (hosting? e-mail? płatności? AI?) + mapa „co posiadamy / co wynajmujemy" — wynik: lista pojedynczych punktów awarii z priorytetami. Dla organizacji pracujących na wrażliwych tematach (prawa człowieka, migranci, osoby LGBTQ+) to element bezpieczeństwa beneficjentów, nie komfortu.
- **Rama rozmowy z zarządem — ryzyko, nie ideologia**: argumentuj przez ciągłość działania („co zrobicie, gdy dostawca wyciągnie wtyczkę?") i precedensy (MTK, Fable 5), nie przez antyamerykańskość czy purystyczny open source. Suwak zamiast rewolucji obniża próg decyzji.
- **Minimalny pakiet dla małej organizacji**: mail na własnej domenie, regularny eksport bazy kontaktów (spójne z zasadą „drogi wyjścia"), kopia krytycznych plików poza jednym dostawcą, przetestowany zapasowy model AI. Koszt: wieczór pracy i kilka euro miesięcznie.
- **Dane beneficjentów = najwyższy priorytet suwerenności**: procesy dotykające osób w kryzysie na modelach lokalnych ([[Bielik]] przez [[Ollama]]) lub w architekturze „model vs wiedza"; strefy bez AI dla rozmów najwrażliwszych.
- **Moduł szkoleniowy „suwerenność cyfrowa organizacji"**: precedensy → suwak → audyt → plan migracji; matryca decyzyjna open source i katalogi alternatyw (switching.software) jako handouty; [[Bielik]]/[[SpeakLeash]] jako polski przykład infrastruktury obywatelskiej.
- **Nisza doradcza**: moment kryzysowy otworzył organizacje na rozmowę o alternatywach — audyt suwerenności może być osobną usługą konsultingową, spinającą wątki AI, danych i fundraisingu (płatności!).

---

## Otwarte pytania

- Gdzie leży próg opłacalności dla małej organizacji: koszt migracji (czas, kompetencje, tarcie zespołu) vs realne prawdopodobieństwo odcięcia — kiedy pozostanie przy Big Tech jest racjonalną decyzją, a kiedy hazardem?
- Czy „europejskie" znaczy „suwerenne"? CLOUD Act łapie amerykańskich dostawców niezależnie od lokalizacji serwera, a Mistral stoi na amerykańskich chipach (paradoks Benaicha) — jak głęboko w stos musi schodzić audyt, żeby nie kupować iluzji?
- Jak pogodzić suwerenność z konkurencyjnością, skoro czołówka modeli LLM jest amerykańska i chińska — czy multi-model z lokalnym fallbackiem to trwały kompromis, czy tylko odroczenie wyboru?
- Kto sfinansuje infrastrukturę sektora? Scholz: filantropia nie inwestuje w technologię infrastrukturalną — czy europejscy grantodawcy uczynią suwerenność cyfrową linią budżetową, tak jak kiedyś cyberbezpieczeństwo?
- Czego brakuje, by temat przeszedł drogę aktywizmu klimatycznego (Foale) — jaki jest odpowiednik „śladu węglowego" dla stosu technologicznego: mierzalny, porównywalny wskaźnik zależności, który organizacja może policzyć i raportować?
