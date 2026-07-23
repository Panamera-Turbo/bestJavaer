# Still Learning Loops? Graph Engineering Is Already Taking Off

[English](./graph-engineering-is-already-taking-off.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Loop%20%E8%BF%98%E6%B2%A1%E7%8E%A9%E6%98%8E%E7%99%BD%EF%BC%8CGraph%20Engineering%20%E5%8F%88%E7%81%AB%E4%BA%86%EF%BC%9A%E8%AF%B4%E7%99%BD%E4%BA%86%EF%BC%8C%E5%B0%B1%E6%98%AF%E7%BB%99%20Agent%20%E7%BB%84%E4%B8%AA%E5%9B%A2%E9%98%9F.md)

> Date: 2026-07-21

On July 18, OpenClaw author Peter Steinberger asked on X: Are you still talking about Loop, or have you already turned to Graph?

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260721111956932.png" alt="Peter Steinberger discusses Loops and Graphs" style="zoom:50%;" />

Two days later, Codez wrote a long tutorial, giving a 14-step route to learn Graph Engineering from scratch.

I believe many people have the same reaction as me:**Loop hasn’t been fully understood yet, so why are you starting to draw again?**
Let me first add a word about what Loop is: Loop is a mechanism that allows a single Agent to repeatedly check and correct itself until the results meet the standards - write it once, check it again, and if it doesn't work, start over again until it meets the standards. It will be used repeatedly as a comparison below.

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/3d27d2bbec467a42adea8cd541ece2f618334556.jpg" alt="Graph Engineering 14-Step Roadmap" style="zoom:50%;" />

