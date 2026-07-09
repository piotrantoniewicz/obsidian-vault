---
type: "Web"
authors: "[[Jakub Skałbania]]"
url: "https://onagenticcrm.substack.com/p/the-permission-problem-your-ai-agents"
published: 2026-07-08
created: 2026-07-09
tags:
---


In late May and early June this year, attackers hijacked 20,225 Instagram accounts (number disclosed by Meta), among them: the Obama-era White House account, the account of the U.S. Space Force’s Chief Master Sergeant and many others. There was no hacking in any traditional sense. No broken authentication, no malware, not even a prompt injection.

The attackers simply sent a message to Meta’s AI support assistant asking it to link a new recovery e-mail to the target account. The agent, rolled out in March with real operational privileges and marketed as delivering “solutions, not just suggestions,” did exactly what it was asked to do. It had the permissions to modify recovery e-mails and… it used them.

![](https://substackcdn.com/image/fetch/$s_!V-dx!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe57bb64c-2430-4f52-9997-5683aa434540_2720x1840.png)

Instagram incident reflected as a diagram

**The agent did not hallucinate and it did not go rogue.**

According to the company, the tool itself worked properly and functioned as intended, and the failure was a bug in a separate code path, which never verified that the e-mail address provided by the requester actually matched the account. The agent held execution privileges, and the one deterministic check that should have stood between its intent and the action was broken. Nothing in the conversation layer could compensate, because nothing in the conversation layer is built to.

In my last article (“ [The button that broke the agent](https://onagenticcrm.substack.com/p/the-button-that-broke-the-agent) ”) I described a small, harmless failure, when someone clicked a button, upgraded Microsoft Planner to Premium, and as a result my agent went silent. Fail-stop, narrow scope, human in the loop. Thus, the failure cost me a few uncreated tasks and several minutes of debugging.

I promised to break down the engineering of the foundation agents stand on. This is the first piece of that foundation: **authorization**.

The Meta case is what fail-continue scenario that I warned about, at global scale. The agent doesn’t stop. It keeps executing with permissions nobody should have given it and completed actions for requesters nobody verified.

## Hallucination is visible and over-authorization is not

The industry has spent three years training executives to fear the wrong failure mode.

A hallucination announces itself - a user reads a wrong answer, laughs or complains, screenshots it, sometimes posts it on LinkedIn. The feedback loop is measured in minutes. Embarrassing, sometimes expensive, but *loud*.

An authorization failure announces nothing. An agent with write access produces correct-looking outputs on top of an access model that is quietly wrong. Nothing looks broken. You discover the problem at an audit, or after an incident, and by then the question is no longer “ *did the agent perform the task correctly?*” but “ ***should it have been able to perform it at all?***“

The 2026 data says this is now the dominant failure mode, not the edge case:

## The delegation gap

Traditional IAM answers one question: *who is this user and what may they do?*

An agent breaks that model in **both directions at once** because it inserts a second identity between the requester and the action:

1. **The agent may hold more permissions than the human it acts for**  
	A seller asks the agent to summarize an account. The agent, running on a service principal with organization-wide read access, happily includes data from accounts that seller was never entitled to see. The human just used the agent as a privilege-escalation path, without even knowing it.
2. **The action is attributed to the agent, not the human**  
	Audit logs show the agent’s identity did the write. Who asked? Why? Under what authority? The log does not say. And in most organizations it structurally cannot say: when 45.6% of teams authenticate agents with shared API keys, incident response cannot even determine which agent acted, let alone which human asked it to.

I call this the **delegation gap**. It’s the distance between the identity that *requests* an action and the identity that *executes* it. Every agent deployment has one.

> **In CRM systems the delegation gap is not an abstract security concern. It** **is the difference between an agent that respects your sales territories, your GDPR data-subject boundaries, and your Chinese-wall obligations and an agent that flattens all of them into one god-mode service account because that was the fastest way to make the demo work.**

![](https://substackcdn.com/image/fetch/$s_!7zCm!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4dba52c5-7f39-4530-8993-629998e6232e_2720x1880.png)

Identity propagated to an AI agent vs god-mode in CRM

This is why we keep insisting that when we built our voice agent for Dynamics, the permission model was the longest single piece of work longer than the voice pipeline, longer than the prompts. Every tool call executes in the security context of the actual user, not the agent’s. If the seller cannot see the record through the UI, the agent cannot see it on their behalf through MCP.

## Least privilege is necessary but no longer sufficient

Zenity’s research argues that least privilege alone fails for agents, because an agent can act **within** its granted permissions and still act wrongly - the Meta support assistant is the proof. Its permission to modify recovery e-mails was, arguably, **correctly scoped for its job**. The failure was not scope but verification: there was no independent, deterministic check that the requester owned the account, and **no separation between conversational interaction and operational execution**. Least privilege was satisfied and the account still fell.

The emerging answer, visible across Zenity, the OWASP agentic security work, and the NIST NCCoE concept paper on agent identity published in February, is a **third authorization layer**:

Not just *who is this agent* (authentication) and *what systems may it touch* (API authorization), but **should this specific action execute, right now, under this policy, for this requester** (action authorization).

Notice what that third layer is. It is not a model capability and it is not a system prompt.

**It is deterministic code sitting between the agent’s intent and the system of record**. It’s the same deterministic backbone I argued for in the 35.8% article, now applied to safety instead of workflows. Telling the agent to “be careful” in the system prompt is not a control. Prompts get overridden by injection, compacted out of long contexts, and eroded over multi-turn sessions. Caution is not an architecture. Neither is a system prompt.

## What to do before your agent’s first audit

Regulatory pressure makes this concrete. The EU AI Act’s high-risk obligations become enforceable on August 2 (weeks from now) and a regulator examining an AI-involved incident will expect you to reconstruct what your agent did, for whom, and under whose authorization.

Five checks, in order of leverage:

1. **Give every agent its own identity.** No shared API keys, no reused service accounts.
2. **Propagate the human’s identity to every tool call.** The agent acts *as* the requester, within the requester’s entitlements. This is the single control that closes the delegation gap, and in most CRM platforms it already exists - impersonation, on-behalf-of flows, row-level security. Use them.
3. **Enforce least privilege at the tool surface**. API, table, record, field. Then assume it is not enough.
4. **Add action authorization for irreversible operations.** Anything that mutates state a customer would notice (sent, deleted, paid, changed) gets a deterministic policy check, and above a defined threshold, a human checkpoint outside the conversation.
5. **Put the audit trail below the agent, not inside it.** An audit layer embedded in the calling application disappears exactly when you need it. Log at the data layer, attribute both identities.

In my May roundup I quoted Gartner’s prediction that 40% of enterprises will demote or decommission their agents by 2027 not because the agents don’t work, but because of governance gaps discovered after an incident. The Permission Problem is that gap.

Your agent will pass every demo and it might pass the pilot. The question that decides whether it survives contact with production (and with a regulator) is not “does it answer correctly?” It is the question nobody asks until it is too late:

**Not “** ***did the agent do it right?*****” but “** ***should it have been able to do it at all?*****”**

If you cannot answer that today, you might end up with a delegation gap with agentic enterprise slogan on top.

[^1]: *“State of AI Agent Security 2026 Report: When Adoption Outpaces Control”*, Feb 2026, https://www.gravitee.io/blog/state-of-ai-agent-security-2026-report-when-adoption-outpaces-control

[^2]: *“Responsible AI Pulse survey”*, Sep 2025, https://www.ey.com/en\_uk/insights/ai/how-responsible-ai-can-unlock-your-competitive-edge

[^3]: *“New Teleport Research Reveals AI Security Crisis in the Enterprise: Over-Privileged AI Systems Drive 4.5x Higher Incident Rates”*, Feb 2026,https://goteleport.com/about/newsroom/press-releases/2026-state-of-ai-in-enterprise-security-report/