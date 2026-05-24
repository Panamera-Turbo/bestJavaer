# DeepSeek 输入 `<think>` 就能偷看别人对话？这事儿先别急着下结论

> 日期：2026-05-19

今天看到一张截图，用户只给 DeepSeek 发了一个东西：

`<think>`

结果它直接开始输出一段莫名其妙的内容，像是在接着别人的任务往下写。更吓人的是，那段内容不是普通回答，而是带着很强的 Prompt 味儿：

“我们被要求生成一个详细的对话……”

![image-20260519151635644](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260519151635644.png)

还有一些很 x 很 xx 的对话，真的不忍直视。

这玩意第一眼看过去，确实挺像后台把别人的对话给拎过来了。

如果这是真的，那就是 P0。

这不是小 bug，不是体验问题，是用户隔离炸了。说白了，就是你打开一个 AI 聊天框，结果它把隔壁老王刚才说的话泄露了。

但是我看完之后，第一反应不是“DeepSeek 已经实锤泄露”，而是另一个更技术一点的判断：

**这更像是特殊 token 把对话模板打乱了，模型开始沿着训练时见过的格式瞎续写。**

注意，我说的是“更像”，不是给 DeepSeek 洗地。

这两个判断差别很大。

一个是产品后台把真实用户数据串线了。

另一个是模型被你塞了一个内部路标，然后开始生成一段看起来像真实对话的东西。

前者是数据库和权限灾难，后者是模型工程和输入边界问题。都不该发生，但严重程度不是一回事。

## `<think>` 不是普通文字

很多人看到 `<think>`，会觉得这不就是一个标签吗？

真不是。

对推理模型来说，`<think>` 很可能不是“用户想让它思考一下”，而是模型内部格式的一部分。

DeepSeek 官方 API 文档里，推理模型会把思考内容放在 `reasoning_content`，最终回答放在 `content`。

再看 DeepSeek-R1 在 Hugging Face 上的 tokenizer 配置，它的 chat template 里会在 assistant 回复前拼出类似 `<｜Assistant｜><think>\n` 这种结构。

这就很关键了。

正常情况下，`<think>` 应该由服务端在正确的位置塞进去，用户不应该直接碰到它。用户输入框里出现这个东西，就像你在普通搜索框里敲了半截 SQL：

```sql
UNION SELECT ...
```

它不一定真能打穿数据库，但这个输入从一开始就不该被当成普通文本。

AI 聊天看起来像你一句我一句，底层其实不是这样。底层是把 system、user、assistant 这些角色，用一堆特殊 token 拼成一长串文本，再丢给模型续写。

大模型本质上还是续写器。

你把内部 token 塞进去，它就可能误以为“哦，现在进入某个内部阶段了”，然后开始补全它在训练里见过的相似格式。

这时候它吐出来的东西，就很容易像另一段对话。

## 为什么它看起来像“别人说过的话”

因为模型最擅长的事，就是生成“像真的一样”的东西。

尤其是聊天模型，它训练时见过大量这类结构：

用户：请你写一个故事。

助手：我会创建一个故事……

用户：帮我分析一下这个问题。

助手：我们需要先理解……

当你只输入一个 `<think>`，模型拿到的是一个很奇怪的半截上下文。它不知道你到底要干啥，但它知道在类似位置后面，经常会出现推理、复述任务、分析需求、生成方案。

于是它开始补。

补着补着，就补出一段“我们被要求生成一个详细的对话”。

这不是它真的去数据库里把某个用户的聊天记录查出来了，而是它在学过的对话里找最像的续写路线。

早在 2023 年，Google DeepMind、UW、Cornell、CMU、UC Berkeley、ETH 的研究者就做过训练数据抽取研究：一些大模型在特定攻击提示下，会吐出训练数据里的原文片段。

也就是说，大模型确实可能记住一部分训练材料，也确实可能在异常输入下把这些东西吐出来。

但是这跟“正在读取其他在线用户的历史对话”不是一回事。

一个是模型参数里的记忆或拟合。

一个是产品后端的数据串线。

看起来都像“泄露”，但技术路径完全不同。

## 那是不是就没事了？

也不是。

我反而觉得，这里最容易被忽略的一点是：

**即使它不是跨用户泄露，用户能在聊天框里触发这种内部格式错乱，本身就说明产品边界没处理干净。**

一个成熟的 AI 产品，至少要挡住三件事。

