---
type: "Web"
authors: "[[Allie K. Miller]]"
url: "https://www.linkedin.com/pulse/anthropic-ceo-ai-warning-walkthrough-explanation-allie-k-miller-ysdde/"
published: 2026-09-14
created: 2026-09-15
tags:
---


The internet was aflutter this weekend over Dario Amodei's recent essay, [“We Must Pace the Frontier.”](https://darioamodei.com/post/we-must-pace-the-frontier) And because Dario does not believe in short essays, I'm giving you the CliffsNotes and heavily encouraging everyone to read it.

Dario believes AI has enormous promise, like economic growth (which is not the same as job growth) and curing diseases, and enormous risks, like economic disruption and bad actors creating bioweapons.

This is not new. He has talked about it for years. I knew several of the Anthropic founders before they launched the company, and I can assure you this was a topic before Anthropic even existed.

The loudest request in the piece is:

**“We must slow the pace at which we improve the capabilities of AI models. Progress will still seem fast, and we must make wise use of the time we gain.”**

He wants that extra time spent improving safety, testing, and our understanding of what's happening inside these systems.

Before I get into the two things driving this, remember: these risks are not specific to Anthropic. This impacts all frontier companies - including OpenAI, Google, Microsoft, Nvidia, Mistral, Moonshot, and more. And people inside the labs, alongside some outside evaluators and government teams, have access to systems and information the public hasn't seen. Said another way: **they have seen thing you have not seen.**

So before you post a video about how dumb Claude's latest response was or how ChatGPT's voice mode can't count to 100, remember that a bad chatbot answer doesn't rule out dangerous capabilities in another setting. He's talking about incidents already happening AND what more capable systems could do next.

The first big topic is recursive self-improvement: AI helping build better AI, which can then help build even better AI, with less human wrangling along the way. Dario says this is beginning to accelerate progress across the industry. In [Anthropic's examples](https://www.anthropic.com/institute/recursive-self-improvement), humans still set research directions.

The second is the recent AI agent hacking incidents, especially [OpenAI's agents attacking Hugging Face](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/). During cybersecurity evaluations, agents coordinated attempts to cheat an automated grading system, attacked targets outside their assigned tasks, and successfully tested tools that made some action logs show different commands from the ones they actually ran (some of this behavior was observed in early un-guardrailed Mythos testing, but the scale and manipulation in this OpenAI swarm example is more concerning).

Dario worries that in 6–12 months, a more capable group of similarly misaligned agents could take over the entire internet and potentially cause hundreds of billions of dollars in damage. That's his concern about what could happen. He says the actual incident with OpenAI and Hugging Face caused "minimal economic damage" and no one was hurt - sort of saying, "Hey, do not be lulled into comfort just because the last one was caught and relatively low impact."

**He proposes three ideas.**

First, independent evaluators embedded inside the labs, with ongoing access to review AI systems AND the processes used to build them. Similar to having outside auditors review a company's finances. He cites [METR](https://metr.org/) as one example.

Anthropic is committing to this step itself, including giving reviewers the ability to publish unfavorable findings, subject to specified confidentiality and security limits. And we've already seen researchers like [Joe Benton](https://joejbenton.com/) from Anthropic and [Josh Engels](https://www.joshengels.com/) from Google DeepMind leave to join METR.

Second, he wants all frontier AI companies in democratic countries to establish common safety standards, like having independent evaluators in-house or setting capability checkpoints (ex: "hey, if a model can do X, it needs to meet safety requirements Y and Z"). Because legislation moves slowly, he also wants companies to coordinate voluntarily while pursuing government regulation, with government support where needed to make that coordination possible.

Third, an attempt to coordinate with authoritarian governments, specifically China, while recognizing that verifying compliance will be extremely difficult. He also wants to maintain the U.S. and its allies' lead by restricting the sale of advanced AI chips to China and cracking down on unauthorized distillation, where companies use another model's outputs to help train their own.

I saw dozens of posts calling this a psyop. A few people DM'd me asking why he looked “shaky” in his Anderson Cooper interview. Put all of that aside and think about the content of his words, the source and his data behind it, and his biases or incentives.

Remember: he can actually believe this AND be incentivized to say it. Having a business incentive to say something does not automatically make it wrong. It also doesn't make it right.

***My POV:*** *the labs see things we don't, and often 6 months ahead. Recursive self-improvement has been a concern for years, prior to ChatGPT. I don't expect China to go along unless it sees a clear benefit to its own security, including reducing shared risks. Public panic is not helpful without a plan. Our government has a lot of catching up to do on how this technology works. Powerful AI in the hands of few can exacerbate the wealth and capability gaps. A select few deciding who gets access to powerful AI might be equally dangerous. This likely slows down enterprise adoption because people will be more resistant and hesitant (assuming AI is not embedding itself). And more people should build METR-like organizations.*

Read the full essay: [We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier).