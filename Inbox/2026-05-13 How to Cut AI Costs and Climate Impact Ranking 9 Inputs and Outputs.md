---
type: "Web"
authors: "[[Andy Crestodina]]"
url: "https://www.orbitmedia.com/blog/ai-costs-climate-file-formats/?utm_campaign=ai-costs-climate-file-formats&utm_medium=email&_hsenc=p2ANqtz-8I5W30XRdMQKWg8-YD1_HMqtYqWWLGIJDXrxO3vqkkFO6fJaGhKfcj5LxVMwH2G2s_4H7N0N6EqlxaH-DnUSB96RyQu3DZALwRgN6dgsW_qfJvAvk&_hsmi=418612619&utm_source=may14-newsletter"
published: 2026-05-13
created: 2026-05-14
tags:
---


Every AI prompt has two prices.

One shows up on your invoice. The other gets paid in carbon, electricity and water. Both are driven by token usage and what you upload to and export from the AI. And the file formats you choose can change the bill by 10x.

**Why do some files require more processing?**  
There are three factors that combine to determine how hard the AI has to work with any file.

1. Does the AI need to use a tool to open the file or generate the output?
2. How much structural noise (tags, formatting, styles) does the file format require?
3. Is anything being processed as an image instead of text?

Some file types that have lots of formatting and visuals. These require much more processing power. Here’s a simple way to remember this:

- **If you need software to open it, it’s expensive** (DOCX, PPTX, XLSX, PDF)
- **If you can open it in Notepad, it’s efficient** (TXT, MD, CSV, JSON, HTML)

If you need some desktop software to open the file, then the AI needs libraries and tools to parse the file. These libraries and tools add tokens and carbon cost. It may be obvious. You can sit back and watch the AI work harder (and slower) on these files.

**Imagine you’re working on a big report and getting help from AI…**

You can generate all kinds of file formats using AI. Which do you choose?

To get a sense for which file formats are the most popular with marketers, we put a little poll on LinkedIn. We had about 500 responses to the question “When you ask AI to make a big deliverable, what format do you ask for?” The top answer was DOCX by a wide margin.

