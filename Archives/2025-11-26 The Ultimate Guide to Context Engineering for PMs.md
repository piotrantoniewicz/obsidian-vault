---
type: Web
authors: "[[Aakash Gupta]]"
url: https://www.news.aakashg.com/p/context-engineering?utm_source=perplexity
published: 2025-11-26T00:00:00.000Z
created: 2026-03-03T00:00:00.000Z
tags:
  - prompt-engineering
  - LLM
  - narzędzia-AI
---


### All the frameworks, prompts, and checklists you need to master context engineering - from an OpenAI Product Leader

AI product building is a rich man and a poor man’s game.

*On the rich man’s side…*

The chips have never been more powerful, the models have never been more capable, and the barrier to building AI features has never been lower.

*On the poor man’s side…*

Most AI features shipped today **still behave like interns.** Let’s be honest. They’re good in certain use cases. But they need hand holding. And they’re inconsistent.

*Why?*

The answer is rarely “model quality.” It is almost always **context quality**.

*That’s why “context engineering” sounds like an engineering topic, but it is one of **the most important disciplines for [AI PMs](https://aakashgupta.medium.com/the-300k-ai-pm-roadmap-every-skill-you-need-to-master-the-fastest-growing-pm-role-4c6d20eaea86)**.*

---

## World-Class AI leaders Agree

Here’s Tobi Lutke, CEO of Shopify:

![](https://substackcdn.com/image/fetch/$s_!AU0b!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdac2487e-ad57-4d0e-a8ce-0c87042947bb_1176x552.png)

And Andrej Karpathy, OpenAI Co-Founder and former head of Tesla Autopilot:

![](https://substackcdn.com/image/fetch/$s_!Ljf-!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31f26de5-2035-4cca-a1df-b4ab93ff94b6_1176x764.png)

They both are echoing the importance of this skill. So I expected to find lots of great content out there.

Surprisingly, a *ll the other content I found was geared to AI engineers, not AI PMs.*

So I wanted to create the **ultimate guide for PMs**.

---

## Introducing Miqdad Jaffer

*To make sure I deliver, I’ve partnered with a true leader in AI - Miqdad Jaffer, a Product Leader at OpenAI.*

![](https://substackcdn.com/image/fetch/$s_!4o9x!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8598e9b7-6901-4db1-ab73-85a5d83b8bff_1052x490.png)

*Miqdad teaches an awesome [6-week cohort course, the AI PM Certification.](https://maven.com/product-faculty/ai-product-management-certification?promoCode=AAKASH550C7) Get $550 off his course using my code AAKASH550C7. The next cohort starts January 26th.*

---

## Today’s Post

*In my [last podcast episode](https://www.youtube.com/watch?v=jxxD3tVJm0o), I showed you that context engineering can take you to $10M ARR in 60 days. In today’s episode, Miqdad and I break down how to do it yourself:*

![](https://substackcdn.com/image/fetch/$s_!b6Kd!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7966508b-2a44-4d72-aa77-cd19d54830e0_1200x800.png)

1. Why Does Context Engineering Matter?
2. The PM’s Role in Context Engineering
3. The 6 Layers of Context to Include
4. Common Mistakes
5. How to Engineer Context Step-by-Step
6. How to Spec out Features Appropriately
7. Checklists, templates + prompts you can steal

---

## 1\. What is Context Engineering, and Why Does it Matter?

#### Defining Context Engineering

We like Andrej’s definition from above. Context engineering is:

> *The delicate art and science of filling the context window with just the right information for the next step.*

If prompt engineering is the instruction sheet, context engineering is the **entire world the model sees**.

As Ilya Sutskever (another OpenAI founder) highlighted in the [recent Dwarkesh podcast](https://www.youtube.com/watch?v=aR20FWCCjAs), the big difference between humans and LLMs is **LLMs do not infer context magically**. They do not automatically know:

- who the user is
- what the user did 5 seconds ago
- which document is relevant
- what the system knows about the user
- what rules the business must follow
- what data is allowed to be used
- what happened in previous sessions
- whether the user is a beginner or an expert
- which constraints must be met
- which entities exist in the user’s workspace
- how everything relates to everything else

That’s *what we’re going to put in* with context engineering.

#### Why Context Engineering Matters

Everyone wants to talk about model selection and [prompts](https://www.news.aakashg.com/p/prompt-engineering).

![](https://substackcdn.com/image/fetch/$s_!hVmx!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F868c875b-904e-4c27-9a86-ea2758ca72be_984x1066.png)

You can switch from GPT-5.1 to Gemini 3. But, if the system:

- doesn’t know what file the user is working on
- doesn’t see the user’s preferences,
- isn’t aware of the entities or relationships in the workspace,
- cannot recognize the user’s role,
- retrieves irrelevant documents,
- or misses crucial logs…

Then you’re SOL (shit outta luck).

Here’s 2 real life examples:

**Example 1: AI Email Assistants**

When we were [building](https://www.news.aakashg.com/i/160800379/principle-design-for-human-ai-collaboration) Apollo’s email writer, Aakash learned that when the model sees:

We only gave it the last message → output was generic  
We gave it the entire thread → output became coherent  
We gave it the thread + CRM notes → output became personalized  
We gave it thread + CRM + company tone-of-voice → output became brand aligned  
We gave it thread + CRM + tone + relationship context → the ***output became shippable***

It encoded the importance of context engineering in my mind.

**Example 2: AI Coding Assistants**

Let’s take another example. Do a thought exercise: *How has [Cursor](https://www.news.aakashg.com/p/how-cursor-grows) managed to not get replaced with Anthropic and hit $1B ARR?*

— WAIT FOR IT —

— DON’T READ AHEAD TILL YOU THINK ABOUT IT —

Our answer?

When you open a project in [Cursor](https://www.news.aakashg.com/p/how-cursor-grows), it indexes your codebase by computing embeddings for each file, splitting code into semantically meaningful chunks based on the AST structure.

When you ask a question, it converts your query into embeddings, searches a vector database, retrieves the relevant file paths and line numbers, then adds that content to the LLM context.

This is why Cursor lets you choose between models from OpenAI, Anthropic, Gemini, and xAI. The model is almost modular. **The context layer is the moat**.

Google tried to buy Cursor instead of compete. When that failed, they spent $2.4B on [Windsurf](https://www.youtube.com/watch?v=oLmHdymHHg0&embeds_referring_euri=https%3A%2F%2Fwww.news.aakashg.com%2F), the #2 player.

That’s a signal that context engineering **creates defensibility** that *model capability alone cannot replicate*.

![](https://substackcdn.com/image/fetch/$s_!32nv!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72eff0b3-b373-48ed-8304-186c643beeb4_892x1056.png)

*So now that you understand why context engineering is your moat, we’re going to give you **every tactical tool to do it well**: frameworks and canvases to use as a PM + real life checklists, templates & prompts you can steal. It’s easily the deepest guide for AI PMs on the web.*

---

## 2\. The PM’s Role in Context Engineering

Most teams assume context engineering is an engineering problem.

It is not.
