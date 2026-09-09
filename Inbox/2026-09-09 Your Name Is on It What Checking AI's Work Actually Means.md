---
type: "Web"
authors: "[[Wendy Clow]]"
url: "https://www.linkedin.com/pulse/your-name-what-checking-ais-work-actually-means-wendy-clow-hpj8f/"
published: 2026-09-09
created: 2026-09-09
tags:
---


When the grant narrative goes out, your name is on it, not the AI's. That one fact should decide how you use it.

Monday morning I read an article on Medium about software development. It was [Mehmet Ozel reviewing a white paper Google recently published](https://medium.com/data-science-collective/googles-new-sdlc-guide-draws-a-hard-line-between-vibe-coding-and-agentic-engineering-29ee5514c48c), along with his own thinking about it. The paper draws a hard line between two ways people use AI to write code. On one side is what the industry has started calling vibe coding, where somebody with no development background describes what they want and gets working software back. On the other is agentic engineering, where professional developers use AI inside a process that still includes review and testing.

I do not write software for a living. I read the whole thing thinking about nonprofit work.

Here is the passage I underlined:

> "Vibe coding was never designed to handle production-grade correctness requirements. It was designed to get something running fast. Those are fundamentally different goals and the blurring of that line is where the current crisis lives."

Now read it again with your own work in place of the code. Here is how I rewrote it on Monday:

> "Generative AI was never designed to hand you publish-grade, error-free copy. It was designed to get a first draft written fast. Those are fundamentally different goals, and the blurring of that line is where the current crisis lives."

That second version is the reason for this edition. AI is very good at getting you started and not the best at finishing. Almost every AI problem I have seen inside a nonprofit traces back to the blurring of that line.

So this edition is about the finishing. Six ways your organization is probably already using AI, what each one is genuinely good for, how each one fails, and what checking it actually means. They are in a deliberate order, and the order is the point, so stay with me to the end.

### 1\. Brainstorming and second opinions

**Good for:** Generating options when you are stuck. Pressure-testing a plan before you take it anywhere. Asking what questions a skeptical board member would raise about your budget before the board raises them.

**How it fails:** It hands you a mediocre idea. That is the whole failure.

**What checking means:** Nothing. This is the safe one, and it is safe for a structural reason worth understanding, which is that nothing here ships. You are evaluating every suggestion on its merits anyway, so a bad one costs you the two seconds it takes to skip it.

If you are nervous about AI and want somewhere to start, start here. You cannot damage anything.

### 2\. First drafts

**Good for:** Turning a brain dump into something with a shape. This is my own heaviest use. It reliably turns a three-hour writing task into about thirty minutes.

**How it fails:** Visibly. It can produce text that sounds like nobody in particular, full of phrases you would never say out loud, making claims slightly larger than the ones you can support.

**What checking means:** Read it out loud. Replace the words you would never use. Rearrange the sentences until they sound like you talking. Put back the specifics it smoothed away, the actual number, the actual program name, the actual week it happened.

The draft is raw material. What goes out should be yours in every sentence.

### 3\. Summarizing and condensing

**Good for:** Meeting notes into tasks and follow-ups. A forty-page funding announcement into the requirements that apply to you. A long email thread into the decision that got made.

This one is already running in your organization whether or not anyone calls it an AI project. When we ran our audit at Habitat Michigan, turning meeting notes into tasks was one of only four items out of twenty-one that scored both high impact and low difficulty.

**How it fails:** By potentially leaving things out. A summary of a document that contained six important things could hand you five clean bullet points, and nothing in those five bullets tells you a sixth existed. The dissent gets dropped. The condition on the funding gets dropped. The caveat somebody added at the end of the meeting gets dropped.

**What checking means:** Going back to the source to look for what is absent, which is a different skill from reading for errors. It is also the reason this one is harder than it sounds, because you asked for the summary specifically to avoid reading the source.

Two things that can help here: Ask it what it left out. Then ask what the strongest disagreement or the biggest risk in the document was. If either answer contains something your summary did not mention, go and read that section yourself.

### 4\. Research and facts

**Good for:** Orienting yourself in an unfamiliar area. Building a starting list of sources. Getting the shape of a funder's priorities before you read their guidelines properly.

**How it fails:** Confidently. It can give you a statistic, attach a plausible-looking citation, and be wrong. The output carries no signal that the number it gave you is incorrect or in the wrong context.

**What checking means:** Opening the source. Every number and every citation: verify it. If you cannot find the source, the number does not go in the document. Similar to the above item, you can ask it to show you the source of a stat it gave you. Once when I did that, it found its mistake on its own, corrected it, explained how it made the mistake, and gave me the source and detailed explanation for the correct answer.

For nonprofits this is the highest-stakes category on the list, because the number does not stay just in your notes. It ends up in a grant narrative, an appeal letter, or an annual report, next to your organization's name and above somebody's signature. I wrote a full edition on [where this gets dangerous in grant work](https://www.linkedin.com/pulse/ai-grant-writing-what-can-do-cant-when-gets-dangerous-wendy-clow-butmf) back in June, so I will not repeat it here. The short version is the line the Chronicle of Philanthropy quoted from me: it is really easy for AI to help you look bigger than you are.

### 5\. Extracting and sorting at volume

**Good for:** Pulling data out of documents. Triaging and routing incoming email. Categorizing notes. Converting files into a standard format. Our audit list had several of these on it, including email triage for the loan packaging team and converting client photos into standardized PDFs.

**How it fails:** Silently, and then identically, four hundred more times. A single bad judgment may not show up as just one error. It can show up as the same error applied consistently across every record, which is the version hardest to spot, because consistency is what correct output also looks like.

**What checking means:** Sampling, which is a habit most of us do not have. Pull twenty at random and check them properly. Then deliberately check the edges: the oldest record, the one with a blank field, the household with two different last names, the name with an apostrophe in it, the gift that came in as a negative number.

### 6\. Lightweight software

**Good for:** Small tools that do one thing. A form that feeds a spreadsheet. A script that renames a folder of files. This is the vibe coding the original article was about, and it has genuinely put simple software within reach of people who could never build it before, which I think is one of the best things AI has done.

**How it fails:** Later. It works on the three cases you tried it on, and it keeps working until the day somebody enters a date in a different format or a name with an apostrophe, and then it either stops or, worse, keeps going and gets it wrong.

**What checking means:** Testing it, on purpose, with input designed to break it. Leave a required field empty. Type the date the wrong way round. Use a name with punctuation in it. Run it on last year's data where you already know the right answer and see whether it agrees with you.

This is the only one of the six where checking is literally a test rather than a read, and it is the reason software people have review and testing built into their process at all.

### The part I actually want you to take away

Look at the order those six are in.

At the top, the failures are cheap and obvious. A bad brainstorm suggestion is low risk. A weak first draft is visible in the first paragraph, because you read every word before it goes out.

At the bottom, the failures are expensive and invisible. A miscategorized donor file looks exactly like a correctly categorized one. A script that mishandles apostrophes keeps producing output the whole time it is wrong.

Now notice what else changes as you go down that list. The tasks at the bottom are the ones that feel most like relief. Handing over a forty-page document, or four hundred records, or a job you do not know how to do yourself, feels like getting your afternoon back. It genuinely is. Your ability to notice a mistake drops at exactly the point where the volume goes up and the work gets handed over most completely.

Nobody proofreads a summary against the original. The entire reason you asked for a summary was to avoid reading the original.

So here is the rule I would write on the wall:

**The harder a mistake would be to spot, the harder you should look for it.**

Before you hand a task over, ask yourself one question. If this came back wrong, how would I find out? When you do not have an answer, you have found the work that needs checking.

Most of us do the opposite without thinking about it. We read the board memo four times because the board matters, and we accept four hundred categorized records without opening any of them because the task was boring.

### Your name, your voice, your truth

I will say the same thing [I said on Monday](https://lnkd.in/p/d2nBYXZk), because it is the part that matters most for our sector.

Never let AI speak for you. You control the message, the voice, and whether what goes out is true. Let it replace the blank page and get you moving. The finished piece should be yours.

The relationships you have with your supporters, your donors, and the people you serve took years to build, and they are not the place to take your hands off the wheel.

For the record, and because I told you I would: I used AI to get to a first draft of this article. Then I did everything in #2 to it.

---

If you want to talk through where AI is already being used in your organization and what checking it should look like, I do free 30-minute consultations. Send me a DM and we will get it on the calendar.