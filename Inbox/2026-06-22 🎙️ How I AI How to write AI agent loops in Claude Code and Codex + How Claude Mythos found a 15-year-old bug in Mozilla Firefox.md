---
type: "Web"
authors: "[[Lenny Rachitsky]]"
url: "https://www.lennysnewsletter.com/p/how-i-ai-how-to-write-ai-agent-loops?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-06-22
created: 2026-06-23
tags:
---


![](https://substackcdn.com/image/fetch/$s_!gWeJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F361d81ef-7faf-4d8e-8028-5d5e03432a9a_2329x551.png)

### How to design AI agent loops: schedules, goals, and subagents in Claude Code and Codex

![](https://www.youtube.com/watch?v=JoXbk2fm7jM)

Listen now on **[YouTube](https://youtu.be/JoXbk2fm7jM) • [Spotify](https://open.spotify.com/episode/43kcUzpSfJExbkIotdUbBp) • [Apple Podcasts](https://podcasts.apple.com/us/podcast/how-to-design-ai-agent-loops-schedules-goals-and/id1809663079?i=1000773109920)**

![](https://substackcdn.com/image/fetch/$s_!hnh5!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa30d9a22-40aa-4d45-a24b-526a1d2989cc_1600x114.png)

> **Brought to you by:**
> 
> - **[WorkOS](https://workos.com/?utm_source=lennys_howiai&utm_medium=podcast&utm_campaign=q22025)** —Make your app enterprise-ready today
> - **[Runway](https://runwayml.com/howIAI)** —The creative AI platform for images, video and more

In this hands-on tutorial, Claire explains the difference between heartbeats, crons, hooks, and goal-based loops, then builds real automations in Claude Code and Codex, including a daily PR-review loop and a weekly skills loop that spawns its own subagents. If you’ve heard “loop engineering” and wondered what it actually means, this is the beginner-friendly breakdown.

#### Biggest takeaways:

1. **A loop is just a prompt that fires itself, nothing more exotic than that.** The reason “loops” sound intimidating is that the hype cycle turned a basic automation concept into something mystical. Heartbeats, crons, and webhooks have been around forever. What’s new is pointing them at an AI agent instead of a batch job.
2. **Goals are the most powerful loop type, and the one most people get wrong.** A goal loop sets an outcome and runs an agent against it until the outcome is validated or the agent gets stuck. It doesn’t stop on a timer; it stops when the work is actually done. Fuzzy success criteria means the agent loops forever, burning tokens, so my advice is to let Codex write its own goals, using OpenAI’s goal-writing guide as a starting point.
3. **Think about loops the way you think about onboarding an employee.** Define the job: what they check, how often, what output you want, and who to contact when something’s wrong. “Every Friday at 10 a.m., review all merged PRs and identify skills our agents are missing” is a job description. It’s also a loop prompt.
4. **Your agent can have its own agents. This is where loops get truly powerful.** The PR-review loop Claire built in Claude Code doesn’t just check PR status; it spins off dedicated subagents to babysit individual PRs until all merge checks are green. The skills loop in Codex identifies gaps and immediately spawns subagents to validate each new skill using a goal loop.
5. **Loops get expensive if you don’t write them carefully.** If the success criteria is vague or the validation threshold is too thin, the agent will keep running and keep charging without meaningful progress. Monitor both cost and output quality from day one.
6. **The morning briefing in Claude Cowork is a perfect loop starter.** A scheduled task that fires every morning, checks your calendar and email, and sends a summary to Slack is already a fully functional loop. No code required. From there, scaling up to PR reviews or skills identification in Claude Code or Codex is a natural next step.
7. **The power move is loops that generate their own subagent loops.** In the Codex demo, Claire’s weekly automation spawned two named subagents that each ran their own goal loops to validate skills in real time. The ceiling on loop-based automation is basically “how well can you define the job?” not “how complex is the engineering?”

#### Blog and detailed workflow walkthroughs from this episode:

How I AI: Designing AI Agent Loops in Claude Code and Codex: [https://www.chatprd.ai/how-i-ai/how-i-ai-designing-ai-agent-loops-in-claude-code-and-codex](https://www.chatprd.ai/how-i-ai/how-i-ai-designing-ai-agent-loops-in-claude-code-and-codex)  
↳ Build a Self-Improving AI to Generate Agent Skills in Codex: [https://www.chatprd.ai/how-i-ai/workflows/build-a-self-improving-ai-to-generate-agent-skills-in-codex](https://www.chatprd.ai/how-i-ai/workflows/build-a-self-improving-ai-to-generate-agent-skills-in-codex)  
↳ Automate Daily Pull Request Reviews with a Claude Code Agent: [https://www.chatprd.ai/how-i-ai/workflows/automate-daily-pull-request-reviews-with-a-claude-code-agent](https://www.chatprd.ai/how-i-ai/workflows/automate-daily-pull-request-reviews-with-a-claude-code-agent)

