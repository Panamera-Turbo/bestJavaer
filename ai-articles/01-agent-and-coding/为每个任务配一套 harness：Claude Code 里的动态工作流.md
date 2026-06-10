# 为每个任务配一套 harness：Claude Code 里的动态工作流

> 日期：2026-06-05


![image-20260605092343445](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092343445.png)

大家好，我是 cxuan，一个和 AI Agent 互相折磨的 builder。

先说个我自己的事。

之前我用 `/goal` 挂过一个跑了 75 小时的任务。当时还挺得意，觉得这就是 agent 的终极形态，交代一句，它自己埋头干三天。

结果收益和它烧掉的 token 以及时间根本不成正比。

任务跑到后半程，它开始自我陶醉：我一开始定的约束，跑着跑着就当没看见了。

我一直认为的是我的 Prompt 或者我的目标设定有问题。

直到上周，Claude Code 发布了新的 Opus 4.8 模型，并介绍了其中有一项叫做 dynamic workflows（动态工作流）的特性之后，我才觉得，我这个 goal 也许非常适合使用 dynamic workflows。

这个特性说的是，Claude 现在能即时写出每个任务自己的 harness 了。

默认的 Claude Code harness 是为写代码做的，但它对很多别的类型的任务也好用，比如 Research（研究）、安全分析、agent teams，或者 Code Review（代码审查）。

Workflows 让你能动态创建这种 harness，它使得 Claude 能在内部更原生地解决上面这些问题。你还能把这些 workflow 分享给别人、反复复用。

我会结合这篇文章和自己上手 workflows 的初步体会和心得，来和大家聊聊 dynamic workflows。

> 话虽如此，最佳实践仍在成形中！dynamic workflows 往往更费 token，所以什么时候用、怎么用，得仔细想清楚。

---

## 示例 prompt

在进入技术细节之前，我来给你抛出几个示例 prompt，让你对 workflows 这个东西，有点感觉。

> “这个测试大概每 50 次跑会挂 1 次。建一个 workflow 来复现它，提出几种理论，并在 worktree 里对抗式地验证它们。/goal 在某一种理论成立之前别停。”
>
> 
>
> “用一个 workflow，翻一遍我最近的 50 个 session，从里面挖出我反复在做的那些纠正，把高频出现的变成 CLAUDE.md 规则。”
>
> 
>
> “拿我的商业计划，跑一个 workflow，让不同的 agent 分别从投资人、客户、竞争对手的角度把它琢磨清楚。”
>
> 
>
> “这里有一个装了 80 份简历的文件夹，用一个 workflow 按后端岗位给它们排名，并把前十名复核一遍。用 AskUserQuestion 工具来问我，问出一份评分标准。”
>
> 
>
> “我得给这个 CLI 工具起个名。用一个 workflow 头脑风暴出一堆候选，再跑一场淘汰赛选出前三名。”
>
> 
>
> “用一个 workflow 把我们代码里的 User 模型全局重命名成 Account。”
>
> 
>
> “过一遍我的博客草稿，用一个 workflow 把里面每一条技术声明都对着代码库核一遍——我不想发出去任何错的东西。”

---

大家在用 AI Agent 的时候，是不是会经常这么干，在一个 session（会话）里面，让 Claude Code 同时完成规划和执行工作？

对很多写代码的任务，这套非常有效；

但碰上长时间运行、大规模并行、需要高度结构化的对抗性任务，它处理的并不好。

原因在于：Claude 在单个 context window 里啃一个复杂任务的时间越长，就越容易陷入下面这三种模式。

* **Agentic laziness（agent 偷懒）**指的是 Claude 在一个特别复杂、多环节的任务还没干完时就停下，做了一部分就宣布任务完成了，比如一次安全审查有 50 项，它处理了其中 20 项就收工了。

* **Self-preferential bias（自我偏袒）**指的是 Claude 倾向于偏爱自己产出的结果或发现，尤其是在被要求对照评分标准去验证或评判的时候。