第一，用户输入不能直接污染 chat template。你不能让用户随便输入 `<｜User｜>`、`<｜Assistant｜>`、`<think>`、`</think>` 这种内部控制符，然后模型还真按这个节奏跑。

第二，思考内容和最终回答要隔离清楚。DeepSeek 文档里也写得很明确，`reasoning_content` 和 `content` 是并列字段，后续多轮对话里怎么处理也有规则。开发者如果自己拼上下文，把上一轮的思考内容乱塞回去，很容易制造奇怪行为。

第三，训练数据和用户数据要有治理边界。DeepSeek 隐私政策里写了，它可能收集用户的 text input、prompt、uploaded files、feedback、chat history 等内容，也写了这些个人数据会在中国境内处理和存储。

这不是阴谋论，这是它自己政策里写的。

所以你不能因为这次 `<think>` 大概率不是后台串线，就得出“放心随便用”的结论。

这就像你家门锁这次不是被撬开的，而是你没关严实。

不是同一种事故，但都说明你家安全设计有问题。

---

我看到很多人拿截图直接下结论，说这就是其他用户对话。

这个判断有些武断了。

要证明跨用户泄露，至少要有更硬的证据。

比如，输出里出现了某个真实用户独有的信息，而且这个信息能被当事人确认。

比如，不同账号、不同网络、不同时间，能稳定打到同一类后台数据，而不是每次随机生成一段看起来像对话的文本。

再比如，输出里带着真实会话 ID、时间戳、账号标识、上传文件名这类后端痕迹。

只有这些证据出现，才能更接近“用户数据泄露”这个结论。

截至 2026 年 5 月 19 日，我能看到的公开材料更像另一种情况：多人复现了异常输出，但异常输出是否来自真实用户聊天，还没被定死，也就是说，你没有明确的证据确实证明数据泄露。

这也是我为什么不愿意直接写“DeepSeek 泄露其他用户对话”。

技术文章最怕这个。

这太容易带节奏了。

---

这件事最值得警惕的，不是 DeepSeek 这一个截图。

而是很多人到现在还把 AI 聊天框当成普通搜索框。

普通搜索框里，你输入一句话，它去查网页。

AI 聊天框不是。

它背后有 system prompt，有对话模板，有上下文拼接，有推理字段，有缓存，有训练数据记忆，还有一堆你看不见的产品工程。

你输入的每一个字，不一定只是在“提问”，也可能在改变模型理解当前对话结构的方式。

这就是为什么 prompt injection、special token injection、context contamination 这些东西会变得越来越重要。

以前写 Web 安全，最怕用户输入进了 SQL、HTML、Shell。

---

所以，这次 DeepSeek 输入 `<think>` 后吐出陌生对话风格内容，我目前更倾向于判断：

它不是已经实锤的跨用户聊天记录泄露。

它更像是 special token 触发了异常续写，模型开始沿着训练时见过的聊天/推理格式往下编。

但是，这不代表没问题。

恰恰相反，这说明 AI 产品还有一块很容易被普通用户忽略的攻击面：模型内部格式和用户输入之间的边界。

以前我们说，不要相信用户输入。

现在得补一句：

**也不要相信用户输入里的 token 只是普通文字。**

AI 时代的安全坑，正在从数据库、接口、权限，慢慢长到 Prompt 和上下文里。



参考资料：

- DeepSeek API Docs：Reasoning Model，`reasoning_content` 与 `content` 的输出结构。https://api-docs.deepseek.com/guides/reasoning_model
- DeepSeek API Docs：Thinking Mode，多轮对话中 `reasoning_content` 的处理规则。https://api-docs.deepseek.com/guides/thinking_mode
- DeepSeek-R1 tokenizer_config，chat template 中包含 `<｜Assistant｜><think>\n`。https://huggingface.co/deepseek-ai/DeepSeek-R1/blob/main/tokenizer_config.json
- Hugging Face：Chat templates 说明，聊天消息会被转换成带 control tokens 的 token 序列。https://huggingface.co/docs/transformers/chat_templating
- DeepSeek-V3 GitHub issue #1314：用户仅输入 `<think>` 后触发无关物理问题回答。https://github.com/deepseek-ai/DeepSeek-V3/issues/1314
- Scalable Extraction of Training Data from Production Language Models，训练数据抽取研究。https://arxiv.org/abs/2311.17035
- DeepSeek Privacy Policy，关于输入、聊天历史、训练用途和存储位置的说明。https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html
