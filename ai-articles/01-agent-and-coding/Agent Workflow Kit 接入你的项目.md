# Agent Workflow Kit 接入你的项目

> 日期：2026-05-21

最近使用 Codex 接手项目的时长大大增加了。

我自己做了很多项目，但做着做着往往就成了玩具，然后告别历史舞台。

但是我觉得这个过程是必要的，除非天选之子，否则大部分人有所成就的过程都是踩着 garbage 上去的。

但是这个过程，其实有可以缩短路径的空间。

我最近就在研究如何让 AI 把项目写的更完善，更像那么回事。

不同的项目是否适用不同的规约，changelog 如何写，artifact 如何做等。

不同的项目对工作流的运用如何，单人项目，短期项目是否适合融入 Agent workflow 。

不同的项目该用哪种 workflow，如何保证 agent.md 不会串线，遵照你的主规约？

如果项目里同时出现 OpenSpec、Superpowers、gstack 这些东西，到底谁说了算？

这些都是需要考虑的问题。

![image-20260521093654698](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260521093654698.png)

之前爽用 AI 的时候，发现真夯啊，AI 一天，人间一年。

后来发现，这是我作为碳基生命出现的幻觉。

所以你看，不仅硅基生命有幻觉，碳基生命的幻觉更是多之又多。

有点跑偏题了。

---

最近一直在研究的一个路线是：Superpowers + OpenSpec + gstack ，是否是一个完备的工作流模式。

这个组合看似很丝滑（项目风格规约+文档先行+不同 agent 模式的 skill 技能），但是它的基础上是属于项目偏好型的，并不适合所有项目。

于是我就有了一个想法，做一个 AI 能看懂的文档，拿到一个项目来判断其是否适合接入 Agent workflow。

直接拿去喂 AI ，它会直接根据项目偏好来判断用哪种不同的 kit 。

想法不能光想。我把它做出来了，叫 Agent Workflow Kit。

https://github.com/crisxuan/agent-workflow-kit

![image-20260521093529414](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260521093529414.png)

它不是又一个工具，它是一份给 AI 看的文档，外加一套打包好的 skill。

它不替你做决定，它帮你判断。

核心就一句话：先评估，再接入。

不是所有项目都配得上一套重流程。一个一次性脚本，你非要给它上 OpenSpec，那不叫规范，那叫行为艺术。

![image-20260521093611504](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260521093611504.png)

所以它干的第一件事，是让 AI 给你的项目打分。

它会从八个维度打分：生命周期、用户、UI、发布风险、安全、外部平台、测试难度、协作，每项 0 到 2 分，满分 16。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260521093841112.png" alt="image-20260521093841112" style="zoom:50%;" />

然后按分数告诉你：这项目该用 Level 几的 workflow，要不要规格层，要不要执行纪律，要不要专家审查。

下面是一个完整的中型 Web App 项目的工作流程。

![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260521094606666.png)

![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260521094630324.png)

说白了，它不让你为了“显得专业”去堆流程。

（当然确实大多数项目头重脚轻，轻轻说的）

---

那它怎么接入你自己的项目？

最糙的办法：把仓库里那份中文文档整个喂给 AI，问它“我这项目该用哪种 workflow”。

讲究一点，用它打包好的 skill，一句话就够：

```text
使用 $agent-workflow-kit-zh-cn 评估这个仓库，并推荐合适的 AI 工作流级别。
```

AI 会先把你的仓库翻一遍，再吐回来一份 Decision：项目类型、风险分、建议级别、该建哪些文件、验证命令是什么，理由是什么。

你看完点头，它才动手写 AGENTS.md。

你不点头，它就只是个秘书。

有一句话挺好的，有事儿秘书干。。。。。。

它也不会自作主张帮你装工具、开 hook、push 代码，这些都得你先点头。

毕竟它再聪明，出了事背锅的还是你。

还有一点，我自己挺在意的。

它不绑定任何工具。

Superpowers、OpenSpec、gstack 这些，在文档里全都只是“示例”，不是“你必须装”。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260521094038035.png" alt="image-20260521094038035" style="zoom:50%;" />

我不想做一个你得按我的来的东西。

我想做的是一个你先想清楚自己到底需要什么的东西。

或者说你的 Agent 知道你想要什么的东西。

---

最后，说回开头。

它不会让你的玩具项目起死回生。该成玩具的，还是会成玩具。

但它至少能让 AI 在帮你堆 garbage 的时候，堆得有那么点章法。

让你下次踩着往上走的那堆，台阶高一点。

这就够了。

欢迎大家提出 issue、PR。
