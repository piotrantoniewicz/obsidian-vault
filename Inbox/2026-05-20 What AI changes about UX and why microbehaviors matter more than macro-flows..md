---
type: "Web"
authors: "[[Katarzyna Szczesna]]"
url: "https://behavioralinsight.substack.com/p/the-cognitive-cost-nobody-put-in?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-05-20
created: 2026-05-20
tags:
---


![](https://substackcdn.com/image/fetch/$s_!C3kj!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12a38f50-24f6-4497-bcfc-3e3cf13355c0_1200x1200.png)

When a new AI-powered interface reaches a user, the first question is usually whether it works. The second is whether it is fast. Rarely does anyone ask how much mental effort the system generates, and for whom it reduces that effort versus quietly multiplying it.

This is where many implementations have a genuine blind spot. We design flows and optimize conversion rates. We measure task completion time and error rates. But we tend to skip something more fundamental: the human brain does not process interfaces the way we assume it does when we draw wireframes.

## Why microbehaviors tell you more than macro-flows

Conventional UX thinking focuses on flows. The user enters, clicks through, reaches the goal. Behavioral design breaks this picture into smaller units, down to the micromoment when a person decides whether to continue or give up. That is where the real story is.

Daniel Kahneman’s research on cognitive systems shows that the vast majority of our decisions are made through System 1, which is fast, automatic, and pattern-based. System 2, the reflective and analytical mode, only engages when the situation demands deliberate effort. The problem is that AI interfaces often unintentionally force a shift into System 2 mode precisely at the moments when users are expecting relief.

**Research note  
**Kahneman and Tversky (1974) described how cognitive heuristics simplify decisions at the cost of accuracy. In interface design, this means that any inconsistent visual signal, unexpected system response, or ambiguous error message can trigger unnecessary cognitive effort, regardless of how efficiently the AI engine beneath it performs.

Microbehaviors, like a brief hesitation before clicking, rereading the same message twice, or switching to another tab “just to check,” are signals we collect far too rarely. They are precisely the evidence that shows where a system fails psychologically, even when it is working correctly at a technical level.

## Friction: not always a problem, but always a design decision

For years, UX design operated under a near-universal rule: the less friction, the better. Remove barriers, simplify the path, reduce the number of clicks. Behavioral design complicates that picture.

Cognitive friction, the brief resistance that slows an action down, can be a design instrument rather than a defect to be eliminated. Thaler and Sunstein, who developed the concept of the nudge, showed that a well-designed choice architecture can guide people toward better decisions without coercion. The point is not to remove friction but to place it where it serves a purpose and remove it where it does not.

**Harmful friction: Resistance without purpose  
**Redundant confirmation steps, unclear error messages, forced verification of AI output without adequate context. It drains cognitive resources and builds frustration without protecting anything.

**Intentional friction: Resistance as protection  
**“Are you sure?” prompts before irreversible actions, a forced pause before deleting records, required confirmation on high-stakes decisions. It creates awareness at the right moment.

**Cognitive overload: Attention fragmentation  
**Too much information at once, conflicting signals from the AI, interfaces that require constant context switching. Each of these leads to errors and abandonment, not just mild inconvenience.

**Cognitive fluency: The ease effect  
**Reber et al. (2004) found that information which is easy to process is rated as more credible and more valuable. Interface readability directly affects how users evaluate the quality of AI output.

When designing with AI, the question is not “how do we remove friction?” It is “where is friction a cost, and where is it a safeguard?” Answering that requires knowledge of what is happening inside the user’s head, not only on the screen.

*“AI systems do not just automate tasks. They reshape where attention goes. And attention is a finite resource.”*

## AI does not always reduce workload. Sometimes it increases it.

That claim sounds counterintuitive. The reason we deploy AI is to make things lighter, faster, and more manageable. And often it does exactly that. But work psychology surfaces a pattern that tends to be called hidden work, and in AI systems it is reaching a new scale.

When a task is automated, the effort associated with it is not eliminated. It is transformed. Instead of executing a task from beginning to end, people shift into monitoring, verifying, and correcting. That is a different kind of work, and it tends to be more fragmented. Attention is split across multiple parallel processes. Responsibility becomes unclear: the system produced the result, but the human must check it, and the cost of a missed error sits with the person, not the model.

## Hidden work in AI systems

**Output verification  
**Checking whether AI produced a correct result. In expert domains, this often requires the same cognitive effort as doing the task independently, with the added burden of managing trust in the system.

**Edge case handling  
**Everything the AI did not handle or handled incorrectly. These cases are rare in volume but require the highest concentration. They generate stress disproportionate to their frequency.

**Context switching  
**Working with AI typically means moving between the AI tool and other resources. Gloria Mark’s research estimates that a full return to focused concentration after switching takes around 23 minutes.

**Managing uncertainty  
**AI systems often do not surface their own confidence levels. Users must judge when to trust the output and when to investigate, without sufficient design cues to guide that judgment.

**Responsibility without clarity  
**When decision ownership is diffuse, a low-level chronic stress emerges. Research on algorithmic management describes this pattern, but it appears in consumer products too, wherever accountability is ambiguous.

The outcome is not always less work. It is always different work. If AI is genuinely going to reduce effort, we need to account for the work it creates, not only the work it removes. That is a design problem, and work psychology has tools to address it.

## Cognitive processes as a starting point for design

Behavioral design with AI is not about memorizing a list of cognitive biases and scanning for them in a design review. It is about understanding what mental state a user is in when they arrive at an interface, and how that state shifts during the interaction.

John Sweller’s cognitive load theory (1988) identifies three types of load: intrinsic, which comes from the complexity of the task itself; extraneous, which comes from the complexity of the interface; and germane, which is the effort required to build new knowledge or schema. Good AI design minimizes extraneous load, does not compound intrinsic load unnecessarily, and where the goal is learning, supports germane load rather than short-circuiting it.

**Implication for product teams  
**When designing an AI flow, “how many clicks does this take?” is secondary to “what types of cognitive load are we generating?” Answering the second question requires different research methods, different success metrics, and personas that account for emotional context and attentional state, not only behavior on screen.

In the context of AI, another layer enters the picture: trust. Mayer, Davis, and Schoorman (1995) define trust through three components: ability, benevolence, and integrity. Users evaluate AI through the same lens, and they do it very quickly, based on design signals. How does the system communicate errors? How does it signal its own uncertainty? How does it respond when inputs are contradictory? All of this constitutes trust design, whether or not it was named that way in the product specification.

## AI patterns that shape decisions: barriers are not just logistical

Every AI interface contains patterns that, intentionally or not, shape user behavior. The difficulty is that designers tend to think about logistical barriers, like the number of steps or the physical effort of a click, while users encounter psychological barriers that operate entirely differently.

- **Default bias  
	**Johnson and Goldstein’s research on organ donation defaults (2003) demonstrated the extraordinary power of preset options. In AI interfaces, the default level of system autonomy, the default format of an output, the default verification mode - all of these design choices strongly determine actual usage, independently of user intention.
- **Automation bias  
	**Parasuraman and Manzey (2010) documented the tendency to over-rely on automated systems at the expense of independent judgment. In practice: users approve AI outputs without verification, not from carelessness, but because the interface never created a moment of deliberate reflection.
- **Framing effects  
	**The way AI presents options shapes choices dramatically. “This option is selected by 80% of users” and “20% of users reject this option” describe identical situations but produce different decisions.
- **Completion anxiety  
	**AI systems that generate long outputs often create a counterproductive obligation: the user feels they must read everything before making a decision. This generates effort and avoidance instead of reducing them.

## What to do with this: designing with psychology, not beside it

Behavioral AI design is not an extra layer applied to an existing product. It is a shift in where the design process begins. It means asking different questions before the first wireframe is drawn.

- What is the user’s cognitive state when they enter this flow? Are they focused or scattered? Is this a high-stakes decision or a routine one?
- What work does this interface remove, and what work does it create in exchange? Is the hidden work visible in the design and supported by it?
- Where should friction appear, and where should the experience be frictionless? Are those decisions conscious or accidental?
- How does the interface communicate AI uncertainty? Does the user know when to trust and when to verify?
- What microbehaviors appear in research, and what do they tell us about psychological barriers rather than logistical ones?

**For product and experience teams  
**Consider building cognitive load measurement into your research process. The NASA Task Load Index provides a structured way to capture subjective mental, physical, and emotional demand. Qualitative methods matter too: cognitive walkthroughs that track attentional states, or think-aloud sessions where participants are asked specifically about moments of uncertainty and effort, not just task completion.

Work psychology and behavioral science are not extras for specialists with time to spare. They are the foundation for building systems that genuinely serve people, rather than systems that perform well in demos and generate invisible costs in daily use.

---

*Behavioral AI design is a discipline that is still maturing, but its questions are already urgent. Every implementation that ignores cognitive processes transfers a cost onto users that will never appear in a product dashboard. Until we start measuring hidden work and designing with the psychology of attention in mind, our AI products will be more impressive than they are genuinely useful.  
  
——*

**Tversky, A., & Kahneman, D. (1974)** “Judgment under Uncertainty: Heuristics and Biases” *Science*, Vol. 185, No. 4157, pp. 1124–1131 DOI: 10.1126/science.185.4157.1124 Potwierdzone. Dostępne w JSTOR i Science.org.

**Sweller, J. (1988)** “Cognitive Load During Problem Solving: Effects on Learning” *Cognitive Science*, Vol. 12, No. 2, pp. 257–285 DOI: 10.1207/s15516709cog1202\_4 Potwierdzone. Dostępne w Wiley Online Library.

**Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995)** “An Integrative Model of Organizational Trust” *Academy of Management Review*, Vol. 20, No. 3, pp. 709–734 Dostępne w JSTOR (stable/258792). Potwierdzone, łącznie z kolejnością autorów i numerem strony.

