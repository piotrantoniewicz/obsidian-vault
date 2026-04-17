---
categories: Clippings
authors:
  - '[[Dickie Bush]]'
url: 'https://aioperatornewsletter.substack.com/p/full-guide-how-to-create-a-master'
source: >-
  [[Archives/2026-04-02 Full Guide How To Create A Master Business Context
  Folder To Arm Your AI With Everything It Needs To Help You Scale Your
  Business, Streamline Workflows, And Create Output You Can Trust|2026-04-02
  Full Guide How To Create A Master Business Context Folder To Arm Your AI With
  Everything It Needs To Help You Scale Your Business, Streamline Workflows, And
  Create Output You Can Trust]]
published: '2026-04-02'
created: '2026-04-12'
relevance: wysoka
tags:
  - context-engineering
  - narzędzia-AI
  - prompt-engineering
---
# Full Guide How To Create A Master Business Context Folder To Arm Your AI With Everything It Needs To Help You Scale Your Business, Streamline Workflows, And Create Output You Can Trust

[[Dickie Bush]] z newslettera AI Operator opisuje system 8 dokumentów kontekstowych, które należy załadować do projektu w [[LLM]], by AI rozumiało biznes na tyle dobrze, że każdy output wymaga minimalnej korekty. Kluczowy insight: większość problemów z jakością outputów AI nie wynika ze słabego promptowania, ale z braku kontekstu — AI nie zna oferty, klientów, lejka sprzedażowego ani głosu marki. Jednorazowe zainwestowanie czasu w odpowiedź na ~150 pytań i stworzenie 8 dokumentów permanentnie podnosi jakość każdej sesji z AI. Koncepcja bezpośrednio łączy się z pojęciem [[context-engineering]] jako nowym kluczowym obszarem kompetencji dla profesjonalistów pracujących z AI.

## Frameworki i metody

**8 dokumentów kontekstowych (Master Business Context Folder):**

1. **The Money Model Builder** — pełny opis oferty: nazwy produktów, obietnice, transformacja, struktura cenowa, ścieżki upsell/downsell/continuity. Bez tego AI jest ślepe na to, co sprzedajesz.
2. **The Perfect Avatar Map** — głęboki profil klienta: aktualna sytuacja, 5 bólów (tangible + emocjonalny), 5 pragnień, co już próbowali, 5 lęków i przekonań blokujących, 5 przekonań niezbędnych do zakupu, 10 głównych obiekcji (niepewność, timing, partner, pieniądze).
3. **The Belief Ladder** — sekwencja przekonań, które prospect musi przyjąć przed zakupem: przekonanie docelowe, unikalny mechanizm, 5-7 szczebli drabiny — od błędnego przekonania wyjściowego do decyzji o zakupie. Zmienia AI ze „generatora copy" w „stratega perswazji".
4. **The Acquisition Blueprint** — mapa wszystkich kanałów pozyskania i lejka sprzedażowego end-to-end: kanały (organic, paid, referrals, SEO, community), etapy lejka (capture → bridge touchpoints → conversion).
5. **The North Star Brief** — jedna strona: wizja (cel długoterminowy), misja (codzienna praca), 3-5 wartości (z opisem jak wyglądają w działaniu), 5-12 zasad operacyjnych (frameworki decyzyjne).
6. **The Org Chart Builder** — struktura zespołu: departamenty, każda osoba z rolą, odpowiedzialnością, przełożonym i stażem. Pozwala AI konkretnie delegować zadania wg imion.
7. **The Tech Stack Inventory** — lista 40+ funkcji biznesowych i przypisanych narzędzi. Bez tego AI proponuje narzędzia, których nie używasz.
8. **The "What Good Looks Like" Vault** — biblioteka najlepszych przykładów: posty, emaile, copy, skrypty, opinie klientów + jeden przykład idealnego głosu i jeden przykład czego głos NIE jest. Eliminuje problem „brzmi jak robot".

**Architektura projektu LLM:**
- Krok 1: Utwórz jeden Project w LLM (np. Claude) — to baza.
- Krok 2: Załaduj wszystkie 8 dokumentów jako pliki projektu — każdy chat dziedziczy kontekst automatycznie.
- Krok 3: Stwórz chaty strategiczne: jeden „CEO Strategy Chat" (decyzje, priorytety, bottlenecki) + jeden chat per departament (Sales, Marketing, Ops, itd.).
- Krok 4: Chaty taktyczne do jednorazowych zadań (email, SOP, copy) — też dziedziczą pełny kontekst.

**Dokumenty uzupełniające:** dashboardy i arkusze danych, wyciągi bankowe/P&L, biblioteka SOP, notatki ze spotkań, połączenie z [[Slack]] przez MCP.

## Wnioski

- [[Context engineering]] to skuteczniejsza dźwignia niż [[prompt engineering]] — 8 dokumentów kontekstowych podnosi jakość każdego outputu permanentnie, bez potrzeby ciągłego re-promptowania przy każdym nowym zadaniu.
- Architektura projekt LLM (jeden projekt + chaty strategiczne + chaty taktyczne) to wzorzec adaptowalny dla dobryai.pl i dla organizacji NGO — każda organizacja może zbudować własne 8 dokumentów i działać z AI jak z konsultantem znającym ich kontekst.
- „What Good Looks Like" Vault eliminuje problem generycznych outputów — biblioteka własnych przykładów contentowych to najważniejszy dokument dla ghostwritingu, content marketingu i tworzenia materiałów szkoleniowych.

## Zastosowanie

System 8 dokumentów kontekstowych warto zaadaptować dla dobryai.pl jako rdzeń własnego workspace'u w Claude — to bezpośrednia implementacja, którą można zrobić w ciągu jednej sesji. W kursie Fundraising z AI moduł ten może posłużyć jako praktyczny „first step" dla organizacji: zanim zaczniesz używać AI operacyjnie, zbuduj kontekst organizacji. Dokumenty 1–5 (money model, avatar, belief ladder, acquisition, north star) naturalnie mapują się na strukturę Second Brain w Obsidian jako materiał obszarowy i projektowy.
