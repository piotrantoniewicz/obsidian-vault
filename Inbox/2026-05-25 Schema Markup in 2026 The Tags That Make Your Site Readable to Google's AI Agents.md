---
type: "Web"
authors: "[[Robert Portillo]]"
url: "https://12amagency.com/blog/schema-markup-in-2026/"
published: 2026-05-25
created: 2026-06-04
tags:
---


[![](https://12amagency.com/wp-content/uploads/2026/03/12am-Logo-01.svg)](https://12amagency.com/)

A friend of mine runs a attorney personal injury practice in Houston. Solid firm, decent site, ranks well for his main local terms. Last month I ran his website through a structured data audit and asked him a simple question: “How much schema do you have?”

His answer: “Some, I think.”

He had Article schema on three blog posts. Nothing else. No Organization, no LocalBusiness, no Service, no FAQ, for an eight-figure practice with 11 years of content and a fully built-out service ladder.

That’s the state of schema on most websites in 2026. And after [Google I/O 2026](https://io.google/), it’s about to become the difference between being cited inside AI answers or being invisible.

## Why schema matters more now than it did six months ago

Google’s I/O 2026 update changed the math on structured data in three specific ways.

**Generative UI needs structured data to build with.** When Google’s AI builds a custom comparison table or calculator on the fly inside the SERP, it’s pulling structured product, service, and review data from indexable sources. Your unstructured prose, no matter how good, can’t be assembled into a mini-app. Your schema can.

**Information agents need machine-readable change signals.** When an agent monitors “best new orthodontists in Plano” 24/7, it’s scanning for structured updates — new reviews, pricing changes, fresh FAQ entries, new service additions. Schema is how those signals reach the agent.

**Citation depends on parseability.** Gemini, ChatGPT, and Perplexity all weight content they can cleanly parse. Schema tells the AI exactly what your page is, who’s on it, what’s being sold, and what’s being claimed. No schema means the AI has to guess. It usually guesses wrong.

If you take one thing from this post: schema went from a nice-to-have to table stakes. You can’t compete in AI search without it.

## The eight schema types that matter most

![](https://12amagency.com/wp-content/uploads/2026/05/The-eight-schema-types-that-matter-most.webp)

There are hundreds of schema types on schema.org. These eight cover roughly 90% of what most businesses need.

### 1\. Organization

The foundation. Every site needs one Organization schema, usually placed in the site-wide header or footer.

{

“@context”: “https://schema.org”,

“@type”: “Organization”,

“name”: “12AM Agency”,

“url”: “https://12amagency.com”,

“logo”: “https://12amagency.com/logo.png”,

“sameAs”: \[

“https://www.linkedin.com/company/12amagency”,

“https://twitter.com/12amagency”

\],

“founder”: “Robert Portillo”,

“foundingDate”: “2020”

}

The sameAs field is critical. It connects your brand to its other web identities and helps Google’s Knowledge Graph confirm you’re a real entity.

### 2\. LocalBusiness

For any business with a physical address or service area. This is what powers Google Business Profile alignment.

{

“@context”: “https://schema.org”,

“@type”: “LocalBusiness”,

“name”: “Smith & Associates”,

“address”: {

“@type”: “PostalAddress”,

“streetAddress”: “123 Main St”,

“addressLocality”: “Dallas”,

“addressRegion”: “TX”,

“postalCode”: “75201”

},

“telephone”: “+1-214-555-0100”,

“openingHours”: “Mo-Fr 09:00-17:00”,

“priceRange”: “$$”

}

Your address, phone, and hours must match Google Business Profile exactly. Inconsistencies cost you trust signals.

### 3\. Service

For service-based businesses, every individual service deserves its own Service schema on its page.

{

“@context”: “https://schema.org”,

“@type”: “Service”,

“serviceType”: “Personal Injury Law”,

“provider”: {

“@type”: “LegalService”,

“name”: “Smith & Associates”

},

“areaServed”: “Dallas, TX”,

“description”: “Representation for car accidents, slip and fall, and wrongful death claims.”

}

Most law firms, dental practices, and home services businesses skip this entirely. Don’t.

### 4\. Product

For anything sold online. Critical for Universal Cart visibility after I/O 2026.

{

“@context”: “https://schema.org”,

“@type”: “Product”,

“name”: “Premium Landscaping Mulch, 2 cu ft”,

“image”: “https://example.com/mulch.jpg”,

“brand”: “SelectSG”,

“offers”: {

“@type”: “Offer”,

“price”: “8.99”,

“priceCurrency”: “USD”,

“availability”: “https://schema.org/InStock”

}

}

If you sell anything and your products don’t have current Product schema with live pricing and availability, you won’t compete inside Universal Cart.

### 5\. FAQPage

The single most important schema type for AI citation. Period.

{

“@context”: “https://schema.org”,

“@type”: “FAQPage”,

“mainEntity”: \[{

“@type”: “Question”,

“name”: “How long does dental implant healing take?”,

“acceptedAnswer”: {

“@type”: “Answer”,

“text”: “Most patients heal in 3 to 6 months, depending on bone density and aftercare compliance.”

}

}\]

}

FAQ schema lets AI systems extract clean question-answer pairs directly. We’ve seen pages with strong FAQ schema get cited 4-5x more often than identical content without it.

### 6\. HowTo

For tutorial, process, or step-based content.

{

“@context”: “https://schema.org”,

“@type”: “HowTo”,

“name”: “How to File a Personal Injury Claim in Texas”,

“step”: \[{

“@type”: “HowToStep”,

“name”: “Document the incident”,

“text”: “Photograph the scene, collect witness contact information, and request a police report.”

}\]

}

Especially powerful for legal, medical, and home services content. AI agents pull HowTo steps directly into synthesized answers.

### 7\. Review

Trust signals for both humans and AI. Two flavors matter: aggregate reviews on the business itself, and individual review schema on testimonial pages.

{

“@context”: “https://schema.org”,

“@type”: “Review”,

“itemReviewed”: {

“@type”: “LegalService”,

“name”: “Smith & Associates”

},

“reviewRating”: {

“@type”: “Rating”,

“ratingValue”: “5”

},

“author”: {

“@type”: “Person”,

“name”: “Maria Garcia”

}

}

Don’t fake these. Google can tell, and AI systems weight verified reviews dramatically more than unverified ones.

### 8\. Article

For every blog post, news piece, or long-form content page.

{

“@context”: “https://schema.org”,

“@type”: “Article”,

“headline”: “Google Just Killed the Search Box”,

“author”: {

“@type”: “Person”,

“name”: “Robert Portillo”,

“url”: “https://12amagency.com/team/robert-portillo”

},

“datePublished”: “2026-05-22”,

“dateModified”: “2026-05-23”,

“publisher”: {

“@type”: “Organization”,

“name”: “12AM Agency”

}

}

The dateModified field matters more than most people realize. AI systems weight freshness heavily, and an out-of-date dateModified tag tells them your content is stale even when it isn’t.

## The four schema mistakes we see most often

After auditing hundreds of client sites, the same problems show up over and over.

**Mistake 1: Schema that doesn’t validate.** Half the sites we audit have at least one schema block with a syntax error, missing required field, or invalid type. Every schema block should be tested in Google’s Rich Results Test and the schema.org validator before going live.

**Mistake 2: Conflicting Organization data.** Your LocalBusiness schema says one address. Your Organization schema says another. Your contact page footer says a third. The AI sees an entity it can’t verify and downgrades you accordingly.

**Mistake 3: Schema without page content to back it up.** Marking up an FAQ that doesn’t actually appear on the page. Marking up reviews that don’t exist. Marking up products without real prices. Google catches this and penalizes it. So do AI systems, more quietly.

**Mistake 4: Stale schema.** Schema written in 2021 and never updated. Pricing schema with two-year-old prices. Article schema with dateModified that hasn’t moved since the post went live. All of it degrades your AI visibility over time.

## The 15-minute schema audit

Run this on your site this week.

1. **Crawl your site** with Screaming Frog or Sitebulb. Export the structured data report. Note which pages have schema and which don’t.
2. **Validate every unique schema type** in Google’s Rich Results Test. Flag anything that throws an error or warning.
3. **Check coverage gaps.** Every service page should have Service schema. Every product should have Product. Every blog post should have Article. Map the gaps.
4. **Audit consistency** across Organization, LocalBusiness, and your Google Business Profile. Name, address, phone, hours, URL — they should match exactly everywhere.
5. **Set a maintenance cadence.** Schema isn’t a one-time deployment. Pricing changes, hours change, services expand. Build a quarterly schema review into your marketing calendar.

If steps 1-3 already feel out of reach, that’s normal. Most in-house marketing teams don’t have the technical capacity for full schema deployment, and most general [SEO agencies](https://12amagency.com/digital-marketing-services/seo-management/) don’t prioritize it.

![12 am agency](https://12amagency.com/wp-content/uploads/2025/08/12-am-agency.webp)

12 am agency

### How 12AM handles schema for clients

For our legal, dental, home services, and franchise clients, schema deployment is one of the first things we touch. We treat it as infrastructure, the layer everything else (content, links, GBP) sits on top of.

Our process: full structured data audit, gap analysis against the eight schemas above, custom JSON-LD deployment via tag manager or direct injection, quarterly maintenance review, and monitoring through Google Search Console’s Enhancements reports.

If your site is missing more than half the schemas in this post, or if you’re not sure what it has at all, we can run a free schema audit and send you the gap report.

[**Request a free schema audit →**](about:blank)

![](https://secure.gravatar.com/avatar/716f454b2743a90c221514ab6b4d354902297d6c378ba66fe106265d167aeb07?s=96&r=g)

Robert Portillo

12 years of LLM and SEO research. Former telecom engineer. I write about the intersection of AI and local search — and what it actually means for businesses trying to get found.