# OpenAI's Codex-Maxxing White Paper: Stop Treating an Agent Like a One-Shot Prompt

[English](./codex-maxxing-stop-using-agents-as-one-shot-prompts.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/OpenAI%20%E8%BF%99%E4%BB%BD%20Codex-maxxing%20%E7%99%BD%E7%9A%AE%E4%B9%A6%EF%BC%8C%E5%88%AB%E5%86%8D%E6%8A%8A%20Agent%20%E5%BD%93%E4%B8%80%E6%AC%A1%E6%80%A7%20prompt%20%E7%94%A8%E4%BA%86.md)

> English edition based on the Chinese original.

> Date: 2026-06-23

OpenAI published a new white paper on June 22, 2026.

It has an unusual name: `Codex-maxxing for long-running work`.

At first I expected another collection of Codex tips. After reading it, I think the message is more direct:

**OpenAI wants people to move Codex from one-shot question answering into a persistent place where long-running work happens.**

That applies to work beyond coding.

The white paper begins by acknowledging that Codex was built for coding work: modifying repositories, producing diffs, reviewing changes, and helping with releases.

Then the emphasis changes. OpenAI argues that work can continue beyond a single prompt when Codex has durable threads, shared memory, tools, recurrence, and a place where a person can review the output.

In plain language:

Stop asking only, "Can you write this for me?"

Give the Agent a persistent workstream. Let it remember the context, return on a schedule, update the artifact, and wait for you to make the decision.

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-01.png" alt="Cover of OpenAI's Codex-maxxing white paper" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

---

## Give the Work a Home

The concept I care about most in the paper is the durable thread.

Automations and the side panel both matter, but the durable thread is the foundation.

OpenAI gives several examples: monitoring social feedback, maintaining open-source projects, supporting the OpenAI CLI and Agents SDK, and running a Chief of Staff workflow.

They share one trait: the work is not finished today. Someone has to return tomorrow.

Maintaining an open-source project, for example, does not end after Codex fixes one issue. Over time it may need to read issues and release notes, notice contribution patterns, remember the maintainer's preferences, and prepare a pull request at the right moment.

Starting a new thread every time breaks the chain of prior context and decisions.

The paper recommends a pinned thread for an important workstream.

That thread becomes the work's home. Context, preferences, old decisions, and open loops all stay there.

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-05.png" alt="Durable threads page" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

There is a cost.

A long thread carries more context, so it can cost more to run than a short one.

OpenAI does not pretend continuity is free. Its position is straightforward: important work is worth some additional cost.

I agree.

Agent tasks often fail in the middle because the Agent forgets why it made an earlier decision.

Humans have the same problem. If a project has no stable place for background, decisions, and next steps, returning after two days is disorienting.

Codex simply makes the problem more visible.

---

## The Value of Voice Input Is Not Speed

The second idea is voice input.

Many people see voice as a faster substitute for typing.

OpenAI is pointing at something else: speaking preserves the way people actually think.

You might say:

> I remember someone named Ben mentioning this in Slack, but I am not sure. Go find it.

You may delete that sentence while typing because it feels incomplete and informal.

Real work often begins exactly there.

A half-remembered name, a vague direction, an uncertain judgment, or a detail that just surfaced can be valuable context for an Agent.

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-07.png" alt="Voice input page" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

I increasingly think Agent context should not be too clean.

An overly polished prompt resembles an exam question: the boundaries are clear, the material is complete, and the expected answer is relatively narrow.

Work does not look like that.

It is usually a pile of incomplete information: a sentence from a meeting, a complaint in Slack, an old comment in the code, or an unhappy customer who never stated the problem directly.

People combine those fragments.

Agents need the fragments too.

The real value of voice input is that it gets the unorganized material out of your head first. Codex can then turn it into a plan, a draft, an artifact, and a set of next actions.

---

## Memory Must Be Reviewable

The white paper dedicates a page to memory and offers a simple structure:

```text
vault/
  TODO.md
  people/
  projects/
  agent/
  notes/
```

The structure is simple, but the direction is right.

A long thread cannot rely only on chat history. Useful context should become something a person can open, edit, diff, and reuse.

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-10.png" alt="Memory vault page" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

The boundary matters.

The code repository contains code.

The vault contains work context.

That includes people, decisions, open loops, daily notes, project state, and details that would otherwise be forgotten in two days.

If the vault lives on GitHub, the diff becomes a review surface for memory.

You can see which facts Codex considered important enough to preserve.

This is critical because long-running work is vulnerable to memory drift.

An Agent may form a vague impression in conversation and later use that impression to make a decision. That is dangerous.

Writing memory down is safer.

Who prefers what? Which project is waiting on whom? Which decision is final? Which loop has closed?

