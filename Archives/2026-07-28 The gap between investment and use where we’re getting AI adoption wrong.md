---
type: "Web"
authors: "[[Kasia Szczesna]]"
url: "https://behavioralinsight.substack.com/p/the-gap-between-investment-and-use?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-07-28
created: 2026-07-29
tags:
  - "strategia-AI"
  - "szkolenia-AI"
  - "trendy-AI"
---


*What you’ll learn from this article:*

- *why 95% of companies see no return on the money they’ve invested in AI, even as more of them use it than ever,*
- *what three behavioral, not technical, barriers explain why fully capable tools sit unused,*
- *what the recent Claude chat leak reveals about how easily trust in an interface gets miscalibrated,*
- *how to design the human’s role around AI step by step, so a rollout actually works.  
	*

![](https://substackcdn.com/image/fetch/$s_!Qjar!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd1f3d22-c6c8-4121-9ec6-b53acf5a0e93_1200x1500.png)

This March, business AI adoption crossed 50% of companies for the first time, according to the Ramp AI Index, up from 35% a year earlier. Stanford reports an even more optimistic figure: enterprise AI adoption rose to 88%, from just 55% two years earlier.

That should be good news, and it would be, if not for the second number sitting right next to it. According to McKinsey, only one percent of leaders describe their AI deployments as mature, and MIT Media Lab went a step further and calculated the actual return on investment: 95% of companies see no measurable return on the money they’ve put into AI.

Billions of dollars are flowing into tools that then sit unused, because half of all companies already have AI, and almost none of them know what to do with it.

## Why This Isn’t a Technology Problem

The first instinct in this situation is to blame the tool, to say it doesn’t have enough power, enough integrations, enough features. The data says otherwise. In a study on the state of AI in marketing, 78% of marketers named skills and training as their biggest barrier, not the technology itself.

That line is worth reading twice, because it’s easy to misread. “Skills and training” doesn’t mean people can’t click the right button. It means nobody taught them when AI should decide on its own, and when they should stop and think for themselves. So this isn’t a technical skills gap. It’s a gap in the language for making decisions.

A company buys a tool, rolls it out to one team, and three months in the tool works exactly as it should, yet people either don’t use it, or use it badly. Not because they’re lazy or resistant to change, but because nobody designed what their role toward that tool actually is. Adoption doesn’t fail at the point of purchase. It fails in day-to-day work, in the moment a person has to decide how much to trust what’s on the screen.

Underneath that one number sit three distinct barriers, and none of them is technical:

- **Incentives**: what people are actually driven by day to day doesn’t match what real collaboration with AI is supposed to look like.
- **Norms**: the unwritten rules about what’s “appropriate” to do yourself versus what can be handed to the system are unclear, or simply don’t exist.
- **Trust**: instead of being calibrated to the tool’s actual quality, it’s either blind or absent.

These three things, not computing power, are what decide whether a tool actually gets used.

### When Claude Itself Becomes the Example

Proof of how costly a poorly calibrated norm can be showed up this week, involving Claude itself. Futurism reported that thousands of conversations and projects users had shared via the “share” feature ended up indexed by Google, including patients’ medical records, children’s contact details, and internal company documents. The “share” button told users the link would be “public,” but it didn’t clearly say the content could be indexed and found by complete strangers, so people trusted a phrase that didn’t convey the full consequences. This is exactly the mechanism I keep writing about: the interface sent an incomplete signal, the norm around what’s safe to share was never made clear, and the cost of that gap landed on the people whose data ended up online, not on the company that designed the button.

## Bringing the Human Back Into the Loop, Without a Plan for What They’re Supposed to Do There

The same problem shows up from the other direction, in the world of agentic AI. After a wave of failures and cases of systems being hijacked through prompt injection, companies started returning to a model with a human in the decision loop. Researchers at MIT Sloan note that companies will maintain some level of human oversight as a safeguard for agentic AI, which undercuts the efficiency gains the technology promised in the first place.

That sentence contains exactly the same mistake I’ve been writing about for months. Companies add a “human in the loop” as a checkpoint without designing what that person is actually supposed to do there. An “approve” button on its own doesn’t create oversight. Oversight only exists in the moment a person has a real reason to stop, think, and sometimes say no. Without that design, oversight is a facade, and the “efficiency gains” companies claim to be losing were never real to begin with, because they rested on false trust rather than genuine collaboration between human and system.

## Adoption as a Third Pillar, Not a Standalone Problem

This is the point where most AI adoption analyses stop: they cite numbers, call the problem “a skills issue,” and recommend more tool-training. I see it differently, because for years I’ve worked at the intersection of three things at once that are rarely treated as one system: building trust, the decision-making process, and adoption that goes beyond simply learning to operate a tool.

Adoption isn’t a standalone problem. It’s an end result. If trust is miscalibrated because the interface sends false signals of certainty, people either stop verifying altogether or ignore good recommendations. And if the decision-making process has no designed space for reflection, a person stops thinking before accepting an AI suggestion, exactly as I wrote earlier about desirable difficulties and the power of effortful paradox. Adoption that looks like a success in the numbers but doesn’t hold up in practice is always the result of these two earlier elements being skipped.

Traditional AI consulting usually stops at one question: does it work. It checks model performance, system integration, ROI on paper, and that’s where the diagnosis ends, because its language doesn’t reach any further. I ask a different question: do people trust it, do they understand it, and do they retain control over it. That’s exactly where most rollouts that formally “work,” yet nobody actually uses, come apart, at the intersection of technical design and human behavior.

## Why I Built a Framework for This

Picture a typical situation: a manager rolls out AI to their team, the tool is good, the budget is approved, training has happened, and yet three months later half the team has gone back to old habits while the other half trusts the system uncritically. Nobody asked beforehand how much control to actually leave with the human in that specific spot, so everyone answered that question for themselves, quietly, with no shared language.

**The BehaviorAI Design Framework** exists to ask that question out loud and answer it in a repeatable way, before the rollout happens, not after something has already gone wrong.

![](https://substackcdn.com/image/fetch/$s_!oIbO!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79bc5a32-ecf8-4b00-97cb-7e5842b3bee1_2245x3179.png)

The framework works as three questions asked in sequence, each one closing a door before the next one opens:

1. **What does the user actually lack?**: not every resistance to AI is a skills gap. Sometimes what’s missing is the opportunity to use it at a natural point in the workflow, and sometimes it’s motivation, because nobody showed the person what they gain from it.
2. **Which mode of collaboration fits this situation?**: this is where the FASCAI language comes in, distinguishing three modes:
	- *full automation*: where the stakes are low and there’s no real reason to involve a human,
		- *fast collaboration*: where the human retains control but without pausing to deliberate over every step,
		- *slow, reflective collaboration*: where the consequences are too serious to hand off to the system without careful thought.
3. **Does this actually protect the user, or does it just look like it does?**: this last question is a test of honesty: it checks whether the safeguard is real, or just an “approve” button with nothing behind it, while also accounting for shifting regulatory requirements.

This way of thinking shows up most clearly in a specific example that comes up in nearly every AI recommendation project. Most teams start with the question “how do we build the recommendation interface?”, and that seemingly small difference leads to entirely different answers than the question that should actually come first: “what makes a user trust this recommendation?” The first question ends at aesthetics and screen layout. The second leads to a design that actually works, instead of conclusions drawn three months after launch, once it turns out people are ignoring what the system suggests anyway.

This framework, together with the pattern library I’ve been building for months, is now turning into a product. The BehaviorAI library maps out concrete design patterns for human-AI interaction, grounded in behavioral science rather than a designer’s intuition, and it helps identify friction points, build trust step by step, and shape habits that turn AI’s potential into real, consistent use, instead of a one-time rollout everyone forgets about after three months. I’m working on the **[BehaviorAI beta](http://behaviorai.eu/)** and **[preparing training](http://kasiaszczesna.pl/)** on the full method, both launching September 7th. More on that soon.

![](https://substackcdn.com/image/fetch/$s_!uPRD!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2100b906-65b2-4d7a-a1f9-7d9bc04c12f6_3168x792.png)

## A Gap That Won’t Close on Its Own

AI adoption isn’t a question of whether companies will buy more tools. They will, and they’re already buying faster than they can put them to use. Whether anyone in that company designed the human’s role toward those tools before the rollout became a fact. Without that, the next wave of investment will just give us a higher adoption percentage and the same stubbornly low maturity percentage.

Ultimately, it comes down to companies building customer and employee experience on trust, rather than discovering the costs after the fact, financial, legal, reputational, and psychological costs that always land on the people who had to work with it.

---

*If AI is deployed in your organization but isn’t quite working, I’d be glad to take a look at exactly where it’s coming apart.*

---

## Sources

1. [Ramp Economics Lab: Ramp AI Index, April 2026](https://econlab.substack.com/p/what-drives-ai-adoption)
2. [Alice Labs: Global AI Adoption Index 2026 (citing McKinsey 2025 data)](https://alicelabs.ai/reports/global-ai-adoption-index-2026)
3. [MIT Sloan: Action items for AI decision makers in 2026 (Davenport, Bean)](https://mitsloan.mit.edu/ideas-made-to-matter/action-items-ai-decision-makers-2026)
4. [Stanford HAI (2025).](https://hai.stanford.edu/ai-index/2025-ai-index-report) *[Artificial Intelligence Index Report 2025.](https://hai.stanford.edu/ai-index/2025-ai-index-report)*
5. [Stanford HAI (2026).](https://hai.stanford.edu/ai-index/2026-ai-index-report) *[Artificial Intelligence Index Report 2026.](https://hai.stanford.edu/ai-index/2026-ai-index-report)*
6. [Futurism: Maggie Harrison Dupré, “A Whole Bunch of People’s Claude Chats Are Publicly Accessible Online, and There’s Some Wildly Private Stuff in There,” July 2026](https://futurism.com/artificial-intelligence/claude-chats-publicly-accessible)
7. [BehaviorAI: pattern library and BehaviorAI Design Framework](https://behaviorai.eu/)
8. [Katarzyna Szczesna: more about the author](https://kasiaszczesna.pl/)

---

## Luka między inwestycją a użyciem: gdzie popełniamy błąd z adopcją AI?

*Z tego artykułu dowiesz się:*

- *dlaczego 95% firm nie widzi zwrotu z pieniędzy zainwestowanych w AI, mimo że coraz więcej z nich w ogóle z niej korzysta,*
- *jakie trzy bariery behawioralne, a nie techniczne, stoją za tym, że gotowe narzędzia leżą nieużywane,*
- *co niedawny wyciek rozmów z Claude’a mówi o tym, jak łatwo źle skalibrować zaufanie do interfejsu,*
- *jak krok po kroku zaprojektować rolę człowieka wobec AI, żeby wdrożenie faktycznie zadziałało.*

![](https://substackcdn.com/image/fetch/$s_!Qjar!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd1f3d22-c6c8-4121-9ec6-b53acf5a0e93_1200x1500.png)

W marcu tego roku adopcja AI w biznesie przekroczyła po raz pierwszy 50% firm, według Ramp AI Index, podczas gdy rok wcześniej było to 35%. Stanford podaje jeszcze bardziej optymistyczną liczbę: adopcja AI w przedsiębiorstwach wzrosła do 88 procent, z 55 procent zaledwie dwa lata wcześniej.

To powinna być dobra wiadomość, i byłaby, gdyby nie druga liczba, która stoi tuż obok niej. Według McKinsey tylko jeden procent liderów opisuje swoje wdrożenia AI jako dojrzałe, a MIT Media Lab poszedł o krok dalej i policzył realny zwrot z inwestycji: 95% firm nie widzi żadnego mierzalnego zwrotu z pieniędzy zainwestowanych w AI.

Miliardy dolarów płyną więc w narzędzia, które potem stoją nieużywane, bo połowa firm ma już AI, a prawie żadna nie wie, co z nim zrobić.

## Dlaczego to nie jest problem technologii

Pierwszy odruch w takiej sytuacji to szukać winy w narzędziu, w tym że ma za mało mocy, za mało integracji, za mało funkcji, ale dane mówią co innego. W badaniu nad stanem AI w marketingu 78% marketerów wskazuje umiejętności i szkolenia jako swoją największą barierę, nie samą technologię.

To zdanie warto przeczytać dwa razy, bo łatwo je źle zrozumieć. “Umiejętności i szkolenia” nie znaczy, że ludzie nie umieją kliknąć we właściwy przycisk, tylko że nikt nie nauczył ich, kiedy AI powinno decydować samo, a kiedy powinni zatrzymać się i pomyśleć sami. To nie jest więc luka kompetencji technicznych, tylko luka języka do podejmowania decyzji.

Firma kupuje narzędzie, wdraża je w jednym zespole, i po trzech miesiącach narzędzie działa dokładnie tak, jak powinno, a ludzie go nie używają, albo używają źle, nie dlatego, że są leniwi czy oporni wobec zmiany, tylko dlatego, że nikt nie zaprojektował, jaka jest ich rola wobec tego narzędzia. Adopcja nie zawodzi więc na etapie zakupu, tylko na etapie codziennej pracy, w momencie, w którym człowiek musi zdecydować, ile zaufać temu, co widzi na ekranie.

Pod tą jedną liczbą kryją się w gruncie rzeczy trzy różne bariery, i żadna z nich nie jest techniczna:

- **Bodźce** - to, czym ludzie kierują się na co dzień, jest niedopasowane do tego, jak faktycznie ma wyglądać współpraca z AI.
- **Normy** - niepisane zasady tego, co “wypada” zrobić samemu, a co można oddać systemowi, są niejasne albo w ogóle nie istnieją.
- **Zaufanie** - zamiast być skalibrowane do realnej jakości narzędzia, jest albo ślepe, albo go w ogóle nie ma.

To właśnie te trzy rzeczy, nie moc obliczeniowa, decydują, czy narzędzie zostanie użyte.

### Kiedy sam Claude staje się przykładem

Dowód na to, jak kosztowna bywa źle skalibrowana norma, pojawił się w tym tygodniu przy okazji samego Claude’a. Futurism opisał, że tysiące rozmów i projektów udostępnionych przez użytkowników za pomocą funkcji “udostępnij” trafiły do wyszukiwarki Google, wśród nich dokumentacja medyczna pacjentów, dane kontaktowe dzieci czy wewnętrzne materiały firmowe. Przycisk “udostępnij” informował, że link będzie “publiczny”, ale nie mówił wprost, że treść może zostać zaindeksowana i odnaleziona przez zupełnie obcych ludzi, więc użytkownicy zaufali sformułowaniu, które nie niosło pełnej informacji o konsekwencjach. To dokładnie ten mechanizm, o którym piszę: interfejs dał niepełny sygnał, norma “co wolno udostępnić” nie była jasna, a koszt tej luki ponieśli ludzie, których dane trafiły do sieci, nie firma, która zaprojektowała przycisk.

## Powrót człowieka do pętli, bez planu, co ma tam robić

Ten sam problem widać z drugiej strony, w świecie agentic AI. Po fali błędów i przypadków przejęcia systemów przez prompt injection firmy zaczęły wracać do modelu z człowiekiem w pętli decyzyjnej, a badacze z MIT Sloan zauważają, że firmy będą utrzymywać pewien poziom nadzoru człowieka jako zabezpieczenie dla agentic AI, co jednak podważa obiecywaną przewagę wydajnościową tej technologii.

To zdanie kryje w sobie dokładnie ten sam błąd, o którym piszę od miesięcy: firmy dodają “człowieka w pętli” jako punkt kontrolny, bez zaprojektowania, co ten człowiek ma tam faktycznie robić. Sam przycisk “zatwierdź” nie tworzy nadzoru, tworzy go dopiero moment, w którym człowiek ma realny powód, żeby się zatrzymać, pomyśleć, i czasem powiedzieć nie. Bez tego projektu nadzór jest fasadą, a “przewaga wydajnościowa”, którą firmy podobno tracą, i tak nigdy nie była realna, bo opierała się na złudnym zaufaniu, nie na rzeczywistej współpracy człowieka z systemem.

## Adopcja jako trzeci filar, nie samodzielny problem

To jest moment, w którym większość analiz adopcji AI się zatrzymuje: podaje liczby, nazywa problem “kompetencyjnym”, proponuje więcej szkoleń z obsługi narzędzia. Ja widzę to inaczej, bo od lat pracuję na styku trzech rzeczy naraz, które rzadko są traktowane jako jeden system: budowania zaufania, procesu podejmowania decyzji i adopcji AI, która wykracza poza samą naukę obsługi narzędzia.

Adopcja nie jest bowiem samodzielnym problemem, tylko efektem końcowym. Jeśli zaufanie kalibruje się źle, bo interfejs daje fałszywe sygnały pewności, ludzie albo przestają weryfikować, albo ignorują dobre rekomendacje, a jeśli proces podejmowania decyzji nie ma zaprojektowanego miejsca na refleksję, człowiek przestaje myśleć, zanim zaakceptuje sugestię AI, dokładnie tak, jak pisałam wcześniej o desirable difficulties i sile paradoksu wysiłku. Adopcja, która wygląda na sukces w liczbach, a nie działa w praktyce, jest zawsze skutkiem tego, że te dwa wcześniejsze elementy zostały pominięte.

Tradycyjny consulting AI zatrzymuje się zwykle na jednym pytaniu: czy to działa. Sprawdza wydajność modelu, integrację z systemami, zwrot z inwestycji na papierze, i na tym kończy diagnozę, bo dalej nie sięga jego język. Ja zadaję inne pytanie: czy ludzie temu ufają, czy to rozumieją i czy zachowują nad tym kontrolę. To właśnie tam, na styku projektu technicznego i ludzkiego zachowania, rozjeżdża się większość wdrożeń, które formalnie “działają”, a mimo to nikt z nich nie korzysta.

## Dlaczego zbudowałam do tego framework

Wyobraź sobie typową sytuację: menedżer wdraża AI w swoim zespole, narzędzie jest dobre, budżet zatwierdzony, szkolenie odbyte, a mimo to za trzy miesiące pół zespołu wraca do starych nawyków, a druga połowa ufa systemowi bezkrytycznie. Nikt nie zapytał wcześniej, ile kontroli faktycznie zostawić człowiekowi w tym konkretnym miejscu pracy, więc każdy odpowiedział sobie na to pytanie sam, po cichu, bez wspólnego języka.

**BehaviorAI Design Framework** powstał właśnie po to, żeby to pytanie zadać na głos i odpowiedzieć na nie w sposób powtarzalny, zanim wdrożenie stanie się faktem, a nie dopiero wtedy, gdy coś już poszło nie tak.

![](https://substackcdn.com/image/fetch/$s_!fm1L!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F01772f21-59dc-4e5f-b3f1-7d87b469ba9d_2245x3179.png)

Framework działa jak trzy pytania zadawane po kolei, każde zamykające drzwi, zanim otworzy się kolejne:

1. **Czego użytkownikowi tak naprawdę brakuje?** nie każdy opór wobec AI to brak umiejętności. Czasem brakuje okazji, żeby jej użyć w naturalnym momencie pracy, a czasem motywacji, bo nikt nie pokazał, co człowiek na tym zyskuje.
2. **Jaki tryb współpracy pasuje do tej sytuacji?** tu wchodzi język FASCAI, który rozróżnia trzy tryby:
	- *pełna automatyzacja* - tam, gdzie stawka jest niska i nie ma po co angażować człowieka,
		- *szybka współpraca* - tam, gdzie człowiek ma zachować kontrolę, ale bez zatrzymywania się nad każdym krokiem,
		- *wolna, refleksyjna współpraca* - tam, gdzie konsekwencje są zbyt poważne, żeby oddać je systemowi bez namysłu.
3. **Czy to naprawdę chroni użytkownika, czy tylko tak wygląda?** ostatnie pytanie jest testem szczerości: sprawdza, czy zabezpieczenie jest realne, czy jest tylko przyciskiem “zatwierdź” bez treści, biorąc pod uwagę również zmieniające się regulacje prawne.

Ten sposób myślenia widać najlepiej na konkretnym przykładzie, który wraca w niemal każdym projekcie związanym z rekomendacjami AI. Większość zespołów zaczyna od pytania “jak zbudować interfejs do rekomendacji?”, a to pozornie drobna różnica prowadzi do zupełnie innych odpowiedzi niż pytanie, które naprawdę powinno paść jako pierwsze: “co sprawia, że użytkownik ufa tej rekomendacji?”. Pierwsze pytanie kończy się na estetyce i układzie ekranu. Drugie prowadzi do projektu, który faktycznie działa, zamiast do wniosków wyciąganych trzy miesiące po wdrożeniu, kiedy okazuje się, że ludzie i tak ignorują to, co system im podpowiada.

To właśnie ten framework, razem z biblioteką wzorców, którą buduję od miesięcy, zamienia się teraz w produkt. Biblioteka BehaviorAI pokazuje konkretne wzorce projektowe interakcji człowiek-AI, oparte na naukach behawioralnych, a nie na intuicji projektanta, i pomaga identyfikować punkty tarcia, budować zaufanie krok po kroku oraz kształtować nawyki, które zamieniają potencjał AI w jej realne, konsekwentne wykorzystanie, zamiast jednorazowego wdrożenia, o którym wszyscy zapominają po trzech miesiącach. Pracuję nad wersją beta **[BehaviorAI](http://behaviorai.eu/)** i **[przygotowuję szkolenie](http://kasiaszczesna.pl/)** z całej metody, oba ruszają 7 września, a więcej o tym już niedługo.

![](https://substackcdn.com/image/fetch/$s_!uPRD!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2100b906-65b2-4d7a-a1f9-7d9bc04c12f6_3168x792.png)

## Luka, która nie zniknie sama

Adopcja AI nie jest pytaniem o to, czy firmy kupią więcej narzędzi, bo kupią, i tak już kupują szybciej niż potrafią z nich korzystać. Czy ktoś w tej firmie zaprojektował rolę człowieka wobec tych narzędzi, zanim wdrożenie stało się faktem? bo bez tego kolejna fala inwestycji da nam po prostu wyższy procent adopcji i ten sam, uparcie niski procent dojrzałości.

Chodzi ostatecznie o to, żeby firmy budowały doświadczenie klienta i pracownika na zaufaniu, a nie odkrywały koszty dopiero po wdrożeniu, finansowe, prawne, reputacyjne i psychologiczne, poniesione zawsze przez ludzi, którzy mieli z tym pracować.

---

*Jeśli w Twojej organizacji AI jest wdrożone, ale nie do końca działa, chętnie przyjrzę się, gdzie dokładnie się rozjeżdża. Link w komentarzu.*