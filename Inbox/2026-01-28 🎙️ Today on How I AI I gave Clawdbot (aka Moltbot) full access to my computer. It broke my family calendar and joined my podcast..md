---
type: "Web"
authors: "[[Lenny Rachitsky]]"
url: "https://www.lennysnewsletter.com/p/today-on-how-i-ai-i-gave-clawdbot?utm_source=substack&utm_medium=email&utm_campaign=email-restack-comment&r=4zdnrk&triedRedirect=true"
published: 2026-01-28
created: 2026-05-12
tags:
---


![](https://substackcdn.com/image/fetch/$s_!gWeJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F361d81ef-7faf-4d8e-8028-5d5e03432a9a_2329x551.png)

Clawdbot is exploding across tech Twitter and Hacker News, with builders racing to plug autonomous agents into their lives before anyone really knows what they’re doing. Claire jumped in at the peak of the hype to find out what’s real, what’s risky, and what happens when you actually let one of these agents run loose on your computer.

![](https://www.youtube.com/watch?v=fcFOYzMeG7U)

![](https://substackcdn.com/image/fetch/$s_!teZk!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F86412ac6-eacc-419e-84e5-50f4b8a572cd_3350x989.png)

Brought to you by Lovable —Build apps by simply chatting with AI

**Listen on [YouTube](https://youtu.be/fcFOYzMeG7U), [Spotify](https://open.spotify.com/episode/5s7j0DP1vPFaKm4Z7Vcwyd?si=cQt8S0R4TxyZ6RJAJxryPA), or [Apple Podcasts](https://podcasts.apple.com/us/podcast/i-gave-clawdbot-aka-moltbot-access-to-my-computer-calendar/id1809663079?i=1000747009405)**

#### Detailed workflow walkthroughs from this episode:

**• How I AI: My 24 Hours with Clawdbot (aka Moltbot)—3 Workflows for a Powerful (and Terrifying) AI Agent:** [https://www.chatprd.ai/how-i-ai/24-hours-with-clawdbot-moltbot-3-workflows-for-ai-agent](https://www.chatprd.ai/how-i-ai/24-hours-with-clawdbot-moltbot-3-workflows-for-ai-agent)

**• How to Securely Set Up and Configure an Open-Source AI Agent like Clawdbot:** [https://www.chatprd.ai/how-i-ai/workflows/how-to-securely-set-up-and-configure-an-open-source-ai-agent-like-clawdbot](https://www.chatprd.ai/how-i-ai/workflows/how-to-securely-set-up-and-configure-an-open-source-ai-agent-like-clawdbot)

![How to Securely Set Up and Configure an Open-Source AI Agent like Clawdbot](https://substackcdn.com/image/fetch/$s_!HiE4!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F497fe3ed-8fcc-41a9-a89f-85e286555375_1376x768.png)

How to Securely Set Up and Configure an Open-Source AI Agent like Clawdbot

**• How to Safely Delegate Calendar Scheduling to an AI Agent:** [https://www.chatprd.ai/how-i-ai/workflows/how-to-safely-delegate-calendar-scheduling-to-an-ai-agent](https://www.chatprd.ai/how-i-ai/workflows/how-to-safely-delegate-calendar-scheduling-to-an-ai-agent)

![How to Safely Delegate Calendar Scheduling to an AI Agent](https://substackcdn.com/image/fetch/$s_!D559!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F834740be-57c9-470f-ae42-cf477a9410d2_1376x768.png)

How to Safely Delegate Calendar Scheduling to an AI Agent

**• Automate Market Research on Reddit Using an AI Agent:** [https://www.chatprd.ai/how-i-ai/workflows/automate-market-research-on-reddit-using-an-ai-agent](https://www.chatprd.ai/how-i-ai/workflows/automate-market-research-on-reddit-using-an-ai-agent)

![Automate Market Research on Reddit Using an AI Agent](https://substackcdn.com/image/fetch/$s_!Ihbq!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2dc61e4-11a4-40bb-8599-690304a0b26c_1376x768.png)

Automate Market Research on Reddit Using an AI Agent

#### Biggest takeaways:

1. **Security should be your top concern.** Claire created a separate user account on her laptop for Clawdbot, gave it its own email address rather than access to hers, and created a limited vault in 1Password. When it requested broad permissions to her Google account (email, contacts, files), she pushed back and limited access to just calendar viewing. These precautions are essential, since Clawdbot has access to your file system.
2. **Prompting matters more than ever with autonomous agents.** Small differences in how you phrase requests can lead to dramatically different outcomes with Clawdbot. When Claire asked it to email podcast guests, she didn’t explicitly say “draft an email for my review,” resulting in immediate sending. With traditional AI tools, this wouldn’t matter as much, but autonomous agents require more precise instructions.
3. **Clawdbot is biased toward impersonation rather than acting as an assistant.** When asked to email podcast guests about rescheduling, it sent emails as Claire rather than identifying itself as her assistant—despite Claire explicitly giving it its own identity. This suggests that the default behavior is impersonation, which creates significant risks if not carefully managed.
4. **The best use case might be asynchronous research tasks rather than real-time assistance.** Claire’s most successful experience was asking Clawdbot to research Reddit for feedback about her product. The AI produced a well-organized report with key insights and reference links, exactly what she’d expect from a human research assistant.
5. **The future of personal AI assistants will require both better interfaces and better security models.** While Clawdbot demonstrates the potential of autonomous agents, it also highlights the challenges. The ideal solution would combine the accessibility of consumer products with proper security boundaries, clear identity management, and reliable performance—a combination that doesn’t yet exist in the market.
6. **The “one-line install” is misleading. Expect to spend hours on setup if you’re not a developer.** Claire spent two hours installing dependencies before she could even run the one-line installer. She had to upgrade Node, install Homebrew, install Xcode, and update NPM manually. This makes Clawdbot firmly in the “hacker/tinkerer” category rather than consumer-ready.
7. **The latency problem makes Clawdbot feel slow compared with other AI tools.** Unlike ChatGPT or Claude, which provide real-time feedback as they work, Clawdbot often goes silent while spinning up subagents to complete tasks. This creates a frustrating user experience where you’re not sure if it’s working or has crashed. Claire had to specifically ask for acknowledgment messages, which it still didn’t consistently provide.
8. **Clawdbot struggles with basic time concepts despite its advanced capabilities.** In a particularly frustrating episode, Clawdbot placed all family calendar events on the wrong day and couldn’t set recurring events. When Claire pointed this out, it claimed it was “mentally calculating” which day of the week each date falls on—a bizarre explanation for an AI.
9. **Voice plus text messaging creates a surprisingly natural interface for an AI assistant.** One of Clawdbot’s strengths is its ability to receive voice messages via Telegram and respond with either text or voice. Claire found this particularly useful while shopping at Target, allowing her to multitask while managing the AI. The ability to instantly add this capability without complex setup demonstrates the power of self-learning agents.
10. **Clawdbot is not just for Mac Minis—it can run on any machine or in the cloud.** Despite what many believe, you don’t need special hardware to run Clawdbot. Claire ran it on an old MacBook Air, and you can even set it up for $5 on Amazon Web Services. The key is understanding that while it runs locally, it doesn’t require fancy hardware unless you’re running massive local models.

▶️ Listen now on **[YouTube](https://youtu.be/fcFOYzMeG7U) | [Spotify](https://open.spotify.com/episode/5s7j0DP1vPFaKm4Z7Vcwyd?si=cQt8S0R4TxyZ6RJAJxryPA&nd=1&dlsi=6f42114d1b5547fe) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/i-gave-clawdbot-aka-moltbot-access-to-my-computer-calendar/id1809663079?i=1000747009405)**

---

If you’re enjoying these episodes, reply and let me know what you’d love to learn more about: AI workflows, hiring, growth, product strategy—anything.

Catch you next week,  
Lenny

*P.S. Want every new episode delivered the moment it drops? Hit “Follow” on your favorite podcast app.*