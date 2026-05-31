# 还在用 Codex 开 xhigh 拉满跑？大错特错

我最近发现一个挺有意思的现象。

不少人用 Codex 的时候，上来就把 effort 开到 `xhigh`。

不管是改个 README，还是修个小 bug，或者是启动一个项目，还是让它帮忙看一段报错，第一反应都是：拉满！！！

（不只针对 Codex ，所有具有 effort 的 LLM 都适用。）

这就像是你本打算洗个车，结果你车开进洗车房把车和人一块洗了。

---

这事儿吧，不能说完全没道理。

`xhigh` 肯定有用。OpenAI 既然给了这个档位，就说明它不是摆设。但是我越来越觉得，把它当默认配置，真不是最佳选项。

**reasoning effort 不是智商开关，它更像一面镜子。**

这面镜子能照出对不同任务难度的依赖程度，是主打多快好省还是啥都不考虑直接拉满。

你需要考虑的是更长的思考时间、更高的 token 消耗、更慢的响应，还有在复杂任务上更充分的推理空间。

但它不会自动帮你把一个烂任务变成好任务。

![image-20260530174346491](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260530174346491.png)

---

我之前也有这个毛病。

刚开始用 coding agent 的时候，心态很朴素：反正我都让它干活了，那就给它开最强。

这就是订阅制的弊端，只要用不完，从心理上感觉就会亏。而且 Codex 上周一周重置三次的节奏，谁都会感觉亏。。。

![image-20260526153155000](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526153155000.png)

但用多了之后会发现，有些任务开 `xhigh`，不仅没必要，甚至有点反效果。

比如让 Codex 改一个变量名，补一段注释，整理一下日志，或者把一段 Markdown 改得更顺一点。

这种任务的核心诉求是什么？

多快好省。

你要的是它看懂、动手、改完、给 diff。不是让它在后台沉思半天，最后给你一个“经过综合权衡”的变量名。

更关键的是，`xhigh` 很容易让人形成一种错觉：只要结果不好，就是模型想得还不够久。

但很多时候，问题根本不在这。

问题可能是你没给测试命令，没说验收标准，也没告诉它哪个目录不能碰，也没把业务背景讲清楚，甚至只是工作区本来就一坨。

这些东西，开再高的 effort 也救不了。

它最多是在错误上下文里更认真地绕路。

---

## 官方其实也没让你一上来就拉满

OpenAI 的 Codex 配置文档里，确实有 `model_reasoning_effort`。它支持 `minimal`、`low`、`medium`、`high`、`xhigh` 这些档位。

![image-20260526153350052](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526153350052.png)

但是在 reasoning models 的说明里，`xhigh` 的定位写得很清楚：深度研究、异步工作流、需要很长 rollout 的 agent 任务，以及安全审计、复杂 code review、困难 coding 任务。

![image-20260526153548884](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526153548884.png)

还有一句我觉得非常关键：

只有当 eval 证明额外延迟和成本值得时，才用 `xhigh`。

这就是很多人用 AI 工具时最容易忽略的地方：我们很容易把“更贵、更慢、更重”误认为“更专业”。

提示词越长，好像越专业。

上下文塞得越满，好像越专业。

MCP 接得越多，好像越专业。

effort 开得越高，好像越专业。

但工程不是这么玩的。工程讲的是约束、反馈和验证。一个任务如果 3 分钟能解决，你非让它用 30 分钟证明自己很努力，这不是专业，这叫看着很专业。

---

## 真正影响 Codex 的，往往不是 effort

Codex 跟普通聊天最大的区别，是它是 agent ，而普通聊天是 chat bot。

agent 会读文件、跑命令、看报错、改代码、再跑测试。

所以真正影响效果的，很多时候不是你把 effort 从 `medium` 拧到 `xhigh`，而是这些更朴实的东西：

项目根目录对不对。

测试命令有没有。

`AGENTS.md` 有没有把规矩讲清楚。

权限给够了没有。

上下文是不是干净。

你有没有告诉它“做到什么程度算完成”。

