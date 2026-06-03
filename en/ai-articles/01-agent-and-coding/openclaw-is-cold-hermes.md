# OpenClaw is cold, Hermes.

[English](./openclaw-is-cold-hermes.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/OpenClaw%20%E5%87%89%E4%BA%86%EF%BC%8CHermes%20%E5%B7%B2%E8%87%B3.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-09

It's written in front

Do you remember the glory of OpenClaw in February and March?

At the time, there was almost one tech world, GitHub Star, all over the world, the media, the press, the media, the screen. Everyone's saying, "The age of Open Source AI Age, OpenClaw is the pole."

And then...

After March 31, the number of times I used OpenClaw on the TG was almost zero.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409050232135.png" alt="image-20260409050232135" style="zoom: 50%;" />

It's not how I feel alone. The wind direction on Twitter, the heat of community discussion, the number of issues in GitHub - are all indicative of the same thing: OpenClaw's growth curve, starting with flat.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409085112401.png" alt="image-20260409085112401" style="zoom: 50%;" />

This article is about three things: **OpenClaw, why not, Hermes Agen, and how this new battle with AI Agen will go.**

Let's not talk nonsense. Let's throw the link out.

https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/

---

# OpenClaw why fell from the altar?

First of all, OpenClaw is not a piece of crap, it's essentially a good framework for controlling plane priorities.

It connects directly to the operating system - reading and writing files, controlling browsers, operating Shell. You can access a variety of LLMs, or you can work with Ollama, and you can't get to your machine from scratch. The Skill plugin system is manually developed using a document-driven identity system Soul.md. The design was very friendly to programmers, and everything was documented in such a way as to allow for visualization of the trials and audits.

Then why isn't it working?

** The issue of stability was introduced in an iterative version. ** This is the reason I have heard the most in communities and communities. A number of major versions around March have undergone a number of functional changes, but new bugs have been brought in. When the number of users is high, the edges are exposed, and there's more and more assue piles, and the speed of response is not keeping pace.

** The snowball of the technical debt is rolling. ** OpenClaw's architecture is designed to pursue everything for adults - controlling document systems, managing browsers, supporting the Skyll plugin system, and ensuring safe sandboxes - these goals are themselves tensioned. In the absence of sufficient resources to maintain it, it is normal to ignore each other.

** Deeper reason: OpenClaw is designed to be "people must be in the decision-making ring". ** This was the advantage in the early days, the point of sale. However, when the number of users is high, most ordinary users do not want to stop to confirm it before every step of the operation. What they want is to say that it's done. OpenClaw can't give this.

** Finally, the impact of the competition. ** Hermes Agent, a new player like this, plays a different card with open boxes and intellectual evolution, diverting part of OpenClaw ' s target users.

---

# Hermes Agent #

Hermes Agent is an open-source, self-hosted, permanent AI Agent.

It is the same as OpenClaw: open source, self-hosting, ability to access chat software such as Telegram / Discord / Slack / WhatsApp to perform actual tasks, data and so on. But the design philosophy of both is different at root.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409050524628.png" alt="image-20260409050524628" style="zoom: 50%;" />

** The core logic of OpenClaw is: Agent = you give tools + you give Skill + you keep an eye on the whole thing.**

**Hermes' core logic is: Agent = you give the target + it learns by itself + you understand more than yourself for a long time.**

That difference sounds a little poignant, for example.

You run a mission with OpenClaw: you're gonna tell it what Skill, where to put the files, how Shell runs. Next time you do the same kind of job, you'll have to say that again. It's a tool. It works well, but it doesn't have long memory.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409085248718.png" alt="image-20260409085248718" style="zoom: 50%;" />

You run the same mission with Hermes: you just say the target, it decides its own way. Upon completion of the mission, it will ** refine this successful implementation path into a Skill** repository. Next time you do the same thing, you don't have to say it's called. And if you do it better with a new method, it'll automatically update that Skill -- old as new, new.

This is Hermes' core selling point: ** Learning from experience, evolving in use.**

---

# The core structure is dismantled

We're not talking about it this time. We're going to take Hermes' structure down several layers by the official web file. You'll find it's not actually a "chatting command line tool" but a set of models, tools, memories, skills, automation and secure borders.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409085456767.png" alt="image-20260409085456767" style="zoom: 50%;" />

First floor: running time entrance level

From official QuickStart and Features Overview, Hermes is actually a unified entrance level.

This entrance level is not just a set of CLI commands, but it covers at least three types of interfaces:

- CLI Session: Run straight`hermes`Enter interactive terminal to support multi-line input, job interruption,`hermes --continue`Restore Recent Session
- Message Platform portal: Through`hermes gateway setup`Take Telegram, Discord, Slack, WhatsApp, expose the same Agent to different sources.
- Auto-entry: Create timed tasks directly in natural languages to allow Hermes to perform in the backstage cycle via gateway or cron

That is to say, Hermes is not "do a command line first, and then add Bot," but treats CLI, messaging platform and automation as different entry points to the same set of runtimes from the very beginning. This is critical because it determines the status, memory, skills and control of Hermes to be reused across access.

#2nd Layer: Models and Tools Implementation Level

The choice of suppliers given by the official Quickstart has actually exposed its bottom structure. Hermes divided Model Call and Tool Call into two things:

- Model side support Nous Portal, OpenAI Codex, OpenRouter, and any OpenAI compatible end Points
- On the side of implementation is a tool system, which is clearly listed in the website Websearch, technical evaluation, file edification, Browner empowerment, memory, delegation.

This means that Hermes' kernel does not bind a model, but rather uses it as a "brain of reasoning" and tools as a "motive organ."

You can understand this layer:

1. Models are responsible for understanding objectives, planning steps and judging whether tools are to be used
2. Tools for real search of web pages, modification of files, running terminals, browsers
The result is re-routed to the model for the next round of reasoning.

And that's why it can pick up OpenAI Codex while emphasizing its own implementation capabilities. Hermes does not focus on "a much chat model", but on "a complete closed ring between models and tools".

Third floor: context assembly layer

It's a layer that many would ignore, but it's like a "control hub".

The official network Features Overview mentions Hermes automatically discovers and loads context files in projects such as`.hermes.md`, `AGENTS.md`, `CLAUDE.md`, `SOUL.md`, `. cursorrules`I don't know. It also supports it.`@`Quote files, folders, Git diff and URLs to feed these content dynamics into the current message.

This suggests that Hermes, before formal reasoning, does a round of context assembly:

- System-level configuration and project rules first.
- Eat files and changes from the user ' s current explicit reference
- and spell memory, skill, external context.
- and finally hand over the whole context to the model.

This step is very much like a "prompt assembly pipeline", rather than simply throwing a user sentence to a model.

And because of this layer, Hermes is able to do both programming assistants and automated assistants and chats. Many of the differences between different missions are based not on changing models but on changing context assembly results.

Level four: lasting memory

This is the difference between Harmes and OpenClaw's biggest point.

This section of the official network is the most clear and worthy of elaboration.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409085611925.png" alt="image-20260409085611925" style="zoom: 50%;" />

Hermes ' built-in memory is not a vague concept, but a set of two fixed documents and a historical search mechanism:

- `MEMORY.md`Agent's environmental memory, project structure, tool pits, workflow experience, proven methodology
- `USER.md`User image, preferences, modes of communication, habits, mined areas, technical level

Both files are defaulted.`~/.hermes/memories/`, and not a real-time RAM, but ** injected as system programt** as frozen snapshot at the beginning of the session. It's important because it means Hermes' use of lasting memory is controlled, stable, and it doesn't mess up the prompt infrastructure while deduced.

The network also provided a clear capacity design:

- `MEMORY.md`Default 2200 characters, about 800 tokens
- `USER.md`Default 1375 character, approximately 500 tokens

What do you want to do with it? It's not unlimited additions, it's for Agent himself to consider or replace old entries. In other words, Hermes, the official understanding of memory is not as good as it is, but rather to compress it into a small piece that really matters.

In addition to this, there is a second line: a historical session search.

Officially, Hermes will save all sessions in SQLite`state. db`, and make full-text search with FTS5. The real need is "Did we discuss the database index strategy last week?" When it comes to this kind of problem, it goes`session_search`This path allows the model to summarize instead of putting all the old conversations ahead of schedule.

So Hermes' memory is actually two-track:

- Permanent memory: small and stable, always in context
- Historical retrieval: large and demand-driven, only when required

This layer has a heavy engineering taste and looks like a real permanent Agent system.

Level 5: External memory

If you think Hermes only has two markdown files, you underestimate it.

The website Memory Providers is very clear: built inside.`MEMORY.md` / `USER.md`It's gonna be open, and it's gonna hang an external memory program. There are eight providers in the current document. Honcho is just one of them.

When external provider is enabled, Hermes does six things automatically:

1. Insert context known to provider
2. Pre-enforcing relevant memory prior to each round of dialogue
Synchronize dialogue to processer after each response
4. Long-term memory extraction at end of session
5. Write built-in memory to mirror to projecter
6. An exclusive tool for Agent exposure

The point of this layer is that Hermes didn't write down the memory structure, but instead made it a plug-in interface.

In particular, Honcho, the official location of the site is "boilt-in memory" for deep user modelling. What it can do is:

- Summarize user habits and targets after the meeting by dialectic reporting
- Make cross-sessions, cross-platforms and even more user portraits of Agent
- Use`honcho_search`, `honcho_context`, `honcho_profile`, `honcho_conclude`Tools for semantic memory retrieval and conclusion management

This means that Hermes' long-term direction is not to "grow up local memory," but to "severe internal memory and external deep memory." This structure is more mature than many integrated Agent programs.

## Sixth floor: skills and procedural memory

If the lasting memory is "who you are, what the environment is and what matters", then the skill layer is "what the hell is going on".

The online definition of Skills is straightforward: it's a load-on-demand knowledge document, follows progressive disclosure, all defaults`~/.hermes/skills/`Down. The key here is not "skill is markdown", but Hermes has identified skills as **special memory**.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409085819605.png" alt="image-20260409085819605" style="zoom: 50%;" />

The official document is very clear:

- After a complicated mission, Agent can create Skill.
- Find the right path after the error. Save it as Skyll.
- Users have corrected and can update Skill.
Agent could even delete the old Skill.

In other words, the skill level is the formal modelling of Hermes for the deposition of experience.

The memory answers:

- Who's the user?
- What's the project?
- What'd you talk about in the past?

Skill answers:

- What do you do with these kinds of missions?
- Which process passed before?
- Which pits have been stepped on?

This is a beautiful layer. Because it's too heavy if you save "user likes simple answers" into "skill," and vice versa, if you shove "how to deploy Kubernetes" into "MEMORY.md." Hermes Officially dissects these two types of things, in effect, by distinguishing between ** factual memory** and ** procedural memory**.

7th floor: Automation and parallel implementation

Hermes, another layer that is often overlooked is the automated layer.

These capabilities are clearly listed in the web site Features Overview:

- Scheduled Tasks: Create a timed task by natural language or cron expression
- Subagent Delegation: Use`delegate_task`Agent, block the context and limit the tool Set
- Code Exchange: Allow Agent to write Python scripts and complete multi-step tool call by sandboxing RPC
- Batch Processing: lot of mass running

This means Hermes is not content with "one-round questions and answers." It has further developed Agent into a dispatch system:

- Timed to run.
- You can take the kids and run in parallel.
- You can use multiple-wheel tools to fold them into programs.
- It can be batched.

This layer is the key to moving Hermes from "interactive assistants" to "operational mission systems".

## Eighth floor: security and isolation

The last level is the secure border, and the security page makes this very clear: Hermes uses defense-in-depth, not single-point protection.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260409085849194.png" alt="image-20260409085849194" style="zoom: 50%;" />

It divides security into five layers:

1. User authorization
2. Approval of hazard orders
3. Container segregation
MCP voucher filter
Context document scanning

Spread out, each floor is not decorated:

- Who's authorized by the user to talk to Agent, support allowlist and DM pairing
- Which operations must be identified inside the ring.
- The containment is controlled by orders to run on this plane, Docker, Singularity or long-range SSH.
- MCP Document Filter Control is external MCP subprocesses that should not see environmental variables
- The context document scan controls the injection of malicious tips in the project.

Hermes didn't give up the border because of "autonomy." On the contrary, it has exposed the most dangerous borders.

# One sentence summing up the architecture #

If it had to be in engineering language, Hermes, I would say:

**Hermes is a multi-entry Agent runtime with tools executive layer, context assembly layer, two-track memory layer, evolutionary skill layer, automated movement control layer, and deep defense security model bottom.**

So the real difference between it and OpenClaw is not just "one smarter, one more loud," but Hermes has taken the three things of "long run, long learning, long reuse" as the first principle in the official architecture.

---

# OpenClaw vs Hermes: Full-dimensional comparison

## Core design philosophy

** OpenClaw**: Control plane priority, people at the centre of the decision chain. All operations require visible authorization, file-driven identity system (SOUL.md). Rule on the definition of a person, Agent enforcement rule.

**Hermes Agen**: Learning cycle priority, Agent evolution. Optimized by using target-driven results feedback. Man defines the target, Agent finds the best path for himself.

# Skill System

** OpenClaw**: manual Skill, document-driven. Developer writes the template, Agent runs by the template. Flexible but dependent on manual maintenance.

**Hermes**: Auto-generated Skill from successful experiences, continuously optimized. Skill will evolve with its use and will not depend on manual maintenance.

# Memory

** OpenClaw**: Visible document recording, manual maintenance. There is no cross-conference learning capability.

** Hermes**: a stratification memory system, inter-conference retention of preferences and experience. The more I use, the better I understand you.

Security model

** OpenClaw**: High control, high authority. All behaviours can be audited at the documentation level, but rely on manual configuration.

**Hermes**: safe sandbox + approval check, default configuration more conservative. More friendly to lay users.

# It's hard to deploy #

** OpenClaw**: There are certain thresholds. Need to retrofit the configuration to understand the SOUL.md mechanism.

**Hermes**: Lighter, case opening, built-in practical functions such as cron.

# The people that apply #

| | OpenClaw | Hermes Agent |
|--|---------|-------------|
|Target users|Hard core developers, privacy sensitive scenes|Teams, individual users who want to save things.|
|Technical background|It takes a lot of power.|It's kind of technical and white.|
|Maintenance costs|Skill, manual, long-term maintenance costs. High|Automatic evolution, low maintenance cost|
|Transparency|High. All operational files are visible.|Center, Skyll generation is black box|
|Flexibility|Very high, SOUL.md fully customized|, relying on built-in evolutionary mechanisms|

---

The limits of Hermes

Hermes has problems with it, can't blow blindly.

**Skill evolved the black box problem. ** It's an automatic mechanism for Skill generation and optimization, which means it's hard to fully understand why this Skill wrote it. When Hermes generated a Skill you didn't approve, you didn't have the ability to change files like OpenClaw.

** Growing up takes time. ** Hermes will understand you better after a long time, but this`long time`It really takes a while to accumulate. If you use it once or several times, Hermes' ability to learn doesn't work.

** There are still limitations to highly privacy-sensitive scenes. ** While Hermes supports local deployment, its Skyll auto-generated mechanism involves the writing of implementation path data into the skill pool - That means your usage itself will be structured and stored. This storage itself needs to be protected for extremely conservative security requirements.

---

How?

In the end, the difference between the two is the difference between ** "human rule" and "autonomy".**

OpenClaw selection:
- You need full visibility and control over Agent every step of the operation.
- Special security compliance requirements requiring audit of all acts at the document level
- Trying to customize Agent's ability to develop its own Skill system
- Your scenes need to work with systems, browser depths. - Yeah.
- You have time and energy.

Choose Hermes Argentina:
- You want Agent to get to know your way of work as he uses it.
- I don't want to do this. I want to do it fast.
- Need to automate a time line. The built-in Cron Scheduler is practical.
- You need a safer default configuration to reduce manual clearance.
- It's a small team.

** Practical proposal: may be used in combination.**

Using OpenClaw as the primary control layer, it is suitable for high-risk tasks that require precise control. Use Hermes Agent for light implementation of routine tasks that are repetitive and allow for automatic learning optimization. Experimental functions are isolated to Hermes nodes to facilitate rollback without affecting core business.

---

My opinion

OpenClaw represents a very reasonable idea:** return of control to mankind**. All its designs - SOUL.md, explicit authorization, document auditing - revolve around the same proposition: one should know what Agent is doing and should be able to intervene in every step of Agent.

That's right. This sense of control is the basis of trust, especially for users of technological origin.

Hermes represents another line of thought: ** To make Agent really useful**. It acknowledges the reality that most people do not have the time and energy to fine-tune the management of an Agent and do not want to stop and approve it every time. So it makes "self-learning" an built-in capability, automates repetitive decision-making and transforms people from "supervisors" to "supervisors."

Both approaches have markets and limitations.

The problem with OpenClaw is that it assumes that users are willing and able to intervene continuously. In fact, most people are reluctant. It's too late to open a computer with a whole bunch of things, either to turn off the security mechanism or not.

The problem with Hermes is that it's doing "automated evolution," but it's not transparent to users. Agent learned what, why, on what basis a decision is made -- these are black boxes. Users choose between full trust and non-use. The middle zone is small.

In the short term, OpenClaw will also be the mainstream in hard-core developers ' communities, especially in environments with high privacy requirements. In the long run, the Agent paradigm that can evolve will become the mainstream - – The question is whether the transparency and control of this "evolutionary" mechanism is truly universal.

Hermes has taken the first step. OpenClaw will not die, but it needs to address not just the technical debt, but the transformation of product thinking.

Technical choice has no standard answer. Let's figure out what your scene really needs and decide which one to use.

By the way, one more thing to say here is that OpenClaw is a local Chinese user.

---

# Reference source

1. [2026 AI Agent: OpenClaw vs Hermes Agent](https://cloud.tencent.com/developer/news/3700465)- A community of cloud developers.
2. [28. 4k Star! OpenClaw's latest replacement for Hermes Agent.](https://zhuanlan.zhihu.com/p/2024913544848623338)- The column.
3. [OpenClaw vs Hermes Agent: A Thorough Comparison for Your Use](https://www.youtube.com/watch?v=eJzQuC9Dy3w) - YouTube
4. [OpenClaw vs. Hermes Agent: The race to build AI assistants](https://thenewstack.io/persistent-ai-agents-compared/) - The New Stack
5. [Hermes Agent – OpenClaw's Rival? Differences and Best Use Cases](https://www.turingpost.com/p/hermes) - Turing Post
6. [Hermes Argentina: Light, Cross Platform, Custom](https://www.sohu.com/a/1004153546_122413774)- Search the fox.
7. [What Is Hermes Agent? The OpenClaw Alternative with a Built-In Brain](https://www.mindstudio.ai/blog/what-is-hermes-agent-openclaw-alternative/) - MindStudio
