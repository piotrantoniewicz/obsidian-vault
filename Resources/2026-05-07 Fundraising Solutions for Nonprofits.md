---
categories:
  - Clippings
authors: ["[[Click & Pledge]]"]
url: "https://clickandpledge.com/blog/pci-and-soc-2-the-gap-between-compliant-and-secure/"
source: "[[Archives/2026-05-07 Fundraising Solutions for Nonprofits|2026-05-07 Fundraising Solutions for Nonprofits]]"
published: 2026-05-07
created: 2026-07-09
relevance: wysoka
tags:
  - "fundraising"
  - "strategia-organizacji"
---

# Fundraising Solutions for Nonprofits

Click & Pledge tłumaczy różnicę między dwoma standardami bezpieczeństwa istotnymi dla platform fundraisingowych — PCI DSS (dane kart płatniczych) i SOC 2 Type II (kontrole organizacyjne wokół danych darczyńców) — i pokazuje, że fraza "PCI compliant" nie oznacza tego samego dla każdego dostawcy: samoocena (Self-Assessment Questionnaire) i pełny audyt Level 1 przez niezależnego audytora (QSA) obie uprawniają do tej etykiety, mimo drastycznie różnego poziomu rzetelności. Główna teza: organizacje społeczne działają w "gospodarce zaufania" i powinny żądać od dostawców dowodów dopasowanych do architektury systemu, nie deklaracji marketingowych — bo naruszenie danych osobowych darczyńców jest wydarzeniem relacyjnym, nie tylko finansowym, i nie da się go "wydać ponownie" jak karty płatniczej.

## Frameworki i metody

**Poziomy walidacji PCI DSS wg wolumenu transakcji (merchant vs. service provider):** platforma fundraisingowa jest service providerem, nie merchantem — próg Level 1 dla service providera to 300 000 transakcji rocznie (audyt QSA obowiązkowy), podczas gdy dla merchanta to 6 mln — dwudziestokrotna różnica. Dostawca przetwarzający miliony transakcji, ale klasyfikujący się jako merchant, buduje zgodność na złym fundamencie.

**Model dojrzałości dowodów (Tier 0-3) do oceny dostawców:**
1. **Tier 0** — deklaracje marketingowe ("PCI compliant", "bank-level security") bez dokumentacji — praktycznie bez znaczenia.
2. **Tier 1** — atestacja bez jasności zakresu (np. sam SAQ lub SOC 2 Type I) — papiery bez kontekstu.
3. **Tier 2** — dowody dopasowane do architektury: jasny opis przepływu płatności, odpowiednia walidacja PCI, aktualny SOC 2 Type II z określonym zakresem, zobowiązania reagowania na incydenty.
4. **Tier 3** — Tier 2 plus ciągły monitoring, testowany plan reagowania na incydenty, ochrona strony płatności przed manipulacją, testy penetracyjne, wymuszone MFA dla kont administracyjnych.

**Pytania, jakie zarząd organizacji powinien zadawać dostawcom:** gdzie żyją dane osobowe darczyńców i kto może je eksportować masowo; jakie niezależne dowody (raporty SOC 2 Type II, poziom walidacji PCI) dostawca dostarcza; jak chronione są strony donacyjne przed e-skimmingiem; czy dostawca waliduje się jako service provider czy merchant; czy plan reagowania na incydenty był faktycznie testowany, nie tylko spisany.

## Kluczowe dane
- Próg Level 1 dla service providera: 300 000 transakcji rocznie vs. 6 mln dla merchanta (20-krotna różnica)
- Roczny koszt pełnej walidacji Level 1 u Click & Pledge: ok. 200 000 USD (audyty QSA, testy penetracyjne, ciągły monitoring)
- PCI DSS 4.0 (pełne wejście w życie marzec 2025) wprowadza obowiązkowe wymogi 6.4.3 i 11.6.1 dot. ochrony skryptów na stronach płatności przed e-skimmingiem

## Wnioski
- "PCI compliant" to fraza bez wskazania rygoru — organizacja społeczna musi pytać nie "czy jesteście zgodni", tylko "zgodni jako kto, na jakim poziomie i kto to zwalidował".
- PCI DSS i SOC 2 adresują dwa różne ryzyka: kompromitację strony płatności (zdarzenie finansowe) i wyciek danych osobowych darczyńców (zdarzenie relacyjne, bez możliwości "reissue") — dostawca może mieć zgodność PCI i zero kontroli nad dostępem do bazy darczyńców.
- Zabezpieczenie bramki płatności (Stripe, PayPal) nie chroni automatycznie organizacji — jeśli formularz donacyjny jest budowany samodzielnie, to organizacja odpowiada za bezpieczeństwo własnego serwera i kodu wokół formularza.

## Zastosowanie
Gotowy zestaw pytań (Tier 0-3, service provider vs. merchant, SOC 2 Type II) do wykorzystania przy doradztwie dla organizacji społecznych wybierających lub audytujących platformę fundraisingową — szczególnie przydatny przy pracy z klientami przetwarzającymi dane darczyńców i płatności cykliczne. Można zaadaptować jako checklistę due diligence dostawcy do materiałów szkoleniowych o fundraisingu cyfrowym.
