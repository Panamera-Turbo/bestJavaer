# Cursor 掀桌子了，Grok 4.5 这次要上天了？

[English](../../en/ai-articles/02-models-and-research/cursor-grok-4-5-ready-to-take-off.md) | [中文](./Cursor%20%E6%8E%80%E6%A1%8C%E5%AD%90%E4%BA%86%EF%BC%8CGrok%204.5%20%E8%BF%99%E6%AC%A1%E8%A6%81%E4%B8%8A%E5%A4%A9%E4%BA%86%EF%BC%9F.md)

> 日期：2026-07-09

今天早些的时候，SpaceXAI 和 Cursor 一起官宣发布了 Grok 4.5 。

咱就是说，这怎么大模型都赶在一起发布？难道是流量均摊吗？不过话说回来了，感觉 Grok 大模型，国内基本上没啥人用，而且大家基本上都没咋提过，Grok 在大家潜意识里是跟 Gemini 坐一桌的，大家用 Grok 也就是在某知名社交平台贡献了保护费，然后在某社交平台搞搞小 huang 文和小 huang 图啥的，别的没了。

但是这次我看完感觉，可以试试了。

接下来详细给大家聊聊。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709074946016.png" alt="image-20260709074946016" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709075017576.png" alt="image-20260709075017576" style="zoom:50%;" />

Grok 4.5 是 SpaceXAI 为编码、智能任务和知识工作而构建的最智能的模型。这是 SpaceXAI 的最强模型，它是和 Cursor 一起训练而成的。

Grok 4.5 的训练数据集基于**编程、科学、工程和数学**进行训练，Grok 4.5 在实际工程任务中表现出色，在某些测评中超过了 GPT 5.5 xhigh 和 Opus 4.8 max，仅次于刚刚 A 社解封的 Fable 5。

由于原文这块是一个可交互的测评图，不够直观，所以我直接给大家做了个直观的测评图。

（以下模型 effort 默认都是最高档位）

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709075139738.png" alt="image-20260709075139738" style="zoom:50%;" />

Terminal-Bench 2.1 上，Grok 4.5 是 83.3%，基本上就和 GPT-5.5 的 83.4% 齐平，离 Fable 5 的 84.3% 也非常接近。

DeepSWE 1.0 上，Grok 4.5 是 62.0%，比 Opus 4.8 的 55.8% 高，但低于 GPT-5.5 和 Fable 5。

SWE-Bench Pro 上，它是 64.7%。这个成绩能压过 GPT-5.5 和 Composer 2.5，但还打不过 Opus 4.8，更打不过 Fable 5。

所以这组分数支撑不了 Grok 全面登顶这种说法。

但是可以初步说：**Grok 4.5 已经一只脚迈入了第一梯队的门槛**。

（从测评上看是这样的，但实际体验还得各位小伙伴们实测挖掘）

---

文章还提到了 Grok 4.5 的训练过程，Grok 4.5 在数万个 NVIDIA GB300 GPU 上进行了训练，它的训练过程和稳定性技术是专门为了大规模的运行而训练的。

咱就是说，老马果然是算力土豪啊，之前是把 GPU 直接租给了 A 社，现在直接上了数万个 GB300 GPU 参与训练。

别人是拿 token 搞搞自动化流水线，做做 demo ，完成一下公司任务，它这是要拿 token 把人类送上火星啊？

文章提到，除了 token 训练投入了大量的资金之外，还在数据过滤和管理方面投入了大量资金，使得数据混合保持高覆盖率和高信号。

之前发布的 Composer 2.5 是专门为编程领域训练的，这次发布的 Grok 4.5 却在更多领域上进行训练。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709075915254.png" alt="image-20260709075915254" style="zoom:50%;" />

文章还提到，Grok 4.5 具备极强的编程能力，能够胜任从高难度 Rust 和 C/C++ 任务。之前我们用的很多大模型，在 Rust 语言上的训练并不好，所以 Rust 相当于是很多大模型的照妖镜。这次 Grok 4.5 宣布它能够胜任 Rust 和 C/C++ 语言的任务，可以说明 Grok 这次能够直面挑战而不惧了。

----

SpaceXAI 官方稿里给了另一组数字。

Grok 4.5 是 80 TPS，API 价格是每百万输入 token 2 美元、每百万输出 token 6 美元。xAI docs 里也能查到 `grok-4.5`，上下文窗口是 500k tokens。

我把这块也整理成图了。

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/8aa47abb7ba5924c750352b5a7aaab5c68812e27.png" alt="Grok 4.5 价格、上下文和 token 效率" style="zoom: 50%;" />

图中一个刺眼的数字，是 SWE-Bench Pro 的平均输出 token 的对比图。

SpaceXAI 说，Grok 4.5 平均每个任务输出 15,954 tokens，Opus 4.8 max 是 67,020 tokens。也就是官方口径里的 4.2 倍差距。

放在 Coding Agent 里，这是很现实的一件事情，**因为成本是致命的。**

所以这次 Grok 4.5 给我的感觉，不像是跑分又赢麻了。

它好像在说：我不一定每项第一，但我足够强、足够快、足够便宜，能承接大量工程任务。

这让我想到了我上学那会观察到的一个特征：班里的尖子生走的不一定最长远，而班里处于 2 - 5 名的同学，却很容易突然爆发，拉都拉不住的那种。

**这是一个很 Cursor 的目标。**

省流版：有人直接做了总结，Grok 4.5 的优势主要有下面这几点。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709053717141.png" alt="image-20260709053717141" style="zoom: 67%;" />

---

我觉得 Grok 4.5 透露出来的一个信号是，Grok 终于务实了一点。

**AI Coding 的竞争，正在从谁的模型跑分更牛批，变成谁能拿到更真实的工程结果**。

就像老马在帖子上回复的那样，大部分任务，可能不需要 Fable 5 那样的能力。Fable 5 会把 demo 做的更像产品，但是并不是所有的 demo 都是产品，demo 也可以是 demo ，仅此而已。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260709081855127.png" alt="image-20260709081855127" style="zoom:50%;" />

代码能跑起来很简单。

但是遇到问题 Bug 怎么处理、如何验证结果、失败之后怎么办，却越来越向 Harness 靠拢。

Cursor 以前是一个很好用的 AI IDE。

现在看，它也可能是一个模型训练入口。

它能不能上天先不说。

但这次，Grok 至少不像以前那样只是坐在 X 里等人调戏了。

文章参考：

https://x.ai/news/grok-4-5

https://cursor.com/cn/blog/grok-4-5
