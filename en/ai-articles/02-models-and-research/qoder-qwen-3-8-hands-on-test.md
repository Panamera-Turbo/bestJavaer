# Qoder + Qwen 3.8: A Hands-On Test

[English](./qoder-qwen-3-8-hands-on-test.md) | [Chinese Original](../../../ai-articles/02-models-and-research/Qoder%20%2B%20Qwen%203.8%20%E5%AE%9E%E6%B5%8B.md)

> Date: 2026-07-22

On July 19, Alibaba quietly released Qwen3.8-Max-Preview, which is the latest generation base model of Tongyi Qianwen series with a parameter volume of 2.4T. It may be the most powerful model except fable5. I think some friends around me said that the results were good after testing it.

And during this time, I observed many friends talking about Qoder. I wondered if Qoder was not a desktop tool. Then I learned more about it and found that Qoder also has a CLI tool called**Qoder CLI**. I found it interesting, so I planned to try it out.

So I thought, could I use Qoder CLI with Qianwen's latest Qwen3.8-Max-Preview to see the effect in real scenarios.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722080932289.png" alt="image-20260722080932289" style="zoom: 25%;" />

Therefore, this test mainly highlights two aspects. One is whether Qoder CLI can work, and the second is how capable Qwen3.8-Max-Preview is.

Let's talk about Qoder CLI first.

## Qoder CLI

You must already know the development background of Qoder CLI.

Previously, it was revealed that Claude Code secretly collected user environment information through steganography in version v2.1.91, including time zone, proxy settings, and Chinese AI laboratory keywords. This matter is probably known to everyone.

As soon as this incident came out, Chinese people, including me, were disgusted with Company A's approach. However, Claude Code is a very useful CLI tool. What should we use it if we don't use it?

So within a few days Qoder released Qoder CLI.

**Qoder CLI is an AI programming assistant command line tool launched by Qoder. It is also an alternative to Claude Code and is called the domestic version of Claude Code**.

The installation is very simple. Friends with different operating systems can directly execute the corresponding commands to install with one click.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722061627838.png" alt="image-20260722061627838" style="zoom:50%;" />

Taking Mac as an example, just execute**curl -fsSL https://qoder.com.cn/install | bash**directly.

After installation, you can use `qoderclicn` under any project, and then log in through Alibaba Cloud.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722062046486.png" alt="image-20260722062046486" style="zoom:50%;" />

This Qoder CLI also inherits the one-green-to-the-bottom style of the Qoder family, but it still looks quite fresh.

The common commands are basically complete, so here is a brief introduction to you.

`/login` can be used to log in to the Qoder account. You can choose to log in directly through the web page, or you can use `Access Token` to log in.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722063722158.png" alt="image-20260722063722158" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722063851385.png" alt="image-20260722063851385" style="zoom: 50%;" />

Use `/init` to initialize or update the `AGENTS.md` memory file in your project. Claude Code uses `CLAUDE.md` to save the project agreement. Qoder corresponds to `AGENTS.md`, so he just changed the name.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722064419512.png" alt="image-20260722064419512" style="zoom:50%;" />

You can use Quick mode for brief initialization, or you can use Interactive mode for interactive initialization.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722065015598.png" alt="image-20260722065015598" style="zoom:50%;" />

`/status` can view the CLI status, including version, model, account, API connectivity, tool status, etc. The tab on the left can also display the usage. Of course, using `/usage` has the same effect.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722064903062.png" alt="image-20260722064903062" style="zoom: 67%;" />

`/Compact` can compress the context.

![image-20260722065738040](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722065738040.png)

`/effort` Adjust the depth of thinking and related model parameters of the current model.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722065814571.png" alt="image-20260722065814571" style="zoom: 67%;" />

Use the `/agents` command to view, create, and manage sub-Agents

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722070717156.png" alt="image-20260722070717156" style="zoom:50%;" />

