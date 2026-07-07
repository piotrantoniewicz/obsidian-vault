---
categories: Concept
tags:
  - strategia-AI
  - organizacje-społeczne
  - strategia-organizacji
created: 2026-07-06
updated: 2026-07-07
relevance: wysoka
sources:
  - "[[2025-09-02 AI Act & RODO 2025 Przewodnik po regulacjach UE karach i compliance]]"
  - "[[2025-07-22 AI w organizacji pozarządowej – 6 pytań, które warto sobie zadać]]"
  - "[[2025-05-06 Jak dbać o prywatność i chronić dane w dobie generatywnej sztucznej inteligencji Poradnik]]"
  - "[[2026-04-30 Jak bezpiecznie wdrożyć AI w organizacji - podsumowanie webinaru z Mateuszem i Kamilem]]"
  - "[[2025-11-12 Hidden Privacy Trap AI That s Silently Compromising Your Nonprofit s Mission LinkedIn]]"
  - "[[2026-01-27 Uważaj, co mówisz chatbotowi. Jak Big Tech trenuje AI na naszych rozmowach]]"
  - "[[2026-06-23 A to nie wycieknie - na ile ufasz AI]]"
---

# RODO i dane wrażliwe (GDPR & Sensitive Data)

RODO to prawny fundament każdej pracy organizacji społecznej z danymi osobowymi, a **dane wrażliwe** (szczególne kategorie: zdrowie, sytuacja socjalna, poglądy, orientacja) to w tym sektorze nie wyjątek, lecz chleb powszedni — dane beneficjentów niemal z definicji do nich należą. Era generatywnej AI podnosi stawkę: najwięksi dostawcy **domyślnie trenują modele na rozmowach użytkowników**, regulamin darmowego narzędzia jest wiążącą umową, a kary mogą się kumulować (do 4% obrotu z RODO + do 7% z AI Act). Teza spinająca całość: **RODO nie blokuje AI — blokuje *źle postawione* AI**; dobrze skonfigurowane wdrożenie daje organizacji *większą* kontrolę nad danymi niż obecne rozproszenie po skrzynkach, dyskach i prywatnych czatach.

---

## Kluczowe mechanizmy

**1. Organizacje społeczne grają o najwyższą stawkę**
Opisanie przypadku beneficjenta w prompcie darmowego chatbota to potencjalne przekazanie danych szczególnych kategorii Big Techowi — bezpośrednie ryzyko naruszenia RODO i, co gorsze, bezpowrotnej utraty zaufania beneficjentów, darczyńców i partnerów ([[Wayan Vota]]). Do tego dochodzi warstwa regulacyjna: RODO i [[AI Act]] obowiązują **jednocześnie i eksterytorialnie**, a większość organizacji używających chatbotów, systemów rekomendacji czy CRM z AI jest już „podmiotem stosującym" w rozumieniu AI Act — z konkretnymi obowiązkami, niezależnie od tego, że niczego nie tworzy ([[Kasia Krzywicka]]).

**2. Obowiązki, nie zakazy — mapa zgodności**
Rdzeń RODO przy AI to cztery pytania: **podstawa prawna** przetwarzania, **zasada minimalizacji** (tylko niezbędne dane), **DPIA** (ocena skutków dla ochrony danych — przy AI często obowiązkowa) i **obowiązki informacyjne** (osoba musi wiedzieć jasno i przystępnie, że jej dane przetwarza AI). Nad tym mapa 8 kroków compliance (Krzywicka): rejestr systemów AI → analiza RODO każdego → weryfikacja AI Act (zakazy, wysokie ryzyko) → plan naprawczy → aktualizacja polityk i klauzul → analiza biasu w procesach → transparentność wobec użytkowników → **compliance jako proces ciągły**, nie jednorazowy projekt. Dla decyzji wrażliwych minimum dobrej praktyki to human-in-the-loop — AI nigdy nie decyduje w pełni automatycznie o sprawach beneficjentów (Maciejewicz).