* **Goal drift（目标漂移）**指的是跨越多轮对话之后，对最初目标的忠实度会一点点流失。

  在 compaction（上下文压缩）之后尤其明显。像是边界情况要求、例如“别做 X” 的这类约束，它很容易在过程中丢掉。

这三种里，我对第三种最有发言权。我开头那个跑了 75 小时的 goal，翻车翻的就是这儿，它把我的规矩给忘了。

创建一个 workflow 有助于对抗这些问题，它用一组各自拥有独立 context window、目标聚焦又彼此隔离的 Claude 来协同作业。

---

## 动态工作流 vs 静态工作流

你以前可能用过 Claude Agent SDK 或者 `claude -p` 来创建静态工作流，这种方式会把多个 Claude Code 实例协同到一起。

有了 Claude Opus 4.8 和 dynamic workflows 之后，Claude 现在已经聪明到能为你的具体用例写出一套量身定制的 harness。

![image-20260605092358458](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092358458.png)

---

## 几个好用的模式

你只需要让 Claude 做一个 workflow 就能开始用 dynamic workflows，或者用触发词 `ultracode` 来确保 Claude Code 给你建一个。

但 dynamic workflows 它有几种运作模型，你脑子里把这些装上，下次就能帮你判断什么时候该用、以及怎么通过 prompt 去引导 Claude。

Claude 在搭 workflow 时，常会用到、也常会组合起来的，有下面这几种模式：

![image-20260605092409727](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092409727.png)

* **Classify-and-act（先分类再行动）**：用一个分类 agent 判断任务的类型，再根据任务路由到不同的 agent 或不同的行为。或者，在末尾用一个分类 agent 来决定最终输出。

* **Fan-out-and-synthesize（大活拆开再合并）**：把一个任务拆成许多更小的步骤，每一步跑一个 agent，再把这些结果合并起来。当小步骤数量很多，或者每一步都受益于自己那份干净的 context window、好让它们互不干扰、不交叉污染时，这招特别好用。

  合并那一步是个 barrier，起到屏障作用，等所有 agent 执行完成后，再把它们的结构化输出并成一个结果。

* **Adversarial verification（对抗式核查）**：每 fork（派生）出一个 agent，就会再派生出一个或几个独立的 agent，对照一份评分标准或判据，对抗式地验证前者的输出。

* **Generate-and-filter（生成再过滤）**：就某个主题生成一批想法，再按评分标准或通过验证去过滤，去掉重复的，只留下质量最高、经过检验的那些。

* **Tournament（淘汰赛）**：不去分工，而是让 agent 们在同一件事上竞争。派生 N 个 agent，各用不同的思路去尝试同一个任务。然后用 prompt 或模型充当评委，两两比较地评判结果，直到选出一个胜者。

* **Loop until done（循环到完成）**：对那种工作量未知的任务，不要设固定的轮数，而是循环地派生 agent，直到满足某个停止条件（没有新发现了，或者日志里不再有报错）。

这六个不用全记。我自己最常想起来用的就两个：fan-out（把大活拆开并行跑）和对抗式核查（让一个 agent 专门去挑另一个的错）。一个治慢，一个治它自我偏袒。

剩下那几个，遇到对的场景自然会想起来。

---

Thariq 有句话我很认同：**他发现 workflows 用在非技术工作上，有时反而更有用。**

下面他给出了适用于 workflows 的几种方式。

### 迁移与重构

Bun 就是用 workflows 从 Zig 重写成 Rust 的。

关键是把任务拆成一连串需要逐个处理的步骤，比如调用点、失败的测试、各个模块等等。为每一处修复在一个 worktree 里派生一个 subagent 去改，再让另一个 agent 对抗式地审查，然后把它们合并。可以考虑告诉 agent 别用太吃资源的命令，这样你就能最大化并行，又不至于把机器上的资源耗光。

### 深度研究

Claude Code 发布了一个深度研究 skill（`/deep-research`），它就用了 dynamic workflows。

