---
categories: Concept
tags:
  - context-engineering
  - strategia-AI
  - strategia-organizacji
created: 2026-07-06
updated: 2026-07-06
relevance: wysoka
sources:
  - "[[2026-06-24 How a Former NYU Professor Uses Claude Code]]"
  - "[[2026-06-14 A frontier without an ecosystem is not stable]]"
  - "[[2025-07-28 Beyond Prompts How Context Engineering Could Revolutionize Your Nonprofit AI Workflows]]"
  - "[[2025-10-02 Your Nonprofit s Data Strategy Needs an Upgrade Why Structure Beats Volume in the AI Age]]"
  - "[[2026-05-20 Your Data Strategy is Your Mission Strategy]]"
  - "[[2026-04-02 Full Guide How To Create A Master Business Context Folder To Arm Your AI With Everything It Needs To Help You Scale Your Business, Streamline Workflows, And Create Output You Can Trust]]"
  - "[[2025-12-29 Co tracimy, gdy wszystko zapisuje się samo? Amelia Acker, Archiving Machines From Punch Cards to Platforms, 2025]]"
---

# Context layer organizacji (organizacyjna warstwa kontekstu)

Trwała, odpytywalna baza całej wiedzy organizacji — transkrypty spotkań, maile, dokumenty programowe, historia darczyńców, archiwum treści, decyzje i porażki — z której systemy AI czerpią kontekst do każdego zadania. To **makro-warstwa nad pojedynczym oknem kontekstu**: okno jest ulotne i minimalistyczne, warstwa — trwała i rosnąca; łączy je retrieval, który pobiera z warstwy tylko to, czego potrzebuje bieżące zadanie. Stawka jest strategiczna, nie techniczna ([[Satya Nadella]]): organizacja, która buduje na tej warstwie własną **pętlę uczenia się**, kompounduje wiedzę niemożliwą do skopiowania przez podmianę modelu — *„możesz zlecić zadanie, a nawet pracę, ale nigdy nie możesz zlecić swojego uczenia się"*. Warstwa kontekstu to fosa.

---

## Kluczowe mechanizmy

**1. Odwrócona reguła: minimalizm w oknie, maksymalizm w warstwie**
Na poziomie pojedynczego wywołania kontekst to skończony budżet (goldilocks zone) — ale na poziomie organizacji reguła się odwraca: **nagrywaj i archiwizuj wszystko** (spotkania, tickety, maile, support), bez perfekcyjnej kuracji „bo to spotkanie było słabe" ([[Andrea Jones-Rooy]]). Modele są dziś dużo lepsze w przeszukiwaniu wielkich surowych zbiorów niż kiedyś, a porażki mają wartość diagnostyczną. Surowiec zamienia się w wartość przez **odpytywanie**: „jakie 5 skarg wraca?", „jakie 3 błędy powtarzam?", „jak zmieniły się nasze wzorce przez kwartał?". Mikro-wariant osobisty: codzienne voice memo gromadzone miesiącami i analizowane hurtowo.

**2. Fosa i pętla uczenia się — human capital + token capital**
Nadella rozróżnia **human capital** (wiedza, relacje, osąd ludzi) i **token capital** (własne zdolności AI organizacji) — mają się wzajemnie wzmacniać, nie zastępować. Architektura pętli: każdy workflow produkuje sygnał → prywatne evale mierzą, czy system poprawia się względem wyników *ważnych dla organizacji* → baza wiedzy zyskuje pamięć instytucjonalną → „hill climbing machine" kompoundująca przewagę. Test kontroli: **suwerenność modelu** — czy możesz wymienić generalistyczny model bez utraty „eksperta organizacyjnego" zakodowanego w warstwie? Jeśli ekspert żyje w warstwie kontekstu (a nie w konkretnym narzędziu), odpowiedź brzmi tak.

