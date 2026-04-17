---
categories: Clippings
authors:
  - "[[Al Iverson]]"
url: https://www.spamresource.com/2026/01/guest-post-spamtraps-arent-hygiene.html
source: "[[2026-01-27 Guest Post Spamtraps Aren t a Hygiene Problem -- They’re a Data Integrity Problem]]"
published: 2026-01-27
created: 2026-03-22
relevance: średnia
tags:
  - digital-campaigning
  - organizacje-społeczne
---

# Guest Post: Spamtraps Aren't a Hygiene Problem — They're a Data Integrity Problem

[[Al Iverson]] i [[Pekka Jalonen]] z [[Koli-Lõks]] stawiają tezę, że spamtrapy (pułapki spamowe) są sygnałem nie o brudnej liście, lecz o utracie kontroli nad integralnością danych na wejściu do systemu. Cztery typy pułapek (honeypot, pristine, recycled, typo) mapują się każda na inny rodzaj błędu procesu: złe źródło pozyskania, brak weryfikacji intencji subskrybenta, utratę suppressions między systemami lub dziurawą walidację formularzy. Problemy z dostarczalnością często pojawiają się bez widocznych ostrzeżeń w standardowych metrykach — trapy nie odbijają i nie skarżą się, po prostu kumulują dowody. Artykuł jest szczególnie przydatny jako mapa diagnostyczna: każdy typ pułapki wskazuje na konkretny punkt procesu, który wymaga naprawy.

## Frameworki i metody

- **4 typy spamtrapów i ich diagnoza:**
  - *Honeypot* — pułapka intencji na wejściu: adres zebrany przez bota/scraper, wskazuje na niekontrolowane źródło pozyskania (co-reg, import CSV bez historii)
  - *Pristine* — pułapka akwizycji: adres, który nigdy nie należał do prawdziwego subskrybenta; ekspozycja na pristine = utrata kontroli nad granicą wejścia do systemu
  - *Recycled* — pułapka dyscypliny lifecycleowej: adres kiedyś aktywny, potem wygasły (550 5.1.1 przez min. 12 miesięcy), reaktywowany jako pułapka; pojawia się przy przywracaniu starych segmentów lub utracie suppressions między systemami
  - *Typo* — pułapka jakości inputu: adres z literówką domenową (gnail.com zamiast gmail.com), wskazuje na formularz bez walidacji lub ręczny wpis bez weryfikacji
- **Provenance chain** — dla każdego adresu: źródło, timestamp, form ID, wersja consent textu, IP, user agent; jeśli nie możesz zrekonstruować tej ścieżki, adres jest nieuzasadniony
- **"No lineage, no send"** — zasada: brak audytowalnej ścieżki = nie wysyłasz
- **Suppression persistence** — suppresje muszą przetrwać każdą granicę systemową (import, migracja, integracja); utrata suppressions to najczęstsza przyczyna recycled traps

## Wnioski

- Dostarczalność emaili to kwestia procesów, nie tylko treści — NGO, które mają problemy z filtrami, powinny patrzeć najpierw na integralność pozyskiwania adresów, nie na temat wiadomości
- Spamtrapy nie dają widocznych bounców — filtrowanie tightens się po cichu, bez spike'u skarg, co sprawia, że diagnoza jest trudna bez znajomości typów pułapek
- Dla organizacji integrujących zewnętrzne narzędzia (np. [[Make.com]]) kluczowe jest, by suppressions były synchronizowane między systemami; każda integracja to potencjalna granica, na której suppresje mogą zginąć

## Zastosowanie

Wiedza przydatna przy konsultacjach z NGO, które zgłaszają nagły spadek dostarczalności emaili bez widocznej przyczyny — szczególnie po imporcie listy lub integracji nowego narzędzia. Framework 4 typów pułapek jest gotową mapą diagnostyczną do zastosowania w audycie email programu. Zasada provenance jest użyteczna w szkoleniach z RODO i dobrych praktyk zbierania danych kontaktowych.
