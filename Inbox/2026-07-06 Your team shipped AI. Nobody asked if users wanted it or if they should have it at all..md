---
type: "Web"
authors: "[[Kasia Szczesna]]"
url: "https://behavioralinsight.substack.com/p/your-team-shipped-ai-nobody-asked?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-07-06
created: 2026-07-11
tags:
---


I attended a product conference where presenter after presenter showed how their organizations were deploying AI. Every presentation revolved around the same metrics: speed of deployment, number of features, time saved. Not one touched on what changed in user behavior, whether people were actually making better decisions with the system’s help, or what happened when the AI got something wrong. This isn’t a criticism of enthusiasm around AI. It’s an observation of a gap that most organizations only start to notice when adoption rates stop climbing, users begin signaling distrust, and regulators start asking how the system influences human decision-making.

---

## Three questions nobody asks before deployment

BehaviorAI Design Framework starts from the premise that every AI deployment in a product or organization is a behavioral intervention. You are changing the way people think, decide, and act. Doing this deliberately requires answering three questions in a specific order.

---

## Question one: What is blocking the behavior you want to change?

Before designing an AI solution, it helps to understand why the desired behavior isn’t happening now. Is it a matter of knowledge, motivation, or opportunity - does the user not know, not want to, or simply not have the conditions to act because of how the system or environment is set up? This is a COM-B diagnosis applied not to a patient but to a digital product user.

An insurance company deploys AI for product recommendations and assumes salespeople will use it because it saves them time. After three months, adoption is at 12%. The reason turns out to be straightforward: salespeople don’t trust recommendations they don’t understand, so they default to their own judgment even when it’s less precise. This isn’t an interface problem or a model quality issue. It’s a problem of perceived system competence that would never have been caught during the design phase without a behavioral diagnosis.

If the product team had started by asking “what makes a salesperson trust a recommendation?” instead of “how do we build an interface for recommendations?”, the answers would have been completely different. A COM-B diagnosis would have shown that the barrier wasn’t in capability or in knowing how to use the tool, but in motivation - specifically in the sense that AI works like a black box whose outputs can’t be verified or defended in front of a client. That’s a starting point for design, not a conclusion to draw three months after launch.

### Trust in AI doesn’t work the same way as trust in people

Trust in another person builds over time, through repeated experiences and through the ability to ask a question and get an explanation that actually makes sense to you. Trust in an AI system builds differently — through predictability of behavior, transparency of intent, and the sense that the system is working for me rather than instead of me.

A useful example from product design practice: when you ship a new AI-powered search feature, users typically test it a few times, check whether the results “make sense,” and either start using it regularly or go back to their previous way of working. That window the first two or three uses is not the moment for communicating the system’s capabilities. It’s the moment where the foundation of trust is either built or broken. If the AI returns a result the user can’t evaluate or challenge, they won’t come back to try again - they’ll return to what they knew, because at least there they understand what they’re getting. In practice this means trust isn’t a state that appears once after a well-designed onboarding, but a process where every point of contact either builds the relationship or chips away at it. A behavioral diagnosis needs to account for where the user is in that trajectory and what specifically is blocking or eroding trust at that particular point.

---

## Question two: What should change, and how?

Once you understand what’s blocking the change, you can select the right intervention. The framework draws on the Behaviour Change Wheel, enriched with design patterns specific to AI — transparency, personalization, error handling, uncertainty communication. This is where BehaviorAI Pattern Library comes in, not as an aesthetic solution but as a repertoire of interventions matched to the identified behavioral problem.

But before reaching for a specific pattern, there’s a question most teams skip: how deeply should AI enter the user’s decision-making process?

### Fast and Slow Collaborative AI - when AI accelerates, and when it thinks alongside you

Kahneman described two cognitive systems: the fast, automatic, intuitive one, and the slow, analytical, deliberative one. AI is typically designed to replace the second to analyze data, generate recommendations, and make decisions faster and more cheaply than a human. The problem is that not all decisions should be fast, and not all should be delegated to the system.

