# Cursor Flipped the Table: Is Grok 4.5 Ready to Take Off?

[English](./cursor-grok-4-5-ready-to-take-off.md) | [Chinese Original](../../../ai-articles/02-models-and-research/Cursor%20%E6%8E%80%E6%A1%8C%E5%AD%90%E4%BA%86%EF%BC%8CGrok%204.5%20%E8%BF%99%E6%AC%A1%E8%A6%81%E4%B8%8A%E5%A4%A9%E4%BA%86%EF%BC%9F.md)

> Date: 2026-07-09

Earlier today, SpaceXAI and Cursor officially announced the release of Grok 4.5.

Let’s just say, why are all the big models released at the same time? Is the traffic evenly distributed? But having said that, I feel that the big Grok model is basically not used by anyone in China, and basically no one mentions it. Grok sits at the same table as Gemini in everyone’s subconscious. When everyone uses Grok, they contribute protection fees to a well-known social platform, and then create small articles and pictures on a certain social platform, and nothing else.

But this time I felt like I could give it a try after reading it.

Let me talk to you in detail next.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709074946016.png" alt="image-20260709074946016" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709075017576.png" alt="image-20260709075017576" style="zoom:50%;" />

Grok 4.5 is the smartest model SpaceXAI has ever built for coding, smart tasks, and knowledge work. This is SpaceXAI’s strongest model and it is trained with Cursor.

The training data set of Grok 4.5 is based on**Programming, Science, Engineering and Mathematics**. Grok 4.5 performs well in actual engineering tasks, exceeding GPT 5.5 xhigh and Opus 4.8 max in some evaluations, second only to Fable 5, which was just unblocked by Company A.

Since the original article is an interactive evaluation diagram, which is not intuitive enough, I directly made an intuitive evaluation diagram for everyone.

(The following model effort defaults to the highest gear)

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709075139738.png" alt="image-20260709075139738" style="zoom:50%;" />

On Terminal-Bench 2.1, Grok 4.5 is 83.3%, which is basically the same as GPT-5.5’s 83.4%, and very close to Fable 5’s 84.3%.

On DeepSWE 1.0, Grok 4.5 is 62.0%, which is higher than Opus 4.8’s 55.8%, but lower than GPT-5.5 and Fable 5.

On SWE-Bench Pro, it is 64.7%. This result can beat GPT-5.5 and Composer 2.5, but it cannot beat Opus 4.8, let alone Fable 5.

So this set of scores does not support the claim that Grok has fully reached the top.

But we can preliminarily say:**Grok 4.5 has already entered the threshold of the first echelon**.

(This seems to be the case from the evaluation, but the actual experience needs to be discovered by your friends)

---

The article also mentions the training process of Grok 4.5. Grok 4.5 was trained on tens of thousands of NVIDIA GB300 GPUs. Its training process and stability technology are specially trained for large-scale operations.

Let’s just say that Lao Ma is really a tycoon in terms of computing power. He previously rented his GPU directly to Company A, but now he directly uses tens of thousands of GB300 GPUs to participate in training.

Others use tokens to build automated assembly lines, do demos, and complete company tasks. Are they using tokens to send humans to Mars?

The article mentioned that in addition to investing a lot of money in token training, a lot of money has also been invested in data filtering and management, so that the data mix maintains high coverage and high signal.

The previously released Composer 2.5 was specially trained for the programming field, but the Grok 4.5 released this time is trained in more fields.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709075915254.png" alt="image-20260709075915254" style="zoom:50%;" />

The article also mentioned that Grok 4.5 has extremely strong programming capabilities and is capable of complex Rust and C/C++ tasks. Many large models we used before were not well trained in the Rust language, so Rust is equivalent to a mirror for many large models. This time Grok 4.5 announced that it is capable of tasks in Rust and C/C++ languages, which shows that Grok is able to face the challenge this time without fear.

----

SpaceXAI’s official release gave another set of numbers.

Grok 4.5 is 80 TPS, and the API price is $2 per million input tokens and $6 per million output tokens. `grok-4.5` can also be found in xAI docs, and the context window is 500k tokens.

I also organized this piece into a picture.

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/8aa47abb7ba5924c750352b5a7aaab5c68812e27.png" alt="Grok 4.5 Price, context and token efficiency" style="zoom: 50%;" />

A dazzling number in the picture is a comparison chart of the average output token of SWE-Bench Pro.

SpaceXAI says Grok 4.5 outputs an average of 15,954 tokens per mission, and Opus 4.8 max is 67,020 tokens. That is the official 4.2 times gap.

In Coding Agent, this is a very realistic thing, because the cost is fatal.**
So this time Grok 4.5 doesn’t feel like I’m winning again in terms of running points.

It seems to be saying: I may not be the first in everything, but I am strong enough, fast enough, and cheap enough to undertake a large number of engineering tasks.

This reminds me of a characteristic I observed when I was in school: the top students in the class may not necessarily go the longest, but the students who are ranked 2-5 in the class are prone to sudden outbursts and are unable to hold back.

**This is a very Cursor goal.**
Flow-saving version: Someone directly summarized that the advantages of Grok 4.5 mainly include the following points.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709053717141.png" alt="image-20260709053717141" style="zoom: 67%;" />

---

I think one of the signals revealed by Grok 4.5 is that Grok is finally a little more pragmatic.

**The competition in AI Coding is changing from whose model has better running scores to who can get more realistic engineering results**.

As Lao Ma replied on the post, most tasks may not require the ability of Fable 5. Fable 5 will make demos more like products, but not all demos are products, demos can also be demos, that's all.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709081855127.png" alt="image-20260709081855127" style="zoom:50%;" />

The code is very simple to run.

But when encountering problems and bugs, how to deal with them, how to verify the results, and what to do after failure, they are getting closer and closer to Harness.

Cursor used to be a very useful AI IDE.

Now look, it may also be a model training entrance.

Whether it can go to heaven or not is not yet known.

But this time, at least Grok isn't just sitting in an X waiting to be teased like before.

Article reference:

https://x.ai/news/grok-4-5

https://cursor.com/cn/blog/grok-4-5
