---
categories: Clippings
authors: ["[[Casey Crane]]"]
url: https://www.thesslstore.com/blog/how-to-set-up-bimi-and-a-mark-certificate-to-display-your-email-logo/
source: "[[Archives/2024-12-03 How to Set Up BIMI and a Mark Certificate to Display Your Email Logo|2024-12-03 How to Set Up BIMI and a Mark Certificate to Display Your Email Logo]]"
published: 2024-12-03
created: 2026-03-23
relevance: średnia
tags:
  - "digital-campaigning"
  - "content-marketing"
---

# How to Set Up BIMI and a Mark Certificate to Display Your Email Logo

BIMI (Brand Indicators for Message Identification) to standard pozwalający organizacjom wyświetlać logo marki w skrzynce odbiorcy jeszcze przed otwarciem wiadomości emailowej. Badania DMA z 2023 roku wskazują, że rozpoznawalność marki jest dla odbiorców kluczowym czynnikiem przy decyzji o otwarciu emaila, a widoczne logo nadawcy zajmuje trzecie miejsce wśród czynników wpływających na tę decyzję. Wdrożenie BIMI wymaga skonfigurowania rekordów SPF, DKIM i DMARC na domenie wysyłkowej, przygotowania logo w formacie SVG Tiny 1.2 oraz uzyskania certyfikatu Mark Certificate od zatwierdzonego urzędu certyfikacji. Artykuł prowadzi przez pełny, pięcioetapowy proces konfiguracji — od wymagań technicznych po rejestrację DNS.

## Frameworki i metody

Konfiguracja BIMI — 5 kroków:
1. **DMARC compliance** — skonfiguruj rekordy SPF i DKIM dla wszystkich usług wysyłkowych (np. [[Mailchimp]], [[Brevo]]), następnie wdróż DMARC najpierw w trybie monitorowania (`p=none`), potem enforcement (`p=quarantine` lub `p=reject`)
2. **Przygotowanie logo** — logo musi być plikiem SVG w formacie SVG Tiny 1.2 (profil PS), proporcje 1:1, maks. 32 KB, bez zewnętrznych linków i zbędnych elementów interaktywnych
3. **Zakup Mark Certificate** — Common Mark Certificate (CMC) dla logo bez znaku towarowego lub Verified Mark Certificate (VMC) dla zarejestrowanego znaku towarowego (VMC daje niebieski tick weryfikacji w Gmail); certyfikaty wystawiają wyłącznie DigiCert i Entrust
4. **Walidacja przez urząd certyfikacji** — organizacja przechodzi weryfikację: legalność podmiotu, kontrola domeny, własność logo
5. **Konfiguracja rekordu BIMI** — dodaj rekord TXT do DNS: `v=BIMI1; l=https://url/logo.svg; a=https://url/certyfikat.pem`

## Kluczowe dane

- Odbiorcy spędzają średnio 11 sekund na jednym emailu (DMA Email Consumer Tracking 2023)
- 3 na 5 odbiorców uznaje rozpoznawalność marki za główny czynnik decydujący o otwarciu emaila
- Logo marki to trzeci najważniejszy czynnik wpływający na decyzję o otwarciu wiadomości

## Wnioski

- Wdrożenie BIMI wymaga wcześniejszego skonfigurowania DMARC, co samo w sobie poprawia bezpieczeństwo i dostarczalność emaili — warto zrobić to niezależnie od BIMI, bo chroni domenę przed spoofingiem
- CMC jest dostępny dla organizacji bez zarejestrowanego znaku towarowego, więc większość NGO może wdrożyć wyświetlanie logo bez kosztownego procesu rejestracji marki
- Logo organizacji widoczne przed otwarciem emaila buduje zaufanie i zwiększa open rate — szczególnie ważne w kampaniach fundraisingowych i digital campaigningu

## Zastosowanie

Dla organizacji prowadzących regularne kampanie emailowe (fundraising, advocacy, newslettery) BIMI to konkretny sposób na profesjonalizację komunikacji i poprawę wskaźników otwarć bez zmiany treści. Wdrożenie jest jednorazowe i techniczne, ale artykuł daje wystarczająco szczegółową instrukcję krok po kroku. Przydatne przy doradztwie NGO w zakresie email marketingu i budowania wiarygodności marki w skrzynce odbiorcy.
