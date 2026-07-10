# A GitHub Project That Keeps AI Coding Agents Working on a Schedule: loop-engineering

[English](./loop-engineering-turns-ai-coding-agents-into-recurring-workers.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E4%BB%8A%E5%A4%A9%20Github%20%E7%9C%8B%E5%88%B0%E4%B8%80%E4%B8%AA%E8%AE%A9%20AI%20%E7%BC%96%E7%A0%81%20Agent%20%E6%8C%81%E7%BB%AD%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%9Aloop-engineering.md)

> English edition based on the Chinese original.

> Date: 2026-07-08

I came across a GitHub project recently and spent a few days thinking about it. The idea is genuinely useful.

It does not teach prompt writing or model tuning.

It does something else: **it helps AI coding Agents work continuously and reliably, much like scheduled jobs.**

![GitHub project preview](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-01-github.png)

The project is called **loop-engineering**. At the time of writing it had 6,415 stars, used the MIT license, and listed JavaScript as its primary language.

---

## What Is It?

In one sentence: **a set of operating practices and tools for keeping AI coding Agents running over time.**

It is not a new model, a chat interface, or an IDE plugin.

It is a set of operating rules plus several npm commands.

It supports **Grok, Claude Code, Codex, and OpenCode**, with integration examples for Cursor, Windsurf, and OpenClaw.

![Loop Engineering logo](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-02-loop-engineering.svg)

Here, a loop means a persistent workflow:

> **Find a task on a schedule -> let an Agent handle it -> verify the result -> continue, commit, or ask a person for help**

Think of it as giving an Agent an alarm clock. It wakes up, does the work, checks the result, and then either delivers it or tries again.

---

## What Problem Does It Solve?

Most people use coding Agents like this:

> Find a problem -> type a prompt -> wait -> discover the result is wrong -> type another prompt -> wait again

That is fine for occasional work.

The problem is that some jobs happen every day:

- Check whether CI is failing.
- Organize new issues.
- Follow the status of pull requests.
- Update the changelog.

Doing this manually is tedious. Asking an Agent to do it raises a different problem: how do you make the Agent show up on schedule?

**loop-engineering turns repeated repository work into a pipeline.**

> Scheduled trigger -> task filtering -> state loading -> isolated worktree -> Agent execution -> verification -> human confirmation

![A complete loop](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-07-loop-engineering-5.svg)

The goal is not to let the Agent run forever. The important part is defining the rules in advance: when it can continue, when it must stop, and how many failures are allowed before a person has to step in.

---

## Three Parts That Stood Out

### 1. The Loop Is Split Into Five Components

The project breaks the workflow into a clear set of parts:

- **Scheduler**: when the loop runs.
- **Worktree**: where changes stay isolated from the main branch.
- **Skills**: what the Agent knows how to do.
- **Plugins and connectors**: which external systems it can reach.
- **Sub-agents**: who executes and who reviews.

A layer of **persistent state** sits around those components, recording what happened last time and where the work is currently blocked.

That decomposition makes the project feel engineered rather than improvised.

![Five foundation pieces and persistent state](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-06-loop-engineering-4.jpg)

### 2. Seven Ready-to-Use Patterns

The repository includes seven patterns:

| Pattern | Purpose | Suggested cadence |
| :--- | :--- | :--- |
| Daily Triage | Daily repository review | Daily |
| PR Babysitter | Pull request follow-up | As needed |
| CI Sweeper | CI failure investigation | On each CI run |
| Dependency Sweeper | Dependency updates | Periodically |
| Changelog Drafter | Changelog drafts | On each release |
| Post-Merge Cleanup | Cleanup after merging | After each merge |
| Issue Triage | Issue classification | Daily |

Each pattern includes a suggested cadence, risk level, and guidance about how much autonomy to allow during the first stage.

![Seven loop patterns](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-08-loop-engineering-6.svg)

### 3. Three Practical Commands

```bash
npx @cobusgreyling/loop-init . --pattern daily-triage --tool codex
```

This creates the starter files.

```bash
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1 --cadence 1d
```

This estimates what one run per day will cost.

```bash
npx @cobusgreyling/loop-audit . --suggest
```

This checks whether the budget, state, constraints, and verification rules have been filled in.

These commands convinced me that the project has thought about deployment, not only the concept.

---

## The Part I Appreciate Most: It Does Not Oversell Full Automation

Many AI projects begin by promising that an Agent will do everything automatically.

**loop-engineering does not make that promise.**

Its official quickstart says:

> **During the first week, generate reports only. Do not apply fixes automatically, and do not merge anything automatically.**

Once the output is stable, a team can move from L1 reporting to L2 assisted changes and eventually L3 unattended execution.

That pacing reads like advice from someone who has operated real systems.

![Loop Engineering overview](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-03-loop-engineering-1.jpeg)

---

## A Few Things to Watch

The repository is direct about its limitations:

- Sub-agents **multiply token usage**, so costs rise faster.
- **Verification remains a human responsibility**. An Agent should not be trusted to validate itself.
- The longer a loop runs, the easier it becomes for a team to **lose track of code the Agent changed**.

That last point is especially real.

---

## How to Try It Quickly

The easiest starting point is **Daily Triage**. It checks a repository, identifies important work, and writes a report without modifying code.

Run these three commands in a test repository:

```bash
npx @cobusgreyling/loop-init . --pattern daily-triage --tool codex
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1 --cadence 1d
npx @cobusgreyling/loop-audit . --suggest
```

Then read the reports for a week. Confirm that the tasks it identifies are genuinely useful before allowing it to change anything.

![loop-init and loop-audit demo](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-04-loop-engineering-2.gif)

---

## Who Is It For?

**A good fit:** teams already using Claude Code, Codex, or another coding Agent and losing time to repetitive repository work. CI investigation, dependency updates, issue classification, and PR follow-up all have clear inputs and outputs, which makes them suitable first loops.

**Probably too much:** people who only ask AI to edit an occasional code snippet. The structure is heavy for that use case.

---

## Three Things to Control Before You Start

1. Which external systems the Agent can access.
2. How much budget each run can spend.
3. Who performs the final verification.

Try third-party npm packages in a test repository first. **Do not grant automatic merge or production permissions on day one.**

![loop-engineering project card](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-10-image.png)

---

## My Take

I used to think the phrase "let AI work automatically" was mostly vague marketing.

loop-engineering changed my mind because it turns the idea into files that can be inspected, edited, and rolled back.

`STATE.md` records current state. `LOOP.md` defines operating rules. `loop-budget.md` limits spending. `loop-run-log.md` records each execution. When something goes wrong, you can at least inspect what the loop read, what it did, and why it continued.

The project does not ask you to trust the Agent.

It helps you **see what the Agent is doing**.

That is the right direction.

Project: [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)

That is all for today. See you next time.

![Project star growth](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-09-loop-engineering-7.svg)
