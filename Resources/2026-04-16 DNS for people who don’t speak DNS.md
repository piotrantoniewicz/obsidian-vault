---
categories:
  - Clippings
authors: ["[[Sara Cederberg]]"]
url: "https://www.civicshoutnewsletter.com/p/dns-for-people-who-don-t-speak-dns"
source: "[[Archives/2026-04-16 DNS for people who don’t speak DNS|2026-04-16 DNS for people who don’t speak DNS]]"
published: 2026-04-16
created: 2026-08-25
relevance: wysoka
tags:
  - "digital-campaigning"
  - "organizacje-społeczne"
---

# DNS for people who don’t speak DNS

Sara Cederberg tłumaczy bez żargonu, czym są rekordy [[SPF]], [[DKIM]] i [[DMARC]] i dlaczego decydują o dostarczalności maili. Jej główna teza: nie musisz być ekspertem od DNS, ale musisz wiedzieć dość, żeby zadać właściwe pytania konsultantowi lub webdeveloperowi i sprawdzić, czy podstawy są ogarnięte. Od 2024 roku [[Google]] i [[Yahoo]] egzekwują te wymagania wobec masowych nadawców, a [[Microsoft]] dołączył w maju 2025 — brak uwierzytelnienia to dziś nie zaniedbanie techniczne, tylko realne ryzyko, że kampania nie dotrze do skrzynek. Dla organizacji wysyłających newslettery i apele to fundament, na którym stoi cała reszta programu mailowego.

## Frameworki i metody

**Trzy rekordy DNS istotne dla poczty — metafory autorki:**

1. **[[SPF]] (Sender Policy Framework) — lista gości.** Deklaruje, które usługi mają prawo wysyłać maile w imieniu Twojej domeny. Każda platforma, z której wysyłasz, musi być w rekordzie. Jeśli usługi nie ma na liście, dostawcy skrzynek mogą uznać wiadomość za podejrzaną.

2. **[[DKIM]] (DomainKeys Identified Mail) — pieczęć woskowa.** Dodaje podpis cyfrowy do każdej wiadomości, dzięki czemu serwer odbiorcy weryfikuje, że treść nie została zmieniona po drodze. Klucz generuje zwykle platforma mailingowa — Twoim zadaniem jest opublikowanie go w DNS.

3. **[[DMARC]] — instrukcja dla bramkarza.** Spina SPF i DKIM i mówi dostawcom, co zrobić z wiadomością, która nie przeszła uwierzytelnienia. Trzy poziomy polityki: `none` (tylko monitorowanie), `quarantine` (do spamu), `reject` (blokada). Polityka `none` oznacza, że obserwujesz, ale nie chronisz.

**Jak sprawdzić stan wyjściowy:**
- Wpisz domenę w darmowe narzędzia [[MXToolbox]] i sprawdź rekordy SPF, DKIM i DMARC.
- Braki i błędne konfiguracje to punkt startowy naprawy.
- Zaplanuj przejście z `none` przez `quarantine` do `reject` — to warunek konieczny także dla wyświetlania logo w skrzynce przez [[BIMI]].

## Kluczowe dane
- Od 2024 r. [[Google]] i [[Yahoo]] wymagają SPF, DKIM i DMARC od nadawców wysyłających ponad 5000 maili dziennie
- [[Microsoft]] wprowadził analogiczne wymagania dla Outlook, Hotmail i Live.com w maju 2025

## Wnioski
- Uwierzytelnianie domeny przestało być opcją techniczną — to warunek wejścia do skrzynki u największych dostawców i element reputacji nadawcy.
- Polityka [[DMARC]] na poziomie `none` daje złudzenie bezpieczeństwa: raportuje nadużycia, ale ich nie blokuje; migracja do `quarantine` i `reject` powinna być zaplanowanym procesem, nie jednorazowym przełącznikiem.
- Rekordy DNS załatwiają tylko dostarczenie wiadomości — o tym, co dzieje się dalej, decyduje jakość bazy adresowej.

## Cytat
> Nie musisz zostać ekspertem od DNS. Musisz wiedzieć tyle, żeby zadać właściwe pytania i upewnić się, że podstawy są zrobione.

## Zastosowanie
Gotowy materiał na moduł techniczny w kursie mailowym „Fundraising z AI" — trzy metafory (lista gości, pieczęć, bramkarz) tłumaczą SPF/DKIM/DMARC osobom bez zaplecza IT. W pracy konsultacyjnej z organizacjami warto zacząć każdy audyt komunikacji mailowej od sprawdzenia domeny w [[MXToolbox]] — to pięciominutowa diagnoza, która często wyjaśnia spadki otwarć. Dla klientów prowadzących kampanie email-to-target migracja DMARC do `reject` to konkretna rekomendacja z mierzalnym efektem.
