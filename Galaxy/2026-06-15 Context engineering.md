---
type: concept
tags:
  - context-engineering
  - LLM
  - narzędzia-AI
created: 2026-06-15
updated: 2026-06-26
relevance: wysoka
sources:
  - "[[2025-09-29 Effective context engineering for AI agents]]"
  - "[[2025-11-26 The Ultimate Guide to Context Engineering for PMs]]"
  - "[[2025-07-28 Beyond Prompts How Context Engineering Could Revolutionize Your Nonprofit AI Workflows]]"
  - "[[2026-05-25 Harness, Scaffold, and the AI Agent Terms Worth Getting Right]]"
  - "[[2026-03-29 Przestań promptować... zacznij delegować]]"
  - "[[2026-02-01 🧠 czas na mózg agenta AI! 3-6]]"
  - "[[2026-05-22 The One AI Writing Hack Nobody Talks About.]]"
  - "[[2026-06-20 Piotr, zero razy tysiąc to dalej... zero]]"
  - "[[2026-06-24 How a Former NYU Professor Uses Claude Code]]"
---

# Context engineering (projektowanie kontekstu)

Context engineering to dyscyplina **świadomego doboru wszystkich tokenów trafiających do modelu w danym momencie** — nie tylko treści promptu, ale całego stanu: instrukcji systemowych, opisów narzędzi, historii rozmowy, pobranej wiedzy i danych zewnętrznych. [[Anthropic]] opisuje ją jako naturalną ewolucję prompt engineeringu: prompt engineering pisze *instrukcję*, context engineering zarządza *całym oknem*. Przewodnia zasada brzmi: znaleźć **najmniejszy możliwy zestaw tokenów o wysokim sygnale**, który maksymalizuje prawdopodobieństwo pożądanego zachowania. Sens praktyczny jest podwójny — jakość outputu [[LLM]] zależy dziś bardziej od jakości kontekstu niż od wyboru modelu (zmiana modelu bez poprawy kontekstu rzadko cokolwiek zmienia), a kontekst jest **zasobem skończonym o malejących przychodach krańcowych**: każdy zbędny token uszczupla „budżet uwagi" modelu. To pojęcie-parasol, pod którym [[2026-06-14 RAG|RAG]] jest jednym (retrieval-owym) szczególnym przypadkiem.

---

## Kluczowe mechanizmy

**1. Kontekst to skończony budżet — context rot**
Wraz ze wzrostem długości okna zdolność modelu do precyzyjnego wyszukania właściwej informacji **maleje** — zjawisko zwane *context rot*, dotyczące wszystkich modeli, choć z różną intensywnością. Konsekwencja jest kontrintuicyjna: celem nie jest *maksymalizacja* ilości dostarczonej informacji, lecz **minimalizacja szumu**. Więcej kontekstu bywa gorsze niż mniej. Dlatego context engineering to ciągła kuracja — faza doboru powtarza się przy *każdym* wywołaniu modelu, nie raz na początku.