*Picture source: [Codez original text](https://x.com/0xCodez/status/2079165300625330317)*

Therefore, I will not talk about the 14 nouns one by one in this article - Node, Edge, Schema, Router, Fan-out/Fan-in that appear in the 14 steps will be covered in vernacular later. Let me put it in a way that ordinary people can understand:

**Graph Engineering is to divide the work among a group of Agents and stipulate how the work is handed over, where to check, and when to stop.**
Remember this sentence first, and the pictures that follow will not be so scary.

## First think of the Agent as a new employee

Let’s say you hire a new employee and ask them to write you an AI newsletter every day.

The simplest way is to leave everything to him: find the news, read the original text, check the authenticity, highlight the key points, write the article, and correct typos.

This is the single Agent that everyone is familiar with.

Prompt is equivalent to the job requirement you gave him. Loop is equivalent to him writing the check, finding something wrong, and then redoing it until it passes the test.

Simple tasks are fine, but when there are too many things to do, the employee becomes overwhelmed. He needs to read the information while memorizing numbers, and also consider the structure of the article. The context he can remember is becoming more and more full, and he forgets what he has read earlier faster and faster.

Graph Engineering did something that everyone seems to know how to optimize:**Don’t let one person do so many things, form a team.**
Some people look for information, some people check facts, some people write manuscripts, and some people are responsible for pointing out errors. The division of labor was clear, and a final draft was finally implemented.

![The relationship between Graph, Agent and Graph Reasoning](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/8a82f52a5dd286c95e78afbf67cbf0f4beab8ba8.jpg)

By the way, let me clarify a confusing word: Graph Reasoning appearing in the picture is not the same thing as Graph Engineering discussed in this article. Graph Reasoning favors the reasoning structure within the model, while Graph Engineering favors multi-agent orchestration at the engineering level. This article is about the latter.

This picture looks complicated. In fact, most of the small dots and small boxes below can be understood as different employees and different jobs.

## Node is the employee, Edge is the handover order

The two most important words in Graph are Node and Edge.

Node, that is, node. You can think of it as one position: document writer, translator, fact checker, author, reviewer.

Edge, that is, edge. It indicates from whose hand the work is handed over, and what is handed over.

![The node is responsible for the work, and the edge only transmits the data of real dependencies.](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a6eec3093e796d8f059b87e4ec71fa85d64937d1.png)

There is a particularly easy pitfall here: there is a sequence of doing things, but it does not mean that they are dependent.

For example, I ask Agent to summarize this document and then check the weather in Beijing. The weather query does not need to wait for the summary to be completed before execution, but the two tasks can be started at the same time.

This is where many Agents are slow. All tasks are written as A → B → C → D. The previous task cannot be completed and the following task will never be started.

![After cutting off the false dependencies, the linear chain becomes a parallel graph.](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/f90dee9452cfa1118adf957a767b515fca2e713a.png)

To give a more intuitive example: Both B and C only need the information provided by A, and C does not need the results of B. Then after A is completed, B and C can be started at the same time. There is no need for C to wait behind B.

Therefore, the most basic ability of Graph Engineering is to see clearly the real dependencies between tasks:**Which tasks need to wait and which tasks can be started at the same time.**
---

After tasks can be parallelized, the problem changes from who to wait for whom to how to deliver the results to the next Agent.

For example, after the data clerk Agent checked the data, he only handed back a large paragraph of text. The agent responsible for writing could neither find the link to the original text, nor could he tell which were facts and which were conclusions, so he could only guess again.

The solution is to provide a fixed format for each handover. For example, the data clerk must return three items: title, original text link, and importance. If one item is missing, the handover will be unqualified; only after everything is complete, the writing agent can continue working.

Technically, this formatting rule is called `Schema`. You can think of it as a unified handover order.

![Node contracts connect Providers, Consumers, Schemas and tests](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/86d287ae73aaa5fb075020884ff9f13b0d2dc514.jpg)

Now it’s easy to understand when we look at Node and Edge: Node stipulates what the Agent is responsible for, and Edge stipulates which data it wants to hand over to whom. The clearer the handoff format, the easier it will be for the next Agent to understand.

![Data dependencies and execution relationships in complex task graphs](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/2bd1e378505609963837e40d568b80c650afb2d2.png)

Therefore, the real difficulty of multi-Agent is to clearly write down the deliverables of each step in advance, how to check them, and what to do if errors occur.

If these rules are not set well, the greater the number of Agents, the more rework will be caused.

## The most commonly used picture is actually a rhombus

The most common Graph shapes are not complex.

First split the task and let several people do it at the same time; after completing the task, take back the results, remove duplicates and filter them; and finally hand them over to one person to unify the results.

![Subagents and Agent Teams in parallel](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/7b0fa1e3c97561416e2a402fff6252e642e6f77c.jpg)

Take writing this article as an example.

One Agent reads the original text of All three sides can start at the same time.

After the data comes back, duplicate content will be removed first, and then it will be handed over to the final drafter and reviewer (that is, me). So I don't have to work with a dozen web pages on my back, I just need to get the organized results.

![The results of multiple paths converge at the barrier node](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a3655de836c7163522d45979d99edd90f54dff02.jpg)

This is Fan-out and Fan-in.

Fan-out means handing out work, and fan-in means taking back the results. The two actions are connected together to form the diamond shape below.

![The most commonly used diamond topology in Graph Engineering](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/4442b333b5e3a584d42a02f0b04e2d92d710bafe.png)

It's easy to understand when it comes to writing an article: first let several agents check the information at the same time, then let the program automatically remove duplicates and classify, and finally hand over the sorted materials to an agent, which will form the final conclusion.

---

The previous agents have finished searching for information at the same time, and the program has also completed deduplication and classification. However, these materials cannot be used directly to write articles, because they may quote outdated information, or they may regard other people's paraphrases as official conclusions.

Therefore, after the last Agent gets the materials, he needs to make a round of acceptance judgment first: whether the link can be opened, whether the numbers and dates can match, whether there are conflicts between different sources, and then he can start writing.

Technically, the fault-finding role is called `Reviewer` or `Verifier`. Its job is not to write another answer, but to check whether the previous answer can be trusted.

But "checking" is not a fixed action, and the intensity depends on the severity of the matter.

From a common point of view, it is enough for one Agent to quickly check; when it comes to important data, security issues or product conclusions, it is necessary to arrange for several Agents to cross-check from different angles. The role that decides "which inspection process this matter should go through" is called `Router`. It is like a triage table, directing tasks to different sides according to their importance.

![Routing nodes select different edges based on risk levels](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/48776aaaf80ca399917b38999a78631963fba116.png)

If the agent responsible for checking the information says that it has been officially confirmed, the verification agent must find the official original text; if it can only find media reports, the conclusion will be downgraded or even returned to re-check. Only content that can withstand inspection will be included in the article.

![Multiple validators checking the same finding from different angles](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/434577f632d762b0dd1db2b8701a4cee06295fb5.png)

If the Agent is not querying data, but modifying the code, one more step of isolation is required: giving each Agent an independent workspace. Otherwise, if two people modify the same file at the same time, the person who saves it later may directly overwrite the previous person's results.

![Use Git worktree to isolate multiple parallel writing nodes](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/60d9fd2c93126b48e0775f9f7482341d1c7c1875.png)

If a problem is found during the inspection, you need to return to the previous stage of Agent replenishing data and then check again. This creates a cycle.

![Loops must have feedback, validation and stopping conditions](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a77a58dd40d7b13a90d8298db1d6e352aea317bd.png)

But the loop must specify when it will end. For example, if no new problems are found in two consecutive rounds, it will stop. Otherwise, it will be like the boss keeps shouting to check again, the Agent will keep working, and the token will keep burning.

To put it bluntly, the whole process is:**Some people look for information, some people organize the information, and there are still people who specifically check the information. If the inspection fails, it will be returned and redone, and the final conclusion will be made only after it passes.**
---

I have been talking about assigning tasks to multiple Agents, but one thing cannot be ignored: every time an Agent is started, it must read materials, think and output answers separately, and these operations will consume tokens.

For example, in order to write an article, calling the ten strongest models to check the data at the same time may indeed be more comprehensive than one model, but it is also equivalent to hiring ten experts at ten times the price. Parallelism saves waiting time, but it doesn't let those ten people work for free.

The way to save money is not to give all the work to the most expensive model. Extracting titles, organizing formats, and simple classification can be completed by cheap models; judging the authenticity of messages, handling conflicts, and forming final conclusions are then handed over to more capable models.

It's like an editorial department: the editor-in-chief doesn't have to go in person to sort out the information. You can call him when you really need to make a decision.

![Select different models for different nodes in Claude Code](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/82e60695a9a9ecec281a5da1ff9ea87ee008e00f.jpg)

In addition to the model chosen, how the tasks are arranged will also affect the speed.

For example, if you want to put ten pieces of information together to eliminate duplicates, you must wait until all ten Agents come back before starting. Just like a meeting, you can only move to the next step when everyone is present.

But if each piece of information can be processed individually, there is no need to wait for everyone. When the first copy comes back, check the first copy first, and then process the second copy when the second copy comes back, like an assembly line.

![Latency difference between parallel barrier and pipeline pipeline](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/e86b0f2b8908c35bd265cadc64eace783febc602.png)

Therefore, designing an Agent Graph essentially requires three calculations: how many Agents to start, what model each Agent uses, and which steps must wait for each other.

**If Graph is well designed, it can complete tasks faster with less money; if it is not designed well, it just allows more models to burn tokens faster.**
---

At this point, you may have discovered a problem: Graph does allow multiple Agents to work together, but the graph itself still needs to be designed by someone.

Who checks the information, who is responsible for verification, which tasks can be started at the same time, which steps must wait, and who makes the final conclusion - in the past, these rules usually had to be written by developers in advance.

What Claude Code's Dynamic Workflows wants to do is to hand over this part of the work to Claude.

About [Claude Dynamic Workflows](https://mp.weixin.qq.com/s/0tbHJ3uH-WXZHlTuZcEX_A) , you can read this article.

You just need to tell it the end goal. Claude will first analyze the task and then generate a JavaScript orchestration script.

Taking article writing as an example, it can arrange for several Agents to separately search for original texts, official documents, and external discussions; when the information comes back, let the program remove duplicates; then call the Verification Agent to check the source, and finally hand it over to the Writing Agent to output the article.

![Claude Code dynamically generates Workflow through ultracode](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/293e57b52461b68cb2f98f551fcb7497defc3930.jpg)

In Claude Code, you can directly ask it to use Workflow, or you can run `/deep-research`. After opening `ultracode`, Claude will also first determine whether the current task is complex enough and whether it is really worth starting a group of Agents.

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/c93c91ae5db5ad14fe2373fbd22d8c52aa77231d.png" alt="Claude Dynamic Workflows run interface" style="zoom:50%;" />

*Picture source: [Anthropic Dynamic Workflows official introduction](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)*

Here is a statement that is easily misunderstood: orchestration scripts can achieve zero-model tokens.

What it really means is that the management actions of dispatching tasks, waiting for results, and merging data are completed by ordinary JavaScript without the need to call the model again. But each Agent that actually goes out to work will still consume tokens normally.

To put it bluntly, just because employees on the shift schedule don’t get paid, it doesn’t mean that employees on the schedule don’t get paid either.**
As of July 2026, the upper limit given by Claude's official documentation is to run 16 Agents at the same time, and a single Workflow can start up to 1,000 Agents (see [Claude Code Docs](https://code.claude.com/docs/en/workflows)). This represents how many tasks the system can carry, but it does not mean that ordinary tasks should also be full of people.

The picture below is a complete set of processes finally assembled from the original article.

![A complete Agent Graph: expansion, merging, verification and synthesis](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/fd57f0339b3364eceebcf8fe5242dbef00753ce8.png)

It seems dense at first glance, but after taking it apart, it is still the same as mentioned before: first determine the scope of the task, and then check the information separately; use a fixed format to hand over, and organize it with a program; arrange Agent verification, and finally form a conclusion; the entire process also needs to control the stopping conditions and costs.

Claude can now automatically generate this set of processes, but there are still three questions to check: whether the tasks are split reasonably, whether there are verifications where verification is required, and whether it is worthwhile to start so many Agents. In other words, we don’t necessarily have to draw every node by hand, but we still have to judge whether the division of labor arranged by Claude can actually complete the task.

---

Seeing this, Xiaobai does not need to install a Graph framework immediately, let alone arrange a dozen Agents for each task.

If you just summarize a PDF, modify a title, and leave it to an Agent to do it from beginning to end, it is usually faster and cheaper. Cutting it into one picture in order to appear advanced will only increase the chances of waiting, handovers and errors.

Graph is really useful when a task starts to have the following situations: several pieces of work can be performed simultaneously; an Agent can no longer see it; the results must be independently checked; and the entire process is repeated many times.

If you really want to do it, you can start with the simplest step. First let an Agent complete the entire task and find the slowest or most error-prone link; then split out a branch that can be parallelized; if you are really worried that the answer is unreliable, add a verification Agent. After the process is stable, the framework and automatic orchestration will be considered last.

In the final analysis,**Loop solves how an Agent works repeatedly until the thing is done; Graph solves how multiple Agents divide work, hand over, and check, and how to avoid burning tokens in vain.**
Graph is not the focus. Why each arrow in the Graph exists is the real problem that Graph Engineering wants to solve.

---

### References

- [Codez: Graph Engineering with Claude, 14 steps original text](https://x.com/0xCodez/status/2079165300625330317)

- [Anthropic：Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

- [Claude Code Docs：Dynamic Workflows](https://code.claude.com/docs/en/workflows)

- [LangGraph official document: Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api)