**3. Domyślne trenowanie i paradoks prywatności**
Badanie [[Stanford University]] (Jennifer King, 28 dokumentów polityk prywatności): **wszystkie sześć największych firm AI domyślnie wykorzystuje rozmowy do trenowania modeli**, często bez realnej możliwości sprzeciwu. Regulamin narzędzia to wiążąca umowa — wpisanie danych beneficjentów do darmowego narzędzia może oznaczać zgodę na ich wykorzystanie przez dostawcę. Mechanizm psychologiczny pogłębia problem: interfejs konwersacyjny uruchamia społeczne skrypty zaufania i skłania do ujawniania więcej, niż zamierzamy (paradoks prywatności). Reguły kciuka: *„albo płacisz pieniędzmi, albo płacisz danymi"* — wersje płatne są bezpieczniejsze od darmowych, a dostęp przez [[API]] zwykle bezpieczniejszy niż aplikacja webowa (większość dostawców nie trenuje na danych z API).

**4. Warstwa techniczna: anonimizacja → architektura → lokalność**
Trzy piętra ochrony. **Anonimizacja przed wysłaniem** ([[Kamil Śliwowski]]): pseudonimizacja, maskowanie, uogólnianie (wiek → przedział), zamiana danych, szum — do modelu trafia niezbędne minimum. **Architektura „model vs wiedza"** (wPraktyce.AI): model na serwerach europejskich pod DPA i RODO to co innego niż publiczny czat, a firmowa wiedza w bazie [[2026-06-14 RAG|RAG]] leży wyłącznie u klienta; opcja skrajna to deployment offline („zamknięta puszka"). **Modele lokalne** ([[Ollama]], LM Studio, jan.ai) eliminują transfer danych do chmury w ogóle — rekomendacja dla procesów dotykających danych beneficjentów. Do tego natychmiast wdrażalne **strefy bez AI**: rozmowy prawne, HR, dane darczyńców — bez botów transkrybujących (Vota).

**5. Vendor due diligence — pytania zamiast zaufania**
Pięć pytań do każdego dostawcy AI (Chrobok/Porembiński): Czy dane trenują model? Gdzie są przechowywane i kto ma dostęp? Co się z nimi dzieje po końcu subskrypcji? Czy podpiszesz **DPA** (Data Processing Agreement)? Jakie masz certyfikaty (ISO, SOC 2)? Dla narzędzi transkrypcji spotkań — najczęstszego konia trojańskiego — dodatkowa piątka (Vota): mechanizm udokumentowanej zgody (RODO art. 6 i 13), serwery UE/SCC (a nie CLOUD Act), umowny zakaz trenowania na nagraniach, polityka retencji z automatycznym usuwaniem, redakcja wrażliwych fragmentów. Zgoda na nagrywanie musi być dwustronna.

**6. Paradoks bezpieczeństwa — największe ryzyko to nie wdrożenie, lecz jego brak**
Ponad **60% pracowników używa narzędzi AI bez wiedzy przełożonych** (Shadow AI) — dane wyciekają nie przez formalne wdrożenia, lecz przez „ciche" wklejanie do publicznego [[ChatGPT]] i rozproszenie danych po skrzynkach byłych pracowników i prywatnych dyskach. Odpowiedź to nie zakaz (zakazy ukrywają problem), lecz: inwentaryzacja → prosta polityka (jedna strona, 3 pytania: czego nie wklejać, których narzędzi używamy, kto odpowiada) → dobór narzędzi wg 4 poziomów bezpieczeństwa (darmowe → Pro → Enterprise/DPA → lokalne) → edukacja jak BHP, z **just culture**: nie karać za przyznanie się do incydentu, bo przestaną być zgłaszane. Od strony bazy kontaktów te same zasady przybierają formę praktyk [[2026-06-29 Higiena listy|higieny listy]]: audytowalna ścieżka pochodzenia rekordu (provenance), suppression zamiast kasowania, double opt-in — zgodność i jakość danych to jedna dyscyplina.

---

## Powiązane pojęcia

