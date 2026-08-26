---
type: "Web"
authors: "[[Kasia Szczesna]]"
url: "https://behavioralinsight.substack.com/p/a-process-doesnt-have-a-single-level?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-08-24
created: 2026-08-25
tags:
  - "strategia-AI"
  - "automatyzacja"
  - "strategia-organizacji"
---


#### A review of nearly a decade of research on Human–AI Interaction shows that the question “what should we automate?” is simply too broad. What matters much more is how control, responsibility, and human capability shift across different stages of the process.

This article is based on research that I translated with the help of a model (unfortunately, I don’t speak Chinese:)  
Enjoy the read,  
Kasia ❤

![](https://substackcdn.com/image/fetch/$s_!G8bL!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd579951f-dc53-47ca-a5c8-9f97cd8f7c1a_1200x1500.png)

### What you’ll learn from this article:

- why “what should we automate?” may be too broad a question,
- how having a human in the loop differs from giving that human meaningful influence over a decision,
- how control and responsibility should shift across different stages of a process,
- when AI strengthens human capability and when it starts to replace it,
- why mapping human behavior should come before calibrating the role of AI.

I recently read a review by a team from **Zhejiang University** summarizing nearly a decade of their work on human–AI interaction. It introduces a concept that, for me, organizes this problem better than almost anything I have recently seen in AI implementation materials. They call it **bidirectional empowerment**, and it consists of three elements. **Human-Centered Human–AI Interaction (HCHAC)** asks two fundamental questions: **in which direction does empowerment flow** and **who holds control at a given stage?**

The 3 mechanisms within **HCHAC** translate into three questions that can be asked separately for each stage of a workflow, rather than once for the task as a whole:

1. **Vertical leadership (human over AI).**  
	**Where in this workflow is the decision that a human cannot delegate?**  
	The authors specifically point to ethical judgments and strategic choices. In product terms, this becomes a practical question: which step requires a hard stop rather than simply an option to undo what has already happened?
2. **Transformational leadership (AI empowers the human).**  
	**Does this step increase the user’s capability, or replace it?**  
	If, after three months of using the tool, the user performs the task worse without it than they did before adopting it, then what was described as empowerment was, in reality, substitution.
3. **Shared responsibility.**  
	**How does the allocation of responsibility change across different stages?**  
	This is where I see the greatest practical value, because it challenges the implicit assumption that a task has one level of automation. A real workflow consists of stages with very different profiles: gathering information may operate as System 0, interpretation as System 2, and drafting as System 1. A pattern card designed for the “entire task” will therefore always be miscalibrated for at least one stage.

![](https://substackcdn.com/image/fetch/$s_!SOax!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe72389ab-a9e1-46b3-a8b1-8b4e4f4d52e8_1536x1024.jpeg)

## This is not the same as human-in-the-loop

It is easy to confuse bidirectional empowerment with the human-in-the-loop principle, but they are not the same thing, and the distinction matters in practice. Human-in-the-loop tells us that a human is present. It does not tell us why that person is there or whether their presence actually changes anything. You can technically meet the requirement by adding an approval button and then end up with logs showing a 100% approval rate, which tells you exactly one thing: nobody has ever rejected anything. Presence without influence is hardly oversight.

Bidirectional empowerment asks a more difficult question:

> **At this point, can the human genuinely change the course of what happens, and do they have enough information and understanding to make that decision?**

There is a simple test for this, and I recommend running it after a quarter rather than only during the planning phase. Check whether the team can perform the task without the tool better or worse than they could before implementation. If they perform worse, it was not empowerment.

## A process is not a single block

In workshops and training sessions that I take part in myself, almost the same question comes up every time at the beginning: what do we want to automate?

I understand where it comes from. It is concrete, it produces a list, and a list can be priced, scoped, and put into a budget. But the question already contains an answer. It assumes that a process is a single block that is either automated or not, and that we already know where the value sits within that block and where the risk lies.

Usually, we do not, because nobody has yet looked at the process from the perspective of the people actually working within it.

A diagram on a slide may have four boxes and three arrows. Reality contains hundreds of microbehaviors that cannot be predicted from behind a desk. Someone scans the output instead of reading it because the model was right the last two times. Someone else checks everything line by line because they trusted it once, got burned, and never forgot it. Someone exports the output into a spreadsheet because that is the only place where they can see the whole picture at once. Someone asks a colleague from another team instead of asking the system. Nobody reports these behaviors because nobody considers them “work,” and yet this is exactly what the process is made of.

There is also something else that perhaps was not yet such a significant problem two years ago. People within the same team are now at completely different stages of maturity with this technology. One person works with a model every day and has already developed a sense for when not to trust it. Another has used it three times and either accepts everything without checking or avoids it entirely. The same stage of the process, the same role in the organization, two completely different behaviors. One level of automation will not work for both, because for one person it will be too permissive and for the other too restrictive.

We can call this a difference in maturity and move on, but that is not enough. Maturity is itself a variable that changes over time, which means a calibration performed once will stop fitting six months later, regardless of how well it was designed at the beginning.

## That is why I map before I calibrate

In my **[BehaviorAI Design Framework](https://www.kasiaszczesna.pl/behaviorai-design-framework)**[,](https://www.kasiaszczesna.pl/behaviorai-design-framework) these are two separate steps, and the order is not cosmetic.

During the mapping stage, I break the workflow down into phases and look at what actually happens to the human in each one. Not what is supposed to happen according to the documented procedure, but what actually happens. Where does the person genuinely make a decision? Where are they merely approving someone else’s decision? Where have they already stopped paying attention, even though they remain formally accountable? Where do they bypass the system because working without it is faster?

Only during the calibration stage do I determine how much collaboration with AI makes sense in each individual phase and at which points the decision needs to return to the human.

If you start with calibration, you end up with one slider for the entire process, which brings you right back to where you started. I connect all of this with a behavioral science perspective through **Fast and Slow Collaborative AI**.

## What we still do not know

I am leaving this for the end because I believe an article like this should also be clear about its limitations.

The authors of the review explicitly point out what is still missing. We do not yet have strong strategies for dynamically transferring control between humans and AI systems, which happens to be one of the most difficult problems in practice. We also lack long-term data, which means outcomes such as skill degradation or growing cognitive dependence are still poorly measured. The authors themselves acknowledge that we know less about these effects than we would like to.

That is certainly not a reason to stop implementing AI. For me, it is a reason to define the allocation of control deliberately, phase by phase, and revisit it after a quarter rather than setting one automation level at the beginning and never touching it again.

Because the better question to ask at the start is not “what should we automate?” but “what is happening to the human here before we change anything?”

### If you’re working on a similar challenge

If you’re designing a process where AI is meant to support people in making decisions, it is worth first looking at what actually happens to the human at each stage of the work.

That is where I start when working with teams through the BehaviorAI Design Framework. If this way of thinking reflects some of the challenges you’re working on, I’d be happy to talk!  
Kasia

---

*[Based on: Gao, Z., Zhao, Y., Pan, H., Xu, W. (2026). Toward Human-Centered Human–AI Interaction: Advances in Theoretical Frameworks and Practice. arXiv:2601.11812](https://arxiv.org/abs/2601.11812)*

*[www.kasiaszczesna.pl](https://www.kasiaszczesna.pl/)*

## Proces nie ma jednego poziomu automatyzacji

#### W jakim miejscu procesu decyzję powinien podejmować człowiek, gdzie AI może go wspierać, a gdzie przejąć większą część pracy? Przegląd blisko dekady badań nad Human–AI Interaction pokazuje, że pytanie „co zautomatyzować?” jest po prostu zbyt ogólne. Dużo ważniejsze jest to, jak zmienia się podział kontroli, odpowiedzialności i kompetencji na kolejnych etapach procesu.

![](https://substackcdn.com/image/fetch/$s_!v_ab!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f218145-8643-4786-9139-b12196843e09_1200x1500.png)

Ten tekst powstał na podstawie badania, które tłumaczyłam z modelem (niestety nie znam chińskiego:)

Miłego czytania,  
Kasia ❤

### Z tego artykułu dowiesz się:

- dlaczego pytanie „co zautomatyzować?” może być zbyt ogólne na początku wdrożenia AI,
- czym różni się obecność człowieka w pętli od realnego wpływu na decyzję,
- jak zmieniać poziom kontroli i odpowiedzialności między kolejnymi fazami procesu,
- kiedy AI wzmacnia kompetencje człowieka, a kiedy zaczyna je zastępować,
- dlaczego w BehaviorAI Design Framework najpierw mapuję zachowania, a dopiero później kalibruję rolę AI.

Czytałam ostatnio przegląd zespołu z Uniwersytetu Zhejiang, który podsumowuje blisko dekadę ich prac nad interakcją człowieka z AI. Jest tam pojęcie, które porządkuje ten problem lepiej niż wszystko, co ostatnio widziałam w materiałach wdrożeniowych. Nazywają to dwukierunkowym wzmocnieniem i składa się z trzech rzeczy.**Human-Centered Human–AI Interaction (HCHAC)** odpowiada na pytanie: **w którą stronę** **płynie wzmocnienie** i **kto trzyma władzę w danej fazie**.

Trzy mechanizmy z **HCHAC** przekładają się na 3 pytania, które można zadać osobno dla każdej fazy przepływu, a nie raz dla całego zadania:

1. **Przywództwo wertykalne (człowiek nad AI).**
	**Gdzie w tym przepływie leży decyzja, której człowiek nie może oddać?**  
	Autorzy wskazują konkretnie oceny etyczne i wybory strategiczne. W produkcie to się przekłada na pytanie: który krok musi mieć twardy punkt zatrzymania, a nie tylko możliwość cofnięcia.
2. **Przywództwo transformacyjne (AI wzmacnia człowieka).**  
	**Czy ten krok podnosi zdolność użytkownika, czy ją zastępuje?**  
	Jeśli po trzech miesiącach korzystania użytkownik radzi sobie z zadaniem gorzej bez narzędzia niż na starcie, deklarowane wzmocnienie było w rzeczywistości substytucją.
3. **Współdzielona odpowiedzialność.**  
	**Jak alokacja zmienia się między fazami?**  
	Tu jest najważniejsza korzyść praktyczna, bo rozbija milczące założenie, że zadanie ma jeden poziom automatyzacji. Realny przepływ ma fazy o różnym profilu: zbieranie materiału może być System 0, interpretacja System 2, redakcja System 1. Karta wzorca zaprojektowana pod „całe zadanie” zawsze będzie źle skalibrowana w co najmniej jednej fazie.

![](https://substackcdn.com/image/fetch/$s_!DDYy!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d48fceb-2739-474d-ab74-eed1eaa93d4d_1536x1024.jpeg)

## To nie to samo co człowiek w pętli

Łatwo pomylić dwukierunkowe wzmocnienie z zasadą człowieka w pętli, ale to inne rzeczy i różnica ma znaczenie praktyczne.

Człowiek w pętli mówi, że człowiek jest obecny. Nie mówi, po co tam jest i czy jego obecność cokolwiek zmienia. Można spełnić ten warunek, wstawiając przycisk zatwierdzenia i mieć w logach sto procent zatwierdzeń, co znaczy dokładnie tyle, że nikt nigdy nic nie odrzucił. Obecność bez wpływu to raczej żaden nadzór.

Dwukierunkowe wzmocnienie zadaje trudniejsze pytanie:

> **czy w tym punkcie człowiek naprawdę może zmienić bieg sprawy, i czy ma z czego tę decyzję podjąć?**

Jest do tego prosty test, który polecam robić po kwartale, a nie na etapie planowania. Sprawdź, czy zespół radzi sobie z zadaniem bez narzędzia lepiej niż przed wdrożeniem, czy gorzej. Jeśli gorzej, to nie było wzmocnienie.

## Proces nie jest jednym blokiem

Na warsztatach czy szkoleniach w których sama biorę udział, prawie zawsze pada to samo pytanie na start: co chcemy zautomatyzować.

Rozumiem, skąd się bierze. Jest konkretne, prowadzi do listy, a listę da się wycenić i wpisać do budżetu. Tylko że ono już zawiera odpowiedź. Zakłada, że proces to jeden blok, który albo się automatyzuje, albo nie, i że wiemy, gdzie w tym bloku siedzi wartość, a gdzie ryzyko.

Zwykle nie wiemy, bo nikt jeszcze nie spojrzał na ten proces od strony ludzi, którzy w nim siedzą.

Diagram na slajdzie ma cztery pola i trzy strzałki. Rzeczywistość ma setki mikrozachowań, których zza biurka nie da się przewidzieć. Ktoś skanuje wynik wzrokiem zamiast go czytać, bo 2 razy się zgadzało. Ktoś inny sprawdza wszystko po kolei, bo raz się sparzył i już nie zapomniał. Ktoś eksportuje do arkusza, bo tam widzi całość naraz. Ktoś pyta koleżankę z drugiego zespołu, zamiast pytać system. Nikt tego nie zgłasza, bo nikt tego za pracę nie uważa, a przecież właśnie z tego składa się proces.

Do tego dochodzi coś, co może 2 lata temu nie było jeszcze problemem. Ludzie w jednym zespole są dziś na całkiem różnym etapie z tą technologią. Jedna osoba pracuje z modelem codziennie i ma już wyczucie, kiedy mu nie ufać. Druga widziała go trzy razy i albo przyjmuje wszystko bez sprawdzania, albo nie tyka wcale. Ta sama faza procesu, ta sama rola w strukturze, dwa całkiem inne zachowania. Jeden poziom automatyzacji nie obsłuży obu, bo dla jednej osoby będzie zbyt luźny, a dla drugiej zbyt ciasny.

Można to nazwać różną dojrzałością i przejść dalej, ale to za mało. To zmienna, która sama się zmienia w czasie, więc kalibracja zrobiona raz przestanie pasować po pół roku, i to niezależnie od tego, jak dobrze została zrobiona na starcie.

## Dlatego mapuję przed kalibracją

W moim **[BehaviorAI Design Framework](https://www.kasiaszczesna.pl/behaviorai-design-framework)** to są dwa osobne kroki i kolejność nie jest kosmetyczna.

W kroku mapowania rozkładam przepływ na fazy i patrzę, co się w każdej z nich dzieje z człowiekiem. Nie co powinno się dziać zgodnie z procedurą, tylko co się dzieje. Gdzie faktycznie podejmuje decyzję. Gdzie tylko zatwierdza cudzą. Gdzie już przestał patrzeć, choć formalnie nadal odpowiada. Gdzie obchodzi system, bo szybciej mu bez niego.

Dopiero w kroku kalibracji ustalam, ile współpracy z AI ma sens w każdej fazie osobno i w którym punkcie decyzja musi wrócić do człowieka.

Jeśli zaczniesz od kalibracji, dostaniesz jeden suwak dla całego procesu, czyli wrócisz tam, skąd wyszłaś lub wyszedłeś. Wszystko to łączę z podejściem nauk behawioralnych - Fast and Slow Collaborative AI.

## Czego jeszcze nie wiemy

Zostawiam to na koniec, bo uważam, że taki tekst powinien mówić też o swoich granicach.

Autorzy przeglądu sami wskazują, czego brakuje. Nie mamy dobrych strategii dynamicznego przekazywania kontroli między człowiekiem i systemem, czyli akurat tego, co w praktyce jest najtrudniejsze. Nie mamy też danych z długiego okresu, więc skutki takie jak degradacja kompetencji albo narastająca zależność poznawcza są dziś słabo zmierzone. Sami przyznają, że wiedzą o tym mniej, niż by chcieli.

To z pewnością nie powód, żeby wstrzymywać wdrożenia. Dla mnie osobiście jest to powód, żeby rozpisać alokację świadomie, fazami, i wrócić do niej po kwartale zamiast ustawiać jeden suwak na starcie i już nigdy go nie ruszać.

## Jeśli pracujesz nad podobnym wyzwaniem

Jeśli projektujesz proces, w którym AI ma wspierać ludzi w podejmowaniu decyzji, warto najpierw zobaczyć, co naprawdę dzieje się z człowiekiem na poszczególnych etapach pracy.

Właśnie od tego zaczynam pracę z zespołami w ramach BehaviorAI Design Framework. Jeśli ten sposób myślenia jest bliski wyzwaniom, nad którymi pracujecie, chętnie porozmawiam!

---

*[Based on: Gao, Z., Zhao, Y., Pan, H., Xu, W. (2026). Toward Human-Centered Human–AI Interaction: Advances in Theoretical Frameworks and Practice. arXiv:2601.11812](https://arxiv.org/abs/2601.11812)*

*[www.kasiaszczesna.pl](https://www.kasiaszczesna.pl/)*