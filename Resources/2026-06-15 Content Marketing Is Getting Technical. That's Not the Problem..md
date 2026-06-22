---
categories:
  - Clippings
authors: ["[[Ina Toncheva]]"]
url: "https://inatoncheva.substack.com/p/content-marketing-is-getting-technical"
source: "[[Archives/2026-06-15 Content Marketing Is Getting Technical. That's Not the Problem.|2026-06-15 Content Marketing Is Getting Technical. That's Not the Problem.]]"
published: 2026-06-15
created: 2026-06-20
relevance: wysoka
tags:
  - "content-marketing"
  - "strategia-AI"
  - "narzędzia-AI"
---

# Content Marketing Is Getting Technical. That's Not the Problem.

[[Ina Toncheva]] analizuje listę zadań [[Ryan Law]] (Director of Content Marketing w [[Ahrefs]]) na pierwszy dzień jako Head of Content — roadmapę, która brzmi jak plan dewelopera: statyczna strona na GitHubie, vector embeddings całego bloga, cron job do odświeżania artykułów, Content OS jako centralny dashboard. Kluczowa teza autorki: techniczny charakter tych zadań jest drugorzędny — ważne jest, że opisują one nową definicję roli content marketera jako menedżera systemów AI, nie twórcy treści. Ograniczającym czynnikiem nie jest technologia, lecz zdolność do wyobrażenia sobie, co zbudować i dlaczego — a ta luka między „Ahrefs może to zrobić" a „przeciętna firma może to zrobić" zamyka się szybciej niż większość ludzi zakłada.

## Frameworki i metody

**8-punktowa architektura Content OS według Ryana Law:**

1. **Blog jako codebase** — statyczna strona (GitHub + Netlify/Cloudflare) zamiast WordPressa, by agenci AI mogli pisać bezpośrednio do plików
2. **Customer language mining** — wydobycie fraz z Gong/Intercom/Slack; dwu- i trzywyrazowe kombinacje = kąty contentowe i klastry słów kluczowych
3. **"Source of truth" w Markdown** — infrastruktura promptów: lista funkcji, przewodnik głosu, priorytety strategiczne — pliki referencyjne dla każdego workflow AI
4. **Vector embeddings całego bloga** — konwersja artykułów na wektory znaczeniowe; pozwala mierzyć autorytet tematyczny, wykrywać "topic drift" i automatyzować linkowanie wewnętrzne
5. **Automatyczny content audit** — Ahrefs MCP + Brand Radar + Site Audit + Google Search Console; output: lista priorytetów do naprawy, nie dashboardy
6. **Daily cron job** — skrypt odświeżający top artykuły: wykrywa luki tematyczne względem konkurencji, aktualizuje dane, zapisuje draft do ludzkiej akceptacji
7. **Content gap analysis** — Ahrefs MCP + Firehose (monitoring nowych treści u konkurencji w czasie rzeczywistym)
8. **Content OS / Agent A** — centralny dashboard scalający wszystkie powyższe raporty i automatyzacje w jeden interfejs

## Wnioski
- Rola content marketera ewoluuje w kierunku „managera AI" — ustawia wizję, buduje system, recenzuje output i stosuje ocenę jakościową; to trudniejsza praca, nie mniejsza.
- Pliki "source of truth" w Markdown to wzorzec identyczny z systemem zarządzania wiedzą w vaulcie: kontekst zakodowany w plikach referencyjnych sprawia, że AI pracuje spójnie bez powtarzania instrukcji w każdym prompcie.
- Bariera wejścia technicznego szybko znika — narzędzia opisane przez [[Ahrefs]] były 6 miesięcy temu niedostępne dla non-developerów; dziś większość da się opisać po angielsku [[Claude Code|Claude]] i mieć działającą wersję w ciągu dnia.

## Cytat
> AI naprawdę wkłada „manager" z powrotem do „Content Marketing Manager". Operujemy teraz na wyższym poziomie abstrakcji.

## Zastosowanie
Dla klientów NGO: architektura Content OS to zbyt techniczna, ale idea "source of truth" w Markdown (profil organizacji, lista programów, tone of voice) jest transferowalna natychmiast — to dokładnie wzorzec pliku kontekstu w Cowork. Dla dobryai.pl: ten artykuł to gotowy materiał do case study „jak AI zmienia rolę content marketera" i punkt startowy dla szkolenia z AI dla komunikatorów NGO. Warto śledzić [[Ahrefs]] jako laboratorium praktyczne — ich publiczne blueprinty to rzadkie okno na zaawansowane wdrożenia AI w treściach.
