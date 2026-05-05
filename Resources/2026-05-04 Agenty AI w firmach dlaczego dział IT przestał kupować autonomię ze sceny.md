---
categories: Clippings
authors: ["[[Mateusz Wojdalski]]"]
url: https://devstockacademy.pl/blog/branza-it-i-nowe-technologie/agenty-ai-firmy-kryzys-zaufania-microsoft-ai-tour-2026/
source: "[[Archives/2026-05-04 Agenty AI w firmach dlaczego dział IT przestał kupować autonomię ze sceny|2026-05-04 Agenty AI w firmach dlaczego dział IT przestał kupować autonomię ze sceny]]"
published: 2026-05-04
created: 2026-05-05
relevance: wysoka
tags:
  - "strategia-AI"
  - "automatyzacja"
  - "narzędzia-AI"
---

# Agenty AI w firmach — dlaczego dział IT przestał kupować autonomię ze sceny

Artykuł opisuje zjawisko "agent washing" — przemianowywania starych narzędzi (asystentów konwersacyjnych, chatbotów, RPA) na "agenty AI" bez realnych zmian architektonicznych, wyłącznie po to by uzasadnić wyższą cenę. Na przykładzie [[Microsoft]] AI Tour w Zurychu (kwiecień 2026) autor pokazuje, że enterprise klienci coraz częściej rozpoznają ten chwyt. [[Gartner]] prognozuje, że ponad 40% projektów z agentami AI zostanie skasowanych do 2027 roku — nie z powodu słabych modeli, lecz braku wartości biznesowej, rosnących kosztów obliczeniowych i niewystarczającej obsługi wyjątków w produkcji.

## Frameworki i metody
- **4 elementy odróżniające demo od produkcji**: (1) obsługa wyjątków — co się dzieje gdy użytkownik odpowie inaczej niż przewidziano w skrypcie; (2) integracje — agent musi działać z istniejącym systemem CRM, bazą klientów i kalendarzami, nie obok nich; (3) ślad audytowy — dział zgodności musi wiedzieć kto zatwierdził daną decyzję; (4) koszty — koszt jednostkowy wywołania agenta w produkcji, nie w środowisku testowym
- **Test 3 pytań dla kupującego**: poproś dostawcę o (1) konkretny case z audytowalnym dziennikiem decyzji, (2) koszt jednostkowy operacji w produkcji, (3) mechanizm wycofania zmiany gdy agent się myli — jeśli odpowiada slajdami zamiast linkiem do dokumentacji, masz odpowiedź na temat dojrzałości produktu

## Kluczowe dane
- [[Gartner]]: ponad 40% projektów z agentami AI zostanie skasowanych do końca 2027 roku
- Szacunkowy rynek agentów AI: 47 mld USD do 2030 roku
- Tylko ~130 firm na rynku ma faktycznie autonomiczne systemy AI — reszta to chatboty z ulepszonym promptem lub RPA z nowym brandingiem

## Wnioski
- "Agent washing" to rebranding starych produktów bez zmian architektonicznych — klient enterprise zaczyna to rozpoznawać i zamiast pytać o autonomię, pyta o ROI i konkretne oszczędności
- Ponad 90% agentów wdrożonych w 2024–2025 roku przestało działać nie przez błędy modelu, lecz przez brak przygotowania na wyjątki, integracje z legacy systemami i kontrolę kosztów
- Realną wartość przynosi automatyzacja z audytowalnym dziennikiem decyzji i jasnym kosztem jednostkowym — nie "autonomia z keynote'a"

## Cytat
> Klient nie chce kupić autonomii ze sceny. Chce kupić rachunek, który spada w dół.

## Zastosowanie
Artykuł dostarcza języka i argumentów przydatnych w rozmowach z NGO rozważającymi wdrożenia AI — szczególnie gdy organizacje pytają o gotowe agenty. Test 3 pytań można wbudować w moduł oceny ofert dostawców AI w szkoleniach dobryai.pl lub w kurs "Fundraising z AI".
