# Qoder + Qwen 3.8 实测

[English](../../en/ai-articles/02-models-and-research/qoder-qwen-3-8-hands-on-test.md) | [中文](./Qoder%20%2B%20Qwen%203.8%20%E5%AE%9E%E6%B5%8B.md)

> 日期：2026-07-22

7 月 19 日阿里低调发布了 Qwen3.8-Max-Preview，这是通义千问系列最新一代基座模型，参数量也达 2.4T。可能是除了 fable5 外最强大的模型，我看身边有小伙伴说测试了一下效果不错。

而且这段时间我观察到了很多朋友在说 Qoder ，我寻思 Qoder 不是一个桌面端的工具吗，然后我又了解了一番，发现 Qoder 还出了个 CLI 工具，叫做 **Qoder CLI**，我感觉有点意思，所以打算上手体验下。

于是我想着，能不能用 Qoder CLI 来搭配千问最新的 Qwen3.8-Max-Preview 看一下真实场景下的效果如何呢。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722080932289.png" alt="image-20260722080932289" style="zoom: 25%;" />

所以这次测试主要突出两个方面，一个是 Qoder CLI 到底能不能行，第二个是 Qwen3.8-Max-Preview 的能力到底如何。

先来聊聊 Qoder CLI 吧。

## Qoder CLI

Qoder CLI 的开发背景大家想必已经知道了吧。

之前 Claude Code 被爆出来在 v2.1.91 版本中通过隐写术（Steganography）秘密收集用户环境信息，包括时区、代理设置、中国 AI 实验室关键词这件事情估计大家应该都知道了。

这事儿一出来，国人包括我在内都对 A 社的做法很厌恶，但是 Claude Code 又是一个很好使的 CLI 工具，我们不用它了用什么？

于是没过几天 Qoder 发布了 Qoder CLI 。

**Qoder CLI 是 Qoder 推出的 AI 编程助手命令行工具，也是 Claude Code 的平替方案，被称为国产版 Claude Code**。

安装很简单，不同操作系统的小伙伴直接执行对应的命令就能一键安装。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722061627838.png" alt="image-20260722061627838" style="zoom:50%;" />

以为 Mac 为例，直接执行 **curl -fsSL https://qoder.com.cn/install | bash** 就可以了。

装完之后，你可以在任意 project 下面使用 `qoderclicn` ，然后通过阿里云登录一下就行了。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722062046486.png" alt="image-20260722062046486" style="zoom:50%;" />

这个 Qoder CLI 也继承了 Qoder 家族一绿到底的风格，不过看起来还是蛮清新的。

常见的命令基本上都比较齐全，这里给大家先简要介绍下。

`/login` 可以用来登录 Qoder 账号，可以选择网页端直接登录，也可以使用 `Access Token`来登录

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722063722158.png" alt="image-20260722063722158" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722063851385.png" alt="image-20260722063851385" style="zoom: 50%;" />

使用 `/init` 可以在项目中初始化或更新 `AGENTS.md` 记忆文件。Claude Code 用 `CLAUDE.md` 保存项目约定，Qoder 对应的是 `AGENTS.md` ，就直接把名字换了一下。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722064419512.png" alt="image-20260722064419512" style="zoom:50%;" />

可以使用 Quick 模式简要初始化，也可以使用 Interactive 的方式来交互式初始化。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722065015598.png" alt="image-20260722065015598" style="zoom:50%;" />

`/status` 可以查看 CLI 状态，包括版本、模型、账号、API 连通性、工具状态等，左侧的 tab 还可以显示用量，当然使用 `/usage` 效果一样。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722064903062.png" alt="image-20260722064903062" style="zoom: 67%;" />

`/Compact` 可以压缩上下文。

![image-20260722065738040](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722065738040.png)

`/effort` 调整当前模型的思考深度及相关模型参数。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722065814571.png" alt="image-20260722065814571" style="zoom: 67%;" />

使用`/agents` 命令来查看、创建、管理子 Agent

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722070717156.png" alt="image-20260722070717156" style="zoom:50%;" />

