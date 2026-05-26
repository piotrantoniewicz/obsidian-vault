---
categories: Clippings
authors: ["[[Tal Raviv]]"]
url: https://www.lennysnewsletter.com/p/make-product-management-fun-again
source: "[[Archives/2025-04-29 Make product management fun again with AI agents|2025-04-29 Make product management fun again with AI agents]]"
published: 2025-04-29
created: 2026-05-12
relevance: średnia
tags:
  - "automatyzacja"
  - "narzędzia-AI"
  - "strategia-AI"
---

# Make product management fun again with AI agents

[[Tal Raviv]] opisuje praktyczny framework budowania agentów AI dla product managerów, skupiając się na kategorii "AI automations" — narzędzi jak [[Zapier]], Lindy AI, Relay.app czy Gumloop, które działają proaktywnie, podejmują realne akcje i tworzą własne pętle feedbacku. Główna teza: agenci AI najlepiej sprawdzają się przy powtarzalnych, ciągłych zadaniach wymagających odrobiny oceny i pisania — analogicznie do delegowania pracy juniorowi, nie ekspertowi. Artykuł zawiera gotowy prompt do AI przekształcający opis zadania w step-by-step instrukcje dla dowolnej platformy, co radykalnie obniża barierę wejścia. Pięć zasad projektowania agenta: zacznij małe, ogranicz potencjalne straty, buduj słowami, iteruj z wyrozumiałością, stopniowo buduj zaufanie.

## Frameworki i metody

- **6-cechowe spektrum agentów AI** — stopień "agentyczności" systemu określa obecność: działania proaktywnego, tworzenia planu, korzystania z kontekstu, dostępu do danych na żywo, podejmowania akcji w świecie rzeczywistym, tworzenia własnej pętli feedbacku
- **Checklist projektowania agenta (5 pytań)**:
  1. Czy rozumiem to zadanie na tyle, by je opisać krok po kroku?
  2. Czy mogę zacząć od czegoś mniejszego (najgorsza jedna czynność, nie cały workflow)?
  3. Czy ograniczyłem potencjalne straty (DM zamiast publicznego kanału, draft zamiast wysłanego emaila)?
  4. Czy dałem wystarczający kontekst (kto jest w CS team, jaki framework priorytetyzacji)?
  5. Czy pozostaję blisko surowych sygnałów klientów (cytaty i linki, nie tylko podsumowania)?
- **Wzorce bezpiecznego wdrożenia** — zamiast pingować kanał → wyślij mi DM; zamiast wysyłać email → utwórz draft; zamiast podejmować decyzję → zarekomenduj; zamiast modyfikować dokument → dołącz sugestię na końcu
- **Prompt do AI agent buildera** — gotowy megaprompt do o3 Deep Research lub Perplexity, który na podstawie opisu zadania generuje step-by-step instrukcje dla Zapier/Lindy/Relay/Cassidy/Gumloop z uwzględnieniem ograniczeń każdej platformy

## Wnioski

- Najlepsza platforma agentów to ta, którą firma już używa i której ufa — integracja z istniejącym [[Make.com]] lub Zapierem jest ważniejsza niż wybór "najlepszego" narzędzia
- Agenci AI nie zastąpią intuicji opartej na bezpośrednim kontakcie z "klientem" — narzędzie powinno pokazywać cytaty i linki do oryginałów, nie tylko podsumowania
- Delegowanie do AI juniora działa na tych samych zasadach co delegowanie do człowieka: jasne instrukcje, przykłady sukcesu, iteracja z feedbackiem

## Zastosowanie

Framework "AI junior intern" pasuje bezpośrednio do automatyzacji outreachu NGO: Piotr mógłby zdefiniować zadanie dla agenta jako "znajdź nowe NGO pasujące do profilu ICP, uzupełnij dane kontaktowe i przygotuj draft wiadomości do mojej weryfikacji". Gotowy prompt do AI agent buildera można uruchomić w Claude lub Perplexity i uzyskać instrukcje konfiguracji w [[Make.com]] lub Zapierze bez kodowania. Zasada "zostań blisko surowych sygnałów" to ważne przypomnienie przy automatyzacji komunikacji z darczyńcami — agent powinien linkować do oryginalnych odpowiedzi, nie tylko syntetyzować.
