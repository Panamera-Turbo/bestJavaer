# 今天 Github 看到一个把 AI Agent 工作流打包成操作系统的项目：ECC

[English](../../en/ai-articles/01-agent-and-coding/ecc-packages-ai-agent-workflows-into-an-operating-system.md) | [中文](./%E4%BB%8A%E5%A4%A9%20Github%20%E7%9C%8B%E5%88%B0%E4%B8%80%E4%B8%AA%E6%8A%8A%20AI%20Agent%20%E5%B7%A5%E4%BD%9C%E6%B5%81%E6%89%93%E5%8C%85%E6%88%90%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%9AECC.md)

> 日期：2026-07-01

这次看到的是这个项目：

[affaan-m/ECC](https://github.com/affaan-m/ECC)

![GitHub 项目预览](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-01-github-preview.png)

## 1. 它到底是什么

ECC，全名现在更偏向 Everything Claude Code / Agent Harness Operating System。

简单说，它不是一个单独的聊天机器人，也不是一个只给 Claude Code 用的配置包。

它更像是一套给 AI 编程工具用的工作流底座：把 agents、skills、hooks、rules、MCP 配置、命令兼容层、安全扫描和跨工具安装方式，集中整理到一个仓库里。

项目 README 里写得很直接：它可以用于 Claude Code、Codex、Cursor、OpenCode、Gemini、Zed、GitHub Copilot 等工具。也就是说，它想解决的不是“某一个 IDE 怎么变聪明”，而是“这些 Agent 工具怎么有一套可复用的工作方式”。

![ECC 项目定位图](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-02-hero.png)

截至 2026-07-01 我查看 GitHub API 时，它是 MIT 协议，主语言标记为 JavaScript，约 224K stars、34K forks，当天还有 push 记录。

## 2. 它解决什么麻烦

现在用 AI 编程工具，最常见的问题不是“模型不会写代码”。

更麻烦的是：每个项目都要重新告诉它规则，每次长会话都容易丢上下文，代码审查、测试、文档、排查构建错误这些流程也经常散在不同提示词里。

ECC 的思路是把这些东西沉淀成可复用组件。

比如：

- `skills` 负责具体工作流，比如 TDD、代码审查、安全检查、文档查找。
- `agents` 负责把任务分给更专门的子代理。
- `hooks` 负责在工具调用前后做提醒、校验或记录。
- `rules` 负责长期生效的工程规范。
- 安装器和插件清单负责把这些组件放进不同 harness 里。

![ECC 精简指南](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-03-shortform-header.png)

这对经常使用 Claude Code、Codex 或 Cursor 的人会比较有感。

因为真正影响体验的，往往不是一次提示词写得多漂亮，而是能不能把一套工作习惯稳定带到下一个项目里。

## 3. 核心看点

第一个看点是它的组件数量。

当前 README 里写的是：67 个 agents、277 个 skills、92 个 legacy command shims。这个数量已经不是“几个示例 prompt”，而是一个长期维护的工作流库。

第二个看点是跨工具支持。

ECC 早期名字更像 Everything Claude Code，但现在明显在往 “agent harness” 方向走。也就是同一套规则、技能和安装逻辑，不只服务 Claude Code，还要兼容 Codex、Cursor、OpenCode 等环境。

第三个看点是 hooks。

Hook 的作用是让 Agent 在某些节点自动做事。比如执行命令前提醒、工具调用后检查、会话结束时保存摘要。它不是让模型“记住所有东西”，而是把记忆和校验变成工作流的一部分。

![PostToolUse Hook 示例](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-04-posttooluse-hook.png)

第四个看点是它没有只停在本地配置。

仓库里还连接了 ECC Tools GitHub App、AgentShield、安全指南、成本控制、dashboard GUI、安装诊断和卸载流程。也就是说，它在尝试覆盖从本地使用到团队仓库治理的完整链路。

## 4. 为什么值得看

ECC 值得看的地方，不在于它能不能替你一键写完所有代码。

它更值得看的，是它把“怎么让 AI Agent 长期可用”这件事拆得很细。

比如 README 里反复提醒：插件安装和手动安装不要叠加。因为叠加之后容易出现重复 skill、重复 hook、重复运行时行为。

这个提醒很朴素，但也说明作者真的遇到过这些问题。

![Claude 插件界面示例](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-05-plugins-interface.jpeg)

它还专门强调 MCP 不要全部打开。

很多人一开始会把各种 MCP 都装上，结果工具列表膨胀，上下文窗口被占掉，Agent 反而变慢。ECC 的指南里给了一个很实用的建议：可以配置很多 MCP，但真正启用的要少。

这类细节，比单纯堆功能更有参考价值。

## 5. 怎么用起来

如果只是想试试，README 推荐先走 Claude Code 插件路径：

```bash
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

如果只想要规则、agents、commands 和核心 skills，不想让 hooks 介入太多，可以走 minimal profile：

```bash
git clone https://github.com/affaan-m/ECC.git
cd ECC
./install.sh --profile minimal --target claude
```

Windows 上也有 PowerShell 版本：

```powershell
.\install.ps1 --profile minimal --target claude
```

如果你已经通过插件安装，README 明确建议不要再跑 full installer。

更稳的做法是：插件负责 skills、commands 和 hooks；rules 只复制自己真正需要的目录，比如 `rules/common` 和 `rules/typescript`。

![会话记忆与持久化示意](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-06-session-storage.png)

它也提供了一个咨询式命令，用来先问应该装什么组件：

```bash
npx ecc consult "security reviews" --target claude
```

这个设计挺适合组件很多的项目。先问计划，再安装，比上来全量复制更安全。

## 6. 适合谁，以及先注意什么

ECC 更适合三类人。

第一类，是已经重度使用 Claude Code、Codex、Cursor 或 OpenCode 的开发者。

如果你每天都在和 Agent 一起写代码，ECC 里的 skills、agents、hooks 和 rules 很容易给你提供参考。

第二类，是在团队里推动 AI 编程规范的人。

它不是简单给一个“提示词大全”，而是把审查、测试、文档、安装、状态、卸载、GitHub App 这些环节都放进同一个体系里，适合拿来研究团队落地方式。

![并行工作流示意](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-07-parallel-workflow.png)

第三类，是关注 Agent 安全的人。

ECC 里有独立安全指南和 AgentShield 相关内容，会讨论攻击向量、沙箱、净化、CVE 和审计流程。对经常让 Agent 读仓库、跑命令、改代码的人来说，这部分比“又多了几个命令”更重要。

![ECC 安全指南](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260701-affaan-m-ecc-08-security-guide.png)

不过它也不是所有人都要立刻装。

如果你只是偶尔问 AI 几个代码问题，ECC 的组件密度可能会显得太重。更好的方式是先读它的 shortform guide 和 README，挑出其中一小部分实践，比如 rules 拆分、hook 校验、session summary，再决定要不要安装。

另外要注意官方来源。

README 特别提醒，只从 GitHub 仓库、npm 包 `ecc-universal` / `ecc-agentshield`、GitHub App、插件标识 `ecc@ecc` 和官网 `ecc.tools` 这些官方渠道安装。第三方搬运源不要直接用。

今天就先聊到这里。