**2. Anatomia dobrego kontekstu — „goldilocks zone"**
[[Anthropic]] dzieli stan na warstwy, każdą z własną zasadą:
- **System prompt** w strefie złotego środka — nie za szczegółowy (kruchy, przeładowany regułami na każdy edge case), nie za ogólny (brak konkretnych sygnałów). Optimum: dość konkretny, by kierować zachowaniem, dość elastyczny, by model działał samodzielnie.
- **Narzędzia** — minimalny działający zestaw, bez nakładających się funkcji, opisy jednoznaczne i token-efektywne.
- **Przykłady** — kanoniczne, reprezentatywne wzorce zamiast listy wyjątków („pictures worth a thousand words").

**3. Warstwowość: kontekst budowany przyrostowo**
[[LLM]] nie inferuje kontekstu sam — nie wie, kim jest użytkownik, co robił przed chwilą, które dokumenty są istotne ani jakie reguły obowiązują. Na przykładzie asystenta mailowego widać, jak każda dodana warstwa skokowo podnosi jakość: ostatnia wiadomość → cały wątek → wątek + [[CRM]] → + ton marki → + historia relacji = output gotowy do wysyłki. Sześć warstw, które trzeba dostarczyć *explicite*: tożsamość użytkownika, historia działań, istotne dokumenty, dane systemowe, reguły biznesowe, relacje między encjami.

**4. Techniki dla zadań długodystansowych (long-horizon)**
Gdy zadanie przekracza pojemność okna, kontekstem trzeba aktywnie zarządzać:
- **Compaction** — podsumowanie kontekstu bliskiego granicy do nowego okna; zachowuje decyzje, niezrealizowane zadania i szczegóły implementacji, usuwa zbędne wyniki narzędzi. Bezpieczna forma minimalna: czyszczenie starych tool outputs.
- **Structured note-taking** — agent zapisuje notatki *poza* oknem (plik `NOTES.md`, lista zadań) i wczytuje je na żądanie. Pamięć długoterminowa zewnętrzna vs krótkoterminowa w oknie.
- **Sub-agent architectures** — wyspecjalizowane [[2026-06-14 RAG|subagenty]] eksplorują dziesiątki tysięcy tokenów z czystym kontekstem i zwracają skondensowane podsumowanie (1000–2000 tokenów) do agenta głównego. To nie tylko obejście limitu, ale lepszy *separation of concerns*.

**5. Just-in-time retrieval — leniwe ładowanie kontekstu**
Zamiast ładować wszystkie dane z góry, agent przechowuje **lekkie identyfikatory** (ścieżki plików, zapytania, linki) i pobiera treść dynamicznie w runtime (glob, grep, zapytanie do bazy). *Progressive disclosure*: kontekst odkrywany stopniowo, w pamięci tylko to, co właśnie potrzebne. Wzorcowa hybryda: stały rdzeń (jak `CLAUDE.md`) ładowany z góry + eksploracja na żądanie. Tu RAG wpina się jako jedna z technik retrievalu, nie jako całość zagadnienia.

**6. Miejsce w stosie agenta — co to NIE jest**
Glosariusz [[HuggingFace]] precyzuje granice: context engineering to **projektowanie tego, co trafia do okna**, i jest częścią *scaffoldingu* (warstwa definiująca zachowanie: system prompt, opisy narzędzi, zarządzanie kontekstem między krokami) — w odróżnieniu od *harnessa* (warstwa wykonawcza: pętla wywołań, obsługa narzędzi, decyzja o zatrzymaniu). Wzór: `Agent = Model + Harness`. Ten sam model (np. [[Claude]]) zachowuje się zupełnie inaczej przy różnym kontekście i różnym harnessie — context engineering odpowiada za pierwszą z tych zmiennych.

**7. Project Room / Data Room — przygotować środowisko, zanim agent napisze ([[Nate B Jones]])**
Halucynacje w poważnej pracy z wiedzą są **strukturalne** — biorą się z chaotycznego środowiska plików, nie ze złego modelu ani promptu (kazus kancelarii Sullivan & Cromwell: dziesiątki sfabrykowanych cytatów w piśmie sądowym). Nie naprawi tego lepszy prompt — naprawia to przygotowanie kontekstu. Pierwsza instrukcja dla agenta zmienia się więc z „napisz dokument" na „zbuduj pokój roboczy": cztery artefakty generowane *przed* finałem — **Source Inventory** (tabela: ścieżka, typ, data, autorytatywność, aktualność, co źródło wspiera), **Conflict Log** (sprzeczności między źródłami do rozstrzygnięcia przez człowieka), **Missing Context List** (czego brakuje — bo brakujące dane są często ważniejsze niż dostępne; jeśli model nie wie, że czegoś brak, wynajduje odpowiedź) i **Duplicates Report** (rodziny wersji — w AI duplikat to problem z rozumowaniem, nie tylko porządkiem). Dopiero potem krótki prompt: które źródło jest autorytatywne dla liczb, które dla kontekstu, a które to tło — i napisz. Podział ról jak w [[2026-06-14 RAG|RAG]]: agent buduje canvas, człowiek decyduje, agent pisze.

**8. Context layer organizacji — „boil the ocean" zamiast kuracji ([[Andrea Jones-Rooy]])**
Obok minimalistycznego okna pojedynczego wywołania istnieje druga, makro-warstwa: **trwała baza kontekstu całej organizacji**, z której agent czerpie. Tu reguła jest odwrotna do minimalności na poziomie okna — Jones-Rooy i [[Allie K Miller]] radzą **nagrywać i archiwizować wszystko** (transkrypty spotkań, tickety, maile, support), bez perfekcyjnej kuracji „bo to spotkanie było za słabej jakości". Argument: modele są dziś dużo lepsze w przeszukiwaniu wielkich, surowych zbiorów niż 5 lat temu, gdy trzeba było ręcznie szukać igły w stogu; a porażki i nieudane spotkania mają wartość diagnostyczną (analogia ze stand-upem — uczysz się na złych występach). Surowiec zamienia się w wartość przez *odpytywanie* tego archiwum („jakie 5 skarg klientów wraca?", „jakie 3 błędy powtarzam?", „jak zmieniły się moje wzorce w 3 miesiące?"). Mikro-wariant osobisty: codzienne 5–40 min voice memo gromadzone miesiącami i przepuszczane przez [[Claude Code]]. To uzasadnia rozdzielenie ról: just-in-time retrieval (mechanizm 5) pobiera z tej warstwy tylko to, co potrzebne do danego okna — a sam vault [[Obsidian]] + `qmd` jest dokładnie taką warstwą kontekstu.

