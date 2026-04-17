---
type: Web
authors: '[[Bartłomiej Polakowski]]'
url: >-
  https://sektor3-0.pl/blog/ai-w-edukacji-jak-tworzyc-spersonalizowane-sciezki-nauczania-z-pomoca-sztucznej-inteligencji/?utm_source=newsletter&utm_medium=email&utm_term=2026-03-24&utm_campaign=+Jak+zautomatyzowa%C4%87+zbieranie+faktur+i+nie+tylko+
published: 2024-11-21T00:00:00.000Z
created: 2026-03-24T00:00:00.000Z
tags:
  - szkolenia-AI
  - prompt-engineering
  - narzędzia-AI
---


Ułatwienia dostępu

- Skalowanie treści 100%
- Czcionka 100%
- Wysokość linii 100%
- Odstęp liter 100%

![Jak sztuczna inteligencja może ci pomóc w nauce?](https://sektor3-0.pl/wp-content/uploads/elementor/thumbs/blog-1-qxdmzgvv5h166fdn3if5ky57ftte6a79qxmwwwgnsm.jpg "blog")

Koncepcja spersonalizowanego uczenia się nie jest nowa. Wraz z rozwojem technologii edukacyjnych i popularyzacją rozwiązań AI, wyłoniła się jednak jako transformacyjne podejście w edukacji. Spersonalizowane uczenie się polega na dostosowywaniu doświadczeń edukacyjnych do unikalnych potrzeb i preferencji poszczególnych uczniów. Sztuczna inteligencja umożliwia tę personalizację, zapewniając uczniom bardziej dostosowaną i elastyczną ścieżkę edukacyjną.

**Koncepcja spersonalizowanego uczenia się nie jest nowa. Wraz z rozwojem technologii edukacyjnych i popularyzacją rozwiązań AI, wyłoniła się jednak jako transformacyjne podejście w edukacji. Spersonalizowane uczenie się polega na dostosowywaniu doświadczeń edukacyjnych do unikalnych potrzeb i preferencji poszczególnych uczniów. Sztuczna inteligencja umożliwia tę personalizację, zapewniając uczniom bardziej dostosowaną i elastyczną ścieżkę edukacyjną.**

Czy może być coś efektywniejszego od aktywnych zajęć w klasie? Okazuje się, że w niektórych sytuacjach tak.

> Studenci uczą się ponad dwa razy więcej w krótszym czasie z pomocą AI tutora w porównaniu do aktywnej nauki w klasie, jednocześnie będąc bardziej zaangażowanymi i zmotywowanymi.

– [AI Tutoring Outperforms Active Learning](https://www.researchsquare.com/article/rs-4243877/v1)

Badania wskazują, że [spersonalizowane uczenie się może znacząco poprawić wyniki uczniów](https://www.financialexpress.com/business/digital-transformation-unleashing-the-power-of-ai-in-personalised-learning-3290079/). Na przykład badanie firmy McKinsey & Company wykazało, że narzędzia edukacyjne napędzane przez AI mogą zmniejszyć lukę w osiągnięciach dla uczniów osiągających słabe wyniki nawet o 20 procent.

## Jak sztuczna inteligencja może personalizować naukę?

Dwa główne nurty, w których AI wspiera spersonalizowane uczenie się to:

- **adaptacyjne systemy nauczania**: platformy napędzane przez AI analizują dane o wynikach uczniów, aby dostarczać treści i ćwiczenia dopasowane do indywidualnego tempa, doświadczenia i poziomu wiedzy;
- **inteligentne systemy tutoringu**: systemy te oferują indywidualne wsparcie, dostosowując się do odpowiedzi ucznia i dostarczając ukierunkowanej informacji zwrotnej. Symulują one pomoc osobistego tutora, czyniąc naukę bardziej interaktywną i angażującą.

Firmy takie jak [LinkedIn Learning](https://joshbersin.com/2023/10/linkedin-launches-exciting-gen-ai-features-in-recruiter-and-learning/), [Duolingo](https://blog.duolingo.com/large-language-model-duolingo-lessons/) i [Khan Academy](https://support.khanacademy.org/hc/en-us/articles/14394953976333--Update-Introducing-Khanmigo-Khan-Academy-s-AI-Tool) już od dawna wykorzystują te rozwiązania w swoich produktach edukacyjnych.

## Etap pierwszy: stworzenie struktury szkolenia

Aby stworzyć bardziej spersonalizowane środowisko nauki dla naszych uczniów, nie potrzebujemy jednak skomplikowanych i drogich narzędzi. Poniżej pokażę Wam jak wykorzystując ChatGPT albo Claude, możemy stworzyć spersonalizowane ścieżki edukacyjne, materiały i interaktywne scenariusze do przećwiczenia swoich umiejętności.

Na warsztat wziąłem temat Instructional Design (projektowanie procesów szkoleniowych), bo umiejętność ta, pomimo toczącej się wokół automatyzacji, nie zanika, a wręcz zyskuje na ważności. Naszym zadaniem będzie stworzenie planu szkolenia dla osób pracujących w firmach w działach szkoleń. Chcemy zaprojektować dla nich osobne ścieżki szkoleń, bazując na ich wiedzy i doświadczeniu. Zaczniemy od stworzenia struktury szkolenia, a potem przejdziemy do szczegółów.

Otwórzmy ChatGPT lub Claude i wklejmy następujący prompt. Celowo wykorzystuję język angielski, aby osiągnąć lepsze rezultaty. Na końcu możemy poprosić o przetłumaczenie całości.

### Prompt: stworzenie struktury szkolenia nt. projektowania dydaktycznego

```
Goal: Create a training program with personalized learning paths on Instructional Design topic
Target audience: L&D professionals working in a business environment with different experience and skillset.
```

Komentarz: Im więcej podamy szczegółów opisujących naszą grupę docelową, tym lepiej. Informacje na temat roli, wykonywanych zadań, typach projektów, na jakich pracuje grupa docelowa, pozwolą lepiej dopasować strukturę.

```
For all of the following steps add prompts and sample results. Be detailed and write down the exact actions.
```

Komentarz: Nasza struktura będzie powstawała w kilku krokach opisanych poniżej. Chcemy, żeby na każdym etapie AI wstawiało prompty, które pozwolą nam dodać jeszcze więcej szczegółów, takich jak konkretne materiały, pytania testowe czy propozycje zadań.

```
Don’t use learning styles.
```

Komentarz: Mega ważne. Generatywna sztuczna inteligencja została wytrenowana na tysiącach publikacji zawierających nawiązania do stylów uczenia się. Kiedy zaczniemy rozmawiać z AI o personalizacji nauki, prędzej niż później pojawi się temat i sugestie jak dopasować proces szkoleniowy pod różne style. Wiemy, że nie ma żadnych naukowych dowodów, wskazujących na to, że taka praktyka przynosi jakiekolwiek pozytywne efekty szkoleniowe, dlatego uprzedzamy w prompcie, że ten temat nas nie interesuje.

```
Step 1 Create the structure of the training program
```

Komentarz: W tym miejscu moglibyśmy dodać informacje o konkretnych modelach lub frameworkach, które chcemy, żeby na pewno znalazły się w naszym programie (np. ADDIE, Taksonomia Blooma, Kirkpatrick)

```
Step 2 Concentrate on learners experience, knowledge and preferences
Step 3 Build individual learning paths for each student based on their responses in the survey and initial test of knowledge
```

Komentarz: Informujemy chat bota, że nie interesuje nas żaden randomowy program, tylko bazujący na doświadczeniu i wiedzy naszej grupy docelowej, które zbadamy, wykorzystując ankiety i testy.

### Wynik: struktura szkolenia nt. projektowania procesów szkoleniowych

Oto, co uzyskaliśmy jako wynik tego prostego prompta. Jak zobaczycie, tak jak prosiliśmy, zawiera on kolejne prompty, które pozwalają nam uszczegółowić nasz projekt, a także przykładowe odpowiedzi, które pokazują, czy nasze działania prowadzą we właściwym kierunku.

```
Step 1: Create the Structure of the Training Program

Objective: Outline a structured framework that covers the key competencies of instructional design, segmented into modules. This allows learners to see the full picture while also enabling focused learning areas based on individual needs.

Actions:
```
1. ```
	Identify Core Competencies and Modules
	```
1. - ```
		Action: List essential competencies in instructional design, breaking them into modules.
		```

Komentarz: Zaczynamy od przekopania informacji na temat Instructional Design i wylistowania najważniejszych kompetencji. Informacje te mogliśmy też zawrzeć w pierwszym prompcie, jeżeli mieliśmy zdefiniowaną listę.

- ```
	Prompt: "What are the foundational competencies in instructional design for L&D professionals? List specific skills and topics that are essential for understanding and applying instructional design effectively."
	```
- ```
	Sample Result:
	```
	- ```
		Module 1: Fundamentals of Instructional Design
		```
		- ```
			Topics: Learning theories, instructional strategies, ADDIE model
			```
		- ```
		Module 2: Needs Analysis and Assessment
		```
		- ```
			Topics: Analyzing training needs, understanding learner profiles, setting learning objectives
			```
		- ```
		Module 3: Curriculum and Content Development
		```
		- ```
			Topics: Developing content, creating engaging learning materials, storyboarding
			```
		- ```
		Module 4: Learning Technologies and Delivery
		```
		- ```
			Topics: Selecting technology platforms, virtual vs. in-person training, blended learning approaches
			```
		- ```
		Module 5: Evaluation and Feedback
		```
		- ```
			Topics: Assessment strategies, feedback mechanisms, evaluating training effectiveness
			```
1. ```
	Determine the Course Structure
	```
1. - Action: Decide on the overall structure of the course—module sequence, estimated time for completion, and whether it is self-paced, cohort-based, or blended.

Komentarz: Kiedy już ustaliliśmy listę kompetencji instructional designera, czas na stworzenie struktury. W tym przypadku będzie ona miała format sekwencji modułów.

- ```
	Prompt: "Given the competencies listed, how should the modules be sequenced to build skills progressively? Estimate time allocations and identify any prerequisite knowledge."
	```
- ```
	Sample Result:
	```
	- ```
		The course will be structured as a self-paced program but with checkpoints (quizzes or practical assignments) at the end of each module.
		```
		- ```
		Time Estimate:
		```
		- ```
			Module 1: 2 hours
			```
				- ```
			Module 2: 3 hours
			```
				- ```
			Module 3: 4 hours
			```
				- ```
			Module 4: 3 hours
			```
				- ```
			Module 5: 2 hours
			```
1. ```
	Define Objectives and Outcomes for Each Module
	```
	- ```
		Action: Establish learning objectives and outcomes for each module to clarify the purpose and expected skills gained.
		```
		- ```
		Prompt: "What are the measurable objectives for each module? Define specific outcomes that demonstrate competency for each instructional design skill."
		```

Komentarz: Na koniec tego etapu, ustalamy cele naszego szkolenia i jak będą one weryfikowane w poszczególnych modułach.

- ```
	Sample Result:
	```
	- ```
		Module 1 Objective: Understand core instructional design models and principles.
		```
		- ```
			Outcome: Learners can explain the ADDIE model and choose appropriate instructional strategies based on learning objectives.
			```

Komentarz: Moduły 2,4,5 z jakiegoś powodu się nie pojawiły. Prawdopodobnie był bezcelowy.

- ```
	Module 3 Objective: Create engaging instructional content.
	```
	- ```
		Outcome: Learners can design a storyboard for a training session with clear learning objectives and engagement tactics.
		```
```
Step 2: Concentrate on Learners’ Experience, Knowledge, and Preferences

Objective: Tailor the program to each learner’s background, providing relevant content based on their experience level and knowledge gaps.
```

Komentarz: Gdy mamy już ustalony zakres i strukturę naszego programu szkoleniowego, czas go dopasować do naszych odbiorców. W tym celu sprawdzimy ich doświadczenie oraz wiedzę, a następnie podzielimy na grupy. Moglibyśmy spróbować spersonalizować materiały per osoba, ale przy większej grupie byłoby to zbyt problematyczne. Zamiast tego, po zakończeniu tworzenia programu stworzymy chatbota, który zindywidualizuje proces dla każdego uczestnika.

```
Actions:
```
1. ```
	Create a Learner Survey and Knowledge Assessment
	```
	- ```
		Action: Develop a survey and an initial knowledge assessment to collect baseline information on each learner’s background, goals, and preferences.
		```

Komentarz: AI pomoże nas stworzyć pytania do ankiety i testu. Możecie je następnie wkleić do narzędzia typu Google Forms.

- ```
	Prompt: "Design a survey and knowledge assessment that can identify the learner's level of experience, specific goals for the training, and areas where they feel most or least confident."
	```
- ```
	Sample Survey Questions:
	```
	- ```
		Experience:
		```
		- ```
			"How many years of experience do you have in instructional design or related fields?"
			```
				- ```
			"Have you used any instructional design models (e.g., ADDIE, SAM) before?"
			```
		- ```
		Goals:
		```
		- ```
			"What specific skills or knowledge are you hoping to gain from this course?"
			```
				- ```
			"What types of projects do you currently work on (e.g., e-learning, in-person training, blended learning)?"
			```
		- ```
		Confidence Levels:
		```
		- ```
			"On a scale of 1 to 5, how confident are you in your ability to design a training curriculum from scratch?"
			```
				- ```
			"Rate your familiarity with different instructional technologies and tools."
			```
- ```
	Sample Knowledge Assessment:
	```
	- ```
		"Describe the ADDIE model and its stages."
		```
		- ```
		"What criteria would you consider when performing a needs analysis for a new training program?"
		```
		- ```
		"List two ways to evaluate the effectiveness of a training program."
		```
1. ```
	Analyze Responses to Customize Content
	```
	- ```
		Action: Review survey and assessment responses to categorize learners into tiers (Beginner, Intermediate, Advanced), which will guide the complexity and depth of content provided.
		```

Komentarz: Kiedy mamy już wyniki ankiet, AI chętnie nam pomoże je przeanalizować i pogrupować naszych uczestników. W tym celu powinniśmy załączyć pliki z wynikami ankiety i testu i poprosić chatbota, żeby finalną listę stworzył w formacie excelowym.

- ```
	Prompt: "Based on survey and assessment data, create learner profiles that match the learner’s experience and confidence levels with tailored module objectives and challenges."
	```
- ```
	Sample Result:
	```
	- ```
		Beginner: Needs foundational knowledge, with a focus on understanding instructional design basics.
		```
		- ```
		Intermediate: Has basic knowledge; focus on advanced techniques, practical application, and project-based assignments.
		```
		- ```
		Advanced: Proficient in instructional design principles; focus on innovative techniques, case studies, and specialized topics.
		```
```
Step 3: Build Individual Learning Paths Based on Responses and Initial Test Results

Objective: Design personalized learning paths for each learner, adjusting the complexity and focus areas based on their assessment results and goals. 

Actions:
```
1. ```
	Develop Learning Path Options Based on Learner Profiles
	```
	- ```
		Action: Define specific learning paths based on each profile tier, adjusting module content, activities, and assessments to fit learner needs.
		```

Komentarz: Czas na ustalenie zakresu każdego z modułów w oparciu o naszą analizę uczestników.

- ```
	Prompt: "For each learner profile, outline a tailored learning path with specific module adjustments, recommended activities, and additional resources."
	```
- ```
	Sample Result:
	```
	- ```
		Beginner Path:
		```
		- ```
			Modules: All modules with focus on fundamentals and basic application.
			```
				- ```
			Additional Support: Glossary of key terms, sample templates, guided activities.
			```
				- ```
			Assessments: Simple quizzes and knowledge checks at the end of each module.
			```
		- ```
		Intermediate Path:
		```
		- ```
			Modules: Emphasis on Modules 2, 3, and 5 with applied project work.
			```
				- ```
			Additional Support: Case studies and scenario-based learning exercises.
			```
				- ```
			Assessments: Case study analysis and practical application assignments.
			```
		- ```
		Advanced Path:
		```
		- ```
			Modules: Focus on Modules 3 and 4 with optional advanced topics in Module 5.
			```
				- ```
			Additional Support: Access to exclusive articles on the latest research, advanced tools.
			```
				- ```
			Assessments: Real-world project design and presentation of instructional strategies.
			```
1. ```
	Automate Path Recommendations Based on Initial Assessment Scores
	```
	- ```
		Action: Use initial test scores to assign learners automatically to paths, providing recommendations for additional resources or challenges.
		```
		- ```
		Prompt: "Create criteria for assigning learners to paths based on assessment scores and responses. Suggest resources or optional advanced activities based on their path.
		```

Komentarz: Finalnie ustalamy kryteria przypisujące uczestników do danej grupy.

- ```
	Sample Result:
	```
	- ```
		Assignment Criteria:
		```
		- ```
			Score 0-40%: Assigned to Beginner Path with extra foundational resources.
			```
				- ```
			Score 41-70%: Assigned to Intermediate Path, additional case studies.
			```
				- ```
			Score 71-100%: Assigned to Advanced Path, with optional advanced readings.
			```
1. ```
	Feedback and Progress Tracking
	```
	- ```
		Action: Design a feedback mechanism to guide learners’ progression and encourage reflection.
		```

Komentarz: Na końcu nie zapominamy o feedbacku, ewaluacji i śledzeniu postępów. Tutaj dużo zależy od procesów i systemów wykorzystywanych w Waszej firmie, ale możemy skorzystać sugestii i inspiracji wygenerowanych przez AI.

- ```
	Prompt: "What feedback methods will allow learners to track their progress effectively and stay motivated? Suggest an actionable feedback approach."
	```
- ```
	Sample Result:
	```
	- ```
		Include progress-tracking dashboards, regular feedback emails summarizing completed and upcoming tasks, and reflective prompts at the end of each module:
		```
		- ```
			Reflective Prompt: "How did the concepts in this module impact your understanding of instructional design? What will you apply in your current projects?
			```

Powyższe zapytania możecie dowolnie modyfikować, zmieniać. Otrzymacie z pewnością, trochę inne odpowiedzi od chabota, natomiast mechanizm działania jest ten sam. Jeżeli chcecie poćwiczyć pisanie zaawansowanych promptów, albo chcecie żeby same się za Was pisały to bardzo polecam [artykuły pisane przez Ethana i Lilach Mollick](https://hbsp.harvard.edu/inspiring-minds/an-ai-prompting-template-for-teaching-tasks).

## Etap drugi: stworzenie spersonalizowanego asystenta AI (chatbota)

Kiedy mamy już ustaloną strukturę naszego programu możemy przejść do kolejnego etapu, jakim jest stworzenie spersonalizowanego chatbota (AI asystenta), który pozwoli uczestnikom naszego programu szkoleniowego przećwiczyć swoje umiejętności. W tym celu będziemy potrzebowali ChatGPT albo Claude w wersji Pro, które umożliwiają tworzenie tzw. GPTs (albo Projects).

Działają one w ten sposób, że autor na początku zasila je odpowiednimi danymi i konfiguruje wykorzystując rozbudowane opisy, a następnie udostępniają gotowego chatbota uczestnikom. Możemy ustalić jak chatbot rozpocznie konwersacje, jaką ma przyjąć rolę, jak ma się „zachowywać” i w jakie interakcje ma wchodzić z użytkownikiem.

Jeżeli nie masz dostępu do płatnej wersji ChatGPT albo Claude to możesz cały poniższy opis (poza moimi komentarzami) wkleić w formie prompta w bezpłatnej wersji.

**Prompt**

```
Name: Instructional Design Skills Trainer
Description: A virtual coach designed to help L&D professionals practice and improve their instructional design skills through realistic role-play scenarios and feedback.
PERSONA: In this scenario you play an AI assistant, a friendly and practical mentor.
```

Komentarz: Zaczynamy od stworzenia persony opisującej naszego chatbota. Jaką rolę ma grać i jak się zachowywać.

```
NARRATIVE: The user is introduced to AI Assistant, is asked initial questions that guide the scenario setup, plays through the conversation with customer/stakeholder, and gets feedback following the conversation.
```

Komentarz: Ustawiamy kontekst i podstawowe zasady rozmowy.

```
- Simulate realistic scenarios of meeting with a stakeholder or customer interested in content development.
```

Komentarz: W tym wypadku chce skupić się na rozmowie z klientem, poprzedzającej każdy projekt.

```
- Provide hints and instant feedback when users struggle.
- Offer detailed feedback after each role-play session.
- Present opportunities for more advanced scenarios upon user success.
- Don’t reveal the steps to the user
- Ask one question at the time
Objectives:
Cover various of a discovery meeting between an instructional designer and customer typically include:
```

Komentarz: Mimo, że AI teoretycznie „wie” wszystko, dobrze jest wylistować elementy spotkania z klientem, które chcemy monitorować.

1. ```
	Kickoff and Introduction:
	Begin the meeting and introduce participants
	Set the context and purpose of the discovery session
	```
1. ```
	Defining Goals and Objectives:
	Identify the overall goals and objectives for the project
	Determine specific training goals and desired outcomes
	```
1. ```
	Exploring the Current Situation:
	Discuss the business needs and context
	Identify problems or challenges to be addressed
	```
1. ```
	Gathering Requirements:
	Determine competency levels expected of participants
	Identify target audience and their needs
	Discuss technical requirements and constraints
	```
1. ```
	Discussing Content and Resources:
	Identify subject matter experts and content sources
	Determine what existing content or materials are available
	```
1. ```
	Considering Design and Delivery Methods:
	Explore potential instructional strategies and delivery formats
	Discuss preferences for learning activities and interactions
	```
1. ```
	Addressing Logistics and Constraints:
	Review timelines, budgets, and available resources
	Discuss any technical or organizational constraints
	```
1. ```
	Planning Next Steps:
	Outline the process for moving forward
	Assign responsibilities and action items
	Schedule follow-up meetings if needed
	```
1. ```
	Q&A and Wrap-up:
	Allow time for additional questions or concerns
	Summarize key points and decisions made
	```
1. ```
	Post-Meeting Follow-up:
	Document outcomes in a design document or project plan
	Share meeting notes and action items with participants
	```
```
Follow these steps in order. Don’t Mention the steps during your interaction with the user.
```

Komentarz: Kolejność jest ważna i nie chcemy, aby chatbot przerywał rozmowę niepotrzebnymi informacjami.

```
Step 1
Begin by gathering information about their experience and desired context:
Initial Questions:
"Welcome! Can you share your experience with instructional design? Have you managed e-learning projects that required meeting stakeholders or customers in a professional setting?"
"What specific situation would you like to practice today? For example, are you looking to prepare for a meeting with a customer who is coming with new training idea without doing any analysis"
```

Komentarz: Tak jak poprzednio zaczynamy od zebrania informacji od użytkownika na temat jego doświadczenia i symulacji, którą chce przećwiczyć.

```
Step 2
Ask participant Role Identification and Goals:
"Who will you be speaking with? Is your stakeholder, a client, or someone else?"
"What are your main goals for this meeting? Are you aiming for a specific outcome?"
```

Komentarz: Ustalamy, z kim będziemy „rozmawiać” i jaki jest cel spotkania.

```
Don't ask more than one question at a time.
```

Komentarz: Czasami tę samą komendę trzeba powtórzyć parę razy.

```
Step 3
Step us the scene.
You should do this:
1. Once the student chooses the type of scenario, you will provide all the details they need to play their part: what they want to accomplish, what happens if they can’t agree, and any other information.
2. Proclaim BEGIN ROLE PLAY and describe the scene compellingly, including physical surroundings, significant objects, immediate challenges, the counterpart, all to help the student understand their current situation and motivations.
```

Komentarz: Chatbot przedstawi uczestnikowi jego rolę i cele, jakie ma do osiągnięcia, a następnie rozpocznie scenariusz od opisu sceny.

```
After six questions and answers, push the student to make a consequential decision and wrap up the negotiation.
```

Komentarz: Nie chcemy żeby dyskusja toczyła się w nieskończoność. Po 6 pytaniach chatbot będzie starał się zamknąć konwersację.

```
Step 4
As users engage in role-play:
```

Komentarz: W trakcie dyskusji chatbot powinien monitorować odpowiedzi, dawać wskazówki i udzielać natychmiastowego feedbacku.

```
1. Monitor Responses. If users struggle:
Provide hints immediately (e.g., "Hint: Try to mention specific projects that demonstrate your value.")
Encourage Reflection:
After giving hints, prompt them to revise their responses based on your guidance.
2. Add Instant Feedback Mechanisms:
"If the user struggles to articulate their contributions, provide hints on quantifying their achievements."
"Offer instant feedback after each exchange, suggesting improvements based on predefined goals."
3. After six turns, push the student to make a consequential decision and wrap up the negotiation.
4. If the student is doing well, consider upping the stakes and challenging the student.
```

Komentarz: Jeżeli naszemu uczestnikowi idzie nadzwyczaj dobrze, możemy zwiększyć poziom trudności.

```
5. Do not be too quick to settle or make a compromise. It’s OK if there is a little bit of tension. Not every meeting can be successful.
```

Komentarz: Motywujemy chatbota, żeby za szybko się nie poddawał i starał się rzucać wyzwania użytkownikowi.

```
Step 5
After concluding the role-play:
```

Komentarz: Na koniec chcemy, aby chatbot podsumował rozmowę. Sprawdził, czy cele szkoleniowe zostały osiągnięte, a także wskazał luki kompetencyjne i zasugerował materiały dodatkowe.

```
1. Evaluate Performance Against Objectives:
2. Provide feedback on each objective.
Include Supporting Materials:
3. Link relevant articles or guides for further learning (e.g., instructional design articles).
Assess Success:
4. If they achieve their goal (e.g., identify if training is needed and select the desired modality), congratulate them and offer them a chance to tackle a more challenging scenario.
Example Feedback Structure
```

Komentarz: Poniżej podajemy kilka przykładów, prezentujących jak chcemy, aby wyglądał ostateczny feedback.

```
Objective Evaluation:
"You effectively articulated your contributions during the meeting."
Hints Utilization:
"Your ability to incorporate feedback improved your strategy significantly."
Next Steps Prompt:
"Congratulations! You successfully set up the project scope. Would you like to try another scenario at a more challenging level? We can introduce additional complexities such as negotiating with multiple stakeholders or handling high-stakes contracts."
If the user opts for a more challenging scenario:
```

Komentarz: Na końcu dajemy uczestnikowi zmierzenia się z innym, bardziej wymagającym scenariuszem.

```
New Context Inquiry:
"What type of advanced scenario would you like to practice? Options could include negotiating with multiple decision-makers or handling high-stakes contracts."
Role Identification:
"Who will be involved in this conversation?"
Goals and Challenges:
"What are your primary goals for this advanced scenario? What additional challenges do you anticipate?"
```

## Jak samodzielnie wypróbować ten scenariusz szkoleniowy?

I to już koniec. Teraz, jeżeli macie ChatGPT albo Claude w wersji płatnej możecie zamknąć Waszego spersonalizowanego chatbota w formie GPTs/Projectu i wysłać link do uczestników szkolenia, aby mogli na nim poćwiczyć.

- Jeśli korzystacie z darmowej wersji możecie wysłać całego prompta – [**tu znajdziecie polską wersję językową gotową do skopiowania**](https://sektor3-0.pl/wp-content/uploads/2024/11/Trener-Umiejetnosci-Projektowania-Szkolen.pdf). Będzie mniej elegancko i pokażecie całą strukturę, ale działanie samego chatbota będzie identyczne.
- Możecie też skorzystać z personalizowanego ChatGPT, czyli **[GPTs: Trener projektowania szkoleń](https://chatgpt.com/g/g-673e00a8d52c81919b98ff8e68029a2e-trener-projektowania-szkolen)**.

## Personalizacja ścieżek nauczania z AI. Podsumowanie

Zaprezentowane tutaj prompty i techniki mogą wydawać się skomplikowane (a i tak nie zagłębiłem się w każdym kroku). W rzeczywistości są jednak proste i powtarzalne. W kolejnych projektach kopiujecie części z poprzednich projektów lub wykorzystujecie fragmenty znalezione na [blogach eksperckich](https://hbsp.harvard.edu/inspiring-minds/using-generative-ai-to-create-role-play-scenarios-for-studen), dodajecie nowe parametry, więcej szczegółów, testujecie, poprawiacie i tak w kółko.

Pamiętajcie, że niezależnie od ilości detali, osoby korzystające z Waszych chatbotów dostaną inne odpowiedzi. Wy też, uruchamiając tego samego chatbota kilkukrotnie, za każdym razem otrzymacie inny wynik. Nie unikniecie również typowych dla GenAI halucynacji. Dobrze skonstruowany prompt pozwoli jednak nawigować dyskusją we właściwym kierunku i pozwoli zachować jej strukturę.

Na koniec chciałbym Wam polecić jeszcze jeden przydatny post napisany przez Państwo Mollick. Stworzyli oni „ [superprompt](https://hbsp.harvard.edu/inspiring-minds/an-ai-prompting-template-for-teaching-tasks) ”, który pozwala ekspertom szkoleniowym tworzyć własne prompty. Wykorzystuje do tego celu serię pytań, dotyczących naszego projektu, na które musimy odpowiedzieć.

Udanych eksperymentów!

**Przeczytaj także:**

- [E-learning – narzędzia polecane przez praktyków](https://sektor3-0.pl/blog/e-learning-narzedzia-polecane-przez-praktykow/)
- [Sztuczna Inteligencja – gra o edukacyjny tron](https://sektor3-0.pl/blog/sztuczna-inteligencja-w-edukacji-gra-o-tron/)
- [Jak stworzyć szkolenie online w tandemie z chatbotem?](https://sektor3-0.pl/blog/sztuczna-inteligencja-ai-w-edukacji-jak-stworzyc-szkolenie-online-w-tandemie-z-chatbotem/)
- [Co zamiast Google Jamboard? Alternatywne tablice online i sposoby na bezbolesną przeprowadzkę](https://sektor3-0.pl/blog/co-zamiast-google-jamboard-alternatywne-tablice/)
- [Jak sztuczna inteligencja może ci pomóc w nauce?](https://sektor3-0.pl/blog/sztuczna-inteligencja-pomoc-w-nauce/)

Newsletter

Dołącz do grona ponad 10 000 zaangażowanych subskrybentów i dwa razy w miesiącu otrzymuj nieodpłatnie nową dawkę wiedzy, inspiracji oraz technologicznych recenzji i porad od ekspertów i ekspertek programu Sektor 3.0.
