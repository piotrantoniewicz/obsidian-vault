---
type: Web
authors: '[[Kasia Szczesna]]'
url: >-
  https://behavioralinsight.substack.com/p/not-every-shortcut-is-good-design?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true
published: 2026-08-04
created: 2026-08-04
tags:
  - strategia-AI
  - trendy-AI
  - szkolenia-AI
---


This question is not abstract. It sits inside every project I work on. A client comes in asking for their AI assistant to be faster, smoother, so the user never has to think about anything. And for most of my career, I was taught that this is exactly what good design looks like. Fewer clicks. Less effort. Less resistance.

Three pieces I read over the past month came together and showed me why that assumption needs to be revisited.

## Friction that teaches

A team from the University of Toronto and Yale, Zohar, Bloom, and Inzlicht, published a short but very precise piece in Communications Psychology titled Against frictionless AI. Their starting point is simple. People have always chosen the path of least resistance, it is one of the most universal principles in psychology. And at the same time, we regularly seek out that resistance ourselves, because without it, nothing holds much value for us. This phenomenon is called the effort paradox.

![](https://substackcdn.com/image/fetch/$s_!MYwf!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b7ec9f5-7bbd-4f33-a346-3d5e9c9daf95_987x617.jpeg)

The authors write about something they call desirable difficulties. Struggling to encode, retrieve, and reorganize information, whether through active engagement, persistence, or adjustment, produces deeper comprehension and more durable retention. When AI removes that effort and hands over a ready-made solution, this process gets interrupted before it has a chance to work. And indeed, there is already evidence that people who use AI struggle to accurately recall or reproduce their own work, acquire fewer skills, and perform worse once AI support is taken away.

This is not limited to cognitive processes. Effort can be unpleasant, but it is often struggle and difficulty that make life meaningful. When people work toward a task, they feel more competent and value the outcome of that labor more highly. Even when a task is objectively meaningless, simply adding friction to it increases people’s sense of purpose and significance. This helps explain why people rate their own imperfect writing as more meaningful than polished prose produced with the help of ChatGPT, and why they demand comparable compensation for it.

The authors are careful here. They are not arguing for making products harder on purpose, because the relationship between effort and meaning follows an inverted U shape. Too little friction takes away the benefits, too much overwhelms. The real question is being able to recognize which friction protects the user and which friction only frustrates them.

## The trust economy

The second thread that struck me just as hard is about how difficult it is to recognize the moment when something starts going wrong. Pat Pataranutaporn from MIT Media Lab, who studies how people design their own personalized AI, put it in a way I won’t forget in an interview for MIT News. I often joke that if AI showed up looking like the Terminator, it would be much easier for us to know what to do. The real challenge is that AI often appears as a warm friend, coach, tutor, or companion. That makes it difficult to recognize when something is going wrong.

In his study, Pataranutaporn and his team showed that people designing their own chatbot mispredicted its behavior on 11 out of 15 measured traits, typically overestimating positive qualities and underestimating risks such as excessive agreeableness. Even more striking, when the team gave users a tool to see inside the model’s internal representations, trust in the system increased, but the way people designed their chatbots did not change. Transparency on its own is not enough. That is an important lesson for anyone who assumes that transparency alone solves the trust problem.

Because trust in AI is a scarce resource right now. A study by KPMG and the University of Melbourne, covering 47 countries, found that fewer than half of people trust AI, while nearly two thirds admit to relying on its output without checking it. That gap matters, because trust behaves like capital. It accumulates slowly and is lost instantly, and it does not come back at the old price. Deloitte had to refund part of the cost of a government contract in Australia after an AI-assisted report was found to contain fabricated sources.

You can already see where a new market of trust gatekeepers is emerging. The Big Four accounting firms are rolling out AI assurance services as a separate line of business, essentially selling the right to say that a system has been tested. Insurers at Lloyd’s of London have started building policies that cover losses from AI hallucinations, where models are evaluated before coverage is issued and payouts are triggered if agreed performance thresholds are no longer met. Universities are going back to handwritten, proctored exams, because a take-home essay no longer proves what it used to. Sweden is spending over one hundred million dollars to bring printed textbooks back into schools, and Norway has announced a near total ban on AI in elementary schools. The economist Herbert Simon wrote about this back in 1971, noting that a wealth of information creates a poverty of attention. Different institutions are responding in different ways, but all of them are retreating toward systems they can actually trust.

## How do you know which friction to keep

These three threads, research on desirable difficulties, a blind spot in how people design AI, and the frantic construction of trust infrastructure, all lead to the same question. If the answer is neither to remove every piece of friction nor to leave it everywhere, then how do you actually decide, in a given moment of interaction, which friction to keep and which to remove.

That question is what the BehaviorAI Design Framework was built to answer. I built it as a three-question, gated methodology precisely because the answer is never intuitive or a one-time call. It has to be a repeatable design decision.

**Question one: diagnosis.** This is based on the COM-B model. Before designing any intervention, we ask whether the user lacks capability, opportunity, or motivation to behave in the desired way. In the context of frictionless AI, this question sounds different than usual. We are not asking how to make it easier for the user to reach their goal. We are asking whether the ease we are about to add in this specific spot takes away something the user actually needs, such as the chance to learn something or to check their own judgment.

On its own, diagnosis is still too general to translate into an actual design decision. That is why I added a second layer between diagnosis and intervention, which I call FASCAI, short for Fast and Slow Collaborative AI. It names the mode in which a human and an AI should be working together at a given moment, borrowed from Kahneman’s System 1 and System 2, extended with a System 0.

System 0 is full automation, where AI acts without human involvement. System 1 is fast, intuitive collaboration, where the human keeps control but doesn’t need to consciously process every step. System 2 is slow, reflective collaboration, where the human is meant to think, verify, and build their own understanding.

The easiest way to show this is with a concrete example. Take an AI assistant that helps draft email replies. When a user accepts a suggested reply to a routine meeting confirmation, that is a transactional task with no cognitive stakes, so System 0 is the right mode and frictionless is a good decision here, not a mistake. When AI proposes a reply to a message from an important client, tone and relationship judgment come into play, so System 1 is needed: a short pause and the chance to adjust before the message goes out. When AI is meant to help draft a reply in a disputed matter, such as a complaint or a negotiation, the stakes and consequences are high, so System 2 is needed: the user’s own draft first, before seeing the AI’s version, so they don’t lose their own judgment on a matter where they alone carry the responsibility.

The mistake Zohar, Bloom, and Inzlicht warn about is exactly this: products default into System 0 everywhere, because it is cheaper to design and performs better in usability testing, even in places that should have stayed in System 1 or System 2.

**Question two: intervention.** Once we know which FASCAI mode should be active at a given moment, we use the Behaviour Change Wheel together with the BehaviorAI pattern library to design the actual solution. For System 1, that means a pattern that adds a pause before accepting an AI suggestion, or a pattern that surfaces the system’s confidence level instead of presenting an answer as fact. For System 2, that means a pattern that asks the user to form their own conclusion before showing them the model’s answer. These are concrete tools that respond directly to the problem the authors describe around desirable difficulties.

**Question three: ethics.** This closes the process. Even once we know how to design the intervention, we ask whether we have the right to do it and whose interests it actually serves. This question guards against a situation where the intention to reduce friction quietly turns into manipulation, or into designing the kind of dependency Pataranutaporn warns about when he talks about a model that constantly validates the user instead of occasionally correcting them.

This framework does not hand you a ready answer for how much friction is the right amount. Nobody has that answer today, because it depends on context, on the user’s stage of life, and on what is actually at stake in the decision. What it does give you is a structure that will not let you skip the question before you ship the next convenience feature, and a way to diagnose the same interaction, name its correct mode, and assign it a concrete pattern, instead of deciding on friction intuitively every single time.

This is the layer I have been designing for years, the one between what AI can do and what it should do for a specific user in a specific moment. Science is only now starting to give it a name.

---

*If you are working on a product where AI is responsible for key user decisions, I would be glad to walk you through the full framework and pattern library. Link in the comments.*

---

## Sources

1. Zohar, Bloom, Inzlicht — *Against frictionless AI*, Communications Psychology, 2026 [https://www.nature.com/articles/s44271-026-00402-1](https://www.nature.com/articles/s44271-026-00402-1)
2. Pat Pataranutaporn (MIT Media Lab), interview — *3 Questions: Neural transparency and the future of AI design*, MIT News, July 2026 [https://news.mit.edu/2026/3-questions-neural-transparency-and-future-of-ai-design-0715](https://news.mit.edu/2026/3-questions-neural-transparency-and-future-of-ai-design-0715)
3. Observer — article on AI trust and the economics of power and judgment, July 2026 [https://observer.com/2026/07/future-ai-power-judgment-trust/](https://observer.com/2026/07/future-ai-power-judgment-trust/)
4. KPMG and University of Melbourne — study on trust in AI across 47 countries [https://kpmg.com/xx/en/media/press-releases/2025/04/trust-of-ai-remains-a-critical-challenge.html](https://kpmg.com/xx/en/media/press-releases/2025/04/trust-of-ai-remains-a-critical-challenge.html)
5. Deloitte — partial refund of an Australian government contract after fabricated sources were found in an AI-assisted report [https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund/](https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund/)
6. The Big Four — launch of AI assurance services as a business line [https://thefinancestory.com/big-4-to-launch-ai-assurance-services](https://thefinancestory.com/big-4-to-launch-ai-assurance-services)
7. Lloyd’s of London — insurance policies covering AI hallucinations [https://www.armilla.ai/resources/insurers-launch-cover-for-losses-caused-by-ai-chatbot-errors](https://www.armilla.ai/resources/insurers-launch-cover-for-losses-caused-by-ai-chatbot-errors)

## Nie każde ułatwienie jest dobrym projektem

Od kilku tygodni wraca do mnie jedno pytanie. Czy to, co uważamy za sukces w projektowaniu produktów AI, czyli usunięcie każdego możliwego tarcia, nie jest czasem błędem w założeniach.

To pytanie nie jest abstrakcyjne. Siedzi w każdym projekcie, w którym uczestniczę. Klient przychodzi z prośbą o to, żeby jego asystent AI był szybszy, bardziej płynny, żeby użytkownik nie musiał się nad niczym zastanawiać. I przez większość mojej kariery uczono mnie, że to jest właśnie dobry projekt. Mniej kliknięć. Mniej wysiłku. Mniej oporu.

Trzy teksty, które przeczytałam w ostatnim miesiącu, złożyły mi się w jedną całość i pokazały, dlaczego to założenie trzeba zrewidować.

## Tarcie, które uczy

Zespół z University of Toronto i Yale, Zohar, Bloom i Inzlicht, opublikował w Communications Psychology krótki, ale bardzo precyzyjny tekst zatytułowany Against frictionless AI. Ich punkt wyjścia jest prosty. Ludzie od zawsze wybierają ścieżkę najmniejszego oporu, to jedna z najbardziej uniwersalnych zasad psychologii. A jednocześnie regularnie sami sobie ten opór fundujemy, bo bez niego nic nie ma dla nas wartości. Zjawisko to nazywa się paradoksem wysiłku.

![](https://substackcdn.com/image/fetch/$s_!MYwf!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6b7ec9f5-7bbd-4f33-a346-3d5e9c9daf95_987x617.jpeg)

Autorzy piszą o czymś, co nazywają desirable difficulties, czyli pożądanych trudnościach. Zmaganie się z kodowaniem, przywoływaniem i reorganizacją informacji, niezależnie od tego, czy dzieje się to przez aktywne zaangażowanie, wytrwałość czy korektę, prowadzi do głębszego zrozumienia i trwalszego zapamiętywania. Kiedy AI usuwa ten wysiłek i podaje gotowe rozwiązanie, ten proces zostaje przerwany, zanim zdąży zadziałać. I rzeczywiście, są już dowody na to, że osoby korzystające z AI gorzej odtwarzają własną pracę, uczą się mniej i osiągają słabsze wyniki, gdy wsparcie AI zostaje odebrane.

To dotyczy nie tylko procesów poznawczych. Wysiłek bywa nieprzyjemny, ale to właśnie trud i zmaganie często nadają życiu sens. Kiedy pracujemy nad zadaniem, czujemy się bardziej kompetentni i wyżej cenimy efekt swojej pracy. Nawet jeśli zadanie jest obiektywnie pozbawione znaczenia, samo dodanie do niego tarcia zwiększa poczucie celu i sensu. To dlatego ludzie oceniają własny, niedoskonały tekst jako bardziej znaczący niż wygładzoną prozę napisaną przy pomocy ChatGPT, i domagają się za niego podobnej rekompensaty co za tekst dopracowany przez AI.

Autorzy są przy tym ostrożni. Nie postulują, żeby robić produkty trudniejsze na siłę, bo związek między wysiłkiem a sensem ma kształt odwróconej litery U. Zbyt mało tarcia odbiera nam korzyści, zbyt dużo przytłacza. Chodzi o umiejętność rozpoznania, które tarcie chroni użytkownika, a które tylko go frustruje.

## Ekonomia zaufania

Drugi wątek, który uderzył mnie równie mocno, dotyczy tego, jak trudno nam rozpoznać moment, w którym coś idzie nie tak. Pat Pataranutaporn z MIT Media Lab, który bada, jak ludzie projektują swoje spersonalizowane AI, ujął to w rozmowie dla MIT News w sposób, którego nie zapomnę. “Często żartuję, że gdyby sztuczna inteligencja pojawiła się jak Terminator, o wiele łatwiej byłoby nam wiedzieć, co robić.”  
Prawdziwym wyzwaniem jest to, że sztuczna inteligencja często jawi się jako serdeczny przyjaciel, trener, nauczyciel czy towarzysz. To utrudnia rozpoznanie, że coś idzie nie tak.

W swoim badaniu Pataranutaporn i jego zespół pokazali, że ludzie projektujący własnego chatbota mylą się w przewidywaniu jego zachowania w 11 na 15 badanych cech, zwykle przeceniając cechy pozytywne i nie doceniając ryzyka, takiego jak nadmierna uległość modelu. Co ciekawsze, kiedy zespół dał użytkownikom narzędzie do wglądu w wewnętrzne reprezentacje modelu, zaufanie do systemu wzrosło, ale sposób projektowania chatbotów się nie zmienił. Sama przejrzystość nie wystarcza. To ważna lekcja dla każdego, kto myśli, że transparentność sama w sobie rozwiązuje problem zaufania.

Bo zaufanie do AI jest dziś rzadkim zasobem. Badanie KPMG i Uniwersytetu w Melbourne, obejmujące 47 krajów, pokazało, że mniej niż połowa ludzi ufa sztucznej inteligencji, a prawie dwie trzecie przyznaje, że polega na jej wynikach bez ich sprawdzania. Ta rozbieżność ma znaczenie, bo zaufanie zachowuje się jak kapitał. Buduje się powoli, a traci się natychmiast, i nie wraca po dawnej cenie. Deloitte musiał zwrócić część kosztów kontraktu rządowego w Australii po tym, jak w raporcie wspomaganym przez AI znaleziono zmyślone źródła.

Widać już, gdzie rodzi się nowy rynek strażników tego zaufania. Wielka Czwórka firm audytorskich wprowadza usługi zapewnienia bezpieczeństwa AI jako osobną linię biznesową, sprzedając prawo do stwierdzenia, że system został przetestowany. Ubezpieczyciele Lloyd’s of London zaczęli tworzyć polisy chroniące przed halucynacjami AI, w których modele są oceniane przed wystawieniem ubezpieczenia, a wypłata następuje, jeśli uzgodnione progi wydajności przestają być spełnione. Uniwersytety wracają do egzaminów pisanych ręcznie i nadzorowanych, bo esej napisany w domu przestał być dowodem czegokolwiek. Szwecja wydaje ponad sto milionów dolarów na przywrócenie drukowanych podręczników do szkół, a Norwegia ogłosiła niemal całkowity zakaz stosowania AI w szkołach podstawowych. Ekonomista Herbert Simon pisał o tym już w tysiąc dziewięćset siedemdziesiątym pierwszym roku, że bogactwo informacji prowadzi do ubóstwa uwagi. Różne instytucje reagują dziś w różny sposób, ale wszystkie wycofują się do systemów, którym można zaufać.

## Skąd wiadomo, które tarcie zostawić

Te trzy wątki, badania nad pożądanymi trudnościami, ślepy punkt w projektowaniu AI i gorączkowe budowanie infrastruktury zaufania, prowadzą do tego samego pytania. Skoro nie chodzi o to, żeby usuwać każde tarcie ani żeby zostawiać je wszędzie, to jak konkretnie zdecydować, które tarcie w danym momencie interakcji zostawić, a które usunąć.

To pytanie stało u początku BehaviorAI Design Framework. Zbudowałam go jako trzypytaniową, bramkową metodologię, właśnie dlatego, że odpowiedź nigdy nie jest intuicyjna ani jednorazowa, tylko musi być powtarzalną decyzją projektową.

**Pytanie pierwsze: diagnoza.** Opiera się na modelu COM-B. Zanim zaprojektujemy jakąkolwiek interwencję, pytamy, czy użytkownikowi brakuje zdolności, okazji czy motywacji, żeby zachować się w pożądany sposób. W kontekście frictionless AI to pytanie brzmi inaczej niż zwykle. Nie pytamy, jak ułatwić użytkownikowi dotarcie do celu, tylko czy ułatwienie w tym konkretnym miejscu odbiera mu coś, czego rzeczywiście potrzebuje, na przykład możliwość nauczenia się czegoś albo zweryfikowania własnego osądu.

Diagnoza sama w sobie jest jednak zbyt ogólna, żeby przełożyć ją na konkretny projekt. Dlatego między diagnozą a interwencją wstawiłam drugą warstwę, którą nazywam FASCAI, czyli Fast and Slow Collaborative AI. To sposób nazwania trybu, w jakim człowiek i AI powinni współpracować w danym momencie, zapożyczony od Kahnemana i jego Systemów 1 i 2, rozszerzony o System 0.

System 0 to pełna automatyzacja, w której AI działa bez udziału człowieka. System 1 to szybka, intuicyjna współpraca, w której człowiek zachowuje kontrolę, ale nie musi świadomie przetwarzać każdego kroku. System 2 to wolna, refleksyjna współpraca, w której człowiek ma myśleć, weryfikować, budować własne zrozumienie.

Najprościej pokazać to na konkretnym przykładzie. Weźmy asystenta AI, który pomaga odpowiadać na e-maile. Kiedy użytkownik akceptuje sugerowaną odpowiedź na rutynowe potwierdzenie spotkania, to zadanie transakcyjne bez konsekwencji poznawczych, więc System 0 jest właściwym trybem i frictionless jest tu dobrą decyzją, nie błędem. Kiedy AI proponuje odpowiedź na wiadomość od ważnego klienta, w grę wchodzi ocena tonu i relacji, więc potrzebny jest System 1, czyli krótka pauza i możliwość korekty, zanim wiadomość wyjdzie. Kiedy AI ma pomóc napisać odpowiedź w sprawie spornej, na przykład reklamacji albo negocjacji warunków, stawka i konsekwencje są wysokie, więc potrzebny jest System 2, czyli własny szkic użytkownika przed pokazaniem wersji AI, żeby nie stracił własnego osądu w sprawie, w której on jeden ponosi odpowiedzialność.

Błąd, przed którym ostrzegają Zohar, Bloom i Inzlicht, polega właśnie na tym, że produkty domyślnie ześlizgują się do Systemu 0 wszędzie, bo jest tańszy w projektowaniu i lepiej wypada w testach użyteczności, nawet w miejscach, które powinny zostać w Systemie 1 albo 2.

**Pytanie drugie: interwencja.** Kiedy wiemy już, jaki tryb FASCAI powinien działać w danym momencie, korzystamy z Behaviour Change Wheel razem z biblioteką wzorców BehaviorAI, żeby zaprojektować konkretne rozwiązanie. Dla Systemu 1 to wzorzec pauzy przed zaakceptowaniem sugestii AI albo widoczny poziom pewności systemu zamiast gotowej odpowiedzi podanej jako fakt. Dla Systemu 2 to wzorzec, który prosi użytkownika o samodzielne sformułowanie wniosku, zanim pokażemy mu odpowiedź modelu. To są konkretne narzędzia odpowiadające na dokładnie ten problem, o którym piszą autorzy tekstu o desirable difficulties.

**Pytanie trzecie: etyka.** Domyka cały proces. Nawet jeśli wiemy, jak zaprojektować interwencję, pytamy, czy mamy prawo to zrobić i czyim interesom to służy. To pytanie chroni przed sytuacją, w której intencja obniżenia tarcia po drodze zamienia się w manipulację albo w projektowanie zależności, o której ostrzega Pataranutaporn, mówiąc o modelu, który stale afirmuje użytkownika zamiast go czasem skorygować.

Ten framework nie daje gotowej odpowiedzi na pytanie, ile tarcia jest właściwe. Nikt jej dziś nie ma, bo to zależy od kontekstu, etapu życia użytkownika i stawki decyzji. Ale daje strukturę, która nie pozwala pominąć pytania, zanim wdroży się kolejne ułatwienie, i pozwala tę samą interakcję zdiagnozować, nazwać jej właściwy tryb i przypisać jej konkretny wzorzec, zamiast rozstrzygać o tarciu intuicyjnie za każdym razem od nowa.

Właśnie tę warstwę, między tym, co AI potrafi zrobić, a tym, co powinno zrobić dla konkretnego użytkownika w konkretnym momencie, projektuję od lat. Dopiero teraz nauka zaczyna nazywać ją po imieniu.

---

*Jeśli pracujesz nad produktem, w którym AI odpowiada za kluczowe decyzje użytkownika, chętnie pokażę, jak wygląda pełna wersja frameworku i biblioteki wzorców. Link w komentarzu.*

---

## Źródła

1. Zohar, Bloom, Inzlicht — *Against frictionless AI*, Communications Psychology, 2026 [https://www.nature.com/articles/s44271-026-00402-1](https://www.nature.com/articles/s44271-026-00402-1)
2. Pat Pataranutaporn (MIT Media Lab), wywiad — *3 Questions: Neural transparency and the future of AI design*, MIT News, lipiec 2026 [https://news.mit.edu/2026/3-questions-neural-transparency-and-future-of-ai-design-0715](https://news.mit.edu/2026/3-questions-neural-transparency-and-future-of-ai-design-0715)
3. Observer — artykuł o zaufaniu do AI i ekonomii władzy/osądu, lipiec 2026 [https://observer.com/2026/07/future-ai-power-judgment-trust/](https://observer.com/2026/07/future-ai-power-judgment-trust/)
4. KPMG i Uniwersytet w Melbourne — badanie o zaufaniu do AI w 47 krajach [https://kpmg.com/xx/en/media/press-releases/2025/04/trust-of-ai-remains-a-critical-challenge.html](https://kpmg.com/xx/en/media/press-releases/2025/04/trust-of-ai-remains-a-critical-challenge.html)
5. Deloitte — zwrot części kosztów kontraktu rządowego w Australii po wykryciu zmyślonych źródeł w raporcie wspomaganym AI [https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund/](https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund/)
6. Wielka Czwórka — wprowadzenie usług AI assurance jako linii biznesowej [https://thefinancestory.com/big-4-to-launch-ai-assurance-services](https://thefinancestory.com/big-4-to-launch-ai-assurance-services)
7. Lloyd’s of London — polisy ubezpieczeniowe od halucynacji AI [https://www.armilla.ai/resources/insurers-launch-cover-for-losses-caused-by-ai-chatbot-errors](https://www.armilla.ai/resources/insurers-launch-cover-for-losses-caused-by-ai-chatbot-errors)
