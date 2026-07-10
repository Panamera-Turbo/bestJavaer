# Claude Code 源码分析第一篇：Claude Code 为什么不是一个聊天机器人，而是一个 Agent 系统

[English](../../en/ai-articles/01-agent-and-coding/claude-code-from-source-why-it-is-an-agent-system-not-a-chatbot.md) | [中文](./Claude%20Code%20%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E7%AC%AC%E4%B8%80%E7%AF%87%EF%BC%9AClaude%20Code%20%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E6%98%AF%E4%B8%80%E4%B8%AA%E8%81%8A%E5%A4%A9%E6%9C%BA%E5%99%A8%E4%BA%BA%EF%BC%8C%E8%80%8C%E6%98%AF%E4%B8%80%E4%B8%AA%20Agent%20%E7%B3%BB%E7%BB%9F.md)

> 日期：2026-06-25

这篇开始，我们正式来啃 `Claude Code from Source`。

这本书挺有意思。

作者不是在写一篇“Claude Code 好牛逼”的介绍文，而是把 Claude Code 早期 npm 包里 source map 暴露出来的 TypeScript 源码做了一遍架构拆解。

注意，是架构拆解，不是源码搬运。

原站自己也说了：书里不保留 Claude Code 原始源码，代码块都改成了伪代码，重点是分析架构、模式和工程取舍。

所以我这个系列也按这个方式来：

**按原文顺序逐节翻译和解释，但不贴原始源码，不做源码复刻。**

第一篇讲的是整本书的总纲：

`The Architecture of an AI Agent`。

也就是：一个 AI Agent 到底是怎么被组织起来的。

![Claude Code from Source 封面](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/cover.jpg)

*▲ 图源：Claude Code from Source 首页封面截图*

---

## 你到底在看什么

原文一开头就把传统 CLI 和 Agentic CLI 做了一个区分。

传统的 CLI ，其本质上就是一个函数，比如 `grep` ，你执行 grep 的时候不会要同时运行 `sed`，

>需要解释一下 grep 和 sed 都是什么。

简单说，`grep` 是用来“找文本”的命令。

比如你有一个很大的日志文件，想找里面所有包含 `error` 的行，就可以用 `grep "error" app.log`。

它不会理解你的业务，也不会判断下一步该干什么。

它只做一件事：从输入里把匹配的文本找出来。

`sed` 则更像一个“文本流水线编辑器”。

它可以把一段文本里的某些内容替换掉，比如把所有 `foo` 改成 `bar`。

但它也一样，不会自己突然说：“我觉得你这个日志格式不太对，我顺手帮你重构一下。”

这就是传统 CLI 的关键：工具很强，但边界很清楚。

你让它干什么，它就干什么。

它不会越过你的命令去自己规划。

`curl` 也不会下载完东西以后，再根据下载的内容进行补全。

**传统的 CLI 很简单，就是一条命令，执行一个操作，获得确定性的输出。**



这里需要绘制一幅图。

![传统 CLI 工作方式](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@dabed70/claude-code-from-source/ch01/ch01-00-traditional-cli.png)

*▲ 传统 CLI 的核心契约：用户给明确命令，程序执行固定逻辑，最后返回确定性输出。*



但是 Agentic CLI 把这套方式全打碎了。

你不再是需要使用传统的 CLI 的方式了。

Agentic CLI 会接受人类自然语言的描述，根据自然语言的提示，来决定使用哪些工具。并且按照具体的情况要求顺序的调用这些工具，获得结果，然后进行循环，直到任务完成或用户停止为止。



绘制一张图。

![Agentic CLI 工作方式](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@dabed70/claude-code-from-source/ch01/ch01-00-agentic-cli.png)

*▲ Agentic CLI 的重点不是执行单条命令，而是围绕模型形成“决策、调用工具、观察结果、继续决策”的循环。*



由此我们可以给 Agentic CLI 下一个定义：

Agentic CLI 不是一串固定的指令，而是围绕着大语言模型运转的一个循环，模型会在运行时自己生成下一步指令。

而 Claude Code 就是 Anthropic 对这个想法的生产级实现。



Claude Code 是一个 TypeScript 单体应用，它将终端变成一个由 Claude 驱动的完整开发环境。目前 Claude Code 的使用人数也有几百万了，这意味着 Claude Code 背后的每个架构决策，都会产生实际的影响。