---

## Frameworki-kotwice

- **Zasada minimalności (Anthropic)** — „najmniejszy zestaw tokenów o wysokim sygnale"; kontekst jako zasób z malejącymi przychodami krańcowymi, nie magazyn do zapełnienia.
- **SCOPE (Gayle Roberts)** — operacyjny framework budowania trwałej bazy wiedzy organizacyjnej dla AI: **S**torage (centralizacja), **C**leaning (usunięcie bałaganu), **O**rganization (struktura, index files, relationship maps), **P**reparation (formaty AI-friendly + próbki tonu), **E**ngagement (połączenie AI z bazą). Efekt-kotwica: propozycja grantowa 20 godzin → 20 minut.
- **Trzy poziomy delegowania (Robert Szewczyk)** — (1) lepszy Google (copy-paste, zero kontekstu), (2) pogaduszki z chatbotem (kontekst powtarzany za każdym razem), (3) asystent z „Twoim DNA" (kontekst dostarczony raz, działa zawsze). Większość użytkowników utknęła na poziomie 1 — nie z braku umiejętności, lecz świadomości.
- **Analogia pracownika (Roberts)** — prompting = stażysta; Custom GPT = freelancer per projekt; context engineering = wieloletni pracownik znający organizację na wylot.
- **Project/Data Room (Jones)** — 4 artefakty przed pisaniem: Source Inventory / Conflict Log / Missing Context List / Duplicates Report; „czy agent może przygotować warunki, w których dobra praca jest możliwa?".
- **Prompt „5 decyzji" + Zero × Mnożnik (Woliński)** — przed dużym zadaniem zapytaj LLM: „wypisz 5 decyzji, których NIE powinienem Ci oddawać, bo wymagają wiedzy o mojej firmie/branży/kliencie"; AI mnoży to, co masz — mnożysz zero, dostajesz zero.
- **Liczby-kotwice**: subagent zwraca 1000–2000 tokenów z dziesiątek tysięcy przeczytanych; „context layer" jako fosa konkurencyjna — [[Cursor]] osiągnął 1 mld USD ARR dzięki warstwie kontekstu (nie modelowi), [[Google]] zapłacił 2,4 mld USD za [[Windsurf]] zamiast konkurować.