![Poll results showing 54% of marketers prefer AI deliverables in DOCX format, followed by PDF (21%), PPTX (13%), and HTML (12%); 484 total votes.](https://www.orbitmedia.com/wp-content/uploads/2026/05/marketers-word-docs.png) But those are all very different types of files, each requiring very different levels of effort from the AI to generate. They have different costs in terms of tokens (processing power), electricity (carbon output) and credit usage (money).

**Which file formats have the highest costs?**

To measure that difference, I took a recent article and gave it to Claude in six different file formats, then analyzed the token count using the “v1/messages/count\_tokens” API endpoint. I measured in both directions:

- **Input Measurement (added to prompts):** I asked the AI to “summarize” the piece as provided in the six formats, including a nicely designed PowerPoint version of the article that I’ve used in presentations.
- **Output Measurement (generated for downloading):** I then reversed the process and asked AI to “generate” the content in those same file formats.

Here is the relative cost in tokens, which translates directly into energy consumption, environmental impact and financial cost. You can see that mileage varies.

The difference is huge. HTML and PDF are expensive to read but cheap to write. DOCX is expensive in both directions. PPTX is by far the heaviest, slowest and most expensive in the bunch.

Let’s look closer and consider more file formats. This table explains how AI sees the files and handles the processing, in and out.

![Table comparing the AI efficiency of 9 input and output formats, ranked by reading and generating effort from lowest to highest, including TXT, CSV, HTML, PDF, DOCX, XLS, PPT, SVG, and JPG.](https://www.orbitmedia.com/wp-content/uploads/2026/05/9-Inputs-and-Outputs-Ranked-by-AI-Efficiency.webp)

Let’s look closer at the rankings, share tips and consider lighter-weight alternatives to the heavy, popular options.

## The formats, use cases and alternatives

**1\. Text Files (TXT)  
**The smallest, lightest file possible. But contains no formatting. Good for large amounts of text where formatting isn’t important, such as podcast transcripts.

*Lighter alternative: None.*

**2\. Markdown Files (MD)  
**Markdown is the language AI agents speak best. It’s also readable by humans and not much heavier than a TXT file. Formatting and tables are added through characters, not tags. It’s the fast, efficient champion of AI inputs. It’s also great as a draft that you can edit within the AI, getting all of the content ready before publishing to a heavier format.

*Lighter alternative: None.*

**3\. Comma Separated Files (CSV)  
**Lightweight, structured and easy for AI to parse. Great for simple tables, lists, exports, keyword research, analytics data and CRM records. No formatting, formulas or multiple sheets. Just rows and columns.

*Lighter alternative: If it’s just a short list or simple table, paste it directly into the prompt.*

**4\. Web Pages (HTML)**  
HTML was our least common answer in the LinkedIn Poll above, but they have many advantages. They’re not too heavy to generate and easy to share (everyone has a browser) Maybe the ideal for reports. Then can even include interactivity, but this adds a lot of weight.

HTML files don’t play nice with Google Docs. You can’t paste HTML into a Google Doc and if you upload them to Google Drive, they don’t render the HTML when you open them.

*Lighter alternative: If you don’t need print-ready formatting, MD carries the same content at a fraction of the cost.*

**5\. Word Docs (DOCX)**  
This is the most common file format for outputs, according to our little LinkedIn Poll above. No surprise. It’s still a standard for word processing. But it’s a heavy file format with lots of tags and formatting. It wasn’t built for AI.

Like all archive formats, these need parsing on the way in and libraries on the way out.

- Instead of importing a DOCX file to AI, convert it into an MD file and then upload (use Google Docs or save to TCT then change the file extension)
- Instead of exporting a DOCX file from AI, make an MD file then paste it into a fresh DOCX file (fast, easy, but may require a little manual styling)

*Lighter alternative: MD for drafts, HTML for polished-looking documents.*

**6\. Excel Files (XLSX)**  
Useful when you need multiple sheets, formulas, filters, formatting or charts. But all of that structure adds weight. For AI inputs, XLSX files are overkill unless you need formulas and logic.

*Lighter alternative: If you don’t need formulas or formatting, CSV does the same job at a fraction of the cost.*

**7\. PowerPoint Files (.PPTX)**  
These have a very high cost output. They require a ton of processing. Every layout decision in every slide is all code that the AI has to read. And images require a separate, slower model. Those visuals drive up the bill.

Better yet, just don’t mix AI and PPTX files if you’re concerned about costs. If you need to make a PPTX in AI, produce the output just once, at the very end of the process.

And don’t use AI for small edits to decks. It’s faster and cheaper to make little changes manually in PowerPoint. If you must edit within the AI, be explicit: “Just regenerate slide 3, keep everything else the same.”

*Lighter alternative: If the slide format isn’t the deliverable, an HTML file carries the same content far more cheaply.*

**8\. PDF Files**  
If you’re building a Custom GPT, Claude Project or Gemini Gem, you may be tempted to upload some relevant PDFs. But before you do, start with this prompt: *“I’m planning to add this PDF document to your knowledge sources, so let’s convert it to an MD file first. But before we do, what should be trimmed? Or consolidated”*

The AI will suggest edits that will reduce costs without sacrificing quality. And the smaller file (MD, not PDF) will make all future conversations with this project cheaper and lower-emissions. It’s a double-win.

*Lighter alternative: Use MD for text-heavy documents, HTML for designed reports*

**9\. Images (PNG / JPG)**  
AI image generation is not done with an LLM. It’s a separate model that uses “visual tokens.” If you’ve had AI make pictures, you’ve seen how slow it is. That’s because it requires a lot of processing power.

If you’re only worried about the financial costs and not the environment, you can generate images in a cheaper model (Ideogram is the best) and save the credits in your daily workhorse AI, where you sometimes hit credit limits.

*Lighter alternative: For screenshots of text, just paste the text instead, if possible.*

## Where costs multiply: editing files in AI

Here’s where things get really expensive. It isn’t obvious, but all marketers should know this:

**Every iteration on a heavy file format costs as much as making it from scratch.**

That’s right. If you ask for even a small change to that DOCX file, the AI may start over and create the document all over again, with all of that token cost, energy use and carbon impact.

Smart AI users know to work on files in a simple format, such as an.md file, where the costs are much lower. Iterate in text, then generate the final format once everything is final. Here are a few tips for efficient AI prompting:

1. **Brainstorm first, no file generation yet.** Tell the AI what you want to make, but instruct it not to make the final format yet… *“Don’t generate the DOCX output until I ask for it. Let’s refine the idea first…”*
2. **Ask for lightweight previews.** While working on the draft, ask it to show a simple markdown format you can preview… *“Show a preview in a lightweight markdown format so I can review it efficiently.”*
3. **Iterate in the text.** Have the conversation about content in MD or right in the chat. Get the structure right, get the wording right, get the order right, all in plain text, where iterations are cheap.
4. **Batch your changes.** If you have five edits, give all five in one prompt. Each prompt that edits a heavy file pays the full regeneration cost. Five separate change prompts is 5x the cost. One consolidated change prompt that lists five edits is 1x the cost. *“Change X to Y and move it up in the doc. Remove Z completely.”*
5. **Ask for the final format once, in the end.** Don’t ask for the output until you’re ready for showtime. This is the single biggest efficiency win. All set? Content locked in? Now have it make the big file once and once only. “ *Changes are final. Now generate the DOCX file. Use these styles…”*
6. **One more final tweak? Do it outside the AI.** Export the big file and make final final changes (there’s always one more, right?) after it’s landed on your computer. Download it → Review it → Tweak it → Ship it

Having AI make tweaks to a DOCX or PPTX file is slow, processor intensive and uses more energy than necessary. It’s like driving a giant truck a half block to pick up a few groceries.

## Let’s ask the experts: “Which are the best file formats for AI?”

Marketing veterans and AI experts make thoughtful cases about AI efficiency and file formats.

---

| ![A man with glasses is smiling in this black and white portrait photo.](https://www.orbitmedia.com/wp-content/uploads/2024/08/chris-penn.png) | ###### Chris Penn, Trust Insights  **Choose the smallest model that will get the job done.**   *“In tools like Gemini, ChatGPT, and Copilot, there are a range of model choices but they all tend to fall in two categories: fast and dumb (instant, fast, Flash, etc.), slow and smart (pro/thinking/etc.) The smaller and faster (and dumber) the model is, the less energy it uses.*  *My rule of thumb: if you’re doing a task that requires less than two rounds of revision, use a fast model. Example: summarizing an email, etc. If you’re doing a task that requires more than two rounds of revision, use a slow model, but know it imposes a much heavier carbon cost.”* |
| --- | --- |

---

| ![A smiling man in formal attire is pictured in a circular frame.](https://www.orbitmedia.com/wp-content/uploads/2024/11/john.png) | ###### John Jantsch, Duct Tape Marketing  **HTML wins on both ends. Cheaper to make, cheaper to change.   ***“I’ve been making slide decks for small business clients for 20 years. Most get opened once and never looked at again. So why am I burning an hour designing in PowerPoint when an HTML page does the same job and renders on any device the client owns? Same logic with SOPs. Nobody wants to crack open a 14-page Word doc to figure out how to post on LinkedIn. They want a link they can scroll on their phone.*  *The reason we didn’t already ship HTML is simple. You had to know HTML, or fight with a website builder. PowerPoint and Word had visual editors that a non-coder could use. AI flipped that. You describe what you want in plain English, and you get a self-contained file you can open locally or host for free. Need changes? Just ask. It rewrites in seconds.*  *It’s also lighter on the planet. HTML is plain text that the AI types directly. DOCX and PPTX are zip archives of XML that the AI has to assemble with separate code libraries. That burns far more processing every time you generate a file. And every time you ask for a small tweak to a DOCX, the AI usually rebuilds the whole document from scratch. The same edit on an HTML file costs almost nothing. Multiply that across a year of client work, and the gap is enormous.”* |
| --- | --- |

---

| ![A middle-aged man with light hair, a short beard, and a slight smile, wearing a dark collared shirt, posed in front of a plain white background.](https://www.orbitmedia.com/wp-content/uploads/2026/05/john-nugent.webp) | ###### John Nugent, Magnolia  **Slides are becoming obsolete   ***“The advancements in AI tools in the last 4-5 months have made slide/presentation tools almost obsolete. You still need to deliver in a client-friendly format, but if you’re doing custom HTML right, they won’t want to receive anything else.”* |
| --- | --- |

---

| ![A man with glasses is smiling in this black and white portrait photo.](https://www.orbitmedia.com/wp-content/uploads/2024/08/chris-penn.png) | ###### Chris Penn, Trust Insights  **XLSX files are a nightmare**   *“For tabular data, LLMs struggle natively with anything in a table format. Want to represent your data in a machine-readable format that’s also eternally compatible? Ask for JSON or even better, YAML. It converts tables into lists, and LLMs can use them perfectly – AND modify them easily. When you’re done with the LLM, use a free program like jq or yq to convert them back into a tabular format of your choosing, no AI needed.”* |
| --- | --- |

---

| ![A smiling man in formal attire is pictured in a circular frame.](https://www.orbitmedia.com/wp-content/uploads/2024/11/john.png) | ###### John Jantsch, Duct Tape Marketing  **Markdown is the next move.   ***“Drop a free tool like [MD Reader](https://chromewebstore.google.com/detail/markdown-reader/medapdbncneneejhbgcjceippjlfkmkg) into your browser, and any.md file renders cleanly the second you open it. (This is what Wikipedia runs on.) Your team’s playbooks and SOPs look like a real page without anyone fussing over fonts. You write in plain text, and the browser handles the rest. All while using the most token-friendly file that exists.*  *Perhaps today is a new beginning for you: a new format for your big deliverables (HTML) and a new file format for everyday AI collaboration (MD).”* |
| --- | --- |

---

So far, we’ve covered things you can control. Now we’ll pan out and see how your prompts fit into a much bigger picture…

## The AI cost you can’t control: training the models

Prompting isn’t the biggest cost of AI. It’s training the models. Building a model and keeping it trained requires huge amounts of energy. Every big tech firm with a frontier AI model spends at least $100M per year on training, emitting tens of thousands of tons of carbon (and methane, nitrous oxide, etc.) not to mention water (evaporative cooling to keep servers from overheating).

This is not something users like you and I can control. No matter how much or little you use AI, these companies will continue to invest, incurring financial costs for themselves and environmental costs for us all. Compare the cost for AI model training and user AI prompting:

![Table comparing the carbon footprint of AI training (~40,000 tons CO₂), one ChatGPT prompt (~3 g CO₂), and one Google search (~0.2 g CO₂).](https://www.orbitmedia.com/wp-content/uploads/2026/05/carbon-footprint.png)

When asked about this, Sam Altman recently brushed off concerns about AI’s energy use, comparing it to the food humans eat.

*“People talk about how much energy it takes to train an AI model, but it also takes a lot of energy to train a human. It takes about 20 years of life, and all the food you consume during that time, before you become smart.”*

Sounds dismissive. But he has a point about the high carbon cost for human consumption. So let’s look at that…

## If you’re really concerned about your carbon footprint…

There are two main inputs that drive the carbon footprint for you, me and everyone else on the planet: **air travel and meat eating.** AI aside, any of us can reduce our carbon footprint by cutting back a bit on these activities. This puts AI use in the proper context of each of our true individual impacts.

![Table comparing estimated CO₂ emissions from ChatGPT prompts to common activities like flights, driving, and food, showing emissions in grams and equivalent prompt counts for each activity.](https://www.orbitmedia.com/wp-content/uploads/2026/05/human-activity-vs-chatgpt.png)

## Shrink your AI carbon footprint

My friends who are the most proficient with AI talk about “token efficiency.” They work hard to reduce credit expenditures. They run the cheapest model possible for each specific job. They put data in tables to avoid prompting completely when possible. They even install AIs locally on their laptops for simpler tasks. The best AI users obsess over efficiency.

But you don’t need to be an AI pro to be efficient. Smart decisions about file formats saves processing power, carbon emissions, water use and yes, money.

Minimizing the impact of AI on the planet is all of our jobs.

### Wait, more practical insights? Yes, please!

## There is more where this came from…

The best content from this blog are available all in one place – our book. Now on its 7th edition.

**Content Chemistry, The Illustrated Handbook for Content Marketing**, is packed with practical tips, real-world examples, and expert insights. A must-read for anyone looking to build a content strategy that drives real business impact. Check out the [reviews on Amazon](https://www.amazon.com/Content-Chemistry-7th-Illustrated-Marketing/dp/1732046522/ref=sr_1_1).

![Book cover of "Content Chemistry" alongside a quote praising it as highly practical for modern digital marketing, attributed to Jay Baer, NYT best-selling author.](https://www.orbitmedia.com/wp-content/uploads/2024/11/content-chemistry-book-quote.jpg)