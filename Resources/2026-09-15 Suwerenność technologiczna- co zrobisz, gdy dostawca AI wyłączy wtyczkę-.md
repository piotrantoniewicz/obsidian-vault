---
categories:
  - Clippings
authors: ["[[Piotr Antoniewicz]]"]
url: "https://publicystyka.ngo.pl/suwerennosc-technologiczna-co-zrobisz-gdy-dostawca-ai-wylaczy-wtyczke"
source: "[[Archives/2026-09-15 Suwerenność technologiczna- co zrobisz, gdy dostawca AI wyłączy wtyczkę-|2026-09-15 Suwerenność technologiczna- co zrobisz, gdy dostawca AI wyłączy wtyczkę-]]"
published: 2026-09-15
created: 2026-09-16
relevance: wysoka
tags:
  - "strategia-AI"
  - "organizacje-społeczne"
  - "strategia-organizacji"
---

# Suwerenność technologiczna: co zrobisz, gdy dostawca AI wyłączy wtyczkę?

Własny artykuł (publicystyka.ngo.pl) argumentuje, że suwerenność technologiczna małej organizacji — czyli zdolność do działania niezależnie od decyzji jednego dostawcy AI, chmury czy płatności — przestała być kwestią teoretyczną. Punktem wyjścia są konkretne precedensy: wyłączenie modelu Anthropic Fable 5 na 19 dni po decyzji eksportowej USA, zawieszenie konta MTK w Microsoft 365 po sankcjach, oraz drastyczne podwyżki cen licencji VMware po przejęciu przez Broadcom. Tekst pokazuje, że lokalizacja serwera nie chroni przed jurysdykcją (CLOUD Act), a polskie dane (raport Klon/Jawor i Sektor 3.0) potwierdzają, że sektor NGO szybko przechodzi na chmurę i AI, jednocześnie prawie nie myśląc o bezpieczeństwie ciągłości działania. Główna teza: suwerenności nie buduje się rewolucją, tylko stopniowym „przesuwaniem suwaka" — małymi, tanimi krokami zmniejszającymi pojedyncze punkty awarii.

## Frameworki i metody
- **Trzy pytania o suwerenność** (rama Pabla Defendiniego) — czyje są nasze dane (czy trafiają na serwer poza naszą kontrolą)?; czyja jest infrastruktura (czy znamy jej realny koszt finansowy i środowiskowy)?; czyj jest osąd (jakie decyzje oddajemy AI na stałe, tracąc kompetencję)?
- **Suwak, nie przełącznik** (rama Adama Tkaczyka) — migracja jako stopniowy proces w czterech etapach: 1) wyszukiwarka i przeglądarka (5 minut, zero kosztów); 2) mail na własnej domenie (kilka euro miesięcznie, zapewnia przenośność); 3) pliki i dokumenty (ok. dwa dni pracy, nowe projekty od razu w docelowym miejscu); 4) analityka, treści i AI (miesiąc równoległych testów przed pełnym przejściem).
- **Audyt zależności — cztery pytania**: kto hostuje stronę i dane?; kto obsługuje pocztę?; kto przetwarza płatności?; kto trzyma pliki w chmurze?; które procesy stoją na jednym dostawcy AI?
- **Strategia multi-model** — warstwa abstrakcji łącząca różnych dostawców (np. [[Open Router]]), modele lokalne (Bielik, Mistral, Plum) do zadań rutynowych i prywatna chmura do procesów krytycznych, budowana zanim nastąpi przymusowy przestój.

## Kluczowe dane
- Anthropic wyłączył model Fable 5 na 19 dni (czerwiec–1 lipca 2026) na mocy decyzji eksportowej Departamentu Handlu USA.
- AWS, Microsoft Azure i Google Cloud kontrolują łącznie ok. 63–70% rynku chmury (Synergy Research, Q1 2026).
- Wg raportu Klon/Jawor i Sektor 3.0: 37% polskich NGO korzysta ze współdzielonej chmury (wzrost z 25% w 2021), 29% korzysta z narzędzi AI, ale tylko 14% wskazuje poprawę bezpieczeństwa danych jako potrzebę.
- Wg IBM Institute for Business Value (czerwiec 2026): tylko 9% kadry zarządzającej firm deklaruje pełne rozumienie zależności od dostawców AI, a 71% uważa zmianę głównego dostawcy AI za trudną.

## Wnioski
- Ryzyko utraty dostępu do AI/chmury/płatności jest realne i już się zdarzało (Fable 5, MTK, VMware/Broadcom) — to nie scenariusz hipotetyczny, tylko powtarzalny wzorzec.
- Lokalizacja serwera nie daje ochrony prawnej wobec amerykańskich dostawców (CLOUD Act) — kluczowe jest posiadanie planu B, a nie geografia infrastruktury.
- Budowanie suwerenności można zacząć od zera kosztem i bez działu IT — pierwszy krok „suwaka" (przeglądarka/wyszukiwarka) zajmuje 5 minut, co obala argument o barierze czasowej dla małych organizacji.

## Zastosowanie
Gotowy materiał do wykorzystania w szkoleniach i konsultacjach dla NGO — szablon „mapy zależności" i checklista „4 kroki w jeden dzień" z artykułu można od razu zaproponować klientom jako punkt wyjścia do audytu infrastruktury. Ramę „suwak, nie przełącznik" warto też stosować przy własnym doradztwie wdrożeniowym (dobryai.pl), żeby obniżać opór klientów przed rozpoczęciem migracji.
