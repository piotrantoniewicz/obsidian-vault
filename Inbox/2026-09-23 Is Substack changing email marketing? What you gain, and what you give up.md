---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/is-substack-changing-email-marketing-what-you-gain-and-what-you-give-up?utm_medium=email&_hsenc=p2ANqtz-9dalVvg7IZi86cgBe9A686fULrVF-su0RhQKstFR85a-ase1xah4Y85G-zEWr9AUDPdvqlnQ0vAC5u-GRcpN71idbJkhAmRrTNRzis8yKhHP7-2MI&_hsmi=147074739&utm_content=146701193&utm_source=hs_email"
published: 2026-09-23
created: 2026-10-01
tags:
---


Substack keeps coming up. In my inbox, in client conversations, in the should-we-be-on-there question that lands about once a fortnight. There are now something like 1.8 MILLION active creators on it, and it has quietly stopped being a writing tool and turned into a social network with email attached.

Two separate conversations are happening about it and people keep merging them, which is why the answers people get are so unsatisfying.

The first is technical. What happens to your email when you publish on infrastructure you do not control, cannot audit and cannot fix.

The second is strategic, and it is the more interesting one. What a newsletter even is now, who people want to hear from, and why so many brand newsletters are ignored while individual creators are building readerships people look forward to.

Both matter, they have completely different answers, and my short version is this: Substack is brilliant for publishing and rubbish for email marketing, and those are not the same activity (a lot of people are about to argue with me here, and that is fine).

## Part technical layer

## What you are doing when you send from Substack

### You are borrowing somebody else’s domain

By default, Substack newsletters are sent from a substack.com address. Everything on the sending side is handled by the platform, which is a large part of the appeal, because nobody starting a newsletter wants to think about DNS records.

Which means your sender reputation is not yours. You are inheriting the aggregate behaviour of every other publication on the platform, so your inbox placement is partly a function of what 1.8 million other writers are doing with their sending. Let that sit for a second.

- The upside is real, so let me be fair about it. Substack operates at enormous scale with people whose job is deliverability, and that is a better setup than almost any individual creator would build alone. For somebody who would otherwise be sending from a badly configured domain with no authentication, it is an improvement.
- The downside is that you have no visibility and no control. You cannot audit it, you cannot influence it, you cannot fix it. If the shared reputation dips, yours dips with it, and the only action available to you is waiting. For somebody who does this for a living, that is a deeply uncomfortable sentence to type.

### The custom domain does less than people assume

Substack does support custom domains. You can connect one you already own or buy one through the platform, and it will handle the DNS configuration and the apex redirect.

What it does not do is hand you control of your email authentication, and that distinction gets missed constantly.

- You cannot edit every DNS record. Which means you cannot configure SPF, DKIM and DMARC with the precision you would need to properly own your deliverability. You get whatever authentication setup the platform provides.
- Custom domains do not use Substack's built-in email authentication. So the arrangement is worse than it sounds, because you take on responsibility for configuring it yourself while still not having full control of the records. Worst of both worlds.
- The sending server is still theirs. A custom domain changes the address on the envelope. It does not move you off shared infrastructure, and if that infrastructure has a bad week, your domain is affected by association.
- And there are practical costs to switching to one. If you ever revert to the Substack URL, every custom domain link breaks, you lose whatever SEO you built, you cannot redirect back, and Substack stops featuring your publication as prominently on its own network.

### The thing you cannot export

Now the part that matters most, and the part almost everybody gets wrong in both directions.

You can export your list. Settings, export, and you get a CSV with your subscribers, your posts and your stats, ready to load into any other platform. Substack does not lock your audience in, and anybody telling you otherwise is wrong.

What you cannot export is your sender reputation, and that is the bit that matters.

Every open, click and reply your subscribers have generated over the last two years has been building a history attached to substack.com, not to you. So the day you move that list somewhere else, Gmail, Microsoft and Yahoo see a sender they have no history with, emailing people who have never had anything from that address before.

Your audience is portable, your reachability is not, and the second one decides whether the first one ever sees you again.

- You will be warming from zero, on a list that already knows you. A strange and expensive place to be, because the humans recognise you and the machines do not, and only one of those gets a vote on whether the email arrives.
- The export itself can be lossy. One writer documented exporting just over four thousand subscribers, getting around 3,749 in the CSV, and ending up with roughly 3,100 after import. Several hundred people disappeared somewhere between the two platforms.
- Plan a move off Substack like a domain migration. Because functionally that is what it is. Tell people before you go, start with your most engaged readers, ramp slowly, and expect the first few sends to underperform badly.

### Who Substack suits, and who it does not

The answer is not the same for everybody, so let me split it.

- It suits creators and writers whose business is the publication. One audience, one relationship, no commercial email programme sitting alongside it, no segmentation requirements, and no appetite for managing infrastructure. Substack removes a genuine barrier and the discovery network is a real advantage.
- It does not suit a business with a real email programme. If email is a revenue channel, if you need lifecycle automation, segmentation, exclusions, transactional sending or any control over your reputation, Substack is the wrong tool and it was never trying to be the right one.
- And the version that worries me most is running BOTH. A business publishing on Substack while also sending marketing email from its own domain is teaching its audience two different sender identities, splitting the engagement signals between them, and building reputation somewhere it does not own while neglecting the place it does. I see this more than you would think.

## The bigger shift

## Newsletters are not dead, the word is just doing too much work

Now the interesting half, because the technical stuff is a trade-off and this is a genuine change in how people relate to email.

### The word is the problem

Ask most businesses what their newsletter is and you get a container. Company news nobody asked for, three product updates, a round-up of blogs, an event promotion, a job advert, and something about the office move.

