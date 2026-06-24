# 幽默，一个 Github 名字叫“马尾辫”，但是他给你省了 80% 的 token

这两天我注意到一个 Github，刚看到的时候，还是有点搞笑的。

![image-20260622094701408](https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260622094701408.png)

看到这个 readme ，你第一反应是不是会想到又是哪个大聪明在恶搞。

或者觉得这又是一个什么恶趣味的 Github 。

其实不是，这是一个正经的能帮助大家减少 Token 消耗的 Github。

它的介绍是这么说的

>Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

让你的 Agent 一样像个成熟的高级开发人员一样，最好的代码就是你不写代码。

你现在看到这个介绍，会不会想起来你接触的高级开发，他们发量有些不足，有的甚至很极客，带着眼镜，不修边幅。

他们在公司的时间比版本控制的历史还长。

**但是当他们坐在电脑前面的时候，你用 50 行的代码被他用一行就搞定了。**

这个“马尾辫”老哥的形象，在项目里也描述得活灵活现。

> Long ponytail. Oval glasses. Has been at the company longer than the version control. You show him fifty lines; he looks at them, says nothing, and replaces them with one.

长马尾，椭圆眼镜，工龄比公司的版本控制系统还老。你给他看五十行代码，他瞅一眼，啥也不说，反手给你换成一行。**Ponytail 干的事，就是把这位老哥的灵魂塞进你的 AI Agent 里。**

---

然后 Repo 给你展示了一个 benchmark 效果。

（我实际看了一下，现在的 benchmark 测试比前两天的不一样了）

如果只看早期 benchmark，最吸引人的数字是：代码少 80%-94%，成本低 42%-75%，速度快 3-6 倍。

现在它写的是：

**平均少 54% 代码，最高少 94%；成本低 20%；速度快 27%；安全率 100%。**

![Ponytail 最新 agentic benchmark](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/github/ponytail-20260622/ponytail-benchmark-agentic-20260622.svg)

很多开源项目如果拿到了一个好看的数字，会恨不得把它钉死在 Readme 首页。

但 Ponytail 的作者承认旧 benchmark 有问题，然后重新做了一套更接近真实 Agent 使用场景的测试。

这说明这个 Github ，不像是一个专门用来刷数据、洗评分的 Github。

---

不过，重新做 benchmark 测试，其实是有缘由的。

Ponytail 一开始的 benchmark，是单次生成。

也就是给模型一个 prompt，让它吐一段答案，然后数代码行。

这种 benchmark 的测试跟我们真实用 Coding Agent 的方式不太一样。

真实情况里，Agent 不是只在聊天框里回你一段代码。

它会进项目目录，看文件，改代码，留下一个 git diff。

所以有人在 issue #126 里提出了一个质疑。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260622104109774.png" alt="image-20260622104109774" style="zoom:50%;" />

单次生成里的基准线太容易“话多”，模型会写解释、写注意事项、写多个方案，于是最后统计“回答里的代码行数”，很容易把基准线放大。

还有一个更关键的问题：

如果只是让 Agent 少写，会不会把安全校验也省掉？比如路径拼接、SQL 参数、用户输入、token 校验，这些东西不能因为 Ponytail 的懒得做而省略这些步骤。

这个质疑确实也很合理。

不过，Ponytail 的作者没有忽略这个质疑，他重新做了一个 agentic benchmark。

这次不是单次补全，这次是让真实 Claude Code session 去改一个真实开源仓库。

仓库选的是 `tiangolo/full-stack-fastapi-template`，一个 FastAPI + React 项目。

模型是 Haiku 4.5，任务是 12 个真实 feature ticket，每组跑 4 次。

最后统计的对象也换了，直接看 Agent 留下来的 `git diff` 新增行数。

而且它还加了安全任务。

让生成出来的函数去跑路径穿越、SQL 注入、伪造 token、异常 CSV、配额耗尽这类对抗输入。

这才像一个正常人类会关心的 benchmark。

我把官方 benchmark 里的 setup 翻成中文，大概是这样。

![Ponytail agentic benchmark 中文整理](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@9378c29/github/ponytail-20260622/ponytail-agentic-setup-cn-v3-20260622.png)

*整理依据：[Ponytail agentic benchmark](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)。*

安全任务这块也可以翻成一张图。

![Ponytail safety benchmark 中文整理](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@9378c29/github/ponytail-20260622/ponytail-agentic-safety-cn-v3-20260622.png)

*整理依据：[Ponytail agentic benchmark](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/results/2026-06-18-agentic.md)。*

---

我觉得新数据更可信了。

12 个 feature task 平均下来：

| 方案                   | 代码行数 | tokens | 成本 | 时间 | 安全 |
| ---------------------- | -------: | -----: | ---: | ---: | ---: |
| Ponytail               |     -54% |   -22% | -20% | -27% | 100% |
| caveman                |     -20% |    +7% |  +3% |  +2% | 100% |
| YAGNI one-liner prompt |     -33% |   -14% | -21% | -30% |  95% |

这里有两个点很重要。

