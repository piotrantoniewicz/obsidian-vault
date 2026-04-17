---
type: Web
authors: "[[Miquel Duran-Frigola]]"
url: https://builders.mozilla.org/community-code-and-chemistry/?utm_source=substack&utm_medium=email
published: 2024-10-24T00:00:00.000Z
created: 2026-03-02T00:00:00.000Z
tags:
  - trendy-AI
  - narzędzia-AI
---


by [Miquel Duran-Frigola](https://builders.mozilla.org/profile/miquel-duran-frigola-phd/)

on

![](https://builders.mozilla.org/wp-content/uploads/2024/11/ersilia_2.jpg)

[Miquel Duran-Frigola](https://builders.mozilla.org/profile/miquel-duran-frigola-phd/) is the Chief Scientific Officer and Co-Founder at Ersilia.

This year’s [Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) was awarded to David Baker (University of Washington), Demis Hassabis, and John M. Jumper (DeepMind) for their groundbreaking contributions to protein structure elucidation and design using AI. And this year’s Physics Prize recognized the invention of neural networks, which set the mathematical basis for the current AI revolution. As a computational biologist and the co-founder of an [AI-driven tech non-profit](https://www.ersilia.io/about), I can only be delighted by the news. Computation has become essential to experimental science.

> The future of scientific innovation lies not in isolation but in the powerful combination of cutting-edge technology and open scientific collaboration.

The central dogma of molecular biology is, more or less, as follows. DNA sequences are transcribed into RNA sequences and translated into protein sequences. Protein sequences are composed of an alphabet of 20 amino acids. The length and composition of protein sequences will determine how they will fold in the 3D space, and this 3D structure will allow proteins to perform their function as if they were microscopic machines. The diversity and beauty of folded proteins are awe-inspiring (look at these paintings by [David S. Goodsell](https://ccsb.scripps.edu/goodsell/) to get an idea).

Given a DNA sequence, it is easy to infer the protein sequence. Yet, for decades, predicting 3D structures from 1D protein sequences was thought to be computationally intractable.

The Nobel Prize committee celebrates AI’s contribution to cracking the code for protein structures. Specifically, they recognize Hassabis and Jumper for developing [AlphaFold 2](https://github.com/google-deepmind/alphafold), an AI tool that can predict a protein structure from its sequence, and Baker for his work in the opposite direction, i.e., predicting sequence from the structure. The latter, known as protein design, directly impacts biomedical engineering since, given a desired 3D shape (naturally occurring or human-invented), it can suggest a protein sequence that can fulfill it.

Baker has also made remarkable contributions in the sequence-to-structure direction, with [RossettaFold](https://github.com/RosettaCommons/RoseTTAFold) being a competitive alternative to AlphaFold 2. One was published in [*Science*](https://www.science.org/doi/10.1126/science.abj8754) and the other in [*Nature*](https://www.nature.com/articles/s41586-021-03819-2) around the same date in 2021. 1D-to-3D and 3D-to-1D problems are two sides of the same coin as if they were text-to-image and image-to-text AI tasks.

David Baker is a well-established computational biologist who has shaped an entire field of research, publishing several landmark papers year after year for over two decades. The case of Hassabis and Jumper is different, though. Hassabis did not receive formal training in molecular sciences, and Jumper is the youngest chemistry Nobel awardee in 70 years.

![](https://builders.mozilla.org/wp-content/uploads/2024/11/chemistry_accent.png)

Chemistry and biology are not DeepMind’s core focus. Its groundbreaking research is a testament to AI’s incredible, almost magical, ability to transition from field to field and make a significant impact at an unprecedented speed. The algorithms stay more or less the same, and what changes is the data that is fed into the models.

The critical data source for the 2024 Nobel laureates in Chemistry was the Protein Data Bank (PDB), which has served as the reference repository for protein structure data obtained from X-ray crystallography and other techniques since the 1970s.

Experimental determination of protein structures is a laborious process that can take several years to complete. Today, the PDB contains over 200k experimentally resolved structures, resulting from millions of hours of laboratory work by the scientific community. Replicating these structures is estimated to cost over $10 billion USD.

Without the high-quality, public training data available in the PDB, the current AI breakthroughs would not have been possible.

> …a testament to AI’s incredible, almost magical, ability to transition from field to field and make a significant impact at an unprecedented speed.

This training data is just one instance of the triumph of open science. Another is the [Critical Assessment of Protein Structure Prediction](https://predictioncenter.org/) (CASP) initiative.

CASP is a bi-yearly competition that challenges participants with a set of protein sequences whose structures are only known to its organizers. It produces a trusted and reputable benchmark used to assess protein-to-structure prediction methods. When the results of the 14th CASP edition revealed the astounding performance of AlphaFold 2, with a prediction-vs-experiment match above 90/100 for two-thirds of the proteins, we all understood that the field was about to be transformed.

It is because of the publicly funded CASP initiative — a community effort established in 1994 — that AlphaFold 2 gained immediate respect.

Soon after the release of the CASP leaderboard, AlphaFold 2 was published in *Nature,* which increased general awareness of the tool. The AlphaFold 2 code was open-sourced, leading many, [including us](https://github.com/ersilia-os/osm-pfatp4-structure) at Ersilia, to try it on their proteins of interest.

Since its launch, several variations of AlphaFold 2 have been published. The tool has become essential scientific infrastructure thanks to the open science practices that accelerated its success and widespread use.

DeepMind partnered with the European Bioinformatics Institute (EBI) to massively pre-calculate the structures of over 200 million protein sequences belonging to species spread across the tree of life. All results were made available as an [easy-to-browse database](https://alphafold.ebi.ac.uk/). This formidable effort changed the research horizon overnight. In our case, we suddenly had access to thousands of predicted protein structures for neglected disease pathogens.

AlphaFold 2’s success cannot be explained without an active and rigorous open science environment. *The PDB was used as a training dataset, CASP was trusted for benchmarking, code was made available upon publication, and a public repository at EBI was created to store results.*

Baker’s stories of open science are just as compelling, if not more — among the many tools his team has developed is [Foldit](https://fold.it/). This widely popular citizen science platform gamifies the challenge of protein folding. *It is hard to imagine this happening in a secretive, closed-source, and IP-locked ecosystem.*

In March this year, a successor of the RossettaFold tool from Baker’s lab, RossettaFold All-Atom, was published in *Science*. Shortly after, the new AlphaFold 3 was announced in *Nature*, along with a [web server](https://alphafoldserver.com/about) to run predictions online.

The latest AI methods perfect all molecule types, including proteins, DNA, RNA, and chemical compounds. This has enormous potential for drug discovery — a highly profitable endeavor.

Regrettably, the code for AlphaFold 3 is not public, and the web server has capped capabilities for drug molecule candidates. This shift to a closed approach sparked a wave of reactions in the scientific community, questioning whether, no matter the economic incentives for keeping the code private, *Nature* should have published a tool that is not reproducible, transparent, and reusable.

As with other state-of-the-art AI models such as GPT, open-source surrogates of AlphaFold 3 are beginning to flourish, and I do not doubt that competitive alternatives will soon be available to the community. However, without abiding by the principles of open science, it seems unlikely that AlphaFold 3 will garner the same type of esteem within the scientific research community as its predecessor.

The success stories of Baker, Hassabis, and Jumper demonstrate that scientific progress accelerates when built upon public databases, transparent benchmarking, accessible code, and community participation. As we move forward in an era where AI increasingly intersects with traditional sciences, this Nobel Prize serves as a compelling reminder that the path to groundbreaking discoveries is paved with brilliant minds *and* the democratic sharing of knowledge and tools. The future of scientific innovation lies not in isolation but in the powerful combination of cutting-edge technology and open scientific collaboration.

## About the Author

## Miquel Duran-Frigola

Miquel is the Chief Scientific Officer and Co-Founder at Ersilia. His research interests lie at the intersection between drug discovery and large-scale biological data analysis. He has held positions at IRB Barcelona, the Massachusetts Institute of Technology (MIT), Tel Aviv University, ISGlobal-CISM (Mozambique), and CIDRZ (Zambia). He holds an MSc in Bioinformatics and a PhD in Biomedicine from Pompeu Fabra University, as well as a BSc in Chemistry from Ramon Llull University.

## Related stories

- ### Building Our Way Out
	Beyond the Machine Learning Mote
	![A representation of a mote of dust.](https://builders.mozilla.org/wp-content/uploads/2024/12/Firefly-A-photograph-of-a-single-very-small-smooth-mote-floats-alone-in-contrast-to-an-unfathomably-9_BW-scaled.jpg)
- ### For the Builders
	![](https://builders.mozilla.org/wp-content/uploads/2024/11/Antikythera_.png)
- ### Emergent Organization
	What if Companies Looked Like Neural Networks?
	![](https://builders.mozilla.org/wp-content/uploads/2024/11/emergent_org.png)
- ### The Interface Revolution
	AI and Human Intent in the Algorithmic Age
	![](https://builders.mozilla.org/wp-content/uploads/2024/11/Interface_Rev.png)