**3. Od 20 godzin do 20 minut — SCOPE i analogia pracownika**
Efekt dobrze zbudowanej warstwy jest mierzalny: propozycja grantowa 20 godzin → 5 godzin (dobry prompting) → **20 minut** (context engineering z bazą wiedzy organizacji; Gayle Roberts). Ścieżka budowy to framework **SCOPE**: Storage (centralizacja) → Cleaning (usunięcie bałaganu) → Organization (struktura, indeksy, mapy relacji) → Preparation (formaty przyjazne AI + próbki głosu organizacji) → Engagement (spięcie platformy AI z bazą). Analogia poziomów: prompting = stażysta, custom GPT = freelancer od projektu, warstwa kontekstu = **wieloletni pracownik, który zna misję na wylot**. Mała organizacja może zacząć od 3 dokumentów.

**4. Napięcie: „zalej ocean" vs „struktura bije wolumen" — i jego rozstrzygnięcie**
Tectonica dowodzi tezy pozornie przeciwnej do Jones-Rooy: o przewadze nie decyduje ilość danych, lecz **czystość, połączenie i kontekst** — jeden zadbany [[CRM]] z historią zaangażowania jest cenniejszy niż wielka zaniedbana baza, a AI karmiona chaosem produkuje chaos. Rozstrzygnięcie: obie reguły dotyczą **różnych pięter warstwy**. Surowe archiwum jakościowe (transkrypty, notatki, treści) może być maksymalistyczne, bo nawiguje po nim retrieval; dane **operacyjne** (rekordy darczyńców, segmenty, zgody) muszą być ustrukturyzowane, bo na nich AI podejmuje działania. Warstwa kontekstu = surowy ocean **plus** warstwa dostępu (indeksy, metadane, wyszukiwanie) — bez nawigacji ocean jest tylko bagnem.

**5. Minimalny wariant startowy — master context folder**
Nie trzeba infrastruktury, żeby zacząć: system **8 dokumentów kontekstowych** ładowanych do projektu LLM (Dickie Bush) — North Star (wizja, misja, wartości, zasady decyzyjne), profil odbiorcy, opis oferty/programów, mapa kanałów, struktura zespołu, stos narzędzi oraz **„What Good Looks Like" vault**: biblioteka najlepszych własnych treści + wzorzec głosu (i kontrprzykład, czym głos *nie* jest) — to on eliminuje generyczne outputy. Każdy nowy czat dziedziczy całość. Dla organizacji społecznej: teoria zmiany, persony darczyńców i beneficjentów, najlepsze apele i raporty.

**6. Gdzie leży warstwa — suwerenność jako decyzja misyjna**
Warstwa kontekstu zawiera najcenniejsze (i najwrażliwsze) dane organizacji, więc *gdzie* leży, jest wyborem politycznym i etycznym, nie technicznym detalem. Amelia Acker: platformy przejmują „suwerenność funkcjonalną" nad danymi przez automatyzację archiwizacji — dane raz oddane „nigdy w pełni nie znikną". Bryan Neider podnosi to do rangi dyscypliny przywódczej: **data strategy = mission strategy**, z filarami takimi jak sovereign AI adoption (dane nie trenują cudzych modeli), data residency i **no-access mindset** (nawet operator chmury nie ma wglądu — krytyczne dla schronisk, usług zdrowotnych). Lokalne i hybrydowe rozwiązania (własny vault, [[2026-06-14 RAG|RAG]] u siebie) to praktyczna realizacja: *„nie zarządzamy danymi — sprawujemy opiekę nad zaufaniem"*.

---

## Powiązane pojęcia

