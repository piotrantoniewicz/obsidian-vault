---
authors:
  - '[[ai-leaders]]'
categories:
  - Clippings
created: '2026-08-19'
published: '2026-08-19'
relevance: wysoka
source: >-
  [[Archives/2026-08-19 Dane, których nie masz, a właściwie nie wiesz, że masz.
  KSeF, e-Doręczenia i koniec wymówek|2026-08-19 Dane, których nie masz, a
  właściwie nie wiesz, że masz. KSeF, e-Doręczenia i koniec wymówek]]
tags:
  - strategia-AI
  - automatyzacja
  - narzędzia-AI
url: >-
  https://aileaders.pl/artykuly/dane-ksef-e-doreczenia-i-koniec-wymowek/?ref=aileaders-pl-newsletter
---
# Dane, których nie masz, a właściwie nie wiesz, że masz. KSeF, e-Doręczenia i koniec wymówek

Artykuł ai-leaders.pl argumentuje, że polskie firmy przestały mieć wymówkę „brak danych/API" dla wdrożeń AI, bo od 1 kwietnia 2026 r. każda faktura to ustrukturyzowany plik XML w centralnym systemie KSeF, a nie skan czy PDF. Tekst pokazuje konkretnie, co siedzi w schemacie FA(3), jak dobrać się do danych przez API KSeF 2.0 bez software house'u i jakie use case'y (mapa wydatków, ciche podwyżki cen, cash flow, duplikaty, koncentracja przychodów) można zrobić jeszcze w tym kwartale — przy czym w większości z nich generatywna AI wcale nie jest głównym bohaterem. Druga część dotyczy e-Doręczeń i terminu 1 października 2026 dla jednoosobowych działalności, ze szczególnym naciskiem na to, że automatyzacja odczytu pisma nie może zastąpić jasno przypisanej odpowiedzialności człowieka za reakcję. Kluczowa teza dla liderów AI: strukturalne dane bez sensownego katalogowania i tak zostają bałaganem, tylko łatwiejszym do zmierzenia — i dopiero tu LLM zaczyna realnie zarabiać na siebie.

## Frameworki i metody

**Ścieżka minimalna dostępu do API KSeF 2.0 (bez software house'u):**
1. **Uprawnienia** — zgłoszenie ZAW-FA i nadanie uprawnienia InvoiceRead; najczęstszy punkt, w którym wdrożenie stoi tydzień.
2. **Uwierzytelnienie** — challenge, podpis certyfikatem lub tokenem, token dostępowy do kolejnych operacji.
3. **Metadane, potem treść** — filtrowanie po dacie, NIP kontrahenta, typie (sprzedaż/zakup), statusie, dopiero potem pobranie XML lub eksport wsadowy.
4. **Limity** — rate limity API, pobieranie wsadowe z paginacją jako proces nocny, nie kliknięcie w przycisk.
5. **Parsowanie i model danych** — XML → tabela pozycji + tabela nagłówków; ok. dzień pracy jednej osoby plus tydzień porządkowania.

**Pięć use case'ów na dane z KSeF (z pytaniem biznesowym, KPI i tym, czego nie robić):** mapa wydatków i koncentracja dostawców (GROUP BY, nie LLM), ciche podwyżki cen per pozycja, prognoza cash flow z terminów płatności (model statystyczny bije GenAI), duplikaty i faktury-widmo (klasyczny ML), koncentracja przychodów i struktura oferty.

**Pięć pułapek KSeF/e-Doręczeń:** PDF przestał być fakturą (jest tylko wizualizacją); brak kar administracyjnych do 2027 to nie brak obowiązku; hybryda faktur z numerem KSeF i bez niego psuje JPK_VAT; załącznik w FA(3) nie służy plikom binarnym; XML ≠ dobre dane — ustrukturyzowany bałagan to wciąż bałagan, dopóki nazwy pozycji nie zostaną znormalizowane.

**Trzy pytania przed wysłaniem danych z faktur do zewnętrznego modelu:** dokąd to leci (dostawca, region, retencja, podprocesor), czy musi lecieć w całości (pseudonimizacja rozwiązuje 80% problemu za 20% wysiłku), kto to zatwierdził (brak odpowiedzi = shadow AI na danych finansowych firmy).

## Kluczowe dane
- Od 1 kwietnia 2026 r. obowiązek KSeF objął wszystkich pozostałych przedsiębiorców (wcześniej, od 1 lutego 2026, firmy z obrotem >200 mln zł w 2024 r.).
- Od 1 stycznia 2027 kończy się okres bez kar administracyjnych: sankcje do 100% kwoty VAT z faktury wystawionej poza systemem, przy fakturach bez wykazanego podatku — do 18,7% kwoty brutto.
- Faktury przechowywane są w KSeF przez 10 lat.
- Termin na założenie adresu do e-Doręczeń dla jednoosobowych działalności wpisanych do CEIDG przed 1 stycznia 2025 to 1 października 2026.

## Wnioski
- [[KSeF]] rozwiązał przy okazji najczęstszy blocker wdrożeń AI w polskich MŚP — brak ustrukturyzowanych danych i API — ale to nie znaczy, że dane są od razu gotowe do użycia: normalizacja nazw pozycji i katalogowanie to wciąż osobna praca.
- Najlepsze use case'y na start nie wymagają generatywnej AI (GROUP BY, model statystyczny, klasyczny ML) — GenAI wchodzi dopiero przy porządkowaniu i normalizacji ustrukturyzowanego bałaganu.
- Automatyzacja odczytu dokumentu (KSeF, e-Doręczenia) bez jasno przypisanej odpowiedzialności człowieka za reakcję to pozorna automatyzacja — realne ryzyko przenosi się z „czy system to wykryje" na „kto o tym wie i zareaguje".

## Cytat
> Ustrukturyzowany bałagan to wciąż bałagan — tyle że łatwiej go teraz zmierzyć.

## Zastosowanie
Konkretny, gotowy do użycia materiał na szkolenia i konsultacje AI dla organizacji i małych firm (dobryai.pl) — checklista na 30 dni i pięć use case'ów to gotowy szkielet warsztatu „od czego zacząć wdrożenie AI". Ramka trzech pytań przed wysłaniem danych do modelu przydaje się też przy budowaniu polityk AI dla klientów NGO, analogicznie do wcześniejszych materiałów o governance AI w sektorze.
