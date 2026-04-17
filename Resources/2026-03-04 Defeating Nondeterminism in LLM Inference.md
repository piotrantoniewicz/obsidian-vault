---
categories: Clippings
authors: "[[Horace He]]"
url: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
source: "[[Archives/2026-03-04 Defeating Nondeterminism in LLM Inference|2026-03-04 Defeating Nondeterminism in LLM Inference]]"
published: 2026-03-04
created: 2026-03-06
relevance: niska
tags:
  - LLM
---

# Defeating Nondeterminism in LLM Inference

Horace He i [[Thinking Machines Lab]] szczegółowo analizują źródła niedeterminizmu w silnikach inferencji [[LLM]], obalając popularną hipotezę "floating-point + concurrency". Prawdziwym winowajcą są atomic adds używane w kernelach GPU, które sumują liczby w niesystematycznej kolejności zależnej od harmonogramowania wątków — stąd wyniki różnią się nawet przy temperature=0. Autorzy proponują rozwiązanie: batch-invariant kernels (dedykowane implementacje RMSNorm, matrix multiplication i attention), które dają bitowo identyczne wyniki niezależnie od rozmiaru batcha i kolejności wykonania wątków. Deterministyczne inference ma konkretne zastosowanie w trenowaniu on-policy RL, gdzie niespójności logprob między trainerem a samplerem mogą degradować jakość treningu.

## Kluczowe dane

- Nawet przy temperature=0 standardowe silniki inferencji ([[vLLM]], [[SGLang]]) nie są deterministyczne
- Źródłem niedeterminizmu są atomic adds w redukcjach GPU — niesystematyczna kolejność sumowania wynikająca z harmonogramowania wątków
- Batch-invariant kernels rozwiązują problem całkowicie: wyniki są bitowo identyczne niezależnie od batcha

## Wnioski

- Niedeterminizm w [[LLM]] inference to inżynieryjny problem rozwiązywalny — nie inherentna właściwość probabilistycznych modeli, lecz konsekwencja implementacyjnych wyborów w kernelach GPU
- Batch-invariant kernels (RMSNorm, matrix multiplication, attention) pozwalają uzyskać pełną reprodukowalność wyników bez utraty wydajności, co otwiera drogę do wiarygodnych testów regresyjnych
- Deterministyczne inference jest warunkiem koniecznym dla trenowania on-policy RL z podziałem na trainer i sampler — bez niego pojawia się błąd systematyczny degradujący wyniki

## Zastosowanie

Jako konsultant AI możesz napotkać pytania klientów o reprodukowalność i spójność wyników LLM — ten artykuł dostarcza technicznego rozumienia, dlaczego temperature=0 nie gwarantuje deterministycznych odpowiedzi i kiedy jest to faktycznie problemem.
