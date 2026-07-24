---
type: "Web"
authors: "[[Beth O'Malley]]"
url: "https://weareastral.co.uk/thevault/email-accessibility-and-the-european-accessibility-act-what-it-is-who-it-affects-and-what-to-do-about-it?utm_medium=email&_hsenc=p2ANqtz-8WlrBqdovC-pdLUOBntW_JG9DBpDIO5eWNYJlkxQtenvoBNe5C6qa_L6_zj06OdmHJE3QZv-IpogtOLU3toEcXplEOHsLUGr34EiidOIVR0hL9gxE&_hsmi=141442980&utm_content=141381565&utm_source=hs_email"
published: 2026-07-22
created: 2026-07-24
tags:
---


*The European Accessibility Act came into force on 28 June 2025. This blog explains what it means for your email marketing, who is affected, and the practical changes that bring your emails up to standard.*

Accessibility in email has been a best practice conversation for years. Most marketers know they should use alt text. Most know large fonts are better than small ones. Most know colour contrast matters. And most have still not made the systematic changes that would make their emails actually accessible.

The [European Accessibility Act](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/european-accessibility-act-eaa_en) changes the framing from should to must, at least for businesses operating in or selling to EU markets. From 28 June 2025, email accessibility is a compliance issue as well as a design one, and the standard it points to is the same one that has underpinned good email design all along.

This blog is the practical version: what the EAA is, who it affects, what it specifically requires when it comes to email, and what you need to do to meet it. It is also, I will say upfront, a very good set of reasons to finally do the things that good email design demanded anyway.

## What is the European Accessibility Act?

The European Accessibility Act (EAA) is EU legislation that requires businesses to make their digital products and services accessible to people with disabilities. It came into full force on 28 June 2025 and covers a wide range of digital experiences: websites, mobile apps, e-commerce platforms, ATMs, ticketing machines, banking services, and electronic communications — which includes marketing email.

The EAA is not a new idea. It is built on WCAG ([Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21/)), the same internationally recognised standard that has existed for years and that most digital accessibility work already references. What the EAA does is give it legal weight across EU member states and set a compliance deadline.

The practical effect for email marketers: your marketing emails need to meet accessibility standards. Not aspirationally, not eventually, but now, at least for any subscriber base that includes people in EU member states.

### Who is affected?

The EAA applies to any business that offers products or services in the EU — not just EU-based businesses. A UK company emailing subscribers who are located in France, Germany, Spain, or any other EU member state is in scope.

There is an exemption for microenterprises: businesses with fewer than ten employees and an annual turnover or balance sheet total under €2 million. If that is you, the EAA’s specific requirements do not apply in the same way, though the underlying accessibility principles are still good practice worth following.

If you are above that threshold and you have EU subscribers, this applies to you.

## Why email accessibility matters — beyond compliance

Before we get into the practical requirements, it is worth being clear about why accessibility in email matters at a level beyond legal compliance — because the compliance framing can make it feel like a box-ticking exercise when it is actually something more fundamental.

Approximately one in five people worldwide has some form of disability. This includes visual impairments (from full blindness to colour blindness to low vision), cognitive conditions (dyslexia, ADHD, processing differences), physical impairments affecting how people interact with devices, and hearing impairments where audio content is involved. These are not edge cases or niche audiences. They are a significant proportion of the people on your list.

Beyond disability, accessibility benefits a much wider audience than people generally assume. Older recipients whose eyesight has deteriorated. People reading email on mobile in bright sunlight where contrast is critical. People on slow connections where image-heavy emails do not load. People using voice assistants or wearables where screen reading is how they consume email. People in a hurry who scan rather than read, for whom clear hierarchy and structure matter enormously.

Accessible email design is, by and large, good email design. The principles that make email accessible — clear structure, readable type, sufficient contrast, meaningful alt text, content that works without images — are the principles that make email perform well across all audiences. The EAA has not invented a new set of requirements that are in tension with good email practice. It has formalised requirements that good email practice already pointed to.

## What the EAA specifically requires for email marketing

The EAA does not publish a checklist of email requirements. It points to accessibility standards, primarily WCAG 2.1 at AA level and requires that digital communications meet them.

### 1\. Alt text on every image — meaningful alt text

*Not "image", not blank, not the filename. Describe what it actually shows.*

A screen reader — the technology used by people with visual impairments to consume digital content — reads the alt text of an image aloud when it encounters one. If your alt text is blank, the screen reader says nothing. If it says "image" or "banner" or "hero-final-v3.jpg", it says that instead of anything useful.

Meaningful alt text describes what the image shows and, where relevant, its purpose in context. A product image: "Blue ceramic travel mug with lid, 350ml." A decorative divider: leave the alt text blank intentionally (alt="") so screen readers know to skip it. A button saved as an image: the alt text should be the button label — "Shop now" or whatever the action is.

One image-only emails are the most extreme case. If your entire email is one large image with all the copy inside it, a screen reader cannot read any of it, and a subscriber with images disabled sees nothing. Image-only emails fail accessibility standards and, now, fail the EAA. The content of your email needs to exist as live text.

### 2\. Colour contrast — sufficient, not just matching

*WCAG AA standard: 4.5:1 for body text, 3:1 for large text and UI elements.*

Colour contrast affects anyone with low vision or colour blindness, and colour blindness affects approximately 8% of men and 0.5% of women. Light grey text on a white background fails. Pale pink text on white fails. Your brand colours may fail — check them before assuming.

