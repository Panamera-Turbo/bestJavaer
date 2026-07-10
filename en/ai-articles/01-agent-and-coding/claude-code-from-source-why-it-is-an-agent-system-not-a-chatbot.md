# Claude Code From Source, Part 1: Why Claude Code Is an Agent System, Not a Chatbot

[English](./claude-code-from-source-why-it-is-an-agent-system-not-a-chatbot.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Claude%20Code%20%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E7%AC%AC%E4%B8%80%E7%AF%87%EF%BC%9AClaude%20Code%20%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E6%98%AF%E4%B8%80%E4%B8%AA%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA%EF%BC%8C%E8%80%8C%E6%98%AF%E4%B8%80%E4%B8%AA%20Agent%20%E7%B3%BB%E7%BB%9F.md)

> English edition based on the Chinese original.

> Date: 2026-06-25

This article begins my close reading of `Claude Code from Source`.

The book is unusual.

It does not offer another enthusiastic introduction to Claude Code. It studies the architecture exposed through TypeScript source code that appeared in source maps from an early Claude Code npm package.

The distinction matters: this is architecture analysis, not source-code redistribution.

The site says it does not preserve Claude Code's original source. Its code blocks are pseudocode, and its focus is architecture, patterns, and engineering trade-offs.

I will follow the same rule throughout this series:

**Translate and explain each section in the original order without reproducing the source code or rebuilding the implementation.**

The first chapter is the book's map:

`The Architecture of an AI Agent`.

In other words, how is an AI Agent actually organized?

![Claude Code from Source cover](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/cover.jpg)

*Source: screenshot of the Claude Code from Source home page.*

---

## What Are We Looking At?

The chapter begins by separating a traditional CLI from an agentic CLI.

A traditional CLI is essentially a function. When you run `grep`, it does not decide to run `sed` as well.

If those names are unfamiliar, `grep` searches text.

For example, if you have a large log file and want every line containing `error`, you can run `grep "error" app.log`.

It does not understand your business, and it does not decide what should happen next.

It performs one operation: find matching text in the input.

`sed` is closer to a stream editor. It can replace every occurrence of `foo` with `bar`.

It will not suddenly decide that the log format should be refactored.

That is the contract of a traditional CLI. A tool may be powerful, but its boundary is clear.

You tell it exactly what to do, and it does that.

`curl` does not download content and then independently decide how to complete the next step.

**A traditional CLI executes one command, performs one operation, and returns a deterministic result.**

![How a traditional CLI works](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@dabed70/claude-code-from-source/ch01/ch01-00-traditional-cli.png)

*A user gives an explicit command, the program runs fixed logic, and a deterministic result comes back.*

An agentic CLI breaks that contract.

It accepts a natural-language goal, decides which tools to use, calls them in an order determined at runtime, observes the results, and repeats the process until the task finishes or the user stops it.

![How an agentic CLI works](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@dabed70/claude-code-from-source/ch01/ch01-00-agentic-cli.png)

*The central structure is a loop: decide, call a tool, observe the result, and decide again.*

That gives us a useful definition:

An agentic CLI is not a fixed list of instructions. It is a loop organized around a large language model, and the model generates the next instruction at runtime.

Claude Code is Anthropic's production implementation of that idea.

It is a TypeScript monolith that turns the terminal into a Claude-powered development environment. Millions of people now use Claude Code, which means its architectural decisions have consequences at real scale.

The first chapter extracts six mental models. Later chapters enlarge each one.

## Six Core Abstractions

According to the book, Claude Code rests on six core abstractions.

Hundreds of utility functions, terminal renderers, Vim emulation, cost tracking, and everything else ultimately serve these six parts.

![Six core abstractions in Claude Code](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-01-six-key-abstractions.png)

*Source: screenshot from the interactive diagram in chapter one.*

They are Query Loop, Tool System, Tasks, State, Memory, and Hooks.

### 1. Query Loop: The Heartbeat

The book calls `query.ts` the heartbeat of the system.

That description is accurate because Claude Code repeatedly:

- Calls the model.
- Receives a streamed response.
- Collects tool calls.
- Executes tools.
- Appends tool results to message history.
- Starts the next round.

