---
categories:
  - "Emails"
published: 2026-03-05
created: 2026-04-30
labels:
  - "Mateusz Chrobok"
relevance: wysoka
tags:
  - "trendy-AI"
  - "LLM"
  - "strategia-AI"
---

# Nie mówię „żegnaj", tylko „do zobaczenia" 👋

Newsletter Mateusza Chroboka z marca 2026 skupia się na przełomowym badaniu z ETH Zurich, [[Anthropic]] i MATS Research, które pokazuje, że anonimowość w internecie kosztuje teraz od 1 do 4 dolarów do złamania — za pomocą systemu ESRC opartego na [[LLM]]. Badacze połączyli blisko tysiąc kont na Hacker News z profilami LinkedIn przy 90% precyzji, osiągając skuteczność 500 razy wyższą niż klasyczne metody statystyczne. Konkluzja jest niepokojąca: "praktyczna anonimowość" — ta oparta na nieopłacalności, nie niemożliwości — właśnie przestała istnieć. W short newsach: efekt Streisand z cenzurą słowa "Microslop" przez Microsoft, rekomendacja EROD o nielegalności wymuszania rejestracji w sklepach, oraz ustawa stanu Waszyngton zakazująca wszczepania pracownikom mikrochipów.

## Frameworki i metody

- **System ESRC (Extract, Score, Rank, Cross-reference)** — czterostopniowa metoda deanonimizacji: (1) wyodrębnienie cech tożsamościowych z anonimowych postów (kraj, branża, hobby, wspomniane konferencje), (2) kodowanie w wektory, (3) przeszukanie bazy kandydatów, (4) rozszerzone łańcuchy rozumowania [[LLM]] do wskazania dopasowania

## Kluczowe dane

- Koszt deanonimizacji jednej osoby: 1–4 USD za profil, cały eksperyment poniżej 2000 USD
- Hacker News: ~1000 kont połączonych z LinkedIn przy 90% precyzji i 54% recall (pula 89 tys. użytkowników)
- Poprawa skuteczności vs. klasyczne metody statystyczne: 500-krotna
- Reddit (zamknięta grupa filmowa): 8,5% skuteczność przy 90% precyzji — ale dla użytkowników z ≥10 tytułami filmów skok do 48%

## Wnioski

- Każdy wpis w internecie — wzmianka o mieście, branży, hobby, konferencji — tworzy unikalny odcisk palca; im więcej piszesz, tym łatwiej Cię zidentyfikować, co dotyczy też przedstawicieli NGO aktywnych w mediach społecznościowych i na forach branżowych
- Wieloetapowe ataki [[LLM]] (każdy krok wygląda niewinnie, razem tworzą maszynę do deanonimizacji) to nowa klasa zagrożeń, przed którą filtry bezpieczeństwa modeli są nieskuteczne — warto uwzględnić to w szkoleniach z cyberbezpieczeństwa dla organizacji
- Rekomendacja EROD o przymusowych kontach w sklepach to praktyczna zmiana dla każdej organizacji prowadzącej sklep online — sprzedaż bez rejestracji powinna być domyślną opcją pod RODO

## Cytat

> "Zapytaj siebie — czy zespół sprytnych detektywów mógłby ustalić, kim jesteś, na podstawie Twoich postów? Jeśli tak, agenci LLM prawdopodobnie też mogą. A koszt tego z każdym miesiącem spada."

## Zastosowanie

Temat deanonimizacji przez [[LLM]] to gotowy case study do szkoleń AI dla NGO — pokazuje konkretne ryzyko związane z aktywnością w internecie i demitologizuje "bezpieczną anonimowość". Rekomendacja EROD jest praktycznie użyteczna dla organizacji prowadzących sklepy z gadżetami, cegiełkami czy kursami. Badanie ETH Zurich warto cytować w kontekście dyskusji o granicach możliwości obecnych modeli językowych.
