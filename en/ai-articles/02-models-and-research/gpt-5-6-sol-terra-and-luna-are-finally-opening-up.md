# GPT-5.6 Is Finally Opening Up: Sol, Terra, and Luna Arrive This Thursday

[English](./gpt-5-6-sol-terra-and-luna-are-finally-opening-up.md) | [Chinese Original](../../../ai-articles/02-models-and-research/GPT-5.6%20%E7%BB%88%E4%BA%8E%E8%A7%A3%E7%A6%81%EF%BC%9ASol%E3%80%81Terra%E3%80%81Luna%EF%BC%8C%E6%9C%AC%E5%91%A8%E5%9B%9B%E4%B8%80%E8%B5%B7%E4%B8%8A%EF%BC%81.md)

> English edition based on the Chinese original.

> Date: 2026-07-08

Here we go. GPT-5.6 has finally been cleared for a broader release.

After Anthropic restored worldwide access to Fable 5, OpenAI has now announced that GPT-5.6 Sol will launch publicly this Thursday alongside Terra and Luna, while preview access expands around the world.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260708121657785.png" alt="OpenAI announces that GPT-5.6 Sol, Terra, and Luna will launch on Thursday as global preview access expands" style="zoom:50%;" />

A lot of people, myself included, have been waiting for this.

One clarification first: "opening up" does not mean everyone can open ChatGPT right now and select GPT-5.6 from the model list.

OpenAI's latest wording is that the models will launch publicly on Thursday and that global preview access is expanding. At the time of writing, the [official Help Center article](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna) still carries the earlier preview terms: GPT-5.6 is mainly available through the API and Codex to approved organizations, while ChatGPT is not yet included in the preview.

So the precise description is that the final gate has started to lift. It has not disappeared completely.

## Three Versions Arrive Together

OpenAI is not releasing a single model this time. GPT-5.6 arrives as a complete product family:

- **Sol** is the flagship and the most capable model in the generation.
- **Terra** is the balanced model for everyday work and better price-performance.
- **Luna** is the speed model, with the lowest cost for high-frequency, low-latency tasks.

The names are fun: sun, earth, and moon. The whole family is here.

But these are not merely large, medium, and small versions. OpenAI has assigned each one a different kind of work.

Sol takes on the hardest problems. Terra brings the capability down to a more practical price point. Luna is designed for products where response time and per-call cost matter.

According to OpenAI's [first preview announcement](https://openai.com/index/previewing-gpt-5-6-sol/), Terra can compete with GPT-5.5 at half the cost, while Luna is the fastest and cheapest member of the GPT-5.6 family.

GPT-5.6 is clearly competing for more than the title of strongest model.

It is also competing for production workloads.

## The Agent Capabilities Matter More

GPT-5.6 will of course offer stronger reasoning, better coding, and the ability to spend longer on difficult problems.

What stands out to me, though, is not another few points on a benchmark. OpenAI is continuing the shift from a single model answering a question toward a system that completes work.

GPT-5.6 adds **Max reasoning effort**. In plain language, it lets Sol spend more time thinking through especially difficult tasks instead of rushing to submit an answer.

The more interesting addition is **Ultra mode**.

Instead of relying on one Agent from start to finish, Ultra can send multiple sub-agents to work on a difficult task in parallel. It is like giving a highly capable employee a small team: one person researches, another writes code, another verifies the result, and the work is consolidated at the end.

That helps explain why OpenAI is emphasizing terminal work, long-running scientific tasks, and cybersecurity rather than ordinary question answering.

OpenAI says GPT-5.6 Sol set a new best result on Terminal-Bench 2.1, which tests command-line planning, iteration, and tool coordination. On GeneBench v1, a long-horizon genomics benchmark, it outperformed GPT-5.5 while using fewer tokens. It also advanced both capability and reasoning efficiency in vulnerability research and exploitation tests.

The plain-English translation is simple:

**GPT-5.6 looks more like an Agent that can keep working, not merely a model that can chat more intelligently.**

OpenAI also plans to deploy GPT-5.6 Sol on Cerebras in July, with speeds as high as 750 tokens per second. The initial rollout will still be limited to selected customers, so universal access is not here yet.

## Pricing Is More Restrained Than Expected

API pricing for all three models has also been announced, per million tokens:

| Model | Input | Output |
| --- | ---: | ---: |
| GPT-5.6 Sol | $5 | $30 |
| GPT-5.6 Terra | $2.50 | $15 |
| GPT-5.6 Luna | $1 | $6 |

Sol is not cheap, but it is not priced as a demonstration-only model either. Terra and Luna have more obvious jobs: one is meant to become a default productivity model, and the other is built for large-scale usage.

OpenAI has also added more predictable Prompt Cache behavior, including explicit cache breakpoints and a guaranteed cache duration of at least 30 minutes. Cached reads still receive a 90% discount.

That may sound unimportant to ordinary users. For teams processing millions or tens of millions of tokens every day, stable caching can matter more than shaving a few cents off the headline model price.

A model can produce one spectacular answer. After one hundred thousand calls, the bill becomes the most honest benchmark.

## Why Did This Opening Attract So Much Attention?

GPT-5.6 was never an ordinary model launch.

When OpenAI first previewed GPT-5.6 on June 26, access was limited to a small group of trusted partners and organizations. OpenAI explicitly said the staged release involved safety coordination with the US government, especially because the model had reached higher capability levels in cybersecurity, biology, and chemistry.

Around the same time, Anthropic's Fable 5 went through a similar sequence: release, suspension under export restrictions, and eventual restoration of global access.

The frontier-model race in 2026 is no longer only about who has the highest score.

There is a more practical question: **if ordinary users and developers cannot access a model, its capability exists only in launch events and evaluation tables.**

Seen from that angle, the important part of this announcement is not another benchmark victory. Frontier capability is beginning to reach a wider group of users again.

## Greater Capability Means Watching Its Hands

A stronger Agent also brings new problems.

OpenAI is unusually direct in the GPT-5.6 [system card](https://deploymentsafety.openai.com/gpt-5-6-preview/gpt-5-6-preview.pdf). In internal simulations, Sol was more likely than GPT-5.5 to pursue a goal too aggressively, sometimes taking actions the user had not clearly authorized.

This is a typical Agent-era failure mode.

An older model might answer a sentence incorrectly. A newer model can open a terminal, modify files, call tools, and operate external systems. Its mistakes can change things in the real world.

Capability is not the problem. Acting without permission is.

So my main questions about GPT-5.6 are not its peak scores. I want to see three things in real work:

First, are the results dependable after a long task?

Second, when an operation has an unclear boundary, will it stop and ask?

Third, once Ultra mode brings in a group of sub-agents, does the efficiency gain cover the added time and token cost?

No benchmark answers those questions yet.

## Final Thoughts

Whatever happens next, GPT-5.6 is no longer something most of us can only watch from a distance.

Sol, Terra, and Luna are launching together. Global preview access is expanding. OpenAI and Anthropic's new flagship generations are finally returning to the same table.

The interesting contest now is not who can print "the strongest" on a poster. It is who can deliver these intimidating capabilities to more people in a stable, affordable, and controllable form.

See you Thursday.

Hopefully we get more than an announcement this time. Hopefully we can actually use it.

---

**References**

- [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [OpenAI Help Center: A preview of GPT-5.6 Sol, Terra, and Luna](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)
- [OpenAI: GPT-5.6 Preview System Card](https://deploymentsafety.openai.com/gpt-5-6-preview/gpt-5-6-preview.pdf)
- [Anthropic: Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)
