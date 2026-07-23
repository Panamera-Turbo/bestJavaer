# Loop 还没玩明白，Graph Engineering 又火了：说白了，就是给 Agent 组个团队

[English](../../en/ai-articles/01-agent-and-coding/graph-engineering-is-already-taking-off.md) | [中文](./Loop%20%E8%BF%98%E6%B2%A1%E7%8E%A9%E6%98%8E%E7%99%BD%EF%BC%8CGraph%20Engineering%20%E5%8F%88%E7%81%AB%E4%BA%86%EF%BC%9A%E8%AF%B4%E7%99%BD%E4%BA%86%EF%BC%8C%E5%B0%B1%E6%98%AF%E7%BB%99%20Agent%20%E7%BB%84%E4%B8%AA%E5%9B%A2%E9%98%9F.md)

> 日期：2026-07-21

7 月 18 日，OpenClaw 作者 Peter Steinberger 在 X 上问了一句：大家还在聊 Loop，还是已经转向 Graph 了？

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260721111956932.png" alt="Peter Steinberger 讨论 Loop 和 Graph" style="zoom:50%;" />

两天后，Codez 写了一篇很长的教程，给出一条从零开始学习 Graph Engineering 的 14 步路线。

我相信很多人的反应跟我一样：**Loop 还没玩明白，怎么又开始画图了？**

先补一句 Loop 是啥：Loop 是让单个 Agent 反复自我检查、自我修正，直到结果达标为止的机制——写完一遍、检查一遍，不行就重来，做到合格为止。下文会反复拿它当对照。

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/3d27d2bbec467a42adea8cd541ece2f618334556.jpg" alt="Graph Engineering 14 步路线图" style="zoom:50%;" />