Every entry point eventually reaches this loop.

The ordinary REPL uses it.

SDK calls use it.

Sub-agents use it.

Headless `--print` mode uses it.

The implementation detail that matters is that the loop is an async generator.

It does not run to completion and return one large result. It keeps yielding messages while the work proceeds. The UI consumes those messages with `for await`.

That has several benefits.

First, it provides natural backpressure.

If the UI cannot consume events quickly enough, the generator pauses instead of flooding the rest of the program.

Second, cancellation is cleaner.

A user interruption can let the generator finish its cleanup instead of leaving control scattered across callbacks.

Third, termination reasons are typed.

The system does not merely say that execution ended. It records whether the cause was normal completion, user cancellation, token-budget exhaustion, a stop hook, the maximum number of rounds, or an unrecoverable error.

This is a production concern.

Many Agent demos appear to work until someone asks, "Why did it stop?"

Claude Code makes the stopping reason a first-class part of the system.

### 2. Tool System: The Agent's Hands

The second abstraction is the tool system.

A tool is anything the Agent can do in the world: read a file, run a shell command, edit code, or search the web.

In Claude Code, a tool is more than a function.

Each tool describes its identity, input schema, execution logic, permission requirements, and rendering behavior.

It also declares whether it is safe to run concurrently.

Reading files can usually happen in parallel.

Writing files or running state-changing commands cannot be parallelized casually.

The tool executor divides calls into concurrent and serial batches.

Some concurrency-safe calls can begin before the model has finished generating its entire response.

That is streaming tool execution.

As soon as the model produces a `Read` call, the system can start reading the file while the model continues generating.

This is important because many Agent implementations treat tool use as post-processing after the model's answer.

Claude Code overlaps model streaming and tool execution.

That is one reason it feels like a running system rather than a question-answer script.

### 3. Tasks: Background Work and Sub-agents

Tasks are background work units, especially those that carry sub-agents.

The chapter describes a state machine:

`pending -> running -> completed | failed | killed`

The central piece is `AgentTool`.

When Claude Code creates a sub-agent, it does not branch into an entirely different implementation. It starts another `query()` generator.

That new query loop has its own message history, tool set, and permission mode.

A sub-agent is therefore not a lightweight callback.

It is a smaller Agent.

This gives Claude Code recursive delegation. One Agent can delegate to another, which can delegate again.

That power is dangerous.

Once a sub-agent can make decisions, run commands, and modify files, it can also move beyond what the user intended.

The permission system therefore includes a `bubble` mode.

A sub-agent cannot approve a dangerous action by itself. The request bubbles up to the parent Agent or the user.

My interpretation is simple:

**Capability can be delegated. Responsibility cannot.**

That is an important boundary in a multi-Agent system.

### 4. State: Two Layers

Claude Code uses two layers of state.

The first is a mutable singleton named `STATE`.

It stores session-level infrastructure such as the current working directory, model configuration, cost tracking, telemetry counters, and the session ID. The book describes roughly 80 fields.

This state is initialized at startup and then mutated directly. It is not reactive.

The second layer is a minimal reactive store that resembles Zustand.

It drives frequently changing UI state: messages, input modes, tool approvals, and progress indicators.

The split is simple and sensible.

Not every state change should trigger a UI update.

Infrastructure state changes rarely and is read often.

UI state changes constantly and must be reactive.

Putting everything in one reactive store eventually creates tangled subscriptions.

That is especially risky in an Agent CLI, where model calls, tool execution, terminal rendering, cost tracking, and user input all happen at the same time.

If hot and cold state are not separated, the architecture will eventually become unstable.

### 5. Memory: Context Across Sessions

The fifth abstraction is memory.

The chapter describes three levels:

- Project memory in `CLAUDE.md`.
- User memory in `~/.claude/MEMORY.md`.
- Team memory shared through symbolic links.

At the start of a session, Claude Code scans the memory files, parses frontmatter, and lets an LLM decide which memories are relevant to the current conversation.

This is more interesting than simply extending the context window.

Claude Code turns long-term rules into files.

