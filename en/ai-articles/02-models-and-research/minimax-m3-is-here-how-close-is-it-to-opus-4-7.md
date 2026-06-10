# MiniMax M3 Is Here: How Close Is It to Opus 4.7?

[English](./minimax-m3-is-here-how-close-is-it-to-opus-4-7.md) | [Chinese Original](../../../ai-articles/02-models-and-research/MiniMax%20M3%20%E5%8F%91%E5%B8%83%EF%BC%8C%E6%8D%AE%E8%AF%B4%E6%8E%A5%E8%BF%91%20Opus%204.7%EF%BC%9F%E7%9C%9F%E7%9A%84%E5%81%87%E7%9A%84.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-06-02


MiniMax officially released M3. The official location is Coding/Agent, 1M context, prototype.

A few days before the official release, I saw a message that I could get into the M3 and then I went in, and I thought it was an internal test that was released for a while, but I didn't think it was released today, and this internal detector, apart from offering a seven-day free trial, seemed useless.

I've got a little partner around me who's been doing model tests, and this time he's exaggerating M3, and this is just one thing that I'm looking at, is that M3 is even taller than a pus 4.6.

MiniMax M3 Free score 4,88, A+. GPT 5.5 xhigh, Claude 4.7 Opus Max and Gemini 3.1 Pro. On a single score, it's really close to the one in Opus 4.7.

But in the same line of work there is a very good note: Slow, 7m51s.

![image-20260601142025101](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601142025101.png)

* Source: Survey of small partners.

So the article doesn't want to be written in "National Production Model Hangs Opus." That's the way it's written.

So what I'm more concerned about is: **M3 which experience is close to Opus 4.7, and which experience isn't enough for Opus 4.7?**

It's not about another model.

This is not the same as many national models published in the past.

You used to prefer single points: math, code, text, token. But M3 is talking about combination capacity this time. It does not just want to answer a question, but rather to go into a long-distance stream, reading the code, reading the log, adjusting the tools, changing the programme and running again.

![image-20260601142005725](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601142005725.png)

*Figure source: I'm drawing it myself. Data is from MiniMax's official blog and model page.

There are several key figures in the official blog:

SWE-Bench Pro 59.0 per cent, Terminal-Bench 2.1 is 66.0 per cent, SWE-fficiency 34.8 per cent, Kernel Bench Hard 28.8 per cent, MCP Atlas 74.2 per cent.

These figures are seen alone, not necessarily in a sense. What is really moving is the official saying: on SWE-Bench Pro, M3 exceeds GPT-5.5 and Gemini 3.1 Pro, close to Opus 4.7; on SVG-Bench, M3 exceeds Opus 4.7.

Note that it is ** near**, not fully equivalent.

Close to Opus, close to where

I prefer to limit this "close" to a range: **Coding/Agent's long-range mission experience**.

Because, from the official sources, M3's most wanted proof this time is not "I'll write a function," but "I can move on in a complex mission." And that's where models like Opus used to make the most difference.

![image-20260601143516615](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601143516615.png)

*Figure source: I made it myself; experience charts came from user screenshots, official indicators came from MiniMax release page.

The model page also gave an interesting point: M3 score on Brownecomp 83.5, Opus 4.7 is 79.3. In other words, at least in the official caliber, M3 has been able to make a positive comparison with Opus 4.7 in the capacity of autonomous browsing and information retrieval.

But you can't ignore the slowness of experience.

If your scene is a daily chat, quick question and answer, and you add a code to it, seven minutes is hard. You can't pretend it's silky every time a model runs for 24 hours.

So my first judgment is: **M3 is more like an engineering model for a backstage run than a chat model for every word. **

# 1M, the context is not for show

Officially, this time again, the MSA, that's...`MiniMax Sparse Attention`.

In short, it wants to solve the problem of a context-based cost explosion. Officially, M3 API top support 1M tokens, background 512K. In 1 million context length, M3 calculated the amount of 1/20 per token per previous generation model, prefill accelerated by more than 9 times, decoding accelerated by more than 15 times.

![image-20260601143537873](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601143537873.png)

*Source: MiniMax official blog.

It sounds technical, but it's realistic in the Coding Age scene.

In a real development mission, the context is not a PDF. It is a warehouse structure, historical changes, user-modified needs, testing logs, reasons for failure, tool call records, code review opinions, and the judgement that Agent has made before himself.

Once the model drifts, it starts to duplicate work.

You let it fix the bug, it's already out of the A scenario, and after dozens of rounds it's out of the A scenario. You make it UI, and it's already known in front of you not to use a component, and then itches back in the back. This experience is more head-to-head than simply wrong code.

So M3's 1M context is really going to solve **Agent can't remember why he came here on a long mission. **

---


There are three tasks in the official blog, which I think is more interesting than most benchmarks.

The first is the return of the paper. MiniMax threw an ICLR 2025 Outlook Paper Award paper, Learning Diamonds of LLM Finetuning, to M3 to make it recover independently. Officially, M3 ran for nearly 12 hours, producing 18 numbers and 23 experiments, running through core experiments.

![image-20260601142329807](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601142329807.png)

*Source: MiniMax official blog.

The second is the CUDA algorithm optimization.

The task is a little harder. The starting point is a task description, a Benchmark script, a Triton skeleton that cannot be directly operated, without high performance reference. M3 Completing 147 benchmark submissions and 1,959 tool calls in approximately 24 hours pushed the peak utilization rate of the Hopper FP8 GEMM from 7.6% to 71.3%, equivalent to 9.4 times the acceleration.

![image-20260601143621019](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601143621019.png)

*Source: MiniMax official blog.

The third is PostTrain Bench. It will allow M3 to synthesize, train, evaluate, and iterative for four pre-trained Base models in 12 hours. The official results were M3 score 0.37, slightly lower than 0.42 of Opus 4.7 and 0.39 of GPT-55, but clearly ahead of other models.

![image-20260601142415072](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601142415072.png)

*Source: I drew it myself, and the data came from MiniMax's official blog.

I'll add a conservative note here: these are official self-measures, not independent third parties.

But they are in the right direction. Because of the real Agent test, it can't just ask, "Is the final answer right?" It's also to see if it can continue at a time when feedback is thin, paths are unclear and the context is getting dirty.

This ability, used to be the most expensive place for a model like Opus.

---


M3 There is also a point of sale that cannot be bypassed: price and availability.

The official synchronisation of MiniMax Token Plan: Plus 49 million token, Max 119 million token, Ultra 469 million token per month. Officially, at the same price, it's about 15 times what Claude subscribes to.

![image-20260601142656671](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260601142656671.png)

*Source: MiniMax official blog.

That is why it remains attractive even slowly.

The problem with the Opus grade model is not that it's expensive, but that you don't dare let it run. A long-range Agent mission is hundreds of thousands and millions of tokens, and the price will determine whether you dare give it to it.

M3 If you can put the "long-range capability near Opus" on a more everyday cost, it's not about adding an A+ to the model's ranking, it's about making the developers really start taking Agent first.

But we need to stay here. The official blog says that the technical report will be updated within the next 10 days and open-source model weights will be applied; the model page will also be open on HuggingFace and GitHub to support private cluster deployment and fine-tuning.

In other words, it is now possible to experience it first, but with open source weights, technical reports, third-party re-examinations, it will have to wait for official completion.

---

My conclusion

If "Experience close to Opus 4.7" means that it understands big goals in the context of the Coding/Agent long-range mission, preserves context, keeps calling tools, and moves forward after multiple rounds of failure, it is well founded.

If "Empirical approaches to Opus 4.7" means that each scene is as steady as Opus, as fast as it is, and as good as the bottom, it's blown.

M3 The real value of this time is to push the Frontier model into the day-to-day development of one of the most expensive capabilities in the past. It does not necessarily replace Opus, but it may change the way many people use it.

You used to leave Opus with key tasks.

Now you might hang M3 in a real warehouse and let it run all afternoon to see if it's still working on its 145th, 220th, 500th try.

That's the most interesting place this time.

If you've taken the M3 through the real warehouse, especially the mission of an hour or more, you're welcome to throw me the sample of where the slowness is, where the steadyness is, where the fall is. It's not the first round, it's the second half of the long line.

---

Source:

- MiniMax official blog:[MiniMax M3: Frontline Coding Capability, 1M context, original multimodularity, all one model for you.](https://www.minimaxi.com/blog/minimax-m3)
- MiniMax Model Page:[MiniMax M3](https://www.minimax.io/models/text/m3)
- OpenRouter model page:[MiniMax M3 - API Pricing & Providers](https://openrouter.ai/minimax/minimax-m3)
- A screenshot of experiences provided by users

#MiniMax #M3 #Coding #Agent #Opus

The label is just an archive, and it's worth the next round of real project samples.
