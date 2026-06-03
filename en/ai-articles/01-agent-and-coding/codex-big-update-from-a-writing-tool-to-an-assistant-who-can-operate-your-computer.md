# Codex Big Update: From a writing tool to an assistant who can operate your computer

[English](./codex-big-update-from-a-writing-tool-to-an-assistant-who-can-operate-your-computer.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Codex%20%E5%A4%A7%E6%9B%B4%E6%96%B0%EF%BC%9A%E4%BB%8E%E5%86%99%E4%BB%A3%E7%A0%81%E5%B7%A5%E5%85%B7%E5%8F%98%E6%88%90%E8%83%BD%E6%93%8D%E4%BD%9C%E4%BD%A0%E7%94%B5%E8%84%91%E7%9A%84%E5%8A%A9%E6%89%8B.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-18

Codex has received a major update. It's new.`Computer use`Computer Assistant is required to install the Computer use plugin locally in Mac (Windows is also expected to be available soon)

You can set up a Computer use on the Codex desktop.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260418155533936.png" alt="image-20260418155533936" style="zoom: 50%;" />

You can use the computer directly, Codex can view and operate the graphical user interface on MacOS.

It can be used for command line tools or tasks that are not structured enough to perform, such as checking desktop applications, using browsers, changing application settings, processing data sources in non-plug-in form, or repeating errors that occur only in graphical user interfaces.

Codex officially said so.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260418100838365.png" alt="image-20260418100838365" style="zoom: 50%;" />

If you want to install Mac on top, you need to open it.

1. ** Screen recording** permissions to see the target application.
2. **Authorization of ancillary functions** to enable Codex to click, enter and navigate.

But as long as you're install Computer Use, CodeX will guide you to the installation, very silky.

![c4bd2859fd980a588df1eac79b73c05d](https://cdn.jsdelivr.net/gh/doggaifan/picbed/c4bd2859fd980a588df1eac79b73c05d.jpg)

Computer use solves a long-term pain point: a little GUI-level shock for software that is not open to API. Formerly, angent stopped when it came to this kind of app, and now Codex works like a human being.

It's based on models that capture screenshots, understand interface content, and then return to the operational instructions to be executed - "Click the top right button," "Play XXX in the input box", "roll page". These operations are performed by harness, and the results are then intercepted and the rings are closed.

More than 90 plugins were added to the wave, bringing in tools such as Atlas sian Rovo, CircleCI, CodeRabbit, Gitlab Issues, Microsoft's family barrel, and Neuon under the Databricks flag.

# So what can it do #

I asked Codex himself to answer what it could do.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/af3e279b8998f87d6dd19279b3dc2e9b.png" alt="af3e279b8998f87d6dd19279b3dc2e9b" style="zoom: 50%;" />

And then I showed it the lowest-risk test -- it showed it how the system worked.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260418154335455.png" alt="image-20260418154335455" style="zoom: 50%;" />



Show it. Let it send my daughter-in-law a message.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260417204735178.png" alt="image-20260417204735178" style="zoom: 50%;" />

Even a circle of friends is not a problem.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260418154419351.png" alt="image-20260418154419351" style="zoom: 67%;" />

# Officially: When to use, when to use

OpenAI has an important reminder in its official document:

> Because computer use can affect app and system state outside your project workspace, use it for scoped tasks and review permission prompts before continuing.

An official list of scenes suitable for the use of Computer use:

- Test MacOS application, iOS emulator process or other desktop application
- Interact with software without API
- Re-emerge only in graphical interface bug
- Change Application Settings
- Processing data sources without plugins

Not suitable scenarios: involves high-risk operations such as payments, the deletion of large amounts of data, and sensitive operations that require login certification and cannot be manually identified.

# I feel like it's the GUI version of Claw

OpenClaw, you all know -- let AI control your computer tools, mouse, keyboard, browser take over. The benefits are free open source, and the downside is trouble-laying, pure commanding and reticence.

And I feel that Codex's built-in Computer use is equivalent to a GUI version of Claw, and you don't know how everyone thinks, after all, OpenClaw's toughest father Peter has been put on board OpenAI, and I think this time that Computer use is the next time AI will be the prototype to take over your personal PC.

Codex is now the GUI version of this logic - interface, project isolation, Skills Extension, Automation. OpenClaw has almost everything it can, and there are more support and distribution channels for OpenAi.

Claude Code, Cursor, all these competitions are heading in the direction of Universal Age. OpenAI's strategy this time is clear: turning Codex from a programming assistant in the editor to a digital colleague who works across the application, over time, across the tool chain.

It's not a functional supercharge, it's a direct ** location migration.**

Source

- [Computer Use – Codex app - OpenAI Developers](https://developers.openai.com/codex/app/computer-use)
- [New Codex features include the ability to use your computer in the background - Ars Technica](https://arstechnica.com/ai/2026/04/new-codex-features-include-the-ability-to-use-your-computer-in-the-background/)
- [OpenAI expands Codex beyond coding with computer use, memory and plugins - Neowin](https://www.neowin.net/news/openai-expands-codex-beyond-coding-with-computer-use-memory-and-plugins/)
- [OpenAI's Codex Desktop can run your computer now - ZDNET](https://www.zdnet.com/article/openai-codex-desktop-update/)
- [Run long horizon tasks with Codex - OpenAI Developers](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)
- [OpenAI drastically updates Codex desktop app - VentureBeat](https://venturebeat.com/technology/openai-drastically-updates-codex-desktop-app-to-use-all-other-apps-on-your-computer-generate-images-preview-webpages/)
- [OpenAI Codex Update Adds Computer Use, Image Generation, and Plugins - MacRumors](https://www.macrumors.com/2026/04/16/openai-codex-mac-update/)
