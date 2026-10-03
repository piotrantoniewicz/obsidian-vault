---
type: "Web"
authors:
url: "https://aininjas.pl/priv/d599ecfd-f26a-47fa-992c-2195f921cc7b/"
published:
created: 2026-10-02
tags:
  - "prompt-engineering"
  - "szkolenia-AI"
---


![Schemat promptu](https://aininjas.pl/fundamentyai/ninja-blueprint.png)

“Garbage in, garbage out” (Śmieci na wejściu, śmieci na wyjściu) — to zasada stara jak informatyka, ale nigdy nie była tak aktualna jak przy AI. Jeśli Twoje polecenie jest niejasne, odpowiedź będzie przeciętna.

Aby uzyskać wybitne wyniki, musimy przestać “rozmawiać” z AI, a zacząć je “programować” językiem naturalnym. Najlepszym sposobem na to jest używanie struktury. Poznaj Framework **R-F-K-A**.

---

## R - Rola (Role)

**Kim ma być model?**

Deklaracja roli to najprostszy i **najbardziej niedoceniany** sposób na poprawę jakości odpowiedzi. Kiedy mówisz modelowi, kim jest, aktywujesz konkretne wzorce z jego danych treningowych i narzucasz styl komunikacji.

### Dlaczego rola działa?

Model został wytrenowany na miliardach tekstów pisanych przez różne osoby: lekarzy, prawników, programistów, poetów. Gdy określasz rolę, mówisz mu: *“Odpowiadaj tak, jak odpowiadałyby osoby z tej grupy w danych treningowych”*.

### Jak definiować rolę?

**Poziom 1 - Podstawowy (zawód):**

```plaintext
Działaj jako doświadczony copywriter.
```

**Poziom 2 - Szczegółowy (zawód + specjalizacja + doświadczenie):**

```plaintext
Działaj jako doświadczony copywriter specjalizujący się w branży SaaS,
który przez 10 lat pisał teksty dla startupów technologicznych.
```

**Poziom 3 - Kontekstowy (zawód + specjalizacja + perspektywa + ograniczenia):**

```plaintext
Działaj jako doświadczony copywriter SaaS, który właśnie zakończył
kampanię dla firmy podobnej do mojej. Wiesz, co działa na rynku B2B,
ale unikasz korporacyjnego żargonu. Preferujesz bezpośredni, ludzki ton.
```

### Przykłady ról dla różnych zadań

| Zadanie | Słaba rola | Dobra rola |
| --- | --- | --- |
| Analiza umowy | ”Jesteś prawnikiem" | "Jesteś radcą prawnym specjalizującym się w umowach B2B z 15-letnim doświadczeniem. Zwracasz uwagę na ryzyka dla klienta.” |
| Nauka programowania | ”Jesteś programistą" | "Jesteś cierpliwym mentorem programowania, który tłumaczy koncepcje używając prostych analogii. Zawsze zaczynasz od podstaw i budujesz zrozumienie krok po kroku.” |
| Feedback do tekstu | ”Oceń tekst" | "Jesteś surowym ale sprawiedliwym redaktorem naczelnym, który dba o klarowność przekazu. Wskazujesz konkretne problemy i proponujesz rozwiązania.” |

### Anti-pattern: Rola “supermana”

Unikaj dawania modeli zbyt wielu cech naraz:

```plaintext
❌ "Jesteś najlepszym ekspertem na świecie w marketingu, psychologii,
sprzedaży, copywritingu i analizie danych, który zawsze daje
genialne odpowiedzi."
```

Zbyt wiele superlatyw rozmywa fokus. Lepiej:

```plaintext
✅ "Jesteś ekspertem od copywritingu z doświadczeniem w psychologii
sprzedaży. Skupiasz się na konwersji."
```

---

## F - Format (Format)

**Jak ma wyglądać wynik?**

Nigdy nie zostawiaj formatowania przypadkowi. Model domyślnie generuje *cokolwiek wydaje mu się pasować*. Bądź precyzyjny.

### Dlaczego format jest ważny?

1. **Oszczędza czas** - nie musisz przekształcać odpowiedzi
2. **Poprawia jakość** - wymusza strukturę myślenia
3. **Ułatwia przetwarzanie** - szczególnie przy automatyzacji

### Rodzaje formatów do wyboru

**Tekstowe:**

- Akapit / esej
- Lista punktowana
- Lista numerowana
- Tabela
- FAQ (pytanie-odpowiedź)
- Dialog / scenariusz

**Strukturalne:**

- JSON
- XML
- Markdown
- YAML
- CSV

**Długość:**

- Liczba słów: “Odpowiedź w maksymalnie 100 słowach”
- Liczba punktów: “Podaj dokładnie 5 argumentów”
- Liczba zdań: “Jedno zdanie”

### Precyzyjne określanie formatu

**Słabo:**

```plaintext
Zrób listę.
```

**Dobrze:**

```plaintext
Wynik przedstaw jako numerowaną listę 5-7 punktów.
Każdy punkt: maksymalnie jedno zdanie, zaczynające się od czasownika.
```

**Bardzo dobrze (dla tabeli):**

```plaintext
Przedstaw wynik jako tabelę z 4 kolumnami:
| Narzędzie | Cena miesięczna | Główna zaleta | Główna wada |

Posortuj od najtańszego. Dodaj na końcu wiersz z podsumowaniem.
```

### Przykład: Ten sam temat, różne formaty

**Prompt:** “Opisz zalety pracy zdalnej”

**Format 1 - Lista:**

```plaintext
Format: Lista 5 punktów, każdy punkt w jednym zdaniu.
```

Wynik:

1. Eliminacja dojazdów oszczędza 2+ godziny dziennie.
2. Elastyczne godziny pozwalają dostosować pracę do życia.
3. Własne środowisko zwiększa komfort i produktywność. …

**Format 2 - Tabela:**

```plaintext
Format: Tabela z kolumnami [Zaleta] [Dla kogo kluczowa] [Potencjalne ryzyko]
```

Wynik: | Zaleta | Dla kogo kluczowa | Potencjalne ryzyko | | Brak dojazdów | Rodzice, osoby z daleka od biura | Brak ruchu, izolacja | | Elastyczność | Freelancerzy, “sowy nocne” | Rozmycie granic praca/życie |

---

## K - Kontekst (Context)

**Co model musi wiedzieć, żeby wykonać zadanie?**

To tutaj większość osób popełnia największy błąd - dają **za mało informacji**. Model nie siedzi w Twojej głowie. Nie zna Twojej firmy, Twoich klientów ani Twojego celu.

### Złota zasada kontekstu

> Podaj wszystko, co musiałbyś powiedzieć nowemu pracownikowi w pierwszy dzień, żeby mógł wykonać to zadanie.

### Co powinien zawierać kontekst?

**1\. Odbiorca (Kto to przeczyta/użyje?)**

```plaintext
❌ "Napisz opis produktu"
✅ "Napisz opis produktu dla programistów seniorów,
którzy szukają narzędzi do automatyzacji testów.
Nie tłumacz podstawowych pojęć jak CI/CD."
```

**2\. Cel (Po co to robimy?)**

```plaintext
❌ "Streść ten artykuł"
✅ "Streść ten artykuł tak, żebym mógł zdecydować
czy warto go przeczytać w całości. Skup się na
głównej tezie i nowatorskich wnioskach."
```

**3\. Ograniczenia (Czego unikać?)**

```plaintext
❌ "Napisz email"
✅ "Napisz email. Unikaj słów: 'innowacyjny', 'synergia', 'dynamiczny'.
Ton: profesjonalny ale nie korporacyjny. Bez wykrzykników."
```

**4\. Tło (Co już wiem/mam?)**

```plaintext
❌ "Pomóż mi z prezentacją"
✅ "Przygotowuję prezentację dla zarządu (10 osób, głównie finansiści)
o wdrożeniu AI w obsłudze klienta. Mam już dane o redukcji kosztów
o 30%. Potrzebuję pomocy z argumentacją ROI."
```

### Szablon kontekstu (do kopiowania)

```plaintext
KONTEKST:
- Odbiorca: [kto przeczyta/użyje wynik]
- Cel: [co chcę osiągnąć]
- Tło: [co już wiem/mam]
- Ograniczenia: [czego unikać, limity]
- Ton: [formalny/nieformalny/techniczny/prosty]
```

### Ile kontekstu to za dużo?

Nowoczesne modele radzą sobie z długim kontekstem, ale istnieją granice:

- **Zbyt mało** = generyczne odpowiedzi
- **Zbyt dużo** = model może się “zgubić” w detalach

**Heurystyka:** Jeśli Twój kontekst jest dłuższy niż 500 słów, rozważ podzielenie zadania na części lub użycie podsumowania.

---

## A - Akcja (Action)

**Co dokładnie ma się wydarzyć?**

Akcja to konkretne polecenie wykonawcze. To tutaj określasz **co** model ma zrobić (rola mówi *kim* ma być, format mówi *jak* ma wyglądać wynik).

### Zasady dobrej akcji

**1\. Używaj czasowników operacyjnych**

| Słabe czasowniki | Mocne czasowniki |
| --- | --- |
| Zrób coś z tym | Przeanalizuj, Porównaj, Przekształć |
| Pomóż mi z… | Napisz, Stwórz, Wygeneruj |
| Powiedz mi o… | Wyjaśnij, Opisz, Zdefiniuj |
| Zajmij się… | Sprawdź, Popraw, Ulepsz |

**2\. Określ sekwencję kroków (jeśli zadanie jest złożone)**

```plaintext
❌ "Sprawdź ten tekst"

✅ "1. Przeczytaj tekst i zidentyfikuj 3 główne problemy
   2. Dla każdego problemu zaproponuj konkretną poprawkę
   3. Przepisz jeden akapit jako przykład
   4. Oceń poziom trudności poprawek (łatwe/średnie/trudne)"
```

**3\. Bądź konkretny co do oczekiwanego wyniku**

```plaintext
❌ "Daj mi pomysły na marketing"

✅ "Wygeneruj 10 konkretnych pomysłów na posty LinkedIn
   promujące kurs online o AI. Każdy pomysł:
   - Hook (pierwsze zdanie przyciągające uwagę)
   - Główna wartość dla czytelnika
   - Call-to-action"
```

---

## Pełny przykład: Zamiana słabego prompta w profesjonalny

### Słaby prompt

```plaintext
Napisz mi plan treningowy.
```

**Wynik:** Generyczny plan (rozgrzewka, bieganie, pompki), bezwartościowy dla konkretnej osoby.

### Prompt R-F-K-A

```plaintext
ROLA:
Działaj jako certyfikowany trener personalny specjalizujący się
w treningu siłowym dla osób po 40. roku życia z problemami z kręgosłupem.

KONTEKST:
Jestem mężczyzną, 42 lata, praca siedząca (8h dziennie przy biurku).
Mam dostęp do siłowni, ale mam tylko 45 minut 3 razy w tygodniu.
Mój cel to redukcja bólu pleców i lekka budowa mięśni.
Nie mam kontuzji, ale lekarz zalecił unikanie mocnego obciążania kręgosłupa.

FORMAT:
Stwórz plan w formie tabeli na 3 dni treningowe (Trening A, B, C).
Kolumny: [Ćwiczenie] [Serie x powtórzenia] [Uwagi bezpieczeństwa]
Na końcu dodaj listę 3 ćwiczeń, których absolutnie muszę unikać.

AKCJA:
Przygotuj plan uwzględniający moje ograniczenia czasowe i zdrowotne.
Zacznij od rozgrzewki specyficznej dla osób z problemami kręgosłupa.
```

**Wynik:** Spersonalizowany plan, za który w realnym świecie trzeba by zapłacić specjaliście.

---

## Ćwiczenie praktyczne: Napraw Prompt

**Słaby prompt:**

```plaintext
Wymyśl nazwę dla mojej firmy.
```

**Twoje zadanie - przepisz go używając R-F-K-A:**

1. **Rola:** Kim powinien być model? (np. ekspert brandingu, specjalista od nazewnictwa)
2. **Format:** Jak ma wyglądać wynik? (lista? z opisami domen? z uzasadnieniem?)
3. **Kontekst:** Co model musi wiedzieć? (branża? wartości? grupa docelowa? styl?)
4. **Akcja:** Co dokładnie ma zrobić? (ile nazw? czy sprawdzić dostępność domen?)

**Przykładowe rozwiązanie:**

```plaintext
ROLA: Jesteś ekspertem od nazewnictwa marek z doświadczeniem w branży tech.

KONTEKST: Zakładam firmę oferującą kursy online o AI dla przedsiębiorców.
Grupa docelowa: właściciele małych firm 35-50 lat, którzy boją się zostać w tyle.
Wartości: przystępność, praktyczność, brak technobełkotu.
Styl: nowoczesny ale nie "zimny", raczej przyjazny.
Konkurencja używa nazw jak "AI Academy", "DataSchool" - chcę się wyróżnić.

FORMAT: Lista 10 nazw. Dla każdej:
- Nazwa
- Dostępność domeny .pl i .com (oznacz ✓ lub ✗)
- Jedno zdanie uzasadnienia

AKCJA: Wygeneruj nazwy, które są łatwe do wymówienia po polsku,
zapamiętania i nie wymagają tłumaczenia. Unikaj akronimów.
```

Wykonaj to w swoim narzędziu AI i porównaj jakość odpowiedzi!

---

## Materiały dodatkowe

- [Prompting Guide - Techniques](https://www.promptingguide.ai/techniques) - Zaawansowane techniki promptowania
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - Oficjalny poradnik OpenAI
- [Anthropic Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering) - Poradnik od twórców Claude
- [Learn Prompting](https://learnprompting.org/) - Darmowy kurs promptowania