Project conventions, architectural decisions, debugging history, and personal preferences do not have to remain buried in chat history. They become documents that can be opened, edited, and versioned.

That is more dependable than hoping a model remembers.

People do not read enormous chat histories, and models can focus on the wrong detail.

Files are different.

People can edit them. Agents can read them. Teams can synchronize them.

I increasingly think the best Agent memory is not a mysterious database. It is maintainable documentation.

### 6. Hooks: Lifecycle Interceptors

The sixth abstraction is hooks.

Claude Code hooks can run four kinds of execution across 27 lifecycle events.

The execution types include shell commands, one-shot LLM prompts, multi-turn Agent conversations, and HTTP webhooks.

Hooks can:

- Block tool execution.
- Modify input.
- Inject additional context.
- Short-circuit the query loop.

Part of the permission system is implemented through hooks.

A `PreToolUse` hook can reject a tool call before the interactive permission prompt appears.

This matters because LLM decisions are unstable.

You cannot rely on the model to remember every engineering rule every time.

Hooks move some mandatory behavior out of model discretion and into a deterministic system.

Tests must run before a commit.

Dangerous commands must be blocked.

Certain directories must not change.

Specific output must be recorded in an audit log.

Do not rely on a prompt for rules like these.

Relying on the prompt is relying on luck.

## The Golden Path: From Enter to Output

The chapter then follows Claude Code's golden path: the complete route from a user's request to the final output.

The example is simple:

The user types, "Add error handling to the login function," and presses Enter.

![Claude Code golden path](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-02-golden-path.png)

*Source: screenshot from the interactive diagram in chapter one.*

The path looks like this:

1. The user enters a task in the REPL.
2. The REPL hands the message to the Query Loop.
3. The Query Loop calls the model API.
4. The model streams content and tool calls.
5. Reads, edits, and commands go to the StreamingToolExecutor.
6. The tool system performs the actions.
7. Tool results are appended to message history.
8. The Query Loop calls the model again with the new context.
9. The loop continues until the model stops requesting tools or an external condition stops it.

The chapter emphasizes three details.

First, the query loop is a generator, not a callback chain.

The REPL pulls messages with `for await`, so the UI's consumption rate naturally affects generation.

This is a good fit for a terminal product, where unbounded output can overwhelm the interface.

Second, tool execution overlaps model streaming.

The `StreamingToolExecutor` does not wait for the entire response. As soon as a concurrency-safe call appears, it can start.

The book calls this speculative execution.

There is a cost. If later model output changes the earlier intent, the result may have to be discarded.

The case is uncommon, and the latency improvement is valuable.

Third, the whole loop is reentrant.

Tool results do not enter a separate processing stage. They become part of message history. The model sees them and decides the next action.

The Agent runtime is therefore a repeated loop between model, tools, and message history.

## The Permission System Prevents a Security Incident

Claude Code can run arbitrary shell commands on your machine.

It can modify files, launch processes, make network requests, and rewrite Git history.

Without a permission system, that capability would be a security incident waiting to happen.

![Claude Code permission resolution](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-03-permission-resolution.png)

*Source: screenshot from the interactive diagram in chapter one.*

The chapter lists seven permission modes, roughly from most permissive to most restrictive:

| Mode | Meaning |
| --- | --- |
| `bypassPermissions` | Allow everything without checks, mainly for internal use or testing |
| `dontAsk` | Allow actions and record them without prompting the user |
| `auto` | Use a lightweight LLM classifier to allow or reject an action |
| `acceptEdits` | Approve file edits automatically and ask about other side effects |
| `default` | Ask the user to confirm important actions |
| `plan` | Read-only mode that blocks modifications |
| `bubble` | Make a sub-agent send permission requests to its parent |

The `auto` mode is especially interesting.

It runs a separate lightweight LLM call. The classifier receives conversation history and a compressed representation of the tool input, then decides whether the action matches the user's original intent.

If the user asked to fix tests, reading files, running tests, and editing relevant files may be reasonable.

Deleting a directory, changing SSH configuration, or accessing an unrelated path should be blocked.

This creates a middle layer between completely trusting the model and interrupting the user at every step.

The classifier is still an LLM.

It is not an absolute security boundary. It is a risk filter.

