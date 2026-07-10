# 今天 Github 看到一个让 AI 编码 Agent 持续工作的项目：loop-engineering

[English](../../en/ai-articles/01-agent-and-coding/loop-engineering-turns-ai-coding-agents-into-recurring-workers.md) | [中文](./%E4%BB%8A%E5%A4%A9%20Github%20%E7%9C%8B%E5%88%B0%E4%B8%80%E4%B8%AA%E8%AE%A9%20AI%20%E7%BC%96%E7%A0%81%20Agent%20%E6%8C%81%E7%BB%AD%E5%B7%A5%E4%BD%9C%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%9Aloop-engineering.md)

> 日期：2026-07-08

最近在GitHub上看到一个项目，琢磨了好几天，觉得挺有意思。

它不教你怎么写提示词，也不教你怎么调模型参数。

它做的是另一件事：**让AI编码Agent像定时任务一样，持续、稳定地帮你干活。**

![GitHub 项目预览](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-01-github.png)

项目叫 **loop-engineering**，6,415 Star，MIT协议，主语言JavaScript。

------

## 它到底是个啥？

一句话说：**一套让AI编码Agent持续运行的实践方案 + 配套工具。**

它不是新模型，不是聊天界面，也不是IDE插件。

它是一套“运行规则” + 几个npm命令。

支持 **Grok、Claude Code、Codex、Opencode**，也给Cursor、Windsurf、OpenClaw准备了接入示例。

![Loop Engineering 标志](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-02-loop-engineering.svg)

“循环”这个词，可以理解成一个持续运行的工作流：

> **定时找任务 → Agent处理 → 验证结果 → 决定继续、提交、还是喊人**

有点像给Agent装了一个“定时闹钟”，到点就起来干活，干完检查，检查完要么交差要么重来。

------

## 解决了什么麻烦？

现在大家用编码Agent，通常是这样的：

> 发现问题 → 敲提示词 → 等结果 → 发现不对 → 再敲一次 → 再等……

偶尔用用还行。

但问题是，有些活是**每天都要干的**：

- 检查CI有没有挂
- 整理新Issue
- 跟进PR状态
- 更新变更日志

这些事让真人干，烦。让Agent干，又不知道怎么让它“定时上班”。

**loop-engineering的思路是：把这些重复工作拆成一条流水线。**

> 定时触发 → 筛选任务 → 读取状态 → 创建独立worktree → Agent执行 → 验证 → 人工确认

![一个完整循环的流程](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-07-loop-engineering-5.svg)

关键不是让Agent永远跑下去，而是**提前定好规则：什么时候继续，什么时候停，失败几次之后必须叫人。**

------

## 三个让我觉得“有点东西”的地方

### 1. 把循环拆成五个零件

项目把整个循环拆得很清楚：

- **定时任务** —— 什么时候触发
- **worktree** —— 隔离改动，不影响主分支
- **技能** —— Agent需要会什么
- **插件与连接器** —— 对接哪些外部系统
- **子Agent** —— 谁来执行、谁来复核

外面再加一层**持久状态**，记录上次做了什么、现在卡在哪。

这个拆法让我觉得它不是随便写写，是真的在工程化这件事。

![五个基础部分与持久状态](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-06-loop-engineering-4.jpg)

### 2. 七种可以直接套用的场景

仓库已经整理好了7种模式：

| 模式               | 干啥的       | 建议频率 |
| :----------------- | :----------- | :------- |
| Daily Triage       | 每日仓库巡检 | 每天     |
| PR Babysitter      | PR跟进       | 按需     |
| CI Sweeper         | CI失败排查   | 每次CI   |
| Dependency Sweeper | 依赖更新     | 定期     |
| Changelog Drafter  | 变更日志草稿 | 每次发布 |
| Post-Merge Cleanup | 合并后清理   | 每次合并 |
| Issue Triage       | Issue分类    | 每天     |

每一种都标出了建议频率、风险级别和第一阶段开放程度。

![7 种循环模式](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-08-loop-engineering-6.svg)

### 3. 配套了三个实用命令

bash

```
npx @cobusgreyling/loop-init . --pattern daily-triage --tool codex
```



生成起步文件。

bash

```
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1 --cadence 1d
```



先估算一下每天跑一次要花多少。

bash

```
npx @cobusgreyling/loop-audit . --suggest
```



检查预算、状态、约束和验证规则有没有补齐。

这三个命令让我觉得这项目**是真的考虑过落地**的，不只是写个概念。

------

## 我最欣赏的一点：不吹“全自动”

很多AI项目上来就说“让你的Agent全自动干活”。

**loop-engineering没有这么写。**

官方Quickstart里明确建议：

> **第一周只生成报告，不自动修复，更不自动合并。**

等输出稳定了，再从L1报告模式逐步放开到L2辅助修改和L3无人执行。

这个节奏感，我觉得是做过真实项目的人才会写的。

![Loop Engineering 总览](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-03-loop-engineering-1.jpeg)

------

## 几个需要留意的点

仓库自己也写得很实在：

- 子Agent会**放大token消耗** —— 钱会花得更快
- **验证责任仍然在人** —— 别指望Agent自己检查自己
- 循环跑得越久，团队越容易**看不懂它改过的代码** —— 这一点我觉得特别真实

------

## 怎么快速试一下？

最容易上手的是 **Daily Triage**，只检查仓库、整理重点，写报告，不改代码。

在一个测试仓库里跑这三条命令：

bash

```
npx @cobusgreyling/loop-init . --pattern daily-triage --tool codex
npx @cobusgreyling/loop-cost --pattern daily-triage --level L1 --cadence 1d
npx @cobusgreyling/loop-audit . --suggest
```



然后**只看一周报告**，确认它找出来的任务确实有用，再考虑允许它动手改东西。

![loop-init 与 loop-audit 演示](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-04-loop-engineering-2.gif)

------

## 适合谁？

**适合：** 已经在用Claude Code、Codex等编码Agent，又被每天重复的仓库工作消耗时间的团队。CI排查、依赖更新、Issue分类、PR跟进这些有明确输入输出的活，最适合拿来试。

**不适合：** 只是偶尔让AI改一段代码的人。这套结构对那种场景太重了。

------

## 上手前盯住三件事

1. Agent能访问哪些外部系统
2. 每轮最多花多少预算
3. 谁来做最后验证

第三方npm包建议先在测试仓库里跑，**不要一上来就给自动合并和生产权限**。

![loop-engineering 项目卡片](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-10-image.png)

------

## 说点实在的

我以前一直觉得“让AI自动干活”这件事有点虚。

loop-engineering让我改观的地方在于，它把这件事**落到了一些能检查、能修改、能回滚的文件上**。

`STATE.md`记录当前状态，`LOOP.md`写运行规则，`loop-budget.md`限制预算，`loop-run-log.md`记录每次执行。出了问题，至少能翻翻日志看循环读了什么、做了什么、为什么还在继续。

它不是让你“相信Agent”，而是让你**能看清楚Agent在干什么**。

这个思路我觉得是对的。

------

项目地址：https://github.com/cobusgreyling/loop-engineering

今天就聊到这。下期见。

![项目 Star 增长图](https://cdn.jsdelivr.net/gh/crisxuan/prehub@main/docs/images/github-daily/github-20260708-cobusgreyling-loop-engineering-09-loop-engineering-7.svg)