这第一节的内容，会抽象出来**六种心智模型**，后面的每一章，都是围绕着这六种心智模型来展开，都是把每一种心智模型进行放大。





## 六个核心抽象

原文说，Claude Code 建立在六个核心抽象之上。

剩下那些东西，比如几百个工具函数、终端渲染器、Vim 模拟、成本追踪，本质上都是在服务这六个抽象。

![Claude Code 六个核心抽象](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-01-six-key-abstractions.png)

*▲ 图源：Claude Code from Source 第一章交互图截图*

这六个东西分别是：

Query Loop、Tool System、Tasks、State、Memory、Hooks。

我一个个说。

### 1. Query Loop：整个系统的心跳

原文把 `query.ts` 称为整个系统的 heartbeat。

心跳这个词很准。

因为 Claude Code 最核心的事情，就是一轮一轮地跑：

调用模型；

接收流式响应；

收集工具调用；

执行工具；

把工具结果追加回消息历史；

然后继续下一轮。

所有入口最终都会走到这个循环里。

普通 REPL 是它。

SDK 调用是它。

sub-agent 是它。

无头模式 `--print` 也是它。

原文提到一个实现细节：这个循环是一个 async generator。

这个词可能有点抽象。

简单说，它不是一次性跑完再返回结果，而是一边运行，一边不断把消息吐出去。

外面的 UI 用 `for await` 这种方式慢慢消费。

这带来几个好处。

第一，天然支持背压。

UI 如果消费不过来，生成器就会暂停，不会疯狂往外喷事件。

第二，取消比较干净。

用户中断的时候，可以让生成器收尾，而不是在一堆 callback 里乱飞。

第三，结束原因是类型化的。

它不是含糊地说“结束了”，而是明确告诉你为什么结束：

正常完成、用户取消、token 预算耗尽、stop hook 拦截、最大轮次到了，或者不可恢复错误。

这个设计非常工程。

很多 Agent demo 看起来能跑，但最怕问一句：

“它为什么停？”

答不上来。

Claude Code 这里把“停止原因”变成了系统的一等公民。

这就是生产系统和 demo 的区别。

### 2. Tool System：模型真正伸出去的手

第二个抽象是工具系统。

原文说，工具就是 Agent 在世界里能做的任何事。

读文件、跑 shell、编辑代码、搜索网页，都是工具。

这句话看起来简单，但里面藏了很多工程复杂度。

Claude Code 里的工具不是普通函数。

每个工具都要描述自己的身份、输入 schema、执行逻辑、权限要求、渲染方式。

更关键的是，工具还要声明自己能不能并发。

比如读文件通常可以并行。

但写文件、跑会修改状态的命令，就不能随便并行。

原文还提到，工具执行器会把工具调用拆成可并发和必须串行的批次。

更狠的是，有些并发安全的工具，不需要等模型整段回复生成完，就可以先开始跑。

这就是流式工具执行。

比如模型刚吐出一个 `Read` 调用，系统就可以先去读文件。

模型还在继续说，文件结果可能已经回来了。

这里我感觉挺关键。

很多人做 Agent 的时候，会把工具当成“模型回答之后的后处理”。

Claude Code 不是这么想。

它把工具执行和模型流式输出揉在了一起。

这就是为什么 Agent 看起来像一个活的系统，而不是一个问答脚本。

### 3. Tasks：后台任务和 Sub-agent

第三个抽象是 Tasks。

Tasks 是后台工作单元，主要用来承载 sub-agent。

原文说它有一个状态机：

`pending -> running -> completed | failed | killed`

也就是等待、运行、完成、失败、被杀掉。

重点在于 `AgentTool`。

当 Claude Code 派生一个 sub-agent 的时候，它不是写一套特殊分支逻辑，而是启动一个新的 `query()` 生成器。

这个新的 query loop 有自己的消息历史、自己的工具集合、自己的权限模式。

所以 sub-agent 本质上不是一个“轻量回调”。

它是一个小的 Agent。

这就给 Claude Code 带来了递归能力：

一个 Agent 可以委托给另一个 Agent，另一个 Agent 还可以继续委托。

但这里也很危险。

因为一旦 sub-agent 能自己做决定、自己跑命令、自己改文件，系统就可能失控。

所以后面权限系统里会出现一个很重要的 `bubble` 模式。

