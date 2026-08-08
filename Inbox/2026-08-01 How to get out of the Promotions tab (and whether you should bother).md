---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/how-to-get-out-of-the-promotions-tab-and-whether-you-should-bother?utm_medium=email&_hsenc=p2ANqtz--rTwgzuT2Tl742LCKirWD9jjOzUycxdt7J82SiSv3bvOirLFpol-coceAkQtALIE83lqawdp7CTaXxKP8PMo9hJ_z0pWCmqLw2Q1aDdZLPhy1k4NM&_hsmi=142599401&utm_content=142598984&utm_source=hs_email"
published: 2026-08-01
created: 2026-08-08
tags:
---


This is one of the questions (yes another most-asked question hahah) I get most, and it usually arrives with a bit of frustration attached.

Everything's set up properly, the emails are good, and yet there you are, filed away in Promotions with every other brand and their dog.

Most articles on this will hand you a list of tricks and tips, but hopefully you know already, we're not like most other content.

I'm not going to do that, partly because the tricks mostly don't work, but mainly because the honest answer is more useful and more interesting than the trick list.

The honest answer is that it depends entirely on which subscribers you're talking about.

With people who have been on your list for two years, you're fighting a pattern you spent two years building, and you will mostly lose.

With people who signed up last week, you have a real and largely unused opportunity — because the classifier hasn't decided anything about them yet.

So: how I'd actually do it, whether it works, whether you should, and what the tools are really selling you.

## How Gmail decides if you go to the promotions tab

Before anything else, you need to know what you're dealing with, because a lot of the advice out there is built on a model of Gmail that hasn't been accurate for years.

It is not a keyword filter (not anymore!). There is no banned word list, stripping out 'free' and removing your emoji is not doing what people think it's doing.

Tab placement is a machine learning classification, and Google has said it uses signals including who the sender is, what type of content the message contains, and how users have historically interacted with similar mail. Roughly in order of how much they matter:

- That specific recipient's history with you. The strongest signal by some distance. Opens, clicks, replies, and whether they've ever dragged you into Primary themselves.
- Your domain's overall pattern. What sort of mail you generally send, and how people generally respond to it.
- Content and structure. Image-heavy templates, high link density, buttons, tracking pixels, multi-column layouts, thin text. Read as commercial. Text-dominant and conversational reads as personal.
- Header signals. A reply-to that doesn't match your from address nudges you away from 'personal correspondence'.

One more thing worth knowing is that Gmail applies these labels in the background even for people who have tabs switched off entirely. The classification is always happening, whether or not anybody can see it.

## Gmail is not the only one doing this

Almost everything written about tabs is written about Gmail, and then applied to every other inbox as though they all work the same way, which they don't. Yahoo, Microsoft and Apple all sort mail now, they each do it differently, and one of them isn't a mailbox provider at all, which changes quite a lot about what you can influence.

Before the differences, the thing they share. Every one of these systems is weighing some version of the same four inputs: who you are as a sender, what the message looks like structurally, whether it went to one person or a hundred thousand, and how this particular recipient has behaved towards you before.

None of them has published the recipe, and I'd treat anybody claiming to know the exact weightings with a fair amount of suspicion.

#### Yahoo

Yahoo took a different route for years. Rather than sorting mail on arrival, it offered Views, a filing system sitting down the side of the inbox that grouped your receipts, subscriptions, shopping and travel mail so you could find things without searching. Useful for the user, but it wasn't routing anything and it wasn't deciding where your campaign landed. That has changed! The desktop redesign brought in inbox tabs, with Priority sitting alongside Offers, Newsletters, Social and an All view, and categories switched on or off in settings.

The interesting part for us is that Yahoo separates Newsletters from Offers, and Gmail doesn't. In Gmail, the thoughtful weekly you spent two days writing and the flash sale from a brand you bought socks from once both land in Promotions. Yahoo is drawing a line between content somebody subscribed to and somebody selling them something, which is a distinction worth taking seriously, because if you send both from the same domain under the same from name, you're asking a classifier to make a separation you haven't made yourself.

Yahoo has not published technical criteria for tab placement. Anybody handing you a definitive Yahoo playbook right now is guessing!

#### Microsoft: Outlook, Hotmail and Live

Microsoft gives you two buckets rather than five. Focused holds what Outlook predicts you want now, Other holds everything else, and it's been that way since 2016 when it replaced Clutter. It's the default across Outlook.com consumer accounts, Outlook on the web, Microsoft 365 and the mobile apps.

Three things make Microsoft different from the others.

