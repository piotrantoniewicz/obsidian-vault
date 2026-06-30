---
categories:
  - Clippings
authors: ["[[The Agency Fund]]"]
url: "https://theagencyfund.substack.com/p/a-default-tech-stack-for-the-social?r=1pabzg&utm_medium=ios&triedRedirect=true"
source: "[[Archives/2026-06-25 A Default Tech Stack for the Social Sector|2026-06-25 A Default Tech Stack for the Social Sector]]"
published: 2026-06-25
created: 2026-06-30
relevance: wysoka
tags:
  - "strategia-AI"
  - "narzędzia-AI"
  - "organizacje-społeczne"
---

# A Default Tech Stack for the Social Sector

[[The Agency Fund]], we współpracy z data.org, Fast Forward i IDinsight, publikuje domyślny zestaw narzędzi technologicznych dla organizacji społecznych z małymi zespołami IT — po ocenie ponad 50 narzędzi we współpracy z ponad 30 organizacjami w Azji, Afryce i Ameryce Łacińskiej. Stack podzielony jest na trzy warstwy: AI, obserwacja i uczenie się oraz front-end. Kluczowe podejście: nie buduj wszystkiego naraz — zidentyfikuj wąskie gardło operacyjne i zacznij tam. Większość rekomendowanych narzędzi jest open-source lub oferuje hojne plany darmowe z rabatami dla NGO.

## Frameworki i metody

**Trzy warstwy stacku dla organizacji społecznych:**

**Warstwa AI:**
- LLM gateway: [[OpenRouter]] (domyślny) — unikaj lock-in; unified interface dla Gemini, OpenAI, Claude
- Monitoring LLM: [[Langfuse]] — śledzenie wywołań modelu, debugowanie regresji; uruchom przed startem, nie po
- Mowa STT/TTS: ElevenLabs (globalnie) lub Sarvam (języki indyjskie)
- Agent builders: OpenRouter Agents SDK lub Pydantic AI — model-agnostic; alternatywy: Claude Agents SDK, OpenAI Agents SDK
- Baza wektorowa: natywne file search od dostawcy LLM (start dla większości); Weaviate lub pgvector gdy zależy na unikaniu lock-in

**Warstwa obserwacji i uczenia się:**
- Data pipeline: Airbyte → BigQuery → dbt
- Dashboardy: Looker Studio (darmowe, zintegrowane z BigQuery); Metabase dla self-hosted
- Orkiestracja workflow: [[n8n]] — low-code, rosnąca dostępność dla NGO (**oficjalny default dla sektora**)
- Analiza ad hoc: Colab notebooks; Claude + dbt + Postgres [[MCP]] przyspiesza ~5x
- Eksperymenty A/B: Evidential (open-source, zbudowany dla NGO); alternatywy: Growthbook, Posthog

**Warstwa front-end:**
- Zbieranie danych w terenie (offline, niskie łącze): SurveyCTO (domyślny); CommCare dla case management; KoBoToolbox gdy priorytet: koszt
- Chatboty mobilne (WhatsApp/Telegram): Glific (koszt + społeczność NGO) lub Turn.io (doświadczenie użytkownika)
- Własne aplikacje (1–2 osobowy zespół): FastAPI + Next.js + Postgres + Tailwind + Vercel + Claude Code

**Pięć lekcji z pola:**
1. Standaryzuj metryki produktowe zanim zbudujesz analitykę — inaczej każdy zespół liczy "zaangażowanie" inaczej
2. Buduj systemy ewaluacji ([[Langfuse]]) przed skalowaniem — retroaktywna infrastruktura jest kosztowna
3. Uczyń eksperymentowanie nawykiem, nie jednorazowym projektem — bariera jest kulturowa, nie techniczna
4. Rozpoznawaj luki i dziel się nimi publicznie — niektórych problemów (np. identity resolution) nie rozwiązuje żadne gotowe narzędzie
5. Buduj tylko to, co służy misji — każda nowa funkcja wymaga utrzymania i nawigacji przez użytkownika

## Kluczowe dane

- Ocena ponad 50 narzędzi we współpracy z ponad 30 organizacjami (Azja, Afryka, Ameryka Łacińska)
- Claude + dbt + Postgres MCP skrócił czas analizy ad hoc ~5x w projektach The Agency Fund
- 26% organizacji nonprofit nie ma konta na YouTube (dane: M+R Benchmarks 2025)

## Wnioski

- [[n8n]] to oficjalny default dla orkiestracji workflow w sektorze NGO według The Agency Fund — potwierdza wybór tej kategorii narzędzi i pozwala się na to powoływać w pracy z klientami
- Najtańsza baza wektorowa to często żadna baza — jeśli dokumenty mieszczą się w oknie kontekstowym modelu, pomiń retrieval i wrzuć je do promptu z cachingiem
- Stack AI dla NGO nie wymaga wielkiej inwestycji — większość narzędzi jest open-source lub ma hojne plany darmowe z rabatami nonprofit; bariera wejścia spadła dramatycznie

## Cytat

> Najtańsza baza wektorowa to często żadna baza wektorowa.

## Zastosowanie

Ten artykuł to gotowy materiał referencyjny do szkoleń i konsultacji z klientami NGO — konkretny, zweryfikowany przez zewnętrzny podmiot stack zamiast teorii. Przy wdrożeniach AI warto odwołać się do tej mapy jako zewnętrznej walidacji wyboru narzędzi ([[n8n]], [[Langfuse]], [[OpenRouter]]). Dla klientów NGO rozważających własne produkty cyfrowe — sekcja "custom applications" z Claude Code jako domyślnym narzędziem to argument za podejściem vibe-coding + agentowe środowisko pracy.