第一个点，Ponytail 不是在所有任务里都减少了 90%，它在“Agent 容易过度设计”的地方容易努力过度，比如日期选择器。

原因很简单，浏览器原生就有 `<input type="date">`、`<input type="color">`、`<input type="file">`。

Agent 如果不被约束，很容易自己写一套组件。

Ponytail 会先问一句：平台自己有没有？

有，那就别写了。

第二个点，它在没什么可省的地方，也不会硬省。

现在它告诉你：有些任务能省很多，有些后端任务省不了。

这就比较真实了。

---

### 这个项目如何做的

这个项目它不是个插件，也不是个新工具，**它就是一套“决策规则集”**。

在 AI 动手写代码之前，必须要先过一下他的六类核心判断：

![image-20260618101100160](https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260618101100160.png)

1. **这东西需要存在吗？** → 不需要就直接跳过（YAGNI 原则）
2. **标准库能搞定吗？** → 能用就用
3. **平台原生功能有吗？** → 有就直接用
4. **已安装的依赖里有吗？** → 有就别重复造轮子
5. **能一行搞定吗？** → 就写一行
6. **以上都不行？** → 才写最少量的必要代码

进过这六步判断，你的 Agent 根本水不了。

然后这个判断下方还有一行小字，这行小字容易注意到

>“懒惰，并不是疏忽；信任边界验证、数据丢失处理、安全性和可访问性永远不会被忽视”

![image-20260622172026056](https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260622172026056.png)

---

## 具体怎么用

大家更关心的，其实是它装完之后到底怎么用。

我把它分成三种情况说。

第一种，你用 Codex 。

官方 README 里把 Claude Code、Codex、GitHub Copilot CLI 的安装方式都列出来了。

![Ponytail 官方安装说明截图](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/github/ponytail-20260622/ponytail-install-official-20260622.png)

*图源：[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) README。*

先在终端里加 Ponytail marketplace：

```bash
codex plugin marketplace add DietrichGebert/ponytail
codex
```

然后进入 Codex 之后，打开 `/plugins`。

选择 Ponytail marketplace，安装 Ponytail。

装完之后再打开 `/hooks`。

这里会看到它的两个 lifecycle hooks。

不要直接闭眼信任，先看一下它要做什么，再点 trust。

它的作用是让 Ponytail 在新 session 里自动注入规则，并追踪当前模式。

如果你用的是 Codex desktop app，需要安装后重启一下 app。

在 Codex 里，一般可以这样用。

普通小改动，直接让它带 Ponytail 干活：

```text
Use Ponytail mode for this task.
只改这个 bug，优先用现有代码和标准库，不要新增依赖。
```

如果它已经给了一个很大的 diff，不要着急让他继续改。

可以先用

```text
@ponytail-review
```

这个命令看的不是 bug。

它专门看“哪里写多了”。

比如手写了标准库已有的东西、为了一个实现抽了 interface、为了一个调用者加了 factory、为了一个永远没人改的值加了 config。

它最后会给你一个 delete-list。

第二种，你用 Claude Code。

Claude Code 的安装方式：

```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

装完以后，Ponytail 默认是 full 模式。

你可以用 `/ponytail` 看当前状态，也可以手动切：

![Ponytail 官方命令表截图](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/github/ponytail-20260622/ponytail-commands-official-20260622.png)

*图源：[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) README。*

一般来说 ponytail 分为下面几种模式：

```text
/ponytail lite
/ponytail full
/ponytail ultra
/ponytail off
```

`lite` 更像提醒。

它会告诉你更懒惰一点的方案，但不会强行替你决定。

`full` 是我觉得最适合日常使用的模式。

它会按照上面提到的六步决策法。这是他的那条决策流程：先标准库，再平台原生，再已有依赖，最后才写代码。

`ultra` 就比较牛批了。

这个模式适合那种你打开项目看到一堆 wrapper、factory、abstract class，血压已经飙升的时候。

但我不建议你把 ultra 当默认模式。

它适合清理过度工程，不适合所有开发场景。

第三种，你不想装插件。

那就用 instruction 文件。

Ponytail 的 agent portability 文档里，把不同工具该放哪个文件也列出来了。

![Ponytail agent portability 官方截图](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/github/ponytail-20260622/ponytail-adapters-official-20260622.png)

*图源：[Ponytail agent portability](https://github.com/DietrichGebert/ponytail/blob/main/docs/agent-portability.md)。*

比如在项目根目录放 `AGENTS.md`。

Ponytail 仓库本身就提供了一份 `AGENTS.md`，你可以复制到自己的项目里。

Codex、VS Code Codex extension、CodeWhale 这类能读 `AGENTS.md` 的工具，就适用于这条规则。

Cursor 可以放到 `.cursor/rules/`。

Windsurf 可以放到 `.windsurf/rules/`。

Cline 可以放到 `.clinerules/`。

GitHub Copilot editor 可以放到 `.github/copilot-instructions.md`。

这种方式没有插件的模式切换和 hooks，但最核心的规则能生效。

对很多项目来说，这已经够用了。