- [[2026-06-15 Context engineering|Context engineering]] — strona macierzysta: warstwa kontekstu wydzieliła się z tamtejszego mechanizmu 8; context engineering zarządza oknem (mikro), ta strona — trwałą bazą, z której okno czerpie (makro).
- [[2026-07-06 Evale|Evale]] — pętla uczenia się wymaga prywatnych evali („czy system poprawia się względem *naszych* wyników"); zarazem otwarte pytanie obu stron: co jest benchmarkiem samej bazy wiedzy?
- [[2026-06-14 RAG|RAG]] — techniczny most między warstwą a oknem: retrieval pobiera z bazy organizacji dokładnie to, czego potrzebuje bieżące zadanie; RAG lokalny/hybrydowy to realizacja suwerenności warstwy.
- [[2026-07-06 RODO i dane wrażliwe|RODO i dane wrażliwe]] — warstwa pełna danych osobowych i wrażliwych: „nagrywaj wszystko" wymaga protokołów zgody, minimalizacji na wejściu do modeli i architektury „model vs wiedza".
- [[2026-06-13 Wdrażanie AI w organizacji społecznej|Wdrażanie AI w organizacji społecznej]] — filar gotowości danych w praktyce: „AI odsłania istniejące słabości", a warstwa kontekstu to systemowa odpowiedź zamiast łatania per narzędzie.
- [[2026-07-06 LLM Wiki|LLM Wiki]] — treściowa realizacja warstwy po stronie wiedzy syntetycznej: encyklopedia pojęć budowana przez LLM-bibliotekarza (metoda Karpathy'ego) nad surowym archiwum.

---

## Zastosowanie w kontekście organizacji społecznych

- **Własny wzorzec do pokazywania klientom**: vault Obsidian + `qmd` + indeksy to działająca warstwa kontekstu (surowe Archives + syntetyczne Resources + Galaxy jako wiki) — żywe demo zamiast slajdów.
- **Start dla organizacji — SCOPE na 3 treściach**: wybierz trzy najczęściej tworzone materiały (wnioski grantowe, newsletter, raporty) i zbuduj warstwę tylko dla nich; mierz efekt czasowy (20h → 20min to argument, który zarząd rozumie bez tłumaczenia).
- **Wersja zerowa: 8 dokumentów NGO** — teoria zmiany + persony darczyńców/beneficjentów + programy + kanały + zespół + narzędzia + biblioteka najlepszych treści z wzorcem głosu; jedna sesja warsztatowa, jeden projekt w Claude.
- **Rytuał zasilania i odpytywania**: transkrypcje spotkań (z protokołami zgody!), notatki z decyzji, retro — plus kwartalne pytania do archiwum: „jakie skargi wracają?", „które apele działały?", „co obiecaliśmy i czego nie zrobiliśmy?".
- **Audyt strategii danych jako usługa** — przed wdrożeniem jakiegokolwiek narzędzia AI: czystość / połączenie / kontekst danych operacyjnych + decyzja o lokalizacji warstwy (suwerenność) — checklist z Tectonica + 5 filarów Neidera.
- **Argument fosy dla zarządu**: narzędzia AI są u wszystkich te same — przewagą organizacji jest to, czego nikt inny nie ma: jej własna, skumulowana, odpytywalna wiedza; inwestycja w warstwę kontekstu procentuje przy *każdym* przyszłym modelu.

---

## Otwarte pytania

- Co jest benchmarkiem dla samej warstwy — jak ocenić, że baza wiedzy jest „dobra", zanim zobaczymy jej efekt w outputach (wspólne otwarte pytanie z [[2026-07-06 Evale|Evalami]])?
- Jak pogodzić „nagrywaj wszystko" z zasadą minimalizacji danych z RODO — czy da się prowadzić maksymalistyczne archiwum jakościowe bez gromadzenia danych osobowych ponad potrzebę?
- Kto utrzymuje warstwę w małej organizacji — czy rola „bibliotekarza kontekstu" (człowiek + LLM) może być cząstkowa, czy bez właściciela warstwa nieuchronnie gnije?
- Ile struktury na wejściu, a ile w retrieval — gdzie leży punkt równowagi dla organizacji bez technicznego zaplecza: porządkować dane czy inwestować w lepsze wyszukiwanie?
- Czy „suwerenność modelu" jest realnie osiągalna dla organizacji społecznej na narzędziach SaaS — co w praktyce oznacza „zabierz warstwę i odejdź", gdy kontekst żyje w Projects/Gems/Copilotach dostawców?
