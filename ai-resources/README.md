# AI 资源

这些资源来自文章里提到过的 GitHub 项目和日常会用到的工具。这里不做大而全的 awesome list，只保留读者点开后能快速判断用途的项目：它能解决什么问题，为什么值得收藏，以及适合放到什么场景里用。

## Agent 与编程工作流

- [Agent Workflow Kit](https://github.com/crisxuan/agent-workflow-kit)

  推荐理由：把“要不要给项目接入 Agent workflow”这件事做成可评估的流程，适合在真实项目里先看生命周期、协作复杂度和发布风险，再决定要不要引入更重的规约。

- [Codex Usage Estimator](https://github.com/crisxuan/codex-usage)

  推荐理由：适合关心 Codex 用量、token 成本和订阅额度的人。它把模糊的“今天好像用得很多”拆成可观察的本地数据，方便判断 cached input、output 和整体消耗到底在哪里。

- [tiktoken](https://github.com/openai/tiktoken)

  推荐理由：OpenAI 官方 tokenizer。想估算 prompt 成本、理解上下文长度、或者自己做 token 统计工具时，它比拍脑袋数字符可靠得多。

- [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)

  推荐理由：这个仓库很小，但抓住了 AI coding 最容易翻车的几个点：先想再写、保持简单、只做相关改动、围绕目标验证。适合拿来给 coding agent 加一层工程纪律。

- [Buddy Reroll](https://github.com/crisxuan/buddy-reroll)

  推荐理由：偏好玩的小工具，适合观察 AI 产品里的“桌面宠物”和状态入口能怎么玩。它不算基础设施，但能提供一些轻量交互和产品趣味的灵感。

## 工具、资源与知识管理

- [free-for.dev](https://github.com/ripienaar/free-for-dev)

  推荐理由：开发者免费服务清单。做 AI 原型、个人项目、Demo 或小型工具时，经常需要云服务、数据库、监控、CI、邮件、存储等免费额度，这个仓库很适合先查一遍。

- [Layweout](https://github.com/crisxuan/layweout)

  推荐理由：面向公众号发布流程的 Markdown/HTML 排版工作台。适合需要把技术文章、AI 文章稳定复制到公众号编辑器的人，重点不是预览花哨，而是导出后不容易崩。

- [worldmonitor](https://github.com/koala73/worldmonitor)

  推荐理由：一个全球态势监控仪表盘项目，适合看 AI、新闻聚合、地缘信息和实时看板怎么结合。就算不直接部署，也很适合当产品形态参考。

- [RuView](https://github.com/ruvnet/RuView)

  推荐理由：用普通 WiFi 信号做空间感知和存在检测的项目，思路很有脑洞。适合想看看 AI 如何从纯文本工具延伸到物理世界感知的人。

## 本地生成、安全与案例观察

- [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

  推荐理由：本地跑 Stable Diffusion 的经典入口。适合想了解本地 AI 绘图、插件生态、模型管理和 API 调用的人，也是很多图像生成实验的基础工具。

- [openclaw-security-practice-guide](https://github.com/slowmist/openclaw-security-practice-guide)

  推荐理由：面向 OpenClaw 使用场景的安全实践指南。适合关注 Agent 权限、日常巡检、漏洞暴露面和自动化工具安全边界的人。

- [Gpt-Agreement-Payment](https://github.com/DanOps-1/Gpt-Agreement-Payment)

  推荐理由：更适合作为风控和协议链路观察样本，而不是拿来直接使用。它能帮助读者理解支付、OAuth、浏览器环境和平台风控之间的复杂关系，也提醒大家不要把灰色自动化当成稳定方案。