- Explicit user training carries enormous weight. A recipient can right-click and choose 'Always move to Focused' or 'Always move to Other', and that single action sticks for every message you send them afterwards. Gmail mostly infers what somebody wants; Outlook lets them instruct it outright. That cuts both ways, because one irritated recipient can file you in Other permanently, and one interested one can pull you into Focused permanently. It's worth asking for, once, the same way you'd ask a Gmail subscriber to drag you across.
- Corporate mailboxes have an administrator. In B2B, the person you're emailing may not control the setting at all, because tenant admins can enable or disable Focused Inbox across an organisation and push safe sender lists centrally. Some of your placement is an IT decision made by somebody who has never heard of you.
- It's mid-migration. Microsoft has been moving some tenants off Focused and Other onto a Gmail-shaped inbox with Primary, Promotions, Social and Updates categories instead. So if you optimise hard around a two-bucket model, you may be optimising for something Microsoft is in the process of leaving behind.

#### Apple Mail and iCloud

Apple Mail isn't a mailbox provider, it's a mail client. The categories are applied on the device by the app, sitting on top of whatever the actual mailbox provider already decided. A Gmail address read on an iPhone gets Google's classification and then Apple's, layered one over the other.

Since iOS 18.2, and now across iPhone, iPad, Mac and icloud.com, that means four categories: Primary, Transactions, Updates and Promotions.

What matters about it:

- It happens on-device. There's no Apple equivalent of Postmaster Tools, no feedback loop, and nothing to monitor. You cannot see where you're landing and neither can your ESP. This is the most opaque part of the entire subject.
- Messages group by sender. Outside Primary, your emails stack into a digest view with the rest of your recent sends. Your campaign isn't a message in a list, it's one layer in a pile, and the senders who suffer most from that are the high-frequency ones mailing an audience that isn't especially engaged.
- Summaries can replace your preheader. Apple may show a generated summary of what the email says rather than the preview text you wrote, which means the hook you crafted isn't necessarily the line doing the work.
- Time-sensitive mail can appear in Primary as well. Apple's own documentation says that a Transactions, Updates or Promotions message carrying time-sensitive information also shows up in the Primary list, which is worth knowing if you send anything genuinely time-bound.
- Users can recategorise a sender permanently. One action from the digest view, 'Categorize Sender', and every current and future message from you moves to the category they picked. That's simultaneously the biggest risk and the cleanest opportunity on this whole list, because it's the one place where a subscriber can put you exactly where they want you and have it stay there.

## How these algorithms change, and how you find out

The totally, VERY honest answer is that you don't find out in advance, and mostly you don't find out at all.

Interface changes get announced, because users can see them. Classifier tuning doesn't! Google told everybody about relevance sorting in Promotions because it visibly changed what people see when they open the tab. Nobody publishes a note saying they adjusted the weighting on image-to-text ratio last Tuesday, and they never will, because the moment they do, somebody games it.

What's more useful is understanding that change reaches you differently depending on the provider.

- Gmail, Yahoo and Microsoft change server-side. It's continuous, it's often staged in ways you can't observe, and there's no version number to track. You get the new behaviour whether you noticed or not.
- Apple ships with the operating system. Changes arrive with an iOS, iPadOS or macOS release and then spread across your list gradually as individual people update their phones. So an Apple-driven shift shows up in your data as a slow drift over months rather than a step change on a particular date, which makes it very easy to misattribute to something you did.
- Microsoft is also moving tenants between two different models entirely. Two of your B2B subscribers at two different companies may currently be on two different systems, so your Outlook data isn't measuring one thing.

Which is why the measuring section further down matters more than the tactics one. You will almost always learn about a change from your own cohort data, and you will learn about it late. That isn't defeatism, it's just the shape of the problem, and planning around it beats being surprised by it.

| **Provider** | **The buckets** | **Who's in control** | **The thing to know** |
| --- | --- | --- | --- |
| **Gmail** | Primary, Social, Promotions, Updates, Forums | Per-user model; subscriber can drag between tabs | Labels are applied in the background even with tabs switched off, and Promotions now sorts by relevance rather than recency |
| **Yahoo** | Priority, Offers, Newsletters, Social, All | Per-user; categories toggled on or off in settings | Separates newsletters from offers, which Gmail does not. No published placement criteria, so treat confident advice carefully |
| **Microsoft** | Focused and Other; some tenants now on Primary, Promotions, Social, Updates | Subscriber can force it permanently; admins can disable it organisation-wide | Mid-migration between two models, and in B2B your placement is partly somebody else’s IT decision |
| **Apple Mail and iCloud** | Primary, Transactions, Updates, Promotions | On-device; subscriber can recategorise a sender permanently in one action | A client rather than a provider, so it layers on top of everything above. Digest grouping and generated summaries change what actually gets seen |

