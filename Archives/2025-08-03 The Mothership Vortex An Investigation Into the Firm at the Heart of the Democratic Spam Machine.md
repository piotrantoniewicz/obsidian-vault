---
type: Web
authors: '[[Adam Bonica]]'
url: >-
  https://data4democracy.substack.com/p/the-mothership-vortex-an-investigation?utm_medium=email&_hsenc=p2ANqtz-861itxo5o6AFEOVlgRA2g4dxgFUFuaSTKmm2W4kPfS9Btfm3MKgQJHGxIwrUB9KWrpMCpR09_mTF1m75QqXTgWqccIqvPo8L0lv-0oDQ17AqJHS-E&_hsmi=114881976&utm_content=114881976&utm_source=hs_email
published: 2025-08-03T00:00:00.000Z
created: 2026-03-19T00:00:00.000Z
tags:
  - digital-campaigning
  - fundraising
  - organizacje-społeczne
---


### How a single consulting firm extracted $282 million from a network of spam PACs while delivering just $11 million to actual campaigns.

The digital deluge is a familiar annoyance for anyone on a Democratic fundraising list. It's a relentless cacophony of bizarre texts and emails, each one more urgent than the last, promising that your immediate $15 donation is the only thing standing between democracy and the abyss.

The main rationale offered for this fundraising frenzy is that it's a necessary evil—that the tactics, while unpleasant, are brutally effective at raising the money needed to win. But an analysis of the official FEC filings tells a very different story. The fundraising model is not a brutally effective tool for the party; it is a financial vortex that consumes the vast majority of every dollar it raises.

