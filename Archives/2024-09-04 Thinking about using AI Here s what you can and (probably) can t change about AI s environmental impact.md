---
type: Web
authors: ["[[Hannah Smith]]", "[[Chris Adams]]"]
url: >-
  https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/
published: 2024-09-04T00:00:00.000Z
created: 2026-03-25T00:00:00.000Z
tags:
  - strategia-AI
  - organizacje-społeczne
  - trendy-AI
---


![The picture uses the metaphor of an ivory tower to show where decision making is done, with a representation of a neural network coming out of it, above a crowd of people's heads (shown in green to symbolise grass roots). Some of them are reaching up to try and take some control and pull the net down to them, but the image can also be read as AI targeting and some of them.](https://www.thegreenwebfoundation.org/wp-content/uploads/JamillahKnowles-Weand-AIPeopleand-Ivory-Tower-AI.jpg)

Image credit: [Jamillah Knowles](https://www.jemimahknightstudio.com/work/ai) & [We and AI](https://weandai.org/) / [Better Images of AI](https://www.betterimagesofai.org/) / People and Ivory Tower AI / [Licenced by CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Executive summary

This briefing is intended to help people with a responsibility for AI projects understand the considerations around their *direct* negative environmental impact arising from AI. We cover what to be mindful of, what mitigating strategies are available today, and their limitations.

As the climate crisis deepens, the direct negative consequences of AI on the world around us is a growing concern. This stems from the immense quantity of resources, such as electricity, water and raw materials, required to manufacture and run the infrastructure and hardware supporting such complex computations. Current predictions forecast a near doubling of electricity use from data centres between 2022 and 2026. Furthermore, what we do with AI-related hardware once it reaches the end of its life is an unanswered question. Globally, e-waste is recognised as the fastest growing waste stream in the world.

In this report, we deep dive into five key areas of knowledge that we believe serve as a useful foundation when considering your direct impacts. These are:

1. **There’s a large and growing environmental impact associated with AI adoption**
2. **Mass adoption of AI is jeopardising existing company sustainability goals**
3. **AI’s footprint can be ~~measured~~ estimated, but it’s an emerging discipline**
4. **Changing your choice of AI model and task impacts the footprint**
5. **Any AI code can be run in ways that reduce the footprint**

Armed with this knowledge, the next logical question is what can you do about it? We outline three practical actions you can take to make a difference to your direct environmental impact, and any associated limitations with this approach. These are:

1. Question your use of AI ➡️ know when to use it
2. Optimise AI use ➡️ use it responsibly
3. Prioritise getting estimates of AI’s footprint ➡️ ask for your usage data from suppliers

If you are on a journey to dig deeper into these questions and actions and need support, [get in touch](https://www.thegreenwebfoundation.org/services/).

---

## Introduction

### What is AI?

When we say *artificial intelligence* (AI) in this report, while the term goes all the way back to 1956,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#288ab581-045e-4532-b7c3-f5128e642011">1</a></sup> we’re referring to a specific subcategory of computing called *machine learning* (ML). An ML system is best considered as a predictive systemrelying on *models,* designed to perform a set of distinct tasks using statistical analysis gleaned from specific data it’s been trained on.

ML models are used in a huge range of places. In every case, the model is effectively making a prediction based on previously seen data. Photos are enhanced based on massive datasets of photos that have been classified by human experts as “good” or “bad”. Shopping recommendations are based on what people classed as “similar to you” have previously bought. Even in a conversation with an “AI” assistant, each word is down to a model making predictions about what next word is most likely to sound convincing, based on thousands of conversations previously fed into it.

Enough predictions in sequence can generate entire sentences that resemble a chat with a person. This ‘generative’ behaviour has given rise to the term *Generative AI*. Generative AI models are trained on vast sets of data enabling them to perform a growing range of tasks beyond just generating text to generating images, speech, videos.

### The story of AI’s adoption boom

The AI approach has proven to be powerful and versatile.

Generative AI in particular has captured the popular imagination, resulting in a fast and dramatic race for adoption. As an example, ChatGPT,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ab950a31-e433-4a0a-a869-64d8e85e89f5">2</a></sup> OpenAI’s flagship Generative AI service, took only two months to reach 100 million users.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#5d41eb08-f2e8-4ee1-a0e1-a973fa23ede2">3</a></sup> The same scale took Instagram two years and Facebook nearly five years.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e6882555-452f-4d32-ad1f-58bfc264e44f">4</a></sup>

In January 2023, Microsoft invested $10 billion into OpenAI, licensing their models for use across their entire product line. In response Google, whose researchers were behind the original ‘Transformer’ architecture that ChatGPT <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#6f871c6b-6179-46ab-b953-b0e4f58a8d37">5</a></sup> was based on, announced their own PaLM 2 model. This is used in over 25 products as well as Google’s flagship Search, Docs, Gmail services.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#a96c4221-fccb-4674-aa58-425c88c7ed61">6</a></sup>

The same year, Meta made their own move. In addition to investing tens of billions of dollars into their own digital infrastructure, they also released their *Llama* series of Generative AI models under a relatively permissive licence.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#d89435cf-f957-444d-94df-3b44c17e4c99">7</a></sup> This meant the models could be run by anyone with access to hardware powerful enough to run them. This can be seen as a strategic move to build an open ecosystem to counter Microsoft’s and Google’s early lead. It was interpreted as such in the technology industry, particularly after the leaked memo within Google stating, “We have no moat, and neither does OpenAI.” <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#89cb199d-8046-44e2-ac20-a5a8d496e427">8</a></sup>

#### From arms race to gold rush

As more companies entered the fray, the open ecosystem of AI models grew quickly. This drove new demand for AI-specific hardware and infrastructure. Over the last three years, large firms like Google, Amazon, Microsoft and Meta have spent a combined $130-150 billion each year on capital expenditure,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e6bceb59-5911-4eb3-a530-86fe5480e7ce">9</a></sup> publicly citing AI data centres as a primary driver of this spending.

Meanwhile, Nvidia, the company making most of the chips used for AI, has also seen its own valuation increase more than sevenfold since 2020 on the back of this boom. In June, Nvidia eclipsed Amazon, Google, Apple, and Microsoft to briefly become listed as the most valuable company in the US,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fe77a547-6c94-4848-af79-c6b3267834f8">10</a></sup> before settling back into position as the third most valuable company in the US,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fd40f252-e6ce-4928-bf67-cd6b844cb90e">11</a></sup> with a market capitalisation of more than $2.3 trillion.

Just like Nvidia’s heady valuations are based on future earnings, the investments made by the large firms mentioned above have been made on predictions of *future* demand for AI services. A growing number of organisations are hoping to catch this wave of interest by speculatively designing new AI-centered products or new AI-enabled features in existing products.

In the summer of 2024, AI is still a hot topic. OpenAI is claiming 200 million weekly active users—twice as many as it had last November.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#55c36ccb-11bf-4939-a953-7bcfb8cacd19">12</a></sup> Hundreds of billions of dollars have been invested in AI infrastructure, and this is projected to continue. Investment bank Goldman Sachs is expecting in the region of $1 trillion to be invested in AI infrastructure in the coming years.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#d9160f76-e2f4-4ba8-a7be-07aa6245e073">13</a></sup> For context, this is a figure comparable to the level of investment in telecoms infrastructure during the dot-com bubble in the late 1990’s and early 2000’s.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#bd919d60-0026-4ddd-9364-1c132f546215">14</a></sup> There are similar parallels to the productivity gains promised by increased network capacity deployed.

### Growing concerns about the deployment of AI

AI services bring a range of risks to society. In response, there’s been a Cambrian explosion of AI risk frameworks developed to document and mitigate against the associated harms from use. The MIT AI risk repository now tracks no less than 43 different AI risk frameworks, covering more than 700 separate identified risks to mitigate.

Even when we put aside these societal risks, environmental or otherwise, valid questions remain about who is actually benefiting from the wider deployment of AI models.

It’s not difficult to find reports extolling the positive climate benefits of deploying of AI, like Boston Consulting Group’s *Accelerating Climate Action with AI* <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#df9e9219-2734-49d5-98cf-dcb17d91f224">15</a></sup> and consulting firms like Accenture talking about *How Gen AI can Accelerate Sustainability*.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#42b75e6a-7ded-44f9-948d-343c384cb5c2">16</a></sup> At the same time, some of the biggest winners from AI are management consultant firms *making money selling the consulting around AI,* rather than the organisations deploying it themselves.

For context, Boston Consulting Group, and McKinsey are expecting 20% and 40% of their consulting revenue respectively to come from advising clients on how to use Generative AI in 2024. Meanwhile, corporate AI projects are turning out to have a failure rate of around 80% <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#9422c57b-4238-4167-82b6-b37526e47cf0">17</a></sup>, based on recent research from the non-profit RAND corporation—a rate twice that of standard IT projects.

One of the reasons appears to be related to the kinds of problems people are trying to solve with AI, like automating away expensive labour. If we put aside the ethical questions around doing so, it is often the automation of increasingly expensive labour that is needed to justify continued multi-hundred billion dollar investments in AI infrastructure. In the eyes of analysts at Goldman Sachs in the report *Gen AI: Too Much Spend, Too Little Benefit?*, this isn’t happening. In their view, AI is not built to solve these complex problems and is unlikely to deliver the promised benefits.

#### Will the environmental impacts of AI resolve themselves as the shine wears off?

If delivering on the promised value of AI and (in particular generative AI) is proving to be more complicated than initially suggested, then perhaps the money will dry up. Perhaps the frenzy of activity around AI, with corresponding it’s environmental impacts will go the way of hype around the Metaverse, or Blockchains.

However, this doesn’t appear to be the case. The largest tech firms’ continued guidance to stakeholders is that they intend to keep making massive investments in new AI-focussed data centres regardless. Google and Meta and Microsoft are all still bullish in their investment plans.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#cb00bf96-4b57-4d57-be8c-3a4510860dae">18</a></sup> Microsoft CFO Amy Hood is advising shareholders to expect a 15 year timeframe for seeing returns—meaning they’re prepared to keep losing money on it—and to expect further increases in infrastructure build out beyond 2025.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#de4c68e8-e2e8-43f9-9ae4-0e3f0e19a2f8">19</a></sup>

### Understanding the direct environmental impacts of AI

Now we’ve set a high level backdrop of what’s happening in the AI space, we’ll provide some guidance for thinking about the direct environmental impacts of AI. Before we do, we need to explain why we don’t cover some of the wider outcomes of deploying AI.

#### Why focus on the direct environmental impact of AI?

It’s easy to find examples of AI projects that set out to deliver sustainability outcomes. These are sometimes referred to as *AI for Good*, *AI for Climate* or *AI for Sustainability*, or under a broader term, *Tech for Good*. They’re fun to read, and fun to write about.

These projects are also often used to ward off any criticism of the direct impact of deploying AI services. The argument usually goes as follows:

*If there are positive impacts and negative environmental impacts of deploying AI, then the environmental costs are an acceptable price to pay for the benefits they offer.*

There are two problems with this argument – the first is about data, the second is about the argument itself.

##### The first problem: the data

Broadly speaking, it’s quite easy to find predictions about the positive environmental impacts of digital services or statements about the benefits they *could* deliver. **However, the sector has a relatively poor record of validating that these interventions *have* worked at the scale promised** —such that ICT Sustainability expert Vlad Coroama has coined the term *Chronic Potentialitis* to describe this lack of follow-through.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#66e5e4c7-b644-4019-9456-a8e360238a54">20</a></sup> We cover this in more detail in our own Fog of Enactment report from 2022 <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#38ffcceb-6432-40d5-97e8-f59bd7dbfe9c">21</a></sup> but we can illustrate this with a simple question.

> **Is AI being used to accelerate oil and gas extraction *more* than than it’s used to decarbonise our society?**

As it stands, Microsoft, arguably the leader in AI deployment, and one of the market leaders selling to the oil and gas sector won’t even share who’s buying AI services across the different fossil and non-fossil energy sectors with *its own staff after making commitments do so,*<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#f2236f8d-7ead-4fe7-b8fb-7c2ed20df2e5">22</a></sup> let alone with anyone else.

No technology firm we know of discloses this information either, but firms like Gartner *do* share analysis of how they expect spending on AI in the oil and gas sector to double to $2.7 billion by 2027.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#f26f2009-dcc6-48fd-9405-66cd02d04492">23</a></sup>

Elsewhere management consultancies like EY have proudly stated on their websites that “more than 92% of oil and gas companies are either currently investing in AI or plan to in the next two years,” as they chase new business.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#80565f30-c09f-420a-b51f-c46759199260">24</a></sup> A recent report from Karen Hao in the Atlantic details Microsoft aggressively chasing multiple hundred-million dollar deals to accellerate fossil fuel extraction with various oil supermajors like ExxonMobil, Chevon and Shell <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#01d0375f-544c-4ee4-855e-f9384e0b7bec">25</a></sup>.

These stories are just as important for answering the question posed above, and they highlight how right now, we don’t have the information to have a data-informed conversation about the wider impacts of AI.

So if we spend all our time talking how good “AI for Good” *could* be, without talking about how much AI capacity *actually is* *being used for fossil fuel extraction right now*, then we are falling for the same tactics of predatory delay <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e98400a9-c56b-46ae-8bcf-1a126d807d26">26</a></sup> used for the last two decades to ward off substantive action on the key driver of climate change – burning fossil fuels.

##### The second problem: the argument itself

Secondly, even if we had access to the data, the existence of an upside in any intervention, AI or otherwise, doesn’t automatically free us from the responsibility of thinking about how to mitigate the downsides. When we build systems that store sensitive data, like financial or health records, the fact that they’re useful doesn’t free us from having to think about how to keep the systems safe. AI is no different in this respect.

As we’ll see later in the briefing, these responsibilities can carry the full weight of the law behind them, and there is already plenty to think about.

#### What to expect from this briefing

This briefing is intended to help people developing an internal AI policy, or people responsible for AI projects to understand the considerations around their *direct* environmental impact.

If we deploy AI, what does all this mean for the environment? More specifically, what does it mean for those of us working in organisations with a commitment to reduce the environmental harms resulting from our activities? What mitigating strategies are available and how do these align with other strategic concerns such as productivity and profitability?

---

## 5 things every business should know about the environmental impact of AI

1\. There’s a large and growing environmental impact associated with AI adoption

2\. Mass adoption of AI is jeopardising existing company sustainability goals

3\. AI’s footprint can be ~~measured~~ estimated, but it’s an emerging discipline

4\. Changing your choice of AI model and task impacts the footprint

5\. Any AI code can be run in ways that reduce the footprint

### 1\. There’s a large and growing environmental impact associated with AI adoption

For decades, we’ve been under the illusion that digital is up in a cloud somewhere, intangible and floating harmlessly. The reality couldn’t be further from the truth. Digital infrastructure and devices are manufactured from, powered by, and located in the material world. Some of us are privileged so direct experience of these negative impacts is lessened, but they are definitely felt by many.

In the list of operations that businesses consider to have the most environmental impact, digital technologies are often overlooked. Yet, recent studies by digitally-enabled service based organisations like Salesforce <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#7c92e282-19f3-41ff-9378-218d897d0570">27</a></sup> and ABN Amro <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#923bc85e-a726-4ee6-a615-63248ad2fbdb">28</a></sup> estimate that **digital accounts for 40-50% of their organisation’s greenhouse gas emissions**. This is likely to be more than most businesses assume.

We’ll cover how digital technologies in general create harmful environmental impacts, and the role AI is playing in exacerbating this.

#### How do digital technologies create environmental impact?

All digital technologies require a range of natural resources for their manufacture and operation. This is true for the servers in data centres and the laptops and networks in our houses and offices. Here’s a brief overview of the most common environmental impacts.

##### Greenhouse gas emissions from generating electricity

Digital technologies rely on massive amounts of electricity for both manufacture and day-to-day usage. Most of the time, this comes from burning fossil fuels. Whilst we are in the middle of a generational transition away from fossil fuels to cleaner sources such as renewables, this hasn’t happened yet. The International Energy Agency’s Electricity 2024 report reminds us that **“power generation is currently the largest source of carbon dioxide (CO2) emissions in the world.” <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#538cee20-df6d-478b-9093-2bea4a2cf871">29</a></sup>**

Digital infrastructure consumed about 460 TWh of electricity worldwide in 2022—almost 2% of total global electricity demand. This equates to about one and half times the UK’s entire electricity usage. This is a growing figure too. In the same report, **the IEA expects a near doubling of electricity use from data centres between 2022 and 2026.** Such is the rate of AI data centre growth, that it warranted special attention in the IEA’s report this year. AI demand is broken out for the first time in their analysis.

![Bar chart showing the estimated electricyt demand from traditional data centres, dedicated AI data centres and crytocurrencies, 2023 and 2026, bae case. Source IEA Electricity 2024 report.](https://www.thegreenwebfoundation.org/wp-content/uploads/Data-center-electricity-demand.jpg)

Estimated electricity demands from traditional data centres, dedicated AI data centres and cryptocurrencies, 2022 and 2026, cited in https://www.iea.org/reports/electricity-2024

Within AI circles we see similar predictions. *Semi Analysis*, a publication known for in-depth analysis of trends in AI, is even more bullish about AI growth. In their own modelling, they expect AI to overtake all traditional data centre power demands by 2028**.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#4980d386-3c91-492b-92e0-c4dd3d82b2c1">30</a></sup>**

![Bar chart showing global data center critical IT power in megawatts. 2022 shows approx 40MW growing to 140,000 in 2028.](https://www.thegreenwebfoundation.org/wp-content/uploads/Global-data-center-critical-IT-power.jpg)

Data centre power capacity growth will accelerate from a 12-15% CAGR (compound annual growth rate) to a 25% CAGR over the next few years. Global Datacenter Critical IT power demand will surge from 49 Gigawatts (GW) in 2023 to 96 GW by 2026, of which AI will consume ~40 GW. Cited in https://www.semianalysis.com/p/ai-datacenter-energy-dilemma-race

Attempting to put the enormous increase in emissions into perspective at an individual user level is tricky, as we get into in part three “AI’s footprint can be ~~measured~~ estimated, but it’s an emerging discipline.” A good example comes from looking towards the impact of incorporating AI into search engines such as Google. **A single generative AI query could use 4 to 5 times more energy than a regular search engine query** <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#0d32cd14-c8c2-48e2-919f-41e6056c61a3">31</a></sup>**.** Others found that average energy consumption per search could be 6.9–8.9 Wh, compared to 0.3 Wh for a standard Google search.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#534725b8-601d-4242-8ef6-10fc091cb9f2">32</a></sup> This gives us an enormous range of 4-30 times larger. Whichever end of the scale the figures land, it’s a significant increase.

You might be wondering if the recent boom in renewable electricity generation means this isn’t a problem. It still is. **Globally, the regions with the most projected data centre capacity tend to be areas where a larger share of electricity generation comes from fossil fuels.**<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#1eb76217-8412-4949-81c8-2a5df81c9e38">33</a></sup> We can’t automatically rely on the electricity used to power these facilities to come from clean, fossil-free generation. Furthermore, hardware manufacture relies on lots of embodied energy. Embodied energy is the energy required to produce goods or services, considered as if that energy were incorporated or ’embodied’ in the product itself. These figures are not routinely published by hardware vendors, but even these vendors acknowledge this as a problem.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#d158a3ff-733d-4efd-b330-67cfb0727eba">34</a></sup>

##### Greenhouse gas emissions from building data centres

The construction of a brand new data centre requires vast amounts of concrete and steel, both of which are major sources of greenhouse gas emissions. On average, a ton of cement will produce 1.25 tons of carbon emissions, largely from the roasted limestone and silica. Concrete accounts for as much as 40% of a data centre’s construction, followed by fuel at 25% and then steel—both reinforcement and structural—which can account for 10% of a project’s carbon footprint each.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e9e48239-7d37-43a8-a013-be1c973da089">35</a></sup>

When complete, the world’s largest data centre, Switch’s Citadel campus near Reno in Nevada <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#8bdba7da-9b64-4f27-8a9a-d6fb90b1c505">36</a></sup> will occupy 7.3 million square feet, equivalent to roughly 80 football pitches. Whilst we haven’t been able to find public figures about the materials required to construct an enormous structure, we can safely assume it will be massive amounts.

##### Freshwater usage for cooling

In recent years, the water footprint associated with digital, and in particular data centre water consumption, has become a prominent issue.

A byproduct of running servers is heat. Data centres need to keep hardware cool. The most common kind of evaporative cooling systems in data centres consume significant amounts of water. In 2023 researchers from the University of Texas and Riverside <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#9db83ec5-3359-44fc-8490-95385c9c71db">37</a></sup> estimated that **training OpenAI’s ChatGPT3 large language model in Microsoft’s data centres used around 700,000 litres of fresh drinking water, and in addition, around 500ml of water was consumed for every 10-50 responses in a typical chat session.**

Why is this kind of water usage a problem? In many cases, water is drawn from aquifers in regions that are already at risk of drought and water stress.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#62774744-c12e-4211-ae17-f4bf18ea4008">38</a></sup> There are clear ethical questions about allocating fresh water for use in data centres ahead of use as drinking water by local communities or agriculture. Agreements to keep water usage secret between local authorities and tech firms <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#78961f0f-975c-4cff-abe7-00c3ea79c3e7">39</a></sup> only make this situation murkier.

There’s one other indirect link between digital technologies and water use. Because data centres use so much electricity in general, the water consumed during the generation of electricity is significant in its own right. **In the USA, around 40% of all the water drawn from lakes or rivers is used to cool nuclear and fossil fuel power plants during their operation, making it the largest single use of freshwater in the country** <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#b3632726-fcf5-40e3-b80f-cc872bd5960b">40</a></sup>**.**

##### Depletion of materials and degradation of land from mining and e-waste

Finally, there’s an environmental impact from obtaining minerals from the earth’s crust to manufacture electronics. Take two minerals, copper and gold, that are often used for their conductivity and malleability. Typically more than 100 tonnes need to be dug up to produce one tonne of refined copper. For gold, the figure is between 250 tonnes and 1000 tonnes for a single kilogram.

Once ore is dug up, various chemically intensive and energy intensive processes are needed to extract the desired minerals. These often result in toxic tailing pools and other forms of waste, making land unusable for any other purpose.

We need to be aware that these are not circular supply chains. Electronics recycling rates are generally below 20% in Europe and the USA <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#1397a44d-d4dc-4ace-b3a9-3a94609e63fe">41</a></sup>. These are regions where support for these practices is greatest. Other regions don’t fare nearly as well. **Electrical waste is named by the Baker Institute at Rice University as the fastest growing waste stream globally <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#0c02ec15-550a-4b13-bd75-d50a0d7c4e4e">42</a></sup> producing an average of 7.3 kilograms per person per year.** All this unrecyclable e-waste ends up in rubbish dumps. The most toxic place in the world is an e-waste site in Ghana according to The Science Times.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#8e65b3db-8f17-4d4c-bd14-d568e95e99d0">43</a></sup>

#### How AI is amplifying these harms

##### AI can work on conventional hardware, but increasingly relies on new specialised hardware

AI is especially compute intensive. This means the code is performing huge numbers of complex calculations and is often required to do so quickly. This requires a lot of computing resources such as CPUs, memory and storage. While AI tasks can run on conventional CPUs, they take a long time. One solution is to use lots of CPUs. Another is to use specialised CPUs. These may be more efficient per calculation run, but they’re used to perform more computations often leading to consuming larger amounts of resources.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#7761c3a0-015a-4e90-890a-a2e587cb0bd3">44</a></sup>

Additionally, manufacturing new and more specialised new hardware is much more resource intensive than reusing existing hardware.

##### AI hardware is associated with denser resource usage in the same space

In addition to individual accelerators being more power hungry, they are sold in denser clusters of hardware. In a conventional data centere, 5 to 15 kilowatts of power use per server rack is common with conventional hyperscalers towards the top end. In March 2024, the market leader Nvidia launched their DGX server taking up an entire rack, with a specified power draw of 120 kilowatts. Other infrastructure providers are aiming for higher figures per rack <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#53f41c24-11be-436f-a4d4-2328b01e70fb">45</a></sup>. More power per rack means more heat to get rid of, which often means more water to keep hardware cool.

**This denser use of new hardware leads to new infrastructure being used**

The greater power demands of hardware place different loads on the surrounding infrastructure too.

Existing grid connections to existing data centres are frequently not able to serve the required amounts of electricity without upgrades, so to meet the localised energy demand, some organisations are deploying their own fossil fuel infrastructure to meet demand crunches.

In August 2024, it emerged that Elon Musk’s xAI had begun to deploying sets of mobile fossil gas turbines to supplement the supply from the grid, to make the 100MW shortfall in power demand from their new AI datacentre in Memphis, Tennessee <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#3fd8a23f-53ad-4f44-8795-e101b207c3c1">46</a></sup>.

Elsewhere, last summer Microsoft applied for and secured planning to build a 100 MW gas turbine plant on the site of one of its larger datacentres to help meet its own demand <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#389fd84f-8ba2-4e2f-9516-097ccf5d1a9a">47</a></sup>. In some cases like Microsoft, this is not intended to run constantly, but once deployed, there is a strong incentive to use the infrastructure more to make back the costs of the initial investment.

Finally, where we *are* making progress in decomissioning fossil fuel infrastructure, like old coal power plants, AI demand growth is slowing or reversing this trend. Bringing coal generation back online that would have been retired, or in some cases building entirely new gas turbines, is seen in some circles as one of the fastest way to meet the new demand coming from AI infrastructure <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#bd0e09dc-4b5d-4613-ac66-97b6ec800002">48</a></sup>. The problems here are myriad. Once fossil fuel infrastructure is built, it can often “lock in” future emissions over the years they are expected to operate. The local pollution also shortens the lives of people living around the powerplant <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fdd27875-c1da-4e06-a3fe-73e3b5bdddfe">49</a></sup>. Even in the best scenario once its built, when this new capacity is decomissioned early, the cost of decomissioning this new fossil infrastructure, and replacing it with clean energy is often shifted onto residents through higher electricity bills.

In the energy sector, this issue of renewed or brand new fossil fuel infrastructure being used to meet new demand for AI is seen as serious enough for groups like Energy Innovation to issue dedicated policy briefs <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#4f64a057-7241-4cc3-bb57-11bb815b8052">50</a></sup> specifically aimed at heading this off.

### 2\. Mass adoption of AI is jeopardising existing company sustainability goals

The sheer amount of resources needed to support the current and forecast demand from AI is colossal and unprecedented.

This is a real, immediate concern for all organisations looking to achieve net-zero targets, or other existing sustainability goals.

Let’s look at examples of how significant AI adoption has impacted the ability of some technology industry leaders to meet their own sustainability goals. These are large, well funded companies with enviable access to talent and capital. If AI is causing them to rethink their sustainability plans, it’s reasonable to think smaller firms will need to as well.

#### How are the AI leaders faring?

Microsoft, one of the most enthusiastic adopters of AI in the technology sector, and now the largest investor of OpenAI, has seen its own emissions surge by around 45% in the last three years. Part of this has been down to its own recent investments in AI infrastructure. Microsoft spent around $50 billion in 2023 on new facilities and data centre expansion for its Azure cloud computing services which are used to power OpenAI’s products.

These investments by Microsoft have contributed to the firm missing its own supply chain decarbonisation targets, as detailed in a recent report by Stand.Earth.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#eb77915f-4145-4eb7-a796-5707c9491cc0">51</a></sup> This isn’t just because of their scale—the limited choice in suppliers creating AI hardware complicates supply chain decarbonisation, too. In the rush for AI, Microsoft has broken its own supplier code of conduct, which requires suppliers to have a minimum target of 55% absolute reduction in emissions by 2030.

As of August 2024, not a single one of the key suppliers providing AI accelerated hardware, including AMD, Intel and Nvidia, has goals that meet this standard. **If you have carbon reduction goals, and OpenAI or OpenAI-powered products are in your supply chain, then you have partners in your supply chain already missing their own targets. This is likely to make meeting your own commitments more difficult.**

![Microsoft's requirements and its 10 suppliers' scope 1 and 2 GHG reductions targets by 2030 reduction targets](https://www.thegreenwebfoundation.org/wp-content/uploads/Microsofts-requirements-and-its-10-suppliers-reduction-targets.jpg)

Microsoft’s requirements and its 10 suppliers’ scope 1 and 2 GHG reductions targets by 2030 reduction targets. Cited in Ctrl-Alt-Incomplete: The Gaps in Microsoft’s Climate Leadership.

Microsoft isn’t alone in needing to revisit its own plans to meet earlier carbon reduction commitments after significant AI investments. Even after accounting for Google’s sector leading investments in renewable energy, Google’s own sustainability report in 2023 showed a jump of more than a third in carbon reported emissions from electricity usage in their data centres.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#6f7a2cda-ce43-4709-9bfc-fb13cc0a62f8">52</a></sup>

In March 2024, Google admitted they were also revising their strategy <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ff10bc56-f455-4e61-bc51-e4693a62db10">53</a></sup> after their recent investments in infrastructure to meet electricity demand introduced by AI hardware. Just looking at the struggles of these well-resourced firms highlights two significant challenges:

1. How does the industry decarbonise a supply chain consisting of AI hardware suppliers?
2. How can data centres responsibly source the vast amounts of energy they consume?

### 3\. AI’s footprint can be measured estimated, but it’s an emerging discipline

Broadly speaking AI’s lifecycle breaks down into three main stages:

1. ***Manufacture*** – building the hardware used for training and inference
2. ***Training*** – creating an AI model
3. ***Inference*** – using a trained model to answer questions

For each stage of this lifecycle, there are ecological impacts resulting from the use of earth’s resources:

| **Scale** | **How the impact happens** |
| --- | --- |
| **Manufacture**   Building the hardware for training and inference | Manufacturing processes require amounts of electricity, heat, and very pure water.      Manufacture often occurs in regions with fossil fuel heavy grids and rely on fossil fuels for high temperature heat. |
| **Training**   Creating an AI model | Training a single model can rely on thousands of hours of computing time on specialised power hungry hardware.      Energy usage scales with model size, and model sizes keep growing.      Keeping this hardware cool can consume significant amounts of water. |
| **Inference**   Using a trained model to answer questions | Inference can be run on a wide range of hardware depending on the model used.      For large language models, specialised hardware is often used, consuming more power for faster responses times (i.e. GPUs and TPUs over CPUs).      Like training, computation requires cooling, which requires water. |

#### Why is creating estimates difficult?

Finding precise numbers for a specific AI model lifecycle can be challenging, and especially so for Generative AI models. **Having model-level data is an essential first step when trying to understand your own impact of using such a tool.** There are two common blockers for this.

Firstly, we have some issues on getting data about the footprint of AI hardware manufacture. While some producers list figures for typical energy consumption, they don’t provide information about the energy required for building the hardware at the outset. As an aside, they also don’t provide public information about any other resource inputs such as water or rare raw materials.

Secondly, we face a similar problem when trying to understand the implications from training and inference. **Most cloud providers treat two key data points for making estimations as trade secret information: i) the amount of energy consumed by the servers running the AI model and ii) the carbon emissions of that energy.**

#### How can we get around this?

Faced with this lack of disclosure, responsible technologists are drawing upon work put into the public domain by various AI researchers <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e57110f0-eaa7-4f33-8cbb-45434de63ee7">54</a></sup> to make their own evidence-based estimates. One of the best examples is from the startup [Hugging Face](https://huggingface.co/), the largest hub for AI models globally. They shared their figures for [*BLOOM*](https://huggingface.co/bigscience/bloom), a large language model:

> *“We estimate that BLOOM’s final training emitted approximately 24.7 tonnes of carbon (equivalent) if we consider only the dynamic power consumption, and 50.5 tonnes if we account for all processes ranging from equipment manufacturing to energy-based operational consumption.”*

To put this into context, 50.5 tonnes is roughly the same emissions as the annual electricity use from 50 UK households each year. *BLOOM* ’s figures are often used as a reference for making estimations of other large language models from different providers. Research like this doesn’t just help us to produce a final estimate. It also provides insight into where in the AI lifecycle impact happens. We can use this to understand where we might focus efforts for meaningful reductions.

#### Where to look for environmental footprint figures of models

The use of “model cards,” first popularised at Google in 2018, is now a widespread approach. Model cards document the features and performance characteristics of AI models in a consistent and standardised form. The European [AI Act](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence), the first comprehensive set of regulation on AI, requires AI system designers to provide model cards for a wide range of models. Hugging Face provides guidance on how to disclose the environmental footprint of various models.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ac0c57ee-f7a1-4b50-9c9e-1369dd36938c">55</a></sup>

The most recent model from Meta, Llama 3.1, now has a model card listed on HuggingFace.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#afab74ec-a128-418a-86be-007ed6013469">56</a></sup> It does not go as far as BLOOM in terms of disclosure and focuses mainly on the carbon footprint of training. However, we now have official figures in comparable form. Meta discloses a location-based carbon footprint model of 11,390 tonnes of carbon dioxide equivalent. This is nearly 500 times larger than the BLOOM model from a few years earlier. Hugging Face also provide searching tools to find and sort various machine learning models by their carbon footprint.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#c406a613-b5ce-4dde-8b89-e62ea5f9146d">57</a></sup>

**However, while disclosure for the carbon footprint of *training* of models is becoming more commonplace, figures for *inference* are harder to come by.** Very few services that use AI models disclose any per usage figures. Until the companies with access to the data disclose figures, we are reliant on tools that make estimates “from the outside” again.

Gen AI Impact’s open source EcoLogits project is currently the best example we have found of a tool that provides usage-based estimates for the use of inference from the largest AI services and can be included into AI projects. The team clearly document their approach,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#4ff795bf-cd2b-4344-8370-919e9b7b901e">58</a></sup> as well as where they have made assumptions, and where limits are to their approach. They also offer a calculator for very quick estimates.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ed510a58-6b88-4e34-8a4f-082937da9f98">59</a></sup>

**Ultimately, if you consume AI powered services and want to understand your likely impact from using them, you’ll probably need to request figures from vendors, as they are best placed to provide them.**

There are also reasons to request these figures from a regulatory point of view. **The European AI Act has *mandated* the publishing of information about the environmental impact of creating foundational models, with significant penalties for non compliance.** This is likely a significant factor in Meta’s recent LLama 3 model being published with a model card containing environmental impact information and links to clear methodologies.

Other legislation like the Corporate Sustainability Reporting Directive (CSRD) in Europe mandates the reporting from 2025 onwards about the environmental footprint of organisations and their operations—including their supply chains. If activity by an organisation is considered large enough to count as being “material” to their reported carbon footprint, then it either needs to be included in the reporting or the organisation needs to show how they decided something was *not* material to their impact. Either way, deciding whether an activity is material to reporting is difficult to do without access to the underlying data, and this is data that we know exists.

### 4\. Changing your choice of AI model and task impacts the footprint

If you know that it is possible to estimate the footprints of different AI models,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#c05faed3-0241-40fc-88d5-13fb5184e981">60</a></sup> then a logical next step might be to ask yourself if one model might be a better choice than another. The short answer is yes. It is possible to determine if one model is better than another. It’s also useful to know that some types of tasks tend to be more resource intensive than others.

#### Different tasks require different amounts of energy

Once again, while there are new projects to benchmark various AI activities, this is a developing field. If we want to understand the relative resource impact of different AI tasks, we can look to recently published work by AI researchers. Published in December 2023, *Power Hungry Processing: Watts Driving the Cost of AI Deployment?*<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#9dd4af01-2f61-4984-9043-9d2a80f617ae">61</a></sup> provides useful, independent numbers in the public domain for the first time.

![Table showing energy usage for top ten AI powered tasks in KWh](https://www.thegreenwebfoundation.org/wp-content/uploads/Energy-per-1000-queries.jpg)

Mean and standard deviation of energy per 1,000 queries for the ten tasks examined in our analysis. Cited in Power Hungry Processing: Watts Driving the Cost of AI Deployment?

This tells us that using AI to summarise some text probably doesn’t use more energy than carrying out a search on Google or Bing. But using AI to generate an image might use as much energy as recharging your phone.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#38335665-a2b4-41ec-a413-424d3ff829df">62</a></sup> Do bear in mind these figures help us understand the inference (usage) part of the lifecycle. But they don’t take into account the other parts of the lifecycle. Therefore these figures should be viewed as an incomplete picture of impact.

#### For the same task different models can use different amounts of energy

Once we’ve an idea of how impactful a specific task might be, there’s scope to reduce the impact through careful choice of models for a specific task. Research shows how much this can vary.

![Data visualisation by Hugging Face shows that different tasks use different amounts of energy. It also shows that for the same task, different models use different amounts of energy too.](https://www.thegreenwebfoundation.org/wp-content/uploads/Task-by-task-energy-comparison.jpg)

Data visualisation by Hugging Face shows that different tasks use different amounts of energy 63. It also shows that for the same task, different models use different amounts of energy, too.

This chart can be overwhelming at first glance, so let’s focus on the figures for a single task: image generation listed on the far right. For this, we can see the energy use varies from 11 KWh per image for the *Stable diffusion* model to 0.7KWh for the *tiny-sd* model. This is a 15x difference. Both these models are doing the same task, producing an image.

Therefore supplier choice matters as not all models impact in the same way. Some organisations are paying more attention to this than others and talking openly about the work they’re doing in this field. A good example of a large firm working in the open is Salesforce.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#3ebe8746-efc8-4dd1-bc6f-8c003b5fd978">64</a></sup> They publish impact figures for their own models and also write about their own efforts.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#012021be-d640-44ba-b4cb-4849de278396">65</a></sup> While it is in its early stages, the Energy Star AI project <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#50672472-9465-4d78-ae20-5ce76272f701">66</a></sup> is an interesting initiative to make the benchmarking of models accessible and actionable with early buy-in from companies like Salesforce.

The key takeaway here is that reducing the impact of AI isn’t just applicable to those creating models. As users of these models, if we can gather enough data to discern the differences between them, we can make better choices over which has less impact.

### 5\. Any AI code can be run in ways that reduce the footprint

Finally, even if we’re not able to choose the models we use, there are still a few options to reduce the impact of AI. **The emissions of an AI model are not just dependent on the quantity of electricity used, but also where the electricity comes from. Carbon intensity is a standard way of talking about this.**

Cleaner electricity produced by renewable sources has a lower carbon intensity. This means that for every unit of electricity produced there are fewer emissions. On the flip side, electricity produced by burning fossil fuels is more polluting and has a higher carbon intensity.

In reality, most of any given region’s electricity comes from a variety of sources. The proportion produced by renewables, fossil fuels and nuclear changes based on many factors. This causes the carbon intensity of electricity to fluctuate, which can be used as an advantage. Let’s look at an example of this in an AI context. The *BLOOM* model mentioned previously is similar in size and complexity to the model used in OpenAI’s Chat-GPT, *GPT-3*. **However, *BLOOM* resulted in almost 20 times lower carbon emissions. How? By using different hardware to reduce the energy consumption and running the computation in a place with lower carbon intensity power.**

![Comparison of models and key performance metrics](https://www.thegreenwebfoundation.org/wp-content/uploads/Comparison-of-models-and-key-performance-metrics.jpg)

Click to enlarge. Credit Boris Gamazayichikov, AI Sustainability lead at Salesforce

This diagram tells us a few useful things:

- You can reduce the impact through specifying the location of a data centre
- You can reduce the impact through choice of hosting provider

Let’s unpack each of these in turn.

#### You can reduce the impact through specifying the location of a data centre

In different parts of the world, the electricity powering a data centre will have varying carbon intensities. In Poland or India there is a higher proportion of fossil fuels like coal generating electricity than compared to the UK. **Therefore, all things being equal, the same model will have a higher carbon footprint if run in a Polish or Indian data centre over a British equivalent.**

Why is this? Using the same AI model will be performing the same task running on the same hardware but the task runs in a ‘cleaner’ region, using cleaner energy, so the carbon footprint will be lower. A growing number of data centre vendors provide this information to users now to aid decision making**.** The [Green Software Foundation](https://greensoftware.foundation/) has a compiled list of the carbon intensity of power use in every single region of Microsoft, Amazon, and Google’s cloud services, as part of their the *Real Time Energy and Carbon Standard for Cloud Providers project* <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#94e0e073-5b2a-4899-ade5-a2203338c7c4">67</a></sup>, lead by Adrian Cockroft and Pindy Bhullar. The Green Web Foundation is a contributing member to this project.

#### You can reduce the impact through choice of hosting provider

Not everyone can choose to run AI computation in the greenest grids on earth, and there are many valid reasons for not automatically choosing to move computing workloads to far flung destinations. For example, some data has to stay inside national borders for compliance reasons. Faced with this, choice of vendor matters once again as in some organisations sustainability has a higher priority than others.

**On the same grid, with the same model, and the same amount of computation to carry out, vendor choice can make a difference.** There may be providers who are prioritising a circular first approach and looking beyond just procuring green energy.

In the UK, Deepgreen <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fc4b18fd-4ee6-4118-845b-4ce75985a2ce">68</a></sup> is an example. They have built a business around placing micro data centres in places where the heat generated by computation is an asset rather than a liability. In addition to running on cleaner power, they site their servers in buildings where the heat goes towards heating swimming pools via heat exchangers rather than requiring fresh water to be consumed for cooling. This saves energy but also saves on water and gas needed for heating.

---

## Recommendations: 3 actions for every business when considering using AI

The best solutions to every problem start with a grounding in the wider context and what contributes to causing issues in the first place. Above, we outlined five key topic areas we think you need to know to get you started. Armed with this knowledge, the next logical question is what can I do with it?

Here we outline three actions you can take to make a difference.

It may seem obvious, but the best way to reduce the environmental harm resulting from the AI is to only use for purposes it’s well suited to.

The world of AI is full of the promise of endless productivity and efficiency, but it rarely lives up to the hype. Therefore, ask careful questions about whether AI automation will really solve your business problems, or if it is destined to become another failed digital transformation. Can you balance the trade-off between increasing your share of carbon emissions and the potential productivity gains?

#### Avoiding the use of AI

A growing number of companies, like Zulip,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#66bc2ff0-e996-4159-abea-d7ec68efd013">69</a></sup> Procreate,<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#bdb71608-631c-4fa3-934a-0d49187b87a3">70</a></sup> and others are explicitly making a point of not using LLMs or AI as part of their products. These are not usually on environmental grounds but instead revolve around other ethical concerns. This is similar to how a number of firms made public statements about steering clear of cryptocurrencies and blockchains. Another movement in this space is [Not Made by AI](https://notbyai.fyi/about), aimed at those who wish to promote their content as AI-free.

#### Resources

Here is our curated list of resources aimed at guiding you through these questions:

- [Careful Industries](https://www.careful.industries/carefulai), based in the UK, is an ethical research consultancy offering quality services to businesses wishing to navigate AI. They provide training, tools and workshops for developing socially responsible and have experience working at a policy-making level.
- [MySociety’s own AI policy](https://research.mysociety.org/html/ai-framework/) is one of the best and clearest examples for a technology led non-profit. They also blog about how they’ve used it to inform decisions on climate projects like [CAPE](https://cape.mysociety.org/about/).
- RAND Corporation’s [Avoiding the Anti-Patterns of AI](https://www.rand.org/pubs/research_reports/RRA2680-1.html) report covers common ways AI projects go wrong, identifying mitigating strategies and areas to focus on *first*, before reaching for AI to solve a poorly understood problem.
- The Ada Lovelace Institute’s document [AI Assurance – Assessing and Mitigating risks across the AI lifecycle](https://www.adalovelaceinstitute.org/report/risks-ai-systems/) offers a relatively concise explanation of the different interventions organisations might make at different states of the lifecycle of project.
- [The MIT Risk Repository](https://airisk.mit.edu/) is a very thorough resource. It contains the AI Risk Database which captures 700+ risks extracted from 43 existing frameworks, the Causal Taxonomy of AI Risks classifies how, when, and why these risks occur and The Domain Taxonomy of AI Risks classifies these risks into seven domains (e.g., “Misinformation”) and 23 subdomains (e.g., “False or misleading information”). This is a great timesaver and much faster than trawling the web yourself to find them.

If you do decide AI is the right choice for your specific task, spend time choosing responsible suppliers. As we’ve detailed, not all AI is created equally. There are already ways that suppliers can make different choices to reduce this impact. Here’s a summary of how you can (or can’t) mitigate the environmental harms when choosing to use AI.

*NB Organisations who are users of AI through* [*SaaS*](https://en.wikipedia.org/wiki/Software_as_a_service) *models, e.g. use AI services others provide or choose to host AI tools using third-party services such as cloud services are likely to find this table most useful.*

| **Area of choice** | **SaaS users of AI can change?** | **Self-hosting users of AI can change?** | **Notes** | **What systemic changes would make this easier or possible?** |
| --- | --- | --- | --- | --- |
| **Your choice of model for a specific task** | ✅ | ✅ | It’s possible to use model cards to support decision making.      Hop to “ [For the same task different models can use different amounts of energy](http://same-task-different-amounts-of-energy/) ” for the detail. | More funding and guidance for how to estimate and disclose reliable figures.   Strong enforcement of the new laws in the AI Act that require transparency for using models (inference), not just training them.   Notable organisations in this space: [European AI & Society Fund](https://europeanaifund.org/); [AI Now Institute](https://ainowinstitute.org/); [Data & Society](https://datasociety.net/). |
| **Your choice of hosting provider** | ❌ | ✅ | It’s possible to use model cards to support decision making.      Hop to “ [For the same task different models can use different amounts of energy](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#same-task-different-amounts-of-energy) ” for the detail. | Better incentives to create a circular economy for hardware.   Policy to support community outcomes eg reducing community harms (massive water use in areas of drought) and share the good things (heat, grid capacity and resilience).   Support alternatives to monopoly.   Notable organisations in this space: [Open Compute](https://www.opencompute.org/); [Critical Infrastructure Lab](https://www.criticalinfralab.net/); [Common Wealth](https://www.common-wealth.org/publications/dynamics-of-corporate-governance-beyond-ownership-in-ai); |
| **Your choice of data centre location** | ❌ | ✅ | For using AI tools provided by others, your options are limited to asking questions of suppliers, not affecting direct change yourself. Some model cards do provide this openly.   If you are self-hosting AI tools, many hosting providers operate data centres in multiple locations and you can choose between them.   Hop to “ [Reduce the impact through specifying the location of a data centre](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#choice-of-hosting-provider) ” for the detail. | Whilst it’s possible you can get this information, it could be a lot easier and more transparent.   In Europe, the Energy Efficiency Directive and related laws have compelled firms to compile information at a datacentre level about their water usage, how clean the energy they use is, and a host of other relevant datapoints.   In some cases this data is in the public domain. Where it isn’t you, can request it.      We we intend to surface this in the [Green Web Directory](https://app.greenweb.org/directory/) as it becomes widely and consistently available. |
| **Your choice of hardware supplier** | ❌ | ❌ | Hardware supplier is typically a choice made by a hosting provider. That said, the market is currently dominated by Nvidia, and there’s little choice in reality. In the current structure, the power imbalance means the main providers have enough leverage to refuse to provide transparency on emissions.      Nvidia has not published information beyond power usage. Other providers like AMD are entering the market – they have not published much information either.      Large tech firms are building their own specialised hardware, but do not have an encouraging history of disclosure. | Address the consolidation that exists within hardware manufacturing.      Support / mandate interoperability at the hardware software layer, i.e, support alternatives Nvidia’s CUDA software allowing competition on transparency.      Apply lessons from other sectors where public subsidies come with concessions on societally important factors (prevailing wages, environmental disclosure, etc). A high profile example would be the progressive set of measures used in the [US Inflation Reduction Act.](https://www.utilitydive.com/news/inflation-reduction-act-ira-labor-standards-job-creation/724693/) |
| **Introduction of AI features to tools you already use.** | ❌ | ❌ | More software is coming bundled with AI. [Google Maps](https://blog.google/products/maps/google-maps-generative-ai-local-guides/) is one example, but there are many more.   You can ask suppliers for ways to opt out, if you know it’s there in the first place. | Force an explicit opt-in, and disclosure to be required. There are some precedents with the GDPR on the right to restrict processing (though focussed on personal data) <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#7af2ce23-e003-4b67-aa24-b76676dc2f1a">71</a></sup>, and the FTC’s rulings on secondary use of personal data to train algorithms <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#045a66ee-ac9a-4f8e-ab1a-ec909e82160b">72</a></sup> |

Landmark AI-focused legislation like the [EU’s AI Act](https://www.europarl.europa.eu/topics/en/topic/artificial-intelligence) has made progress in this area. It places an emphasis on reducing the consumption of energy and ‘other resources consumption’ for high-risk AI systems and just on energy-efficient development for general-purpose AI models. Both are expected to include training and usage (inference). This is already making changes in the data that’s available, but many argue it was a missed opportunity.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e887b54a-d0ce-4b67-9cd9-b08de643f382">73</a></sup>

The good news is there’s further EU legislation that will provide a much needed push for organisations to report on useful data on their environmental impact, such as the [Corporate Sustainability Reporting Directive](https://plana.earth/policy/corporate-sustainability-reporting-directive-csrd) (CSRD) and [Energy Efficiency Directive](https://www.datacenterdynamics.com/en/news/european-energy-efficiency-directive-published-with-mandatory-data-center-reporting/) (EED). The EED mandates that every data centre above a certain size in Europe will need to collect absolute figures for water usage, energy consumption, and renewable energy share.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#32c839cd-f338-4c42-8083-0a2d4a7678d2">74</a></sup>

**What to ask for**

Firstly, insist on as much transparency as possible. Even with the best of intentions, estimating digital emissions is loaded with assumptions. Request clarity around the methodology used and data sources. **note:** We’re currently working on sample language to add to commercial agreements to request this – drop us a line if you’d like to collaborate with us.

**Ask for location-based *and* market-based figures for the use of AI services.** A location-based method reports what an organisation is physically putting into the air, in other words its “real” emissions. The market-based approach shows what an organisation is responsible for through its purchasing decisions, such as a renewable energy contract. The results can be very different, and there are significant issues associated with only using market-based numbers.

You might also consider writing disclosure clauses into agreements like how large providers do with their suppliers, such as the Salesforce sustainability exhibit.<sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#47bd17fc-a131-432e-b8a2-bc510bdffe28">75</a></sup>

**Making your own estimates**

In the absence of data from suppliers, you may need to estimate these numbers in order to comply. If you need a guiding hand to get you started, we offer [technical expertise](https://www.thegreenwebfoundation.org/services/) as well as tailored guidance on the above recommendations.

---

## Acknowledgements

This report is made available under a Creative Commons Attribution 4.0 International (CC BY SA 4.0) licence. For media or other inquiries please [get in touch](https://www.thegreenwebfoundation.org/support-form/).

Special thanks to all those whose insights and feedback contributed to this report: Boris Gamazaychikov, Holly Alpine, Justin Mason, Carole Touma, Melissa Hsiung, Tamara Kneese, David Rees, and amongst others, members of climateAction.tech community who provided feedback anonymously.

### Suggested citation

Smith, H & Adams, C (2024): Thinking about using AI? Here’s what you can and (probably) can’t change about its environmental impact. Green Web Foundation 2024.

---

## Footnotes

1. [Dartmouth Summer Research Project on Artificial Intelligence](https://en.m.wikipedia.org/wiki/Dartmouth_workshop). [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#288ab581-045e-4532-b7c3-f5128e642011-link)
2. [ChatGPT website](https://chat.openai.com/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ab950a31-e433-4a0a-a869-64d8e85e89f5-link)
3. [ChatGPT take two months to reach 100 million users](https://www.theguardian.com/technology/2023/feb/02/chatgpt-100-million-users-open-ai-fastest-growing-app) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#5d41eb08-f2e8-4ee1-a0e1-a973fa23ede2-link)
4. ElPais: [ChatGPT achieves in six months what Facebook needed a decade to do: The meteoric rise of the AI chatbot](https://english.elpais.com/science-tech/2023-06-14/chatgpt-achieves-in-six-months-what-facebook-needed-a-decade-to-do-the-meteoric-rise-of-the-ai-chatbot.html) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e6882555-452f-4d32-ad1f-58bfc264e44f-link)
5. P [aper from Google Research, Attention Is All You Need](https://research.google/pubs/attention-is-all-you-need/) introducing the Transformer Architecture for Machine learning.  
	[↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#6f871c6b-6179-46ab-b953-b0e4f58a8d37-link)
6. [Google’s website introducing its Palm2 model](https://ai.google/discover/palm2), as well as [coverage from Ars Technica](https://arstechnica.com/information-technology/2023/05/googles-top-ai-model-palm-2-hopes-to-upstage-gpt-4-in-generative-mastery/) and [ZDNet’s coverage of Google I/O event](https://www.zdnet.com/article/every-major-ai-feature-announced-at-google-io-2023/).. [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#a96c4221-fccb-4674-aa58-425c88c7ed61-link)
7. Meta’s Llama Series of models are not released under an open source licence, and have some restrictions, but are freely downloadable, and many companies are using them in their own services. See more [on their Llama Ecosytstem website](https://ai.meta.com/blog/llama-2-updates-connect-2023/). [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#d89435cf-f957-444d-94df-3b44c17e4c99-link)
8. [Commentary from Semi Analysis](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither) around “We have no moat, and Neither does OpenAI” – leaked internal Google memo warning Open Source AI Will Outcompete Google and OpenAI [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#89cb199d-8046-44e2-ac20-a5a8d496e427-link)
9. Historical and project capital expenditure charts from the [linked Financial Times article](https://archive.is/RAX4M) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e6bceb59-5911-4eb3-a530-86fe5480e7ce-link)
10. [CNN: Nvidia surpasses Microsoft to become the largest public company in the world](https://edition.cnn.com/2024/06/18/markets/nvidia-largest-public-company/index.html) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fe77a547-6c94-4848-af79-c6b3267834f8-link)
11. [Reuters: Nvidia loses top spot to Microsoft after 3% drop](https://www.reuters.com/markets/us/nvidia-set-solidify-position-worlds-most-valuable-company-2024-06-20/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fd40f252-e6ce-4928-bf67-cd6b844cb90e-link)
12. Numbers collected by [Django co-founder and AI researcher Simon Willison](https://simonwillison.net/2024/Aug/31/openai-says-chatgpt-usage-has-doubled-since-last-year/), referencing multiple news outlets. [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#55c36ccb-11bf-4939-a953-7bcfb8cacd19-link)
13. Goldman Sachs Report – [Gen AI: too Much spend, too little benefit?](https://www.goldmansachs.com/images/migrated/insights/pages/gs-research/gen-ai--too-much-spend,-too-little-benefit-/TOM_AI%202.0_ForRedaction.pdf) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#d9160f76-e2f4-4ba8-a7be-07aa6245e073-link)
14. [Lessons from History: The Rise and Fall of the Telecom Bubble](https://www.fabricatedknowledge.com/p/lessons-from-history-the-rise-and?utm_source=publication-search#:~:text=Another%20difference%20I,an%20important%20comparison.) – detailing the similarities and difference in AI and network capacity build out [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#bd919d60-0026-4ddd-9364-1c132f546215-link)
15. See Boston Consulting Group’s November 2023 report – [How AI Can Speed Climate Action](https://www.bcg.com/publications/2023/how-ai-can-speedup-climate-action) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#df9e9219-2734-49d5-98cf-dcb17d91f224-link)
16. See [Sustainability Magazine – Accenture: How Gen AI can Accelerate Sustainability](https://sustainabilitymag.com/articles/accenture-how-gen-ai-can-accelerate-sustainability) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#42b75e6a-7ded-44f9-948d-343c384cb5c2-link)
17. Research from RAND – [The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed](https://www.rand.org/pubs/research_reports/RRA2680-1.html) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#9422c57b-4238-4167-82b6-b37526e47cf0-link)
18. CNN: [Has the AI bubble burst? Wall Street wonders if artificial intelligence will ever make money](https://edition.cnn.com/2024/08/02/tech/wall-street-asks-big-tech-will-ai-ever-make-money/index.html#:~:text=Some%20investors%20had,years%20and%20beyond.%E2%80%9D) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#cb00bf96-4b57-4d57-be8c-3a4510860dae-link)
19. CNN: [Has the AI bubble burst? Wall Street wonders if artificial intelligence will ever make money](https://edition.cnn.com/2024/08/02/tech/wall-street-asks-big-tech-will-ai-ever-make-money/index.html#:~:text=Some%20investors%20had,years%20and%20beyond.%E2%80%9D) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#de4c68e8-e2e8-43f9-9ae4-0e3f0e19a2f8-link)
20. [The Chronic Potentialitis of Digital Enablement](https://www.linkedin.com/pulse/chronic-potentialitis-digital-enablement-vlad-constantin-coroam%C4%83-crtjc/), and the specific references to GeSI’s reports from 2008 through 2019 as well as the forecast enablement of sustainable activity, compared to the validates enablement. [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#66e5e4c7-b644-4019-9456-a8e360238a54-link)
21. [Towards a Fossil-Free Internet: The Fog of Enactment](https://www.thegreenwebfoundation.org/publications/report-fog-of-enactment/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#38ffcceb-6432-40d5-97e8-f59bd7dbfe9c-link)
22. In 2022, the Microsoft VP of Energy committed to providing a breakdown to its sustainability community of the energy division’s activity across six different sectors, from oil and gas extraction to low- or zero-carbon energy, as well as an analysis of personnel resources assigned to extractive industries versus renewable energy. As of Sept 2024, nothing has been shared. [Grist: Microsoft employees spent years fighting the tech giant’s oil ties. Now, they’re speaking out.](https://grist.org/accountability/microsoft-employees-spent-years-fighting-the-tech-giants-oil-ties-now-theyre-speaking-out/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#f2236f8d-7ead-4fe7-b8fb-7c2ed20df2e5-link)
23. Global AI software spending in the oil and gas market is forecast to increase 24.3% in 2024 to $1.5 billion and reach $2.9 billion by 2027 – [Gartner – Compare AI Software Spending in the Oil and Gas Industry, 2023-2027](https://www.gartner.com/en/documents/5318464) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#f26f2009-dcc6-48fd-9405-66cd02d04492-link)
24. Survey referenced on page taken down, but available on the Internet Archive. – [EY: Applying AI in oil and gas](https://web.archive.org/web/20230816201206/https://www.ey.com/en_lb/applying-ai-in-oil-and-gas) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#80565f30-c09f-420a-b51f-c46759199260-link)
25. See Karan Hao in the [Atlantic: Microsoft’s hypocrisy on AI](https://www.theatlantic.com/technology/archive/2024/09/microsoft-ai-oil-contracts/679804/?gift=lhL3dXSYCcu9vqTqEbg0OHfJiu_TRdq079IHN4QaSAE&utm_source=copy-link&utm_medium=social&utm_campaign=share) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#01d0375f-544c-4ee4-855e-f9384e0b7bec-link)
26. See Alex Steffen on [Predatory Delay and the Rights of Future Generations](https://medium.com/@AlexSteffen/predatory-delay-and-the-rights-of-future-generations-69b06094a16) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e98400a9-c56b-46ae-8bcf-1a126d807d26-link)
27. [Environment Variables – The Week in Green Software: Net Zero Cloud](https://podcasts.castplus.fm/e/vnwrkjm8-the-week-in-green-software-net-zero-cloud) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#7c92e282-19f3-41ff-9378-218d897d0570-link)
28. [ABN Amro sustainability reports](https://www.abnamro.com/en/over-abn-amro/information/sustainability-reporting-and-publications?selectedTab=Reporting) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#923bc85e-a726-4ee6-a615-63248ad2fbdb-link)
29. [IEA Electricity 2024 report](https://iea.blob.core.windows.net/assets/ddd078a8-422b-44a9-a668-52355f24133b/Electricity2024-Analysisandforecastto2026.pdf) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#538cee20-df6d-478b-9093-2bea4a2cf871-link)
30. Semi Analysis: [AI data centre Energy Dilemma – Race for AI data centre Space](https://www.semianalysis.com/p/ai-datacenter-energy-dilemma-race) and Semi Analysis’s Accelerator Industry Model [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#4980d386-3c91-492b-92e0-c4dd3d82b2c1-link)
31. [Joule: Commentary – The growing energy footprint of artificial intelligence – Alex De Vries](https://www.cell.com/joule/abstract/S2542-4351\(23\)00365-3) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#0d32cd14-c8c2-48e2-919f-41e6056c61a3-link)
32. [ChatCO2 – Safeguards Needed For AI’s Climate Risks](https://www.greenpeace.org/usa/chatco2-safeguards-needed-for-ais-climate-risks/) – Greenpeace [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#534725b8-601d-4242-8ef6-10fc091cb9f2-link)
33. In the USA, where the most the datacenter capacity is located, it tends to be in areas with easy access to gas or coal, like North Virginia. At a national level, fossil generation from coal and gas still makes up most of the electricity generation in the USA. China likely the nation with the next highest amount of data centre capacity also has a coal-heavy grid. For more, see [SemiAnalysis: AI Datacenter Energy Dilemma – Race for AI Datacenter Space](https://www.semianalysis.com/p/ai-datacenter-energy-dilemma-race#:~:text=In%20addition%2C%20the,mix%20in%202022.), and [Ember Climate’s grid intensity explorer](https://ember-climate.org/data/data-tools/data-explorer/). [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#1eb76217-8412-4949-81c8-2a5df81c9e38-link)
34. Datacenter Dynamics: [AWS, Digital Realty, Google, Meta, Microsoft, and Schneider Electric call for greater supplier transparency on Scope 3 emissions](https://www.datacenterdynamics.com/en/news/aws-digital-realty-google-meta-microsoft-and-schneider-electric-call-for-greater-supplier-transparency-on-scope-3-emissions/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#d158a3ff-733d-4efd-b330-67cfb0727eba-link)
35. [Sustainable data centers require sustainable construction](https://www.datacenterdynamics.com/en/analysis/sustainable-data-centers-require-sustainable-construction/) – Data Centre Dynamics <sup><a href="https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#bd978d97-9a78-481d-82c1-d4b1298149e0">*</a></sup> [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e9e48239-7d37-43a8-a013-be1c973da089-link)
36. [Tahoe Reno Exascale data centre](https://www.switch.com/tahoe-reno/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#8bdba7da-9b64-4f27-8a9a-d6fb90b1c505-link)
37. [Making AI Less “Thirsty”: Uncovering and Addressing the Secret Water Footprint of AI Models](https://ar5iv.labs.arxiv.org/html/2304.03271) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#9db83ec5-3359-44fc-8490-95385c9c71db-link)
38. [Water wars: Court halts Google data center in Chile amid climate controversy](https://www.sciencetimes.com/articles/47939/20240101/top-10-poisonous-places-earth-limits-humans.htm) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#62774744-c12e-4211-ae17-f4bf18ea4008-link)
39. In the town of the Dalles, Oregon, it only emerged at more than a quarter of the town’s water was being used by Google after a 13 month legal fight to keep this information being published. See [Oregon Live: Google’s water use is soaring in The Dalles, records show, with two more data centers to come](https://www.oregonlive.com/silicon-forest/2022/12/googles-water-use-is-soaring-in-the-dalles-records-show-with-two-more-data-centers-to-come.html) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#78961f0f-975c-4cff-abe7-00c3ea79c3e7-link)
40. US Energy Information Administration: \` [U.S. thermoelectric plants are the largest source of U.S. water withdrawals, accounting for more than 40% of total U.S. water withdrawals in 2015.](https://www.eia.gov/todayinenergy/detail.php?id=50698#:~:text=u.s.%20thermoelectric%20plants%20are%20the%20largest%20source%20of%20u.s.%20water%20withdrawals%2C%20accounting%20for%20more%20than%2040%25%20of%20total%20u.s.%20water%20withdrawals%20in%202015.%20) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#b3632726-fcf5-40e3-b80f-cc872bd5960b-link)
41. See Materals Today: [The significance of product design in the circular economy: A sustainable approach to the design of data centre equipment as demonstrated via the CEDaCI design case study](https://cdn.prod.website-files.com/5d1ca4414cf9cbff0c5be3eb/644bbfb443931f7fba423bd3_1-s2.0-S2214785322022507-main.pdf) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#1397a44d-d4dc-4ace-b3a9-3a94609e63fe-link)
42. [Closing the Loop on the World’s Fastest-growing Waste Stream: Electronics](https://www.bakerinstitute.org/research/closing-loop-worlds-fastest-growing-waste-stream-electronics) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#0c02ec15-550a-4b13-bd75-d50a0d7c4e4e-link)
43. [Top 10 Most Poisonous Places on Earth Off Limits to Humans](https://www.sciencetimes.com/articles/47939/20240101/top-10-poisonous-places-earth-limits-humans.htm) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#8e65b3db-8f17-4d4c-bd14-d568e95e99d0-link)
44. Nvidia’s recent H100 AI accelerators hardware offers more performance per watt than predecessors, but also consumers significantly higher amounts of power. For more, see [DataCentre Knowledge: Nvidia’s H100 – What It Is, What It Does, and Why It Matters](https://www.datacenterknowledge.com/data-center-hardware/nvidia-s-h100-what-it-is-what-it-does-and-why-it-matters) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#7761c3a0-015a-4e90-890a-a2e587cb0bd3-link)
45. Stack infrastructure, a supplier to large hyperscaler providers, publicly announced they are working on designs to support up to 300kW of power draw for AI workloads. [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#53f41c24-11be-436f-a4d4-2328b01e70fb-link)
46. See CNBC: [Elon Musk’s xAI accused of worsening Memphis smog with unauthorized gas turbines at data center](https://www.cnbc.com/2024/08/28/musk-xai-accused-of-worsening-memphis-smog-with-unauthorized-turbines.html) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#3fd8a23f-53ad-4f44-8795-e101b207c3c1-link)
47. Irish Business Post: [Microsoft secures planning for €100m gas plant to power data centre](https://archive.ph/Z8GFp) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#389fd84f-8ba2-4e2f-9516-097ccf5d1a9a-link)
48. the Register: [Surging datacenter power demand slows the demise of US coal plants](https://www.theregister.com/2024/05/31/datacenter_power_crunch/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#bd0e09dc-4b5d-4613-ac66-97b6ec800002-link)
49. Scientific American: [Coal Power Kills a ‘Staggering’ Number of Americans](https://www.scientificamerican.com/article/coal-power-kills-a-staggering-number-of-americans/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fdd27875-c1da-4e06-a3fe-73e3b5bdddfe-link)
50. Latitude Media: [Transition AI – Can the Grid Handle AI’s Power Demand?](https://www.latitudemedia.com/events/transition-ai-can-the-grid-handle-ai-power-demand) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#4f64a057-7241-4cc3-bb57-11bb815b8052-link)
51. Stand.Earth – [Ctrl-Alt-Incomplete: The Gaps in Microsoft’s Climate Leadership,](https://stand.earth/wp-content/uploads/2024/02/Microsoft-An-IT-giant-lacking-leadership-on-climate-and-energy-2.pdf) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#eb77915f-4145-4eb7-a796-5707c9491cc0-link)
52. [Google’s 2023 environment report](https://www.gstatic.com/gumdrop/sustainability/google-2023-environmental-report.pdf), footnote 148 – “Our Scope 2 market-based emissions increased 37%, primarily due to increased data centre electricity consumption and a lack of full regional coverage of renewable energy procurement in the United States and Asia Pacific regions.” [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#6f7a2cda-ce43-4709-9bfc-fb13cc0a62f8-link)
53. [Google hiring team lead to develop new net zero strategy after AI data centre energy boom](https://www.datacenterdynamics.com/en/news/google-hiring-team-lead-to-develop-new-net-zero-strategy-after-ai-data-center-energy-boom/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ff10bc56-f455-4e61-bc51-e4693a62db10-link)
54. [Estimating the Carbon Footprint of BLOOM, a 176B Parameter Language Model](https://arxiv.org/abs/2211.02001) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e57110f0-eaa7-4f33-8cbb-45434de63ee7-link)
55. Guidance on how to disclose [https://huggingface.co/docs/hub/model-cards-co2](https://huggingface.co/docs/hub/model-cards-co2) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ac0c57ee-f7a1-4b50-9c9e-1369dd36938c-link)
56. Taken from the [model card for Llama 3 on Hugging face](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B). [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#afab74ec-a128-418a-86be-007ed6013469-link)
57. *A search sorting by co2 emissions –* [huggingface.co/models?other=co2\_eq\_emissions&sort=trending](https://huggingface.co/models?other=co2_eq_emissions&sort=trending) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#c406a613-b5ce-4dde-8b89-e62ea5f9146d-link)
58. [Ecologit methodology pages for LLM inference an example](https://ecologits.ai/latest/methodology/llm_inference/). [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#4ff795bf-cd2b-4344-8370-919e9b7b901e-link)
59. Gen AI Impact’s – [AI EcoLogits Calculator uses the same Ecologits code](https://huggingface.co/spaces/genai-impact/ecologits-calculator), with various preset scenarios [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#ed510a58-6b88-4e34-8a4f-082937da9f98-link)
60. [ML Leaderboard from the ML Energy project](https://ml.energy/leaderboard/?__theme=light), as an example open project. [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#c05faed3-0241-40fc-88d5-13fb5184e981-link)
61. Recent paper [Power Hungry Processing: Watts Driving the Cost of AI Deployment?](https://arxiv.org/abs/2311.16863) for a further details [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#9dd4af01-2f61-4984-9043-9d2a80f617ae-link)
62. MIT Technogy Review – [Making an image with Generative AI uses as much energy as charging your phone](https://www.technologyreview.com/2023/12/01/1084189/making-an-image-with-generative-ai-uses-as-much-energy-as-charging-your-phone/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#38335665-a2b4-41ec-a413-424d3ff829df-link)
63. Data visualisation from [Hugging Face: CO2 Inference Demo](https://huggingface.co/spaces/sasha/CO2_inference) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#309dacf9-0a3a-4c3d-88d5-ee7a61b19613-link)
64. Salesforce list [their models on Hugging Face](https://huggingface.co/Salesforce) with model cards containing various data, including their resource impact. [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#3ebe8746-efc8-4dd1-bc6f-8c003b5fd978-link)
65. [The Ever-Growing Power of Small Models](https://blog.salesforceairesearch.com/the-ever-growing-power-of-small-models/), for examples of Salesforce writing about using different models for the same task. [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#012021be-d640-44ba-b4cb-4849de278396-link)
66. [Light bulbs have energy ratings — so why can’t AI chatbots?](https://www.nature.com/articles/d41586-024-02680-3) On nature.com [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#50672472-9465-4d78-ae20-5ce76272f701-link)
67. [Green Software Foundation – Real Time Cloud Project and working group.](https://github.com/Green-Software-Foundation/real-time-cloud) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#94e0e073-5b2a-4899-ade5-a2203338c7c4-link)
68. [Deep Green – use waste heat from datacentres to support local community activities](https://deepgreen.energy/) – [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#fc4b18fd-4ee6-4118-845b-4ce75985a2ce-link)
69. [Zulip blog:Self-hosting keeps your private data out of AI models](https://blog.zulip.com/2024/05/23/self-hosting-keeps-your-private-data-out-of-ai-models/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#66bc2ff0-e996-4159-abea-d7ec68efd013-link)
70. [Procreate: AI is not our future](https://procreate.com/ai) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#bdb71608-631c-4fa3-934a-0d49187b87a3-link)
71. ICO – [GDPR – Right to restrict processing](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-restrict-processing/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#7af2ce23-e003-4b67-aa24-b76676dc2f1a-link)
72. US FTC: [FTC and DOJ Charge Amazon with Violating Children’s Privacy Law by Keeping Kids’ Alexa Voice Recordings Forever and Undermining Parents’ Deletion Requests](https://www.ftc.gov/news-events/news/press-releases/2023/05/ftc-doj-charge-amazon-violating-childrens-privacy-law-keeping-kids-alexa-voice-recordings-forever) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#045a66ee-ac9a-4f8e-ab1a-ec909e82160b-link)
73. [The EU AI Act and environmental protection: the case for a missed opportunity](https://eu.boell.org/en/2024/04/08/eu-ai-act-missed-opportunity) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#e887b54a-d0ce-4b67-9cd9-b08de643f382-link)
74. [European Energy Efficiency Directive published, with mandatory data center reporting](https://www.datacenterdynamics.com/en/news/european-energy-efficiency-directive-published-with-mandatory-data-center-reporting/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#32c839cd-f338-4c42-8083-0a2d4a7678d2-link)
75. [Salesforce Urges Suppliers to Reduce Carbon Emissions, Adds Climate to Contracts](https://www.salesforce.com/news/stories/salesforce-urges-suppliers-to-reduce-carbon-emissions-adds-climate-to-contracts/) [↩︎](https://www.thegreenwebfoundation.org/publications/report-ai-environmental-impact/#47bd17fc-a131-432e-b8a2-bc510bdffe28-link)
