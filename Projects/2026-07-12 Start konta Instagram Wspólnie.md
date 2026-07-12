---
categories:
  - Project
status: Aktywny
created: 2026-07-12
due: 2026-12-31
area: "[[Digital campaigning]]"
tags:
  - digital-campaigning
  - content-marketing
---

# Start konta Instagram Wspólnie

Uruchomić konto **@wspolnie** na Instagramie (progresywne treści: Polska — polityka, prawa, przestrzenie pozapolityczne) wraz z tygodniowym workflow treści: AI robi research i szkice, człowiek decyduje i publikuje. Sukces = profil opublikowany z pierwszymi postami i **stabilny tygodniowy rytm** (`/research-tygodnia` → publikacja) działający przez co najmniej 2–3 cykle.

**Tempo celowo niespieszne — to nie jest priorytet.** Strategia audience-first zakłada budowę przez miesiące; Faza 2 (organizacja + lista mailowa) najwcześniej na przełomie 2026/2027 i jest poza zakresem tego projektu. W Fazie 1 świadomie **bez listy mailowej** (decyzja z czerwca 2026).

**Stan (2026-07-12):** marka gotowa (logo 2026, paleta, szablony postów w Canvie), workflow subagentów Claude Code zaimplementowany (5 agentów + orkiestrator `/research-tygodnia`), ale jeszcze nie przetestowany. Równolegle działa chmurowy agent Managed Agents (cotygodniowy research, do wygaszenia po stabilizacji lokalnego workflowu).

## Kolejne kroki
- [ ] Pierwszy testowy cykl `/research-tygodnia` — do końca **sierpnia 2026**
- [ ] Migracja treści z `system-prompt.md` do `context/` (jedno kanoniczne źródło) — przy okazji testowego cyklu
- [ ] `skrypty/generator-kafelkow.py` (do tego czasu grafiki ręcznie w Canvie) — **wrzesień–październik 2026**
- [ ] Finalne bio + struktura profilu (highlighty, plan pierwszych postów) — **październik 2026**
- [ ] Soft launch: pierwsze posty na koncie — **jesień 2026** (październik–listopad)
- [ ] Wygaszenie Managed Agents (deployment/cron) — po 1–2 stabilnych cyklach lokalnego workflowu
- [ ] Opcjonalnie: test badge'a w 48 px + mockup profilu (avatar + siatka 9 postów)

## Powiązane zasoby
- `~/Projekty/Instagram/` — folder roboczy i źródło prawdy: `CLAUDE.md` (workflow, marka, zasady), `NOTATKI-PROJEKTU.md` (dziennik decyzji), `branding.md`, `context/`, `szablony/`, `workflow-subagenci.md`
- [[Digital campaigning]] — obszar nadrzędny
- [[digital-campaigning]] · [[content-marketing]] — domeny tematyczne

## Log decyzji
- 2026-07-12 — utworzenie huba projektu w vaultcie (źródło prawdy treści i stanu pozostaje w `~/Projekty/Instagram`). Routing: Project (ma metę — konto wystartowało + stabilny rytm publikacji), pod nowym obszarem [[Digital campaigning]]. Terminy rozpisane rozmyślnie luźno: projekt nie jest priorytetem, a strategia audience-first nie wymaga pośpiechu.
- 2026-07-12 — folder roboczy przeniesiony z `~/Documents/Instagram` do `~/Projekty/Instagram` (reorganizacja: wszystkie projekty w `~/Projekty`); ścieżki w plikach projektu zaktualizowane. W `~/Documents/Instagram` została stara kopia — do ręcznego usunięcia.
- 2026-06 (przeniesione z notatek) — Faza 1 = czysta budowa zasięgu **bez listy mailowej**; mailing dopiero w Fazie 2, gdy powstanie organizacja.
