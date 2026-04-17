---
type: "Web"
authors: "[[Florian Engel]]"
url: "https://www.impact-stack.org/how-to-protect-your-charitys-forms-from-spam/"
published: 2026-03-05
created: 2026-04-13
tags:
  - digital-campaigning
  - automatyzacja
  - organizacje-społeczne
---


Spam is a real challenge for campaigning and fundraising. It weakens your campaign’s legitimacy, harms email deliverability, wastes paid media budget, and disrupts genuine supporter engagement.

It’s an ongoing fight to keep supporter experiences friction free, while preventing bad actors from attacking your pages. You may not be seeing large-scale spam attacks right now, but with AI tools making it cheaper than ever to create bots that spam forms, it’s a risk you should be thinking about.

There is no one-size-fits-all solution to fighting spam attacks. But there are various layers of protection you can put in place to increase your action page’s resilience. These layers work together to make it more expensive for bots to attack your pages, enabling you to fend off spammers.

The challenge facing charity campaigners and fundraisers is this: how do you prevent automated submissions to your online action forms without making it harder for genuine supporters to act?

## Why is spam a problem for campaigners and fundraisers?

### Campaign risks

If your charity’s email-to-target or email-to-MP action pages are spammed, their legitimacy suffers. Spam messages can land in your target’s inbox with your charity’s name on them. The credibility of genuine supporter voices is undermined, and it becomes easier for your target to dismiss your campaign.

If emails-to-target (such as MPs) are triggered by spam submissions, they may be flagged as spam and increase the spam score of all your emails. That means even submissions from real supporters may not reach your target.

