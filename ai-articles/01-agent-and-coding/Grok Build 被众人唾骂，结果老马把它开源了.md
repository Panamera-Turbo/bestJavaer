# Grok Build 被众人唾骂，结果老马把它开源了

[English](../../en/ai-articles/01-agent-and-coding/grok-build-was-criticized-then-open-sourced.md) | [中文](./Grok%20Build%20%E8%A2%AB%E4%BC%97%E4%BA%BA%E5%94%BE%E9%AA%82%EF%BC%8C%E7%BB%93%E6%9E%9C%E8%80%81%E9%A9%AC%E6%8A%8A%E5%AE%83%E5%BC%80%E6%BA%90%E4%BA%86.md)

> 日期：2026-07-22

Grok Build 前两天属实是站在风口浪尖上了。

先给大家先复盘一下整个事情。

一份针对 `grok 0.2.93` 的[流量分析](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547)显示，Grok Build 在测试中上传了整个 Git 仓库，其中包括未被 Agent 读取的文件和 Git 历史；研究者还在上传内容里找到了测试用的 `.env`  字符串。

这份分析确实证明了数据传输、服务端接收和存储，但**没有证明 xAI 一定拿这些数据训练了模型**。

云端 AI 编程工具把任务需要的代码发给模型，这很正常。

争议点在于，它传出去的代码范围远超当前的任务需要，而且当时的安装和快速上手文档没有把整库上传机制讲明白。

这才是令大家闹心，唾骂的地方。

SpaceXAI 随后宣布把 Grok Build CLI 里的 `/privacy` 作为回应。这个命令用于查看或切换隐私与数据保留状态。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716081611791.png" alt="SpaceXAI 对 Grok Build 数据问题的回应" style="zoom:50%;" />

*图源：SpaceXAI 官方回应截图*

当你在命令行敲入 `/privacy` 的时候，界面会明确标注代码不会被用于模型训练。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716081959745.png" alt="Grok Build CLI 的 privacy 状态" style="zoom:50%;" />

*图源：Grok Build CLI 截图*

这里要给大家提个醒了：**不会用于训练，不等于数据完全不会离开本机。**

云端模型想理解代码，总要接收一部分上下文。前面的流量分析也发现，在当时被测试的版本里，关闭 Improve the model 后，整库上传仍然会发生。

---

然后，在今天 7 月 15 日，SpaceXAI 宣布把 Grok Build 开源，同时重置所有用户的使用额度。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716082108557.png" alt="SpaceXAI 宣布开源 Grok Build" style="zoom:33%;" />

*图源：SpaceXAI 官方账号截图*

老马也正面回应了这个事情。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083825776.png" alt="Elon Musk 对 Grok Build 隐私问题的回应" style="zoom:50%;" />

*图源：Elon Musk 公开回应截图*

这次开源，看着像是让广大开源爱好者参与进来。从另一个角度看，它也明显带着危机回应和信任修复的色彩。

因为挨骂和公关修复的时间离得太近了。

默认保留关闭、历史数据删除、源码公开、额度重置，几个措施同时出现了。说这和前面的隐私争议完全没关系，我反正是不信的。

---

很多人看到 Grok Build 开源，很容易理解成 Grok 模型也开了。还是不一样的。

[官方仓库](https://github.com/xai-org/grok-build)开放的是 Grok Build 的 Rust CLI/TUI、Agent 运行时和工具框架，第一方代码采用 Apache 2.0 许可证。**Grok 4.5 的模型权重、训练代码和 xAI 云端服务没有随之开放。**

![Grok Build GitHub 仓库与许可证](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716082850739.png)

*图源：Grok Build 主页*

严格来说，这是真开源了。Apache 2.0 允许使用、修改、分发和做商业衍生。

而且它不只是把一个空壳扔出来。你可以从源码构建 CLI，查看文件读取、命令执行、沙箱、工具调用和上传相关实现。

官方文档还支持配置自定义模型和 `base_url`，所以你能把这个 Harness 接到其他 API，或者接到兼容接口的本地推理服务。

我看了一下 Grok Build 的开源仓库，官方已经写得很明确：

![Grok Build 仓库贡献政策](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083124561.png)

*图源：Grok Build GitHub 仓库截图*

- 仓库目前只有一次历史提交；
- 官方明确表示不接受外部 Pull Request 和主动提交的安全补丁；
- GitHub 上还没有与源码仓库对应的正式 Release；
- 开源代码是否与用户下载的官方二进制逐字对应，还需要可复现构建、版本标签和签名机制来证明。

官方在 [CONTRIBUTING.md](https://github.com/xai-org/grok-build/blob/main/CONTRIBUTING.md) 里直接写的很明确。

![image-20260716095816563](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716095816563.png)

所以我理解 Grok 现在的路线是这样的：你可以看、可以本地编译、可以 Fork，也可以基于 Apache 2.0 做自己的版本；

但是官方暂时不准备跟社区一起开发主仓库。

这也解释了为什么仓库没有开放常见的公共 Issue 和 PR 流程。

安全问题有单独的 `SECURITY.md` 通道，普通功能建议和代码贡献暂时进不了主仓库。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716100013245.png" alt="image-20260716100013245" style="zoom:50%;" />

说我得难听一点：代码给你看，Fork 也随你便，但官方暂时不想收你的 shit code 。。。

---

Grok Build 这次开源也不是先例，前面已经有 [Codex CLI](https://github.com/openai/codex) 和 [Gemini CLI](https://github.com/google-gemini/gemini-cli)。它们同样没有开放背后的模型权重，开放的都是 Agent CLI 和运行框架。

**Codex CLI：**

![Codex CLI GitHub 仓库](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083543195.png)

*图源：OpenAI Codex GitHub 仓库截图*

**Gemini CLI：**

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083626387.png" alt="Gemini CLI GitHub 仓库" style="zoom:50%;" />

*图源：Google Gemini CLI GitHub 仓库截图*

区别主要在社区治理。

Codex 和 Gemini CLI 都保留了完整的公开提交历史，也开放 Issue、Pull Request 和讨论区。

Gemini CLI 的 README 甚至明确邀请社区提交代码改进。

也就是说，你该提 Issue 提 Issue，该提 PR 提 PR。

至于 A 社的 Claude Code，源码确实也被人扒出来了，我相信基本上大家也是人手一份了。

所以这次 Grok build 确实开源了，但目前来看，他们并不想做社区。

不过我看到某知名社交平台上几乎全是吹的，鲜有人提到官方不接受公共 PR 这件事。这是我看到少数直接点出问题的评论。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716091457691.png" alt="关于 Grok Build 不接受外部贡献的评论" style="zoom:50%;" />

*图源：社交平台公开评论截图*

---

如果你用 Cursor，这几天确实是甜蜜时刻了。

Cursor 直接把模型使用量翻倍了。Grok Build 这边随后选择直接重置用户额度。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716090038075.png" alt="Cursor 提供 Grok 4.5 双倍用量" style="zoom:50%;" />

老马这一套操作确实听起来很诱人，又是把源码开放，又是重置额度的，而且 Cursor 这边直接把额度 double 了。

所以我更加确切地相信，这次开源确实是一场公关上的胜利。它迅速的转移了公众的注意力。

所以这次开源最大的价值，我认为其实是把一部分信任从公司承诺变成了可检查的源码。

但它既不能抹掉此前已经抓到的上传行为，也不能单独证明当前官方二进制已经彻底停止整库上传了。