**Johnson, E. J., & Goldstein, D. (2003)** “Do Defaults Save Lives?” *Science*, Vol. 302, pp. 1338–1339 DOI: 10.1126/science.1091721 Potwierdzone. Badanie jest rzeczywiste i dotyczy dokładnie organdawstwa i domyślnych opcji opt-in vs opt-out.

**Parasuraman, R., & Manzey, D. H. (2010)** “Complacency and Bias in Human Use of Automation: An Attentional Integration” *Human Factors: The Journal of the Human Factors and Ergonomics Society*, Vol. 52, No. 3, pp. 381–410 DOI: 10.1177/0018720810376055 Potwierdzone w pełni, łącznie z rokiem i współautorem Manzey.

**Reber, R., Schwarz, N., & Winkielman, P. (2004)** “Processing Fluency and Aesthetic Pleasure: Is Beauty in the Perceiver’s Processing Experience?” *Personality and Social Psychology Review*, Vol. 8, No. 4, pp. 364–382 Potwierdzone. Uwaga: to badanie dotyczy estetyki i przyjemności przetwarzania, a nie bezpośrednio wiarygodności. Pokrewne badanie Reber & Schwarz (1999) w *Consciousness and Cognition* bardziej wprost mówi o fluency a sądach o prawdziwości. Jeśli artykuł ma konkretne przypisy, warto użyć obu.

**Gloria Mark (2008)** “The Cost of Interrupted Work: More Speed and Stress” *CHI 2008 Conference Proceedings*, UC Irvine Liczba 23 minut jest potwierdzona i pochodzi właśnie z tego badania. Cytowana przez Fast Company, Gallup i UCI.