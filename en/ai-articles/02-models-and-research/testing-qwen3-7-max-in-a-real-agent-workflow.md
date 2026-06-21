# Testing Qwen3.7-Max in a Real Agent Workflow

[English](./testing-qwen3-7-max-in-a-real-agent-workflow.md) | [Chinese Original](../../../ai-articles/02-models-and-research/%E5%AE%9E%E6%B5%8B%20Qwen3.7-Max%E5%A4%A7%E6%A8%A1%E5%9E%8B.md)

> English edition based on the Chinese original.

> Date: 2026-06-20

I had tested many large models before, but I had not seriously tested Qwen in my own production workflow. So during the holiday I used a real project, not a toy demo, to see whether Qwen3.7-Max could finish a cross-project, cross-frontend-and-backend Agent workflow that could actually be verified.

The tools I used were Qoder CN and QoderWork.

![Qoder CN](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260620061909187.png)

Qoder CN is an AI coding assistant for developers. QoderWork is a desktop AI work assistant for broader office and productivity scenarios.

Qwen3.7-Max is positioned around several capabilities: strong coding, strong tool calling, long-horizon execution, cross-framework generalization, office productivity, and even physical-world agents. The official examples emphasize long autonomous optimization runs, tool calls across MCP and code execution environments, and compatibility with frameworks such as Claude Code, OpenClaw, Qwen Code, and custom harnesses.

My own test was narrower and more useful: can it understand a real project, find real problems, plan a fix, modify the code, and leave me with something I can verify?

The project I used is PreHub, a GitHub open-source project discovery and recommendation product. It collects GitHub projects, scores candidates, supports manual review, publishes daily recommendations, and has a Radar page for trend monitoring.

The stack is not tiny. There is a Next.js frontend, a Go API and worker, PostgreSQL, project collection, candidate scoring, daily recommendations, a Radar dashboard, Vercel multi-service deployment, and scheduled tasks. A model has to understand pages, APIs, data, jobs, and deployment constraints at the same time.

That is the real test. If the model does not understand whether Radar is using all GitHub projects or only PreHub's sampled pool, or how the Go API and Next.js BFF connect, the code it writes will not matter.

Qwen3.7-Max did well on project understanding. The part that stood out was not that it found problems. Other models can list code issues too. The useful part was that it grouped problems by scenario: admin flows, caching, error states, data definitions, and explanation gaps. GPT-5.5 and Opus 4.8 were able to point out specific code problems, but their output was more scattered.

That difference matters in a real product. PreHub is mostly a personal tool I use myself, so several areas were not polished: admin states, cache behavior, empty states, error explanations, and data scope descriptions. Qwen's diagnosis made those gaps easier to turn into a repair plan.

I then asked it to fix several of the problems it found.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260620000018573.png" alt="Qwen repair task" style="zoom:50%;" />

This was the first moment where it felt closer to engineering collaboration than a simple chatbot answer. It did not just say what was wrong. It kept the surrounding constraints in mind, made changes in a controlled way, and gave me a path to verify the result.

The takeaway is simple: Qwen3.7-Max is not only interesting as a benchmark model. In this test it was useful as a project-level coding agent, especially for understanding messy product context and turning that context into repairable engineering tasks.

It still needs human review. It still needs verification. But the direction is right: the value is not one spectacular answer. The value is whether it can stay inside a real workflow long enough to help you move the project forward.
