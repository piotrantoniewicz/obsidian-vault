---
categories: Clippings
authors: ["[[dr Ewa Chamczyk]]"]
url: https://haimagazine.com/pl/ai_branza/it/karpathy-ai-to-nie-prad-to-nowy-system-operacyjny/
source: "[[Archives/2025-07-17 Karpathy AI to nowy system operacyjny - hAI Magazine|2025-07-17 Karpathy AI to nowy system operacyjny - hAI Magazine]]"
published: 2025-07-17
created: 2026-03-24
relevance: wysoka
tags:
  - "strategia-AI"
  - "LLM"
  - "trendy-AI"
---

# Karpathy AI to nowy system operacyjny - hAI Magazine

Artykuł [[dr Ewa Chamczyk]] w hAI Magazine prezentuje i komentuje ramowy model [[Andrej Karpathy]] opisujący AI nie jako „nową elektryczność" (metafora Andrew Nga), lecz jako nowy, uniwersalny komputer — platformę do tworzenia, nie tylko zasób do konsumowania. Karpathy wyróżnia trzy epoki oprogramowania (Software 1.0/2.0/3.0), porównuje [[LLM]] do komputerów mainframe lat 60. i proponuje koncepcję „suwaka autonomii" jako praktyczną odpowiedź na pytanie, jak wdrażać AI odpowiedzialnie. Artykuł omawia też „lukę infrastrukturalną" jako kluczowe wyzwanie kolejnej dekady.

## Frameworki i metody

**Trzy epoki oprogramowania wg Karpathy:**
- **Software 1.0** — klasyczny kod (C++, Java); rzemieślnik piszący jawną, deterministyczną logikę linijka po linijce; precyzyjny, ale kruchy wobec niejednoznaczności
- **Software 2.0** — uczenie maszynowe; zamiast reguł → dane; deweloper staje się kuratorem zbiorów treningowych; „czarne skrzynki" zdolne do rozpoznawania wzorców
- **Software 3.0** — [[LLM]] i język naturalny jako interfejs programowania; zamiast pisać kod lub kuratorować dane → opisujesz problem w dialogu z modelem; człowiek staje się architektem, redaktorem i „psychologiem AI"

**LLM jako analogia komputera:**
- Model (np. [[GPT-4]]) = CPU (procesor wykonujący polecenia)
- Okno kontekstowe = RAM (pamięć robocza dla bieżącej sesji)
- Narzędzia i wtyczki (internet, kalkulator, interpreter kodu) = peryferia i sterowniki
- Aplikacje (Cursor, Perplexity) = przenośne programy działające na różnych „OS-ach" (modelach)

**Psychologia [[LLM]] — paradoks Raymonda i Leonarda:**
- Jak **Raymond z „Rain Mana"** — genialne przetwarzanie w oknie kontekstowym, fotograficzna pamięć krótkotrwała, zdolność korelacji tysięcy stron tekstu
- Jak **Leonard z „Memento"** — głęboka amnezja po zamknięciu kontekstu, podatność na sugestie, halucynacje jako „statystyczne echa brzmące poprawnie"
- Jedyna skuteczna strategia: **generuj, a potem weryfikuj** — człowiek pozostaje pilotem

**Suwak autonomii:**
- Zamiast pełnej autonomii AI: model jak egzoszkielet z „Iron Mana" — wzmacnia, nie zastępuje
- AI generuje, człowiek akceptuje/modyfikuje/odrzuca jednym kliknięciem
- Stopniowe delegowanie zadań wraz z budowaniem zaufania

## Kluczowe dane

- Karpathy stworzył aplikację mobilną „MenuGen" w weekend, bez znajomości Swift — eksperyment pokazał granicę vibe codingu: kod działa w izolacji, ale nie daje rady z infrastrukturą (API, uwierzytelnianie, konfiguracja serwera)

## Wnioski

- Największym blokerem masowego wdrożenia AI jest „luka infrastrukturalna" — modele nie potrafią działać w cyfrowym świecie zaprojektowanym dla ludzi (niejasna dokumentacja API, graficzne UI, wieloetapowe uwierzytelnianie); przyszłość należy do organizacji budujących infrastrukturę przyjazną dla agentów AI.
- Centralizacja obliczeń AI (ogromne koszty = kilku gigantów) tworzy ryzyko monopoli na inteligencję — istotny kontekst dla organizacji pozarządowych myślących o suwerenności cyfrowej i lokalnych modelach AI.
- Framework Software 1.0/2.0/3.0 jest gotową narracją dydaktyczną do szkolenia z AI — tłumaczy, dlaczego „programowanie" przestało wymagać znajomości składni i dlaczego prompt engineering to nowa forma pisania kodu.

## Cytat

> „Jesteśmy w roku 1960 rozwoju systemów operacyjnych. To, co dziś wydaje się rewolucyjne, za dekadę będzie wyglądać prymitywnie."

## Zastosowanie

Framework trzech epok oprogramowania jest gotową strukturą do modułu wprowadzającego na szkoleniach z AI dla NGO — wyjaśnia kontekst historyczny bez technicznego żargonu. Psychologia LLM (Raymond + Leonard) to doskonała metafora do tłumaczenia, dlaczego AI popełnia błędy i dlaczego weryfikacja jest obowiązkowa. Koncepcja suwaka autonomii może stanowić podstawę do rozmowy z zarządami NGO o tym, jak wdrażać AI bez utraty kontroli.
