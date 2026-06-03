# How to Get the Most Out of Codex

[English](./how-to-get-the-most-out-of-codex.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E5%A6%82%E4%BD%95%E6%8A%8A%20Codex%20%E7%94%A8%E5%88%B0%E6%9E%81%E8%87%B4.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


For the first time, most developers use programming events to write codes: check a warehouse, generate a diff, run tests, open a full request.

This is still the focus of Codex. But much of the work on the computer is based on code: executing shell commands, browsing web pages, calling API, exporting documents, responding to events, triggering automation. When these interfaces are always open to Codex, it makes people feel no longer like programming assistants in a narrow sense, but more like a system used to do all kinds of work on computers.

Codex applies this transition to reality. A thread (thread) keeps context, uses tools, presents, and multi-wheel prompt continues, rather than reset after each interaction.

If you want more from Codex, you need to put these together:

- durable threads, keep context
- Voice, managing, queuing, keeping users on the way back. Lee.
- Browser, browser-use, MCP server and connéctor to enable Codex to move outside the warehouse
- Thread automation and goal (Goals) to continue work as users leave
- Sidebar (sidepanel), where users review codes, documents, slides and other products

---

# Enduring threads

> Lasting Thread: a long-run Codex Thread that keeps the working context across multiple sessions.

The toplined threads are one way to put the long-term threads on hand. It is suitable for recurring work streams such as:

- A Chief of Staff route.
- A distribution thread.
- A document review thread.
- A line for external surveillance.

These are permanent workspaces, not short chats. Codex can return to these lines over and over time, preserving previous decisions, preferences and working context - otherwise they will have to be rebuilt from scratch.

The shortcut of the top line makes this work. Command-1 to Command-9 can jump directly into saved threads.

> This is really useful because it's been developed with AI for a long time, and I'll find that many times the same task will be scattered in a different Thread, which is the equivalent of turning Thread into a role.

---

# Voice input

The value of voice input is that it captures a rough version of an idea before it is compressed into text.

Codex has embedded voice input. It's particularly useful when it's natural and it's typographical, but it's very awkward:

I remember a guy named Ben who mentioned this in Slack.
I don't remember the details.
Go check it out.

This is usually enough for an agent who can search, gather context and report back.

When the mission is not yet fully operational, it is appropriate to pour out a brain for two or three minutes.

Reproduction text is the same. An original conference transcript, or an oral plan note, tends to provide better material than a brief summary, as it retains uncertainty, emphasis and unfinished thought.

---

Control and queue

It becomes more useful when the voice is matched by clear control over an ongoing mission.

> Steering: By the end of the current step, interrupt an ongoing Codex mission in a new direction.

When angent goes in the wrong direction and needs to correct it before it's finished, manipulation is useful. For example, in evaluating a website, users can interrupt their work while marking the interface in a sidebar:

- Make this smaller.
- The distance between these two elements doesn't feel right.
- It's the wrong story.

> Queuing: Add something that Codex will do after the current step has been completed.

Line up is different. It does not interrupt ongoing missions, but ranks the next. The user may say:

When this is done, the preview link is sent to the reviewers in Slack.

Control the change that Codex is doing right now, line up to change what happens next. Both allow users to remain close to it as work unfolds.

Steering is also very useful, and I'm using Steering regularly when I'm using Goal to get him to run an implementation plan to determine whether it matches expectations, if it's drifting, etc.

---

Tools and reach range

Once a thread has continuity, the next question is what it can do. Codex can extend from one layer to another:

- `$browser`, the application internal browser in the sidebar where Codex can check and mark the web world Noodles.
- `@chrome`, corresponds to the login browser state, and to the workstream based on Chrome
- `@computer`jobs that only exist in the desktop GUI (GUI)

`$browser`Suits the browser review in the sidebar.`@chrome`Fits to browsers that rely on the context of the user crome and require login.`@computer`Fits to tasks that can only be performed through the desktop GUI.

MCP server and connéctor extend the same thinking to the rest of the workflow.

Slack, Gmail and Calendar are important because many important tasks begin with messages, inbox entries or scheduling problems and become code.

Skills allows duplicate work streams to be reused. Once a stream has proved useful, wrap it up into a skill so that Codex can run again next time without learning the process from zero.

---

I can work anywhere

The Codex mobile version changed the "user has to sit in front of the job". A task can be started on Mac - where the documents, access and local configuration are already there - and then move forward when users view it on their mobile phones.

This is important at some small moments. A person can leave the workplace on a longer mission in Codex, answer a question outside, approve the next step, or change the course before returning to the seat. The local environment remains in place without the need for users.

---

## Automation

Automation of Codex work as planned. If a repetitive task should start entirely new in a workspace - for example, a daily newspaper, or a regular warehouse inspection - it should be timed automation. If the plan should go back to an active conversation with the context, it would be automatic with the thread.

> Wire automation: heart beating, periodic awakening, returning to the same Codex line as planned.

It's very useful to have toplines, but they're still waiting for users to come back. Wire automation allows for checking something every few minutes or hours, continuing until a condition is met and adjusting the rhythm over time.

A Chief of Staff may run every 30 minutes:

> Every 30 minutes, check the Slack and Gmail messages that require my attention and no response.
Help me prioritize the most important things.
> If someone asks me a question, study the answer as thoroughly as possible and draft a response for me, but do not send it.

When users return, the most expensive part of collecting context is often completed. It's still up to people to decide what to send.

Wire automation is also appropriate for feedback cycles. A linear automation can keep an eye on comments from pull reQuest, Google Docs, or Slack's response, and keep the surroundings moving forward when the user leaves.

Imagine an animated workflow: the reviewers shared a video in Slack. An automated thread check this session as planned, render an updated version when comments arrive, and respond in the same session @ the evaluator. If an integration does not complete the final upload, desktop automation can do this through GUI.

This cycle spans three places: receiving feedback with Slack, reproducing with the code library, automating the final upload with the desktop.

It's also important for my day-to-day life, but it's like a time job, and it's supposed to be well known.

---

## /goal

The Goals are the strongest when a mission has a real finish line and angent can keep moving towards it. A weak goal is to:

> Target: Longer-run Codex missions with a finish line, where angent works for a long time.

> Get this plan out of the Markdown file.

A stronger goal has a measurable success standard.

For example, an engineer may be moving an internal tool from Python to Rust: build a new directory, define a target and write the finish line clearly - new results are not complete until the module tests are passed.

One objective combines continuous implementation with a Verifier. User defines the result, the condition of the stop, and the signal that indicates whether Codex is near the end point.

Useful certifiers include:

- A test package.
- A benchmark.
- Once, bug, repeat.
- A validation matrix.
- An end-to-end workflow that must be kept through.

Ambitiousness is important, but without proof, it is simply a wish.

>jason's role for /goal is almost identical to what I and everyone expected, and AI can help you do all the work in a row, but you have to make sure he doesn't drift.

---

# Sidebar

The sidebar leaves the results next to the conversation that produced it. Users do not need to export a product and switch it to the context, but can examine it in situ. The output may be code, but it may also be a slide, a PDF, a browser page, a table, or other products generated during the process.

It is particularly good at four things:

1. Inspection of products
2. Marking where changes are needed
3. Operating the web community Noodles.
4. Review changes

The sidebar allows users to view Marktown, spreadsheets, data tables, documents and slides in situ. They can inspect, mark, modify these products without interrupting the entire circuit.

![image-20260528225123982](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260528225123982.png)

That slide or PDF can be kept next to the thread that produced it, and can be reviewed and repaired directly at any time.

![image-20260528225140304](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260528225140304.png)

Apply an internal browser to allow Codex to check a releasing page, control it, and respond directly to the comment on the reviewed interface. Comments on a page or product remain within the working circuit instead of becoming a separate handover.

The web page becomes both an output and a control interface. Codex can build a product, open it in the sidebar, check it, debug it and grind the same object on the ground.

![image-20260528225157527](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260528225157527.png)

The following are particularly appropriate:

- `index. html`, for light static products
- Storybook for UI evaluation
- Remotion Studio for programmable animations
- Slide based on browser for presentation
- Data applications (data apps) for analysis of class workflows

A single index. html file, without a server, can be a lasting, interactive product. Wire automation can also refresh these static products over time, so that when users return, new things are waiting in the thread.

---

# Sharing memories

They become even more useful when long-run threads share a memory located outside any individual dialogue.

> Sharing memory: the enduring context that is stored outside a single thread allows future work to be carried on from a clear, accessible item.

One way to afford time is to keep a durable thread anchor in an Obsidian vaault. Operationally, this means a folder consisting of a plain text file, which is always easy to check, edit, move and keep over time. The team can put this folder in cloud storage, Git, Dropbox, Google Drive, or any other synchronous layer suitable for its own workflow.

A vault may be about this:

```
vault/
├── TODO.md
├── people/
├── projects/
├── agent/
└── notes/
```

At the top,`AGENTS.md`It can be defined: how Codex should update this workspace when it knows more about people, projects, decisions and unfinished business.

Do not copy an exact vart structure. To teach ant: where to live, what to keep, and when not to make unnecessary changes.

A practical one.`AGENTS.md`It may read:

- Put`~/vault`As a permanent work memory.
- Better to regulate notes than to spread them everywhere.
- Todos, people, projects, daily summaries and draft notes are clearly placed.
- Retain decisions, block items, responsible persons, dates and useful links.
- If there's no meaningful change, we're not gonna stir this up.

The code warehouse contains the code. vault contains a rolling context: about the people involved, what has changed, where the cards are, what needs to be followed up, and what would otherwise disappear between sessions.

The important context should not be in a single record of dialogue. Write it somewhere where the next thread can go on.

Codex has a first-party memory function.`Settings > Personalization > Memories`Lee. They provide a local memory layer for preferences, recurring workflows and known pits. They are a supplement to, and not a substitute for, the context of the obvious. Chronicle pulls in the same direction -- it helps Codex build memories from the nearest screen context.

From the code

Codex still starts with the code. However, more work around the code can now be accessed through the same system: MCP server, browser interface, desktop control, linear automation, and reviewable products.

This changes the control model. Controls interrupt ongoing work. Line up and line up the next task. Wire automation keeps a thread active as users walk away. And the goal is to add a specific finish line so that Codex can work on it.

Now, Codex is able to carry a work stream from command to execution, to product evaluation, even if the work has left the code warehouse.

---

# My thoughts

Many of the functions of this presentation are very useful to me.

The old model is a prompt for a diff, angent is a function you call. The new model is a long line, you take it like a colleague. Steering is a face-to-face interruption, queuing is the next thing to say, automation is it works on its own, goal is giving it an acceptance standard. The long list of articles is essentially an original language of management subordinates.

And a very tasteful one is that /goal that section, goal didn't verify that your blueprint was just a wish. This is not just about Codex being set up.

The real problem with Agent's landing is not the power, the power is long enough, and what's missing is an answer to whether it did the right thing. Python moves Rust, and that's a good example of how it works at the finish line -- it's a single test, not a similar feeling. My own basics and my articles are identical: without the task of validation, the output of angent is largely not directly usable.

But the most important section is the sharing of memories, but it is placed very far behind. The background of the previous series of capabilities is to allow a thread to continue over a long period of time; but as long as the context is only in the record of the dialogue, the so-called long term is a lie - the long distance is lost.

What really lasts is the vault: a plain text folder, plus one.`AGENTS.md`Teach angent how to maintain it. Watch out for the AGENTS.md.

One last point: vault, this model is not unique to OpenAI. Claude Code.`CLAUDE.md`And the same thing that comes to mind -- the memory of angent is the original text file in the warehouse, which can see, change, have a version control. Angent is not the model, but the external memory.

The function OpenAi will always add, but the lasting, plain-text memory that you're maintaining, you have to do it yourself.

---

* Original language: Jason Liu (@jxnlco), Getting the most out of Codex, 2026-05-20 published in X (long form). Thrust link: https://x.com/jxnlco/status/2057153744630890620*
