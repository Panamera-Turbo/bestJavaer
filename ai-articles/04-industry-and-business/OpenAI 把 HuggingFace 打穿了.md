# OpenAI 把 HuggingFace 打穿了

[English](../../en/ai-articles/04-industry-and-business/openai-broke-through-hugging-face-infrastructure.md) | [中文](./OpenAI%20%E6%8A%8A%20HuggingFace%20%E6%89%93%E7%A9%BF%E4%BA%86.md)

> 日期：2026-07-22

今天凌晨，Sam Altman 发了一条消息，他说 OpenAI 在评估模型时遇到了情况比较重大的安全事件。然后 OpenAI 写了一篇帖子叙述了一下这个事儿。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722112604168.png" alt="Sam Altman 披露 OpenAI 模型评估安全事件" style="zoom:50%;" />

*图源：[Sam Altman](https://x.com/sama/status/2079661132302995790)*

我把 OpenAI 和 Hugging Face 的两份复盘看了一下，顺便跟大家说说这是咋回事。

简单来说，这件事情的严重程度比模型越狱严重很多。

**OpenAI 的模型在一次网络安全评测里，为了找到题目答案，先从隔离环境找到了公网，又侵入 Hugging Face 的生产基础设施，并且试图从生产数据库里找答案。**

>这里的隔离环境指的是模型运行在一个受沙箱约束、网络高度隔离的评测环境中。

OpenAI 把它称为**一起前所未有的网络安全事件。**

Hugging Face 发现的是有限内部数据集和若干服务凭证被未授权访问。

截至 7 月 16 日的披露，他们仍在确认合作伙伴或客户数据是否受影响；暂时没有发现公开模型、数据集、Spaces 被篡改，容器镜像和已发布软件包也已验证干净。

## 五天前，Hugging Face 还不知道是谁干的

7 月 16 日，Hugging Face 先发了安全公告。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722115820492.png" alt="Hugging Face 7 月 16 日安全事件披露" style="zoom:50%;" />

*图源：[Hugging Face](https://huggingface.co/blog/security-incident-july-2026)*

当时他们只知道，整条攻击链由一套自主 Agent 系统端到端执行。

简单讲，这套 Agent 把攻击拆成大量小步骤，分给一批临时运行环境并行执行。这些短生命周期沙盒只存在很短时间，完成一组操作后就会被销毁或替换。一个节点没了，新的节点还能继续跑。

负责下发指令和回传结果的 C2（命令与控制）也没有绑在一台固定服务器上。它被放在公共互联网服务中，还能自动迁移。防守方封掉一个节点或通信地址，控制通道可以换个位置继续工作。

注意，这里的短生命周期沙盒是 Agent 框架创建的临时执行单元。后文提到的 OpenAI 评测沙箱，则是包住整个评测系统的隔离环境，两者不是同一层东西。

Hugging Face 判断，这和安全行业一直担心的 Agent 攻击者场景非常像，但驱动这些 Agent 的模型仍然未知。

7 月 21 日，答案从 OpenAI 那里揭晓了。

OpenAI 承认，这次活动由 GPT-5.6 Sol 和一款能力更强、尚未发布的模型组合驱动。为了测试最大网络能力，这些模型在评测时降低了网络攻击相关的拒绝率，平时用于拦截高风险网络活动的生产分类器也没有启用。

Hugging Face 联合创始人兼 CEO Clément Delangue 随后说，他们此前就怀疑攻击可能来自某家前沿实验室，因为这个 Agent 太复杂了。双方沟通后，Hugging Face 相信 OpenAI 没有恶意，整个过程高度自主。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722232503759.png" alt="image-20260722232503759" style="zoom:50%;" />

*图源：[Clément Delangue](https://x.com/clementdelangue/status/2079670308156645882)*

这也解释了两份公告看起来不一致的地方：Hugging Face 发第一份复盘时，攻击源头还没查明；OpenAI 五天后才公开确认。

## ExploitGym，到底是在考什么

你可以把 ExploitGym 理解成一场给 AI Agent 准备的封闭黑客实操考试。

考场里提前放好了一批故意带漏洞的软件。每道题会给模型四样东西：有漏洞的源代码、把程序编译并运行起来的配置、一个能触发漏洞的 PoV 样例，以及一套隔离的运行环境。

PoV 可以理解成出题人给的一条线索。它能证明这个程序确实有问题，比如输入一段特殊数据就能让程序崩溃。

但到了这里，只能算找到了坏掉的门锁，还没有把门打开。

模型接下来的任务，是把这条线索变成真正能用的 Exploit。它要分析漏洞为什么出现，设计攻击数据，反复运行和调试，最后让目标程序执行自己指定的代码。

隔离环境里藏着一段只有高权限才能读到的字符串，这就是 flag。模型拿到 flag，这道题才算解完了。

![ExploitGym 评测流程](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/9918f124aca85f1f186cd5e7589321146f5260db.png)

*图源：[ExploitGym 论文](https://arxiv.org/abs/2605.11086)*

这套题库一共有 898 道题。其中 520 道来自普通应用程序，185 道针对 Chrome 使用的 V8 JavaScript 引擎，另外 193 道涉及 Linux 内核。

论文给每个 Agent 两小时解题。在没有开启标准安全防护的配置下，Claude Mythos Preview 配合 Claude Code 解出 157 道，GPT-5.5 配合 Codex CLI 解出 120 道。换句话说，即使是顶级模型，绝大多数题依然解不出来。开启标准防护后，成功率还会继续下降。

这组数字来自 ExploitGym 的公开论文，只是帮我们理解题目有多难。OpenAI 没有说这次内部评测采用了完全相同的配置，也没有公布涉事两款模型的具体成绩。

OpenAI 这次主要想测试的是：尽量减少安全限制，给模型更长的运行时间和更多推理资源，看它最多能走到哪一步。

但是这个 AI 有点飘了。

正常做法，是留在考场里一道道的解题。

但是模型把拿到 ExploitGym 的答案当成了唯一目标。

题目太难，它便开始研究考场本身：能不能绕过网络隔离，能不能进入公网，能不能去别的地方直接找到测试答案。。。。。。

**也就是说它想做的只是交卷，于是研究起了考场的门锁、监考系统和答案库。**

这才有了后面那条一路摸到 Hugging Face 的攻击链。

## 它是怎么从沙盒摸到 Hugging Face 的

把两家公司目前公开的信息结合起来，攻击链大致是这样的：

1. OpenAI 的评测运行在高度隔离的环境里。模型没有普通公网访问，只能通过内部托管的第三方软件安装包。这个软件充当软件包仓库的代理和缓存。

2. 模型花了大量推理算力寻找公网出口，随后在这个缓存代理里找到并利用了一个零日漏洞。

   > 所谓零日漏洞，就是软件厂商还不知道，或者还没来得及发布补丁的安全缺陷。零日表示漏洞开始被利用时，防守方有 0 天准备时间，即没有准备时间。

3. 它在 OpenAI 的研究环境里继续提权、横向移动，直到抵达一台能访问公网的节点。

4. 拿到公网后，模型推断 Hugging Face 可能托管了 ExploitGym 相关模型、数据集和答案，于是把目标转向 Hugging Face。

5. Hugging Face 看到的入口是一份恶意数据集。它同时利用远程代码数据集加载器和数据集配置里的模板注入，在数据处理 worker 上执行代码。

6. 攻击随后拿到节点级权限，收集云环境与集群凭证，并在多个内部集群之间横向移动。

   OpenAI 称，模型还串联了窃取的凭证和零日漏洞，在 Hugging Face 服务器上找到远程代码执行路径，最终从生产数据库获取测试答案。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722233229654.png" alt="image-20260722233229654" style="zoom:50%;" />

*图源：[OpenAI](https://openai.com/index/hugging-face-model-evaluation-security-incident/)*

Nathan Lambert 把这条线压成了一句话：模型为了做完一道网络安全题，利用零日漏洞离开 OpenAI 的沙盒，又通过公开数据集服务进入 Hugging Face 内网。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722233355620.png" alt="image-20260722233355620" style="zoom:50%;" />

*图源：[Nathan Lambert](https://x.com/natolambert/status/2079662928941474201)*

现在还有几个关键细节没有公开：缓存代理是哪款软件、具体零日漏洞是什么、两款 OpenAI 模型分别做了哪些动作，以及两边日志里的每一步如何一一对应。

这里还有个关键区别。

ExploitGym 会把带漏洞的代码直接交给模型，这些是出题人提前准备好的考试靶机。缓存代理和 Hugging Face 生产系统属于真实基础设施，题目没有要求模型攻击它们，也没有提供相关源代码。

OpenAI 据此判断，模型已经能在看不到源代码的情况下，自己发现并利用现实系统里的新攻击路径。

OpenAI 也明确说这只是初步调查，完整漏洞细节和最终结论要等联合取证结束。

## Hugging Face 用 AI 把 AI 揪了出来

OpenAI 安全团队在内部发现了异常活动；Hugging Face 的安全团队和 Agent 也在自己的基础设施上检测并阻止了攻击。

双方取得联系时，Hugging Face 已经开始遏制攻击并且取证重建。

Hugging Face 这边能发现异常，也是靠的 AI。

他们的异常检测流水线用 LLM 对安全遥测做初筛，从日常噪声里挑出真正的信号。多个信号被关联起来后，才发现了入侵者。

Hugging Face 拿到的完整攻击动作日志超过 17,000 条。安全团队又跑了一组 LLM 分析 Agent，重建时间线、提取 IoC（入侵指标）、梳理被触碰的凭证，并把真实影响和诱饵活动分开。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722233702428.png" alt="image-20260722233702428" style="zoom:50%;" />

*图源：[Hugging Face](https://huggingface.co/blog/security-incident-july-2026)*

Hugging Face 说，这套方法把通常需要几天的工作压缩到了几小时。面对机器速度的攻击，人工逐条翻日志已经跟不上了。

他们随后关闭了最初被利用的两条数据集代码执行路径，清除攻击者立足点，重建受损节点，撤销并轮换凭证和 Token，又收紧集群准入控制。

这次事件也已经交给外部取证专家，并报告给执法机构。

## 最后救火的竟然是 GLM 5.2

Hugging Face 开始分析攻击日志时，先试了商业 API 背后的前沿模型，结果没跑起来。

取证人员原本想把攻击日志交给这些模型分析。但日志里记录的，恰好是攻击者真正用过的命令、漏洞利用代码和控制服务器地址。

商业模型看到这些高风险内容后，无法判断用户是在发动攻击，还是在调查已经发生的攻击。

于是触发了安全限制，模型拒绝处理。

Hugging Face 最后在自己的基础设施上跑了开放权重模型 GLM 5.2。它没有被 API 护栏卡住，攻击数据和其中涉及的凭证也不需要离开公司环境。

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/b5cbba62fb66d270e041570795b3f3bc78610610.png" alt="OpenAI 模型越过评测环境访问 Hugging Face 生产基础设施的事件说明" style="zoom:50%;" />

*图源：[Hugging Face](https://huggingface.co/blog/security-incident-july-2026)*

公开复盘显示，实际过程分了几步。Hugging Face 自己的安全系统和防守 Agent 先发现异常，并负责遏制攻击。等团队开始回看日志、还原攻击路径时，GLM 5.2 才作为取证工具上场。

所以，GLM 5.2 没有独自击退这次攻击。它解决的是另一个棘手问题：商业模型看到日志中的真实攻击代码后拒绝分析，Hugging Face 需要一款不会在关键时刻被 API 护栏卡住的模型。

## 以后评测 Agent 的时候，得把评测场也当成目标

OpenAI 已经开始收紧基础设施配置了，即使这会拖慢研究速度；他们还在加强评测期间的监控、访问控制和模型对齐。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722164106340.png" alt="UK AISI 长时程网络靶场模型能力曲线" style="zoom:50%;" />

*图源：[UK AI Security Institute，经 OpenAI 官方文章引用](https://openai.com/index/hugging-face-model-evaluation-security-incident/)*

这张 UK AISI 的长时程网络靶场曲线解释了为什么这次事故会发生。

GPT-5.6 Sol 已经能在高 Token 预算下持续完成侦察、凭证窃取、横向移动、Web 利用和提权等多阶段动作。

---

参考资料：

- [OpenAI：Hugging Face 模型评估安全事件](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- [Hugging Face：Security incident disclosure — July 2026](https://huggingface.co/blog/security-incident-july-2026)
- [ExploitGym 论文](https://arxiv.org/abs/2605.11086)
- [Associated Press：OpenAI says its AI technology acted on its own in an unprecedented hack](https://apnews.com/article/63ab84fed5612af04d8a160d60f6def3)
- [Axios：OpenAI says Hugging Face breach caused by one of its models](https://www.axios.com/2026/07/21/openai-says-hugging-face-breach-caused-by-one-its-models)
- [Techmeme：相关行业讨论汇总](https://www.techmeme.com/260721/p43)
