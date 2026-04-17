---
categories: Clippings
authors: ["[[Marzena Kacprowicz]]"]
url: https://sektor3-0.pl/blog/automatyzacja-zadan-jak-przyspieszyc-zbieranie-faktur/
source: "[[Archives/2024-11-19 Automatyzacja zadań. Jak przyspieszyć zbieranie faktur z załączników i tworzenie zestawień|2024-11-19 Automatyzacja zadań. Jak przyspieszyć zbieranie faktur z załączników i tworzenie zestawień]]"
published: 2024-11-19
created: 2026-03-24
relevance: wysoka
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "organizacje-społeczne"
---

# Automatyzacja zadań. Jak przyspieszyć zbieranie faktur z załączników i tworzenie zestawień

Artykuł [[Sektor 3.0]] autorstwa Marzeny Kacprowicz to praktyczny tutorial krok po kroku: jak zbudować w [[Make.com]] automatyzację pobierającą faktury z Gmaila, zapisującą je na Dysku Google i uzupełniającą zestawienie w Google Sheets — za pomocą gotowego szablonu, bez pisania kodu, w darmowym planie. Autorka podkreśla, że ten sam schemat (e-mail z załącznikiem → dysk → arkusz) można zastosować do dziesiątek innych procesów w NGO: konkursów, zgód RODO, kart obiegowych, rachunków. To klasyczny przykład automatyzacji niskokosztowej, którą każda organizacja może wdrożyć samodzielnie.

## Frameworki i metody
- **5-krokowy proces budowania automatyzacji w [[Make.com]]**:
  1. Stwórz folder na Dysku Google do przechowywania faktur
  2. Stwórz arkusz Google Sheets z kolumnami: data wpływu, nadawca, e-mail nadawcy, nazwa pliku, link do faktury
  3. Skonfiguruj automatyzację w Make: użyj gotowego szablonu „Save Gmail emails and attachments to Google Sheets and Google Drive"; połącz konto Google; ustaw filtr `has:attachment label:faktura`
  4. Przetestuj automatyzację (Run Once) na przykładowym mailu
  5. Ustaw częstotliwość uruchamiania (np. raz dziennie, by nie przekroczyć 1000 operacji/mies. w darmowym planie)
- **Schemat ogólny** (zastosowanie wielokrotne): trigger (etykieta e-mail) → pobieranie załącznika → zapis na dysku → zapis metadanych w arkuszu
- **Inne zastosowania**: zbieranie prac konkursowych, zgód na wizerunek, kart obiegowych, rachunków cyklicznych

## Kluczowe dane
- Darmowy plan [[Make.com]]: 1000 operacji/miesiąc
- Koszt 1 maila z 1 załącznikiem: 4 operacje; przy 1 uruchomieniu dziennie to ~120 operacji/miesiąc (dobrze w darmowym planie)

## Wnioski
- [[Make.com]] z gotowymi szablonami obniża barierę wejścia do automatyzacji dla NGO praktycznie do zera — brak kodowania, gotowy szablon, darmowy plan wystarczający do prostych procesów.
- Automatyzacja oparta na etykietach Gmail to wzorzec, który da się powielić dla wielu typów dokumentów przepływających przez skrzynkę organizacji — jeden raz skonfigurowany oszczędza godziny pracy miesięcznie.
- Artykuł może być podstawą ćwiczenia praktycznego na warsztatach z automatyzacji dla NGO — prosty, konkretny problem + gotowe rozwiązanie krok po kroku.

## Zastosowanie
Automatyzacja faktur to dobry punkt wejścia do rozmowy o [[Make.com]] z organizacjami, które boją się „automatyzacji" jako czegoś technicznego — konkretny, bliski życiu przykład. Warto zbudować na tym module bibliotekę szablonów automatyzacji dla NGO jako produkt/usługę w ramach dobryai.pl. Schemat Gmail → Dysk → Arkusz można rozszerzyć o AI (np. wyciąganie danych z faktury przez [[Claude]]) jako kolejny krok w bardziej zaawansowanym wariancie.
