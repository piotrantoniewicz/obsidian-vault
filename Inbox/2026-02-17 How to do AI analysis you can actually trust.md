---
type: "Web"
authors: "[[Caitlin Sullivan]]"
url: "https://www.lennysnewsletter.com/p/how-to-do-ai-analysis-you-can-actually?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-02-17
created: 2026-05-12
tags:
---


*👋 Hey there, I’m Lenny. Each week, I answer reader questions about building product, driving growth, and accelerating your career. For more: [Lenny’s Podcast](https://www.lennysnewsletter.com/podcast) | [Lennybot](https://www.lennybot.com/) | [How I AI](https://www.youtube.com/@howiaipodcast) | My favorite [AI/PM courses](https://maven.com/lenny), [public speaking course](https://ultraspeaking.com/lennyslist?via=lenny), and [interview prep copilot](https://www.benerez.com/copilot/lenny)*

*P.S. Get a full free year of Lovable, Manus, Replit, Gamma, n8n, Canva, ElevenLabs, Amp, Factory, Devin, Bolt, Wispr Flow, Linear, PostHog, Framer, Railway, Granola, Warp, Perplexity, Magic Patterns, Mobbin, ChatPRD, and Stripe Atlas [by becoming an Insider subscriber](https://www.lennysnewsletter.com/subscribe?plan=founding).*

---

The problem with AI is that the output always looks confident—even when it’s full of lies: made-up quotes, false insights, and completely wrong conclusions. As today’s guest author, [Caitlin Sullivan](https://www.linkedin.com/in/caitlindsullivan/), puts it, “ **These mistakes are invisible until a stakeholder asks a question you can’t answer, or a decision falls apart three months later, or you realize the ‘customer evidence’ behind a major investment actually had enormous holes.”**

A user-research veteran, Caitlin has been at the bleeding edge of using AI for user research. She’s trained hundreds of product and research professionals at companies big and small on effective AI-powered customer research and advised teams at companies like Canva and YouTube. **Below, she shares her four most effective techniques for getting real, trustworthy, and actionable user insights out of ChatGPT, Claude, Gemini, or your LLM of choice.** Let’s get into it.

*For more from Caitlin, find her on [LinkedIn](https://www.linkedin.com/in/caitlindsullivan/) and in her new course, [Claude Code for Customer Insights](https://bit.ly/3ZB1jd8).*

*P.S. You can listen to this post in convenient podcast form: [Spotify](https://open.spotify.com/show/0IIunA06qMtrcQLfypTooj) / [Apple](https://podcasts.apple.com/us/podcast/lennys-reads/id1810314693) / [YouTube](https://www.youtube.com/@lennysreads).*

---

![](https://substackcdn.com/image/fetch/$s_!o_Ba!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8cd6012c-6a31-4cc1-962e-35820925743f_1456x970.png)

Everyone’s “analyzing” customer data with AI. But everyone’s also getting answers full of slop: hallucinations, wrong conclusions, and “insights” that just parrot back what you already told it.

Put the same customer conversation transcripts into two models and get a choose-your-own-adventure experience in return. Each model will give you a different narrative, different “evidence,” and wildly different product recommendations, with the same high level of confidence. Below are two real outputs from that experiment. One is misleading. One is trustworthy. Can you tell which is which?

![](https://substackcdn.com/image/fetch/$s_!xmwL!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe002abc-bf87-4b23-9908-7ffd44f62703_1456x550.png)

When they’re side by side, you might spot the problems with the one on the left. But that’s not how this works in practice. You get one output, it reads confidently, and you build your next decision on top of it and never see what’s missing. This is exactly why verification matters.

Here’s what separates these answers: the left output cherry-picks three enthusiastic quotes and leaps to a confident recommendation (“Yes, build a screen”), without questioning whether those quotes represent the full dataset. It looks persuasive, but it’s the AI equivalent of confirmation bias.

The right output does something harder. It challenges the surface-level request (“Do not interpret screen feedback as a single, literal feature request”), segments users by actual need, and flags pricing risk with specific participant timestamps you can verify. It’s messier and doesn’t oversimplify things, but it’s real.

The difference between the two examples above comes down to crucial steps in my workflow to address common failure modes of AI analysis. Those steps force LLMs to maintain the customer’s exact words, dig deep beyond superficial patterns, and catch contradictions in customer stories that will skew final recommendations. Without those checks, false but convincing-looking insights go into a deck and influence a million-dollar decision in the *wrong* direction.

In this post, I’ll show you how to get relevant and verified insights you can trust. You’ll learn about four failure modes that silently break your AI-supported insights:

1. Invented evidence
2. False or generic insights
3. “Signal” that doesn’t guide better decisions
4. Contradictory insights

I’ll also teach you my prompting techniques to prevent and catch these errors before they lead to the wrong final decisions. These tactics work across Claude, ChatGPT, Gemini, and with interviews, surveys, or any qualitative or mixed data you’re trying to make sense of with the help of AI.

### Why AI struggles with customer research data

Before we get into failure modes, you need to understand what’s difficult about this kind of data for AI in the first place. Models fail with interviews and surveys in different ways.

**Interviews are unstructured and messy.**

A 45-minute research interview is a messy, wandering conversation. A participant may contradict themself. They go on tangents. They say something important at minute 8 and reframe it completely at minute 35.

LLMs handle this by imposing structure and jumping to conclusions a bit too fast. They find clean themes immediately, pull quotes that fit them best, produce tidy summaries, and call it a day.

But real analysis requires sitting with the mess, noticing contradictions, weighing tangents, and catching tone shifts. Without explicit guidance, AI flattens all of that into something that *looks* like insight but misses what actually matters.

**Even when surveys look structured, they’re not.**

You’d think a CSV would be easy to parse. Rows and columns—what’s complicated about that? A lot.

A column of 200 responses to “Why did you cancel?” is just as messy as interview data; maybe worse, because you have none of the context. In an interview, you remember that they hesitated, or had just complained about a specific feature. In a survey, you get “It wasn’t for me” and nothing else.

Your CSV may also not be as clean as you think. Different tools export differently. SurveyMonkey might put question text in headers, while Qualtrics exports headers with internal codes. Some exports even include metadata columns—timestamps, internal tags—sitting right next to customer responses, without clear differentiation. If you don’t tell AI which columns contain the customer’s voice and which to ignore, it analyzes everything as signal. I’ve seen AI treat an internal note (“flagged for follow-up”) as something the customer said.

Even “structured” columns hide complexity. A header that says “Q3\_churn probability” tells AI nothing about the scale, the question wording, or whether 5/5 is good or bad.

When analyzing interviews, AI models require help with structure, evidence extraction, and contradiction detection. With surveys, they require help with interpretation, column disambiguation, and understanding what sparse responses actually mean.

The four failure modes below hit both data types and anything similar. Fixing these will typically 10x both the reliability and relevance of your AI analysis results.

## What each LLM is best used for

Not all LLMs are equal for analysis work. I’ve run the same analysis process across Claude, ChatGPT, and Gemini over 100 times and worked with discovery tool product teams like Maze testing prompts across models to see what delivers.

Here’s what you need to know about each model:

**Claude:** Best for thorough analysis with depth and nuance. Delivers more quotes and covers more ground with less pushing. The tradeoff: it gives you the whole brain dump, so themes aren’t always “proven”—you get breadth, not just the safe patterns.

**Gemini (and NotebookLM):** Best for highly evidenced themes and now video analysis. Gives you fewer themes but with stronger grounding. Expect to prompt multiple times to get completeness, and to ask for longer quotes. Unique advantage: it can analyze non-verbal behaviors in video, which the others can’t (yet).

**ChatGPT:** Best for final framing and stakeholder communication. Most creative of the three—including with “verbatim quotes,” unfortunately. Least reliable for real evidence (combines quotes), but excels at packaging relevant findings for a specific audience.

Let me show you what I mean:

![](https://substackcdn.com/image/fetch/$s_!TDI0!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12cb6ecf-5611-47cf-96f6-98a48b704443_1456x502.png)

Want to see the transcript used in this example? Click here.

Unless I give these models more instruction, there are meaningful differences in output. There’s theme overlap, but ChatGPT misses the user’s value/price sensitivity reaction, and all three models give different confidence scores and quotes—some verbatim, some summarized.

This becomes obvious when we can see all three side by side, but most teams have one LLM enterprise account and won’t see the shortcomings of the one they use. ChatGPT summarizes and mashes together verbatim quotes, Claude is more conservative with confidence scores, and Gemini often chooses too-short snippets of customer voice.

**My recommendation:** If you have a choice, use Claude for analysis work. It covers more ground while staying rooted in the actual data. You get depth and breadth without as much pushing. The tradeoff is that it doesn’t filter for you. You’ll often get validated patterns and half-formed hypotheses presented on equal ground, and you’ll need to verify that themes are well-evidenced. But that’s a better starting point than having to prompt three times before being sure your analysis partner hasn’t missed something.

**A note on examples:** For consistency, the examples throughout this post typically use ChatGPT. It’s still the most widely used model among my client teams and students, and it’s also the most prone to the specific failure modes I’m covering. The fixes work and improve results across all three models.

## Four ways AI data analyses lie to you, and how to fix them

After more than 2,000 hours of testing customer discovery workflows with AI, I’ve found that there are four distinct failure modes for AI analysis—and reliable fixes for each one that consistently work across platforms, data types, models, and workflows.

### Failure mode #1: Invented evidence

#### What the problem looks like

Despite massive improvements across most reasoning models, hallucinations are still abundant. When I look over the shoulders of product people running analysis, I see two hallucination types all the time:

- Completely fictionalized quotes (still happens among all three major LLMs)
- Frankenstein quotes sewn together from multiple sources that somewhat represent what the user was saying... but isn’t actually their words (particularly common in ChatGPT)

Both types go unnoticed unless you’re checking every quote manually, but both are often caused by *the way you prompt*. You can pretty easily and accidentally trigger ChatGPT to combine multiple customer quotes in ways that can harm our understanding of what the customer was saying. When you add phrases like “max. 100 words” or “for each theme, give a punchy and representative quote that captures it (≤12 words),” you’ll almost always get mash-ups. Highlights in the example below are combinations like this, not the customer’s exact real words.

![](https://substackcdn.com/image/fetch/$s_!z79y!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb4c6aa2-2fd6-40bf-b0ea-7fd5a7e0ab64_1600x770.png)

#### Why this happens

LLMs don’t retrieve quotes like a search engine; they generate text that’s statistically likely given the context. Generation and retrieval are fundamentally different. The model predicts what a quote should look like. If the context is about phone-checking frustration, it generates plausible phone-checking-frustration language. Sometimes that matches the original, sometimes it’s a near-miss, and sometimes it’s fabricated.

“Verbatim” is also an ambiguous word to prompt a model with. Exact characters? Can punctuation differ? What about filler words? Where does the quote start and end? The model fills these gaps with assumptions you never see. Even participant IDs and timestamps can be faked. A citation like “\[P03, 14:30\]” looks authoritative but means nothing if the quote is invented.

#### The fix: Quote selection rules + verification

The solution to this problem, no matter your model, data type, or workflow, has two parts. First, define what a valid quote actually looks like—your quote “rules”—which removes the ambiguity that lets AI fill in gaps. And then verify that quotes in the resulting AI analysis actually exist before you allow the model to use them.

**1\. Define your quote “rules”**

Add this to your analysis prompt:

> `QUOTE SELECTION RULES`
> 
> - `Start where the thought begins, and continue until fully expressed`
> - `Include reasoning, not just conclusions`
> - `Keep hedges and qualifiers — they signal uncertainty`
> - `Include emotional language when present`
> - `Cite with participant ID and approximate timestamp [P02 ~14:30]`
> - `Do not combine statements from different parts of the interview`
> - `If a quote would exceed 3 sentences, break it into separate quotes`

This removes ambiguity. The model now knows what “verbatim” means *to you*: where to start, where to stop, what to include, what not to combine.

I always encourage client teams and course participants to think critically about what makes a quote “good” to them. You’ll likely get much better results right away with my prompt snippet (it’s my favorite copy-paste inclusion) but even better results if you add your own definitions.

**2\. Verify before you use**

After your initial analysis, use this verification prompt to have the LLM confirm that these are real quotes:

> `QUOTE VERIFICATION`
> 
> `For each quote in the analysis above:`
> 
> 1. `Confirm the quote exists verbatim in the source transcript`
> 2. `If the quote is a close paraphrase but not exact, flag it and provide the actual wording`
> 3. `If the quote cannot be located, mark as NOT FOUND`
> 
> `Output format:`
> 
> - `Quote: [the quote]`
> - `Status: VERIFIED / PARAPHRASE / NOT FOUND`
> - `If paraphrase: Actual wording: [what they said]`
> - `Location: [Participant ID, timestamp, or line number]`

Here’s what happens when you run that:

![](https://substackcdn.com/image/fetch/$s_!J6mn!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F949bc484-15cc-4ea6-bb72-82451b0271d7_1600x1266.png)

A majority of the quotes in the previous ChatGPT output were paraphrased, not original verbatim customer statements. This happened with a request for a small set of quotes, so imagine what happens when you’re digging through 20 interviews and getting just as many patterns back.

Without verification, “quotes” like these end up in your deck attributed to a real participant. Sometimes it’s no big deal. Other times, it’s the difference between product language that strongly resonates and messaging that doesn’t convert.

This often takes just an extra five minutes, depending on how much data you’re dealing with. But it catches errors that would otherwise undermine the evidence behind your product decisions.

### Failure mode #2: False or generic insights

#### What the problem looks like

AI finds themes that are too broad and generic to act on, or biased by what you accidentally primed it with. In interviews, you get themes that could describe any product in your category. I hear this constantly from PMs: “The AI analysis just told me what I already know” or “These insights are too generic. I can’t do anything with them.”

They get outputs like:

- “Price is a factor in decisions”
- “People value reliability”
- “Users want more real-time information”

True, probably, but useless for tough decisions—we need to get deeper than that. These themes could come from so many studies out there. Since I’m working with my fake Whoop data here, they could also easily come from any wearables study.

Themes like these don’t tell you whether *your* users want *this* new feature you’re exploring enough to justify the investment, or whether adding it would alienate the customers who chose you specifically because you’re different.

#### Why this happens

AI defaults to finding *consensus*, because LLMs are pattern-finding machines. They surface the (obvious) patterns that easily rise to the top, finding what multiple participants mentioned, and then they generate a pattern-matched theme.

The truly most important insight might be something only a few people said in this particular batch of interviews but that, if shared by more customers, would be a noteworthy business signal. Or the most important insight might even be the tension between what people say they want and what their behavior suggests.

LLMs also bring priors from training. If the model has seen thousands of churn analyses where price is the #1 theme, it will weight toward price even if your full dataset doesn’t support it.

In surveys, that tendency to superficially pattern-match is even worse. When someone writes “It’s not for me” when cancelling, AI has to guess what that means. Without guidance, it’ll likely lump that response with others into a generic “value perception” theme. But “not worth it” could mean:

- Too expensive for what I’d get
- Too data-intensive and I’m not a serious enough athlete
- I don’t want another device to charge
- I need a screen and Whoop doesn’t have one

It’s one response with four completely different implications for your product decision. Multiply that ambiguity across hundreds of survey responses, and your “themes” become meaningless averages that don’t make decisions any easier.

LLMs are trained to find consensus and compress information. Specificity and valuable edge cases get lost. And if your prompt mentions “pricing issues,” watch how many responses suddenly get coded as pricing-related.

In some cases, that can be helpful, because the model makes sure all outputs are relevant to the specific thing you’re working on. But in many cases, it can be biased cherry-picking from the start.

**Here’s an example:**

![](https://substackcdn.com/image/fetch/$s_!xss5!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F019c47ac-f471-4caf-b9bc-7ba83bbe9587_1600x589.png)

These could describe any wearables study. We can’t make a hardware decision from this.

**Another example:**

I asked ChatGPT to find me theme clusters and counts for the churn survey question “What did you hope to do that Whoop failed to support you with?”

The results below are clusters that don’t help us make this decision either. So 18% of churned respondents need “more actionable guidance,” which sounds like a job-to-be-done. But there are too many possible directions within that cluster for us to make a decision more easily. Should Whoop focus on clearer metrics or workout plans, or both? Plus, most of this has nothing to do with our screen decision.

![](https://substackcdn.com/image/fetch/$s_!dtDi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4259eb73-5315-4845-97f2-d6a16c53e6b7_1600x940.png)

When we ask AI to cluster survey responses, we need to give it clear direction with context, or we’re leaving room for mediocre decisions and more manual work.

#### The fix: Context loading that actually guides interpretation

Most people are used to prompt frameworks that have sections like Role, Context, Task, Format, and so on. Context to most of us means including a few lines of background information in the prompt, somewhere near the beginning. When we’re using AI for analysis, that often focuses on the point of this current customer discovery. Think: objectives, hypotheses, and what part of the product we’re working on.

In the past year, I’ve seen more and more people turn the prompt’s “context” section into four paragraphs of anything they could think of about their work, often dictated in a stream of thought while eating lunch.

But neither three lines of objectives nor the whole unstructured backstory is good enough. Effective context loading has *at least* four components that shape how AI interprets everything that follows:

1. **Project context** tells AI the scope and stakes. “Exploring whether to add a screen” is a specific decision with constraints. “Doing customer research” is vague, so AI defaults to generic analysis because you gave it no frame.
2. **Business goal** tells AI what you’re trying to achieve. If you need to know whether a feature would attract new users vs. alienate existing ones in order to prioritize building it, say that. AI will weight evidence toward answering *your* question and addressing *your* decision, not the decision it assumes you’re making.
3. **Product context** gives AI domain knowledge. Without it, AI interprets “I want to see my data” generically. With it, AI understands that statement in the context of a screenless wearable competing against Apple Watch—a completely different interpretation.
4. **Participant overview** tells AI who’s speaking. “I need real-time data” from a churned Garmin switcher means something different than the same words from a loyal user who’s never tried a competitor. AI can only weight evidence correctly if it knows who the evidence is coming from.

The good news is that a lot of what I see people add to the context in their prompts is superfluous. You often don’t need as much information as you think, but it needs to be clear, direct, and relevant information, like the four items above.

**For interviews, put this context into an analysis prompt (or use as a single prompt):**

> `PROJECT CONTEXT    We’re exploring whether to add a screen to Whoop. This is a major hardware decision. These are 10 interviews with churned users.`
> 
> `BUSINESS GOAL    Determine if a screen would:    (a) win back churned users,    (b) fail to solve the core problems of churned users, or    (c) come with other requirements in order to succeed at increasing retention.`
> 
> `PRODUCT CONTEXT    Current: No screen, all data via app. Value prop is focus during activity and day, no distraction, learn what works for you over time.    Key competitors with screens: Apple Watch, Garmin, Suunto.    Without: Oura.    Key tension: Is screenless a limitation for key audiences that are churning (who are still our target audience)? Or are they a request among audiences that we should not focus on?`
> 
> `PARTICIPANT OVERVIEW    All participants are CHURNED users.   Lifetime with Whoop: 6 months to 2 years.   For participant-specific details, see metadata in each file.`

**For surveys, add data structure to the prompt:**

- What are the columns?
- How is it formatted? (Is it a little abnormally structured vs. what might be more typical CSV survey columns or coding?)

Assuming AI will know exactly what your data’s format means is often why silly mistakes happen. Instead, take 30 seconds to write down any part of your CSV file’s format and coding that might be less than 100% clear. That will head off calculation errors and interpretation issues.

Here’s an example of survey context that I’d call non-negotiable (and I often still add a bit more):

> `DATA STRUCTURE    Column A (response_id): Ignore    Column B (product_tier): “one”/“peak”/“life” — use for segmentation    Column C (response): Customer’s voice — primary analysis target    Column D (status): Internal tag — churned or active   Column E (source): “partner_discount,” …`
> 
> `INTERPRETATION GUIDANCE    Audience is churned users only — this is an EXIT survey. No current users.   Focus on specificity, segment differences, and whether a screen would actually solve the stated need.`
> 
> `Note: Column D coding — 0 = churned, 1 = active`

**Here’s what I got when I clarified the context for the interviews—individual verdicts, a tally, and scenario-based recommendations I could actually take to a roadmap discussion.**

*Individual responses analyzed more thoroughly, and each gets a verdict, not just a label:*

![](https://substackcdn.com/image/fetch/$s_!fIsj!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09b306b4-fb2a-4d0e-b704-ed20a6c9d6a9_1600x932.png)

*The tally gives a clear answer: 30% would be retained by a screen:*

![](https://substackcdn.com/image/fetch/$s_!_Te7!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67f412ff-1050-448f-b0f6-9ab7713dfe30_1600x494.png)

*ChatGPT’s summary now gives scenario-based recommendations, not just themes:*

![](https://substackcdn.com/image/fetch/$s_!vLjc!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51b77e2b-2362-497a-8c46-496fed6e8aaa_1600x637.png)

These are simplified versions of context loading, but they’ll work for you as a bare minimum. Less than this, and you’ll waste your context window following up to fix things. In practice, I adapt this structure for different discovery questions and situations. For example, churn analysis requires different context than feature prioritization.

If outputs are still generic or jumbled after context loading, your context probably wasn’t specific enough. Add more detail about what you’re actually trying to decide, where your team is trying to *go*, and what you already know that you don’t want repeated.

### Failure mode #3: “Signal” that doesn’t guide better decisions

#### What the problem looks like

You ask AI to analyze hundreds of cancellation survey responses. It tells you “22 respondents mentioned wanting a screen.” Or “sentiment toward screen feature is 72% positive.”

Great. But should you add a screen? Those numbers can’t answer the question because they don’t tell you:

- How many of those 22 would truly have been retained by a screen?
- How many said “screen” but really meant “better app UX” or “GPS navigation”—things a screen alone wouldn’t solve?
- How many have problems that a screen is completely irrelevant to (billing issues, engagement problems, competitive losses) and might be *more* important to long-term satisfaction and perceived value?

Default AI analysis gives you counts and categories. It doesn’t give you *decision clarity*. “22 people mentioned screens” feels like signal, but it’s not actionable until you know what building a screen would actually solve and *if* it would solve it.

#### Why this happens

LLMs are trained to find patterns and summarize. “Screen” appears 22 times, therefore “screen value is a theme.” But the model doesn’t know that “I check my phone 10 times per workout” (screen would help) and “I went back to Garmin” (because they’d like a screen but also need *other functions*, like trail-running navigation) require completely different solutions from your team.

Without guidance, AI may treat all mentions equally. It can’t distinguish signal that should drive your roadmap from noise that sounds like signal but isn’t.

**Here’s an example:**

![](https://substackcdn.com/image/fetch/$s_!Si2C!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F217758ad-cec1-4681-b018-c94de38934c1_1600x226.png)

Seeing this, you might think, “Lots of respondents want a screen.” But only *some* of them would have *most of their problems* solved by a screen without needing *other* new functionality too.

#### The fix: Few-shot calibration that teaches AI your scale

Few-shot calibration means giving AI concrete examples and, more specifically, examples of each level on your scale. Not descriptions of what the levels mean but actual examples of responses that belong in each bucket, and *why*.

Here’s an example of a calibration I use in my analysis prompts and agents for situations like this screen decision:

> `SOLUTION FIT SCALE (calibrated for screen decision)       1 - SCREEN WOULD RETAIN: Explicit visibility/access pain during activity   Example: “I check my phone 10 times per workout just to see my HR”    Why this is a 1: Specific friction with current workaround. Screen directly solves this. High-value signal for screen investment.       2 - CHEAPER FIX WOULD RETAIN: Sounds screen-related but has lower-cost solution    Example: “App was too clunky to check mid-workout, too many taps”    Why this is a 2: Visibility complaint, but phone was present. App UX fix could solve this without hardware investment.       3 - ENGAGEMENT FIX NEEDED: Stopped using, screen wouldn’t change that    Example: “Just wasn’t using it enough”    Why this is a 3: Self-blame framing, no feature complaint. Screen doesn’t fix habit formation. Needs onboarding/engagement intervention.      4 - OPERATIONAL FIX NEEDED: Billing, support, reliability—not features    Example: “Canceled 3 times and kept getting charged. Telling my running club to avoid.”    Why this is a 4: Trust/process failure. Screen is irrelevant. Needs immediate service recovery.       5 - UNRELATED COMPETITIVE LOSS: Left for alternative, no screen complaint    Example: “Switched to Apple Watch, Whoop was fine”    Why this is a 5: No negative language, no screen mention. May be ecosystem/social/price-driven. Screen alone unlikely to win back.`

The examples above do the teaching. I’m not saying, “This is what good output looks like.” I’m saying, “This is good output, and here’s *why* I labeled it this way, so you can follow my process.”

Without clarity like this, the model invents its own interpretation of what “screen-related churn reasons” look like—and it won’t always match yours. This structure works for any scale. Calibrating demand for new offers? Define what a 1 vs. 5 looks like with clear examples. Prioritizing feature requests, or categorizing neutral feedback more accurately? Same approach. The key is showing AI, not telling.

Here’s an example of what I get when I use an approach like that. It’s just a snippet of two individual responses, but it gives you the idea:

![](https://substackcdn.com/image/fetch/$s_!Dj_g!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15deb8c5-f940-40ea-acbe-64db8c10b311_1600x309.png)

With the right calibration, AI can show you which feedback says “build this” and which says “fix something else first.”

You’ll spend a few extra minutes building a scale for your context, but you can reuse it across analyses. Stack this with the quote verification from Failure Mode 1, and you get actionable interpretation plus real evidence in the customer’s voice. I’ve built agents that interpret data the way a senior researcher would, but in near real time as data comes in.

### Failure mode #4: Contradictory insights

#### What the problem looks like

The analysis looks great, the themes are clear, the quotes are compelling. The summary table is ready for your deck. Maybe the way AI used your guidance around customer feedback intensity looks amazing and you’re eager to run with those results to your next meeting.

But you never checked whether everything AI did so far was solid or filled with holes. You never looked for contradictions in what participants said. You never asked whether the “strong advocate” customer actually hinted at *behaviors* that suggest otherwise.

You present findings with confidence. They’re wrong in ways you can’t see, until someone asks a question you can’t answer or a decision blows up a few weeks later.

This might be the most common failure mode. I hear the scary stories of analysis that didn’t hold up in meetings too often, even with the huge LLM improvements we’ve seen in the past year. The other three failure modes—invented evidence, false or generic insights, “signal” that doesn’t guide better decisions —produce outputs that look good. But without a verification step, you have no way to know they’re wrong.

Most people skip contradiction verification because stories in the first analysis pass feel complete. AI doesn’t say, “By the way, I’m not sure about Participant 03” or “You should double-check this buyer journey.” It presents everything with equal confidence.

#### Why this happens

Human expert analysts do multiple passes instinctively. AI doesn’t, unless you tell it to.

That’s by design. LLMs are trained to produce coherent, helpful responses, not to flag their own uncertainty, by default. The first pass is always a hypothesis. Without another pass that specifically looks for errors, you’re treating a draft as a final answer.

This looks ready to share—but is likely ignoring contradictions in the data:

![](https://substackcdn.com/image/fetch/$s_!tn__!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa557d552-4d51-47b1-a8cf-0a182aea76fd_1374x928.png)

#### The fix: Build a final verification pass into every analysis

Verification means asking AI to audit its own work, specifically looking for the errors you now know to expect. A verification prompt targets the specific failure modes: fabricated evidence, contradictions that change the picture, findings that sound solid but aren’t.

Here’s an example verification prompt:

> `VERIFICATION PASS`
> 
> `Review the analysis above for:`
> 
> 1. `QUOTE VERIFICATION`
> 	- `Confirm each quote exists verbatim in the source`
> 		- `Flag any quotes that are paraphrased, combined, or not found`
> 2. `CONTRADICTION CHECK`
> 	- `For each participant, check if statements at different points conflict`
> 		- `Look for: stated preferences vs. described behaviors, confidence followed by hedging, strong opinions that soften later in the interview`
> 3. `CONFIDENCE ASSESSMENT`
> 	- `For any finding based on limited evidence, flag it`
> 		- `Note participants where the stance is unclear or mixed`
> 
> `Output a verification summary with flags and recommended revisions.`

When you push any LLM to review its own labeling and interpretation, it actually *will* find errors. Some errors will be big missteps; some will be tiny exaggerations of what someone said, lumped in with others in a pattern that doesn’t fit perfectly. Either way, we only want to make big, scary product decisions on evidence that’s had that second (or third) review.

In this case, the AI found major problems with its initial analysis once I ran a final verification to make sure I could trust the conclusions.

![](https://substackcdn.com/image/fetch/$s_!KoF8!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95b8dbba-2800-449a-996c-fe031e9ee759_1600x732.png)

This step adds a few minutes to your analysis, but it could literally save you millions of dollars of investment in the wrong product change if you’ve become reliant on AI’s analysis results. In less extreme cases, it’s still the difference between presenting findings you *hope* are right or presenting insights you’ve stress-tested and stand fully behind.

To wrap up, I want to give you one really fast way to check your latest insights work with AI.

## Try this with your latest analysis

You just learned four failure modes that break most AI analysis, and how to fix each one:

1. **Invented evidence** → Quote selection rules + making sure they’re real
2. **False or generic insights** → Context loading that actually guides interpretation
3. **“Signal” that doesn’t guide better decisions** → Few-shot calibration with real examples
4. **Contradictory insights** → A pass that catches what earlier passes missed

If you apply even one of these to your next project, you’ll get better results than you’re getting now. But don’t wait for your next project. Pick an analysis you’ve already done with AI: an interview summary, survey patterns, anything where you asked AI to find themes or pull quotes. Run the verification pass from Failure Mode 4 on it.

If you’re like most people, you’ll find at least one quote that doesn’t exist, one contradiction that got buried, or one “pattern” based on a single response. That’s not a failure—that’s the system working. Now you know what to fix before it ends up in a deck.

**Verification is the difference between AI output you’ll always second-guess and insights you can stand behind.**

The big problem with AI analysis is that the output always looks confident, with clean themes, punchy quotes, and tidy summaries ready to copy into Gamma for slide styling. Nothing in the output signals “check me again.”

That’s exactly why these failure modes are dangerous. Not because AI is bad at analysis—it’s becoming remarkable—but because the mistakes are invisible until a decision falls apart three months later, or you realize the “customer evidence” behind a major investment actually had enormous holes.

The fixes in this post aren’t about slowing down but about making AI analysis something you can actually defend: evidence you’d bet your reputation on, recommendations you won’t have to walk back. Fifteen minutes of verification now or six months of building the wrong thing later—that’s the trade.

*Thanks, Caitlin! For more from Caitlin, find her on [LinkedIn](https://www.linkedin.com/in/caitlindsullivan/) and in her new course, [Claude Code for Customer Insights](https://maven.com/caitlin/claude-code-insights).*

*Have a fulfilling and productive week 🙏*

---

**If you’re finding this newsletter valuable, share it with a friend, and consider subscribing if you haven’t already. There are [group discounts](https://www.lennysnewsletter.com/subscribe?group=true), [gift options](https://www.lennysnewsletter.com/subscribe?gift=true), and [referral bonuses](https://www.lennysnewsletter.com/leaderboard) available.**

Sincerely,

Lenny 👋