We all have that one obscure skill we’ve inadvertently maxed out. Mine happens to be navigating the labyrinth of campaign finance data. So, after documenting the spam tactics in [a previous article](https://data4democracy.substack.com/p/the-most-valuable-thing-a-party-has), I told myself I’d just take a quick look to see who was behind them and where the money was going.

That "quick look" immediately pulled me in. The illusion of a sprawling grassroots movement, with its dozens of different PAC names, quickly gave way to a much simpler and more alarming reality. It only required pulling on a single thread—tracing who a few of the most aggressive PACs were paying—to watch their entire manufactured world unravel. What emerged was not a diverse network of activists, but a concentrated ecosystem built to serve the firm at its center: **Mothership Strategies.**

*(A repo with all the code needed to replicate this analysis is available for download [here](https://github.com/abonica/Mothership-Strategies-FEC-Analysis/blob/main/mothership_complete_api_analysis.R). A data visualization of the findings is at the bottom of this post.)*

### From Party Insiders to Extraction Engineers

To understand Mothership's central role, one must understand its origins. The firm was founded in 2014 by senior alumni of the Democratic Congressional Campaign Committee (DCCC): its former digital director, Greg Berlin, and deputy digital director, Charles Starnes. During their tenure at the DCCC, they helped pioneer the fundraising model that now dominates Democratic inboxes—a high-volume strategy that relies on emotionally charged, often hyperbolic appeals to compel immediate donations. This model, sometimes called "churn and burn," prioritizes short-term revenue over long-term donor relationships.

After leaving the DCCC, Berlin and Starnes effectively privatized this playbook, building a business around the party's most aggressive tactics and turning an internal strategy into a fundraising powerhouse for the Democratic Party—or so it might seem on the surface.

They became the operational heart of a sprawling nexus of interconnected political action committees, many of which they helped create and which now serve as their primary clients. These are not a diverse collection of grassroots groups; they are a tightly integrated network that functions primarily to funnel funds to Mothership. Their names are likely familiar from the very texts and emails that flood inboxes: Progressive Turnout Project, Stop Republicans, and End Citizens United to name a few.

The relationship between the firm and this network is cemented by blatant self-dealing. The most glaring example is End Citizens United. In 2015, just one year after founding their consulting firm, Mothership principals Greg Berlin and Charles Starnes also co-founded this PAC. It quickly became one of their largest and most reliable clients, a perfect circle of revenue generation that blurs the line between vendor and client.

### Follow the Money

The core defense of these aggressive fundraising tactics rests on a single claim: they are brutally effective. The FEC data proves this is a fallacy. An examination of the money flowing through the Mothership network reveals a system designed not for political impact, but for enriching the consultants who operate it.

To understand the scale of this operation, consider the total amount raised. Since 2018, this core network of Mothership-linked PACs has raised approximately **$678 million** from individual donors. (This number excludes money raised by the firm's other clients, like candidate campaigns, focusing specifically on the interconnected PACs at the heart of this system.) Of that total fundraising haul, **$159 million** was paid directly to Mothership Strategies for consulting fees, accounting for the majority of the **$282 million** Mothership has been paid by all its clients combined.

But the firm's direct cut is only part of the story. The "churn and burn" fundraising model is immensely expensive to operate. Sending millions of texts and emails requires massive spending on digital infrastructure. For instance, FEC filings show this network paid $22.5 million to a single vendor, Message Digital LLC, a firm that specializes in text message delivery.

The remaining hundreds of millions disappeared into a maze of self-reported categories: **$150 million** to consulting/fundraising, **$70 million** to salaries and payroll. There are some disbursements to what seem to be legitimate advocacy and organizing–for instance Progressive Turnout Project reports paying Shawmut Services **$19 million** for canvassing. However, most of the unclassifiable expenditures appear to be administrative costs or media buys that feed back into the fundraising machine itself.

![](https://substackcdn.com/image/fetch/$s_!HCO2!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abe0136-84a8-46e3-9501-4ffb780c1636_712x851.gif)

### How much of the money raised by these groups actually makes it to candidates and party committees?

After subtracting these massive operational costs—the payments to Mothership, the fees for texting services, the cost of digital ads and list rentals—the final sum delivered to candidates and committees is vanishingly small. My analysis of the network's FEC disbursements reveals that, at most, **$11 million** of the $678 million raised from individuals has made its way to candidates, campaigns, or the national party committees.

But here's the number that should end all debate:

This represents a fundraising efficiency rate of just **1.6 percent.**

Here's what that number means: for every dollar a grandmother in Iowa donates believing she's saving democracy, 98 cents goes to consultants and operational costs. Just pennies reach actual campaigns.

### Why the Party Looks the Other Way

This parasitic ecosystem could not thrive without the tacit approval of the Democratic establishment. The relationship between the Mothership network and the official party is not adversarial; it is deeply symbiotic.

The firm's founders are, as noted, alumni of the DCCC. They didn't just bring their contacts; they brought the "churn and burn" playbook, which was developed and honed inside the party's own campaign arm. They simply privatized the party's dirtiest tactics. This is not a rogue operation; it is an outgrowth.

While the network keeps most of the money it raises, it maintains the relationship by funneling a small portion back to the party's central committees. Of the paltry $11 million that makes it to campaigns, approximately half goes to the DNC, DCCC, and DSCC. This provides the party with a trickle of revenue and plausible deniability, allowing it to benefit from the fundraising without taking direct responsibility for the deceptive tactics. In return, the network gains a veneer of official legitimacy.

The infection runs deep. The firm's client list extends far beyond the PAC network to include the party's own heavyweights, like the **House Majority PAC**, and high-profile, establishment-backed candidates such as former DNC Chair Jaime Harrison. The distinction between the party and this network dissolves with one final fact: the Democratic establishment itself is a client, actively hiring the firm at the heart of the vortex.

### The Democratic Party Must Clean House

The evidence from federal election filings permits only one conclusion: the “necessary evil” defense is a lie. A fundraising model with a 1.6% efficiency rate is not a pragmatic fundraising strategy.

The financial waste, staggering as it is, pales beside the deeper damage. Every fabricated deadline, every manipulative text, every email screaming that democracy will end without your $15—each one burns through something more valuable than money: trust. The party that claims to defend democracy is systematically deceiving the very people who believe in it most.

None of this, as far as I can tell, is illegal. But since when is legality the bar? The question isn’t whether the party can tolerate this parasitic ecosystem. It’s whether it should. And the data screams the answer: when consultants pocket $282 million, it reveals a system working exactly as designed—just not for Democrats.

The prescription is simple. Cut ties with firms and any vendors that they do business with that treat donors as marks. Establish and enforce efficiency standards. Demand that fundraising operations deliver actual value to campaigns, not just commissions to consultants.

Most crucially: Recognize that Democratic donors deserve the same honesty the party demands from everyone else.

The party faces a choice. Continue feeding the vortex, or shut it down. Continue enriching consultants who’ve perverted its message, or reclaim its integrity. Continue treating supporters as ATMs, or start treating them as partners.

A party that prides itself on taking the high road doesn’t get to make exceptions for its own fundraising. Not when the cost is this clear. Not when the damage is this deep.

The numbers don’t lie. The Mothership vortex has consumed enough.

Shut it down.

![](https://substackcdn.com/image/fetch/$s_!2LAX!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb50bf6d0-0af7-425a-a0a6-7bcb0a8c1f80_2958x13524.png)

---
