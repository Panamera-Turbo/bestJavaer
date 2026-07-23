# 离谱，GPT-5.6 竟然在后台执行了 rm -rf

[English](../../en/ai-articles/01-agent-and-coding/gpt-5-6-ran-rm-rf-in-the-background.md) | [中文](./%E7%A6%BB%E8%B0%B1%EF%BC%8CGPT-5.6%20%E7%AB%9F%E7%84%B6%E5%9C%A8%E5%90%8E%E5%8F%B0%E6%89%A7%E8%A1%8C%E4%BA%86%20rm%20-rf.md)

> 日期：2026-07-16

大家好，我是 cxuan。

昨天 GPT 5.6 正式公开，某知名社交平台上全是牛批、卧槽、吊打 Fable 5，很多号主也在跟着吹。

但我昨天其实就说过：我要给 GPT 5.6 浇盆冷水。我预感它效果没那么好。

[都在吹 GPT 5.6，但我可能得泼点冷水了。](https://mp.weixin.qq.com/s/sylMeZQM_DX2_SOsAM_s3g)

结果发布才一天多，风向就开始变了。

---

昨天我没收到 Sol 的推送，所以先测了 Terra。

发布时官方口径大概是：Terra 能力和 GPT-5.5 差不多，更省 token。我之前也按这个理解它——**Terra 是 5.5 的省流版**。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711122054159.png" alt="image-20260711122054159" style="zoom:50%;" />

然后体验过程里，首当其冲就撞上两个低级问题。。。。。。

一个是模型跑完了，界面上几乎看不到任何结果。

一个是流式渲染之后，英文夹着中文一起喷出来，读起来像一坨泔水。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711123204082.png" alt="image-20260711123204082" style="zoom:50%;" />

我还分不清，这是 ChatGPT Codex 客户端的问题，还是模型本身的问题。

但结论很简单：**体验有些差。**

---

前天 Grok 4.5 刚出来的时候，我写过一篇，说这次 Grok 4.5 效果其实不错。

[Cursor 掀桌子了，Grok 4.5 这次要上天了？](https://mp.weixin.qq.com/s/uibtdVGdjCg6z9qELv1zpQ)

对 GPT 5.6，我又泼了冷水。

**结果这两个观点，现在都在应验。**

一边是 Grok 4.5 被拿去和第一梯队认真比较。

一边是 GPT 5.6 的热度，正在从吊打一切变成寥寥无几的在吹。

不是说 5.6 完全不能用。是在说：**发布日的情绪，和真正上手后的体感，不是一回事。**

### OpenAI 把重置玩明白了

现在 OpenAI 倒是很清楚一件事情了：额度重置，比再发一篇评测稿更管用。

邀请重置，改 bug 重置，奥特曼打个不会赢的赌输了重置，甚至官方毫无理由直接下场送重置。

属实把重置玩明白了。

但是这招的副作用也很明显：用户会逐渐把重置当成产品体验的一部分，而不是福利。

哪天 OpenAI 如果不送重置了之后呢？

用户可是没有忠诚度，哪个模型好用哪个，哪个模型省 token 用哪个，哪个模型性价比高用哪个。

比如我之前天天吹 GPT 5.5 ，现在不也是在上手用上了 Grok 4.5 么。。。

你要是天天靠补额度维稳，那产品本身一定哪里有问题。

### A 社也坐不住了

GPT 5.6 这波，连一毛不拔的 A 社都跟着重置额度了。

Fable 5 本来是 7 月 7 号结束订阅内的促销额度，后来延到 7 月 12 号；5.6 一公开，A 社又把 5 小时和 weekly limit 全量重置了一遍。

Tibo 直接在官方帖子下面说：他闻到了一股恐惧的气味。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711133940980.png" alt="image-20260711133940980" style="zoom:50%;" />

这话当然带点阴阳了。

不过可以确定的是，A 社确实感觉到了一些压力。否则也不会在 GPT 5.6 刚发布就选择重置额度。

Fable 5 的延迟下线也能证明这一点。

---

我仍然记得当初用 GPT 5.5 时候的惊艳，但这次 GPT-5.6 Sol，吐槽的人不少。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/175fb822cf58282570f809d8d0b9bf87.png" alt="175fb822cf58282570f809d8d0b9bf87" style="zoom:50%;" />

Simon Willison 写过 GPT-5.6 家族（Luna / Terra / Sol）的梳理，也承认 Sol 很能干，但在他常做的复杂编码任务上，**目前还没觉得它比 Fable  更好**。

另外一个更刺眼的点是：官方爱打的 Agents’ Last Exam 上 Sol 很亮眼，但在 SWE-Bench Pro 这种更硬的编码评测上，Fable 5 自报大约 80%，Sol 大约 64.6%。OpenAI 还专门发文质疑 SWE-Bench Pro 有大量坏题——这个动作本身，也说明编码榜单已经开始互撕了。

但是，更严重的是 Matt Shumer。

他测试 GPT-5.6 Sol 时，最终执行了类似 `rm -rf /Users/mattsdevbox` 的操作，把 Mac 上的文件全删光了。

（Matt Shumer 就是写下那篇《有许多大事儿即将发生》的那位）

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711125211332.png" alt="image-20260711125211332" style="zoom:50%;" />

出了这件事后，我对 GPT-5.6 Sol 的信任直接掉了一截。

Theo（t3.gg）也吐槽了一个很工程的问题：把 gpt-5.6-sol 设成 `ultra` 之后，它下面的所有 subagent 也会继承 `ultra`，造成无缘无故的 token 燃烧，而且还无法单独的把 subagent 的 effort 换成 medium。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711131208541.png" alt="image-20260711131208541" style="zoom:50%;" />

因为很多人第一天就会把 effort 拉满，一拉满就疯狂烧 token ，然后回头说 Sol 太贵了。。。

这老哥还有一个帖子更直接，说感谢大厂互卷，让 A 社感到恐惧，于是继续延长 Fable 5 的下线节奏。

我甚至觉得，Fable 5 未必会在 12 号就按原计划切到纯 credits。

现在先立个 flag，看看会不会打脸。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711134359615.png" alt="image-20260711134359615" style="zoom:50%;" />

---

我现在真实感觉到现在的测评，其实看一看就行。

真正决定你换不换默认模型的，还是这几件事：

会不会稳定产出结果，会不会乱删文件，会不会无故烧额度，会不会无缘无故降智，会不会有额外的惊喜。

我不是说 GPT 5.6 没有实力，OpenAI 在 agent 长程任务、工具调用、多 agent 编排上确实很突出。

但发布后的第一波真实反馈里，**稳定性和可控性**，已经压过了再高 10 分的兴奋。

这也是为什么我更愿意先看 Grok 4.5 这类够强、够快、够便宜的选手，而不是只盯着发布会里最顶的那一档。

按照现在的趋势，顶级模型不会用来单纯的干活，而是会整理需求、做设计、拿方案，具体干活，要交给工程能力强，token 消耗没那么快的模型。

---

##

如果你实在想用 GPT 5.6，**先把 effort 调到 medium，别一上来 ultra 拉满。**

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260711134122300.png" alt="image-20260711134122300" style="zoom:50%;" />

这和我之前写过的一篇，以及现在圈里不少人的观点，基本一致：xhigh / ultra 很容易过度思考，还特别废 token，性价比不高。

除非你在做又难又大的攻城略地型任务，否则一般任务里，medium 往往更划算。

[还在用 Codex 把 xhigh 拉满跑？](https://mp.weixin.qq.com/s/F9BDZm2JhjvpytyQ2yH4oQ)

---

说到底，GPT 5.6 现在最大的问题，是新版 Codex 搭配着 GPT 5.6 还没稳定，bug 比较多，而且大家对 GPT 5.6 的期待值有些过高，导致与实际情况有些差距，所以我感觉这次 OpenAI 还是有些着急了。

我现在的态度很简单：Sol 继续观察，Terra 先当省流备胎（其实并不省），Fable 5 额度能蹬上的话还是最佳选择，Grok 4.5 很值得尝试。

现在最应该做的事儿就是等着 GPT 6.x 的发布了。