意思是：sub-agent 遇到危险动作，不能自己批准，要往上冒泡，让父 Agent 或用户决定。

我的理解是：

**能力可以下放，责任不能下放。**

这是多 Agent 系统里很重要的一条线。

### 4. State：两层状态

第四个抽象是状态。

原文说 Claude Code 有两层状态。

第一层是一个可变单例 `STATE`。

它保存的是会话级基础设施状态，比如当前工作目录、模型配置、成本追踪、遥测计数、session ID。

大概 80 个字段。

这层状态启动时设置，后面直接改，不做响应式。

第二层是一个极简响应式 store。

它长得像 Zustand，用来驱动 UI。

里面放消息、输入模式、工具审批、进度条这些会频繁变化的东西。

这个分层很朴素，但很对。

不是所有状态都应该 reactive。

基础设施状态变化少，读得多，不需要每改一下就触发 UI 重绘。

UI 状态变化快，必须响应式。

很多项目一上来喜欢把所有东西都塞进响应式 store，最后订阅关系乱成一团。

Agent CLI 更不能这么搞。

因为它同时在跑模型、跑工具、渲染终端、追踪成本、处理用户输入。

状态冷热不分，后面一定炸。

### 5. Memory：跨会话的上下文

第五个抽象是 Memory。

原文说 Claude Code 的记忆有三层。

项目级：仓库里的 `CLAUDE.md`。

用户级：`~/.claude/MEMORY.md`。

团队级：通过符号链接共享。

每次会话开始时，系统会扫描这些 memory 文件，解析 frontmatter，再让 LLM 判断哪些记忆和当前对话相关。

这个设计非常有意思。

很多人以为 Agent 记忆就是“长上下文”。

但 Claude Code 的做法更像是：把长期规则文件化。

项目约定、架构决策、调试历史、个人偏好，不是只躺在聊天记录里，而是写成能打开、能编辑、能版本管理的文件。

这比“模型好像记得”靠谱多了。

聊天记录太长，人不会读，模型也容易抓错重点。

文件不一样。

人能改，Agent 能读，团队能同步。

我现在越来越觉得，Agent 记忆最好的形态不是神秘数据库，而是可维护文档。

### 6. Hooks：生命周期拦截器

第六个抽象是 Hooks。

原文说，Claude Code 的 hooks 会在 4 类执行类型、27 个不同事件上触发。

这 4 类包括 shell 命令、一次性 LLM prompt、多轮 Agent 对话、HTTP webhook。

Hooks 可以做很多事：

阻止工具执行；

修改输入；

注入额外上下文；

甚至直接短路整个 query loop。

更有意思的是，权限系统本身也部分通过 hooks 实现。

比如 `PreToolUse` hook 可以在交互式权限提示出现之前，就先拒绝某个工具调用。

这点非常关键。

因为 LLM 决策是不稳定的。

你不能指望它每次都记得所有工程规矩。

Hooks 的意义就是把一部分“必须发生”的事，从模型的自由发挥里拿出来，放进确定性系统。

比如：

提交前必须跑测试；

危险命令必须拦截；

某些目录不能改；

某些输出必须追加审计日志。

这类东西别靠 prompt。

靠 prompt 就是祈祷。

## 黄金路径：从按下回车到看到输出

原文接着讲了 Claude Code 的 golden path。

也就是一次请求从输入到输出，完整走过系统的路径。

例子很简单：

用户输入：“给登录函数加错误处理”，然后按下回车。

![Claude Code Golden Path](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-02-golden-path.png)

*▲ 图源：Claude Code from Source 第一章交互图截图*

这条路径大概是这样：

用户在 REPL 输入任务。

REPL 把消息交给 Query Loop。

Query Loop 调用模型 API。

模型流式返回内容和工具调用。

如果模型要读文件、改文件、跑命令，就交给 StreamingToolExecutor。

工具系统执行动作。

工具结果再被塞回消息历史。

Query Loop 带着新上下文再次调用模型。

直到模型不再请求工具，或者外部条件让它停下。

原文提醒这里有三个点要注意。

第一，query loop 是 generator，不是 callback chain。

REPL 是用 `for await` 从里面拉消息。

这意味着 UI 消费速度会自然影响生成速度。

它不是事件总线里那种“你发你的，我处理我的”。

这种写法更适合终端产品。

