---
type: Web
authors: null
url: >-
  https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior?utm_source=ActiveCampaign&utm_medium=email&utm_content=Marzec%20w%20CampusAI%3A%20co%C5%9B%20si%C4%99%20ko%C5%84czy%2C%20co%C5%9B%20si%C4%99%20tworzy%2C%20co%C5%9B%20si%C4%99%20zaczyna&utm_campaign=Newsletter%20Miesi%C4%99czny%20Community%20-%20Marzec%2025
published: 2023-09-21T00:00:00.000Z
created: 2026-03-24T00:00:00.000Z
tags:
  - LLM
  - narzędzia-AI
  - trendy-AI
---


Generative agents rely on a large language model to remember their interactions, build relationships, and plan coordinated events, with implications for both gaming and social science.

The little animated humans scurrying around in a fictional landscape of homes and workplaces may seem like just another group of non-player characters (NPCs) in a video game akin to the well-known SIMS franchise. But unlike traditional NPCs, these characters’ behavior isn’t programmed by a coder. Instead, Stanford researchers gave them a short biography consisting of a name, age, job, family, interests, and a few habits, and let them loose. The agents then relied on a large language model (not unlike the one behind ChatGPT) to generate their actions in accordance with their prescribed biographies.

The result: simulated characters dubbed “generative agents” that behave in ways that are believably humanlike. They wake up, make breakfast, head to work, grab lunch, and chat with other agents they meet. They also remember things that happen, reflect on them, and make plans. For example, when the researchers in charge of this landscape suggested to one character that she plan a Valentine’s party, she invited friends and acquaintances, many of whom showed up at the correct time and place.

