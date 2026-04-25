---
type: Web
authors: '[[Andrew NgI]]'
url: >-
  https://www.deeplearning.ai/the-batch/why-we-need-more-compute-for-inference/?utm_campaign=The%20Batch&utm_medium=email&_hsenc=p2ANqtz-_ucu3lMo9V8LkUGWfG3iHl-uO5UiqIO6BTsZKz0tWJBLxcayptlpI_YhoDkxbSRXUwfDmDIiq4bofgdXXztckcc-bKtcfzPOTumLWzimKF6dZNIpk&_hsmi=385367404&utm_content=385366194&utm_source=hs_email
published: 2024-04-24T00:00:00.000Z
created: 2026-04-24T00:00:00.000Z
tags:
  - trendy-AI
  - LLM
  - strategia-AI
---


## Why We Need More Compute for Inference Today, large language models produce output primarily for humans. But agentic workflows produce lots of output for the models themselves — and that will require much more compute for AI inference.[Letters](https://www.deeplearning.ai/the-batch/tag/letters/)

[

Technical Insights

](https://www.deeplearning.ai/the-batch/tag/technical-insights/)

![Why We Need More Compute for Inference: Today, large language models produce output primarily for humans. But agentic workflows produce lots of output for the models themselves — and that will require much more compute for AI inference.](https://www.deeplearning.ai/_next/image/?url=https%3A%2F%2Fcharonhub.deeplearning.ai%2Fcontent%2Fimages%2F2024%2F04%2FTOKEN-GENERATION-1.png&w=3840&q=75)

Why We Need More Compute for Inference: Today, large language models produce output primarily for humans. But agentic workflows produce lots of output for the models themselves — and that will require much more compute for AI inference.

Dear friends,

Much has been said about many companies’ desire for more compute (as well as data) to train larger foundation models. I think it’s under-appreciated that we have nowhere near enough compute available for inference on foundation models as well.

Years ago, when I was leading teams at Google, Baidu, and Stanford that focused on scaling up deep learning algorithms, many semiconductor manufacturers, data center operators, and academic researchers asked me whether I felt that AI technology would continue to make good use of more compute if they kept on delivering it. For many normal desktop processing workloads, like running a web browser or a text editor, having a faster CPU doesn’t help that much beyond a certain point. So do we really need faster and faster AI processors to train larger and larger models? Each time, I confidently replied “yes!” and encouraged them to keep scaling up compute. (Sometimes, I added half-jokingly that I had never met a machine learning engineer who felt like they had enough compute. 😀)

Fortunately, this prediction has been right so far. However, beyond training, I believe we are also far from exhausting the benefits of faster and higher volumes of inference.

Today, a lot of LLM output is primarily for human consumption. A human might read around 250 words per minute, which is around 6 tokens per second (250 words/min / (0.75 words/token) / (60 secs/min)). So it might initially seem like there’s little value to generating tokens much faster than this.

But in an [agentic workflow](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-8p1gYrpU0XxUFNfmSS3kol8W5-7e4O-CZDhoB8qzXDRMbt3ivdmVgXC7rhNTbUafmUHpkI), an LLM might be prompted repeatedly to reflect on and improve its output, use tools, plan and execute sequences of steps, or implement multiple agents that collaborate with each other. In such settings, we might easily generate hundreds of thousands of tokens or more before showing any output to a user. This makes fast token generation very desirable and makes slower generation a bottleneck to taking better advantage of existing foundation models.

That’s why I’m excited about the work of companies like [Groq](https://groq.com/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-8p1gYrpU0XxUFNfmSS3kol8W5-7e4O-CZDhoB8qzXDRMbt3ivdmVgXC7rhNTbUafmUHpkI), which can generate hundreds of tokens per second. Recently, [SambaNova](https://fast.snova.ai/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-8p1gYrpU0XxUFNfmSS3kol8W5-7e4O-CZDhoB8qzXDRMbt3ivdmVgXC7rhNTbUafmUHpkI) published an impressive demo that hit hundreds of tokens per second.

Incidentally, faster, cheaper token generation will also help make running evaluations (evals), a step that can be slow and expensive today since it typically involves iterating over many examples, more palatable. Having better evals will help many developers with the process of tuning models to improve their performance.

Fortunately, it appears that both training and inference are rapidly becoming cheaper. I recently spoke with Cathie Wood and Charles Roberts of the investment firm ARK, which is famous for its bullish predictions on tech. They [estimate](https://www.ark-invest.com/big-ideas-2024?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-8p1gYrpU0XxUFNfmSS3kol8W5-7e4O-CZDhoB8qzXDRMbt3ivdmVgXC7rhNTbUafmUHpkI) that AI training costs are falling at 75% a year. If they are right, a foundation model that costs $100M to train this year might cost only $25M to train next year. Further, they report that for “enterprise scale use cases, inference costs seem to be falling at an annual rate of ~86%, even faster than training costs.”

I don’t know how accurate these specific predictions will turn out to be, but with improvements in both semiconductors and algorithms, I do see training and inference costs falling rapidly. This will be good for application builders and help AI agentic workflows lift off.

Keep learning!

Andrew

![](https://www.deeplearning.ai/_next/image/?url=https%3A%2F%2Fhome-wordpress.deeplearning.ai%2Fwp-content%2Fuploads%2F2025%2F10%2FVertical-side-banner-ads-10.png&w=3840&q=75)
