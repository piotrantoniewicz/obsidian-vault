---
type: Web
authors: '[[Kasia Szczesna]]'
url: >-
  https://behavioralinsight.substack.com/p/why-no-compliance-test-will-catch?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true
published: 2026-08-12T00:00:00.000Z
created: 2026-08-13T00:00:00.000Z
tags:
  - strategia-AI
  - produkty-cyfrowe
  - LLM
---


![](https://substackcdn.com/image/fetch/$s_!huG5!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd5bc55d-2d49-438d-80d6-d1ff3170f8f7_1800x2250.png)

> *“This article is based on my own research, structure, and choice of sources. I used Claude for editing and refining the text. I take responsibility for it, just as I do for my other products* 😉” Kasia

Product teams look at the screen and see what they designed. They rarely see what’s missing, even though those gaps are usually what costs the most: lost trust, a bad decision by the user, a regulator’s fine. Three of these gaps are especially sneaky, because each one can exist in a product that’s fully legal, fully tested, and shipped to production with a clean conscience across the whole team.

The common thread these days shows up most often around **Article 50 of the AI Act**, the provision requiring users to be told when they’re interacting with an AI system. But this isn’t a piece about that provision. It’s about what happens in a person’s head, regardless of which exact rule happens to be in force, and why a product can pass every compliance test and still fail at the exact moment it was supposed to protect the user.

## Gap 1: Exposure time

Researchers studying warning labels on cigarette packs looked at what happens when a warning is visible for only seven seconds, compared to a longer exposure. The result: that short a window was enough for the warning to formally appear, and nowhere near enough for its content to be consciously processed and remembered.

Placement matters enormously here. In one study conducted in Canada, moving the same warning from the bottom of the pack to the top raised its recognition among smokers from twenty percent to ninety-five percent. Same content, same size, different placement, completely different outcome.

A short exposure window is enough to formally satisfy the requirement to show information, and nowhere near enough for that information to actually be processed.

**Where a message appears determines its effectiveness more than what it says.** Article 50 says nothing about placement, only about presence.

## Gap 2: Habituation

Research using fMRI on habituation to safety warnings shows something surprisingly fast. Activity in the visual centers of the brain responsible for processing these messages drops sharply after just the first few exposures. Not the tenth. Much earlier.

In the same line of research, a three-week field experiment showed that adherence to warnings dropped steadily with every additional day of using the app. Interestingly, messages that changed their appearance each time, so-called polymorphic warnings, turned out to be far more resistant to this decline than static messages that looked identical every time.

The same message, in the same form, stops being genuinely registered after very few exposures, much sooner than most product teams intuitively assume.

**How a message’s form changes over time, not just whether it’s present, determines whether it survives habituation.**

**Article 50 requires that the information appear no later than the first interaction, but says nothing about what should happen to it by the fifth or the fiftieth.**

## Gap 3: Context mismatch

The third mechanism is the least intuitive, and the most important for products where AI plays the role of a companion or confidant. Research into how people treat computers points to what the literature calls the Computers Are Social Actors paradigm. People automatically apply the same social rules to computer systems that they apply to other people, including politeness, expectations of reciprocity, and attributing personality, even when they’re fully aware they’re talking to a machine. Knowing the fact doesn’t switch off the automatic social response.

That’s exactly why an AI label in an app built around relationship falls so flat. Research on parasocial bonds with AI shows that users disclose information to AI systems at a level of intimacy that sometimes exceeds what they share with other people, precisely because the entire interaction design, personalized language, emotional responsiveness, consistency over time, activates the same cognitive pattern as a real relationship. The label saying “this is AI” is one sentence. The rest of the experience is hundreds of signals pointing the other way.

**Knowing factually that you’re talking to a system doesn’t switch off the automatic social response that system triggers.** **These are two separate processes in the brain, not one.**

**The more strongly a product builds the impression of a relationship, the harder it works against its own transparency label, no matter how clearly that label is worded.**

## What these three mechanisms have in common

A standard rollout process checks whether the message exists, whether the wording is correct, whether the provision is formally satisfied. None of the three mechanisms above is a question of whether the message exists. They’re about how long it’s visible, how often it repeats, and how strong a context it’s competing against.

**That’s why a product can pass every legal test and still fail in real use.** **And the team that built it may genuinely have no idea they missed anything, because the checklist they used never asked these questions.**

## 2 patterns that follow from this

**Exposure scaled to risk.**  
The more serious the potential consequence of an interaction, the longer and more visibly the AI message should stay on screen, instead of disappearing in a fraction of a second like most notifications. On the interface, this can mean:

- briefly slowing the transition into a conversation,
- forcing a minimum amount of eye contact with the message, proportional to what’s actually at stake in that interaction.

**A signal that varies over time.**  
Instead of one static AI label shown only at the start, the message changes form on the user’s subsequent visits, so it doesn’t become part of the background the brain has already learned to skip. On the interface, this means:

- rotating the form, placement,
- wording of the message at regular intervals, not a one-time rollout that’s then forgotten.

The third mechanism, context mismatch, needs a separate approach, because it can’t be solved with a single interface element. It requires a product-level decision about whether the degree of personalization and emotional responsiveness crosses a line at some point, past which no label can restore the right distance anymore.

## What to do about it

Compliance with the letter of the law and real protection for the user are two separate things, and companies designing human-AI collaboration need both at once: an audit that looks at the product through the lens of human behavior, not just a checklist, and an approach to designing human-AI interaction that accounts for these three mechanisms from the first sketch, instead of bolting them on at the end as a single line of label text.

**[BehaviorAI Design Framework](https://www.kasiaszczesna.pl/behaviorai-design-framework)** and **[BehaviorAI](http://behaviorai.eu/)** **exists to catch these 3 mechanisms before your users do, or your regulator does.**

This article is based on my own research, structure, and choice of sources. I used Claude for editing and refining the text. I take responsibility for it, just as I do for my other products 😉

Cheers,  
Kasia

---

## References

Lochbuehler, K., Wileyto, E.P., Mercincavage, M., Souprountchouk, V., Burdge, J.Z., Tang, K.Z., Cappella, J.N., Strasser, A.A. (2019). Temporal Effects of Message Congruency on Attention to and Recall of Pictorial Health Warning Labels on Cigarette Packages. *Nicotine & Tobacco Research*, 21(7), 879–886. [https://pmc.ncbi.nlm.nih.gov/articles/PMC6775858/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6775858/)

Hwang, J.E., Yang, Y.S., Oh, Y.M., et al. Differences in visual fixation duration according to the position of graphic health warning labels: An eye-tracking approach. *Tobacco Induced Diseases*. [https://www.tobaccoinduceddiseases.org/Differences-in-visual-fixation-duration-according-to-the-position-of-graphic-health,94327,0,2.html](https://www.tobaccoinduceddiseases.org/Differences-in-visual-fixation-duration-according-to-the-position-of-graphic-health,94327,0,2.html)

Vance, A., Jenkins, J.L., Anderson, B.B., Bjornn, D.K., Kirwan, C.B. (2018). Tuning Out Security Warnings: A Longitudinal Examination of Habituation Through fMRI, Eye Tracking, and Field Experiments. *MIS Quarterly*, 42(2), 355–380. [https://misq.umn.edu/misq/article/42/2/355/1716/Tuning-Out-Security-Warnings-A-](https://misq.umn.edu/misq/article/42/2/355/1716/Tuning-Out-Security-Warnings-A-Longitudinal)

Parasocial relationships with artificial intelligence (AI): A systematic review of benefits and risks. *ScienceDirect* (2026). [https://www.sciencedirect.com/science/article/pii/S2949882126000757](https://www.sciencedirect.com/science/article/pii/S2949882126000757)

## Dlaczego żaden test zgodności tego nie wyłapie. 3 luki, które ciężko wyłapać w produkcie \[AI\]

### Zespół przechodzi audyt prawny z czystym sumieniem. Produkt i tak zawodzi użytkownika dokładnie tam, gdzie miał go chronić.

![](https://substackcdn.com/image/fetch/$s_!ihCq!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2510bec-1a94-4c24-b4ed-3ee6dd39e452_1800x2250.png)

> *“Ten artykuł powstał w oparciu o mój research, strukturę i dobór źródeł. Do redakcji i dopracowania formy wykorzystałam Claude.  
> Biorę za niego odpowiedzialność jak i za swoje produkty.”* 😉*  
> Kasia*

Zespoły produktowe patrzą na ekran i widzą to, co zaprojektowały. Rzadko widzą to, czego tam nie ma, choć właśnie te braki najczęściej kosztują najwięcej: utracone zaufanie, złą decyzję użytkownika, karę regulatora. Trzy z tych luk są szczególnie podstępne, bo każda potrafi istnieć w produkcie formalnie zgodnym z prawem, w pełni przetestowanym, wysłanym na produkcję z czystym sumieniem całego zespołu.

Wspólny mianownik pojawia się dziś najczęściej przy okazji **artykułu 50 AI Act**, przepisu wymagającego informowania użytkownika o interakcji z systemem AI. Ale to nie jest tekst o tym przepisie. To tekst o tym, co dzieje się w głowie człowieka, niezależnie od tego, jaki dokładnie przepis akurat obowiązuje, i dlaczego produkt może przejść każdy test zgodności, a mimo to zawieść dokładnie w momencie, w którym miał chronić użytkownika.

## Luka 1: czas ekspozycji

Badacze badający ostrzeżenia na paczkach papierosów sprawdzili, co dzieje się, gdy komunikat jest widoczny tylko przez siedem sekund, w porównaniu z dłuższą ekspozycją. Wynik: tak krótki czas wystarczał, żeby ostrzeżenie formalnie się pojawiło, i jednocześnie zdecydowanie za mało, żeby jego treść została świadomie przetworzona i zapamiętana.

Umiejscowienie ma przy tym ogromne znaczenie. W jednym z badań przeprowadzonych w Kanadzie, przeniesienie tego samego ostrzeżenia z dołu opakowania na górę zwiększyło jego rozpoznawalność wśród palaczy z dwudziestu do dziewięćdziesięciu pięciu procent. Ta sama treść, ten sam rozmiar, inne miejsce, kompletnie inny wynik.

Krótki czas ekspozycji wystarczy, żeby formalnie spełnić wymóg pokazania informacji, i jednocześnie zdecydowanie za mało, żeby ta informacja została świadomie przetworzona.

**Miejsce, w którym pojawia się komunikat, decyduje o jego skuteczności silniej niż sama treść.** **Artykuł 50 nie mówi nic o umiejscowieniu, tylko o obecności.**

## Luka 2: habituacja

Badania z wykorzystaniem rezonansu magnetycznego nad przyzwyczajaniem się do komunikatów bezpieczeństwa pokazują coś zaskakująco szybkiego. Aktywność w wizualnych ośrodkach mózgu odpowiadających za przetwarzanie takich komunikatów gwałtownie spada już po pierwszych kilku ekspozycjach. Nie po dziesiątej, znacznie wcześniej.

W tym samym nurcie badań, eksperyment terenowy trwający 3 tygodnie pokazał, że przestrzeganie ostrzeżeń systematycznie spadało z każdym kolejnym dniem korzystania z aplikacji. Co ciekawe, komunikaty zmieniające swój wygląd za każdym razem, tak zwane ostrzeżenia polimorficzne, okazały się dużo bardziej odporne na ten spadek niż komunikaty statyczne, identyczne przy każdym pojawieniu się.

Ten sam komunikat, w tej samej formie, przestaje być realnie rejestrowany po bardzo niewielu ekspozycjach, znacznie szybciej, niż intuicyjnie zakłada większość zespołów produktowych.

**Zmienność formy komunikatu, nie tylko jego obecność, decyduje o tym, czy przetrwa on habituację.** **Artykuł 50 wymaga, żeby informacja pojawiła się najpóźniej przy pierwszej interakcji, ale nic nie mówi o tym, co ma się z nią dziać przy piątej czy pięćdziesiątej.**

## Luka 3: niedopasowanie kontekstu

3 mechanizm jest najmniej intuicyjny i najbardziej istotny dla produktów, w których AI odgrywa rolę towarzysza czy powiernika. Badania nad tym, jak ludzie traktują komputery, pokazują coś, co w literaturze funkcjonuje jako paradygmat komputerów jako aktorów społecznych. Ludzie automatycznie stosują wobec systemów komputerowych te same reguły społeczne, co wobec innych ludzi, włącznie z grzecznością, oczekiwaniami wzajemności czy przypisywaniem osobowości, nawet gdy w pełni świadomie wiedzą, że rozmawiają z maszyną. Świadomość faktu nie wyłącza automatycznej reakcji społecznej.

To dokładnie tłumaczy, dlaczego etykieta AI w aplikacji zbudowanej wokół relacji działa tak słabo. Badania nad więziami paraspołecznymi z AI pokazują, że użytkownicy ujawniają systemom AI informacje na poziomie intymności przewyższającym niekiedy to, co ujawniają innym ludziom, właśnie dlatego że cały projekt interakcji, spersonalizowany język, emocjonalna responsywność, konsekwencja w czasie, aktywuje ten sam schemat poznawczy, co prawdziwa relacja. Etykieta informująca, że to AI, jest jednym zdaniem. Reszta doświadczenia to setki sygnałów idących w przeciwnym kierunku.

**Wiedza faktyczna, że rozmawia się z systemem, nie wyłącza automatycznej reakcji społecznej, którą ten system wywołuje.** **To dwa osobne procesy w mózgu, nie jeden.**

**Im silniej produkt buduje wrażenie relacji, tym mocniej pracuje przeciwko własnej etykiecie transparentności, niezależnie od tego, jak jasno ta etykieta jest sformułowana.**

## Co łączy te 3 mechanizmy

Standardowy proces wdrożenia sprawdza, czy komunikat istnieje, czy tekst jest poprawny, czy przepis formalnie jest spełniony. Żaden z trzech mechanizmów opisanych wyżej nie jest kwestią istnienia komunikatu, tylko tego, jak długo jest widoczny, jak często się powtarza i z jak silnym kontekstem konkuruje.

**To dlatego produkt może przejść każdy test prawny i wciąż zawieść w realnym użyciu.** A zespół, który go budował, może szczerze nie mieć pojęcia, że coś przeoczył, bo checklistą, którą się posługiwał, nigdy nie zadawała tych pytań.

## 2 wzorce, które z tego wynikają

**Ekspozycja skalowana do ryzyka.**  
Im poważniejsza potencjalna konsekwencja interakcji, tym dłużej i bardziej widocznie komunikat o AI utrzymuje się na ekranie, zamiast znikać po ułamku sekundy jak większość powiadomień. Na interfejsie oznacza to na przykład:

- chwilowe spowolnienie przejścia do rozmowy,
- wymuszające minimalny czas kontaktu wzrokowego z komunikatem, proporcjonalnie do tego, o co toczy się interakcja.

**Sygnał zmienny w czasie.**  
Zamiast jednej, statycznej etykiety AI widocznej tylko na starcie, komunikat zmienia swoją formę przy kolejnych powrotach użytkownika, tak żeby nie stał się częścią tła, które mózg nauczył się pomijać już po pierwszych kontaktach. Na interfejsie oznacza to:

- rotację formy, miejsca,
- sformułowania komunikatu w regularnych odstępach, nie jednorazowe wdrożenie i zapomnienie o temacie.

Trzeci mechanizm, niedopasowanie kontekstu, wymaga osobnego podejścia, bo nie da się go rozwiązać jednym elementem interfejsu. Wymaga decyzji na poziomie całego produktu, czy stopień personalizacji i emocjonalnej responsywności nie przekracza w pewnym momencie granicy, po której żadna etykieta nie jest już w stanie przywrócić właściwego dystansu.

## Co z tym zrobić

Zgodność z przepisem i realna ochrona użytkownika to 2 osobne rzeczy, a firmy, które projektują współpracę człowieka z AI, potrzebują obu naraz: audytu, który patrzy na produkt oczami ludzkiego zachowania, nie tylko checklisty, oraz podejścia do projektowania interakcji człowiek-AI, które te 3 mechanizmy bierze pod uwagę od pierwszego szkicu, a nie dokleja na końcu w postaci jednego zdania etykiety.

**[BehaviorAI Design Framework](https://www.kasiaszczesna.pl/behaviorai-design-framework)** i **[BehaviorAI](http://behaviorai.eu/)** powstał dokładnie po to, żeby te trzy mechanizmy złapać, zanim zrobi to użytkownik albo regulator.

*Ten artykuł powstał w oparciu o mój research, strukturę i dobór źródeł. Do redakcji i dopracowania formy wykorzystałam Claude. Biorę za niego odpowiedzialność jak i za swoje produkty;)  
  
Pozdrowienia,  
Kasia*

---

## Bibliografia

Lochbuehler, K., Wileyto, E.P., Mercincavage, M., Souprountchouk, V., Burdge, J.Z., Tang, K.Z., Cappella, J.N., Strasser, A.A. (2019). Temporal Effects of Message Congruency on Attention to and Recall of Pictorial Health Warning Labels on Cigarette Packages. *Nicotine & Tobacco Research*, 21(7), 879–886. [https://pmc.ncbi.nlm.nih.gov/articles/PMC6775858/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6775858/)

Hwang, J.E., Yang, Y.S., Oh, Y.M., et al. Differences in visual fixation duration according to the position of graphic health warning labels: An eye-tracking approach. *Tobacco Induced Diseases*. [https://www.tobaccoinduceddiseases.org/Differences-in-visual-fixation-duration-according-to-the-position-of-graphic-health,94327,0,2.html](https://www.tobaccoinduceddiseases.org/Differences-in-visual-fixation-duration-according-to-the-position-of-graphic-health,94327,0,2.html)

Vance, A., Jenkins, J.L., Anderson, B.B., Bjornn, D.K., Kirwan, C.B. (2018). Tuning Out Security Warnings: A Longitudinal Examination of Habituation Through fMRI, Eye Tracking, and Field Experiments. *MIS Quarterly*, 42(2), 355–380. [https://misq.umn.edu/misq/article/42/2/355/1716/Tuning-Out-Security-Warnings-A-](https://misq.umn.edu/misq/article/42/2/355/1716/Tuning-Out-Security-Warnings-A-Longitudinal)

Parasocial relationships with artificial intelligence (AI): A systematic review of benefits and risks. *ScienceDirect* (2026). [https://www.sciencedirect.com/science/article/pii/S2949882126000757](https://www.sciencedirect.com/science/article/pii/S2949882126000757)