That is not a newsletter, it is an internal status report sent externally, and it exists because somebody decided the business should HAVE a newsletter and then worked out what to put in it. Completely the wrong way round.

People do not hate newsletters. People subscribe to loads of them voluntarily and read them properly. What they hate is the container, and the container has been wearing the name for so long that the name has taken the blame for it.

### What changed: the relationship moved to the person

The shift I keep seeing, and the thing Substack has accelerated rather than created.

People increasingly subscribe to a PERSON rather than to an organisation, and the subscription is an extension of a relationship that already exists somewhere else. You listen to Mel Robbins's podcast for a year, you know her voice, you know what she is like, and signing up to hear from her by email is a tiny step rather than a leap of faith. Same thing with me - if you follow me on LinkedIn and you like the way I think about email, subscribing to RE:markable is barely a decision.

Which explains something that looks odd from the outside. Identical content performs differently depending on whose name is on it, because recognition is processed before content. Your sender name does more work than your subject line ever will, and a name somebody already has a relationship with does the most work of all.

- The creator has a voice, and the voice is the product. You can tell who wrote it without checking, which is the thing most brand newsletters have carefully edited out of themselves.
- The relationship predates the subscription. So the first email arrives to somebody who already knows what they signed up for, rather than to a stranger who filled in a form to get a discount.
- And the promise is narrow. One person, one subject, one perspective. A brand newsletter promising updates from across the business is promising nothing anybody wanted.

### So are brand newsletters finished?

No, and I will happily argue with anybody who says otherwise.

Brand newsletters work, and the ones that work share a shape. There is a person behind it, with a name and a voice, even if the brand is on the envelope. It does one thing rather than everything. The promise is narrow enough that somebody could repeat it back to you. And it is aligned with whatever made people sign up in the first place.

They fail when they are anonymous, when they are a round-up of everything the business did that month, and when the thing that attracted somebody has nothing to do with what subsequently arrives.

### The alignment problem, which is the real failure

Somebody subscribes because of something specific. A piece you wrote, a talk they watched, an answer that helped them, a product they liked. That specific thing is the promise, whether or not you ever wrote it down.

Then the newsletter turns up and it is about the company. New hires, an award, a partnership announcement, an office move. Nothing wrong with any of it, and not one bit of it is what that person came for.

Satisfaction is a comparison between what was expected and what arrived, so the signup context is the denominator for everything that follows. A weekly email full of insight is a delight to somebody who expected occasional updates, and a disappointment to somebody who was promised something else entirely.

### What a newsletter needs to be now

- One purpose you can say in a sentence. If it takes a paragraph to explain what your newsletter is for, it is a container.
- A person attached to it. A name, a voice, a point of view, and ideally a reply address that reaches them.
- A predictable shape. People process a familiar structure faster, which is one of the quieter arguments for consistency over creative variety.
- Alignment with why people subscribed. Which means knowing why they subscribed, which means capturing it at the point of signup rather than guessing later.
- Editing, and the discipline to leave things out. What you removed matters as much as what you included. A newsletter that carries everything the business wants to say is serving the business, and people can tell.
- A reason to exist beyond somebody deciding you should have one. The hardest test, and the one most brand newsletters fail before the first issue.

## The practical bit

## Where this leaves you

### If you are a creator and Substack is working

- Keep it, and know what you are standing on. The trade is convenience and discovery in exchange for control, and it is a reasonable trade for a publication.
- Export your list monthly. It takes two minutes, it gives you a backup independent of any platform decision, and you will never regret having it.
- Do not assume a custom domain has solved deliverability. It has changed the address, not the infrastructure.
- Build at least one relationship off-platform. So that if you ever move, you have a route to your audience that does not depend on a company you do not own.

### If you are a business considering it

- Do not put your commercial email programme on it. Lifecycle, transactional, segmentation, exclusions and reputation management are all outside what it is built for.
- Do not split your sender identity. Running a Substack alongside your own domain divides your engagement signals and teaches your audience two different names for the same business.
- Consider it for a publication with its own identity. If you really do want to build an editorial product with a named author and no commercial machinery attached, it is a reasonable choice.

### If your newsletter is not working

The fix is almost never the platform. Moving a container from one tool to another produces a container in a different tool.

1. Write down what it is for, in one sentence. If you cannot, that is the problem and no amount of design will hide it.
2. Put a person on it. A name, a voice, and a reply address somebody monitors.
3. Find out why people subscribed. Look at your entry points, and start capturing the reason at the point of signup if you are not already.
4. Cut everything that is there because somebody asked for it to be there. The job ad, the award, the partnership announcement. Move them somewhere else or drop them.
5. Make the promise explicit, and keep it. Say what it is and how often at the point of capture, then match it.

## The conclusion

Substack has not changed email marketing. It has exposed something about it that was always true and that the industry found inconvenient.

People will happily read a LOT of email, frequently, for years, if it comes from somebody they want to hear from, about something they chose, in a shape they recognise. Everybody in email has been saying a version of that for two decades and mostly nobody believed it, because the numbers on container-style newsletters suggested people hated email.

They never hated email, they hated that.

What Substack changed is who can do it without a marketing team, and what it asks in return is control of your infrastructure. A trade rather than a scandal, and a perfectly sensible one for a writer with a publication - a bad one for a business with a revenue channel.

Know which of those you are, know what you are standing on, and keep a copy of your list!

## Email, CRM and HubSpot Support

I help marketers and businesses **globally** improve, design and fix their email, CRM, and HubSpot ecosystems, from strategy through to execution.

**My services include:**

- Email marketing strategy, audits, training, workshops, and consultancy
- CRM strategy and enablement
- Full HubSpot implementations, optimisation and onboarding through my agency

If you’re looking for experienced external support (and lots of enjoyment along the way), this is where to start.