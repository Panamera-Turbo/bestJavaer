# Codex's on the phone. That's Agent's supposed to be moving.

[English](./codex-s-on-the-phone-that-s-agent-s-supposed-to-be-moving.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Codex%20%E8%BF%9B%E6%89%8B%E6%9C%BA%E4%BA%86%EF%BC%8C%E8%BF%99%E6%89%8D%E6%98%AF%20Agent%20%E8%AF%A5%E6%9C%89%E7%9A%84%E7%A7%BB%E5%8A%A8%E7%AB%AF.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-15

OpenAI published a new article on May 14, 2026:[Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/).

The core of this update is simple: Codex goes into ChatGPT mobile application.

![Codex mobile preview](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260515054025761.png)

In product form, it is not a new stand-alone App, but is directly present in the iOS and Android client of ChatGPT. It is now preview and is available to all supported areas and covers all schemes, including Free and Go.

To use it, you need to update the ChatGPT mobile application and Codex MacOS app. Sets the entry on the sidebar of the Codex desktop. Windows support is not officially online, officially said soon.

![Codex desktop connect](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260515054802649.png)

It sounds like a little function, but I think it's actually a critical step in Codex's product pattern.

Because after Agent actually started taking on a long mission, the question was no longer just "will it write code?" It was, "It works half way through, and if I need to be there right away."

It's not a remote desktop

A lot of people saw Codex moving, and the first reaction could be: Isn't that remote control?

Nope.

The remote desktop solution is if you can operate a computer on your phone. Codex's move-end solution is if you can take over Agent's workflow on the phone.

The two are very different.

OpenAI was designed this time to connect a mobile phone to a machine running Codex, which could be your laptop, developer or remote environment. Cell phones are loaded in the real-time state of the environment, rather than moving codes, keys and dependencies to the cell phone.

The real mission remains the original machine.

Your documents, certificates, permissions, local settings are kept there. The end of the cell phone is just for you to view the thread, output, screenshot, terminal results, diff, test results and approval status.

It's a logical design.

Cell phones are not suitable for development environments, but they are well suited for decision-making interfaces.

# It's a solution that's stuck in the middle #

Codex, this Agent does a long job, often without running from head to end.

It's got a lot of little forks:

1. You are required to choose one of the two achievement options.
2. You are required to authorize the operation of a risk-based order.
3. The test failed, requiring you to judge whether to continue or change direction.
4. After reading the code, it becomes clear that the requirements are not clear and that you are required to supplement the context.
5. After completing the modifications, you are required to look at the diff and test results.

These are small, but they will stop the whole mission.

You had to sit in front of the computer before you could move on. Now Codex moved these nodes to the phone.

And you can also look outside at what Codex is doing, see what it's finding, approve next steps, switch models, add new ideas, or change direction.

That's where the moving end is really valuable.

It's not for you to write code on the phone, it's for you to keep code jobs on the phone.

All the threads can keep up

OpenAI also stressed that this is not just a new task for computers, it is not just a remote control of individual tasks.

Codex moves the end to handle all the threads you already have.

This is crucial.

Agent is often not a task, but a set of parallel tasks. A thread is changing Bug, a thread is writing tests, a thread is on the research interface, and a thread is sorting out a program.

What really needs mobile support is not "I suddenly think of a mission and send it to a computer", but "I've got a lot of work going on, and I want to know which one needs my involvement at all times".

So Codex moves the end more like an accompanying mission console.

It doesn't keep you by the computer, and it doesn't lose control of Agent's work because you leave the computer.

Safe design is also important

The most susceptible to misinterpretation of such functions is security.

It would be dangerous to just expose our services to the public network. The developers often have code warehouses, environment variables, API Key, SSH configuration, platform account numbers and various local privileges.

OpenAI this time mentioned that Codex uses a security relay to keep trusted machines accessible between different devices, but does not need to expose them directly to the public Internet.

That's the right direction.

The stronger the execution environment, the more sensitive information inside. The best way for the mobile end to participate in the workflow is not to copy the environment, but to connect it safely.

The file is still on the original machine.

Permission is still on the original machine.

The evidence is still on the original machine.

Cell phones are only for viewing, approving and directing.

This is consistent with the safe borders of the real development environment.

# Remote SSH adds to the business scene

This update is not just an entry point on the phone, OpenAI officially pushed Remote SSH to its original ability.

The Codex desktop application can now identify the hosts in the SSH configuration and create projects and run threads in remote machines.

This capacity is critical to the business landscape.

Many teams do not develop on personal computers, but work in managed remote environments. It includes company-approved dependency, evidence, security strategies and computing resources.

If Codex can only run on PCs, it will have difficulty gaining access to this type of workflow.

The point of Remote SSH is that Codex has access to the approved development environment of the enterprise, rather than asking the enterprise to rebuild a new environment for Agent.

Desktop-end start-up missions, remote environment missions, mobile-phone monitoring missions.

Once the link runs, Codex is not just a personal developer tool, but a part of the team infrastructure.

# Hooks and access tokens make it more like a tool

OpenAI also released two engineering-neutral capabilities this time.

One is Programme Access tokens.

Enterprise and Business workspaces can distribute domain certificates from ChatGPT workspace settings for use in CI, distribution process and internal automation.

The other is Hooks.

Hooks is now officially available and covers all plans. It can be used to scan keys in the alert, run a certifier, record conversations, create memories, or customize Codex behaviour to the warehouse and directory.

These two capabilities don't sound like moving ends, but they are closer to what is really needed in the production environment.

Agent wasn't just "talking" to produce.

It needs to be able to access processes, be restrained, audited and trigger checks before and after critical actions.

Hooks addresses customization and governance.

Programmatic access tokens addresses how automated systems can safely call Codex.

The move-end solution is how people get involved.

These three things come together, Codex's form is a lot more complete.

# HIPAA supports a signal

OpenAI also mentioned that the eligible ChatGPT Enterprise workspaces can be used in the local settings CLI, IDE, Codex app which meet the requirements of HIPC.

This update is not necessarily directly related to ordinary users, but the signal is clear: Codex is moving towards a more serious industry scenario.

Medical, financial, and intra-enterprise systems are not missing "models that can write codes".

What they lack is access to the real work environment, respect for authority, compliance requirements, and managed Agent.

So HIPAA supports not an isolated function.

It is essentially in the same direction as Remote SSH, Hooks, access tokens, security relays: Codex needs to move from a personal efficiency tool to an organization-enabled project, Agent.

The real change is the collaborative rhythm

OpenAI mentioned in the article that more than 4 million people are using Codex every week.

There's one more important change behind this number: people and Agent work together no longer in short-term dialogue, but in long-term.

In the short conversation, one word from the man, one word from the model.

In the long line, Agent will read the code, change the file, run the tests, organize the results, and then stop and ask you at the key node.

So the future AI programming tool, the moving end should not be just a chat portal.

It should be a status panel, an approval entrance, a steering wheel.

You don't have to do all the work on the phone.

You just have to show up at a critical moment.

The value of the Codex moving end is right here.

It makes Agent work no longer tied to a computer, a table, a fixed scene. The code is still running in the right environment and people can connect to the workflow anywhere.

That's what Agent's mobile end looks like.
