---
type: Web
authors: null
url: 'https://research.mysociety.org/html/ai-framework/plain.html'
published: null
created: 2026-03-25T00:00:00.000Z
tags:
  - strategia-AI
  - organizacje-społeczne
  - narzędzia-AI
---


## About mySociety

[mySociety](https://www.mysociety.org/) is a registered charity pioneering the use of online technologies to empower people to take their first steps towards greater civic participation. We enable people across the UK to become changemakers by providing technology, research and data, openly and for free.

We run services such as TheyWorkForYou, WhatDoTheyKnow, WriteToThem and FixMyStreet, and are established leaders in the UK (and global) civic tech space - running the global [TICTeC](https://tictec.mysociety.org/) Conference.

Our mission is to use our digital and data skills to put more power in more people's hands so that together we can build a fairer, safer future.

We use digital technology, research and data to:

- understand what citizens want and need in order to participate in democracy
- deliver impactful digital services to citizens and civil society to meet those needs
- demonstrate institutional barriers and provoke better institutional response

We want to evolve old ways of making decisions together, and build new ones in the service of a democracy fit for the 21st century.

## What is this document

This is a working document of issues to consider when considering deploying Generative AI or Machine Learning (GAML) as part of a mySociety output or service.

This is meant as a way of thinking through what we're doing internally, but also being part of wider public conversations about uses of this emerging technology.

We expect firmer principles to emerge over time, but this document reflects the kind of questions we want to ask ourselves as we explore how new technology can fit into our existing mission and practice.

## Key principles

We should use AI solutions when they are the best way of solving problems, are compatible with our wider ethical principles and reputation, and can be sustainably integrated into our work.

This leads to questions and considerations in six domains:

- **Practical** – does it solve a real problem for us or our users?
- **Societal** – does it plausibly result in the kind of social change we want, and have we mitigated change we don't want?
- **Legal/ethical** – does our use of the tools match up to our wider standards and obligations?
- **Reputational** – does using this harm how others view us or our services?
- **Infrastructural** – have we properly considered the costs and benefits over time?
- **Environmental** – have we specifically accounted for environmental costs?

Each section has a set of questions to answer to aid in consideration of the issue. This is not a checklist where you always have to answer yes to every question - but where answering them helps build up a picture for considered and deliberate use of powerful but emerging technology.

## Practical questions

We need to make sure we're not working back from the solution to the problem. Even where we do work back from a workable solution to a valid problem, working forward again may reveal simpler and more sustainable approaches.

This is complicated because there is a certain amount of money and support available for "what does this new solution solve?" – but failing to solve real problems while picking up long term maintenance issues is a possible result of not thinking things through early.

We also need to be clear on how the inherent features of models might work for and against a problem (e.g. text summarisation might be accurate and shorter, but training data biases might lead to ‘incorrect' weighting on what was important, or terms we wouldn't use) – and have processes of assessing acceptable performance.

---

*Questions to answer*

- Is this solving a problem that exists and should be a priority for us and our users?
- Does GAML practically solve the problem to a standard acceptable for our work?
- Is this the best way of solving the problem?

---

## Legal/ethical questions

Before we even get to big integrations with services – AI tools are already available (and in use) in our tool chain. There are practical reasons to distinguish between this kind of use and deeper integration – but it is the same legal/ethical issue.

The main question about generative AI and related LLMs is: are these just doing complicated intellectual property laundering? It's not exactly the same as blockchain – it's a functional product that can solve problems. But so was Napster. Just because something solves a problem doesn't mean there are no questions about how we use it.

Large Language Models and image generators push the idea of copyright to its breaking point. The idea that copyrighted material can be fuzzily accessed for search and research is much more of a problem when that model turns around and is breaking the industry that produces the copyright material.

This isn't just about our feelings, but where these issues cross over into legal uncertainty. As [the New York Times vs Open AI lawsuit](https://nytco-assets.nytimes.com/2023/12/NYT_Complaint_Dec2023.pdf) puts it, it's an argument between a business model based on "Almost Two Centuries of High-Quality, Original, Independent News" and "A Business Model Based on Mass Copyright Infringement". What risk do we run through heavy integration with young businesses (even ones backed by Microsoft)under substantial legal challenge?

There are ways of creating language models on only public domain [<sup>1</sup>](https://research.mysociety.org/html/ai-framework/plain.html#footnote-1) or explicitly licensed data – but the current state of the art is not that. If we think that this is a requirement for ethical use, how does that affect our approach in the short term?

Are compromise approaches enough? Github Copilot has options to restrict output that matches too closely to known licenced data in the source material, meaning that—for cases like autocompletion of code already in a project, or filling in one liners—the licensing status feels defensible. But the model is still trained on all the data and gains value from it – even if it is blocked from directly replicating it.

We don't have to (but may) come to hard stances. But thinking about the options and how these relate to practical ability to deploy tools helps build our understanding and approach.

---

*Questions to answer*

- What is the nature of the tool and organisation that produces it?
- Is the model open source/open weights and is the training data available?
- What is the training data?

---

## Societal questions

At mySociety there is an extent to which our goal is societal change – we think technology is a connector and lever that can be used to make things better. But we also want this change to be intentional, to have been thought through, and be comfortable with the likely consequence of the change. More generally, these tools exist and are being used in governments and other organisations we want to encourage to use technology responsibly. We also want to model what we think is good and responsible behaviour around integration of AI – especially the effective use of technology in decision-making and governance.

When planning out how we use technology, we want to do so purposefully. We may choose to be deliberately disruptive anyway, but we want that to be considered.

---

*Questions to answer*

- Is this a use that would reasonably have a notable effect on either society or the specific ecosystem this service works in? What are the best and worst cases?
- Is this shift consistent with our strategy and ethical framework? Do we have a clear idea of our desired end state when making this decision?
- Is there paired ideas or work that help manage transition towards our preferred end state?

---

## Reputational questions

We can be satisfied that something is practically useful, and ethically acceptable – but suffer reputation harm if others do not agree, or have different thresholds for acceptable error.

For instance, if there is an image generator trained on licensed images it passes the basic test of there being some payment to original artists in the process and is formally copyright-safe. But if we were personally satisfied this was enough and started to use this for report covers and blog posts, would others feel the same? Will all AI image approaches be tarred with the same brush? Or more practically, recognised as having the same end impact: a transfer of viable work for artists to subscription fees to large tech companies.

In the same way, we're seeing other projects race ahead with automatic summaries of Parliamentary transcripts. Will there be a reputational advantage to "No AI used in this website"? [‘Slop'](https://simonwillison.net/2024/May/8/slop/) is starting to take off as a term for AI summaries of dubious usefulness filling previously helpful platforms. We could throw away hard earned reputation by getting this wrong.

The [BBC's guidance](https://www.bbc.co.uk/editorialguidelines/guidance/use-of-artificial-intelligence) reflects that for public facing organisations this is a key consideration, saying that AI use should:

- never undermine the trust of audiences.
- always be transparent and accountable with effective and informed human oversight.
- always be used in a manner consistent with BBC editorial values, in particular of accuracy, impartiality, fairness and privacy.

This affects both the opinion of the people who currently use and trust our services, but also might provide new attack lines to our critics.

In principle, we could integrate machine learning approaches as either a replacement or supplement to volunteers on crowdsourcing projects. There are conceivably ways of doing so where humans are always in the loop, or where AI is confined to error checking – avoiding the auto-pilot problem where humans do not build up the skill to recognise AI sourced error. But does any use of AI in the process give a new attack that undermines the work? For instance, we could get a push back of *"TheyWorkForYou has used inaccurate AI technology to create a misleading and contextless version of my financial interests"*, or *"analysis of our council's climate action is based on AI with known problems and bias - it does not give an accurate or nuanced understanding of the work we've undertaken"*.

It is impossible to be so clean that bad actors can't try and spin out of it. But we need to be careful when connecting the trust our work has with a new technology that has legitimate wider trust problems.

---

*Questions to answer*

- Does the tool touch on an area where a high level of accuracy or trust is required? Can we communicate well how the tool helps us deliver that?
- Does the tool touch on a controversial use of AI? Are there reputational risks in its use?
- Does the tool create the potential for bad faith attacks on our services? Are proportional ways to address this possible?

---

## Infrastructural questions

mySociety has had a lot of impact through the approach of applying relatively mature technology approaches in interesting ways to societal problems. This informs how we adapt and advance our technical approach. We want to have clear eyes on the problems we want to solve rather than the tools we want to use.

Here the concern isn't that AI is a fad, but that it's not stable enough yet. On our charitable projects, funding can have big peaks but long troughs where maintenance is underfunded. If we are too experimental during the good times, we can run into problems during periods without funding to react to problems. If these tools are useful, they'll still be there and more mature in a few years.

Running different kinds of machine learning models on our infrastructure can create new requirements. Smaller models don't *need* GPUs, but it helps for speed and they'll generally be memory intensive. Using external APIs reduces our infrastructure requirements, but raises costs in other ways, such as making us and our reusers dependent on specific companies. This is especially problematic for any service with a strong real-time component. Asynchronous processes (for instance a nightly categorization of WhatDoTheyKnow requests, or the [CAPE approach of precalculating comparisons](https://www.mysociety.org/2023/07/19/machine-learning-can-make-climate-action-plans-more-explorable/)) can be more flexible. But some approaches only work with real-time feedback (e.g. drafting an FOI request).

While in principle, open source GPT-equivalent-ish models that can be deployed on owned infrastructure are viable, they require GPUs to run effectively. This may simplify over time, but it is always going to be likely that the near cutting-edge open source models have higher requirements than our current infrastructure.

As some of this problem relates to sustainability of funding, there's a slightly different angle for commercial services which, if priced appropriately, can support this. E.g. "WhatDoTheyKnow Pro helps thousands of paying users draft and review requests!" is more sustainable than making that available to all users. But commercial services also come with high uptime requirements.

As with the rest of our infrastructure, aligning charitable and commercial infrastructure needs gives more robustness to our charitable services than would otherwise be the case. Where skillsets are mostly supported by ongoing commercial projects, long running maintenance of other services is more practical.

---

*Questions to answer*

- What are the long term costs of deploying this tool? Are there more sustainable alternatives?
- Do we have the skills needed to sufficiently deploy and manage this tool?
- Are there efficiencies with other tools in use in the organisation? (shared skills or common infrastructure)

---

## Environmental questions

Related to infrastructure considerations – we are now tracking the carbon footprint of our infrastructure.

Generative AI systems are [more power intensive](https://arxiv.org/pdf/2311.16863.pdf) than traditional code processing (and more specialised machine learning models). Their one-shot generalist nature means they are highly adaptable to many tasks, but also this creates new overheads in terms of processor requirements, and energy usage.

Models use resources in both their training, and in answering requests. A model trained once may be efficiently reused many times, but in principle commercial AI companies have continuous training and improvement in its models – making this a running cost.

On an individual request, usage is not massive compared to other costs. But at scale, growth of AI models poses new power requirements and environmental challenges. External APIs may be more efficient than adding to our server infrastructure if it's going to be underused – but at scale this new demand creates a need for additional power.

Significant use of AI needn't necessarily mean high emissions. Microsoft Azure (OpenAI's infrastructure) has a goal of 100% renewable energy by 2025 (note that this isn't "we've done this already"). If we were building tools dependent on millions of requests a year, we would want to understand not only the compute cost, but the current environmental impact of that.

---

*Questions to answer*

- Does this generate an ongoing environmental impact that should be tracked as part of our environmental tracking?
- Are there other providers with lower impact?
- Are there more efficient ways of achieving an equivalent result?

---

## Maintenance

The [Google Docs version](https://mysociety.org/aiframeworkcomments) of this document is open for public comments (if people are nice). To republish the web version use the instructions in the [stringprint repo](https://github.com/mysociety/stringprint_document_source) with the slug ‘ai-framework'.

Header image: Photo by [Eric Krull](https://unsplash.com/@ekrull?utm_content=creditCopyText&amp;amp;utm_medium=referral&amp;amp;utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/blue-and-purple-robot-toy-Ejcuhcdfwrs?utm_content=creditCopyText&amp;amp;utm_medium=referral&amp;amp;utm_source=unsplash)