Truly dangerous actions still need deterministic rules and human confirmation.

The default `bubble` behavior for sub-agents is equally important.

A sub-agent cannot approve its own dangerous action. It asks the parent Agent and ultimately the user.

That closes a practical loophole. A well-behaved main Agent is not safe if a delegated sub-agent can quietly run dangerous commands.

Authorization has to move upward.

## Multi-Provider Architecture

Claude Code can reach Claude through four infrastructure paths: the direct API, AWS Bedrock, Google Vertex AI, and Foundry.

The rest of the system does not need to know which path is active.

![Claude Code multi-provider architecture](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-04-multi-provider-architecture.png)

*Source: screenshot from the interactive diagram in chapter one.*

The Anthropic SDK provides wrappers for the different cloud providers. Each wrapper exposes the same interface.

A factory named `getAnthropicClient()` reads environment variables and configuration, chooses a provider, and constructs the corresponding client.

After that, `callModel()` and the rest of the system see only a general Anthropic client.

The Query Loop does not care whether the request uses the direct API or Bedrock.

Provider selection happens during startup and the result is stored in `STATE`.

The Agent loop, tool system, and permission system remain provider-independent.

That separation is good engineering.

Provider choice should be configuration, not logic scattered through the Agent runtime.

The same rule applies when building Agents around Qwen, DeepSeek, self-hosted models, or another vendor.

The upper layer should care about three things:

Send messages.

Receive a stream.

Detect tool calls.

The infrastructure route underneath should not leak throughout the Agent loop.

## The Build System and the Ironic Leak

Claude Code serves as an internal Anthropic tool and a public npm package.

Compile-time feature flags control which modules enter each distribution.

The book shows pseudocode with this shape:

```ts
const module = feature("SOME_FLAG")
  ? require("./some/internal/module")
  : null
```

The `feature()` call comes from `bun:bundle`.

During the build, each flag becomes a Boolean literal. If the flag is false, dead-code elimination removes the entire `require()` branch.

The module is not loaded, added to the bundle, or published.

The code uses `require()` here for a specific reason.

A dynamic `require()` behind a flag can be eliminated completely. A dynamic `import()` returns a Promise and is more likely to remain in the bundle.

The ironic part is that the information leak happened through the build output.

Early npm packages included source maps with `sourcesContent`.

That field contained the original TypeScript source.

Feature flags removed runtime code, but the source map preserved the source text.

That is how people could read Claude Code's architecture.

The engineering lesson is practical:

**Release security has to inspect source maps, metadata, and debugging artifacts as well as the runtime bundle.**

Code absent from the executable artifact may still appear in a more revealing debugging artifact.

## How the Components Connect

The chapter joins the six abstractions into one dependency graph.

