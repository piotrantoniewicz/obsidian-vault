---
categories:
  - "Emails"
published: 2026-04-30
created: 2026-04-30
labels:
  - "AI Managers"
relevance: wysoka
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "szkolenia-AI"
---

# Jak bezpiecznie wdrożyć AI w organizacji – podsumowanie webinaru z Mateuszem i Kamilem

Newsletter podsumowuje webinar [[Mateusz Chrobok|Mateusza Chroboka]] i Kamila Porembińskiego na temat bezpiecznego wdrożenia AI w organizacjach. Centralnym pojęciem jest Shadow AI — niekontrolowane użycie narzędzi AI przez pracowników, które według badań dotyczy ponad 60% firm, bo pracownicy chcą być efektywni, a nikt nie wyznaczył im granic. Eksperci proponują 4-etapowy framework: inwentaryzacja, polityka, wybór narzędzi i edukacja ludzi — podkreślając, że zakazy nie działają, a regulacja i kultura just culture są skuteczniejsze. Materiał zawiera też pięć kluczowych pytań do dostawcy narzędzi AI (m.in. o DPA, lokalizację serwerów, certyfikaty bezpieczeństwa), które pozwalają ocenić ryzyko przed zakupem licencji. Dla organizacji pracujących z wrażliwymi danymi (np. NGO z danymi beneficjentów) szczególnie istotna jest opcja modeli lokalnych uruchamianych bez przesyłania danych na zewnątrz.

## Frameworki i metody

- **Krok 1: Inwentaryzacja** — przed wdrożeniem sprawdź, co już masz: z jakich narzędzi AI korzystają poszczególne zespoły, do jakich celów i jakie dane do nich trafiają; często okazuje się, że firma ma 14 narzędzi robiących 5 tych samych rzeczy
- **Krok 2: Polityka** — prosta, czytelna i aktualizowana polityka (jedna strona wystarczy) odpowiadająca na 3 pytania: czego nie wolno wklejać do AI, których narzędzi używamy i przy jakich warunkach, kto odpowiada za decyzje w tym obszarze
- **Krok 3: Wybór narzędzi** — 4 poziomy bezpieczeństwa: darmowe (ryzyko trenowania modeli na danych), płatne Pro/Plus (ograniczone zabezpieczenia, wymagają ręcznej konfiguracji), Enterprise (centralna kontrola, umowa DPA, wielokrotnie droższe), lokalne (uruchamiane na własnym sprzęcie, zero transferu danych – rekomendowane dla wrażliwych danych)
- **Krok 4: Ludzie i procesy** — edukacja pracowników jak szkolenie BHP: co można wklejać do modelu, jak zgłaszać incydenty, co robić gdy coś wycieknie; we wdrożenie powinni być zaangażowani: lider zmiany, dział IT, prawnik/compliance, zarząd
- **5 pytań do dostawcy AI** — Czy dane są używane do trenowania modelu? Gdzie są przechowywane i kto ma dostęp? Co dzieje się z danymi po zakończeniu subskrypcji? Czy podpiszesz Data Processing Agreement? Jakie certyfikaty bezpieczeństwa posiadasz (ISO, SOC 2)?
- **Just culture** — nie karaj pracowników za przyznanie się do błędu w użyciu AI, bo wtedy incydenty będą ukrywane zamiast zgłaszane

## Kluczowe dane

- Ponad 60% pracowników biurowych korzysta z narzędzi AI bez wiedzy przełożonych
- Korzystanie z modeli przez [[API]] jest zazwyczaj bezpieczniejsze niż przez aplikację webową — większość dostawców nie trenuje modeli na danych z API

## Wnioski

- Shadow AI to norma, nie wyjątek — organizacje powinny regulować i edukować zamiast zakazywać, bo zakazy skutkują ukrywaniem problemów i brakiem kontroli nad tym, co dzieje się z danymi
- Polityka AI nie musi być dokumentem prawnym — prosta, czytelna strona odpowiadająca na 3 pytania jest lepsza niż szczegółowy regulamin, którego nikt nie czyta; zasada: cokolwiek, co będziesz rozwijać, jest lepsze niż nic
- Dla NGO pracujących z danymi beneficjentów warto rozważyć [[LM Studio]] lub inne modele lokalne dla wrażliwych procesów, zamiast wklejać dane do chmurowych narzędzi jak [[ChatGPT]] czy [[Claude]]

## Cytat

> Nie nurkuj tam, gdzie Twój mózg jeszcze nie był — Kamil Porembiński o wdrożeniu AI: najpierw na kartce papieru, z pełną mapą przepływu danych, odpowiedzialnościami i planem na wypadek incydentu.

## Zastosowanie

Framework 4-etapowy (inwentaryzacja → polityka → narzędzia → ludzie) może być bezpośrednio zaadaptowany jako struktura konsultacji wdrożeniowych dla NGO — szczególnie w kontekście wrażliwych danych o beneficjentach, gdzie Shadow AI niesie poważne ryzyko naruszenia RODO. Lista 5 pytań do dostawcy AI to gotowy materiał warsztatowy dla uczestników kursu "Fundraising z AI" — pomaga organizacjom samodzielnie ocenić bezpieczeństwo narzędzi przed zakupem. Koncepcja just culture w kontekście AI jest przydatna przy projektowaniu polityk AI dla organizacji, które chcą budować kulturę odpowiedzialnego korzystania z narzędzi zamiast tworzyć atmosferę strachu.
