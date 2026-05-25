---
type: "Web"
authors: "[[Lenny Rachitsky]]"
url: "https://www.lennysnewsletter.com/p/how-i-ai-html-is-the-new-markdown?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-05-18
created: 2026-05-20
tags:
  - "vibe-coding"
  - "narzędzia-AI"
  - "prompt-engineering"
---


![](https://substackcdn.com/image/fetch/$s_!gWeJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F361d81ef-7faf-4d8e-8028-5d5e03432a9a_2329x551.png)

### HTML is the new Markdown: How Anthropic engineers are building with Claude Code | Thariq Shihipar

![](https://www.youtube.com/watch?v=Qrpm7E80wQ0)

Listen now on **[YouTube](https://youtu.be/Qrpm7E80wQ0) • [Spotify](https://open.spotify.com/episode/6Wtk2CxwbHUwYGAe9HWgYT) • [Apple Podcasts](https://podcasts.apple.com/us/podcast/html-is-the-new-markdown-how-anthropic-engineers-are/id1809663079?i=1000768383813)**

![](https://substackcdn.com/image/fetch/$s_!xTLQ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3c60092-622d-4571-be3b-48ef6c66d29b_1600x114.png)

> **Brought to you by:**
> 
> - **[Celigo](https://celigo.com/howIAI)** —Intelligent automation built for AI
> - **[Persona](https://withpersona.com/lp/howiai)** —Trusted identity verification for any use case

**Thariq Shihipar** is an engineer on Anthropic’s Claude Code team. In this episode (recorded live at Anthropic’s Code with Claude event), Thariq shows how he uses HTML artifacts to plan projects, create interactive specs, build throwaway micro-apps, and maintain living design systems that help humans stay in the loop as agents do more of the work. He also explains why engineers are becoming “compute allocators,” why most AI-generated tokens won’t end up in production, and how richer interfaces can lead to better products.

#### Biggest takeaways:

1. **HTML has become the superior format for communicating with AI agents, replacing Markdown for planning and specs.** While Markdown was popular because it’s both human- and machine-readable, HTML offers far richer expression—interactive elements, visual mockups, scrollable sections, and better information density. As Claude’s context windows have expanded and plans have grown to thousands of lines, HTML makes it actually possible to engage with the content rather than just skimming or ignoring it entirely.
2. **Engineers are becoming “compute allocators” rather than code writers.** When Claude can run for eight hours on a single task, you’re really deciding how to spend $500 of compute. The critical skill is no longer writing code; it’s deciding what’s worth building, defining the boundaries of what you need to know, and staying in sync with the agent throughout the process. This happens primarily in the spec and planning phase, making that work more important than ever.
3. **You can build custom, throwaway UIs for editing specific parts of your plans.** Thariq demonstrates this by taking a data visualization rules table from his implementation plan and asking Claude to create an ideal interface for editing just that section. The result is a beautiful, gamified UI that makes engaging with the content actually enjoyable. This “micro software on top of micro software” approach means you can have the perfect tool for every specific problem, then discard it when you’re done.
4. **The future of agent output isn’t more text. It’s more readable interfaces.** Thariq says he stopped reading thousand-line Markdown plans and started asking Claude to edit them instead, which made him less involved in the work. HTML changed that: by turning plans into visual, scrollable, interactive artifacts, Claude makes the output easier to engage with, critique, and improve. The lesson isn’t to read less. It’s to make the work legible enough that you actually want to read it.
5. **Living design systems in HTML are more effective than traditional design tools.** Instead of pointing Claude at a Figma file or GitHub repo, Thariq maintains an HTML file that represents his entire design system: colors, typography, spacing, components. This compressed understanding can be passed around to any project, and Claude can extract design systems from existing codebases and encode them in HTML. It’s both human-readable and machine-readable, with no tradeoff between the two.
6. **The best prompts give Claude enough direction but leave room for creativity.** Thariq’s prompts are remarkably simple: “Create an HTML file with a plan. Help me visualize. Include excerpts, mockups, code, whatever is needed to give me maximum context.” The key is the ending—“whatever is needed”—which signals trust and gives Claude permission to make decisions. Over-constraining with elaborate system prompts often produces worse results than simple, trusting instructions.
7. **Only about 1% of the tokens Thariq generates go into production code.** The vast majority go into dashboards, custom interfaces, weekly status updates, and tools for understanding what he wants to build. This is what abundance looks like—when tokens are cheap, you can afford to make everything you interact with beautiful and tailored to your specific needs. The hope is that this richness in the process translates into better final products.
8. **Test verification is not the same as testing.** This is a nuanced point that Thariq says deserves its own podcast episode, but the core idea is that traditional unit tests are being replaced by verification rubrics, managed agents checking outcomes, and Claude recording videos of what it did. The testing landscape is evolving rapidly, and teams need to think beyond conventional approaches.
9. **Just-in-time documentation in whatever format works is better than centralized, templated systems.** When creating content is nearly free and AI can find anything, the old anxieties about “source of truth” and standardized templates matter less. What matters is the quality of the ideas and whether the documentation helps you build better products. Thariq sends his manager weekly HTML status updates because they’re more likely to actually get read than Markdown or plain text.
10. **Being nice to Claude probably produces better outputs, and it definitely creates a better world.** While no one has run a rigorous A/B test, Thariq prefers to build the world where being kind to AI produces better results. When you’re stern with models, their reasoning gets sad (“the user is right to be disappointed in me”), and that’s not the interaction pattern anyone wants to normalize. Treat Claude like a colleague you respect, not a tool you command.

#### Blog:

How I AI: Thariq Shihipar on Replacing Markdown with HTML for AI-Powered Development: [https://www.chatprd.ai/how-i-ai/claude-code-anthropic-thariq-shihipar-on-replacing-markdown-with-html](https://www.chatprd.ai/how-i-ai/claude-code-anthropic-thariq-shihipar-on-replacing-markdown-with-html)

#### Detailed workflow walkthroughs:

**↳** Generate a Living HTML Design System with AI for UI Consistency: [https://www.chatprd.ai/how-i-ai/workflows/generate-a-living-html-design-system-with-ai-for-ui-consistency](https://www.chatprd.ai/how-i-ai/workflows/generate-a-living-html-design-system-with-ai-for-ui-consistency)

**↳** Build Disposable Micro-Apps with AI to Edit Complex Plans: [https://www.chatprd.ai/how-i-ai/workflows/build-disposable-micro-apps-with-ai-to-edit-complex-plans](https://www.chatprd.ai/how-i-ai/workflows/build-disposable-micro-apps-with-ai-to-edit-complex-plans)

**↳** Create Interactive HTML Project Plans with AI for Better Visualization: [https://www.chatprd.ai/how-i-ai/workflows/create-interactive-html-project-plans-with-ai-for-better-visualization](https://www.chatprd.ai/how-i-ai/workflows/create-interactive-html-project-plans-with-ai-for-better-visualization)

---

If you’re enjoying these episodes, reply and let me know what you’d love to learn more about: AI workflows, hiring, growth, product strategy—anything.

Catch you next week,  
Lenny

*P.S. Want every new episode delivered the moment it drops? Hit “Follow” on your favorite podcast app.*