使用 `/memory` 可以打开记忆概览，包括管理用户级、项目级、本地记忆和自动记忆入口，由于我刚刚完成了 /init 的初始化，所以已经有 Project memory 了。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722070831792.png" alt="image-20260722070831792" style="zoom: 67%;" />

使用 `/model` 切换模型版本。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722071913680.png" alt="image-20260722071913680" style="zoom:50%;" />

如果遇到复杂任务可以交给 Subagent 和[动态工作流](https://docs.qoder.cn/cli/workflows)。

动态工作流会把任务拆成扫描、分析、验证和汇总等阶段，再让多个 Agent 并行或者按流水线执行。任务启动后会放到后台继续运行，通过 `/workflows` 或 `/tasks` 可以查看进度、日志和最终结果。仓库审计、迁移规划、大范围重构这类一次 Agent 很难做完的任务，就比较适合这种方式。

另外，我看到远程和云端能力也有了。[Remote Control](https://docs.qoder.cn/cli/remote-control) 可以让手机或 Web 端查看本机 CLI 的运行状态、处理权限审批和继续下发任务；使用 [`--remote` 云端模式](https://docs.qoder.cn/cli/cloud-mode)，任务会直接跑在 Qoder 管理的云端虚拟机里，即使关掉本地终端，Agent 也会继续执行。

![image-20260722105346744](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722105346744.png)

所以，从 Claude Code 迁过来的话，日常命令、项目记忆、Agent 编排、远程执行和扩展方式基本都能找到对应入口。可以说核心能力基本上都一样了。

### 多模型灵活切换

说到版本切换，Qoder CLI 也支持多模型灵活切换，不绑定单一模型，支持 BYOK（自带 Key），可以接入阿里云百炼、OpenAI 等任意模型。

在 [Qoder CN CLI 的模型文档](https://docs.qoder.cn/cli/model) 里，`/model` 的模型选择界面分成了 Default、New Models 和 Custom 三个标签页。添加自定义模型时，按照 Provider、模型类型、具体模型的顺序选择，再填入自己的 API Key，就能保存并切换使用。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722075022964.png" alt="image-20260722075022964" style="zoom:67%;" />

[Qoder CN CLI 更新日志](https://docs.qoder.cn/product-overview/qoder-cn-cli) 里还能看到这项能力的迭代过程：先加入多模型和 BYOK，随后支持自定义推理地址、自定义模型名，最新版本又补上了上下文窗口和推理深度调节。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722074837013.png" alt="image-20260722074837013" style="zoom:50%;" />

### 5 分钟迁移

如果你是从 Claude Code 的小伙伴转过来的，担心配置相关配置还要重新搞一遍，我也有类似的痛点。不过我看到 Qoder CLI 提供了一键迁移工具，这就很丝滑了。

直达链接：https://qoder.com/zh/marketplace/skill?id=official_lj9fIgpz

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722081038607.png" alt="image-20260722081038607" style="zoom: 33%;" />

直接把提示词复制给 Agent，让它一键安装即可。

安装迁移 skills 之后你也可以使用 `/claude-to-qoder-migration` 来进行迁移。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722092520884.png" alt="image-20260722092520884" style="zoom:50%;" />

装完之后 ，Qoder CLI 会向用户询问这些问题，Memory 要不要复制、Skill 要不要复制、权限怎么设置、MCP 服务器迁不迁移。

![image-20260722090759899](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722090759899.png)

迁移完成后，我让 Qoder CLI 列出来了本次迁移的内容。

移范围包括 `settings`、MCP servers、`commands`、`skills`、`agents`、`hooks`、memory（`CLAUDE.md` → `AGENTS.md`）、output styles、`permissions` 和 `plugins`。

现有 `.mcp.json` 以及 `settings` 中的 `mcpServers` 可以直接交给 Qoder CLI 识别。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722091056685.png" alt="image-20260722091056685" style="zoom:50%;" />

不会迁移的内容包括 auth state、OAuth/session 文件、managed settings、remote settings 和 trust caches。账号与会话信息仍要在 Qoder 中单独配置。

### 安全与审计

CLI 会读取项目文件、执行 Bash 命令，也可能通过 WebFetch、WebSearch 和 MCP 访问外部服务，所以我对于安全这块，我比较担心两件事：它做了什么，以及数据最终去了哪里。

按照 [Qoder CN CLI 的权限文档](https://docs.qoder.cn/cli/permissions) 的说明，每一次工具调用前都会经过权限检查，结果只有 `allow`、`ask` 和 `deny` 三种。文件读写、Bash、Web 抓取、MCP 和 Subagent 都在这套规则里。默认模式下，敏感操作会先请求确认；团队也可以按项目配置允许和禁止规则，限制 CLI 能访问的目录、命令和外部工具。

如果需要留下更完整的操作记录，还可以使用 [Hooks](https://docs.qoder.cn/cli/hook)，比如 `PreToolUse`和 `PostToolUse` 。

需要说明的是，CLI 的权限和 Hooks 主要审计的是**工具调用**。如果企业要求完整追踪所有网络流量，仍然要结合代理、网关或 VPC 的出口日志，不能只看终端里的执行记录。

从企业角度来看，这套安全设计还覆盖了更多环节。根据[阿里云发布的 Qoder 企业版信息](https://finance.sina.com.cn/stock/relnews/hk/2026-07-03/doc-inifpkaw2412058.shtml)，Qoder 采用五层纵深防御架构，并已通过 ISO/IEC 27001:2022 认证。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/qoder-security-defense-in-depth.png" alt="Qoder 五层纵深防御架构" style="zoom:50%;" />

- **传输安全**：全量 TLS 加密，支持 TLS 1.2 strict 和 TLS 1.3，同时加入 WAF 与 DDoS 防护。

- **身份与访问**：支持企业 SSO（SAML 2.0）、MFA、RBAC 和 JWT 令牌验签，控制谁能登录、能访问哪些资源。

- **运行时与 AI 安全**：风险操作依次经过静态规则、AST 语法树分析、LLM 风险评估和沙箱隔离执行，尽量在命令真正落地前把风险拦住。

- **数据存储安全**：通过隐私模式、数据驻留、静态加密和租户隔离，控制数据的存储位置与访问边界。

- **供应链安全**：覆盖安全开发生命周期（SDL）、软件成分分析（SCA）和漏洞披露计划（VDP），从依赖引入到漏洞修复都有对应检查。

[Qoder 企业版页面](https://qoder.com/zh/enterprise) 还列出了隐私模式管控和操作审计。这样一来，前面提到的 CLI 权限和 Hooks 负责把控单次工具调用，企业侧会再加上身份、数据、供应链和操作日志，出了问题也能看到整条链路的情况。

##  Qwen3.8-Max-Preview

介绍完 Qoder CLI 的基本情况后，我们来聊一下 Qwen3.8-Max-Preview。

Qwen3.8-Max-Preview 这次发布很低调，但是模型却低调不起来，2.4T 参数，正在以“天”为单位持续进化，有可能是除了 fable 5 之外最强大的模型。

这次我就用 Qoder CLI 搭配着 Qwen3.8-Max-Preview 来实测一下。

用心的小伙伴其实已经发现了，我上面偶然间透露出来我已经切换到了 Qwen3.8-Max-Preview 模型。

这次我测试的项目，是我最近在新开发的一个项目。

ElecMap 是一个包含 Web、API、数据库、地图服务和自动化测试的真实项目。本次让 Qoder CLI 完成首页从“电影级中国地貌图鉴”到“真实街道路网”的连续缩放，包括地图切换、状态保持、键盘操作、加载失败降级和自动化测试。

### 代码阅读能力

首先我让 Qwen3.8-Max-Preview 基于目前的项目情况来分析一下目前项目的完成度情况，是否根据 OpenSpec 的文档实现了相关需求。

![image-20260722162403769](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722162403769.png)

Qwen3.8-Max-Preview 给出的报告如下。

报告包含了六个层面：

1. 总体完成度
2. 逐 Spec 对照分析
3. 未完成 Tasks 详情
4. 需要优化的点
5. 项目缺陷/风险
6. 结论

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722170950064.png" alt="image-20260722170950064" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722171224140.png" alt="image-20260722171224140" style="zoom: 67%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722171250333.png" alt="image-20260722171250333" style="zoom:67%;" />

这份报告看下来还行，数字后面都能找到对应的 Spec、代码文件和测试。

77 个任务完成了 69 个，完成度 89.6%。51 条需求做完了 49 条，7 个 Spec 基本都有对应代码，还找到了 78 个测试文件。

剩下 8 项里，有 5 项需要业务和法务来定，另外 3 项是部署和验收。

CI 没跑 E2E、搜索和缓存后面可能会有性能问题、生产部署也还没做好，它也都直接列出来了。

所以这次代码阅读测试，Qwen3.8-Max-Preview 的表现我觉得是合格的。

我一直比较喜欢 Qwen 在工程实践上面的表现，上次的 Qwen-3.7-Max 我测试就感觉不错，这次 Qwen3.8-Max-Preview 给出的报告我认为更进一步了。

### 使用 /goal 跑一个长任务

我比较关心 /goal 跑长任务的效果究竟如何，因为我之前使用 /goal 跑过长任务，效果不太理想，所以我想着重测一下这块。

所以我先通过 Goal 让 Qoder CLI 自主分析需求、制定计划、修改代码并运行测试；

```bash
请优化 ElecMap 首页地图的缩放体验和 Q 萌视觉。

目前有两个明显问题：
1. 地图放大、缩小时加载时间较长，画面切换不够流畅。
2. 放大到省份和城市后，地图很像普通高德地图，没有明显的 Q 萌旅行地图风格。

请实际启动项目并体验地图，完成以下改进：
- 找出缩放缓慢的真实原因，减少重复初始化、重复请求和不必要的重新渲染。
- 缩放加载过程中保持画面连续，避免长时间空白、卡顿或突然跳变。
```

![image-20260722201214407](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722201214407.png)

它先排查了一下卡顿原因，主要有三个：缩放时 marker 会反复重建，`setMarkers()` 每次都会全量刷新，视口变化也会让页面频繁重新渲染。

然后它把这几个地方都改了一遍。省份和城市只在跨过缩放层级时更新，marker 只处理有变化的部分，视口更新也限制到了每 120ms 一次。说白了，就是尽量少干重复的活。

视觉上也改了一遍，地图背景、标记、缩放按钮和浮层都统一成了粉蓝色的圆角风格，过渡时间也从 900ms 缩短到了 400ms。

给大家看一下具体的效果。

![image-20260722204839804](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722204839804.png)

比如我缩放到浙江省是这样的效果。

![image-20260722204710395](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722204710395.png)

在青甘大环线附近是这种效果。

![image-20260722205253153](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722205253153.png)

在上海放到最大是这种效果。

![image-20260722210321965](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722210321965.png)

从实际页面看，全国、省份、城市直到街道路网这几层都顺利切出来了。天空蓝背景、粉色标记和圆角浮层也延续到了真实地图这一层，至少不会一放大就完全变成另一套界面。

这次我没有做毫秒级的前后 benchmark，所以不说性能提升了多少百分比。

我的直接感受是地图缩放的连续性确实好了不少，尤其是从中国地貌图切到省份和城市时，不会再长时间空白。

### 多 Agent 并行

我第二个测试，是用多 Agent 分别处理规格分析、前端交互、地图接入和测试审查，记录任务完成度、人工介入次数、运行时间及 Credits 消耗。Prompt 如下

```bash
请使用多 Agent 并行实现 ElecMap 的“城市内容点快速预览”功能。

目标：用户进入城市地图后，可以按景点、人文、美食筛选内容。点击地图标记显示内容预览卡，点击列表项目同步聚焦地图标记，并可进入详情页。手机端使用底部预览卡，支持键盘操作和关闭。

Agent 分工：

- 规格 Agent：分析现有 OpenSpec，补充内容预览、分类筛选和地图/列表同步的验收场景。
- 前端 Agent：实现筛选器、内容预览卡、列表选中状态和手机端交互。
- 地图 Agent：实现内容点加载、标记点击、聚焦、聚合以及地图与列表双向同步。
- 测试 Agent：审查实现，补充单元、E2E 和无障碍测试，运行完整质量检查。
- Team Lead：协调文件边界、合并结果并完成最终验收。

不得新增区县导航、餐馆推荐或路线功能，不得一次加载全国内容，不新增生产依赖。

最终记录各 Agent 的任务完成情况、总完成度、人工介入次数、运行时间和 Qoder CLI Credits 消耗，并提供功能截图、测试结果及剩余问题。
```

![image-20260722184748433](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722184748433.png)

下面是 Agent 工作流的报告说明。

![image-20260722195418433](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722195418433.png)

这一轮一共跑了 53 分钟，拉起了 5 个 Agent。一个补 Spec，一个写前端，一个处理地图，剩下的负责集成和测试。

做出来的功能和我想的差不多。点击地图标记或者列表，就会弹出内容预览卡。

测试情况也还行，Typecheck 和 Lint 都通过了，457 个单元测试全部通过。这次还新写了 13 个单元测试和 5 个 E2E 测试，不过 E2E 需要先启动 Docker 环境，所以最后没有真正跑起来。

整个过程我没有手动介入，主线程自己修复了 3 个类型和测试问题。

不过也没有 100% 完成，5 个 Agent 里有 1 个超时，Credits 也没拿到准确数字，只记录了 82 次工具调用。最终完成度是 95%。

## 模型折扣

我整个实测过程可以用一句话概括：效果不错，量大管饱！Qoder 国际版和 Qoder CN 全家桶都支持。

![image-20260722134147254](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722134147254.png)

而且按照 [Qoder CN 的账号与订阅文档](https://docs.qoder.cn/product-overview/account-and-subscription)，专业版是 59 元/月，包含 2,000 Credits。这 59 元覆盖的是整套个人 Credits，CLI 只是其中一个使用入口。

![image-20260722182305519](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722182305519.png)

再搭配上 [Qwen3.8-Max-Preview 的限时折扣](https://docs.qoder.com/zh/events/qwen-max-preview)，白天 08:00-22:00 是 1 折，Credits 倍率从标准的 0.5x 降到 0.05x；晚上 22:00 到第二天 08:00 是 0.2 折，倍率进一步降到 0.01x。

活动从 2026 年 7 月 19 日开始，目前还没有公布结束时间。所以白天已经很便宜，晚上跑 `/goal` 和多 Agent 这种长任务就更合适了，挂着让它干活，第二天起来看验收结果，非常丝滑。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/wps1.jpg" alt="img" style="zoom: 50%;" />

活干的挺好，而且也便宜，确实属于**量大管饱干活好**了。

Qoder CLI 的使用习惯和 Claude Code 很接近，迁移也很方便，如果你 Claude Code 用不了，可以使用 Qoder CLI 作为丝滑平替。

因为 Qoder CLI 确实可以称之为国产 Claude Code 了。

相关链接

1. [Qwen3.8-Max-Preview 全天 1 折，错峰低至 0.2 折](https://docs.qoder.com/zh/events/qwen-max-preview)
2. [Qoder CN CLI 模型文档](https://docs.qoder.cn/cli/model)
3. [Qoder CN CLI 动态工作流](https://docs.qoder.cn/cli/workflows)
4. [Qoder CN CLI 更新日志](https://docs.qoder.cn/product-overview/qoder-cn-cli)
5. [Claude Code 一键迁移 Skill](https://qoder.com/zh/marketplace/skill?id=official_lj9fIgpz)
6. Qoder CN CLI：[权限](https://docs.qoder.cn/cli/permissions)、[Hooks](https://docs.qoder.cn/cli/hook)、[Remote Control](https://docs.qoder.cn/cli/remote-control)、[云端模式](https://docs.qoder.cn/cli/cloud-mode)
7. [Qoder CN 账号与订阅](https://docs.qoder.cn/product-overview/account-and-subscription)
8. [Qoder 企业版](https://qoder.com/zh/enterprise)
