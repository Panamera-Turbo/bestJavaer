# Still using Codex to drive x high? Big mistake.

[English](./still-using-codex-to-drive-x-high-big-mistake.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E8%BF%98%E5%9C%A8%E7%94%A8%20Codex%20%E5%BC%80%20xhigh%20%E6%8B%89%E6%BB%A1%E8%B7%91%EF%BC%9F%E5%A4%A7%E9%94%99%E7%89%B9%E9%94%99.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


I recently found an interesting phenomenon.

A lot of people use Codex to come up and drive effort.`xhigh`.

Whether it's a new README, or a little bug, or start a project, or let it watch a blunder, the first reaction is: stretch!

(Not only for Codex, all LLMs with effort apply.

It's like you were going to wash a car, and then you drove into the garage and washed it with people.

---

It doesn't make any sense.

`xhigh`It definitely works. OpenAI, given this slot, means it's not set. But I'm getting the feeling that it's not the best option to use it as a default configuration.

** researching effort is not an IQ switch, it's more like a mirror.**

This mirror reflects the degree of dependence on the difficulty of different tasks, whether it is the speed of the main fight or the lack of consideration for a straight stretch.

What you need to think about is longer time, higher token consumption, slower response, and more space for reasoning on complex tasks.

But it doesn't automatically help you turn a bad mission into a good one.

![image-20260530174346491](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260530174346491.png)

---

I had that problem before.

When I first started using the code, I had a very simple mind: I let it work, and I gave it the strongest.

That's the downside of the subscription system, and if it doesn't run out, it feels psychologically bad. And Codex resets the rhythm three times a week, and anyone feels bad.

![image-20260526153155000](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526153155000.png)

But when it's too much, you'll find that some of the missions are going on.`xhigh`Not just unnecessary, but counterproductive.

Let Codex change the name of the variable, add a note, sort out the log, or make a little more smoother.

What are the core demands of such a mandate?

How fast and save.

You want it to understand, to do it, to finish it, to diff. It's not like it's half a day in the back, and it's finally giving you a "comprehensively weighed" variable name.

What's more critical is that we're not going to be able to do this.`xhigh`It's easy to create the illusion that, as long as the result is bad, the model is not long enough.

But in many cases, that is not the problem at all.

The problem may be that you didn't give the test order, you didn't say what the acceptance criteria were, you didn't tell it which directory you couldn't touch, you didn't tell me what the business background was, or even what the workspace was.

These things can't be saved by driving any higher.

At best, it bypasses the road more seriously in the wrong context.

---

The official didn't ask you to fill it up

The Codex configuration file for OpenAI does have`model_reasoning_effort`I don't know. It supports`minimal`, `low`, `medium`, `high`, `xhigh`These slots.

![image-20260526153350052](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526153350052.png)

But in the instructions of reading mobiles,`xhigh`The location is clearly written: in-depth research, walk-through workflows, angent missions that require long rollout, and security audits, complex code review, difficult coding missions.

![image-20260526153548884](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526153548884.png)

And one more thing I think is very critical:

Only if the extra delay and cost are justified by eval`xhigh`.

This is the easiest place to ignore when many people use AI tools: we can easily mistook "more expensive, slower, heavier" as "more professional."

The longer the hint, the more professional it seems.

The more the context gets, the more professional it seems.

The more MCP gets, the more professional it seems.

The higher you drive, the more professional you seem.

But that's not how it works. Engineering is about discipline, feedback and validation. If a mission can be solved in three minutes, you have to give it 30 minutes to prove that you're trying. It's not a professional, it's a professional.

---

# The real influence on Codex is often not effort

The biggest difference between Codex and regular chats is that it's an anent, while regular chats are bit bot.

You can read files, run orders, read errors, change codes, run again.

So the real influence is that you don't often put effort from`medium`Screw`xhigh`And it's these simpler things:

The root list is right.

Test orders have no.

`AGENTS.md`Have you made the rules clear?

Enough privileges.

The context is not clean.

Did you tell it "to what extent it is complete"?

I'm now increasingly convinced of one thing:** a medium with a clear context, which is often more than an xheigh with a context.**

And even more troublesome, the default.`xhigh`It'll make you lazy.

You're going to do less job splits, less acceptance standards, less attention to test feedback, and then you're going to leave all the questions to "think about it".

I used to do that before.

And then xheigh pulled you a piece.

We are often caught in a subscription trap as if we were using it to consume it, not to do it well.

---

# I'd rather be diverted by mission

It's more comfortable to use it, but it's simple to judge the type of task.

![image-20260530174937782](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260530174937782.png)

Light duty.`low`.

For example, rewrites, ticking fields, formatting, a very shallow type error. Such missions do not require in-depth reasoning, they require quick hands and do not play games.

General development`medium`.

A small function, a supplementary test, a normal bug processing, a log reading, a synthesis.`medium`Mostly enough. OpenAI also mentioned in GPT-5. 5 that default is`medium`And a lot of workloads`low`You can run well.

Complex mission back.`high`.

For example, cross-module re-engineering, difficulties bugs, structure options trade-offs, context analysis. At this point, it is reasonable to give more room for reasoning, since the task itself needs to be planned and weighed.

`xhigh`And?

Leave a few real hard things.

Like security audits, complex code review, long-link research, coding workwork, or you've tried.`medium` / `high`It's actually a breath away.

I'll drive again.`xhigh`I think it's okay.

But by default, it belonged to a mosquito with an Italian gun from Li Yunlong.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526164759871.png" alt="image-20260526164759871" style="zoom: 50%;" />

---

If you're used to Codex CLI, you can have a few profiles.

```toml
[profiles. fast]
model_reasoning_effort = "low"

[profiles. work]
model_reasoning_effort = "medium"

[profiles. deep]
model_reasoning_effort = "high"
```

I didn't write here on purpose.`xhigh`.

The reason is that x high shouldn't be the daily entrance to work.

You've got the kind of "this mission today is to get it done hard" and cut it off for a while.

It's a bit like permission.

You do not default on all items to maximum privileges because of the occasional need for full access. The tool gives you a choice, which does not mean that each option fits the default.

---

I've always felt that one of the most misleading words of the AI era was: "AI amplifies people's abilities."

A lot of people heard that, but only the word "deep".

But what it's really cruel is that it also magnifies your confusion.

You've got a clear target. It'll help you get there.

Your judgment is vague, it will lead you further away.

You give it a good question, it gives you a good solution.

You give it a bad question. Open it again.`xhigh`It's just working harder around you.

So one of the principles I'm using in Codex is:

Day`medium`Light task.`low`Complex tasks`high`.

`xhigh`Keep it.

We'll drive when we need it.

**AI is the best solver, but not the expert judge. It's human judgment that really should drive to extra high.**

---

References:

- OpenAI Codex Configuration Reference: `model_reasoning_effort`Support`minimal`, `low`, `medium`, `high`, `xhigh`and`xhigh`Reliance on model support. https://developers.openai.com/codex/config-reference
- OpenAI Reasoning Models: Different appliances for different things.`xhigh`It is only recommended that they be used when additional delays and costs are justified. https://developers.openai.com/api/docs/guides/reasoning#reasoning-effort
- OpenAI Using GPT-5. 5: Default`medium`A lot of workloads`low`I can do well. https://developers.openai.com/api/docs/guides/latest-model#using-reasoning-models
- OpenAI Codex Best Practices: A uniform configuration model, reassonating email, privileges, profiles, etc. are recommended. https://developers.openai.com/codex/learn/best-practices#configure-codex-for-consistency
- OpenAI Codex Pricing: Codex usage is associated with models, task complexity, local or cloudy tasks, with complex context and long tasks consuming more quotas. https://developers.openai.com/codex/pricing
