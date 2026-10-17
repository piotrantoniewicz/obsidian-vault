---
type: "Web"
authors: "[[Kasia Szczesna]]"
url: "https://behavioralinsight.substack.com/p/botsitting-where-ais-saved-time-really?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-10-13
created: 2026-10-16
tags:
  - "strategia-AI"
  - "trendy-AI"
  - "szkolenia-AI"
---


**In this article, you’ll learn:**

- what botsitting is and how much of the time AI was supposed to save actually goes into corrections,
- why adoption dashboards count this work as engagement,
- how to tell a maturing rollout from one where people have simply stopped checking,
- what to measure instead of user counts and licenses,
- how to design verification so the knowledge from corrections stays in the organization.

You probably know this from your own desk. You type a request, the answer appears almost instantly, and for a moment it feels like an hour of work just did itself. Then the second part begins: adding context the model couldn’t have known, checking the numbers, fixing the tone, asking for another version. A [Harvard Business School AI Institute memo](https://aiinstitute.hbs.edu/future-proof-with-ai/memo-october-2026/) has a name for this: *botsitting*.

### The time that leaks

According to [BambooHR data](https://www.hrdive.com/news/almost-half-the-time-workers-spend-on-ai-is-spent-fixing-its-output/829404/), an employee spends about 47 days a year working with AI, and roughly 20 of them go to fixing output and re-prompting. [Workday found](https://www.cfobrew.com/stories/2026/01/22/to-measure-the-roi-of-ai-take-workslop-into-account) that corrections eat 37% of the time AI saves, and only 14% of employees consistently come out ahead. In software, often cited as AI’s biggest success, an [NBER study](https://www.nber.org/papers/w35275) found that commits rose by about 240% after coding agents arrived, while shipped releases rose by only about 30%. Activity grows much faster than results, and that gap is where the promised time disappears.

### Why nobody sees it

Licenses, weekly active users, prompts and tokens come bundled with the tool. The vendor counts them, often on the same basis it uses to bill you, so an adoption report almost writes itself. [BBVA](https://www.bbva.com/en/innovation/harvard-business-review-recognizes-bbva-as-a-benchmark-for-corporate-ai-adoption/), recognized by Harvard Business Review as a benchmark for corporate AI adoption, ran a genuinely thoughtful rollout. Yet the one hard number it offers as proof of success is that more than half of employees use the tools every week. We don’t know how much of that use moves work forward and how much is fixing what the model got wrong.

Botsitting is invisible twice over. The system counts it as engagement, and employees rarely report it, because it’s hard to complain about a tool everyone praises and easy to assume you’re just not prompting well yet.

### The behavioral view

Working with AI means constantly switching between two modes: quickly accepting an answer that sounds right, and slowing down to check it. In FASCAI, the framework I use, that switch is the critical moment, and most organizations leave it to chance.

Over time people get used to AI output. It’s usually fine, so checking starts to feel like a waste of time. Correction time falls, which on a chart looks like a maturing rollout. It can just as easily mean errors have started slipping through. Without more data, you can’t tell the two apart.

There’s another side to this. Christian Catalini argues in [Harvard Business Review](https://hbr.org/2026/10/ai-is-making-verification-the-bottleneck-for-companies) that a company’s most valuable data are the moments when an expert rejects a plausible-looking answer. Seen that way, botsitting is verification, the work that becomes most valuable when execution gets cheap. The problem is that in most companies these corrections go nowhere. Someone fixes the answer, pastes it into an email, and the knowledge of what was wrong disappears when the chat window closes.

![](https://substackcdn.com/image/fetch/$s_!Xa4L!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf3aab75-d9e3-4303-9570-2ba400901647_1200x675.png)

### What to measure instead

Measure outcomes customers feel: cases resolved without a second contact, releases that ship and get used, bids won. Then track the **cost per successful task** for each workflow, meaning total cost, including review and rework, divided by the tasks actually delivered, signed off by the business owner of the process.

I’d add two things. First, count the errors that got past review and came back later; otherwise the metric rewards teams that simply stopped checking. Second, track how often and why people correct or reject AI output. If correction rates drop while customer-facing errors rise, people haven’t gotten better at working with AI. They’ve stopped looking.

### The time doesn’t vanish, it moves

Much of the time AI was supposed to save doesn’t disappear. It moves from doing the work to verifying it. And verification can be designed: who does it, where in the process it’s essential, what a good correction looks like, and where the lessons go.

So here are two questions to ask before your next rollout report. Does anyone know what it costs to deliver one task with AI, corrections included? And do the corrections your people make every day get recorded anywhere?

### How I approach human-AI collaboration

I look at AI rollouts as behavior change projects rather than technology projects. The technology is usually ready; the people, processes and decisions around it often aren’t. Botsitting is a good example. It isn’t a tool problem. It’s verification work that nobody designed. My work falls into three kinds of engagements.

**An audit of AI processes and projects.** This is usually where I start, for clients who say some version of “we deployed AI and we don’t know if it works.” I map where AI sits in a real workflow, where human judgment is supposed to happen and whether it actually does, how people check output under time pressure, and what the organization really measures, including how much of the “saved” time goes into fixing output.

**Building AI adoption.** Adoption isn’t the same as usage. When people work the old way with new tools, or everyone is at a different level and nobody agrees on what good looks like, what’s missing is a standard: which decisions stay with people, when AI output has to be verified, and how corrections get recorded so the team can learn from them.

**Designing human-AI collaboration.** This is work on the tool itself, using patterns from the BehaviorAI Pattern Library: showing confidence, sources and the places worth checking; adding deliberate friction before decisions that matter; creating clear approval moments with a trace of who decided what; and choosing forms that fit the task instead of another chat window. Underneath are FASCAI, my framework for designing how people switch between fast acceptance and careful review, and RIFT, which looks at relationship, interpretation, friction and trust in each interaction.

More and more, I stay with clients into implementation, because that’s when the pressure shows up and when the design either holds or quietly gets worked around.

*“This piece was written with the help of AI. I chose and read the sources myself; the behavioral perspective, FASCAI, RIFT and the [BehaviorAI](http://behaviorai.eu/) Pattern Library are my own work.”  
Cheers,  
Kasia*

## —

## Botsitting. Gdzie naprawdę trafia czas zaoszczędzony przez AI

**AI odpowiada w kilka sekund, a potem przez kwadrans poprawiasz tę odpowiedź. Na dashboardzie wdrożenia ten kwadrans liczy się jako zaangażowanie. Co mówią dane o tej ukrytej pracy, dlaczego organizacje jej nie widzą i co warto mierzyć zamiast liczby użytkowników.**

**Z artykułu dowiesz się:**

- czym jest botsitting i ile czasu „zaoszczędzonego” przez AI faktycznie idzie na poprawki,
- dlaczego dashboardy wdrożeń pokazują tę pracę jako zaangażowanie,
- jak odróżnić dojrzałe wdrożenie od sytuacji, w której ludzie po prostu przestali sprawdzać,
- co mierzyć zamiast liczby użytkowników i licencji,
- jak zaprojektować weryfikację, żeby wiedza z korekt zostawała w organizacji.

Znasz to pewnie z własnego biurka. Wpisujesz polecenie, odpowiedź pojawia się po chwili i masz wrażenie, że godzina pracy właśnie zrobiła się sama. A potem zaczyna się drugi etap: dopisujesz kontekst, którego model nie mógł znać, sprawdzasz liczby, poprawiasz ton, prosisz o nową wersję. W [memo Harvard Business School AI Institute](https://aiinstitute.hbs.edu/future-proof-with-ai/memo-october-2026/) ta praca ma swoją nazwę: *botsitting*.

### Czas, który przecieka

Według [danych BambooHR](https://www.hrdive.com/news/almost-half-the-time-workers-spend-on-ai-is-spent-fixing-its-output/829404/) pracownik spędza z AI około 47 dni w roku, z czego mniej więcej 20 idzie na poprawki i ponowne promptowanie. [Workday](https://www.cfobrew.com/stories/2026/01/22/to-measure-the-roi-of-ai-take-workslop-into-account) wyliczył, że korekty zjadają 37% czasu zaoszczędzonego dzięki AI, a tylko 14% pracowników regularnie wychodzi na plus. W programowaniu, które uchodzi za największy sukces AI, [badanie NBER](https://www.nber.org/papers/w35275) pokazało, że po wprowadzeniu agentów kodujących liczba commitów wzrosła o około 240%, a wdrożonych release’ów tylko o około 30%. Aktywność rośnie dużo szybciej niż efekt i właśnie w tej różnicy znika obiecany czas.

### Dlaczego nikt tego nie widzi

Liczba licencji, aktywni użytkownicy, prompty i tokeny przychodzą w pakiecie z narzędziem. Liczy je dostawca, często na tej samej podstawie, na której wystawia fakturę, więc raport z wdrożenia składa się prawie sam. [BBVA](https://www.bbva.com/en/innovation/harvard-business-review-recognizes-bbva-as-a-benchmark-for-corporate-ai-adoption/), opisane przez Harvard Business Review jako wzorzec korporacyjnej adopcji AI, przeprowadziło naprawdę przemyślane wdrożenie. A jednak jedyną twardą liczbą, którą pokazuje jako dowód sukcesu, jest to, że ponad połowa pracowników używa narzędzi co tydzień. Nie wiemy, ile z tego użycia posuwa pracę do przodu, a ile jest poprawianiem błędów modelu.

Botsitting jest niewidoczny podwójnie. System liczy go jako zaangażowanie, a pracownicy rzadko go zgłaszają, bo trudno narzekać na narzędzie, które wszyscy chwalą, i łatwo uznać, że to my jeszcze nie umiemy dobrze promptować.

### Perspektywa behawioralna

Praca z AI to ciągłe przełączanie się między dwoma trybami: szybkim przyjęciem odpowiedzi, która brzmi dobrze, i zwolnieniem, żeby ją sprawdzić. W modelu FASCAI - Fast and Slow Collaborative AI, na którym opieram swoją pracę, to przełączenie jest momentem kluczowym, a większość organizacji zostawia je przypadkowi.

Z czasem ludzie przyzwyczajają się do wyników AI. Zwykle są poprawne, więc sprawdzanie zaczyna wyglądać na stratę czasu. Czas korekty spada, co na wykresie wygląda jak dojrzewanie wdrożenia. Równie dobrze może jednak oznaczać, że błędy zaczęły przechodzić niezauważone. Bez dodatkowych danych nie da się odróżnić jednego od drugiego.

Jest też druga strona. Christian Catalini pisze w [Harvard Business Review](https://hbr.org/2026/10/ai-is-making-verification-the-bottleneck-for-companies), że najcenniejsze dane firmy to momenty, w których ekspert odrzuca wiarygodnie wyglądającą odpowiedź. W tej perspektywie botsitting to weryfikacja, czyli praca, która zyskuje na wartości, gdy samo wykonanie tanieje. Problem w tym, że w większości firm te korekty nigdzie nie zostają. Ktoś poprawia odpowiedź, wkleja ją do maila, a wiedza o tym, co było nie tak, znika razem z zamkniętym oknem czatu.  
  
Catalini i współautorzy pokazują to na prostej macierzy: o ryzyku decyduje nie to, czy AI potrafi wykonać zadanie, tylko ile kosztuje sprawdzenie wyniku. Botsitting najmocniej daje o sobie znać tam, gdzie wykonanie jest tanie, a weryfikacja droga. To strefa, w której automatyzacja wyprzedza nadzór, a czas „oszczędzony” wraca jako poprawki.

![](https://substackcdn.com/image/fetch/$s_!AGHs!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3546da11-bd88-4581-b6bd-81e32b246333_1200x675.png)

### Co mierzyć zamiast tego

Warto mierzyć wyniki, które odczuwa klient: sprawy rozwiązane bez ponownego kontaktu, release’y wdrożone i używane, wygrane oferty. Do tego **koszt udanego zadania** dla każdego workflow, czyli całkowity koszt łącznie z przeglądem i poprawkami, podzielony przez liczbę zadań faktycznie dowiezionych, zatwierdzany przez biznesowego właściciela procesu.

Dokładam do tego dwie rzeczy. Po pierwsze, trzeba wliczać błędy, które przeszły przez weryfikację i wróciły później, bo inaczej metryka nagradza zespoły, które po prostu przestały sprawdzać. Po drugie, warto śledzić, jak często i dlaczego ludzie poprawiają lub odrzucają wynik AI. Jeśli poprawek jest coraz mniej, a błędów u klientów coraz więcej, to nie znaczy, że ludzie lepiej pracują z AI. Znaczy, że przestali patrzeć.

### Czas nie znika, tylko zmienia miejsce

Duża część czasu, który AI miało nam oszczędzić, nie znika, tylko przenosi się z wykonania do weryfikacji. A weryfikację da się zaprojektować: zdecydować, kto ją wykonuje, w których miejscach procesu jest konieczna, jak wygląda dobra korekta i gdzie trafia wiedza, która z niej wynika.

Dlatego przed kolejnym raportem z wdrożenia warto zadać dwa pytania. Czy ktoś w organizacji wie, ile kosztuje dowiezienie jednego zadania z AI, razem z poprawkami? I czy korekty, które codziennie robią Twoi ludzie, gdziekolwiek zostają?

### Jak podchodzę do współpracy człowieka z AI

Patrzę na wdrożenia AI jak na projekty zmiany zachowań, a nie projekty technologiczne. Technologia zwykle jest gotowa, ale ludzie, procesy i decyzje wokół niej często nie. Botsitting dobrze to pokazuje. To nie jest problem narzędzia, tylko praca weryfikacyjna, której nikt nie zaprojektował. Moja praca dzieli się na trzy rodzaje zaangażowań.

**Audyt procesów i projektów AI.** Od tego zwykle zaczynam, kiedy klient mówi coś w rodzaju „wdrożyliśmy AI i nie wiemy, czy działa”. Sprawdzam, gdzie AI jest w realnym procesie, gdzie ma się pojawić ludzki osąd i czy rzeczywiście się pojawia, jak ludzie sprawdzają wyniki pod presją czasu i co organizacja naprawdę mierzy, łącznie z tym, ile „zaoszczędzonego” czasu idzie na poprawianie wyników.

**Budowanie adopcji AI.** Adopcja to nie to samo co użycie. Kiedy ludzie pracują po staremu z nowymi narzędziami albo każdy jest na innym poziomie i nikt nie wie, jak wygląda dobra praca z AI, brakuje standardu: które decyzje zostają przy ludziach, kiedy wynik AI trzeba zweryfikować i jak zapisywać korekty, żeby zespół mógł się na nich uczyć.

**Projektowanie współpracy człowieka z AI.** To praca nad samym narzędziem, oparta na wzorcach z BehaviorAI Pattern Library: pokazywanie pewności odpowiedzi, źródeł i miejsc wartych sprawdzenia, celowe tarcie przed ważnymi decyzjami, jasne momenty zatwierdzenia ze śladem tego, kto co zdecydował, oraz formy dopasowane do zadania zamiast kolejnego okna czatu. Pod spodem są FASCAI, mój model projektowania przełączania się między szybkim przyjmowaniem a uważnym sprawdzaniem, oraz RIFT, który przygląda się relacji, interpretacji, tarciu i zaufaniu w każdej interakcji.

Coraz częściej zostaję z klientami także w czasie wdrożenia, bo wtedy pojawia się presja i wtedy okazuje się, czy projekt się utrzyma, czy ludzie zaczną go po cichu omijać.  
  
—

*Ten tekst powstał przy wsparciu AI. Źródła wybrałam i przeczytałam sama, a perspektywa behawioralna, FASCAI, RIFT i [BehaviorAI](http://behaviorai.eu/) Pattern Library to moja własna praca.  
Pozdrowienia,  
Kasia*