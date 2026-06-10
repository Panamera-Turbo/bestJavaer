# A Harness for Every Task: Dynamic Workflows in Claude Code

[English](./a-harness-for-every-task-dynamic-workflows-in-claude-code.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E4%B8%BA%E6%AF%8F%E4%B8%AA%E4%BB%BB%E5%8A%A1%E9%85%8D%E4%B8%80%E5%A5%97%20harness%EF%BC%9AClaude%20Code%20%E9%87%8C%E7%9A%84%E5%8A%A8%E6%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-06-05


![image-20260605092343445](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092343445.png)

Hello, I'm cxuan, the one who tortured each other with AI Agent.

Let's start with my own business.

I used it before.`/goal`Hanged over a 75-hour runaway assignment. At the time, he was so proud that he thought it was the ultimate form of agent, which, by the way, he did for three days.

The result is nothing compared to the revenue of the token that it burned down and the time.

The mission ran to the second half, and it began to flaunt itself: I was bound at the beginning, running like I didn't see it.

I've always thought that my Prompt or my target set had problems.

It was only last week that Claude Code released a new Opus 4.8 model and introduced a feature called dynamic workflows, that I felt that this goal might be very suitable for using dynamic workflows.

This feature is that Claude can write his own Harness now.

The default Claude Code Harness is for code writing, but it is useful for many other types of tasks, such as Research (research), security analysis, agent teams, or Code Review.

Workflows allows you to create this natural, which allows Claude to solve these problems in-house. You can also share this workflow with others, repeat it.

I'm going to talk to you about this article and my own initial experience and thoughts.

Dynamic workworks often cost more token, so when and how to use it, you have to think about it.

---

# Example

Before I go into technical details, I'll throw you some examples prompt, make you feel a little bit about this thing.

> > > This test is about to hang up every 50 runs. Build a workflow to reproduce it, present several theories and confrontationally validate them in worktree. /goal, don't stop until a theory has been established."
>
>
>
> > "Throw through my latest 50 sessions with a workflow, dig out the corrections I've been doing over and over again, turn the HF presence into the CLUDE.md rule."
>
>
>
> > "Take my business plan, run a workflow, let different parties figure it out in terms of investors, customers, competitors."
>
>
>
> > Here is a folder containing 80 CVs, ranked them by the back end with a workflow and reviewed by the top 10. Ask me with the AskUserQuestion tool and ask for a rating.
>
>
>
> "I have to name this CLI tool. With a workstorm of candidates, run the top three in a knockout competition."
>
>
>
> "Rename the entire User model of our code as Account with a workflow."
>
>
>
> > Go through my blog draft, and use a workflow to check every technical statement inside -- I don't want to send anything wrong.

---

Do you always do this when you're using AI Agent, in a session, to have Claude Code complete the planning and implementation?

This is very effective for many of the code-writing tasks;

But it does not deal well with confrontational tasks that operate for long periods of time, that are large-scale and that require a highly structured structure.

The reason for this is that the longer Claude eats a complex task in a single context, the easier it is to fall into the following three patterns.

* ** Agency laziness** refers to Claude stopping when a particularly complex, multi-stage mission is not finished and announcing the completion of a part of the mission, such as 50 security clearances, of which 20 were disposed of.

* **Self-preferential bias (self-preference)** refers to Claude ' s preference for results or discoveries of his own output, especially when required to validate or judge against the rating criteria.

* ** Goal Drift (target drift)** refers to a slight loss of loyalty to the original objective after crossing multiple rounds of dialogue.

This is particularly evident after the context. Like border conditions, such as "do not do X", it can easily be lost in the process.

Of these three, I have the most say in the third. I started with the 75-hour goal, flipping over here, and it forgot my rules.

Creating a workflow helps to counter these problems by working together with a set of separate contact window, focused and isolated Claude.

---

# Dynamic workflow vs static workflow

You might have used Claude Agent SDK before.`claude -p`To create static workflows, this way to combine several Claude Code examples.

With Claude Opus 4.8 and dynamic workflows, Claude is now smart enough to write a tailored set of laws for your specific case.

![image-20260605092358458](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092358458.png)

---

A few good models

All you have to do is have Claude do a workflow and start using dynamic workflows or triggers.`ultracode`Make sure Claude Code builds you one.

But dynamic workworks has several operating models, and you put them in your head, and next time you can figure out when to use them, and how to direct Claude through the prompt.

Claude, in setting up the workflow, often uses and combines the following models:

![image-20260605092409727](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092409727.png)

* **Classify-and-act (Classification before Action)**: judge the type of task with a classification agent, then follow the route of the task to different agent or different behaviour. Or, at the end, use a classification entry to determine the final output.

* **Fan-out-and-syntheseize**: Dismantling a task into many smaller steps, running an agent at one point and combining the results. This is particularly useful when there are many small steps, or when each of them benefits from its own clean contact window so that they do not interfere with each other and do not cause pollution.

The consolidation of that step is a barrier that acts as a barrier, and when all agents are completed, they are structured and exported into a single result.

* **Adversarial verification**: for each fork (associated) gives rise to one or more independent agents to verify confrontationally the output of the former against a rating standard or a judgement.

* **Generate-and-filter (generation refiltration)**: Generate a set of ideas on a subject, filter them by rating criteria or through validation, remove repetitions and leave only those of the highest quality and tested.

* Tournament**: Not division of labour, but competition for the same thing. Give birth to N agent, try the same mission in different ways. The results are then judged in comparison with the prompt or model, until a winner is elected.

:: ** Loop until done**: for tasks for which there is no known workload, do not set a fixed number of rotations, but recycle ant until a certain cessation condition is met (no new discovery or no further errors are reported in the log).

None of these six. I used two things I used most often: fan-out and confrontational verification. One slow, one partial.

The rest, the right scenes will come back to mind.

---

There's one thing I agree with Tharik: ** He finds workworks useful in non-technical work, sometimes more useful. **

Here's the ways he gives the workflows.

# Move and rebuild #

Bun rewrites Rust from Zig with workflows.

The key is to break down missions into a series of steps that need to be addressed individually, such as call points, failed tests, modules, etc. For each site to be repaired in one worktree, one subagent to change, and another agent to confrontational review, and then merge them. Think about telling agent not to use the order to eat too much resources so that you can maximize the parallel without draining the machinery.

# Depth study #

Claude Code released an in-depth study skill`/deep-research`It's using dynamic workflows.

In particular, it conducts multiple-road network searches, captures sources, checks in a confrontational manner the statements of these sources, and finally synthesizes a report with quotations.

But such research can be used more than just for web searches. For example, let Claude compile a status report from the context of the Slack, or study how a certain function is achieved by looking into a code library.

# Depth verification

![image-20260605092433094](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092433094.png)

Conversely, if you have a report, every statement of fact that you want to quote is verified and traced, then you can generate a workflow.

Let a delegate find all the statements of fact, and give a subagent for each article to look into.

And you can add another validation agent to check the tracer subagent to make sure it looks hard.

Sort

![image-20260605092444968](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092444968.png)

You may have a list that you want to sort out by a qualitative indicator, and you believe Claude Code is good at judging this indicator, for example, by sorting support sheets by the size of the bug.

But if you want to line up over 1,000 lines in a prompt, the quality will fall, and it won't fit in.

A different approach: run a phase-out in the structure model above, use a two-to-two-comparison agent streaming line (relatively more reliable than absolute scores), or combine the row ranking in parallel.

Each comparison is its own agent, so the definitive cycle is responsible for maintaining the schedule, and only the current order remains in the context.

# Memories and rules

![image-20260605092456622](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092456622.png)

If there's a particular set of rules that you find Claude always missing, always failing to do, even if it's written in the CLUDE.md, then build a workflow.

Lists a rule that must be checked by acquit, a rule accompanied by a checker. Another subagent created by a "suspector" to review these rules and make sure they are reasonable, which will help you avoid too many false reports.

The opposite is true.

From your recent review of the session and code review, dig out the corrections you've been making over and over again, group them together with parallel parties, and test each candidate rule confrontationally (can this rule really stop a real mistake?) and finally extract those that survived back to CLAUDE.md.

# Root investigation #

The most effective way of debugging is to come up with a few separate hypotheses to be tested one by one.

But if you use only one contact window, Claude will be "self-biased".

A workflow can block this from the structure: multiple parties are created, each producing a hypothesis from a non-overlapping evidence.

For example, the logs, the files, the data are independent anent. Each hypothesis then faces a group of certifiers and rebuttals.

It's not just for code. Workflows can be used for sales (why did the March sales drop?), data engineering (why did this pipeline hang up?), or any reset scene.

# # size diversion

![image-20260605092514131](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092514131.png)

Each team has a support queue, a bug report or something that can't be handled by manpower.

A triage workwork will classify each entry, weighting what is already being tracked, and then take action. The operation may be an attempt to repair or may be reported for processing.

There is a good model to use: ban those who read untrustworthy public content from performing high-authority operations, which are done by those who are responsible for this information.

Match the triage workflow`/loop`And you can get Claude to do this on a continuous basis.

# Explore and taste #

It is also useful to explore different solutions to a problem, especially when the problem is taste-neutral (e.g. design or naming) and can be measured by a rating criterion.

Claude could explore a bunch of programs and give an agent a rating on what a good solution looks like.

When reviewing agent considers that the target has been met, the task is completed.

The scheme may also be sequenced or selected on the basis of this rating, in a phase-out contest.

# Evals

You can run a lightweight eval for a given task: give a couple of independent agents in a worktree, compare an agent, compare a given output against a rating.

For example, to assess against a particular case and then grind one of your skills.

# Model and smart path #

Build a classification for your mission, agent, to determine which model to use.

It'll be useful when your mission involves a lot of tol uses, and before you do it, do some research on how to help you identify the best models.

For example, the task of explaining how the auth module works depends on how many files are in the auth module, and how well the code library is.

A classification agent can do this study first, then by the expected complexity of the task to Sonnet or Opus.

---

# When don't use dynamic workflows

Workflows are new. While in many contexts it can produce extraordinary results, not every mission needs it, and it may eventually use much more token.

It's better to use creative workworks to push Claude Code where you've never been before. For a regular code-writing mission, try to ask yourself: Do you really need more thought?

For example, most traditional writing assignments do not require a five-person review mission.

---

A few techniques to build a dynamic workflow

# Prompt

With the specific techniques we're talking about, you can write the prompt in detail, dynamic workflows.

But the workflows are not just for big missions. You can suggest a "quick workflow" model. For example, a quick confrontational review of a given hypothesis.

# co-operate /goal and /loop

I'd like to talk about this, because it just solved my first pit.

The official usage is: workflow that can run again (several, research, verification)`/loop`Time out, again.`/goal`Set it a hard completion requirement.

But I'd rather talk about the relationship between /goal and workflow. But if you just drive, let a brain carry a big goal for a few hours, it'll be like me running. It's the other side of the line: tearing it down into a bunch of little parties who are staring at themselves.

These two have to work. My 75-hour rollover, that's not the problem. If you open up the work first, then goal, then goal, you've got a lot of work to do: a drain that can be independently verified at every step, instead of a brain that's been dry for three days and has lost memory. This difference, I think, is the most useful thing for me in this update.

# Token's budget

You can set a clear token budget for dynamic workflows, limit how much token a task is spent. You can use a budget to suggest it, like "use 10k tokens," and that's a ceiling.

---

# Save and share dynamic workflows

You can save workflow by pressing "s" in the workflow menu. You can check them in.`~/.claude/workflows`Or distribute them through a skill.

![image-20260605092534641](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092534641.png)

Share your JavaScript workflow file in the skill folder and`SKILL.md`It quotes them.

In order to be flexible, you might want to point out Claude: using the workflow of the skill as a template, not a script that has to run word for word.

![image-20260605092548716](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092548716.png)

---

And to take this whole thing to the bottom, my point is that the most important part of this is to turn a big blurry mission into an engineering project that you can prove. **

It fights lazy, partial, drifting, and it's actually one thing you can't verify. Once it's broken down into a bunch of isolated little parties, each with a verification link, you know at least what every step is doing, and you know which step is to be picked by another agent on the spot.

So it's not for your readers' friends. I think there are two things.

- One word, ten minutes. Don't touch it. Just an ant.
- It's a long mission, it's a lot of verification, and you're running through it.

My 75-hour goal, I wouldn't be holding my head hard for three days.



Source: Tharriq, A Harness for every task: dynamic works in Claude Code

References to articles:https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