![How Claude Code's components connect](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-05-how-the-pieces-connect.png)

*Source: screenshot from the interactive diagram in chapter one.*

Memory enters the Query Loop through the system prompt.

The Query Loop drives tool execution.

Tool results return to the Query Loop as messages.

Tasks are recursive Query Loops with isolated message history.

Hooks intercept the Query Loop at defined lifecycle points.

Every module reads or writes State, while the reactive store connects relevant state to the UI.

The circular dependency between the Query Loop and Tool System is the defining structure.

The model generates a tool call.

The tool runs and produces a result.

The result enters message history.

The model sees the result and chooses the next action.

The loop continues until the model stops requesting tools or an external limit such as token budget, maximum rounds, or user cancellation ends it.

That is the core of an Agent.

Without the loop, tools are plugins.

With the loop, the system becomes an Agent.

Later chapters follow the golden path in more detail.

Chapter two explains startup.

Chapter three explains the two-layer state architecture.

Chapter four explains the API layer.

Each later chapter enlarges one part of the same path.

Chapter one is the map. The exploration starts afterward.

## What Can We Reuse?

The final section, Apply This, turns the architecture into patterns that can be used in other Agent systems.

### 1. Use an Async Generator for the Agent Loop

The book recommends an async generator instead of callbacks or an event emitter.

The consumer pulls messages at its own pace, giving natural backpressure.

Cancellation can stop cleanly.

Termination reasons become part of the type system.

This addresses the most frustrating problem in callback-based Agents: it is difficult to know when the loop has truly ended and why.

Many demos accumulate events such as `onModelChunk`, `onToolCall`, `onToolResult`, `onError`, and `onDone`.

The design appears flexible, but control flow quickly becomes difficult to follow.

A generator puts intermediate output and the final stopping reason inside one structure.

### 2. Make Tools Self-Describing

Each tool should declare its concurrency safety, permission needs, and rendering behavior.

A central orchestrator should not memorize every special rule for every tool.

Otherwise, the scheduler becomes a god object. Adding one tool forces changes throughout the system.

Self-describing tools scale more linearly.

Adding tool N+1 should not alter the first N tools.

That matters because Agent toolsets always grow: files, shells, browsers, MCP servers, databases, and internal company systems.

If the interface is unstable at the beginning, the later platform becomes very expensive to maintain.

### 3. Separate Infrastructure State From Reactive State

Not every state change needs a UI update.

Session configuration, cost tracking, and telemetry can live in ordinary mutable objects.

Message history, progress, and approval queues belong in the reactive store.

Their access patterns are different.

Some state changes once during startup and is read a thousand times.

Other state changes every second and must redraw the UI.

Combining those categories creates unnecessary work and confusing dependencies.

This pattern may not look exciting, but it matters. Agent product complexity comes from UI, streaming, tool progress, user approval, cancellation, and recovery as well as AI.

A confused state layer can undermine an otherwise capable Agent.

### 4. Define Permission Modes Instead of Scattering Checks

Use a small set of named modes such as plan, default, auto, and bypass.

Route every permission decision through mode resolution.

Do not let every tool contain its own `if (isAllowed)` branch.

Scattered checks eventually behave inconsistently and leave gaps.

A named mode lets a developer understand the overall security posture of the system.

That is essential because an Agent's risk is not limited to saying something incorrect.

It can perform an incorrect action.

The ability to act requires an explicit permission boundary.

### 5. Reuse the Same Agent Loop for Sub-agents

A sub-agent should be another instance of the same Agent Loop, with its own message history.

Permission requests bubble upward.

This lets every sub-agent inherit the main runtime's guarantees: error handling, tool execution, permission checks, and termination states.

A separate sub-agent implementation creates subtle failures:

The main Agent behaves one way.

The sub-agent behaves another.

Some errors appear only in delegated work.

Some permissions apply only to the parent.

Those bugs are extremely difficult to diagnose.

Recursive reuse of the same loop is a major simplification.

## What Is This Chapter Really About?

After reading chapter one, I do not think its main point is that Claude Code is complicated.

Its point is:

**The complexity of an AI Agent lives in the runtime, not in the model's answer.**

A chatbot turns input into output.

An Agent turns a goal into a sequence of actions.

Actions have side effects.

Side effects change world state.

World state changes the next action.

An Agent therefore needs a loop, tools, permissions, state, memory, hooks, and termination conditions.

Remove any one of them and the system becomes unstable.

This explains why so many Agent demos look exciting and then fail inside real projects.

A demo asks whether the model can imagine the next step.

A production system has to answer harder questions:

Can the next step execute safely?

Does the result return to the model correctly?

Can a failure recover?

Can the user understand what happened?

Will cost remain under control?

Can permissions drift?

Can context drift?

Claude Code is worth studying because it turns this operational work into a system.

The conclusion is simple:

**Do not think of Claude Code as a chat box.**

It is an Agent runtime inside the terminal.

The model is the brain.

Tools are the hands.

Permissions are the brakes.

State is the nervous system.

Memory is long-term experience.

Hooks are engineering discipline.

The Query Loop is the heartbeat.

The next article will cover chapter two: startup.

Even a capable Agent loses if startup is slow, initialization is confused, configuration reads are scattered, or the trust boundary is missing before the user gives it any work.

---

## References

- [Claude Code from Source, Chapter 1: The Architecture of an AI Agent](https://claude-code-from-source.com/ch01-architecture/)
- [Claude Code from Source](https://claude-code-from-source.com/)
- [Anthropic Claude Code Docs: Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
