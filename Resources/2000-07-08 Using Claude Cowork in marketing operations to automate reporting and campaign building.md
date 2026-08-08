---
categories:
  - Clippings
authors:
  - '[[Anthropic]]'
url: >-
  https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds
source: >-
  [[Archives/2000-07-08 Using Claude Cowork in marketing operations to automate
  reporting and campaign building|2000-07-08 Using Claude Cowork in marketing
  operations to automate reporting and campaign building]]
published: '2000-07-08'
created: '2026-08-04'
relevance: wysoka
tags:
  - automatyzacja
  - narzędzia-AI
  - context-engineering
---
# Using Claude Cowork in marketing operations to automate reporting and campaign building

Case study Anthropic pokazuje, jak zespół marketing operations (Ian Chan, Annabel Custer) wykorzystał [[Claude Cowork]] do automatyzacji dwóch pracochłonnych procesów: cotygodniowego raportu metryk marketingowych oraz budowy infrastruktury kampanii (CRM, marketing automation, event platform). Kluczem nie był jeden duży skrypt, lecz zestaw wyspecjalizowanych skilli połączonych z zaplanowanymi zadaniami (scheduled tasks) i konektorami do istniejących narzędzi. Praca, która wcześniej zajmowała 1-2 dni tygodniowo, skróciła się do 1-2 godzin, a rola ludzi przesunęła się z klikania po systemach w stronę walidacji, enablementu i pracy nad jakością danych. Artykuł jest też praktycznym przewodnikiem po budowaniu takich workflow: od proofreading skill po dispatcher skill rozdzielający zadania między specjalistyczne skille.

## Frameworki i metody

**Architektura workflow z Claude Cowork (na przykładzie dwóch zespołów):**

1. **Raportowanie tygodniowe (Ian Chan)** — zaplanowane zadanie w niedzielny wieczór czyta poprzedni raport, transkrypcję ostatniego spotkania, Slacka i zapytania do hurtowni danych, a w poniedziałek zostawia gotowy szkic z tabelami metryk i sugerowanymi kierunkami narracji. Opiera się na 3 skillach: prep skill (składanie raportu), proofreading skill (weryfikacja każdej liczby wobec źródła), action-items skill (zamiana ustaleń na zadania w Asanie).
2. **Budowa eventów (Annabel Custer)** — dispatcher skill co godzinę czyta kanał zgłoszeń, wybiera najpilniejsze zadanie i przekazuje je jednej z pięciu wyspecjalizowanych skilli (event-build, webinar landing page, apply-to-attend, approval-support, data-import). Po zakończeniu budowy osobny agent audytowy — uruchamiany bez wcześniejszego kontekstu — testuje rejestrację na żywej stronie i weryfikuje e-mail potwierdzający, zanim zadanie zostanie oznaczone jako zakończone.
3. **Zasady wdrażania (rekomendacje Anthropic):** zamieniaj powtarzające się korekty w skille; zbuduj najpierw skill do proofreadingu (weryfikacja liczb wobec źródła); po każdym uruchomieniu nowego workflow pytaj Claude, co było trudne w instrukcjach; korzystaj z zaplanowanych zadań (scheduled tasks) do pracy, o której nikt nie musi pamiętać.

## Kluczowe dane
- Raport tygodniowy: z 1-2 dni pracy tygodniowo do ok. 2 godzin.
- Proces budowy eventu obejmuje integrację min. 3 różnych platform (CRM, marketing automation, event management) — tradycyjnie ustawianych ręcznie po kolei.

## Wnioski
- Rozdzielenie ról — osobny dispatcher do routingu i osobne skille wykonawcze — pozwala rozwijać każdą część workflow niezależnie, bez ryzyka, że zmiana w jednym miejscu zepsuje resztę.
- Weryfikacja przez świeżego agenta bez wcześniejszego kontekstu (audit agent) to praktyczny wzorzec kontroli jakości, możliwy do przeniesienia na inne procesy oparte na AI.
- Największa wartość automatyzacji nie leży w oszczędności czasu samej w sobie, lecz w przesunięciu uwagi ludzi na walidację, jakość danych i pracę strategiczną.

## Cytat
> Kiedy zauważysz, że poprawiasz Claude w tej samej sprawie więcej niż raz, ta poprawka powinna trafić do skilla.

## Zastosowanie
Bezpośrednio przekłada się na projekt budowania Second Brain w strukturze EPARAX i pluginy Claude Code — wzorzec „dispatcher + wyspecjalizowane skille + osobny agent audytujący" można zastosować przy własnych narzędziach AI do pracy z klientami NGO. Warto też wdrożyć praktykę „po każdym uruchomieniu pytaj, co było niejasne w instrukcjach" jako stały element rozwijania własnych skilli.