Consider a team lead who receives an automated AI recommendation about backlog prioritization. If the AI simply reorders the tickets without explanation, the team lead will either accept it without reflection, which can be risky or reject it and go back to manual sorting, because there’s no basis for evaluating whether the recommendation makes sense. Neither response is good. But if the AI shows which factors it considered and where its confidence is low, the team lead can quickly assess the recommendation, adjust what requires their contextual knowledge, and make a better decision than they would have made alone. That’s augmentation instead of automation — and it requires a completely different design pattern than “show the result.”

In the **FASCAI (Fast and Slow Collaborative AI)** approach, the question about the mode of collaboration comes before interface design. Should AI replace the user’s thinking at this point through automation? Should it support it by providing data, options, and context while leaving the decision to the human? Should it provoke thinking by surfacing alternatives, challenging assumptions, or slowing down a hasty decision? Each of these modes requires a different design pattern, different communication, and a different distribution of responsibility, and each affects trust and user agency in a different way.

### Agency is not a feature, it’s a design decision

A common mistake in AI design is the assumption that the more the system does for the user, the better the experience. In practice the opposite is often true. A user who doesn’t understand why the AI made a particular decision and has no real way to challenge it isn’t being assisted. They’re being replaced. Over time they either start avoiding the system or stop thinking critically about its outputs, and both of those outcomes are bad.

A very concrete example of this dynamic appears in AI-assisted content moderation tools. When a system automatically rejects a submission without explanation, the moderator loses any sense of influence and starts either mechanically approving AI decisions without verification, or ignoring them entirely and acting on their own judgment. In both cases the AI stops serving its purpose. When that same system shows why it rejected the submission and allows the moderator to decide differently with a recorded reason, the moderator stays in the role of an expert who controls the tool, rather than an employee controlled by it. Results are typically better and adoption is higher.

Designing for agency means the user always knows what the AI did and why, what they can do about it, and what will happen if they decide differently from what the system suggests. This isn’t transparency as a principle - it’s the foundation of trust that allows AI to function effectively over the long term.

---

## Question three: Should this change be made at all?

This is the question most design processes skip, and it matters especially with AI. AI can be designed to shorten a user’s decision-making path, but not every path should be shortened. Coming back to FASCAI: the decision about the mode of collaboration isn’t just a product decision, it’s an ethical one.

If you’re designing AI that automates credit recommendations, diagnoses patient needs, or supports HR decisions, the question “should this automation be here?” stops being philosophical.It becomes a question with an answer required by the regulator, documented in a risk management system, and signed off by someone specific in the organization. The difference between a product designer who asked this question during discovery and one who didn’t is only visible at the moment of an audit or an incident — but by then it’s very costly.

It’s worth thinking about this through the analogy of accessibility. For years, accessibility was treated as an optional step at the end of the process, something to add if there was time. We now know that accessibility built into the process from the beginning is cheaper, more effective, and protects the organization from legal risk. The ethical question about AI works the same way. The earlier it comes in the design process, the less it costs and the more value it delivers.

The framework builds a structure for answering this question through a documented design decision: what is the actual level of AI autonomy in this flow, what happens to human decision-making when AI takes over a given step, and whether the user has a genuine ability to disagree that is designed as a full-fledged path rather than a hidden button at the bottom of a screen.

---

## Who uses it and what it looks like in practice

The framework is a tool for people responsible for product strategy or user experience in organizations that have deployed or are deploying AI and have started to notice that the technology alone isn’t enough. In a workshop setting, a session begins with mapping behavioral barriers, moves through selecting the mode of human-AI collaboration and designing interventions, and ends with an ethical decision documented and ready for audit.

The output isn’t another user journey map - it’s a design decision with visible logic: we know what was blocking change, how we’re addressing it, and why the intervention is ethically and legally justified. This is the layer most AI deployments are missing, and its absence is increasingly visible in adoption numbers, user trust levels, and readiness for regulatory scrutiny.

---

*Kasia Szczęsna — behavioral designer and AI interaction specialist, founder of BehaviorAI. She builds tools and frameworks at the intersection of behavioral science, design, and AI ethics. [behaviorai.eu](https://behaviorai.eu/) | [kasiaszczesna.pl](https://kasiaszczesna.pl/)*