# I finally pulled out the Codex's volume. It wasn't the output.

[English](./i-finally-pulled-out-the-codex-s-volume-it-wasn-t-the-output.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E6%88%91%E7%BB%88%E4%BA%8E%E6%8A%8A%20Codex%20%E7%9A%84%E7%94%A8%E9%87%8F%E6%89%92%E5%87%BA%E6%9D%A5%E4%BA%86%EF%BC%8C%E5%8E%9F%E6%9D%A5%E6%9C%80%E8%B4%B5%E7%9A%84%E4%B8%8D%E6%98%AF%E8%BE%93%E5%87%BA.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-11

I've been using Codex lately and I've been using it more and more, and I've been having a headache in my head:**

As you know, Codex became token's bill, and it was quickly used, so the headaches got worse.

And there's hardly any tools on the Internet that can be used. So what? What else can I do?

My main claim is to calculate the number of subscriptions to the Codex into Token, about what, and then understand what the number of Tokens and Pro 20x are.

So I wrote a little tool: **Codex Usage Estimator**.

Project address: https://github.com/crisxuan/codex-usage

The project did one thing, pulling the Codex usage out for you and generating local SVG charts.

---

Use is simple. When the project is pulled down, run directly under MacOS, Linux or WSL:

```bash
./run. sh
```

Windows PowerShell ran:

```bash
.\run. ps1
```

Script creates Python virtual environment, installs`codex-usage`Command, then run the doctor, demo and test.

Or these orders don't work, so pull down and let AI run out of statistics.

For example, I took a look at Codex on the day:

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260511064434712.png" alt="image-20260511064434712" style="zoom: 50%;" />

Primary means the 5h scale, secondary means the week scale.

As the log shows, I spent about 200 million tokens a day yesterday, and more than 90% of them were applied to the caped input, why so much?

Because I had a mission yesterday.`goal`Command, running for almost 20 hours without interruption, so caught input so much understandable.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260511064712304.png" alt="image-20260511064712304" style="zoom: 50%;" />

Codex-usage also directly generates local SVG charts.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260511065122037.png" alt="image-20260511065122037" style="zoom: 50%;" />

Many times we've never felt the same way about the amount of use, and I used to think it would be a lot more expensive to produce a long output, and it's often input that actually comes out and it's a lot of context, so if we look at total, it's easy to think that every time we burn, it's probably a lot of Cache hits.

As you know, output is the most expensive, so codex-usage calculates Pro 20x to be fully converted to approximately $2, 000 - $2200, so plus a week full is $100 - $110, of course, in extreme cases, because LLM cannot always output.

---

Let's say again that technology works.

The project technology warehouse is also relatively simple, with no traditional "AI preferred language", no Next.js, no database, no back-end service, no log-in system, no flowery dashboard.

Just a Python CLI.

There is only one major dependency:

```text
tiktoken>=0. 7. 0
```

The whole project was divided into a few blocks:

- `codex_logs.py`Read the Codex local session log`token_count`.
- `reporting.py`: Summarize the records into a table in the terminal.
- `charts.py`: Generate local HTML+ inline SVG charts.
- `transcript.py`: Parsing the manually imported Markdown dialog records.
- `storage.py`Other Organiser
- `tokens.py`: Token estimation using tiktoken.
- `cli.py`: Encapsulate these capabilities into command lines.

Local records exist directly:

```text
.codex-usage/
 groups.jsonl
 snapshots.jsonl
 turns.jsonl
 config.json
```

JSONL's advantage is simple.

Let's get to the point.`tiktoken`The official phrase for OpenAI Devicehttps://github.com/openai/tiktoken.

A lot of people may look at token statistics and think of all tokens.`tiktoken`Figure it out.

Not exactly.

It's got two main lines.

The first is the Codex local log.

```bash
codex-usage codex report --today --lang zh
```

This is from the Codex local session log.`token_count`event.

This number of tokens is already in the log itself, and the tools are scans, deltas by window of time, aggregations, displays.

So here's not taking tiktoken again.

It's more like going through the books in a local journal.

The second is manual import transcript.

For example, you save a conversation or a run log into Markdown, and then use:

```bash
codex-usage turn add --group repo-refactor --file transcript.md
```

This is when the tool does not know what the real request is for inside Codex. It can only be estimated on the basis of the visible text you import.

That's when it's needed.`tiktoken`.

If you specify the model, and tiktoken can identify it, it is calculated by the model's corresponding encoding.

So...`tiktoken`The role here is not to decipher Codex's internal usage, but to:

** Replace your locally visible text with a relative token estimate.**

For example, transcript can mark:

```markdown
- codex-usage: user--
User Input

-codex-usage: assant--
Assistant Output

- codex-usage: tool--
Tool Output

- codex-usage: file-content--
Document Context
```

This allows it to estimate user input, assistant output, tool output, context of the file separately.

It's better than a brain using the whole thing as a piece of text.

---

There is also the logic of a task force here. Why be a task force?

Because I think I need to know how much is consumed by different types of task: because simple chats, basic code modifications and large project re-engineering, long angent run is nothing.

So these types can't mix.

Like you used 5% today.

How many questions did you ask?

Or because it ran for eight hours?

Or did you put half the warehouse in it?

Without grouping, it is not clear.

So the tool has a concept of task group.

For example, I could build one:

```bash
codex-usage group create "repo-refactor" --label code
```

Then, before the mission begins, record the current usage:

```bash
codex-usage snapshot --group repo-refactor --usage 42
```

Remember once more after the end of the mission:

```bash
codex-usage snapshot --group repo-refactor --usage 47
```

in the middle of which you can direct the transfer or the running log.

Finally, it will tell you that this task force:

- How many turn.
- Estimating the number of requests.
- How many times did the tools call?
- See how much token is estimated.
- Effective token estimate.
- What's the amount of variation?
- Every 1% of what it looks like token.

This function looks a little manual.

But that's what I want.

Because of subscriptions, there's no 100% reverse.

It is already valuable to have a table of experience.

---

It should be noted, however, that this is not an official COdex usage statistics, so the specific data can only be estimated.

I must stress it here in order to avoid any misunderstanding.

This tool can't do much, but it can follow up as TODO.

- It can't read hidden systems.
- It can't read Codex's internal request.
- It doesn't know how many invisible tools each request carries.
- It doesn't know how to compress history inside the model.
- It cannot convert the percentage of subscriptions directly into official bills.
- It can't tell you how the backstage of OpenAi was cut.

It's not going to work yet, but maybe the follow-up will be perfect, so you can talk about PR, you can talk about issue, and more importantly, point.

And finally, this github has opened ** Micro-Media,** and it's not coming out here anymore, and those who really want to give feedback can go through the code in the project address.