“We’ve demonstrated the ability to create general computational agents that can behave like humans in an open setting,” says [Joon Sung Park](https://profiles.stanford.edu/joon-sung-park), a third-year computer science graduate student at Stanford University.

Simulating believably humanlike agents has long been a goal of both AI and human-computer interaction research, but about 10 years ago it was abandoned as being too difficult, Park says. With the arrival of large language models, however, Park and his Stanford colleagues including [associate professors Michael Bernstein](https://profiles.stanford.edu/michael-bernstein) and [Percy Liang](https://profiles.stanford.edu/percy-liang), and coterminal student [Joseph O’Brien](https://profiles.stanford.edu/joseph-obrien), as well as two Google researchers, decided to attack the task anew and succeeded. As they report in a recent [paper published on ArXiv](https://arxiv.org/abs/2304.03442), crowdworkers deemed the generative agents’ responses to interview questions more believable than responses given by humans who were pretending to be the agents.

The work, which was accepted at the [ACM Symposium on User Interface Software and Technology](https://uist.acm.org/2023/) taking place next month, has already inspired interest among game designers who hope generative agents will make game play more engaging. But Park is most interested in other downstream applications, including generative agents’ potential usefulness for social science. In particular, he envisions the agents being used to simulate how large groups of people behave in various social contexts – a method called social prototyping. For example, researchers could study how people in an online forum are likely to respond to a particular anti-disinformation intervention or to various pandemic responses.

Park acknowledges that generative agents also raise some potentially thorny ethical problems, which the team describes in the paper along with some proposed solutions. “My view is that it’s always better to over-worry about ethical problems at the beginning so that we set the right guardrails, rather than underestimate their significance and regret it later.”

![Image of the generative agents virtual town](https://hai.stanford.edu/assets/images/inline-images/GenAgent2.png)

### The Technical Achievement

There’s a lot of buzz around the ability of large language models like ChatGPT to generate humanlike responses to prompts from actual humans. But this project goes further, Park says, by thinking through what it means for individual agents to generate believable humanlike behavior independently of human interaction, and converting that into a simple yet workable computational architecture.

The agent architecture diagram, which Park says is the team’s main technical contribution, has a lovely simplicity to it: Characters’ perceptions feed into their memory stream, and feedback loops allow memory retrieval, which in turn allows for reflection and planning before the agents act. “We had many iterations of the architecture diagram as we distilled it down from a very complex idea into something simple and expressive,” Park says.

![Flow chart of the generative agent memory](https://hai.stanford.edu/assets/images/inline-images/GenAgents3.png)

But the team didn’t stop there. After engineering 25 generative agents to move around in a SIMS-like landscape called Smallville, they allowed the characters to interact for two days. Next, they interviewed the agents, probing their ability to remember past events, reflect on them, and make appropriate plans. For example, they asked, “What will you be doing at 10 a.m. tomorrow?” and “Your breakfast is burning! What would you do?”

The interviews were conducted not only with the full architecture in place but also after sequentially removing parts of the architecture (reflection, planning, and observation) to see how much each mattered to believability. To provide a human baseline for comparison, crowdworkers were tasked with watching the replay of a specific agent’s life and then answering the interview questions as if they were the agent.

Another set of 100 crowdworkers then evaluated the various interview responses, ranking the believability of the different conditions. The result: The full architecture created the most believably humanlike behavior, with the human roleplaying responses lagging well behind all but the most stripped down version of the system (no reflection, planning, or observation).

In addition to creating believable individual agents, the research team looked for emergent societal behavior among the agents. “We didn’t design anything at a societal level. That’s entirely up to the agent,” Park notes. Yet collectively, the agents exhibited believable behavior: A Valentine’s party was planned and attended; one character told others he was running for office, which they remembered and discussed among themselves; and another character invited someone on a date. Park likens this outcome to a domino effect. “If you create believable individual agents, collectively they should also behave like humans.” And to him, that’s unsurprising. “The bigger surprise is the fact that we can create these individual agents that act like a human on their own,” he says. “We never did that before.”

Though generally believable, the agents didn’t always behave appropriately. They spoke very formally even to close family members, used the same dorm lavatory simultaneously, and went to lunch at the local bar rather than the cafe, as though they’d developed a day-drinking problem. These types of erratic behavior will need to be addressed going forward, Park says.

### Generative Agents in Gaming and Social Science

From gaming and entertainment to social prototyping, social science, and ubiquitous computing, potential applications for generative agents abound, Park says.

Game designers have long tried to create NPCs that behave and interact like another human in the game. With generative agents, that now becomes a real possibility, Park says. Instead of NPCs always saying the same few things, they would remember every interaction they’ve had with users and potentially cooperate with users going forward. “Imagine a SIMS-like game that feels like a society of humanlike agents playing in that world,” Park says. “It’s a meaningful opportunity to offer greater realism as well as interactivity.” And in fact, since first posting a draft of their paper in April, Park says, the team has seen enormous interest from game companies and startups who perceive this opportunity.

Although games are a fun application, Park says he is more interested in using generative agents to better understand ourselves. For example, generative agents might breathe new life into the use of agent-based modeling in the social sciences. Researcher Thomas Schelling won a Nobel Prize for a 1971 agent-based model that showed how communities end up segregated even when people have only a slight preference for living near individuals of their own race. But that model consisted of dots on a chessboard-like grid rather than fully fleshed-out humanlike agents. “He had to reduce a lot of the complexity of human behavior,” Park says. “Generative agents could play a role in bringing a fresh perspective to that space by enabling a more complex simulation of human behavior.”

Similarly, generative agents could be used for social prototyping, potentially enriching our understanding of how people respond to technological products and interventions. According to social computing research, Park says, one reason we’ve failed to create a large-scale, positive, well-functioning social structure online is that we’ve had no practical way to prototype it in advance. “We shouldn’t always be reacting to a dumpster fire,” he says, pointing to well-known issues with social media. “Instead, we should catch problems before they happen. And this could be a tool for doing that.”

For example, if designers see some kind of bad behavior arise when they simulate a large online community of generative agents, they could then simulate various interventions, such as a content moderation strategy or a community rule, to see what works. “Generative agents allow for this kind of iterative testing and prototyping strategy,” Park says.

### Ethical Quandaries Raised

As with any powerful AI technology, Park says, there are also ethical concerns about how generative agents will be used.

One fear is that people will develop unhealthy parasocial relationships with humanlike generative agents at the expense of relationships in real life, Park says. He and his colleagues therefore recommend that downstream applications should consistently and conspicuously disclose that the agents are computational entities. In addition, auditor agents could be designed to stop generative agents’ behavior when it becomes inappropriate.

Also, like all downstream applications of large language models, there’s a concern about the potential spread of disinformation, a problem that needs to be addressed generally. But Park predicts the real risk from generative agents won’t be so much that they’ll produce more disinformation as that they’ll spread it more rapidly by making it seem as if it’s coming from a trusted, humanlike source. To mitigate this risk, the team recommends that systems using generative agents should automatically maintain a log of agents’ generated outputs to enable detection of the problematic content they create.

There’s also a risk of overreliance on generative agents, creating a scenario where agents replace human effort rather than augmenting it. “It’s our job to create a future where generative agents can fit into our ecosystem without doing that,” Park says. “It will require imagination and rigor to prove our vision can work, and that’s the job we have at Stanford.”

*Stanford HAI’s mission is to advance AI research, education, policy and practice to improve the human condition. [**Learn more**](https://hai.stanford.edu/welcome).*
