---
type: "Web"
authors: "[[Lenny Rachitsky]]"
url: "https://www.lennysnewsletter.com/p/this-week-on-how-i-ai-the-power-users?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-01-12
created: 2026-05-12
tags:
---


![](https://substackcdn.com/image/fetch/$s_!gWeJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F361d81ef-7faf-4d8e-8028-5d5e03432a9a_2329x551.png)

Every Monday, host Claire Vo shares a 30- to 45-minute episode with a new guest demoing a practical, impactful way they’ve learned to use AI in their work or life. No pontificating—just specific and actionable advice.

### “A full software engineering teammate”: OpenAI product lead on getting the most out of Codex

![](https://www.youtube.com/watch?v=xeZDHGjG5zM)

![](https://substackcdn.com/image/fetch/$s_!zPc2!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e8148ee-9241-4d77-a1c4-85ace618ceef_1512x210.png)

**Brought to you by:**

> **[Brex](https://brex.com/howiai)** —The intelligent finance platform built for founders
> 
> **[Graphite](https://graphitedev.link/howiai)** —Your AI code review platform

---

**[Alexander Embiricos](http://linkedin.com/in/embirico)**, the product lead for Codex at OpenAI, shares how AI coding agents are actually used in production—from simple fixes to shipping full apps. He breaks down the workflows that make Codex effective at scale, including structured planning with Plans.md, parallel development using Git worktrees, and automated code review across nearly every OpenAI repo. The conversation covers how Codex users dramatically outperformed non-users internally, how OpenAI built the Sora Android app in just 28 days, and what changed with the release of GPT-5.2. We also explore why context matters more than clever prompts, why the real bottleneck is increasingly human judgment rather than code generation, and how AI tools are evolving from standalone destinations into deeply embedded teammates inside existing workflows.

### Detailed workflow walkthroughs from this episode:

• 3 Advanced Codex Workflows for Faster, Smarter Development with OpenAI’s Alex Embiricos: [https://www.chatprd.ai/how-i-ai/advanced-codex-workflows-with-openai-alex-embiricos](https://www.chatprd.ai/how-i-ai/advanced-codex-workflows-with-openai-alex-embiricos)

• How to Use OpenAI Codex to Understand and Modify a New Codebase: [https://www.chatprd.ai/how-i-ai/workflows/how-to-use-openai-codex-to-understand-and-modify-a-new-codebase](https://www.chatprd.ai/how-i-ai/workflows/how-to-use-openai-codex-to-understand-and-modify-a-new-codebase)

![How to Use OpenAI Codex to Understand and Modify a New Codebase](https://substackcdn.com/image/fetch/$s_!Zf3m!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02145d6b-979d-4dee-b09c-2b64f48172ec_1376x768.png)

How to Use OpenAI Codex to Understand and Modify a New Codebase

• How to Architect Complex Software Projects with OpenAI’s Plans.md Technique: [https://www.chatprd.ai/how-i-ai/workflows/how-to-architect-complex-software-projects-with-openai-s-plans-md-technique](https://www.chatprd.ai/how-i-ai/workflows/how-to-architect-complex-software-projects-with-openai-s-plans-md-technique)

![How to Architect Complex Software Projects with OpenAI's Plans.md Technique](https://substackcdn.com/image/fetch/$s_!VLI7!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc11b1401-e550-4fed-8682-cd6f3fbe80ab_1376x768.png)

How to Architect Complex Software Projects with OpenAI's Plans.md Technique

• How to Manage Parallel Development with AI using Git Worktrees and Codex: [https://www.chatprd.ai/how-i-ai/workflows/how-to-manage-parallel-development-with-ai-using-git-worktrees-and-codex](https://www.chatprd.ai/how-i-ai/workflows/how-to-manage-parallel-development-with-ai-using-git-worktrees-and-codex)

![How to Manage Parallel Development with AI using Git Worktrees and Codex](https://substackcdn.com/image/fetch/$s_!of22!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef219ef0-ec10-47e8-8468-4891fe64811b_1376x768.png)

How to Manage Parallel Development with AI using Git Worktrees and Codex

### Biggest takeaways:

1. **The productivity gap between power users and everyone else is significant.** When roughly half of OpenAI was using Codex, those users were producing about 70% more PRs than non-users. Now virtually all technical staff use it: “We’re now at the point where nearly all of technical staff is using Codex constantly.”
2. **Automated code review has become OpenAI’s most widely adopted Codex feature.** It’s enabled on nearly every repo at the company and reviews almost all PRs: “The hit rate on these is really high. We built this feature so that it only points out issues that it’s very confident in, because human attention is so scarce, we really want to protect it.”
3. **Structured planning is critical for complex tasks.** OpenAI published a blog post about effective planning with AI that includes a meta-plan template (Plans.md) that helps Codex create thorough, milestone-based plans. This approach was key to building the Sora Android app in just 28 days: “With coding agents, it doesn’t get easier, but you just move way faster.”
4. **Git worktrees are a powerful way to parallelize AI coding tasks.** Instead of running conflicting changes in the same codebase or creating multiple copies manually, use Git worktrees: “Git has this really nice affordance called a worktree, which basically lets one Git instance track multiple copies of the codebase.” You can even ask Codex to create and manage these worktrees for you.
5. **The new GPT-5.2 model can solve problems previous models couldn’t—often with significantly less thinking time.** Alex cites an example of a bug that no previous model could fix but 5.2 “fought for 37 minutes and was like, ‘This is the bug.’ And then in fact, that was the bug and he got the bug fixed.” The model can also deliver strong results with significantly less thinking time than previous versions.
6. **The limiting factor in AI productivity is increasingly about human direction, not code generation.** “Now that we can just have ubiquitous code and we can basically prototype things trivially, the hard parts become deciding what actually should make it in, thinking what a product should do, knowing a customer actually.”
7. **Context is everything when prompting AI.** Alex recommends: “I don’t usually ask for things from the agent without giving context. So I’ll say, ‘Hey, I want you to change this UI from this to this so that users do this’ or ‘because we don’t want people to be confused about XYZ.’” He believes product managers often make the best prompters because they’re used to not being the expert.
8. **Being polite to AI protects your own humanity.** While not an official OpenAI stance, Alex believes: “I think it’s important to be polite to everyone. And I think that if you start not being polite to chat, I think it can wear off on you. And you just start not being polite to other people in your life.”
9. **The future of AI tools is contextual integration rather than separate destinations.** Features like side chat in Atlas and Codex in your IDE represent a shift toward AI understanding your environment: “For me, the idea of an agent that I don’t have to map myself to its world is really powerful. So side chat is that. Codex is that too, right? You launch it in a codebase and it’s in your environment. You don’t have to go to it.”
10. **The harness (interface to the model) matters as much as the model itself.** As models evolve rapidly, the harness needs to adapt to get the most out of each new capability: “Every time we ship a model, engineers from the Codex team will test it, think about it, talk to the research team. They’re working super-closely together to figure out how to make the most out of the model.”

▶️ Listen now on **[YouTube](https://youtu.be/xeZDHGjG5zM) | [Spotify](https://open.spotify.com/episode/6RNqTaOb5ly3zgQCGB23fE) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/a-full-software-engineering-teammate-openai-product/id1809663079?i=1000744804434)**

---

If you’re enjoying these episodes, reply and let me know what you’d love to learn more about: AI workflows, hiring, growth, product strategy—anything.

Catch you next week,  
Lenny

*P.S. Want every new episode delivered the moment it drops? Hit “Follow” on your favorite podcast app.*