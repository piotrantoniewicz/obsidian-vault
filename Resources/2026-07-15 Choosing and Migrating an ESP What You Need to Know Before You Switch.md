---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/choosing-and-migrating-an-esp-what-nobody-tells-you-before-you-switch"
source: "[[Archives/2026-07-15 Choosing and Migrating an ESP What You Need to Know Before You Switch|2026-07-15 Choosing and Migrating an ESP What You Need to Know Before You Switch]]"
published: 2026-07-15
created: 2026-07-16
relevance: wysoka
tags:
  - "digital-campaigning"
  - "automatyzacja"
  - "strategia-organizacji"
---

# Choosing and Migrating an ESP: What You Need to Know Before You Switch

[[Beth O'Malley]] opisuje, dlaczego migracje platform e-mailowych (ESP) tak często się psują, mimo że sprzedaż i wdrożenie wyglądają gładko. Główna teza: problem zaczyna się już na etapie wyboru platformy — demo pokazuje idealne warunki, a nie to, jak system zachowa się z realnymi, niedoskonałymi danymi organizacji. Autorka rozkłada migrację na sześć faz, które muszą następować w ściśle określonej kolejności, i wskazuje dziesięć najczęstszych, powtarzalnych błędów. To praktyczny przewodnik dla każdego, kto planuje zmianę systemu e-mail marketingowego lub CRM.

## Frameworki i metody

**Sześć faz migracji ESP:**
1. **Audyt przedmigracyjny** — eksport danych historycznych, benchmarków (open rate, click rate, unsubscribe rate), test deliverability, sprawdzenie rekordów SPF/DKIM/DMARC przed przenosinami.
2. **Zrozumienie integracji przed budową** — ustalenie, czy integracja z CRM jest real-time czy działa na synchronizacji cyklicznej; zmapowanie wszystkich formularzy i połączeń Zapier.
3. **Migracja danych we właściwej kolejności** — najpierw listy suppresji (unsubskrybowani, hard bounce, spam complaints), dopiero potem aktywni kontakci; wcześniejsze przygotowanie dokumentu mapowania pól.
4. **Warm-up nowego IP** — stopniowe zwiększanie wolumenu wysyłek z nowej platformy (8–12 tygodni), przy utrzymaniu starego ESP równolegle.
5. **Monitoring po go-live** — codzienna kontrola deliverability i działania automatyzacji.
6. **Wygaszenie starego ESP** — dopiero po min. 8 (najlepiej 12) tygodniach czystych danych deliverability z nowej platformy.

## Kluczowe dane
- Standardowy warm-up IP trwa 8–12 tygodni do osiągnięcia pełnego wolumenu.
- W jednym z opisanych przypadków placement w Outlooku spadł poniżej 60% w ciągu 10 dni po pominięciu warm-upu, a odbudowa zajęła 3 miesiące.
- Minimum 8 tygodni (docelowo 12) czystych danych z nowej platformy przed anulowaniem starego kontraktu ESP.

## Wnioski
- "Plug and play" w sprzedaży ESP zwykle oznacza, że integracja istnieje technicznie — nie, że będzie działać w czasie rzeczywistym z danymi organizacji; różnica między synchronizacją a integracją real-time decyduje o tym, czy zaplanowane [[automatyzacja|automatyzacje]] w ogóle zadziałają.
- Kolejność importu danych ma znaczenie prawne, nie tylko techniczne — import aktywnych kontaktów przed listami suppresji tworzy okno, w którym automatyzacja może wysłać wiadomość do osoby, która się wypisała (ryzyko zgodności z RODO/PECR).
- Migracja to nie projekt techniczny z jedną datą go-live, tylko wieloetapowy proces organizacyjny wymagający audytu, sekwencjonowania i cierpliwości — skróty na każdym etapie odbijają się później.

## Cytat
> Przenoszenie się na nowy adres IP, gdy reputacja wysyłkowa jest już nadszarpnięta, jest jak przeprowadzka, by uciec przed złą historią kredytową — dług i tak jedzie z tobą.

## Zastosowanie
Przydatny checklist przy doradzaniu organizacjom NGO planującym zmianę narzędzia do e-mail marketingu lub integrację z CRM — zwłaszcza lista pytań do zadania dostawcy przed podpisaniem umowy oraz sekwencja importu danych (suppresje przed aktywnymi kontaktami).