Use `/memory` to open the memory overview, including management of user-level, project-level, local memory and automatic memory entries. Since I have just completed the initialization of /init, there is already Project memory.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722070831792.png" alt="image-20260722070831792" style="zoom: 67%;" />

Use `/model` to switch model versions.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722071913680.png" alt="image-20260722071913680" style="zoom:50%;" />

If you encounter complex tasks, you can hand them over to Subagent and [Dynamic Workflow](https://docs.qoder.cn/cli/workflows).

Dynamic workflow will break the task into stages such as scanning, analysis, verification, and summary, and then let multiple agents execute it in parallel or in a pipeline. After the task is started, it will be placed in the background and continue to run. You can view the progress, logs and final results through `/workflows` or `/tasks`. This method is more suitable for tasks such as warehouse auditing, migration planning, and large-scale reconstruction that are difficult for an agent to complete at one time.

In addition, I see remote and cloud capabilities are also available. [Remote Control](https://docs.qoder.cn/cli/remote-control) allows the mobile phone or the Web to view the running status of the local CLI, process permission approval and continue to deliver tasks; using [`--remote` Cloud Mode](https://docs.qoder.cn/cli/cloud-mode), the task will run directly in the cloud virtual machine managed by Qoder. Even if the local terminal is turned off, the Agent will continue to be executed.

![image-20260722105346744](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722105346744.png)

Therefore, if you migrate from Claude Code, you can basically find corresponding entrances for daily commands, project memory, agent orchestration, remote execution and expansion methods. It can be said that the core capabilities are basically the same.

### Flexible switching between multiple models

Speaking of version switching, Qoder CLI also supports flexible switching of multiple models, does not bind a single model, supports BYOK (brings its own Key), and can be connected to any model such as Alibaba Cloud Bailian and OpenAI.

In [Qoder CN CLI model document](https://docs.qoder.cn/cli/model), the model selection interface of `/model` is divided into three tabs: Default, New Models and Custom. When adding a custom model, select it in the order of Provider, model type, and specific model, and then fill in your own API Key to save and switch for use.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722075022964.png" alt="image-20260722075022964" style="zoom:67%;" />

You can also see the iterative process of this capability in [Qoder CN CLI update log](https://docs.qoder.cn/product-overview/qoder-cn-cli): first adding multiple models and BYOK, then supporting custom inference addresses and custom model names, and the latest version adds context windows and inference depth adjustment.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722074837013.png" alt="image-20260722074837013" style="zoom:50%;" />

### 5 minute migration

If you have transferred from a friend of Claude Code, you are worried that you have to configure related configurations all over again. I have similar pain points. However, I saw that Qoder CLI provides a one-click migration tool, which is very smooth.

Direct link: https://qoder.com/zh/marketplace/skill?id=official_lj9fIgpz

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722081038607.png" alt="image-20260722081038607" style="zoom: 33%;" />

Directly copy the prompt word to the Agent and let it install it with one click.

After installing migration skills, you can also use `/claude-to-qoder-migration` to migrate.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722092520884.png" alt="image-20260722092520884" style="zoom:50%;" />

After installation, Qoder CLI will ask the user these questions, whether the memory should be copied, whether the skills should be copied, how to set the permissions, and whether the MCP server should be migrated.

![image-20260722090759899](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722090759899.png)

After the migration was completed, I asked Qoder CLI to list the contents of this migration.

The migration scope includes `settings`, MCP servers, `commands`, `skills`, `agents`, `hooks`, memory (`CLAUDE.md` → `AGENTS.md`), output styles, `permissions` and `plugins`.

The existing `.mcp.json` and `mcpServers` in `settings` can be directly passed to Qoder CLI for identification.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722091056685.png" alt="image-20260722091056685" style="zoom:50%;" />

Things that will not be migrated include auth state, OAuth/session files, managed settings, remote settings, and trust caches. Account and session information still need to be configured separately in Qoder.

### Security and Audit

The CLI will read project files, execute Bash commands, and may also access external services through WebFetch, WebSearch, and MCP, so when it comes to security, I am more worried about two things: what it does, and where the data ends up going.

According to the instructions of [Qoder CN CLI permissions document](https://docs.qoder.cn/cli/permissions), each tool call will be checked for permissions, and the results are only `allow`, `ask` and `deny`. File reading and writing, Bash, web scraping, MCP and Subagent are all included in this set of rules. In default mode, sensitive operations will ask for confirmation first; the team can also configure permission and prohibition rules on a per-project basis to limit the directories, commands, and external tools that the CLI can access.

If you need to leave a more complete operation record, you can also use [Hooks](https://docs.qoder.cn/cli/hook), such as `PreToolUse` and `PostToolUse`.

It should be noted that CLI permissions and Hooks mainly audit**tool calls**. If an enterprise requires complete tracking of all network traffic, it still needs to be combined with the egress logs of the proxy, gateway or VPC, and cannot just look at the execution records in the terminal.

From an enterprise perspective, this security design also covers more aspects. According to [Qoder Enterprise Edition Information released by Alibaba Cloud](https://finance.sina.com.cn/stock/relnews/hk/2026-07-03/doc-inifpkaw2412058.shtml), Qoder adopts a five-layer defense-in-depth architecture and has passed ISO/IEC 27001:2022 certification.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/qoder-security-defense-in-depth.png" alt="Qoder five-layer defense-in-depth architecture" style="zoom:50%;" />

-**Transmission Security**: Full TLS encryption, supports TLS 1.2 strict and TLS 1.3, and adds WAF and DDoS protection.

-**Identity and Access**: Supports enterprise SSO (SAML 2.0), MFA, RBAC and JWT token verification to control who can log in and access which resources.

-**Runtime and AI security**: Risk operations are sequentially executed through static rules, AST syntax tree analysis, LLM risk assessment and sandbox isolation, trying to block risks before the command is actually implemented.

-**Data storage security**: Control the storage location and access boundaries of data through privacy mode, data residency, static encryption and tenant isolation.

-**Supply Chain Security**: Covers the Security Development Lifecycle (SDL), Software Component Analysis (SCA) and Vulnerability Disclosure Plan (VDP), with corresponding inspections from dependency introduction to vulnerability repair.

[Qoder Enterprise Page](https://qoder.com/zh/enterprise) also lists privacy mode controls and operational audits. In this way, the CLI permissions and Hooks mentioned earlier are responsible for controlling a single tool call, and the enterprise side will add identity, data, supply chain and operation logs. If there is a problem, the entire link can be seen.

## Qwen3.8-Max-Preview

After introducing the basic situation of Qoder CLI, let's talk about Qwen3.8-Max-Preview.

Qwen3.8-Max-Preview This release is very low-key, but the model cannot be low-key. The 2.4T parameters are continuing to evolve in "days" and may be the most powerful model except fable 5.

This time I used Qoder CLI with Qwen3.8-Max-Preview to test it.

The attentive friends have actually discovered it. I accidentally revealed above that I have switched to the Qwen3.8-Max-Preview model.

The project I tested this time is a new project I have recently developed.

ElecMap is a real project that includes web, API, database, map service and automated testing. This time, Qoder CLI was used to complete the continuous scaling of the homepage from "movie-level Chinese landform illustration" to "real street network", including map switching, state maintenance, keyboard operations, loading failure downgrade and automated testing.

### code reading ability

First, I asked Qwen3.8-Max-Preview to analyze the completion of the current project based on the current project situation and whether the relevant requirements have been implemented according to the OpenSpec document.

![image-20260722162403769](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722162403769.png)

The report given by Qwen3.8-Max-Preview is as follows.

The report contains six levels:

1. overall completion
2. Spec-by-Spec comparative analysis
3. Unfinished Tasks details
4. Points that need optimization
5. Project flaws/risks
6. Conclusion

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722170950064.png" alt="image-20260722170950064" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722171224140.png" alt="image-20260722171224140" style="zoom: 67%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722171250333.png" alt="image-20260722171250333" style="zoom:67%;" />

This report is okay to read. You can find the corresponding Spec, code files and tests behind the numbers.

69 of 77 tasks were completed, a completion rate of 89.6%. 49 of the 51 requirements have been completed, 7 Specs basically have corresponding codes, and 78 test files have been found.

Of the remaining 8 items, 5 items need to be determined by business and legal affairs, and the other 3 items are deployment and acceptance.

CI does not run E2E, there may be performance issues behind search and caching, and production deployment has not yet been completed. They are all listed directly.

So in this code reading test, I think the performance of Qwen3.8-Max-Preview is qualified.

I have always preferred Qwen's performance in engineering practice. I felt good about the last Qwen-3.7-Max test, and I think the report given by Qwen3.8-Max-Preview this time is even better.

### Use /goal to run a long task

I am more concerned about the effect of /goal running long tasks, because I have used /goal to run long tasks before, and the effect was not ideal, so I want to focus on testing this aspect.

So I first let Qoder CLI analyze requirements, make plans, modify code and run tests independently through Goal;

```bash
Please optimize ElecMap's home page map zooming experience and Q vision.

There are two obvious problems:
1. Maps are scaled up and loaded for longer periods of time and images are not fluent enough.
2. After zooming up to provinces and cities, the map is very much like a normal Gothic map, with no obvious Q travel map style.

Please actually start the project and experience the map and complete the following improvements:
- To identify the real reasons for the slow pace of scaling up, and to reduce duplication of initialization, repeat requests and unnecessary rewriting.
- Keep the image continuous during the scaling-up, avoiding long blanks, Cardon or sudden jumps.
```

![image-20260722201214407](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722201214407.png)

It first checked the reasons for the lag. There are three main reasons: the marker will be repeatedly rebuilt when zooming, `setMarkers()` will be fully refreshed every time, and the viewport changes will also cause the page to be re-rendered frequently.

Then it changed all these places. Provinces and cities only update when crossing zoom levels, markers only handle changes, and viewport updates are limited to once every 120ms. To put it bluntly, it means doing as little repetitive work as possible.

The map background, markers, zoom buttons and floating layers have all been unified into a pink-blue rounded corner style, and the transition time has been shortened from 900ms to 400ms.

Let me show you the specific effect.

![image-20260722204839804](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722204839804.png)

For example, when I zoom to Zhejiang Province, this is the effect.

![image-20260722204710395](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722204710395.png)

This is the effect near the Qinggan-Gansu Ring Road.

![image-20260722205253153](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722205253153.png)

This effect will be maximized in Shanghai.

![image-20260722210321965](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722210321965.png)

Judging from the actual page, the layers of the country, provinces, cities, and street and road networks have been successfully cut out. The sky blue background, pink markers and rounded corner floating layer have also been extended to the real map layer, at least it will not turn into a completely different interface once it is zoomed in.

This time I did not do millisecond-level before and after benchmarks, so I won't say how much performance has been improved.

My immediate feeling is that the continuity of map zooming is indeed much better, especially when switching from China's topographic map to provinces and cities, there will no longer be a blank space for a long time.

### Multi-Agent parallelism

My second test was to use multiple agents to handle specification analysis, front-end interaction, map access and test review respectively, and record task completion, number of manual interventions, running time and Credits consumption. Prompt is as follows

```bash
Use MultiAgent to create the "City Content Point quick preview" feature in parallel.

Target: Users can screen content by location, humanities, food, etc. upon entering the city map. Click on the map tag to show the content preview card, click on the list item to synchronize the focus map tag and access the details page. The end of the cell phone uses the bottom preview card to support keyboard operations and close.

Agent Division of Labour:

- Specifications Agent: Analysis of existing OpenSpec, additional previews, classification filters and acceptance scenarios synchronized with maps/lists.
- Frontend Agent: Interact with filters, content preview cards, list selection status and cellular end.
- Maps Agent: Load content points, mark clicks, focus, aggregates and synchronize maps and lists in two directions.
- Testing Agent: review realization, supplementary units, E2E and accessibility tests, running complete quality checks.
- Team Lead: Coordination of document boundaries, consolidation of results and completion of final inspection and inspection.

No additional district navigation, restaurant recommendations or route functions, no national content may be added at one time and no additional production dependency may be added.

The final recording of Agent's mission accomplishment, total completion, number of manual interventions, running time and consumption of Qode CLI Credits, and the provision of functionality screenshot, test results and remaining issues.
```

![image-20260722184748433](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722184748433.png)

Below are the reporting instructions for the Agent workflow.

![image-20260722195418433](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722195418433.png)

This round lasted a total of 53 minutes, and 5 Agents were pulled up. One adds Spec, one writes the front-end, one handles the map, and the rest is responsible for integration and testing.

The function is pretty much what I expected. Click on the map marker or list, and a content preview card will pop up.

The testing situation is also okay, both Typecheck and Lint passed, and all 457 unit tests passed. This time, 13 new unit tests and 5 E2E tests were written. However, E2E needs to start the Docker environment first, so it did not actually run in the end.

I did not manually intervene in the whole process, and the main thread fixed 3 type and test issues by itself.

However, it was not 100% completed. One of the five Agents timed out. Credits did not get an accurate number. Only 82 tool calls were recorded. Final completion is 95%.

## model discount

My entire actual testing process can be summed up in one sentence: the effect is good, the quantity is large and the tube is full! Both Qoder International Edition and Qoder CN Family Bucket are supported.

![image-20260722134147254](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722134147254.png)

And according to [Qoder CN's account and subscription document](https://docs.qoder.cn/product-overview/account-and-subscription), the professional version is 59 yuan/month, including 2,000 Credits. This 59 yuan covers the entire set of personal credits, and CLI is just one of the entrances.

![image-20260722182305519](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722182305519.png)

Coupled with [Qwen3.8-Max-Preview's limited time discount](https://docs.qoder.com/zh/events/qwen-max-preview), it is 10% off from 08:00-22:00 during the day, and the Credits multiplier is reduced from the standard 0.5x to 0.05x; from 22:00 in the evening to 08:00 the next day, it is 0.2% off, and the multiplier is further reduced to 0.01x.

The event starts on July 19, 2026, and an end time has not yet been announced. So it is already very cheap during the day, but it is more suitable to run long tasks such as `/goal` and multiple Agents at night. Just let it work and get up the next day to see the acceptance results. It is very smooth.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/wps1.jpg" alt="img" style="zoom: 50%;" />

The work is pretty good, and it's cheap. It's really a good job with a lot of work and a lot of control.

The usage habits of Qoder CLI are very close to those of Claude Code, and migration is also very convenient. If you cannot use Claude Code, you can use Qoder CLI as a smooth replacement.

Because Qoder CLI can indeed be called the domestic Claude Code.

Related links

1. [Qwen3.8-Max-Preview 10% off all day, as low as 0.2% off during off-peak hours](https://docs.qoder.com/zh/events/qwen-max-preview)
2. [Qoder CN CLI model document](https://docs.qoder.cn/cli/model)
3. [Qoder CN CLI dynamic workflow](https://docs.qoder.cn/cli/workflows)
4. [Qoder CN CLI update log](https://docs.qoder.cn/product-overview/qoder-cn-cli)
5. [Claude Code one-click migration Skill](https://qoder.com/zh/marketplace/skill?id=official_lj9fIgpz)
6. Qoder CN CLI: [Permissions](https://docs.qoder.cn/cli/permissions), [Hooks](https://docs.qoder.cn/cli/hook), [Remote Control](https://docs.qoder.cn/cli/remote-control), [Cloud Mode](https://docs.qoder.cn/cli/cloud-mode)
7. [Qoder CN Account and Subscription](https://docs.qoder.cn/product-overview/account-and-subscription)
8. [Qoder Enterprise Edition](https://qoder.com/zh/enterprise)