终端 UI 本来就容易被输出刷爆，天然背压很重要。

第二，工具执行和模型流式输出有重叠。

`StreamingToolExecutor` 不会傻等模型整段回复结束。

只要看到一个并发安全的工具调用，就可以先执行。

比如读文件。

模型还在继续生成，文件可能已经读完了。

原文把这叫 speculative execution，投机执行。

当然也有代价。

如果后面模型输出改变了前面的意图，这个结果可能要丢掉。

但这种情况比较少。

换来的好处是速度。

第三，整个循环是可重入的。

工具结果不是走一个单独的“处理阶段”。

它就是消息历史的一部分。

模型看到工具结果以后，继续决定下一步。

所以 Agent 的核心不是“调用一次模型 + 调一次工具”。

而是模型、工具、消息历史之间反复循环。

这就是 Agent 运行时。

## 权限系统：没有它，这玩意就是安全事故

原文到权限系统这一节，语气明显严肃起来了。

Claude Code 能在你机器上跑任意 shell 命令。

它能改文件。

能开子进程。

能发网络请求。

能改 git 历史。

如果没有权限系统，这就是安全灾难。

![Claude Code 权限解析](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-03-permission-resolution.png)

*▲ 图源：Claude Code from Source 第一章交互图截图*

原文列了七种权限模式，从最放开到最保守大概是这样：

| 模式 | 含义 |
| --- | --- |
| `bypassPermissions` | 全部放行，不做检查，主要是内部或测试用 |
| `dontAsk` | 都允许，但仍然记录，不弹用户确认 |
| `auto` | 用一个轻量 LLM 分类器判断该放行还是拒绝 |
| `acceptEdits` | 文件编辑自动批准，其他会产生副作用的动作继续询问 |
| `default` | 标准交互模式，每个关键动作让用户确认 |
| `plan` | 只读模式，所有修改动作都拦住 |
| `bubble` | sub-agent 不自己决定，把权限请求往父级冒泡 |

这里最值得看的是 `auto`。

原文说，auto 模式会跑一个单独的轻量 LLM 调用。

它会看对话记录和工具输入的压缩表示，然后判断这个动作是否符合用户原始意图。

比如用户让它“修复测试”，读文件、跑测试、改相关文件可能合理。

但如果它突然要删目录、改 SSH 配置、访问奇怪路径，就应该被拦下来。

这就是半自动模式的关键。

它不是完全信任模型，也不是每一步都烦用户。

而是用一个额外分类器做中间层。

但这也带来一个问题：

这个分类器本身也是 LLM。

所以它不是绝对安全边界，只能算风险过滤器。

真正危险的动作，还是应该交给确定性规则和用户确认。

sub-agent 默认走 `bubble` 也很关键。

因为 sub-agent 不能自己批准自己的危险动作。

它要向上层 Agent，最后向用户申请。

这解决的是一个很现实的问题：

主 Agent 可能看起来很乖，但它派出去的子 Agent 如果能偷偷跑危险命令，那整个系统还是不安全。

所以多 Agent 里权限必须能向上冒泡。

不是“谁执行谁负责”。

而是“谁授权谁负责”。

## 多 Provider 架构

接着原文讲了 Multi-Provider。

Claude Code 可以通过四种不同基础设施路径访问 Claude。

直接 API、AWS Bedrock、Google Vertex AI、Foundry。

但这些差异对系统其他部分是透明的。

![Claude Code Multi-Provider 架构](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-04-multi-provider-architecture.png)

*▲ 图源：Claude Code from Source 第一章交互图截图*

关键点在于 Anthropic SDK 给不同云厂商都做了 wrapper。

这些 wrapper 对外暴露同一套接口。

`getAnthropicClient()` 这个工厂函数读取环境变量和配置，决定当前该用哪个 provider，然后构造对应 client。

从这以后，`callModel()` 和其他调用方都只把它当成一个通用 Anthropic client。

Query Loop 不需要关心你走的是 Direct API 还是 Bedrock。

Provider 选择在启动时完成，结果存进 `STATE`。

后面的 Agent Loop、工具系统、权限系统，都不管 provider。

这点很工程。

模型供应商路径应该是配置问题，不应该污染 Agent 主循环。

国内做 Agent 的时候也一样。

今天接通义，明天接 DeepSeek，后天接自建模型。

