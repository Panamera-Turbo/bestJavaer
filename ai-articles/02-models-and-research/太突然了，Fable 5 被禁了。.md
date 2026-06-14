# 太突然了，Fable 5 被禁了。

> 日期：2026-06-13


Fable 5 发布也就三天。

前几天大家还在讨论它是不是 Anthropic 最强模型、Claude Code 里到底强不强、订阅用户能白嫖到什么时候。

结果今天直接来了个王炸。

一个小时前，Anthropic 发公告：美国政府以国家安全权限，发出了一项出口管制指令，要求暂停任何外国公民访问 Fable 5 和 Mythos 5。

**注意，是任何外国公民。**

不管你人在美国境内还是境外，都算。甚至 Anthropic 自己的外籍员工，也不能访问。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260613100057672.png" alt="image-20260613100057672" style="zoom:50%;" />

其他 Claude 模型不受影响。

以前我们聊模型发布，聊的是价格、上下文、跑分、API、谁写代码更强。

现在聊模型发布，还得加一条：**受不受管控。**

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260613100546854.png" alt="image-20260613100546854" style="zoom:50%;" />

如果你只是网页端聊天，大概率会被切到别的模型。

如果你在 API 或 Claude Code 里明确指定 `claude-fable-5`，那就直接给你限制了。

然后 A 社为了表示歉意，把额度重置了。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260613100728041.png" alt="image-20260613100728041" style="zoom:50%;" />

这个动作还算有点诚意。

毕竟这波是模型突然被禁了。你刚开一个 Fable 5 session，跑到一半被切掉，那额度算谁的？

## 发生啥事儿了？

Anthropic 在官方声明里说，政府信件没有给出非常具体的国家安全理由。

他们自己的理解是，美国政府认为自己看到了某种绕过 Fable 5 安全机制的方法，也就是所谓 jailbreak。

但是 Anthropic 不太认可这个判断。

它说自己看过演示，里面只是少量已知的小漏洞，其他公开模型也能发现类似问题。Anthropic 还强调，到目前为止，没有测试人员找到能广泛绕过护栏的 universal jailbreak。

这句话说白了就是：

“你说它有风险，我认。但你说这个风险严重到要立刻全量召回，我不认。”

Fable 5 本来就是 Mythos-class 模型。它和 Mythos 5 是同一个底层模型，只是 Fable 5 加了更严格的安全护栏，面向普通用户开放。

Anthropic 自己也承认，它在 cyber、生物化学、模型蒸馏这些方向上做了很重的限制。很多时候，Fable 5 会把请求切到 Opus 4.8。

前几天已经有人吐槽过这个限制太敏感。

问题就在这里：Fable 5 一边是最强能力，一边又是最重护栏。普通用户觉得它太敏感，政府又觉得它还不够安全。

两边都不满意。

## 这段英文是什么意思？

更有意思的是，有人发了一条截图。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260613100826617.png" alt="image-20260613100826617" style="zoom:50%;" />

这段英文大概意思是：

> 如果根据第三方评估认定该模型存在不可接受的风险，政府应有权阻止或制止其部署。但这一权力必须限定在上述四种特定风险范围内，并且必须有防范政治偏袒或任意决策的保护措施。

这太有意思了。

Dario 说模型有可能存在风险的话，政府要有权阻止，然后政府就把 A 社的 Fable 5 给禁了。

Dario ，这一回旋镖挺疼的吧。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260613103142818.png" alt="image-20260613103142818" style="zoom:50%;" />

---

这次 Fable 5 被禁，是一个明显的信号。

**前沿模型的发布以后会同时带着产品属性和政策属性。**

以前模型下线，常见原因是成本、限流、bug、产品策略。

这次多了一个原因：政府认为它有安全风险。

这对开发者影响很大。

你想象一个场景，你正在用 fable 5 改生产代码，然后突然一条禁令，model 你都用不了了，你这还怎么玩？

你用其他 model ，你的代码会不会直接崩了？

所以这次突然一刀切似的禁令，是对所有开发者的不负责任。

我从我这块已经看到了，claude.ai 已经不能使用 fable 5 的 model 了。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260613102544209.png" alt="image-20260613102544209" style="zoom:50%;" />



这事儿太突然了。

但我估计不是最后一次。
