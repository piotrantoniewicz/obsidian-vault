---
type: "Web"
authors: "[[Kasia Szczesna]]"
url: "https://behavioralinsight.substack.com/p/ai-should-support-people-at-work?utm_source=substack%2Csubstack&utm_medium=email%2Cemail&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-07-16
created: 2026-07-16
tags:
  - "strategia-AI"
  - "produkty-cyfrowe"
  - "trendy-AI"
---


![](https://substackcdn.com/image/fetch/$s_!MiZ7!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c855c52-8913-45cf-9eb2-98e8d8782155_1200x1500.png)

In July of this year, **[Stanford Digital Economy Lab published an open letter](https://www.techtimes.com/articles/320398/20260714/nobel-economists-who-doubted-ai-job-fears-now-sound-alarm-white-collar-displacement.htm)** signed by over 200 economists, researchers, and technology leaders, including Eric Schmidt, Reid Hoffman, sixteen Nobel laureates, and AI pioneers such as Yoshua Bengio and Jeff Dean. The letter warns that AI may over the next decade trigger a transformation of the labor market larger than the Industrial Revolution, and that this time the changes could unfold many times faster. The core message was clear: we are not stopping AI development, but we need new institutions, regulations, and economic incentives that will ensure AI complements humans at work rather than simply replacing them.

It’s hard to disagree with that. There is, however, one question the letter doesn’t ask: how do you actually design that?

Because “AI should support, not replace” is not a technology decision or a regulatory one. It’s a design decision, one that gets made long before deployment, during discovery, in roadmap conversations, in every choice about how much autonomy we hand to the system and at which point the decision comes back to a human. And in most organizations it’s a decision made by default, without conscious choice, in the direction of maximum automation.

---

## The default setting: more automation

When I work with product teams, I see the same pattern regardless of industry or organizational scale. Nobody walks into a conference room with a plan to “design a system that takes away people’s sense of agency.” But the default direction of thinking is always the same: what else can AI take over, how do we automate the next step, how do we eliminate the next point of friction in the process.

That’s understandable, because that’s exactly why AI gets deployed, to free people from repetitive and cognitively costly decisions. The problem appears when that assumption becomes invisible and nobody stops to design a boundary. The system takes over more and more steps, the user gradually loses any sense of influence over the outcomes of their work, and eventually “AI supports” has become “AI decides” without any deliberate decision along the way.

What the economists’ letter describes as a macroeconomic problem starts with very concrete, everyday design choices made at the product team level.

---

## Two questions that look the same

Imagine two project management tools. The first recommends task prioritization based on historical data and shows which factors it took into account. The second automatically reorders priorities without asking, with a note in the log that “AI updated the queue.”

The interface in both cases can look nearly identical. But these are completely different products from the user’s perspective. In the first, the user is an expert who receives data to evaluate and makes a decision. In the second, they are an operator who approves or reverses the system’s decisions. This difference fundamentally changes the person’s relationship with the tool, their sense of responsibility for outcomes, and their willingness to think critically when something goes wrong.

Most product discussions about AI stop at the question of what AI should do. The question of what mode it should operate in, and what that means for the person who will live with it every day, comes up far less often.

---

## FASCAI: the question of collaboration architecture

In the approach I use in **[BehaviorAI Design Framework,](https://www.kasiaszczesna.pl/behaviorai-design-framework)** the question about the mode of human-AI collaboration is the first design question, before the interface, before patterns, before wireframes. I call this FASCAI, from Fast and Slow Collaborative AI, drawing on Kahneman’s cognitive systems.

AI is typically designed to replace System 2, the slow, analytical, deliberative, cognitively costly one. Faster, cheaper, without fatigue. The problem is that not all decisions should be fast and not all should be delegated to the system.

The question about the mode of collaboration has three possible answers, each of which leads to a completely different design.

Should AI **replace** the user’s thinking at this point, taking over the decision entirely? That’s automation, justified where the decision is repetitive, well-defined, and the consequences of error are low and easily reversible.

Should it **support** it, providing data, analysis, and context while leaving the decision to the human? That’s augmentation, appropriate where the user has contextual knowledge the AI doesn’t have, or where the consequences of error are serious.

Should it **provoke** thinking, slowing down a hasty decision, surfacing alternatives, questioning assumptions? That’s assisted deliberation, needed where the quality of the decision depends on the person actually thinking through the problem rather than just clicking “approve.”

Each of these modes requires a different design pattern, different communication, and a different distribution of responsibility between the human and the system.

---

## What happens when this decision is made by default

The consequences of a poor decision about automation level are not immediate and are not always visible in standard product metrics. They surface with a delay, in three different forms.

The first is **automation bias**. When AI regularly makes decisions for the user and is regularly right, the user starts to stop verifying its outputs. They treat the system’s results as correct by default, even when the situation is ambiguous. When AI makes a mistake, the error goes unnoticed because the user no longer has the habit of verification. In B2B products where decisions have real business consequences, this is a serious risk that rarely comes up in pre-deployment analysis.

The second is **erosion of agency**. Users who work with a highly automated system over a longer period describe a sense of “doing something, but not quite knowing what.” Formally they are managing a process, but in practice they are approving the system’s decisions at a pace that doesn’t allow for reflection. Over time they either start bypassing AI and returning to previous ways of working, or mechanically approve everything without engaging, and in both cases the value of the product declines. Users often don’t connect this feeling to AI itself, which makes it harder to identify the problem at the product team level.

The third is **loss of trust after an error**. When AI that has been operating autonomously and correctly for a long time makes a mistake in a significant decision, the user has no context to evaluate whether it’s an incident or a symptom. They don’t know when AI was right because it had good data and when it was just lucky. An error from a highly automated system generates a much larger drop in trust than an error from a system that has been operating transparently all along and giving the user the ability to verify its work.

---

## Designing boundaries: three questions before the interface

The decision about automation level should precede interface design, not follow from it. In practice, three questions help that should be asked during discovery.

First: **what are the consequences of an error?** The more serious and harder to reverse, the stronger the argument for augmentation over automation, for leaving the decision to a human with AI support rather than delegating it to the system.

Second: **does the user have contextual knowledge the AI doesn’t have?** AI works on the data it has available. There is always knowledge that isn’t in the system: client relationships, informal agreements, local market specifics, what just changed in the organization. If that knowledge matters to the quality of the decision, automating that decision means systematically ignoring it.

Third: **is the decision regulatorily or ethically sensitive?** The AI Act introduces categories of high-risk systems with limited autonomy levels. But beyond those, there is a broad gray zone of decisions touching on employment, access to financial services, performance evaluation, or content personalization for vulnerable groups. In those areas, the question “should this automation be here?” should have an answer before the product reaches users.

---

## AI silence as a design pattern

“AI silence” is not inaction. It’s designed system behavior in moments when an autonomous decision would be inappropriate due to low confidence, high error risk, or sensitivity of context.

Well-designed silence looks concrete: the system signals that it has recognized a situation requiring a decision, communicates what it knows and with what confidence, indicates that the decision belongs to the user, and provides enough context for that decision to be a good one. This is active system behavior that requires its own design patterns.

A credit risk analysis tool that, faced with an ambiguous profile, instead of generating an automatic decision shows the analyst “this application contains a combination of factors whose pattern did not appear in the training data, we recommend manual review,” doesn’t give up on analysis. It just doesn’t jump to a decision it has no basis for. The user gets information and agency at the same time.

That is “AI supporting people at work,” not as a declaration, but as a concrete design pattern.

---

## From declaration to design decision

The economists’ letter describes the problem at the level where governments and institutions operate. But the daily experience of a person working with AI is designed by product designers and product managers, during discovery, in roadmap conversations, in every decision about how much autonomy we hand to the system.

Accessibility for years was treated as a step added at the end of the process if there was time left. Today we know that approach is more expensive, less effective, and generates legal risk that could have been avoided. The question about the boundaries of AI automation is in exactly the same place in the industry’s maturity cycle, still treated as a separate conversation with a lawyer or ethicist rather than as part of the standard design process.

The declaration “AI should support, not replace” becomes reality or doesn’t in the moment when a team lead receives an automatic backlog update without explanation, when a credit analyst cannot challenge the system’s scoring, when a content moderator loses the sense that their expertise has any meaning. These are design decisions. And they can be made deliberately.

---

*Kasia Szczesna is the founder of **[BehaviorAI](http://behaviorai.eu/)** and the author of the **[BehaviorAI Design Framework](https://www.kasiaszczesna.pl/behaviorai-design-framework)**. She works at the intersection of behavioral science, product design, and AI ethics, helping teams design the behavioral layer of AI products.*