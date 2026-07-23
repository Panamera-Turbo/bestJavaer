# GPT-5.6 Ran rm -rf in the Background

[English](./gpt-5-6-ran-rm-rf-in-the-background.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E7%A6%BB%E8%B0%B1%EF%BC%8CGPT-5.6%20%E7%AB%9F%E7%84%B6%E5%9C%A8%E5%90%8E%E5%8F%B0%E6%89%A7%E8%A1%8C%E4%BA%86%20rm%20-rf.md)

> Date: 2026-07-16

Hello everyone, my name is cxuan.

Yesterday, GPT 5.6 was officially released. A well-known social platform was full of criticism, shit, and slander about Fable 5. Many account owners also followed suit.

But I actually said yesterday: I want to pour cold water on GPT 5.6. I had a feeling it wouldn't work that well.

[Everyone is talking about GPT 5.6, but I might have to throw some cold water on it. ](https://mp.weixin.qq.com/s/sylMeZQM_DX2_SOsAM_s3g)

Just over a day after the results were released, the tide began to change.

---

I didn’t receive a push from Sol yesterday, so I tested Terra first.

At the time of release, the official caliber was probably: Terra’s capabilities are similar to GPT-5.5, and it saves tokens. I used to understand it this way -**Terra is a power-saving version of 5.5**.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711122054159.png" alt="image-20260711122054159" style="zoom:50%;" />

Then during the experience, I encountered two low-level problems first. . . . . .

One is that the model has finished running and there are almost no results visible on the interface.

One is that after streaming rendering, English is sprayed out together with Chinese, which reads like a pile of swill.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711123204082.png" alt="image-20260711123204082" style="zoom:50%;" />

I still can't tell if this is a problem with the ChatGPT Codex client or with the model itself.

But the conclusion is simple: the**experience is somewhat poor.**
---

When Grok 4.5 first came out the day before yesterday, I wrote an article saying that this time Grok 4.5 actually worked well.

[Cursor flipped the table, Grok 4.5 is going to the sky this time? ](https://mp.weixin.qq.com/s/uibtdVGdjCg6z9qELv1zpQ)

I poured cold water on GPT 5.6 again.

**As a result, these two views are now being fulfilled.**
On one side, the Grok 4.5 was seriously compared to the first tier.

On the other hand, the popularity of GPT 5.6 is changing from beating everything to being praised by only a few.

That’s not to say that 5.6 is completely unusable. It is to say:**The emotion on the release day and the physical feeling after actually getting started are not the same thing.**
### OpenAI understands reset

Now OpenAI knows one thing very well: resetting the quota is more effective than issuing another review draft.

Reset by invitation, reset by correcting bugs, reset by Ultraman after making a bet that he couldn't win, and even the official gave him a reset without any reason.

I really figured out the reset.

But the side effects of this move are also obvious: users will gradually regard reset as part of the product experience, rather than as a benefit.

What will happen if OpenAI is not reset one day?

Users have no loyalty. Which model is easier to use? Which model saves tokens? Which model is more cost-effective?

For example, I used to use GPT 5.5 every day, but now I am also using Grok 4.5. . .

If you rely on replenishing your quota every day to maintain stability, there must be something wrong with the product itself.

### Company A can’t sit still anymore.

In this wave of GPT 5.6, even Company A, which had no money to spare, reset its quota.

Fable 5 originally ended the promotional quota within the subscription on July 7, but it was later extended to July 12; as soon as 5.6 was released, Company A reset the 5 hours and weekly limit in full.

Tibo said directly below the official post: He smelled fear.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711133940980.png" alt="image-20260711133940980" style="zoom:50%;" />

There is certainly a yin and yang to this statement.

But what is certain is that Company A does feel some pressure. Otherwise, we would not have chosen to reset the quota as soon as GPT 5.6 was released.

The delayed rollout of Fable 5 also proves this.

---

I still remember how amazing I was when I used GPT 5.5, but this time around GPT-5.6 Sol, many people complained.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/175fb822cf58282570f809d8d0b9bf87.png" alt="175fb822cf58282570f809d8d0b9bf87" style="zoom:50%;" />

Simon Willison has written about sorting out the GPT-5.6 family (Luna/Terra/Sol), and admitted that Sol is very capable, but in terms of complex coding tasks that he often does, he still doesn’t think it is better than Fable.

Another more dazzling point is: Sol is very impressive on the official Agents’ Last Exam, but in a harder coding evaluation such as SWE-Bench Pro, Fable 5 self-reports about 80% and Sol about 64.6%. OpenAI also issued a special article questioning that SWE-Bench Pro has a large number of bad questions - this action itself also shows that the coding rankings have begun to tear each other apart.

But, more serious is Matt Shumer.

When he tested GPT-5.6 Sol, he ended up performing an operation similar to `rm -rf /Users/mattsdevbox`, deleting all the files on his Mac.

(Matt Shumer is the one who wrote “Big things are about to happen.”)

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711125211332.png" alt="image-20260711125211332" style="zoom:50%;" />

After this incident, my trust in GPT-5.6 Sol completely dropped.

Theo (t3.gg) also complained about a very engineering problem: after setting gpt-5.6-sol to `ultra`, all subagents under it will also inherit `ultra`, causing token burning for no reason, and it is also impossible to independently change the subagent's effort to medium.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711131208541.png" alt="image-20260711131208541" style="zoom:50%;" />

Because many people will fill up their effort on the first day, and burn tokens like crazy once they fill up, and then turn around and say that Sol is too expensive. . .

This guy also had a more direct post, saying that he was grateful for the cooperation between major manufacturers, which made Company A feel scared, so he continued to extend the offline rhythm of Fable 5.

I even think that Fable 5 may not switch to pure credits on the 12th as originally planned.

Now set up a flag and see if it will slap you in the face.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711134359615.png" alt="image-20260711134359615" style="zoom:50%;" />

---

I really feel that the current review is actually just a look at it.

What really determines whether you change the default model or not are these few things:

Will it produce stable results, will it randomly delete files, will it burn its credit limit for no reason, will it lose its intelligence for no reason, and will there be any additional surprises?

I'm not saying that GPT 5.6 has no strength. OpenAI is indeed outstanding in agent long-term tasks, tool invocation, and multi-agent orchestration.

But in the first wave of real feedback after the release,**stability and controllability**have already overwhelmed the excitement of being 10 points higher.

This is why I prefer to look at players like Grok 4.5 that are strong enough, fast enough, and cheap enough, instead of just focusing on the top one in the conference.

According to the current trend, top-level models will not be used simply to do work, but will sort out requirements, make designs, and come up with plans. The specific work must be handed over to models with strong engineering capabilities and that do not consume tokens so quickly.

---

##

If you really want to use GPT 5.6, first adjust the effort to medium instead of ultra.**
<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711134122300.png" alt="image-20260711134122300" style="zoom:50%;" />

This is basically consistent with an article I wrote before, as well as the views of many people in the circle now: xhigh/ultra are easy to overthink, are particularly wasteful of tokens, and are not cost-effective.

Unless you are doing a difficult and large siege mission, medium is often more cost-effective for general missions.

[Still using Codex to maximize xhigh? ](https://mp.weixin.qq.com/s/F9BDZm2JhjvpytyQ2yH4oQ)

---

After all, the biggest problem with GPT 5.6 now is that the new version of Codex combined with GPT 5.6 is not stable yet, there are many bugs, and everyone's expectations for GPT 5.6 are a bit too high, resulting in some gaps with the actual situation, so I feel that OpenAI is still a little anxious this time.

My current attitude is very simple: Sol continues to observe, Terra should be used as a spare tire to save money (in fact, it is not), Fable 5 is still the best choice if the quota can be met, and Grok 4.5 is worth trying.

The most important thing to do now is to wait for the release of GPT 6.x.