## Should you be aiming to get in the inbox?

Before you spend a quarter on this, it's worth being clear-eyed about whether it's a problem worth solving for you specifically. There is a real case on both sides and most articles only make one of them.  

The case for caring

- Placement has genuinely shifted. Seed testing suggests senders who used to see roughly a 50/50 Primary/Promotions split now see closer to 25/75, and that's held since late 2024.
- Primary gets processed faster and more attentively, and on mobile it's where the push notifications live.
- Since Gmail's September 2025 change, the Promotions tab sorts by relevance rather than recency — so weak engagement now buries you inside the tab as well as putting you in it.
- Anything that improves your standing with the classifier also improves your standing with the human. The work isn't wasted either way.

The case for letting it go

- Promotions is not spam. Tab sorting and spam filtering are entirely separate systems. You were delivered. You're in the inbox, in a folder.
- Promotions placement generates roughly half the spam complaints that Primary placement does. People are more forgiving of marketing where marketing belongs.
- The impact figures are all over the place. One source puts the read-rate gap at 12%, another at 10–30%, another at 30%. They can't all be right.
- Apple Mail brought in its own categories with iOS 18.2, on by default, across roughly 55% of email opens. There's no unsorted inbox left to escape to.

My position, for what it's worth, is that the effect is real but consistently smaller than the anxiety about it, and the only number that should influence your decision is your own. Borrowed benchmarks on this topic are worth very little.

## How I'd get out of promotions and into the inbox

Split this in two, because the two halves of your list are completely different problems and treating them the same is why most attempts fail.

#### Part one: new subscribers, where this works

When somebody joins your list, the classifier has no history with them. There is no established pattern for it to fall back on. Those first few sends are it, the window where what you do actually sets the baseline rather than fighting one.

And crucially, you're not just training the filter. You're training the subscriber!! The behaviours you're trying to establish, opening, reading, replying, engaging, are the same behaviours the classifier is watching for. Two audiences, one set of actions.

Here's the sequence I'd run:

1. Send the welcome from a person. A real name in the from field, a real reply-to address that goes to a real inbox. Not noreply@.
2. Make the first three or four emails structurally light. They can be HTML, but not image only, be careful with how much 'promotion' you put in.
3. Ask for the move, once - lot's of people will ignore it, but if some do it - it's a win. In the welcome email: if this landed in a folder and not your inbox, move it! Because classification is per-user, this works for that individual. Ask once and mean it. Asking in every email is desperate and stops working immediately.
4. Ask a question you actually want the answer to. A reply is the strongest positive signal a recipient can give you, and most programmes are structurally designed to prevent it. Ask what made them sign up, or what they're struggling with, and read the answers - even a few replies are worth it.
5. Deliver the signup promise immediately. Whatever they were told they'd get, they get it in email one. Expectation met is what makes email two worth opening, and engagement on email two is what the classifier is watching.

#### Part two: your existing list, where it's much harder

I'm not going to pretend this half is as winnable, because it isn't. If your domain has sent marketing email for years and recipients have engaged with it as marketing email, Gmail has learned that pattern and continues routing you accordingly, largely regardless of what any individual message contains. Send one beautiful plain-text email into that, and you've produced a single atypical data point against a very large body of consistent evidence.  
And I'd gently point out that the classifier isn't wrong. If you've sent commercial email for three years, you are a commercial sender.

What you can still do, in order of how much it'll actually move:

- Suppress the long-term unengaged. This is the biggest lever you have on an old list. Every send to somebody who stopped caring in 2023 is evidence against you, and removing them changes your aggregate signal immediately.
- Segment hard by engagement and treat the cohorts differently. Your engaged group can carry a normal programme. Your middling group needs the lighter, reply-driven treatment from part one.
- Run a re-permission on the middle cohort. Not a passive-aggressive 'we miss you' — an actual question with an actual reply expected.
- Separate your sending streams. If transactional, newsletter and promotional mail all go out from one domain with one from name, they contaminate each other's patterns. Splitting them across subdomains and distinct from names lets each build the reputation appropriate to what it actually is.
- Even done well, you're moving a percentage, not a population. Set expectations accordingly, particularly with a stakeholder who's been promised a fix.

## So does it work?

Partially, slowly, and unevenly — which is an unsatisfying answer, so let me be specific about what partially means.