我现在越来越相信一件事：**一个上下文清楚的 medium，经常比一个上下文混乱的 xhigh 靠谱。**

而且更麻烦的是，默认 `xhigh` 会让你变懒。

你会少做任务拆分，少写验收标准，少关心测试反馈，最后把所有问题都丢给“你再好好想想”。

我之前经常这么干。

然后 xhigh 给你拉了一坨。

我们经常陷入到订阅陷阱里面去，就好像我们是为了消耗订阅而用，并不是为了把活干好而用。

---

## 我更推荐按任务分流

比较舒服的用法，其实很简单，先判断任务类型。

![image-20260530174937782](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260530174937782.png)

轻任务就用 `low`。

比如改文案、抽字段、整理格式、修一个很浅的类型错误。这类任务不需要深度推理，需要的是手快、别乱发挥。

常规开发用 `medium`。

写一个小功能、补测试、处理普通 bug、看一段日志、做一次资料综合，`medium` 大部分时候够用。OpenAI 在 GPT-5.5 的说明里也提到，默认是 `medium`，而且很多 workloads 用 `low` 也能跑得不错。

复杂任务再上 `high`。

比如跨模块重构、疑难 bug、架构方案取舍、长上下文分析。这个时候多给一点推理空间是合理的，因为任务本身就需要规划和权衡。

`xhigh` 呢？

留给少数真正硬的东西。

比如安全审计、复杂 code review、长链路研究、特别困难的 coding workflow，或者你已经试过 `medium` / `high`，确实发现它差一口气。

这时候再开 `xhigh`，我觉得没问题。

但默认就开，属于用李云龙的意大利炮打了个蚊子。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260526164759871.png" alt="image-20260526164759871" style="zoom:50%;" />

---

如果你经常用 Codex CLI，可以配几个 profile。

```toml
[profiles.fast]
model_reasoning_effort = "low"

[profiles.work]
model_reasoning_effort = "medium"

[profiles.deep]
model_reasoning_effort = "high"
```

我这里故意没写 `xhigh`。

原因是 xhigh 不应该成为日常的工作入口。

你真遇到那种“今天这个任务就是要让它狠狠干一把”的情况，再临时切过去就行。

这个跟权限也有点像。

你不会因为某个项目偶尔需要全盘访问，就把所有项目默认开成最大权限。工具给你选择，不代表每个选择都适合默认。

---

我一直觉得，AI 时代最容易被误解的一句话是：AI 放大人的能力。

很多人听到这句话，只听到了“放大”。

但它真正残酷的地方在于，它也会放大你的混乱。

你目标清楚，它帮你加速达成目标。

你判断模糊，它会带着你越跑越远。

你给它一个好问题，它能给你一个不错的解法。

你给它一个烂问题，再开 `xhigh`，它也只是更努力地陪你绕圈。

所以我现在用 Codex 的一个原则是：

日常 `medium`，轻任务 `low`，复杂任务 `high`。

`xhigh` 留着。

真到需要的时候再开。

**AI 是解题高手，但不是判断专家。真正该开到 extra high 的，是人的判断力。**

---

参考资料：

- OpenAI Codex Configuration Reference：`model_reasoning_effort` 支持 `minimal`、`low`、`medium`、`high`、`xhigh`，且 `xhigh` 依赖模型支持。https://developers.openai.com/codex/config-reference
- OpenAI Reasoning models：不同 effort 的适用场景，`xhigh` 只建议在评测证明额外延迟和成本值得时使用。https://developers.openai.com/api/docs/guides/reasoning#reasoning-effort
- OpenAI Using GPT-5.5：默认 `medium`，很多 workloads 用 `low` 也能表现良好。https://developers.openai.com/api/docs/guides/latest-model#using-reasoning-models
- OpenAI Codex Best Practices：建议用配置统一模型、reasoning effort、权限、profiles 等。https://developers.openai.com/codex/learn/best-practices#configure-codex-for-consistency
- OpenAI Codex Pricing：Codex 使用量与模型、任务复杂度、本地或云端任务有关，复杂上下文和长任务会消耗更多配额。https://developers.openai.com/codex/pricing