- [[2026-06-15 AI governance|AI governance]] — governance to procesy, role i polityka; ta strona to jego prawny substrat: RODO/AI Act wyznaczają twarde minimum, wokół którego governance buduje praktykę („wyciek danych beneficjentów = incydent RODO").
- [[2026-06-29 Higiena listy|Higiena listy]] — provenance, suppression i double opt-in to jednocześnie praktyki jakości bazy i dowody zgodności; „no lineage, no send" jest zasadą RODO w przebraniu operacyjnym.
- [[2026-06-13 Wdrażanie AI w organizacji społecznej|Wdrażanie AI w organizacji społecznej]] — audyt wrażliwości danych i mapa ich przepływu to obowiązkowy krok gotowości przed jakimkolwiek pilotażem („nie nurkuj tam, gdzie twój mózg jeszcze nie był").
- [[2026-06-14 RAG|RAG]] — architektoniczna odpowiedź na dylemat prywatności: wiedza organizacji w bazie u klienta, model za DPA, opcjonalnie całość offline; „bezpieczniejsza ścieżka" dla danych beneficjentów.
- [[2026-06-15 Agentic AI|Agentic AI]] — im więcej autonomii, tym ostrzejsze pytania o podstawę prawną i nadzór: human-in-the-loop przy danych wrażliwych to wymóg, nie opcja.
- [[AI Act]] — europejska regulacja systemów AI wg poziomów ryzyka (zakazy, systemy wysokiego ryzyka, obowiązki podmiotu stosującego); kandydat na osobną stronę (czerwony link — backlog).
- [[2026-07-07 Suwerenność technologiczna|Suwerenność technologiczna]] — modele lokalne i architektura „model vs wiedza" to nie tylko compliance, lecz element szerszej niezależności od dostawców, których warunki (i dostępność) mogą się zmienić z dnia na dzień.

---

## Zastosowanie w kontekście organizacji społecznych

- **Otwierające ćwiczenie szkoleniowe „policz, gdzie leżą twoje dane"**: uczestnicy sami odkrywają rozproszenie (skrzynki, dyski, prywatne czaty) zanim padnie słowo „ryzyko AI" — odwraca rozmowę z „czy AI jest bezpieczne" na „czy nasz obecny stan jest bezpieczny".
- **Kodeks AI jako usługa doradcza**: jednostronicowa polityka (czego nie wklejać / które narzędzia / kto odpowiada) + zasady human-in-the-loop i strefy bez AI — dokument zespołowy, nie prawniczy; „cokolwiek, co będziesz rozwijać, jest lepsze niż nic".
- **Checklista compliance do kursu „Fundraising z AI"**: 8 kroków Krzywickiej + 5 pytań do dostawcy + pytanie o DPIA — gotowy moduł warsztatowy dla organizacji przetwarzających dane darczyńców i beneficjentów.
- **Standard rekomendacji narzędzi**: płatne wersje jako minimum (nie opcja), API zamiast aplikacji webowej, DPA przy każdym zakupie, modele lokalne dla procesów z danymi beneficjentów.
- **Argument odblokowujący wdrożenia**: „RODO nie blokuje AI — blokuje źle postawione AI" plus paradoks bezpieczeństwa (Shadow AI vs system z logami) — odpowiedź na najczęstszy bloker decyzyjny zarządów.

---

## Otwarte pytania

- Gdzie dokładnie przebiega próg obowiązkowej DPIA przy typowych zastosowaniach AI małej organizacji (transkrypcje spotkań, segmentacja bazy w CRM, chatbot informacyjny) — czy istnieje praktyczna lista kontrolna dla sektora?
- Czy małe organizacje udźwigną compliance AI Act bez etatu prawnika — kto ma pełnić rolę IOD/compliance i czy uproszczenia dla MŚP obejmą także sektor społeczny?
- Jak pogodzić anonimizację z użytecznością — w którym momencie anonimizacja danych beneficjentów odbiera analizie AI wartość merytoryczną i co wtedy: model lokalny czy rezygnacja z automatyzacji?
- Czy przesunięcie terminów compliance dla systemów wysokiego ryzyka (EU AI Act Digital Omnibus, XII 2027) to ulga dająca czas na przygotowanie, czy uśpienie czujności sektora?
- Jak audytować zgodność łańcucha narzędzi no-code (Make.com, Zapier + LLM), gdzie dane osobowe przepływają przez kilku procesorów naraz — kto jest czyim podmiotem przetwarzającym?
