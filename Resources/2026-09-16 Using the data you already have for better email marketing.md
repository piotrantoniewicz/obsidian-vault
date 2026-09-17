---
categories:
  - Clippings
authors: ["[[Beth O'Malley]]"]
url: "https://weareastral.co.uk/thevault/using-the-data-you-already-have-derived-properties-predictive-insights-and-where-ai-really-helps?utm_medium=email&_hsenc=p2ANqtz-8iubLJTbEYvn-ShbH6atWDwsFR9fbmst0Vk0IxtG1LmU4aZgoa2pQJxF1ABFDhaSsMjDRsyQnxiYUe8zxNqLtvuyVg9p6cTHUx72kp6irF63V3xCI&_hsmi=145913605&utm_content=145862482&utm_source=hs_email"
source: "[[Archives/2026-09-16 Using the data you already have for better email marketing|2026-09-16 Using the data you already have for better email marketing]]"
published: 2026-09-16
created: 2026-09-17
relevance: średnia
tags:
  - "narzędzia-AI"
  - "content-marketing"
  - "automatyzacja"
---

# Using the data you already have for better email marketing

Autorka rozróżnia trzy warstwy danych o klientach: zebrane (surowe fakty), wyprowadzone (obliczone z surowych — tu jest cała wartość segmentacji) i predykcyjne (co się prawdopodobnie stanie). Główna teza: większość organizacji nie ma problemu ze zbieraniem danych, ale z ich przetwarzaniem na coś użyteczne — a AI dopiero teraz otworzyło tę warstwę firmom bez zespołu data science. Artykuł ostrzega równocześnie, że predykcje wyglądają jak fakty, choć są hipotezami, i że błędna predykcja rozesłana masowo szkodzi reputacji nadawcy, nie tylko konkretnej kampanii.

## Frameworki i metody

**Trzy warstwy danych:**
1. **Zebrane** — to, co klient powiedział lub co się wydarzyło (zakup, pole formularza, kliknięcie). Faktyczne, ale samo w sobie mało użyteczne.
2. **Wyprowadzone** — obliczone z surowych danych (średnia wartość zamówienia, dni od ostatniego zakupu względem własnej normy klienta, afinność kategorii, zależność od rabatów, etap cyklu życia). To tu leży cała wartość segmentacyjna.
3. **Predykcyjne** — co się prawdopodobnie stanie (skłonność do zakupu, ryzyko odejścia, ryzyko reklamacji). Historycznie wymagało zespołu data science.

**Cztery zastosowania AI powyżej samego pisania treści:**
1. Zamiana wolnego tekstu (powody rejestracji, zgłoszenia supportowe, odpowiedzi na maile, powody rezygnacji, notatki ze sprzedaży) w ustrukturyzowane właściwości do segmentacji.
2. Klastrowanie — szukanie segmentów, których nikt nie przewidział, zamiast dzielenia klientów według z góry założonej hipotezy.
3. Scoring skłonności per osoba — używany głównie do wykluczeń (np. z kampanii dla osób o wysokiej skłonności do reklamacji), nie do celowania.
4. Predykcja czasu per osoba (np. indywidualny rytm uzupełniania zapasów) zamiast jednego interwału dla całej kategorii.

**Kolejność wdrożenia:** 1) zinwentaryzować dane, 2) oznaczyć każde pole jako zebrane/wyprowadzone/predykcyjne/martwe, 3) naprawić dane u podstawy (duplikaty, weryfikacja), 4) zbudować 3 właściwości wyprowadzone, nie 30, 5) sklasyfikować wolny tekst (zaczynając od powodów rejestracji), 6) dodać jedną predykcję i użyć jej do wykluczenia, 7) oznaczyć pochodzenie każdego pola i przypisać właściciela, 8) porównywać predykcje z rzeczywistością kwartalnie.

## Wnioski
- Segmentacja oparta wyłącznie na danych zebranych (kategoria produktu, data zakupu) słabo działa — realna wartość jest w danych wyprowadzonych, czyli policzonych z surowych.
- Predykcja wygląda jak fakt, bo przychodzi jako liczba — każda właściwość predykcyjna potrzebuje widocznego poziomu ufności (wysoki/średni/nieznany), inaczej ryzyko złego targetowania na dużą skalę staje się problemem z reputacją nadawcy, nie tylko z celnością kampanii.
- Zasada „nie przewiduj tego, o co możesz prostu zapytać" — pytać tam, gdzie pytanie jest naturalne, wyprowadzać tam, gdzie pytanie byłoby nachalne, przewidywać tylko tam, gdzie żadne z powyższych nie działa.

## Zastosowanie
Przydatne przy pracy z klientami NGO nad email marketingiem i CRM — zamiast rekomendować zbieranie kolejnych pól w formularzach, można od razu zaproponować audyt istniejących danych (zgłoszenia, odpowiedzi na maile, notatki) i klasyfikację ich AI na potrzeby segmentacji. Framework trzech warstw (zebrane/wyprowadzone/predykcyjne) to gotowy język do rozmowy z klientem o tym, dlaczego "więcej danych" nie rozwiązuje problemu personalizacji.