You will not see a domain-wide flip. There is no morning where you wake up and everything is in Primary, and anyone promising you that is selling something. What you should see, if it's working, is a difference between cohorts. Subscribers who came through a properly built onboarding sequence behaving differently from your legacy list. That's the proof, and it's the only way to measure this honestly.

### How to measure it

- Track placement by cohort, not by campaign. New subscribers acquired since the change versus everybody else.
- Use seed testing and Postmaster data for placement, not your ESP's delivered rate, which counts spam-foldered mail as delivered.
- Watch the trend over months, not the daily figure. Postmaster data lags and fluctuates.
- Track reply rate. It's the signal you're most directly trying to generate, and it's the one nobody reports on.

## Should you, though?

Depends what kind of sender you are, and this is where I'd push back on the assumption that Primary is universally the goal.

| **If you are...** | **Then...** |
| --- | --- |
| A newsletter, personal brand, or relationship-led B2B sender | Worth the effort. Your content genuinely belongs in Primary, the signals that get you there are accurate rather than a costume, and the onboarding work pays off twice. |
| Sending transactional and account mail | Yes, and it should already be there. If it isn't, that's a real problem worth fixing — check your reply-to, your template weight and your link density. |
| Ecommerce, offers, deals, seasonal promotions | Probably not. Your audience opens Promotions in a buying mindset. Fighting to appear next to their family emails invites complaints. Optimise inside the tab instead — annotations, deal badges, product carousels, and enough engagement to survive relevance sorting. |
| Running a mixed programme | Split the streams. Different subdomains, different from names for transactional, editorial and promotional mail, so each builds the pattern that suits it. |

But there are no promises - it's email, you lack control of a LOT of things.

## There are tools out there that promise to get your emails in the inbox - do they work?

There's a whole market selling escape, so it's worth separating what's actually being sold. Three categories, and only one of them is doing anything questionable.

Measurement - legitimate, and you need it

Seed list placement testing and Postmaster monitoring. These tell you where you're landing - not 100% accurate but I use multiple tools over a long period of time o get a good idea of placement. They don't move you anywhere, and they're not pretending to.

Optimisation - legitimate, and underused

Gmail's own annotations, deal badges and product carousels. These make you look better inside Promotions, which is the opposite of escape but is probably the more sensible goal for a lot of senders. Worth knowing: if you don't specify annotations yourself, Gmail may pull its own choice of images from your email into the preview. You either control that, or you leave it to chance.

Manipulation - where I'd be careful

Warmup and reputation-repair services. Here's how they work: you connect your sending account, the service maintains a network of thousands of inboxes, your account sends into that network automatically, and those accounts open your emails, reply, mark them important, and move them out of spam or Promotions. The more aggressive ones insert seed inboxes into your real campaigns and perform those actions at browser level so it looks human.  
The pitch is that this manufactures enough positive engagement to retrain the provider BUT can cause spam issues if you're not careful.  

What Google has said about that

GMass ran the largest warmup system on the internet, working with tens of thousands of accounts. They shut it down in 2023 because Google told them to do so or lose their Gmail API access, and made clear they consider warmup a terms of service violation they don't want happening at all.

The policy language is blunt: applications that use multiple accounts to abuse Google policies, bypass Gmail account limitations, circumvent filters and spam, or otherwise subvert restrictions are barred from Gmail API access.

GMass's founder wrote on the way out that warmup systems put strain on Google's systems in service of fooling those same systems, which is the most honest sentence anyone in the category has produced — and it came from someone who built one of the biggest. They moved from the Gmail API to IMAP and SMTP connections to get around the restriction.

And the structural problem, setting ethics aside

Tab classification is per-user, and the strongest signal is that individual recipient's own history with you. A warmup network is a pool of inboxes that are not your subscribers. Engagement from strangers cannot teach Gmail anything about how your subscriber feels about your email, because that decision is being made inside their account, on their behaviour.  
The vendors more or less concede it. One provider's own documentation admits that once Google has categorised you into Promotions, moving to Primary is difficult even with strong warmup. Another acknowledges that when providers detect thousands of accounts interacting with the same small pool of inboxes in similar patterns, they discount those signals entirely.

Measurement - legitimate, and you need it

Seed list placement testing and Postmaster monitoring. These tell you where you're landing - not 100% accurate but I use multiple tools over a long period of time o get a good idea of placement. They don't move you anywhere, and they're not pretending to.

Optimisation - legitimate, and underused