![An email mail box filled with emails flagged as spam mail.](https://storage.ghost.io/c/d6/06/d606d63d-f051-4a3e-bf05-533bbca9273a/content/images/2026/03/email-spam-in-inbox.jpg)

Spam messages can land in your target’s email inbox with your charity’s name on them.

### Deliverability risks

Over time, your email deliverability can suffer if your list becomes filled with spam data.  
  
If you send emails to bogus addresses, or worse, spam traps (fake addresses set up to catch spammers), your sender reputation drops. Emails to legitimate supporters can start landing in spam or junk folders, making it less likely they’ll see your next big campaign or donation ask. Over time, your email deliverability can suffer if your list becomes filled with spam data.

![Screenshot showing a mouse cursor pointing at the spam folder of an email box with 372 emails in it.](https://storage.ghost.io/c/d6/06/d606d63d-f051-4a3e-bf05-533bbca9273a/content/images/2026/03/email-spam-in-inbox-2.jpg)

If your email list is filled with spam data, your email deliverability can suffer. Emails to legitimate supporters can start landing in spam or junk folders

### Paid ads: paying for bogus leads

If you’re running lead generation ads on platforms like Facebook and Instagram and aren’t taking steps to protect your action pages from spam, you could be paying for bogus data rather than growing your potential donor list. Spam distorts reporting and can lead to miscalculating costs per action.

### Spam undermines user-generated content

User-generated content can be a powerful tactic for charities. But running comments sections, live tickers or meme generators become difficult in a world of spam.

These tactics rely on a digital space that real people can actually use. Spam robs us of them by making that space unusable.

## How to protect your forms from spam attacks

There is no one-size-fits-all approach to protecting your charity’s action pages from spam. Effective spam prevention means putting a number of measures in place.

The goal is to make spam submissions as costly as possible for the attacker, without affecting the experience for real supporters.

You should be using various layers of protection to protect your charity’s forms. The objective is to increase the time and cost needed for spammers to spam your forms, so targeting you becomes no longer worth it.

### Session-based protection

When someone opens a page in their browser, a “session” is created. Whatever they do with the form is tied to that session and to that specific browser. If they close the browser and revisit the page, a new session starts.  
  
This matters because it allows you to identify activity tied to one browser and limit what can be done within a single session. It makes large-scale automation harder.  
Spammers can simulate multiple browsers to get around this, but doing so becomes more expensive.

### GDPR compliant invisible CAPTCHA (“Proof of Work”)

One of the most effective friction-free tools for spam prevention is an invisible CAPTCHA that runs in the background.

There are different ways to achieve this and many different providers that offer systems for “bot detection” and “spam prevention”. But it can be difficult to find solutions that are GDPR compliant and affordable at a scale we get with mass mobilisation.

One of the most promising technologies here is a “proof of work” invisible CAPTCHA. Inspired by crypto concepts, this approach requires the computer accessing the form to solve a small mathematical puzzle. Supporters won’t notice this delay but, at scale, it becomes costly for spammers to run thousands of these puzzles at once.

The difficulty of the puzzle can be increased if needed, further raising the cost of an attack.

Impact Stack 2 includes a GDPR-compliant invisible CAPTCHA as part of its layered approach to protecting forms from spam. If you'd like to find out more, please [book a demo](https://www.impact-stack.org/contact/?utm_content=spamblog).

### Field Validation

Most campaign and fundraising forms include a field for the supporter’s email address.

Requiring email validation and enforcing unique email addresses adds another layer of effort for spammers. It forces more realistic interaction with the form, requiring spammers to use a wide range of different email addresses as part of their attacks.

![Form built in Impact Stack showing the email address field with a red error message saying 'email address field is required'](https://storage.ghost.io/c/d6/06/d606d63d-f051-4a3e-bf05-533bbca9273a/content/images/2026/03/Screenshot-2026-03-03-at-18.58.57.png)

Using forms, like this one built in Impact Stack, requiring email validation and enforcing unique email addresses adds another layer of effort for spammers.

The same principle can be applied when thinking about different form fields. If you have strong validation on the form, it will be more difficult for a bot to submit. Of course, this always has to be considered alongside the user experience of your supporters. You never want to sacrifice the usability of the form to prevent spam.

### Visible CAPTCHA

Traditional CAPTCHAs, such as traffic-light or image puzzles, can be used as an additional layer of protection.  
  
However, they can be difficult to solve and create accessibility challenges for genuine supporters, so they should be used carefully.

Some tools (like Google reCAPTCHA) have raised GDPR compliance questions in the EU, although this may change in 2026. Alternatives such as  
[Friendly CAPTCHA](https://friendlycaptcha.com/?ref=impact-stack.org) or [hCaptcha](https://www.hcaptcha.com/?ref=impact-stack.org) exist, but can become expensive at scale.

![](https://storage.ghost.io/c/d6/06/d606d63d-f051-4a3e-bf05-533bbca9273a/content/images/2026/03/Screenshot-2026-03-03-at-19.04.04.png)

Friendly CAPTCHA provides an alternative to Traditional CAPTCHAs, which can present accessibility and GDPR challenges, but can be expensive to use at scale.

Some forms use simple puzzles like a maths problems to prevent spam. These types of puzzles tend to create a burden for users and may not even be effective at preventing spam, so we would not recommend using them.

On Impact Stack we have built integrations that allow organisations to place these external CAPTCHAs (visible and invisible) on the page to increase protection.

### Honeypot traps

Another method to prevent bots from submitting your form is to include invisible fields to your form that look like regular form fields to spam bots. When bots automatically put content into these fields, the entire form submission is marked as spam.

Honeypot traps can be a useful addition, if they are implemented well. But when implementing these types of traps you can accidentally also prevent legitimate users from filling in the form. In addition, more modern bots can bypass these traps without too much effort. So honeypots should certainly not be the only way your forms are protected.

### Post-Submission Filtering

Even with strong prevention, some spam submissions may get through. Spam scoring after submission is another layer you should ideally have in place. This identifies potential spam using filters and databases of common spammers.It allows you to weed out submissions that are not legitimate, so they don’t end up on your supporter list. That protects your deliverability and prevents you from paying to reach bogus leads.  
  
Services like [Akismet](https://akismet.com/?ref=impact-stack.org) are world-famous for keeping spam off blog post comments. While their pricing is great for smaller numbers, using a service like this for spam scoring at scale can get expensive quickly.

## Impact Stack 2 offers a unique approach to fighting spam

If the software you use to build your charity’s forms does not include these layers, you may not be doing as much as you can to protect your campaigns from spam.

Impact Stack 2 focuses on layered spam protection that is largely invisible to the user, keeping supporter experience friction free, with fast load times and no complicated CAPTCHAs to solve.

This includes:

- Session-based form protection,
- A GDPR-compliant invisible CAPTCHA (“proof of work”),
- Adjustable difficulty levels,
- Optional additional CAPTCHA layers you can add to individual forms.

In the first six months of launching these anti-spam tools, we’ve seen significant success in defending action pages from bots.

Because fighting spam is an evolving battle, we’re also developing features to:

- Automatically “close” old actions so forms are not left exposed (redirecting to another action or page),
- Add further spam scoring after submission to decide whether a record should be processed to your email list.

Want to protect your action pages from spam attacks? [Book an Impact Stack 2 demo now.](https://www.impact-stack.org/contact/?utm_content=spamblog)