The WCAG AA standard requires a contrast ratio of at least 4.5:1 for body text and 3:1 for large text (18pt and above, or 14pt bold and above). There are free contrast checker tools (WebAIM Contrast Checker is the most widely used) that let you input your foreground and background colour hex codes and get an instant pass/fail result.

This applies to all text in your email — body copy, headings, button labels, footer text, navigation links. The 6pt grey unsubscribe link in your footer is subject to the same contrast requirement as your headline.

Use this [accessibility checker](https://webaim.org/resources/contrastchecker/) to help!

### 3\. Readable font sizes

*Minimum 14px for body text. Larger is better.*

Very small text is effectively inaccessible to many readers, including older recipients and people with visual impairments. A widely followed guideline for email is a minimum of 14px for body text and 22px for headlines, with 16px for body text being a better target for mobile.

This is also a practical email performance issue, not just a compliance one. Tiny text on mobile — where a significant proportion of email is now read — is one of the fastest ways to lose a subscriber.

### 4\. Logical heading structure

*Not just bold text. Actual heading tags in the right order.*

Screen readers navigate content by heading structure. If your email uses H1 for the headline, H2 for section headings, and normal paragraph text for body copy — that is how a screen reader will move through it. If you just use bold text or larger font sizes to create visual hierarchy without underlying heading structure in the HTML, a screen reader sees a flat wall of text with no navigation points.

Most email builders handle heading tags, but it is worth checking that the visual design and the underlying HTML structure match. A big bold word that looks like a heading should actually be coded as a heading.

### 5\. Readable in plain text and with images off

*Your email needs to make sense without images loading.*

A meaningful proportion of email is read with images off — either by choice, by corporate email clients that block images by default, or by screen readers that do not render visual elements. Your email needs to communicate its core message without images. This means live text for key content (not images of text), descriptive alt text where images carry meaning, and a layout that does not collapse into an unnavigable mess when images are removed.

### 6\. Accessible link text

*Not "click here". Describe where it goes.*

"Click here" is meaningless to a screen reader user navigating by links. "Read the full guide on email deliverability" tells them exactly what they will get. "Click here to find out more" tells them nothing. Every link in your email should be descriptive enough to make sense out of context.

### 7\. Mobile-friendly by default

*Single column, large tap targets, no reliance on hover states.*

Accessibility and mobile-first design overlap substantially. A single-column layout that resizes gracefully is easier for all users. Large tap targets (minimum 44x44 pixels for buttons) prevent the frustration of mis-tapping on small mobile screens — a particular issue for people with motor impairments. Hover states that hide content entirely are not accessible on touchscreens.

### 8\. Dark mode compatibility

*Your email should not break in dark mode.*

Dark mode is used by a significant and growing proportion of email recipients. An email designed only for light mode can become unreadable in dark mode — dark text on a dark background, images with white backgrounds that become visible as white blocks, inverted colour schemes that clash with brand colours. Testing your email in dark mode is now a standard part of pre-send QA, not an optional extra.

## What to do

The EAA came into force in June 2025. If you have EU subscribers and you have not yet made these changes, you are already behind the deadline. The good news is that most of these changes are template-level fixes rather than campaign-by-campaign work — fix your templates and every email you send afterwards benefits.

Start with a template audit

Go through your current email templates and check each one against the points above. The areas most likely to fail in a standard template: low-contrast footer text, missing or generic alt text on decorative images, image-only header banners where all the key information is trapped inside an image, and font sizes that are fine on desktop but too small on mobile. These are fixable and most of them can be addressed in the template rather than on every send.

Use the right tools

WAVE (Web Accessibility Evaluation Tool) can scan HTML including email HTML for accessibility issues. WebAIM Contrast Checker for colour contrast. Litmus and Email on Acid both include accessibility testing in their preview tools. Your email builder may have built-in accessibility checking — check what is available in your platform.

Test in dark mode

Send test emails to yourself and check them in dark mode on both mobile and desktop. If something breaks visually, fix it in the template. Most email builders allow you to specify how elements should appear in dark mode using CSS media queries.

Train your team

Accessibility decisions happen at the content and design level, not just the technical level. Anyone who writes email copy, designs email templates, or selects images for campaigns needs to understand the accessibility requirements and why they matter. Alt text writing is a skill. Contrast checking needs to become a routine step in template sign-off, not an afterthought.

## A note for UK-based senders

The EAA is EU legislation and applies to EU member states. Post-Brexit, the UK is not directly bound by the EAA. However:

- If you are a UK business emailing subscribers who are located in EU member states, the EAA applies to those emails.
- The UK has its own accessibility legislation: the Public Sector Bodies Accessibility Regulations require WCAG 2.1 AA compliance for public sector organisations. Private sector UK businesses are not directly covered by this, but the direction of travel is clear.
- The WCAG standards that underpin the EAA are international. Meeting them is good practice regardless of which jurisdiction you are primarily concerned about.
- The ICO’s guidance on electronic communications, and PECR, already create obligations around how you communicate with subscribers. Accessibility considerations sit alongside these.

My practical recommendation for UK senders: meet the accessibility standards anyway. The subscriber experience and commercial performance benefits apply regardless of geography, and the regulatory direction of travel is consistent across markets.

### Further reading:

- [Email Design Masterclass](https://weareastral.co.uk/email-design-masterclass) — 90 minutes on design psychology and accessibility
- [The Email Design Handbook](https://weareastral.co.uk/email-design-handbook)
- [Email Marketing Health Check](http://emailhealthcheck.co.uk/)
- [WebAIM Contrast Checker (external tool)](http://webaim.org/resources/contrastchecker/)
- [WCAG 2.1 Guidelines (external reference)](http://w3.org/TR/WCAG21/)