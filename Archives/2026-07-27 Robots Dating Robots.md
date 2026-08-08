---
type: "Web"
authors: "[[Kevin Barenblat]]"
url: "https://aiforhumanity.ffwd.org/p/robots-dating-robots?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-07-27
created: 2026-08-02
tags:
  - "fundraising"
  - "strategia-AI"
  - "prompt-engineering"
---


I’ve seen a lot of good AI tools, many of which I’ve highlighted in this newsletter over the years. I’ve also seen a lot of bad AI tools ([AI moonwalkers](https://shiftrobotics.io/products/moonwalkers?srsltid=AfmBOorLlNGpExvphacIpc8riQ787JNiWKnerDLXHsnQKbQuig4Xt-A5), I will never let you live this down). I’d like to think our recent releases, the [AI Proposal Assessment Tool](https://www.ffwd.org/ai-proposal-assessment) and [AI Grant Writing Coach](https://www.ffwd.org/ai-grant-writing-coach), land closer to the former. There’s nothing fancy technically under the hood, but what is really interesting is everything we learned and decided while building them.

In this issue, I invited a special guest, Fast Forward’s AI advisor Scott J. Kleper, to share what we learned and the principles that guided us along the way.

---

In the 2023 movie *Robots*, two people try to scam each other by sending robot clones of themselves on dates. At least, that’s what we think it’s about; nobody at Fast Forward has seen this film. However, the premise (which we’re pretty sure we got right) makes us fearful of a world where AI is writing nonprofit funding proposals and another AI is judging the proposals. As the AI judges improve, the AI proposal writers soon learn to write proposals that rate higher. Everybody pretends that humans are doing both the reading and the writing, but it’s just robots going on dates with other robots.

When we set out to create a [library of prompts](https://www.ffwd.org/ai-proposal-assessment) to help funders evaluate proposals, we wanted to avoid a Robots Dating Robots scenario. Our goal was to create prompts that would provide *guidance* from AI, not a *decision*. Our process for doing so was itself an exercise in using AI as a guide.

### Agree to Disagree

Our [AI Proposal Assessment Tool](https://www.ffwd.org/ai-proposal-assessment) is meant to work with whichever AI tool a funder prefers. Initially, our goal was *agreement* among AI models. In other words, we wanted to make sure that our prompts would give you the same result whether you were using Claude, Gemini, ChatGPT, or a model you purchased from your local AI superstore. After all, how could we claim that our prompts were useful in assessing proposals if the robots didn’t agree with each other?

Version 0 of our Assessment Tool provided prompts that looked at 18 different aspects of a tech nonprofit funding proposal based on the questions listed in [The Philanthropist’s Guide to Nonprofit AI Investments](https://www.ffwd.org/blog/philanthropists-guide-to-nonprofit-ai-investments). The aspects ranged from appropriate resourcing to ethical considerations. We asked the AI to determine which areas were adequately addressed, which seemed lacking, and which weren’t addressed at all. We were very clear that the AI shouldn’t make a decision on whether or not to fund the proposal, but rather to point out areas of concern to probe. We tested our prompts using a custom skill that would provide us with reports like this:

![](https://substackcdn.com/image/fetch/$s_!xqOr!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79855e18-7418-4318-9dcb-96ddff11ff20_2048x926.png)

Our early testing revealed the folly of this approach. We sent sample proposals to different LLMs along with our prompts. We expected that the responses would mostly be in agreement among the different AI models, but they were not. The results led to frustrating conversations like this:

> *Me: You said that based on the proposal, the nonprofit did NOT have adequate technical resources to implement what they were proposing, but another AI we used said it did.*
> 
> *AI: You’re right! The nonprofit DOES have adequate technical resources.*
> 
> *Me: Then why did you say that it didn’t?*
> 
> *AI: The technical resources they have are contractors, so a strict interpretation of the question would highlight the fact that they do not currently have adequate technical resources on staff.*
> 
> *Me: Okay, so they don’t?*
> 
> *AI: That’s correct.*
> 
> *Me: Arrrgggggg!*

Over and over, we’d find that two models disagreed on their *judgment* of a proposal in the “Status” section, but both applied sound reasoning and brought up important issues in the “Notes” section. The focus on getting a clear “yes” or “no” answer was wasted time when every LLM could easily argue both sides. Disagreement is a bug if you’re asking for a verdict, but a feature if you’re asking for coverage.

### Nudge, Don’t Judge

As we dug into the reasoning that the different models were using to make their determinations, we found *the thought process* *was* *much more compelling than the answers themselves.* Determining whether a nonprofit has adequate technical resources might be useful to a potential funder, but it’s subjective. In contrast, surfacing the use of external contractors as a potential issue is much more actionable. A “red/yellow/green” style of output proved less helpful than gentle nudges of questions to ask and areas to discuss.

In keeping with the latest in AI fads, we ran our prompts in a loop, repeatedly running them with a set of different LLMs and analyzing the output with the following criteria:

1. Are its statements accurate?
2. Does it provide useful, actionable feedback?
3. Does it refrain from making a yes or no determination?

After many times through the refinement loop, our prompts no longer try to make a determination. They encourage a dialogue between the funder and the applicant by suggesting topics to raise. For example, instead of making a determination about whether or not the current team is adequate, the model will say something like:

> *The proposal mentions using external contractors to build the AI features. It may be worth discussing the relationship with the contractors and whether this capability should be developed in-house.*

Raising questions rather than making determinations also fits our strong stance that an AI should not determine the *outcome* of a proposal. We never wanted our tool to tell a funder whether or not to fund a particular nonprofit. We merely wanted a funder to be informed. Getting the AI to come up with a list of questions to ask instead of a grade in each area freed us from a ridiculous pursuit of model consistency while giving funders the framework for a more informative discussion with nonprofits.

### Human Touch

Assuming we don’t want to spend every weekend attending robot weddings, we need to remember that AI works to our greatest advantage when it’s guiding human thinking, not replacing it. Particularly when it comes to decisions that could advance or stifle the critical work that nonprofits are doing, let’s not dismiss the judgment of humans by letting AI make the call.

When developing our new [AI Grant Writing Coach](https://www.ffwd.org/ai-grant-writing-coach), we built upon these learnings. Our prompt development refinement loop has become an internal best practice in creating cross-model prompts that provide guidance without judgment.

*Did we get it right? Try the [AI Proposal Assessment Tool](https://www.ffwd.org/ai-proposal-assessment?_gl=1*ip9vif*_gcl_au*MTYxMjA0ODI0Mi4xNzc4NTE2NTkwLjM3MjE2MDcxMi4xNzg1MTI2MTE3LjE3ODUxMjYxMTcuMTY2MTEwMzk5NS4xNzg1MTI2MTE3LjE3ODUxMjYxMTc.*_ga*MTk1MDA5NjEzOC4xNzc4NTE2NTkx*_ga_GY2NRRGBVN*czE3ODUxNzAwNzUkbzI5JGcxJHQxNzg1MTcwNjA1JGo1MiRsMCRoNzMwNjAwNjI.) and our new [AI Grant Writing Coach](https://www.ffwd.org/ai-grant-writing-coach) and let us know what you think!*