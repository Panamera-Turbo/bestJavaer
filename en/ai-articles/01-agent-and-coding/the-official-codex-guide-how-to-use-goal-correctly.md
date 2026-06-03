# The Official Codex Guide: How to Use /goal Correctly

[English](./the-official-codex-guide-how-to-use-goal-correctly.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Codex%20%E5%AE%98%E6%96%B9%EF%BC%9Agoal%20%E7%9A%84%E6%AD%A3%E7%A1%AE%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-25

Since the end of Tibo sent a statement that repaired the bug used for Codex subscriptions, it is clear that the feeling is that the subscriptions are slow.

So much for now.`/goal`This model can become a little unbridled.

![image-20260525074929785](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260525074929785.png)

Wait, when it comes to /goal, actually, Officer Codex has a very practical use on the Internet, so let's talk about it.

---

Codex officially has a very prominent description of /goal:

> Use /goal when the task requires Codex to work continuously across the rounds to meet verifiable cessation conditions.

Not all commands fit in /goal mode, and the scenes suitable for /goal are mainly:

- Long run coding, with clear conditions for success and certification cycles.
- Codex can continue to make scope progress in projects involving code migration, large-scale re-engineering, deployment re-testing, experiments, games and side projects.
- There is a need for long-term teams with clear success criteria.

The three points above have a clear standard for use.

**/goal achieves the ultimate goal that you hope Codex will be able to accomplish and confirm the validity of the result by means of concrete and verifiable means, while ensuring that the restrictions observed are not undermined.**

To give you an example of how to use /goal:

```prompt
Give a clear border target

/goal converts the login page of this React application to a usable status, fixes the current error and ensures that npm run burn passes.


# Write acceptance criteria

Completion criteria:
- The login forms can be submitted.
- Error hint normal.
- The movement-end layout doesn't spill.
- Npm run lint and npm run burn

# Give me a condition border

Do not change backend interface; only src/app/login related files.

# Give priority

Priority assurance is available, followed by beautification of UI.
```

This is the case where you know what to do with /goal. Have clear objectives and verifiable conditions.

So if you don't know what to do with /goal, it's okay to use this slash?

It's okay.

And one of the things that applies is open exploration when you don't know what you're going to do.

Like what?

![image-20260525081205431](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260525081205431.png)

Of course, this example is a little extreme.

![image-20260525093040293](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260525093040293.png)

But you can make him a hundred degrees or Ali.

![image-20260525093409528](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260525093409528.png)

This suddenly reminds me of the many needs of the ancient programming period, which now seems to be a real landing demand.

---

If you enter /goal on Codex without seeing the slash command appear in the list, then you need`config.toml`Enabled`features. goals`.

```toml
[features]
goals = true
```

You can also start /goal in Codex Cli.

/goal is simpler to use, currently supported

```bash
/goal pause ## pause the goal
/goal resume ## resume the goal
/goal clear ## clear the goal
```

This refers to the use of goals. If you want to use /goals, you need to create a work contract:

1. Specify an objective and a condition for cessation.
2. Tell Codex which documents, documents, issues, logs or plans to read first.
3. Define which orders or products can prove progress.
4. Codex is required to perform checkpoint jobs and keep short progress records.
Run-time /goal to see state
When completed, blocked or directionally changed, control it with pause, resume or clear.

And here's a real-faith advice for you, don't let a /goal order go all the way dark, and I've used /goal to do a 75h command before, but it's not exactly the same as a time loss factor.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/f127f7f7a0e464e7af71159653da1442.png" alt="f127f7f7a0e464e7af71159653da1442" style="zoom: 67%;" />

When you use Goal, you better get Goal to Codex with a tight progress report, a periodic status update, including

- Current checkpoint;
- Verified content;
- Remaining work;
- Whether it is blocked.

If the status report becomes vague, do not continue to add piecemeal instructions, but tighten the goal: specify the next checkpoint, which order to prove completion, and what should be suspended.

The official document location is: /goal more like a backstage job. When you give it clear objectives, it can work on its own for a long time and stop when it is convinced that the conditions for cessation have been met.

Here are a few examples that you can refer to.

Technological dam migration:

```prompt
/goal to move the project from [old technology warehouse] to [target technology warehouse]. Ensures that all pages have consistent visual performance and validates the output with Playwright.
```

Prototype creation:

```prompt
/goal achieves the first version by PLAN.md, creates a test for each milestone and validates the output with Playwright. Reference is made, if necessary, to a given cut-off chart.
```

Phrasing:

```prompt
/goal Optimizing [Phrasing file or directory] until the eval package reaches [target score or pass rate]. Run [eval command] after each change, check the failed example and keep the change small and precise. Achievement of the target, or subsequent modification, will be discontinued when product/policy judgement is required.
```

---

Honestly, I feel right now that /goal is the best match for something, is a PRD or spec.

Because /goal essentially solves the problem of continuous implementation.

However, there is a prerequisite for continued implementation:

** It has to know what it's doing.**

If you just lose one sentence:

```prompt
/goal finish this function according to PRD
```

It's basically the same thing that you give Codex a big direction, and then you let him guess what has to be done, what can be done and where the conflict should stop asking you.

This approach is more risky.

In particular, this type of document, which is often written in terms of "product intent" and "user experience", has many similarities:

- Users want a process to be easier to complete;
- Pages need to be sufficiently clear;
- Interactivity as natural as possible;
- Follow-up can support a capacity.

These descriptions are very understandable to people, but for Codex, without acceptance standards, they are easy to miss.

So what I'd rather recommend is that we don't just let /goal do it directly according to the PRD, but instead let the PRD and the spec combine to produce a blueprint for implementation.

I think so:

```prompt
/goal achieves [functional name] according to docs/PRD.md and docs/SPEC.md.

Read the two documents and organize them:
1. Needs to be met
2. Clarifying non-targets
3. Acceptance and inspection standards for certification
4. Possible areas of ambiguity or conflict
5. Order of recommendation checkpoint implementation

If there is a conflict between the PRD and the SPEC, suspend and specify and do not decide for yourself.
Each checkpoint completed runs the corresponding test.
Only when all acceptance standards are met, construction passes and critical process validation is completed.
```

The focus of this prompt is to break the essay to checklist before it starts.

My own use experience is that PRD and spec better work clearly:

- The PRD is responsible for telling Codex why, who the users are, what the core process is, and what the experience cannot deviate from.
- Spec is responsible for informing Codex how the interface is designed, how the data is flowing, what the boundary conditions are and which tests must be passed.
*/goal is responsible for turning the two documents into an implementation cycle that can be continuously advanced.

In conclusion:

```text
PRD decides direction, spec decides boundary,/goal is responsible for propulsion and validation.
```

These three things work together, and the quality of Codex's execution will be markedly stable.

I've stepped on a pit before, and I've written a complete PRD, and then I'll just let it happen. And as a result, Codex did try hard, but it would take some of the TODOs as current version needs.

For example, the PRD wrote:

Support for multi-tenant configurations may be considered later.

It might really start designing multi-tenant data structures.

Did you say it was wrong?

It's not entirely wrong, because it does appear in the document.

But this is clearly not what should be done at this stage.

So I'm going to add a very important word to the story:

```prompt
The "follow-up" "future" "may consider" "extensible" content that appears in the PRD, and the default is considered non-target unless the SPEC or completion criteria explicitly require that it be achieved.
```

This small restriction is very useful and can significantly reduce Codex's excesses.

If you have a PRD, no spec, I suggest not just open /goal, but let Codex generate a light spec.

For example:

```prompt
Read docs/PRD.md, not code.
Please organize this into an inventory containing:
- Functions that the current version must achieve
- Not a target.
- Data structure and state flow
- UI Page and Key Interactive
- Acceptance and inspection standards
- Test advice.
- Something I need to know.
```

When this spec confirms, then open.

It would be much more stable than reading the PRD by writing code.

If you already have PRD and spec, then you can be a little more radical and just let /goal start running.

This is the complete template I used more often:

```prompt
/goal completes [functional name] version 1 according to docs/PRD.md and docs/SPEC.md.

Implementing rules:
- PRD is the source of product objectives and user processes
- SPEC is the source of the compact for technology realization and interface
- If there is a conflict between the two, the SPEC shall prevail, provided that it is indicated in the progress report
- Future planning default in PRD
- Do not modify modules not related to this function

Working methods:
- Checklist and checkpoint first.
- Run the tests after each checkpoint is completed
- If pages are involved, use the browser to verify the main process
- If construction or testing fails, first fix failure

Completion criteria:
- The current version of the core process available in the PRD
- All interfaces, states, boundary conditions as defined in SPEC are met
- It's through.
- No, no, no.
- Physical validation of key pages or processes

Conditions for discontinuation:
- Stop when all standards are met.
- Suspension and description in case of product judgement, document conflict or need for extension
```

This template looks a little long, but it's actually a little less expensive.

"When will we stop?" "What will we do in the face of conflict"?

It's actually the best place to eat.

In the general conversation, Codex is usually you ask a round, it takes a step.

But it's more like you're giving it a plan and telling it how to get it, and it pushes itself forward.

Of course, there is a very realistic suggestion here:

** Don't let a /goal contract the whole huge PRD.**

If your PRD contains a user system, a payment system, back-office management, a message, a data board, it's best not to write:

```prompt
/goal completes the system according to PRD
```

This can easily be turned into a task of excessive length, and the situation behind it will become increasingly difficult to judge.

The better way is to break the PRD into multiple pieces.

```prompt
/goal completes the login registration module by PRD and SPEC and then authenticates the relevant tests and pages.
```

```prompt
/goal completes the order creation process by PRD and SPEC and does not process the payment call back.
```

```prompt
/goal completes the payback and order flow by PRD and SPEC to ensure that the tests pass.
```

So that each goal has a clear border, and it's easy for you to be ready, pause, resume, clear.

Finally, I'll give you my own judgment:

If a mission can be completed in one sentence and can be completed in 10 minutes, then there is no need to open /goal.

If a task requires repeated reading of documents, changing codes, running tests, looking at pages, repairing failure items, it is very appropriate /goal.

If this task had PRD and spec, it would be more appropriate.

Because that's when /goal isn't helping you to guess what you need, it's helping you to implement what's already defined.

This is where it really works.