Once memory is in files, it can be reviewed.

Reviewability is what makes long-running work acceptable.

---

## Real Long-Running Work Depends on Loops

The thread automations section goes well beyond ordinary reminders.

The paper calls them heartbeat-style recurring wake-up calls.

Codex returns to the same thread on a schedule and continues from the same context.

A normal prompt says, "Do this now."

A thread automation says, "Come back periodically, check whether anything changed, and move the work forward one step."

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-16.png" alt="Thread automations page" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

The paper gives a concrete example:

Every 30 minutes, check Slack and Gmail for messages that need a response. Research the context and draft replies.

Do not send them.

That defines a useful division of labor.

Codex prepares the decision: it finds the messages, gathers context, drafts a response, and raises questions.

The person makes the decision: approve or reject, choose the tone, choose the timing, and decide what is finally sent.

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-19.png" alt="Chief of Staff loop page" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

That boundary cannot be skipped.

Agent automation is often imagined as fully autonomous execution. The paper's examples are more restrained.

In a Chief of Staff loop, a person owns approval, tone, timing, and the final decision.

In a refund follow-up loop, a person owns consent, approval, and every irreversible action.

That is a realistic operating model.

Let the Agent prepare the material until the decision is ready.

Bring a person back before any irreversible action.

---

## A Strong Goal Is the Minimum Requirement

The second half of the white paper discusses goals.

This matches my own experience with Codex.

A weak goal looks like this:

```text
Implement the plan in this Markdown file.
```

There is a task, but no acceptance line.

A strong goal gives Codex a testable standard: expected behavior, review criteria, constraints, or a clear definition of done.

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-22.png" alt="Goals page" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

The paper uses a Rich-to-Rust migration as an example.

The goal becomes concrete: after the migration, the original unit tests still pass.

The existing test suite is the acceptance criterion.

This is an engineering approach.

Without an acceptance line, an Agent can look very busy.

It reads files, modifies code, writes explanations, and offers many reasons for what it did.

Yet constant activity does not mean it is approaching completion.

I try to include language like this in my own Codex tasks:

```text
Completion criteria:
- Existing behavior remains unchanged.
- Relevant tests pass.
- Unrelated modules are not modified.
- Report changed files, verification commands, and failed attempts.
```

This is not process theater.

It tells the Agent when to stop.

---

## The Side Panel Pulls Artifacts Into the Loop

The final major idea is the side panel.

It addresses a practical problem in Agent products: work cannot always be reviewed inside a chat box.

Markdown, spreadsheets, CSV files, PDFs, slides, web pages, and notebooks have their own forms.

They should not be flattened into a conversation transcript.

<img src="../../../ai-articles/01-agent-and-coding/codex-maxxing-assets/page-24.png" alt="Side panel page" style="zoom:50%;" />

*Source: page rendered from OpenAI's official white paper.*

The side panel lets you and Codex look at the same artifact.

You leave a comment on the artifact, and the comment becomes an instruction.

You inspect an `index.html` file in the browser, and Codex edits it.

You inspect formulas and cells in a spreadsheet, and Codex edits them.

You inspect slide layout, and Codex edits the deck.

That is very different from ordinary chat.

The chat box is good for assigning work.

The side panel is better for finishing it.

One line in the paper is especially accurate: the side panel is where Codex begins to become the place where work happens.

That is the part of Codex I will watch most closely. The open question is whether those artifact review surfaces can hold up under everyday work.

---

## What Is the White Paper Really Saying?

My summary is simple:

**OpenAI is moving Codex from executing one task toward maintaining a long-running workstream.**

That requires four elements.

A durable thread gives the work a home.

Reviewable memory prevents context from drifting invisibly.

A verifiable goal tells the Agent when the work is complete.

Human confirmation before irreversible actions gives automation a boundary.

Together, these make Codex look more like a long-term collaborator.

One-shot prompts will continue to exist.

But important work cannot depend entirely on a single prompt.

The Agent needs to remember why the work exists, know the next step, return later, and place an artifact in front of you for review.

The person no longer has to explain everything from the beginning.

The Agent no longer has to guess from the beginning.

That is the meaning behind the strange name Codex-maxxing.

Its core idea is organizing work so an Agent can actually carry it.

---

## Sources

- OpenAI: [Codex-maxxing for long-running work](https://openai.com/index/codex-maxxing-long-running-work/), published June 22, 2026.
- OpenAI PDF: [OAI_WhitePaper_Codex-maxxing26.pdf](https://cdn.openai.com/pdf/8a9f00cf-d379-4e20-b06f-dd7ba5196a11/OAI_WhitePaper_Codex-maxxing26.pdf).
- Images in this article are rendered pages from the official white paper.