具体来说，它会进行多路网络搜索，抓取来源，对抗式地核查这些来源的声明，最后合成一份带引用的报告。

但这类研究不止能用在网络搜索上。比如让 Claude 从 Slack 的上下文里汇编一份状态报告，或者通过深入探查一个代码库来研究某个功能是怎么实现的。

### 深度核查

![image-20260605092433094](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092433094.png)

反过来，如果你有一份报告，想把它引用的每一条事实声明都核查、溯源，那你可以生成一个 workflow。

让一个 agent 找出所有事实声明，再为每一条派生一个 subagent 去细查。

你还可以再加一个验证 agent，去检查那个负责溯源的 subagent，确保它找的来源质量过硬。

### 排序

![image-20260605092444968](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092444968.png)

你可能有一份清单，想按某个定性指标来排序，而你相信 Claude Code 擅长评判这个指标，比如把支持工单按 bug 的严重程度排序。

但如果你想在一个 prompt 里排 1000 多行，质量会下降，也塞不进 context。

换个做法：用上面的架构模式跑一场淘汰赛，用一条两两比较的 agent 流水线（相对判断比绝对打分更可靠），或者并行做分桶排名再合并。

每一次比较都是它自己的一个 agent，于是那个确定性的循环负责维护赛程表，只有当前的排序顺序留在 context 里。

### 记忆与规则遵守

![image-20260605092456622](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092456622.png)

如果有一组特定的规则，你发现 Claude 老是漏掉、老是做不好，哪怕写进了 CLAUDE.md 也不行，那就建一个 workflow。

列出一份必须由验证 agent 检查的规则，一条规则配一个验证 agent。再造一个「怀疑论者」人设的 subagent 去复核这些规则、确保它们本身合理，这能帮你避免太多误报。

反方向也成立。

从你最近的 session 和 code review 评论里，挖出你反复在做的那些纠正，用并行 agent 把它们聚类，对每个候选规则做对抗式验证（这条规则真能拦下一个真实的错误吗？），最后把活下来的那些提炼回 CLAUDE.md。

### 根因调查

调试最有效的方式，是想出几个互相独立的假说再逐一验证。

但如果你只用一个 context window，Claude 会有“自我偏袒” 。

一个 workflow 能从结构上挡住这一点：派生多个 agent，从互不重叠的证据里各自生成假说。

比如，给日志、文件、数据各派一个独立的 agent。每个假说接着面对一组验证者和反驳者。

这不只用于代码。workflows 能用在销售（三月份销量为什么掉了？）、数据工程（这条 pipeline 为什么挂了？），或者任何复盘场景上。

### 规模化分流（triage）

![image-20260605092514131](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092514131.png)

每个团队都有一个支持队列、bug 报告，或者别的什么靠人力处理不完的积压。

一个 triage workflow 会给每个条目分类，跟已经在跟踪的去重，然后采取行动。行动可能是尝试修复，也可能是上报给人来处理。

triage workflow 有个好用的模式叫 quarantine（隔离）：禁止那些读取不可信公开内容的 agent 去执行高权限操作，这些操作改由负责据此信息行动的那批 agent 来完成。

把 triage workflow 配上 `/loop`，就能让 Claude 持续不断地干这件事。

### 探索与品味

探索一个问题的不同解法时，workflows 也很有用，尤其当问题是偏品味的（比如设计或起名），又能用一份评分标准来衡量的时候。

可以让 Claude 探索一堆方案，并给一个审查 agent 一份“好方案长什么样”的评分标准。

当审查 agent 认为已经达标，任务就算完成。

方案也可以基于这份评分标准、用一场淘汰赛的方式来排序或挑选。

### Evals（评测）

你可以为特定任务跑轻量级的 eval：在 worktree 里派生几个独立的 agent，再派生比较 agent，对照一份评分标准去比对、给特定的输出打分。

比如，对照某个判据来评估、然后打磨你做的一个 skill。

