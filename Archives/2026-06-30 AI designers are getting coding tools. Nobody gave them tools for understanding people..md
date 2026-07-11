---
type: "Web"
authors: "[[Kasia Szczesna]]"
url: "https://behavioralinsight.substack.com/p/ai-designers-are-getting-coding-tools?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-06-30
created: 2026-07-11
tags:
  - "narzędzia-AI"
  - "strategia-AI"
  - "trendy-AI"
---


When a product team ships a new AI feature, the questions that come up in the room are almost always technical: is the model good enough, are the responses fast, does the backend integration hold up. Questions about whether the user actually understands what the AI just did, whether its behavior builds trust or triggers anxiety, what happens when it makes a mistake.Those rarely make it onto the agenda. Not because nobody values them, but because there’s no ready language or tooling to answer them.

---

## A problem everyone has, but few name out loud

Design systems have matured over the past two decades. We have tokens, components, libraries, Figma kits and processes that help maintain visual consistency across screens and products. But AI is not just another interface component — it makes decisions, makes mistakes, changes state without explicit user action and personalizes experiences in ways that can surprise even the people who built the system. No existing design system addresses this.

Think of it like the difference between designing a road and designing an intersection with adaptive traffic signals controlled by an algorithm the driver can’t see. We know perfectly well how to design roads. We have standards, materials, proven solutions. But when the road starts deciding on its own when to let a car through and when to stop traffic, we need a completely different set of questions to evaluate whether the design is good. Not “is the asphalt quality sufficient,” but “does the driver understand why they’re stopped and how long they’ll wait.” Design systems solved the first kind of question. BehaviorAI Pattern Library addresses the second.

The result is that teams design AI behavior from scratch on every project. One designer solves the problem of communicating an AI error during onboarding, three months later another team in the same organization faces exactly the same challenge and arrives at a completely different solution. The consequence isn’t just inconsistency. It’s fundamentally a problem of trust, adoption, and increasingly, regulatory compliance.

---

## What BehaviorAI Pattern Library provides

BehaviorAI Pattern Library is a design pattern library organized around behavioral moments, not interface categories. This shifts the starting point: instead of asking “how do I design an AI loading state,” we ask at which moment the user first loses confidence in the system’s behavior and what they need at that point to rebuild it.

This distinction has practical consequences for how designers work. When a design review raises the question “what should the error screen look like,” the answer depends on where this error falls in the interaction sequence, what the user was trying to accomplish, what stage of trust-building with the system they’re at in that moment, and whether the error undermines their previous understanding of how the system works. These are behavioral questions, not visual ones, and the library provides structured answers to them instead of forcing every team to work them out from scratch during a session.

The library covers patterns across seven areas:

- **Onboarding** — how to guide users through their first encounter with AI without losing them in the early days
- **Transparency** — how to communicate AI behavior without drowning users in technical jargon that means nothing to them
- **AI States** — active, processing, error, and uncertainty states, and how to design system behavior across each of them
- **Feedback & Correction** — how to design the correction loop so users actually want to engage with it rather than route around it
- **Personalization** — when adaptation strengthens trust and when it triggers the uncanny valley effect, the feeling that the system knows too much
- **Dark Patterns** — a catalog of patterns to avoid, based on the current taxonomy (Shi et al. 2026)
- **Conversation & Chat UI** — designing conversational interaction beyond the chatbot, in the spaces where the line between UI and dialogue blurs

Each pattern describes the context of use, the behavioral signal, the user’s decision moment, and the recommended design solution with a reference to the psychological mechanisms that drive it.

---

## Use case: onboarding in a B2B product with AI

A team builds a data analysis tool with a built-in AI assistant. The model is solid, the onboarding is short and clear, and the first user tests go without significant issues. Three weeks after launch, the data shows that 60% of users never came back to the AI feature after the first week. In the retro, someone asks the question every product manager knows: “what went wrong if the tests went well?”

This is a classic example of the **AI Invisibility Effect**: the AI works, but users don’t know when, why, or whether they should trust it, so the easiest thing to do is simply avoid it. The problem wasn’t visible in tests because tests measure whether the user can complete a task, not whether they trust the system enough to come back the next day without a moderator sitting next to them. These are different questions and they require different design patterns.

BehaviorAI Pattern Library gives the designer concrete answers about which visual and contextual signals build a user’s sense of agency when facing an autonomous system and which micro-moments during onboarding are critical for building trust versus quietly undermining it. These aren’t answers derived from general principles every time from scratch. They’re patterns collected, described and categorized, ready to apply before production data tells you something went wrong.

---

## Who it’s for and how it works in practice

The library is a working tool, not an encyclopedia. A design manager comes in with a specific problem on the agenda — *“we have a sprint review in two days and we can’t agree on how to handle the situation when AI doesn’t have enough confidence to give a recommendation”* and leaves with a pattern, a rationale, and a list of pitfalls to avoid, rather than another hour of discussion with no resolution.

For organizations implementing the AI Act, the library also serves as a first line of defense against unknowingly designing manipulative patterns, dozens of which are now covered by regulation. The difference between a pattern library and a compliance checklist is that the library works at the design stage, not the audit stage. It lets you avoid building things you’ll have to rebuild later.

If you design AI-powered products and want to stop solving the same problems from scratch every time - the library is for you.

---

*Kasia Szczesna — founder of BehaviorAI. She builds tools and frameworks at the intersection of behavioral science, design, and AI ethics. [behaviorai.eu](https://behaviorai.eu/) | [kasiaszczesna.pl](https://kasiaszczesna.pl/)*