如果你的业务逻辑里到处都是 provider 特判，后面一定会很痛苦。

上层应该只关心：

我发消息；

你返回流；

你告诉我有没有工具调用。

至于底下走哪条基础设施链路，不应该让 Agent Loop 知道太多。

## 构建系统：讽刺的是，泄露点就在这里

这一节讲构建系统。

Claude Code 既是 Anthropic 内部工具，也是公开 npm 包。

同一套代码服务两种分发形态，靠编译期 feature flags 控制哪些东西会被打进去。

原文给了一个模式，大意是：

```ts
const module = feature("SOME_FLAG")
  ? require("./some/internal/module")
  : null
```

这里的 `feature()` 来自 `bun:bundle`，也就是 Bun 的打包 API。

在构建时，每个 feature flag 会被解析成布尔字面量。

如果 flag 是 false，打包器的 dead code elimination 会把对应 `require()` 整段删掉。

也就是说，模块不会加载，不会进 bundle，也不会发布。

原文还解释了为什么这里用 `require()`，而不是 `import()`。

因为被 flag 包起来的动态 `require()` 可以被打包器完整消掉。

而动态 `import()` 返回 Promise，打包器通常必须保留。

这块很细，但挺值得看。

因为它说明 Claude Code 不是简单靠运行时判断来隐藏内部功能。

它是在构建期就把某些路径裁掉。

但讽刺就在这里。

早期 npm 包发布出来的 source map 里带了 `sourcesContent`。

这个字段包含原始 TypeScript 源码。

也就是说，feature flags 确实把运行时代码裁掉了，但 source map 把源码内容留下来了。

这就是 Claude Code 源码能被公开读到的原因。

这里有个很现实的工程教训：

**发布包安全，不只看 runtime bundle，还要看 sourcemap、metadata、调试产物。**

很多团队觉得“代码没打进产物就行”。

不一定。

调试产物可能比运行时代码还诚实。

## 这些组件怎么连起来

原文接着把六个抽象连成了一张依赖图。

![Claude Code 组件连接图](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@45e45a2/claude-code-from-source/ch01/ch01-05-how-the-pieces-connect.png)

*▲ 图源：Claude Code from Source 第一章交互图截图*

Memory 会作为系统提示词的一部分喂给 Query Loop。

Query Loop 驱动工具执行。

工具结果再作为消息回到 Query Loop。

Tasks 是递归的 Query Loop，只是有隔离的消息历史。

Hooks 会在定义好的位置拦截 Query Loop。

State 被所有模块读写，同时响应式 store 把状态桥接到 UI。

原文说，Query Loop 和 Tool System 之间的环形依赖，是这个系统最核心的特征。

模型生成工具调用。

工具执行，产出结果。

结果进入消息历史。

模型看到结果，决定下一步。

这个循环持续下去，直到模型不再生成工具调用，或者 token 预算、最大轮次、用户取消之类的外部约束把它终止。

这一段其实就是 Agent 的本质。

不是“模型 + 工具”这么简单。

而是模型和工具之间形成了一个闭环。

没有闭环，工具只是插件。

有了闭环，才叫 Agent。

原文最后说，后续章节会沿着这条 golden path 展开：

第二章讲系统怎么启动到能执行这条路径；

第三章讲两层状态架构；

第四章讲 API 层；

后面每一章继续放大这条路径的一个局部。

所以第一章就是地图。

后面才是进洞。

## 我们能学什么

最后一节叫 Apply This。

原文把 Claude Code 的架构总结成几条可以迁移到自己 Agent 系统里的模式。

我按原意整理一下，再加一点我的理解。

### 1. Agent Loop 用 async generator，不要乱堆 callback

原文建议，把 Agent Loop 写成 async generator，而不是 callback 或 event emitter。

原因前面讲过：

消费者按自己的节奏拉消息，天然背压；

用户取消时，可以干净停止；

结束原因可以变成类型系统的一部分。

这解决的是 callback Agent 里最烦的问题：

你不知道循环什么时候算结束，也不知道为什么结束。

很多 Agent demo 写到后面就一堆事件：

`onModelChunk`、`onToolCall`、`onToolResult`、`onError`、`onDone`。

看着很灵活，实际上很容易乱。

Generator 的好处是，它把“运行中输出”和“最终停止原因”放在同一个控制结构里。

### 2. 工具要自描述

