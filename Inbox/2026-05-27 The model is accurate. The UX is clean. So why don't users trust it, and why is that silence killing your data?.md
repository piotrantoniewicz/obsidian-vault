---
type: "Web"
authors: "[[Katarzyna Szczesna]]"
url: "https://behavioralinsight.substack.com/p/the-model-is-accurate-the-ux-is-clean?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-05-27
created: 2026-05-29
tags:
---


For designers and product builders creating AI-powered products

![](https://substackcdn.com/image/fetch/$s_!89WF!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf115da9-e261-413e-9b13-38140511cc43_1200x1200.png)

Imagine asking a new coworker to analyze your sales data. They respond immediately, without a moment’s hesitation, without a single “hmm” or “it depends on the context.” They speak directly, confidently, almost mechanically. The answer turns out to be correct, and you go and double-check it anyway, because something about the way it was delivered made you uneasy.

The same thing happens every day in human-AI interactions, and if you’re building a product powered by artificial intelligence, this mechanism is probably already costing you user trust and the data you desperately need.

## A Problem That Isn’t a Technical Problem

Research on clinical decision support tools reveals a troubling pattern: doctors regularly override AI recommendations, even from systems that are historically more accurate than humans. Not because they distrust the algorithm as such, but because the algorithm sounds too confident given the complexity of the clinical situation. The system says “Recommended treatment: X,” the doctor feels internal uncertainty, registers a mismatch between their own state and the system’s message, and ignores the recommendation. We see the same behavior in consumer products, enterprise copilots, and data analysis tools, where users describe AI as “overconfident” and “like it’s bluffing,” even when the AI is right.

We’re dealing with a classic case of expectancy violation, and to understand why this is quietly damaging your product, we need to look at social psychology.

## Expectancy Violation Theory: When “Too Good” Means “Wrong”

**[Expectancy Violation Theory (EVT)](https://www.researchgate.net/publication/314643101_Expectancy_Violations_Theory)** holds that people enter every interaction with a set of unconscious assumptions about how that interaction should unfold. When reality deviates from those expectations, the brain registers an alert and triggers defensive behaviors, regardless of whether the content of the message is actually correct. EVT was originally developed to describe communication between people, but it applies equally well to AI interactions, because people unconsciously treat AI systems as social actors, responding to their tone and feeling uncomfortable when they “act strangely.”

Three components of EVT map directly onto human-AI interactions:

- **Expected uncertainty.** People intuitively associate complex reasoning with visible uncertainty. When an expert thinks out loud, hesitates, and considers alternatives, we trust them more, because they behave like someone who is genuinely thinking. An AI that responds instantly and categorically violates this pattern.
- **Perceived overconfidence.** When the AI’s confidence exceeds the user’s internal confidence, a dissonance emerges and the user stops evaluating the accuracy of the answer and starts evaluating its credibility. The result is distrust, even when the answer is correct.
- **Threat to epistemic control.** Users feel responsible for decisions they make with AI assistance. If the system speaks too confidently, it strips them of the sense that they are ultimately in charge, triggering a defensive response: re-checking data, re-prompting, or rejecting the output entirely.

## An Analogy: The Weather Forecast

When a meteorologist says “it will rain tomorrow,” you listen, but you hold a slight reservation, because you know weather is unpredictable. When they say “there is a 73% chance of rain tomorrow afternoon, though the front may shift by a few hours,” you suddenly trust them more. Not because the second answer is more precise, but because it matches your internal model of a world where some things require interpretation and are genuinely uncertain. An AI without visible uncertainty is a meteorologist who says “sunny tomorrow” with no caveats and no margin of error.

## Use Case: When AI Pushes Away the People It Needs Feedback From

A company rolls out an internal recommendation system, say, a tool that helps prioritize sales tasks. The model is good but not perfect, and to learn and improve it needs feedback from users: was the recommendation accurate, what would they change, what was missing. In practice, users don’t give feedback. They don’t click “thumbs down,” they don’t fill out surveys, they don’t report errors.

The intuitive diagnosis is a UX problem: the button is too small, the survey too long. EVT points to something deeper. When the system presents recommendations with very high confidence, for example “Recommended action: contact client X within 24 hours,” the user faces a psychologically costly dilemma: to share any doubts, they have to challenge a system that sounds more certain than they feel. Most people in a professional context, especially when the system is the company’s official tool, won’t do that. It’s like hiring a consultant who ends every meeting with “I’ve decided, case closed,” and then wonders why no one shares their opinions with him.

The consequences for the model are serious. The company receives feedback mainly from two extreme groups: people who are clearly satisfied and those who are clearly dissatisfied and confident enough to challenge the algorithm. The middle and largest group of users, those with valuable, nuanced observations, stays silent. The model learns from skewed data and becomes increasingly less useful for the very people whose signal it needs most.

## Five Design Decisions That Rebuild Trust

**Calibrate confidence to the type of task.** For interpretive tasks, instead of “Client X is the priority,” try: “Based on available data, client X stands out across three indicators, though it’s worth cross-checking with local context we don’t have.” That’s not hedging, it’s epistemic accuracy.

**Make uncertainty visible in the interface.** Confidence ranges, alternative interpretations, and spans of possible outcomes make users feel invited into a dialogue rather than excluded from one.

**Redesign the language around feedback collection.** “Rate this recommendation” puts the user in the role of examiner. “Did we miss something? Your context is more valuable than our data” signals that their uncertainty is an asset, not a weakness.

**Give users control over the system’s confidence level.** A simple tone setting, such as “Decisive / Balanced / Exploratory,” reduces the discomfort that comes from a mismatch between the system’s certainty and the user’s own uncertainty.

**Treat confidence as a UX variable, not a default model property.** The way you present results and frame recommendations shapes whether users feel like partners in the system or subordinates to it.

## Design for Psychology, Not Just Accuracy

If your system is losing user trust not because it’s wrong but because it sounds too confident for the complexity of the problem, no benchmark will catch that. Behavioral science tells us that trust in a system is not a simple function of its accuracy, but a function of whether its behavior matches deeply rooted expectations about what credible reasoning looks and sounds like. People trust the doctor who says “this could be X, but let’s check Y too,” the meteorologist who gives probability ranges, and the coworker who admits they’re not sure. Your AI system can communicate the same way, not by being less accurate, but by more precisely expressing what it doesn’t know.

## Let’s talk!

If this resonates, [Behavioral AI](https://behaviorai.eu/) is building tools to help organizations understand the human side of AI adoption - the psychological patterns that shape trust, reliance, resistance, decision-making, and behavior around AI systems. You can join the beta at behaviorai.eu.

And if your organization wants to work on understanding the psychology behind how your people adapt to AI, whether that shows up as low adoption, silent feedback loops, or users bypassing the system - we can help through workshops or training sessions focused on behavioral analysis of human-AI interaction.  
  
Let’s talk!  
  
—

*Based on an analysis of Expectancy Violation Theory in the context of human-AI interaction and research on user behavior in decision support systems. Source: Burgoon, J. K. (2016). Expectancy Violations Theory. In: The International Encyclopedia of Interpersonal Communication. Wiley-Blackwell.*