### 模型与智能路由

造一个针对你的任务调过的分类 agent，让它来决定该用哪个模型。

当你的任务会涉及很多次 tool uses、而在执行前先做点研究如何能帮你认出最适合的模型时，会很有用。

举个例子，“解释一下 auth 模块是怎么工作的” 这个任务，最适合的模型取决于 auth 模块里有多少文件、以及代码库的形态。

一个分类 agent 可以先做这个研究，再根据任务的预期复杂度路由到 Sonnet 或 Opus。

---

## 什么时候别用动态工作流

Workflows 是新东西。虽然在很多场景里它能创造出格外好的效果，但并不是每个任务都需要它，而且它可能最终会用掉多得多的 token。

最好是创造性地用 workflows，把 Claude Code 推到你以前没推到过的地方。对常规的写代码任务，试着问问自己：这事真的需要更多算力吗？

比如，大多数传统的写代码任务，并不需要一个五人审查团。

---

## 搭建动态工作流的几个技巧

### Prompt 写法

用我们上面讲的那些具体技巧，可以把 prompt 写得细致，dynamic workflows 的效果最好。

但 Workflows 也不只为大任务准备。你可以提示模型用一个「quick workflow」。比如，对某个假设做一次快速的对抗式审查。

### 配合 /goal 和 /loop

这块我想多聊两句，因为它正好解了我开头那个坑。

官方的用法是：可以重复跑的 workflow（分流、研究、核查这种），用 `/loop` 定时跑，再用 `/goal` 给它设一个硬性的完成要求。

但我更想说的是 /goal 和 workflow 的关系。/goal 管的是「一直干到完成别停」，可你要是只开 /goal、让一个脑子去扛一个几十小时的大目标，它就会像我那次一样，跑着跑着就飘了。workflow 管的是另一头：把活拆成一堆各自只盯着自己那一摊的小 agent。

这俩得搭着用。我那次 75 小时翻车，问题真不在 /goal，是我让一个脑子单扛了一个三天的目标。要是先用 workflow 把活拆开、再拿 /goal 去盯，goal 盯的东西就靠谱多了：一条拆开的、每步都能单独验证的流水线，而不是一个闷头干三天、最后还失忆的脑子。这个区别，我觉得是这次更新里对我最有用的一点。

### Token 用量预算

你可以为 dynamic workflows 设置明确的 token 用量预算，限制一个任务用掉多少 token。你可以用一个预算来提示它，比如「use 10k tokens」，这就会设上上限。

---

## 保存与分享动态工作流

你可以在 workflow 菜单里按「s」来保存 workflow。你可以把它们 check 进 `~/.claude/workflows`，或者通过一个 skill 来分发它们。

![image-20260605092534641](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092534641.png)

要通过 skill 来分享，把你的 JavaScript workflow 文件放进 skill 文件夹，并在 `SKILL.md` 里引用它们。

为了留出更多灵活度，你可能想提示 Claude：把 skill 里的 workflow 当成一个模板，而不是一个必须逐字照跑的脚本。

![image-20260605092548716](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260605092548716.png)

---

把这套东西扒到底，我的看法是：**dynamic workflows 最关键的地方，是把一个模糊的大任务，变成一件你能验证的工程。**

它对抗的偷懒、偏袒、漂移，说的其实是一件事，**黑箱你没法验证**。一旦拆成一堆隔离的、各自带验证环节的小 agent，你至少知道每一步在干嘛，也知道哪一步能被另一个 agent 当场挑错。

所以它适不适合各位读者朋友们，我觉得有两种考量吧。

- 任务一句话能说完、十分钟能干完，别碰，单 agent 就够。
- 任务长、杂、要反复验证，而且你被它跑着跑着就跑偏坑过，那它就是冲着你这个痛点来的。

我那个 75 小时的 goal，要是重来，我大概不会硬着头皮扛三天了。



本文图源：Thariq《A harness for every task: dynamic workflows in Claude Code》

文章参考：https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
