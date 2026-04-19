---
type: "Web"
authors: "[[Mehmet Gökçe]]"
url: "https://mehmetgoekce.substack.com/p/i-built-karpathys-llm-wiki-with-claude"
published: 2026-04-08
created: 2026-04-19
tags:
---


![](https://substackcdn.com/image/fetch/$s_!dX3h!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6468fe7a-04b6-4e7b-aef0-099a44de3f26_1600x900.png)

On April 4, Andrej Karpathy dropped [a gist called “LLM Wiki”](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Within days it had over 5,000 stars. The idea was simple and powerful: instead of scattering your notes across a dozen tools, let an LLM maintain a structured wiki for you. Feed it raw sources. It extracts facts, cross-references them, and keeps the whole thing internally consistent. The wiki becomes a persistent, compounding artifact — not a graveyard of stale notes.

Everyone loved the concept. But here is the thing: almost nobody actually built one. The gist describes a pattern, not an implementation. It tells you *what* to build — three layers, three operations — but not *how* to wire it up with real tools, real files, and real workflows. It is a blueprint for a house, not the house itself.

I built the house. With Claude Code as the LLM brain and Logseq as the wiki UI. After the first few days of use, my wiki has 46 pages across 8 namespaces, automated health checks, and a two-layer cache architecture that turned out to be the key insight Karpathy’s gist does not mention. Here is exactly how it works. The full implementation is open source: [github.com/MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki).

## The Problem: Scattered Knowledge

If you run any kind of technical practice — freelancing, consulting, a side project with ambitions — your knowledge scatters fast. Jira has your tickets. Confluence has your docs. Your CMS has blog drafts. Slack has decisions buried in threads. Your note app has half-finished thoughts. Your AI assistant’s memory has coding rules you taught it three months ago.

The traditional answer is search. RAG (Retrieval-Augmented Generation) lets you query across all these sources. But RAG rediscovers everything from scratch with every query. There is no persistent synthesis. Ask it the same question next week and it does the same work again, possibly arriving at a slightly different answer.

Personal wikis are the alternative — but they die. Everyone starts one. Almost nobody maintains one. As Karpathy puts it in the gist: “the tedious part of maintaining a knowledge base is not the reading or the thinking — it’s the bookkeeping.” Updating cross-references, fixing broken links, keeping metadata current, noticing when information becomes stale. That is death by a thousand paper cuts.

LLMs are perfect at bookkeeping. They do not get bored. They do not skip the cross-reference update because it is Friday afternoon. That is the core insight behind the LLM Wiki pattern.

## Karpathy’s Pattern in 30 Seconds

The gist defines three layers:

1. **Raw Sources** — URLs, papers, conversations, whatever you feed it
2. **The Wiki** — Structured, cross-referenced pages synthesized from those sources
3. **The Schema** — Rules that govern the wiki’s structure (namespaces, required fields, lint checks)

And three operations:

1. **Ingest** — Process a new source, update affected wiki pages
2. **Query** — Search the wiki, synthesize an answer
3. **Lint** — Health check for orphan pages, stale content, broken references

The key insight: “the wiki is a persistent, compounding artifact.” Every ingest makes it more valuable. Unlike RAG, which starts fresh every time, the wiki accumulates refined knowledge over time.

I am not going to rehash the full gist here — [go read it](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), it is short and well-written. What follows is how I turned it into a working system.

## My Stack: Claude Code + Logseq

### Why Claude Code

Claude Code is Anthropic’s CLI tool for Claude. Three features make it the right LLM layer for a wiki:

- **Built-in memory system.** Claude Code has a `CLAUDE.md` file (project instructions loaded every session) and a `memory/` directory for persistent notes. This becomes my L1 cache — more on that in a moment.
- **Custom slash commands.** You can create skills (markdown files that define workflows) and invoke them with `/wiki ingest`, `/wiki query`, `/wiki lint`. The skill reads the schema, operates on the files, and reports back.
- **Direct file access.** Claude Code reads and writes local files. No API wrappers, no intermediate databases. It operates directly on the same markdown files that Logseq renders.

### Why Logseq Over Obsidian

Karpathy’s gist mentions Obsidian. I went with [Logseq](https://logseq.com/) instead, and I think its architecture is actually better suited for LLM-generated content. Here is why:

- **Outliner format.** Every block (line) in Logseq is independently addressable. When Claude updates a wiki page, it can append a new block without touching existing content. In flat markdown, you are always fighting with document structure.
- **Properties syntax.** Logseq uses `property:: value` inline syntax instead of YAML frontmatter. Structured metadata lives right next to the content, which makes it trivial for an LLM to read and update.
- **Graph-native backlinks.** Bidirectional links are automatic. When page A links to page B with `[[Wiki/Tech/Strapi]]`, Logseq shows that reference in page B’s backlinks panel. No manual effort required.
- **Namespace hierarchy.** Logseq uses `/` as a namespace separator — `Wiki/Tech/Strapi`, `Wiki/Projects/OpenShell-Series`. This maps naturally to a wiki’s category structure. On disk, the files use triple underscores: `Wiki___Tech___Strapi.md`.
- **Open source and local-first.** Logseq is AGPL-3.0 licensed. Your data stays as plain markdown files on your machine. No cloud sync requirement, no vendor lock-in. For a knowledge base that may contain sensitive project details, this matters.

The outliner format does take getting used to — every line starts with `-` — but once you internalize it, the structure actually makes more sense for a wiki than flat prose.

## The L1/L2 Architecture

This is the part that is not in Karpathy’s gist, and it turned out to be the most important design decision.

When I started building the wiki, my plan was simple: migrate everything into Logseq. All my project notes, coding rules, deployment gotchas, personal preferences — one system to rule them all.

It took about a day to realize this was wrong.

Some knowledge must be available in every single session, before I even ask a question. Things like “always use `ö/ü/ä`, never `oe/ue/ae` “ or “max 2-3 SSH calls to the VPS, never 10+, or you risk an OOM reboot.” If Claude has to query the wiki to learn these rules, it has already made the mistake.

Other knowledge only matters in specific contexts. The full history of a blog series. The detailed Strapi API publishing workflow. The evaluation of a marketing strategy. Loading all of this into every session would waste the context window and slow things down.

The solution maps to a concept every engineer knows: **CPU cache hierarchy.**

- **L1 = Claude Code Memory (~14 files).** Small, fast, always loaded. Contains rules, gotchas, identity, preferences, and credentials. Loaded automatically at the start of every session. No `/wiki query` needed.
- **L2 = Logseq Wiki (~46 pages).** Large, structured, on-demand. Contains projects, workflows, research, deep technical knowledge. Queried via `/wiki query` when you need it.

![](https://substackcdn.com/image/fetch/$s_!BuJ_!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd694abdf-de4c-41a0-94c7-bf208bbf8798_6720x2631.png)

The routing rule is simple: **Would Claude making a mistake without this knowledge be dangerous or embarrassing?** Then it belongs in L1 — auto-loaded every session. **Would the mistake be merely inconvenient?** Then L2, queried on demand.

For example: my business address changed last year. If Claude uses the old address on a proposal, that is embarrassing. That goes in L1. But the detailed timeline of a book project? If Claude does not know that without being asked, nobody gets hurt. That is L2.

Credentials are a special case — they *must* live in L1, because the wiki is git-tracked. Putting an API token in a Logseq page means putting it in a git repository. The L1 memory directory is excluded from git, making it the only safe place for secrets.

## The Schema: Your Contract with the LLM

Karpathy’s gist mentions a schema layer, but keeps it abstract. In practice, the schema is the single most important file in the system. It is the contract between you and the LLM that governs how every wiki page gets created and maintained.

My schema lives at `Wiki___Schema.md` — a regular Logseq page that the `/wiki` skill reads before every operation. Here is an abbreviated version:

```markup
- wiki-version:: 1.0
- type:: schema
- ## Namespace Conventions
  - Top-Level: Wiki/Business, Wiki/Tech, Wiki/Content,
    Wiki/Projects, Wiki/People, Wiki/Learning,
    Wiki/Reference, Wiki/Careers
  - Page Naming: Title Case, hyphens for multi-word
  - Max depth: 3 levels
  - Files on disk: Triple-underscore separator
    (Wiki___Tech___Strapi.md)
- ## Page Types & Required Properties
  - ### Entity (Person, Client, Tool)
    - type:: entity
    - entity-type:: person | client | tool
    - created:: YYYY-MM-DD
    - updated:: YYYY-MM-DD
    - status:: active | inactive | archived
  - ### Project
    - type:: project
    - status:: active | completed | on-hold
    - created:: YYYY-MM-DD
    - updated:: YYYY-MM-DD
  - ### Knowledge
    - type:: knowledge
    - domain:: tech | business | content
    - confidence:: high | medium | low | stale
  - ### Feedback (Lessons Learned)
    - type:: feedback
    - severity:: critical | important | nice-to-know
  - ### Hub (Namespace Index)
    - type:: hub
    - namespace:: (the namespace this hub indexes)
- ## Lint Rules
  - Orphan Detection: Pages with 0 incoming links
  - Stale Detection: updated:: > 90 days AND confidence:: high
  - Credential Leak: Regex scan for token/password/secret
  - Cross-ref Minimum: Every page needs at least 1 outgoing link
  - L1/L2 Duplicates: Same info in Memory AND Wiki → warning
- ## L1/L2 Boundary
  - L1 (Memory): Rules, gotchas, identity, credentials
  - L2 (Wiki): Projects, workflows, research, deep knowledge
  - Same info in both? → Lint warning
```

Eight top-level namespaces. Five page types, each with required properties. Lint rules that can be checked automatically. And the L1/L2 boundary defined explicitly so the system knows where new knowledge should be routed.

The key point: **without a schema, the LLM creates inconsistent pages.** One page might use `status: active`, another `state:: running`, a third has no status field at all. With a schema, every page follows the same contract, and automated quality checks become possible. It is the difference between a wiki and a pile of notes.

## The /wiki Skill: Claude as Wiki Maintainer

The schema defines the rules. The `/wiki` skill is the engine that enforces them. It is a Claude Code custom slash command with five sub-commands:

![](https://substackcdn.com/image/fetch/$s_!5eCw!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c5c9787-6b1c-4f9a-938f-83b1db94c4b4_1400x532.png)

### Ingest: The Core Operation

Ingest is where the magic happens. When you run `/wiki ingest "Published Part 2 of the OpenShell series"`, here is what Claude does:

![](https://substackcdn.com/image/fetch/$s_!oeu4!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd096bad-9fe7-42b4-a9f9-08bd5166ad1d_7428x620.png)

**Phase 1 — Analyze & Extract.** Claude reads the source (a URL, a file, or plain text) and extracts entities, facts, relationships, and dates. It classifies each piece as business, technical, content, or project knowledge.

**Phase 2 — Scan Wiki.** Claude reads the schema, then scans existing wiki pages to find which ones the new information affects. This is where the cross-referencing happens — if you mention a tool that already has an entity page, Claude knows to update that page too.

**Phase 3 — Update Pages.** Claude creates new pages (with all required properties from the schema) and appends to existing pages. The rule is *append, never overwrite* — existing content is sacred. Target: 5-15 page touches per ingest.

**Phase 4 — Quality Gate.** Before committing, Claude checks: Do all new pages have the required properties? Does every page have at least one cross-reference? Are there any credential patterns in the content? If something fails, it fixes it before proceeding.

**Phase 5 — Report.** A summary of pages created, pages updated, cross-references added, and any warnings.

That single ingest about Part 2 of a blog series might touch the project page (`Wiki/Projects/OpenShell-Series`), the Substack content page, the blog page (noting the German adaptation), the active projects hub, and the content pipeline page. Five pages updated from one sentence of input.

### Query and Lint

**Query** works like a smart search: Claude parses your question, identifies the relevant namespaces and entities, reads the top 3-5 matching pages, and synthesizes an answer with source attribution. If the query reveals a gap in the wiki, it offers to create a new page.

**Lint** is the automated health check. It scans every `Wiki___*.md` file and checks for: orphan pages (no incoming links), stale content (last updated 90+ days ago but still marked high-confidence), missing required properties, broken `[[references]]` to pages that do not exist, and credential patterns that should not be in a git-tracked file. Run it with `--fix` and Claude auto-repairs what it can — creating stub pages for broken links, downgrading stale confidence levels, adding missing hub entries.

## Before & After: What a Good Wiki Article Looks Like

The difference between a dead wiki and a living one is the quality of individual pages. Here is what a placeholder looks like versus a synthesized wiki article.

**Before** (3 lines, written when the page was first created):

```markup
- type:: knowledge
- domain:: content
- ## Substack
  - To be filled via /wiki ingest.
```

**After** (synthesized from 10+ sources over multiple ingest operations):

```markup
- type:: knowledge
- domain:: content
- confidence:: high
- created:: 2026-04-07
- updated:: 2026-04-07
- ## m3mo Bytes (Substack)
  - English tech publication. Deep-dives on AI,
    distributed systems, software engineering.
  - ### Metrics
    - | Metric | Value | As of |
      |--------|-------|-------|
      | Subscribers | ~88 | 2026-03-23 |
      | Published articles | 2 | 2026-04-07 |
      | Cadence | biweekly | — |
      | Paid tier | NO (trigger: 500 subs) | 2026-03-23 |
  - ### Monetization Decision
    - No paid tier until 500 subscribers
    - Real conversion rate: ~3% (not 5-10% Substack claims)
    - At 88 subs → ~3 paid subs = not viable
  - ### Style Guide Essentials (Top 5)
    - 1. Hook in first 2-3 paragraphs
    - 2. Working code with explanations
    - 3. At least 1 Mermaid diagram
    - 4. Honest trade-offs section
    - 5. Fact-check protocol mandatory
  - ### Open Questions
    - Gradual or immediate paid tier at 500 subs?
    - Reddit strategy needs active comment history
  - ### Cross-References
    - [[Wiki/Content/Blog]] — German adaptations
    - [[Wiki/Content/LinkedIn]] — Promotion channel
    - [[Wiki/Reference/Workflows]] — Publishing workflow
```

Six principles make the difference:

1. **Synthesized, not copied.** The page distills knowledge from multiple sources into a coherent article. It is compiled knowledge, not pasted notes.
2. **Dated metrics.** Every number has an “as of” date. When the subscriber count changes, you update the number *and* the date. No ambiguity about freshness.
3. **Decisions with rationale.** The monetization section does not just say “no paid tier” — it explains *why* with actual conversion math.
4. **Layered detail.** The style guide section has the top 5 rules inline and a file path to the full 26K guide. You get the essentials at a glance and can drill deeper when needed.
5. **Cross-referenced.** Every page links to related pages. The Substack page links to the blog (German adaptations), LinkedIn (promotion), and workflows (publishing process).
6. **Honest about open questions.** The “Open Questions” section explicitly names what is unresolved. This is incredibly valuable when you come back to a topic after weeks.

A good wiki article is compiled knowledge, not copied notes.

## Trade-offs & What I’d Do Differently

No system is perfect. Here is what I have learned after the first week:

**The schema feels overengineered at first.** With 10 pages, defining 5 page types and 8 lint rules seems like overkill. At 46 pages, I am already grateful for the consistency. I expect it to pay off even more past 100 pages. If you are starting small, define the schema anyway — it is much harder to retrofit one later.

**Logseq’s outliner format takes adaptation.** Every line starting with `-` is not natural if you come from flat markdown. Tables inside outliners are especially awkward. But the tradeoff — every block being independently addressable — is worth it for LLM-generated content.

**Two systems means you need a clear boundary.** Having both L1 (Memory) and L2 (Wiki) means you could accidentally put the same information in both places. The lint rule that checks for L1/L2 duplicates exists precisely because this happened to me during the initial migration.

**Parallel agents can conflict.** During the initial migration, I had multiple Claude agents writing to wiki files in parallel. The parallel edits caused conflicts — in one case, German umlauts were silently replaced with ASCII equivalents. Lesson: treat wiki files like a shared resource and avoid concurrent writes.

**Start with fewer hub pages.** I created hub pages for every namespace upfront. In hindsight, I would let them emerge organically from ingest operations. Some namespaces only got 2-3 pages, which makes the hub feel empty. Let the content dictate the structure, not the other way around.

## Takeaway

Karpathy was right: “the tedious part of maintaining a knowledge base is not the reading or the thinking — it’s the bookkeeping.” LLMs are perfect for bookkeeping. They do not get bored, they do not skip the cross-reference update, and they can enforce a schema across 46 pages without breaking a sweat.

The L1/L2 split is the missing piece that makes this practical. Without it, you either overload the context window with project details that only matter occasionally, or you risk the LLM not knowing a critical rule because it did not think to query the wiki first. Auto-loaded rules in L1, deep knowledge on demand in L2. Like CPU cache hierarchy for your brain.

You can build this in a single session with Claude Code and Logseq. Define your schema. Create the `/wiki` skill. Ingest your first few sources. The wiki will be sparse at first — that is fine. Every ingest makes it denser, better cross-referenced, more valuable. The compounding effect is real.

Already, I reach for `/wiki query` before searching my email or Confluence. The wiki has the synthesized answer, with dates and rationale, ready to go. That is the promise Karpathy described. It actually works.

The tool is open source: [github.com/MehmetGoekce/llm-wiki](https://github.com/MehmetGoekce/llm-wiki). Setup takes 5 minutes.

What is your approach to knowledge management with LLMs? Are you using RAG, a wiki pattern, or something else entirely? I would love to hear what is working — and what is not — in the comments.

*Subscribe to m3mo Bytes for more deep-dives on developer tools and AI workflows.*