---

## Powiązane pojęcia

- [[2026-06-14 RAG]] — szczególny, retrieval-owy przypadek context engineeringu: dostarczenie do okna świeżo pobranych, zaufanych fragmentów. RAG odpowiada na pytanie „skąd wziąć właściwy kontekst?", context engineering — na szersze „jak ułożyć *całe* okno?".
- [[2026-06-13 Wdrażanie AI w organizacji społecznej]] — context engineering operacjonalizuje regułę „garbage in, garbage out": większość „złych wyników AI" to brak kontekstu, nie wada modelu. SCOPE to konkretna ścieżka wdrożeniowa filaru gotowości danych.
- [[2026-06-14 Storytelling oparty na danych]] — „ton marki" i „głos organizacji" jako warstwy kontekstu: zasilenie modelu próbkami stylu i danymi to warunek outputu gotowego do publikacji, nie generycznego.
- [[2026-06-15 Prompt engineering]] — węższy poprzednik (pisanie samej instrukcji); context engineering go obejmuje i przesuwa punkt ciężkości z treści promptu na cały stan tokenów.
- [[Harness i scaffolding]] — warstwy wykonawcza i definiująca zachowanie agenta; context engineering należy do scaffoldingu (czerwony link — backlog, gdy uzbiera się masa źródeł o architekturze agentów).

---

## Zastosowanie w kontekście NGO

- **Budowa pluginów i skillów [[Claude Code]]**: techniki Anthropic (compaction, just-in-time retrieval, sub-agent architectures, „goldilocks zone" dla system promptów) stosują się wprost do projektowania własnych agentów automatyzujących pracę organizacji. Vault z `CLAUDE.md` + `qmd query` to działający wzorzec stałego rdzenia + eksploracji na żądanie.
- **SCOPE jako usługa wdrożeniowa**: gotowy, wdrażalny przewodnik dla klienta NGO — start od 3 najczęściej tworzonych treści (propozycje grantowe, newslettery, raporty), zbudowanie dla nich bazy kontekstu, pomiar oszczędności czasu. Mała organizacja może zacząć od 3 dokumentów.
- **Szkolenia z AI dla organizacji**: framework trzech poziomów delegowania to gotowe narzędzie dydaktyczne — pokazuje uczestnikom, dlaczego „lepszy prompt" to ślepa uliczka, a inwestycja w kontekst (onboarding AI w organizację) zwraca się wielokrotnie. Mocny przekaz: context > model.
- **Argument sprzedażowy / strategiczny**: „warstwa kontekstu to fosa" — przy doradztwie warto pokazać, że trwała przewaga (i trudność zastąpienia narzędzia) leży w jakości kontekstu, nie w dostępie do modelu, który ma każdy.
- **Higiena pamięci agenta**: parametr długości okna pamięci (np. Simple Memory w [[n8n]]) to konkretna decyzja projektowa — zbyt mały kontekst = „złota rybka", zbyt duży = koszt i context rot; wartość dobiera się do charakteru aplikacji.

---

## Otwarte pytania

- Jak zmierzyć „jakość kontekstu" obiektywnie, zanim zobaczy się output — czy istnieje tańszy sygnał niż eval na realnych zadaniach?
- Gdzie przebiega próg, przy którym warto przejść od ręcznie kuratorowanego kontekstu (SCOPE, pliki) do automatycznego retrievalu (RAG) — i kiedy to przejście jest przedwczesną komplikacją?
- Jak pogodzić *minimalność kontekstu* (mniej tokenów = lepiej) z presją na „dosypywanie" wiedzy o organizacji — kto i jak decyduje, co wyciąć?
- W jakim stopniu polskie NGO są w stanie samodzielnie utrzymać bazę kontekstu (SCOPE wymaga dyscypliny porządkowania danych) bez stałego wsparcia konsultanta — czy to kompetencja do przekazania, czy usługa cykliczna?
