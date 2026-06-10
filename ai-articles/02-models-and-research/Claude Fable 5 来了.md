# Claude Fable 5 来了

> 日期：2026-06-10


<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610062701317.png" alt="image-20260610062701317" style="zoom:50%;" />

昨天就传出来了 Claude Code 可能会发布新模型的消息，果不其然，这就来了。



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610055453048.png" alt="image-20260610055453048" style="zoom:50%;" />

先交代下背景。上次 Opus 4.8 发布的时候，官方就预告过，几周内要把 Mythos 级模型带给所有客户。Mythos Preview 一直没有正式发布，只给少数安全机构和基础设施厂商用，理由是它在网络安全上的能力太强，怕被滥用。

这次 Claude Code 的做法是把同一个底层模型拆成两个名字。Mythos 5 继续留在原来那批合作伙伴手里，普通用户碰不到；

Fable 5 加了一层安全分类器，放出来给所有人。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610061847565.png" alt="image-20260610061847565" style="zoom:50%;" />

名字也起得有讲究，fable 来自拉丁语 fabula，跟希腊语 mythos 是同源词。一个译成寓言，一个译成神话，放出来给所有人听的这个，叫寓言。

先看一下测评数据。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610055538202.png" alt="image-20260610055538202" style="zoom:50%;" />

表头本身就有信息量：写的是 Claude Mythos 5 and Fable 5。小字里说，俩模型分数差在 1 到 3 个点以内，表里报的是高的那个。

跟 Opus 4.8 比，全线赢，有几项是拉开身位的赢。SWE-Bench Pro 80.3% 对 69.2%。FrontierCode 29.3% 对 13.4%，翻了一倍多。空间推理 Blueprint-Bench 38.6% 对 14.5%，接近三倍。

![image-20260610075517060](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610075517060.png)



跟 GPT-5.5 比，大部分也是压着打。SWE-Bench Pro 80.3% 对 58.6%，差出 21 个点。

FrontierCode 这张图更直观。Fable 5 不是只靠堆 token 硬冲，在成本曲线上也压得比较漂亮。

![image-20260610075626982](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610075626982.png)

但 Terminal-Bench 这项我得多说一句。上次 Opus 4.8 发布我吐槽过，这项它干不过 GPT-5.5。这次表里写 88.0%，把 Codex CLI 的 83.4% 给压过去了，但是我得和你说，这是带星号的。

> 星号是什么？
>
> 表底小字说：带星号的项目，因为 Fable 5 在网络安全和生物相关问题上有安全降级，实际得分更接近 Opus 4.8。也就是说 88.0% 是 Mythos 5 的分，你手里这个 Fable 5 干 terminal 的活儿，大概还是 82.7% 上下，跟 Codex CLI 算打平。

最典型的是 ExploitBench，表里 78.0%，Opus 4.8 只有 40.0%，看着像吊打。但它也带星号，你真拿 Fable 5 去跑，分数就掉回 40% 附近。

跟 Mythos Preview 比反而最有意思。SWE-Bench Pro 80.3% 对 77.8%，OSWorld 85.0% 对 85.4%，HLE 带工具 64.5% 对 64.7%——后两项 Preview 还反超一点。

说白了，Fable 5 跟当初那个吓得网络安全股暴跌的 Preview，就是一个段位的东西，互有胜负。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610062743529.png" alt="image-20260610062743529" style="zoom:50%;" />

但是，需要注意的是！降级机制官方也说了：**问到敏感话题，回答你的会静默切成 Opus 4.8。限制主要体现是三类——网络安全、生物与化学、模型蒸馏。**

![image-20260610075710513](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610075710513.png)

官方还给了一个早期数据：超过 95% 的 Fable 会话没有发生 fallback。换句话说，如果你做的是正常写代码、改文档、看财报、跑长任务，大多数时候你拿到的就是 Mythos 级底座。

![image-20260610075836559](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610075836559.png)

Anthropic 这次也把防越狱摆到了台面上。内部评测里，自动红队会在 400 轮里反复重试、回滚、继续绕；外部 bug bounty 超过 1000 小时，没有拿到 universal jailbreak。官方还说，一个外部伙伴测了 30 种公开 jailbreak 技术，Fable 5 对有害单轮网络安全请求是 0 次配合。

官方说的话不能全信，毕竟是官方自测和合作方测试。

不过方向确定了：Fable 5 不会拒绝执行你的任务。而是遇到这种任务会自动把模型给你降级成 Opus 4.8 。

---

除了网络安全之外，官方花了不少篇幅讲生物与化学。

Mythos 5 做过一个 AAV 相关评测。简单讲，就是预测病毒外壳的实验属性。官方说这些候选来自 Dyno Therapeutics，他们没有专门训练模型做这个任务，但 Mythos 级模型靠生物推理超过了专门的 protein language model baseline。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/official-aav-eval.png" alt="AAV viral capsid experimental property prediction chart" style="zoom:50%;" />

这事有两面。

一面是好事：基因疗法、药物研发这类方向，模型真的开始发挥作用了。官方还说，内部蛋白设计专家用 Mythos 5 把部分药物设计流程加速了约 10 倍；14 个蛋白靶点里，有 9 个产出了正在继续研究的强候选。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610080225270.png" alt="image-20260610080225270" style="zoom:50%;" />

另一面就是风险：同样的能力，放错人手里也能做坏事。

所以 Fable 5 暂时会在大多数生物和化学请求上回落到 Opus 4.8。官方后面会开一个生物方向的 trusted access program：去掉生物与化学限制，但保留网络安全限制。

这就是 Anthropic 现在的想法，把能力拆开了，同样也把权限拆开了。

---

价格是 $10 / $50 每百万 token。给两个参照：Opus 4.8 标准价（$5 / $25）的两倍，正好等于 Opus 4.8 fast mode 的价；比 Mythos Preview 当时研究预览的 $25 / $125 便宜一半多。上下文 1M，最大输出 128K。

订阅这边有个要划重点的时间。Claude Code 的模型选择器上挂着一行小字：Included until June 22。6 月 22 日之前，Fable 5 免费包含在 Pro、Max、Team 和企业订阅里；23 号起从订阅里移除，只能走 API 按量付费。官方的说法是，等容量充足了再放回订阅。

![image-20260610080906339](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610080906339.png)

**也就是说接下来这 12 天是个窗口期，我这种 Pro 的也在名单里。这 12 天的额度，直接拉满 Fable 5 开夯了。**

---

说点题外话，我在 Claude 官方发布的小视频中看到了汉字，这是不是从某种角度上来说 A \ 有可能有对中国又好一些了？

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610082136199.png" alt="image-20260610082136199" style="zoom:50%;" />

今天这篇文章就到这里，我们下期再见。





- 官方发布线程：https://x.com/claudeai/status/2064394146916229443
- 模型与定价文档：https://platform.claude.com/docs/en/about-claude/models/overview