Gmail's own annotations, deal badges and product carousels. These make you look better inside Promotions, which is the opposite of escape but is probably the more sensible goal for a lot of senders. Worth knowing: if you don't specify annotations yourself, Gmail may pull its own choice of images from your email into the preview. You either control that, or you leave it to chance.

Manipulation - where I'd be careful

Warmup and reputation-repair services. Here's how they work: you connect your sending account, the service maintains a network of thousands of inboxes, your account sends into that network automatically, and those accounts open your emails, reply, mark them important, and move them out of spam or Promotions. The more aggressive ones insert seed inboxes into your real campaigns and perform those actions at browser level so it looks human.  
The pitch is that this manufactures enough positive engagement to retrain the provider BUT can cause spam issues if you're not careful.  

What Google has said about that

GMass ran the largest warmup system on the internet, working with tens of thousands of accounts. They shut it down in 2023 because Google told them to do so or lose their Gmail API access, and made clear they consider warmup a terms of service violation they don't want happening at all.

The policy language is blunt: applications that use multiple accounts to abuse Google policies, bypass Gmail account limitations, circumvent filters and spam, or otherwise subvert restrictions are barred from Gmail API access.

GMass's founder wrote on the way out that warmup systems put strain on Google's systems in service of fooling those same systems, which is the most honest sentence anyone in the category has produced — and it came from someone who built one of the biggest. They moved from the Gmail API to IMAP and SMTP connections to get around the restriction.

And the structural problem, setting ethics aside

Tab classification is per-user, and the strongest signal is that individual recipient's own history with you. A warmup network is a pool of inboxes that are not your subscribers. Engagement from strangers cannot teach Gmail anything about how your subscriber feels about your email, because that decision is being made inside their account, on their behaviour.  
The vendors more or less concede it. One provider's own documentation admits that once Google has categorised you into Promotions, moving to Primary is difficult even with strong warmup. Another acknowledges that when providers detect thousands of accounts interacting with the same small pool of inboxes in similar patterns, they discount those signals entirely.

Measurement - legitimate, and you need it

Seed list placement testing and Postmaster monitoring. These tell you where you're landing - not 100% accurate but I use multiple tools over a long period of time o get a good idea of placement. They don't move you anywhere, and they're not pretending to.

Optimisation - legitimate, and underused

Gmail's own annotations, deal badges and product carousels. These make you look better inside Promotions, which is the opposite of escape but is probably the more sensible goal for a lot of senders. Worth knowing: if you don't specify annotations yourself, Gmail may pull its own choice of images from your email into the preview. You either control that, or you leave it to chance.

Manipulation - where I'd be careful

Warmup and reputation-repair services. Here's how they work: you connect your sending account, the service maintains a network of thousands of inboxes, your account sends into that network automatically, and those accounts open your emails, reply, mark them important, and move them out of spam or Promotions. The more aggressive ones insert seed inboxes into your real campaigns and perform those actions at browser level so it looks human.  
The pitch is that this manufactures enough positive engagement to retrain the provider BUT can cause spam issues if you're not careful.  

What Google has said about that

GMass ran the largest warmup system on the internet, working with tens of thousands of accounts. They shut it down in 2023 because Google told them to do so or lose their Gmail API access, and made clear they consider warmup a terms of service violation they don't want happening at all.

The policy language is blunt: applications that use multiple accounts to abuse Google policies, bypass Gmail account limitations, circumvent filters and spam, or otherwise subvert restrictions are barred from Gmail API access.

GMass's founder wrote on the way out that warmup systems put strain on Google's systems in service of fooling those same systems, which is the most honest sentence anyone in the category has produced — and it came from someone who built one of the biggest. They moved from the Gmail API to IMAP and SMTP connections to get around the restriction.

And the structural problem, setting ethics aside

Tab classification is per-user, and the strongest signal is that individual recipient's own history with you. A warmup network is a pool of inboxes that are not your subscribers. Engagement from strangers cannot teach Gmail anything about how your subscriber feels about your email, because that decision is being made inside their account, on their behaviour.  
The vendors more or less concede it. One provider's own documentation admits that once Google has categorised you into Promotions, moving to Primary is difficult even with strong warmup. Another acknowledges that when providers detect thousands of accounts interacting with the same small pool of inboxes in similar patterns, they discount those signals entirely.

Gradual volume ramping on a new sending domain is real and sensible, and some of these tools do that part properly. I'm not saying warmup is worthless at everything!! I use warm tools myself.

I'm saying it is structurally incapable of fixing a classification made per-recipient on that recipient's own behaviour — and that's exactly what it's being sold to fix. Everything it simulates, a real subscriber will do for free, if the email is worth it.