每个工具都应该声明自己的并发安全性、权限要求、渲染行为。

不要让一个中央 orchestrator 记住所有工具的特殊规则。

否则工具越多，中央调度器越像上帝对象。

新加一个工具，就要到处改。

自描述工具的好处是线性扩展。

加第 N+1 个工具，不应该影响前 N 个工具。

这点对 Agent 平台特别重要。

因为 Agent 的工具一定会越来越多。

文件工具、shell 工具、浏览器工具、MCP 工具、数据库工具、公司内部工具。

如果工具接口一开始不稳，后面就是灾难。

### 3. 基础设施状态和响应式状态要分开

原文建议，不是所有状态都要触发 UI 更新。

会话配置、成本追踪、遥测，放普通可变对象里就行。

消息历史、进度条、审批队列，放响应式 store。

问题在于访问模式不一样。

有些状态启动时改一次，后面读一千次。

有些状态每秒都在变，而且 UI 必须跟着动。

把这两类混在一起，就是给自己找事。

我感觉这条看起来不性感，但很值钱。

因为 Agent 产品的复杂度不是只来自 AI。

还来自 UI、流式输出、工具进度、用户审批、取消恢复。

状态层如果设计乱了，Agent 再聪明也没用。

### 4. 做权限模式，不要散落权限判断

原文建议，定义一小组命名权限模式，比如 plan、default、auto、bypass。

所有权限决策都通过模式解析。

不要在工具里到处写 `if (isAllowed)`。

这解决的是权限执行不一致的问题。

如果每个工具自己判断权限，最后一定有漏网之鱼。

统一模式链的好处是，你只要知道当前模式，就能判断系统整体安全姿态。

这对 Agent 特别重要。

因为 Agent 的风险不是“它会说错话”。

而是“它会做错事”。

会做事，就必须有权限边界。

### 5. Sub-agent 应该复用同一个 Agent Loop

最后一条是递归 Agent 架构。

原文建议，sub-agent 不要写特殊代码路径。

它应该是同一个 Agent Loop 的新实例，只是有自己的消息历史。

权限向上冒泡。

这样 sub-agent 能继承主 Agent Loop 的所有保证。

错误处理、工具执行、权限系统、终止状态都一致。

如果 sub-agent 是另一套逻辑，就会出现非常隐蔽的问题：

主 Agent 一种行为；

子 Agent 另一种行为；

某些错误只在子 Agent 出现；

某些权限只在主 Agent 生效。

这类 bug 最难查。

所以递归复用同一个 loop，是很重要的工程简化。

## 这一章真正讲的是什么

看完第一章，我觉得它真正想说的不是 Claude Code 有多复杂。

而是：

**AI Agent 的复杂度，不在模型回答，而在运行时。**

聊天机器人只要把输入变成输出。

Agent 要把目标变成一串动作。

动作会产生副作用。

副作用会改变世界状态。

世界状态又会影响下一步动作。

所以 Agent 必须有循环、工具、权限、状态、记忆、hooks、终止条件。

少一个都不稳。

这也是为什么现在很多所谓 Agent demo 看着很热闹，一到真实项目就不行。

因为 demo 解决的是“模型能不能想出下一步”。

生产系统解决的是：

下一步能不能安全执行；

执行结果能不能被正确反馈；

失败能不能恢复；

用户能不能理解发生了什么；

成本会不会爆；

权限会不会越界；

上下文会不会漂。

Claude Code 这类产品真正值得学的地方，就是它把这些脏活累活都系统化了。

所以这篇的结论很简单：

**不要把 Claude Code 当聊天框看。**

它是一个跑在终端里的 Agent runtime。

模型只是大脑。

工具是手。

权限是刹车。

状态是神经系统。

Memory 是长期经验。

Hooks 是工程纪律。

Query Loop 才是心跳。

下一篇我们继续看第二章：启动流程。

一个 Agent 再聪明，如果启动慢、初始化乱、配置读取散、信任边界没立住，用户还没开始让它干活，它就已经输了。

---

参考资料：

- Claude Code from Source, Chapter 1: The Architecture of an AI Agent
  https://claude-code-from-source.com/ch01-architecture/
- Claude Code from Source 首页
  https://claude-code-from-source.com/
- Anthropic Claude Code Docs: Overview
  https://docs.anthropic.com/en/docs/claude-code/overview