*图源：[Codez 原文](https://x.com/0xCodez/status/2079165300625330317)*

所以这篇我不按 14 个名词逐一讲——那 14 步里出现的 Node、Edge、Schema、Router、Fan-out/Fan-in，后面都会用大白话覆盖到。我换成一个普通人能听懂的说法：

**Graph Engineering，就是给一群 Agent 分工，规定工作怎么交接、哪里检查、什么时候停。**

先记住这句话，后面的图就没那么吓人了。

## 先把 Agent 想成一个新员工

假设你招了一个新员工，让他每天给你写一份 AI 新闻简报。

最简单的做法，是把所有事都交给他：找新闻、读原文、核对真假、挑重点、写文章、改错字。

这就是大家熟悉的单 Agent。

Prompt 相当于你给他的工作要求。Loop 相当于他写完检查，发现不对再重做，一直做到合格为止。

简单任务做起来没问题，但事情一多，这位员工就开始忙不过来了。他需要一边翻资料，一边记数字，还要考虑文章结构，能记住的上下文越来越满，前面看过的东西也忘得越来越快。

Graph Engineering 做了一件大家看上去应该都知道如何优化的事儿：**别让一个人干这么多事儿了，组个团队。**

有人找资料，有人核对事实，有人写稿，还有人负责挑错。分工明确，最终促成一篇成稿落地。

![Graph、Agent 和 Graph Reasoning 的关系](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/8a82f52a5dd286c95e78afbf67cbf0f4beab8ba8.jpg)

顺带澄清一个容易混淆的词：图里出现的 Graph Reasoning，和本文讲的 Graph Engineering 不是一回事。Graph Reasoning 偏向模型内部的推理结构，Graph Engineering 偏向工程层面的多 Agent 编排。这篇文章讲的是后者。

这张图看起来很复杂。其实下面那些小圆点、小方框，大多都可以理解成不同员工和不同工作。

## Node 是员工，Edge 是交接单

Graph 里最重要的两个词是 Node 和 Edge。

Node，也就是节点。你可以把它理解成一个岗位：资料员、翻译、事实核对员、作者、审稿人。

Edge，也就是边缘。它表示工作从谁手里交到谁手里，以及交过去什么东西。

![节点负责工作，边只传递真实依赖的数据](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a6eec3093e796d8f059b87e4ec71fa85d64937d1.png)

这里有个特别容易踩的坑：做事有先后顺序，但不代表它们存在依赖关系。

比如我让 Agent 总结这份文件，然后查一下北京天气。天气查询根本不需要等待总结结束后方可执行，而是两个任务可以同时开始。

很多 Agent 慢就慢在这里。所有工作被写成 A → B → C → D，前一个任务结束不了，后一个任务绝不开始。

![线性链条剪掉假依赖后，变成可并行的图](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/f90dee9452cfa1118adf957a767b515fca2e713a.png)

再举个更直观的例子：B 和 C 都只需要 A 提供的资料，C 并不需要 B 的结果。那么 A 完成后，就可以同时启动 B 和 C，没必要让 C 排在 B 后面干等。

所以，Graph Engineering 最基础的能力，是看清任务之间真正的依赖关系：**哪些任务需要等待，哪些任务可以同时开工。**

---

任务可以并行以后，问题就从谁等谁，变成了结果怎么交给下一个 Agent。

比如，资料员 Agent 查完资料，只交回来一大段文字。负责写作的 Agent 既找不到原文链接，也分不清哪些是事实、哪些是结论，只能自己再猜一遍。

解决方法，是给每次交接规定一个固定格式。比如资料员必须返回三项内容：标题、原文链接、重要程度。少一项，这次交接就不合格；全部齐全之后，写作 Agent 才继续工作。

技术上，这份格式规则叫作 `Schema`。你可以把它理解成一张统一的交接单。

![节点契约把 Provider、Consumer、Schema 和测试连接起来](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/86d287ae73aaa5fb075020884ff9f13b0d2dc514.jpg)

现在再看 Node 和 Edge 就容易理解了：Node 规定这个 Agent 负责什么，Edge 规定它要把哪些数据交给谁。交接格式越清楚，下一个 Agent 就越容易理解。

![复杂任务图中的数据依赖与执行关系](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/2bd1e378505609963837e40d568b80c650afb2d2.png)

所以，多 Agent 真正难的是提前写清楚每一步的交付物、如何检查、出错后怎么办。

如果这些规则没定好，那么 Agent 数量越多，造成的返工反而越多。

## 最常用的图，其实就是一颗菱形

最常见的 Graph 形状并不复杂。

先把任务拆分，让几个人同时做；做完之后再把结果收回来，去重、筛选；最后交给一个人统一出结果。

![Subagents 与 Agent Teams 的并行方式](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/7b0fa1e3c97561416e2a402fff6252e642e6f77c.jpg)

就拿写这篇文章来举例子。

一个 Agent 读 X 原文，一个 Agent 查 Anthropic 官方文档，另一个 Agent 看最近大家怎么讨论 Graph Engineering。三边可以同时开始。

资料回来后，先去掉重复内容，再交给最终的拟稿人和审核人（也就是我）。所以我不用背着十几个网页工作，我只需要拿到整理好的结果就行了。

![多路结果在屏障节点汇合](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a3655de836c7163522d45979d99edd90f54dff02.jpg)

这就是 Fan-out 和 Fan-in。

Fan-out 是把工作分出去，Fan-in 是把结果收回来。两个动作连在一起，就构成了下面这颗菱形形态。

![Graph Engineering 最常用的菱形拓扑](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/4442b333b5e3a584d42a02f0b04e2d92d710bafe.png)

放到写文章这件事里就很好理解了：先让几个 Agent 同时查资料，再让程序自动去重、分类，最后把整理好的材料交给一个 Agent，由它形成最终结论。

---

前面几个 Agent 已经同时找完资料，程序也完成了去重和分类。但这些材料还不能直接拿来写文章，因为它们可能引用了过期消息，也可能把别人的转述当成官方结论。

所以，最后一个 Agent 拿到材料后，需要先做一轮验收判断：链接能不能打开，数字和日期能不能对上，不同来源有没有互相矛盾，判断之后才能开始写。

技术上，这个负责挑错的角色叫 `Reviewer` 或 `Verifier`。它的工作不是再写一份答案，而是检查前面的答案能不能相信。

但"检查"这件事并不是一个固定的动作，力度也得看事情轻重。

一个普通的观点，让一个 Agent 快速核对就够了；涉及重要数据、安全问题或产品结论时，就要安排几个 Agent 从不同角度交叉检查。决定"这件事该走哪条检查流程"的角色，叫 `Router`。它像一个分诊台，根据重要程度把任务引向不同的边。

![路由节点根据风险等级选择不同的边](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/48776aaaf80ca399917b38999a78631963fba116.png)

如果负责查资料的 Agent 说官方已经确认，验证 Agent 就要找到官方原文；如果只能找到媒体转述，这条结论就要降级，甚至退回去重新查。只有经得住检查的内容，才会进入到文章中。

![多个验证器从不同角度检查同一个发现](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/434577f632d762b0dd1db2b8701a4cee06295fb5.png)

如果 Agent 执行的不是查资料，而是修改代码，还要多做一步隔离：给每个 Agent 一份独立的工作区。否则两个人同时改同一个文件，后面保存的人可能直接盖掉前一个人的成果。

![用 Git worktree 隔离多个并行写入节点](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/60d9fd2c93126b48e0775f9f7482341d1c7c1875.png)

如果检查发现问题后，需要退回前面的 Agent 补资料的阶段，然后再检查一次。这样就形成了一个循环。

![循环必须带反馈、验证与停止条件](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a77a58dd40d7b13a90d8298db1d6e352aea317bd.png)

但是循环必须规定什么时候结束。比如连续两轮没有发现新问题就停止，否则就像老板一直喊再查一遍，Agent 会不停工作，token 也会一直烧。

整套流程说白了就是：**有人找资料，有人整理资料，还有人专门检查资料。检查不通过就退回重做，通过之后才下最终结论。**

---

前面一直在说把任务分给多个 Agent，但有件事不能忽略：每启动一个 Agent，它都要单独读取材料、思考并输出答案，这些操作都会消耗 token。

比如为了写一篇文章，同时叫来十个最强模型查资料，确实可能比一个模型查得更全面，但也相当于花了十倍价钱请了十位专家。并行能节省等待时间，却不会让这十个人免费工作。

省钱的办法，是别让所有工作都交给最贵的模型。提取标题、整理格式、简单分类，可以让便宜的模型完成；判断消息真假、处理冲突、形成最终结论，再交给能力更强的模型。

这就像一个编辑部：整理资料不必总编辑亲自上，真正需要拍板时再找他。

![Claude Code 中为不同节点选择不同模型](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/82e60695a9a9ecec281a5da1ff9ea87ee008e00f.jpg)

除了选什么模型，任务怎么排也会影响速度。

比如十份资料要放在一起去重，那就必须等十个 Agent 全部回来后再开始，像开会一样，人到齐了才能进入下一步。

但如果每份资料可以单独处理，就不用等所有人。第一份回来就先检查第一份，第二份回来再处理第二份，像流水线一样。

![parallel 屏障与 pipeline 流水线的延迟差异](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/e86b0f2b8908c35bd265cadc64eace783febc602.png)

所以，设计一张 Agent Graph，本质上还要算清三笔账：启动多少个 Agent、每个 Agent 使用什么模型、哪些步骤必须互相等待。

**Graph 设计得好，是用更少的钱更快地完成任务；设计得不好，只是让更多模型一起更快地烧 token。**

---

讲到这里，你可能已经发现了一个问题：Graph 确实能让多个 Agent 一起工作，但这张图本身还是要有人设计。

谁去查资料，谁负责验证，哪些任务可以同时开始，哪一步必须等待，最后由谁下结论——以前，这些规则通常要开发者提前写好。

Claude Code 的 Dynamic Workflows 想做的，就是把这部分工作也交给 Claude。

关于 [Claude Dynamic Workflows](https://mp.weixin.qq.com/s/0tbHJ3uH-WXZHlTuZcEX_A) ，你可以阅读这篇文章。

你只需要告诉它最终目标。Claude 会先分析任务，再生成一段 JavaScript 编排脚本。

还是以写文章为例，它可以安排几个 Agent 分头查找原文、官方文档和外部讨论；等资料回来后，让程序去重；再叫验证 Agent 检查来源，最后交给写作 Agent 输出文章。

![Claude Code 通过 ultracode 动态生成 Workflow](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/293e57b52461b68cb2f98f551fcb7497defc3930.jpg)

在 Claude Code 里，你可以直接要求它使用 Workflow，也可以运行 `/deep-research`。打开 `ultracode` 后，Claude 还会先判断当前任务够不够复杂，是否真的值得启动一组 Agent。

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/c93c91ae5db5ad14fe2373fbd22d8c52aa77231d.png" alt="Claude Dynamic Workflows 运行界面" style="zoom:50%;" />

*图源：[Anthropic Dynamic Workflows 官方介绍](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)*

这里有个很容易误解的说法：编排脚本可以做到零模型 token。

它真正的意思是，分发任务、等待结果和合并数据这些管理动作由普通 JavaScript 完成，不需要再调用一次模型。但真正出去干活的每个 Agent，仍然会正常消耗 token。

说白了，**排班表不拿工资，不代表排班表里的员工也不用拿工资。**

截至 2026 年 7 月，Claude 官方文档给出的上限是同时运行 16 个 Agent，单次 Workflow 最多启动 1,000 个 Agent（见 [Claude Code Docs](https://code.claude.com/docs/en/workflows)）。这代表系统能承载多大的任务，并不代表普通任务也应该把人数拉满。

下面这张图，就是原文最后组装出来的一套完整流程。

![一张完整的 Agent Graph：展开、归并、验证与综合](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/fd57f0339b3364eceebcf8fe5242dbef00753ce8.png)

第一眼看上去密密麻麻，拆开后仍然是前面讲过的几件事：先确定任务范围，再分头查资料；用固定格式交接，用程序整理；安排 Agent 验证，最后形成结论；整个过程还要控制停止条件和成本。

Claude 现在可以自动生成这套流程，但仍然要检查三个问题：任务拆得是否合理，该验证的地方有没有验证，启动这么多 Agent 是否值得。也就是说，我们不一定要亲手画出每个节点，但仍然要判断 Claude 安排的这套分工能不能真正完成任务。

---

看到这里，小白不需要马上安装一个 Graph 框架，更不用给每个任务都安排十几个 Agent。

如果只是总结一份 PDF、修改一个标题，交给一个 Agent 从头做到尾，通常更快也更便宜。为了显得高级硬拆成一张图，只会增加等待、交接和出错的机会。

当任务开始出现下面这些情况时，Graph 才真正有用：有几块工作可以同时进行；一个 Agent 已经看不过来；结果必须经过独立检查；整个过程会反复执行很多次。

真要动手，也可以从最简单的一步开始。先让一个 Agent 完成整个任务，找到最慢或者最容易出错的环节；再拆出一个可以并行的分支；确实担心答案不可靠时，再加一个验证 Agent。等流程稳定之后，最后才考虑框架和自动编排。

说到底，**Loop 解决的是一个 Agent 如何反复工作，直到把事情做完；Graph 解决的是多个 Agent 如何分工、交接、检查，以及如何避免把 token 白白烧掉。**

Graph 不是重点，Graph 里每一条箭头为什么存在，才是 Graph Engineering 真正要解决的问题。

---

### 参考资料

- [Codez：Graph Engineering with Claude，14 步原文](https://x.com/0xCodez/status/2079165300625330317)

- [Anthropic：Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

- [Claude Code Docs：Dynamic Workflows](https://code.claude.com/docs/en/workflows)

- [LangGraph 官方文档：Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api)
