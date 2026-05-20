# Project Onboarding: OpenSpec + Superpowers + gstack

这份文档用于把任意项目接入 **OpenSpec**、**Superpowers** 和 **gstack**，让 AI coding agent 按统一主线工作。

核心原则：

- **OpenSpec 是项目变更的事实来源**：记录为什么做、做什么、验收标准、设计、任务和归档。
- **Superpowers 是 AI 执行纪律**：约束需求澄清、TDD、系统化调试、代码审查和完成前验证。
- **gstack 是专家增强层**：用于 CEO/产品审查、工程审查、设计审查、QA、安全审计、发布和浏览器验证。
- **不要生成多套互相竞争的计划**：如果 OpenSpec 已有 change artifacts，Superpowers 和 gstack 执行时必须优先使用这些 artifacts。

推荐分工：

| 工具 | 角色 | 主要产物 |
|---|---|---|
| OpenSpec | 事实来源 | `openspec/changes/<change>/proposal.md`、`specs/`、`design.md`、`tasks.md` |
| Superpowers | 执行纪律 | TDD、系统化调试、代码审查、完成前验证 |
| gstack | 专家团 | CEO/设计/工程/QA/安全/发布审查结果 |

---

## 1. 适用范围

所有长期维护项目都建议接入。

必须走 OpenSpec 的变更：

- 新功能
- 行为变化
- 架构变化
- 用户可见 UI/交互变化
- 数据抓取、清洗、发布、自动化链路变化
- 登录、权限、账号、支付、平台自动化等高风险逻辑
- 难回滚、影响面不清楚、需要多人/多 agent 协作的改动

可以跳过 OpenSpec 的变更：

- 拼写修正
- 注释修正
- 明确无行为变化的小配置调整
- 一次性探索脚本

即使跳过 OpenSpec，也仍然要使用 Superpowers 的验证和调试纪律。需要 UI、浏览器、发布、安全或产品方向判断时，可以调用 gstack 的对应专家技能。

---

## 2. gstack 接入评估

gstack 不应默认强制接入所有项目。拿到一个新项目时，先评估接入级别。

### 2.1 三种接入级别

| 级别 | 适用场景 | 做法 |
|---|---|---|
| 不接入 | 小脚本、一次性工具、纯库内部实现、无 UI、无发布流程、无安全/账号风险 | 只使用 OpenSpec + Superpowers |
| 轻接入 | 有一定复杂度，但不是持续发布产品；偶尔需要架构、QA、安全或设计审查 | 不写入团队强制规则，只在需要时手动调用 gstack |
| 全接入 | 长期产品、多人协作、用户可见、发布频繁、UI/QA/安全/平台风险明显 | 写入 `AGENTS.md`，建立固定 gstack 审查点 |

### 2.2 快速判断

满足任一条件，至少轻接入 gstack：

- 有真实用户或客户使用
- 有前端 UI、编辑器、仪表盘、内容发布页或复杂交互
- 有 staging/production 发布流程
- 涉及账号、登录、权限、token、cookie、支付或用户数据
- 涉及抓取、自动发布、平台自动化、第三方网站交互
- 改动失败会造成数据损坏、账号风险、线上事故或明显声誉风险
- 需要浏览器真实验收、截图验证、性能基线或发布前 QA

满足三项以上，建议全接入 gstack。

### 2.3 打分表

给项目打分：

| 维度 | 0 分 | 1 分 | 2 分 |
|---|---|---|---|
| 生命周期 | 一次性 | 偶尔维护 | 长期产品 |
| 用户影响 | 仅自己用 | 小范围内部用 | 真实用户/客户用 |
| UI/体验 | 无 UI | 简单 UI | 复杂 UI/编辑器/仪表盘 |
| 发布风险 | 不发布 | 手动发布 | 频繁发布/staging/production |
| 安全/账号 | 无 | 有 API key 或少量权限 | auth/cookie/token/用户数据/账号风险 |
| 平台/自动化 | 无 | 调用第三方 API | 抓取/自动发布/浏览器自动化 |
| 测试难度 | 单元测试足够 | 需要集成测试 | 需要真实浏览器/截图/端到端 |
| 团队协作 | 单人短期 | 单人长期 | 多人或多 agent 协作 |

结论：

- **0-4 分**：不接入 gstack。
- **5-9 分**：轻接入 gstack，只在关键节点使用。
- **10 分以上**：全接入 gstack。
- **任何安全/账号/自动发布高风险项为 2 分**：至少轻接入，并优先使用 `/cso` 或 `/qa-only`。

### 2.4 推荐命令选择

| 项目情况 | 建议 gstack 命令 |
|---|---|
| 方向不清楚 | `/office-hours` |
| 产品范围容易膨胀 | `/plan-ceo-review` |
| 架构、数据流、测试边界复杂 | `/plan-eng-review` |
| UI/交互/编辑器/内容呈现重要 | `/plan-design-review` |
| 已实现，需要找生产级问题 | `/review` |
| 需要真实浏览器验收 | `/qa` |
| 高风险线上/平台账号流程 | `/qa-only` 先报告，不自动操作 |
| 涉及账号、权限、抓取、发布、安全 | `/cso` |
| 准备发 PR 或发布 | `/ship`、`/land-and-deploy` |
| 性能敏感 | `/benchmark` |

### 2.5 不建议接入 gstack 的情况

- 纯算法库或小型 CLI，测试边界清晰。
- 一次性数据处理脚本。
- 学习实验、demo、throwaway prototype。
- 没有浏览器、发布、安全、产品方向判断需求。
- 项目还没稳定，流程成本会明显拖慢探索。

这些项目仍然可以使用 OpenSpec 记录较大变更，并用 Superpowers 保持 TDD、调试和完成前验证。

---

## 3. 全局安装

### 3.1 安装 OpenSpec

```bash
npm install -g @fission-ai/openspec@latest
```

确认安装：

```bash
openspec --version
```

### 3.2 安装 Superpowers

Superpowers 应安装在 AI 工具层，不建议复制进每个项目。

Codex App：

1. 打开 Codex App 的 Plugins
2. 搜索 `Superpowers`
3. 安装并启用

Codex CLI：

```text
/plugins
```

搜索并安装 `superpowers`。

Claude Code：

```bash
/plugin install superpowers@claude-plugins-official
```

### 3.3 安装 gstack

gstack 最自然的使用环境是 Claude Code；也支持 Codex CLI、Cursor、OpenCode 等多种 agent。它不是项目业务依赖，不要把它当成运行时代码引入产品。

Claude Code 全局安装：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack
./setup
```

Codex CLI 安装：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack
./setup --host codex
```

Cursor 安装：

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack
./setup --host cursor
```

团队模式只建议在团队已经决定使用 gstack 后启用：

```bash
(cd ~/.claude/skills/gstack && ./setup --team)
~/.claude/skills/gstack/bin/gstack-team-init optional
```

如果要强制团队使用，把 `optional` 改成 `required`。个人项目建议先用 `optional`。

---

## 4. 单项目初始化

在项目根目录执行：

```bash
cd <your-project>
openspec init --tools codex,claude,cursor
```

如果只使用 Codex：

```bash
openspec init --tools codex
```

如果团队成员使用不同 AI 工具：

```bash
openspec init --tools all
```

初始化后，项目中应出现类似结构：

```text
openspec/
├── changes/
├── specs/
└── config.yaml
```

如果希望启用更完整的 OpenSpec 工作流，例如 `/opsx:verify`、`/opsx:new`、`/opsx:continue`、`/opsx:ff`：

```bash
openspec config profile
openspec update
```

---

## 5. 推荐项目结构

```text
<project>/
├── AGENTS.md
├── openspec/
│   ├── config.yaml
│   ├── specs/
│   └── changes/
├── docs/
├── src/
├── tests/
└── package.json / pyproject.toml / etc.
```

`openspec/` 管长期规格和变更历史。  
`AGENTS.md` 管本项目 AI 工作协议。  
`docs/` 放用户文档、技术说明、运行手册等非 OpenSpec 主线资料。

---

## 6. 标准工作流

### 6.1 中大型功能

```text
Idea
→ /opsx:explore
→ /opsx:propose <change-name>
→ 人工审阅 proposal/specs/design/tasks
→ gstack 做产品/工程/设计前置审查，必要时更新 OpenSpec artifacts
→ AI 按 OpenSpec tasks 实现
→ Superpowers 执行 TDD / systematic debugging / review / verification
→ gstack 做 review / QA / security / release checks
→ /opsx:verify
→ PR / release
→ /opsx:archive
```

### 6.2 已经明确的小功能

```text
/opsx:propose <change-name>
→ 审阅 artifacts
→ 可选：gstack /plan-eng-review 或 /plan-design-review
→ 实现
→ 测试
→ /opsx:archive
```

### 6.3 Bug 修复

```text
复现问题
→ Superpowers systematic-debugging 查根因
→ 如果影响行为或需要长期记录，创建 OpenSpec change
→ 写失败测试
→ 修复
→ 验证
→ 归档 OpenSpec change
```

### 6.4 小改动

```text
直接修改
→ 运行相关测试
→ 报告验证结果
```

---

## 7. AI 执行规则

所有 AI agent 必须遵守：

1. **先检查是否需要 OpenSpec**
   - 非平凡变更必须先创建或更新 `openspec/changes/<change-name>/`。
   - 不确定是否需要时，默认需要。

2. **OpenSpec artifacts 优先**
   - 如果当前已有 `proposal.md`、`design.md`、`tasks.md`，执行时必须读取它们。
   - 不要再创建另一份独立计划，除非用户明确要求。

3. **Superpowers 负责执行纪律**
   - 新功能和 bugfix 优先 TDD。
   - bug 必须先找根因，不要猜修。
   - 完成前必须验证。
   - 需要 review 时，优先从行为风险、遗漏测试、回归风险开始。

4. **实现只做当前 change**
   - 不做无关重构。
   - 不顺手改 unrelated files。
   - 如果发现必须扩大范围，先更新 OpenSpec artifacts，再继续。

5. **验收必须落到证据**
   - 单元测试、集成测试、端到端测试、截图、日志、手动复现步骤，至少提供一种明确证据。
   - 不能只说“应该可以”。

6. **gstack 只做专家增强，不做第二主线**
   - OpenSpec 已经有 artifacts 时，不要用 gstack `/autoplan` 重新生成另一套主计划。
   - 可以用 gstack `/plan-ceo-review`、`/plan-eng-review`、`/plan-design-review` 审查 OpenSpec artifacts。
   - 可以用 gstack `/review`、`/qa`、`/cso`、`/ship` 做实现后的质量门。
   - 如果 gstack 审查发现需要改方向，先更新 OpenSpec artifacts，再继续实现。

---

## 8. 可直接复制的 AGENTS.md 模板

把下面内容放到每个项目根目录的 `AGENTS.md`，再按项目实际情况补充命令。

```markdown
# AI Project Workflow

## Source Of Truth

OpenSpec is the source of truth for non-trivial project changes.

For any feature, behavior change, architecture change, user-facing UI change, data pipeline change, automation change, or risky fix:

1. Create or update an OpenSpec change under `openspec/changes/<change-name>/`.
2. Keep `proposal.md`, `specs/`, `design.md`, and `tasks.md` aligned.
3. Implement only after the OpenSpec artifacts are clear enough to execute.
4. Verify the implementation against the OpenSpec artifacts before completion.
5. Archive completed changes with OpenSpec.

Small typo, comment, or no-behavior config changes may skip OpenSpec.

## Superpowers

Use Superpowers as the execution discipline:

- clarify requirements before implementation
- prefer TDD for features and bug fixes
- debug from root cause, not symptoms
- review before calling work complete
- verify behavior with real tests, browser checks, screenshots, logs, or reproducible commands

If Superpowers asks for a spec or plan, use the current OpenSpec change artifacts instead of creating a separate competing plan unless the user explicitly requests a separate plan.

## gstack

Use gstack as the specialist review and verification layer.

Recommended use:

- `/plan-ceo-review` for product direction, scope, and 10-star product pressure testing
- `/plan-eng-review` for architecture, data flow, edge cases, and test strategy
- `/plan-design-review` for UI/UX plans before implementation
- `/review` after implementation to find production-grade issues
- `/qa` or `/qa-only` for browser/user-flow verification
- `/cso` for security, abuse, auth, user data, scraping, publishing, and platform-risk work
- `/ship` only after tests and verification are complete

Do not use gstack `/autoplan` to create a second plan when an OpenSpec change already exists. Review and improve the OpenSpec artifacts instead.

## Work Scope

Only implement the current requested change.

Do not perform unrelated refactors, formatting churn, dependency upgrades, or broad cleanup unless the OpenSpec change explicitly includes them.

If implementation reveals that the scope must expand, stop and update the OpenSpec artifacts before continuing.

## Testing

Before completion, run the relevant project checks and report the commands and results.

Project commands:

- Install dependencies: `<fill in>`
- Run unit tests: `<fill in>`
- Run lint/typecheck: `<fill in>`
- Run app locally: `<fill in>`
- Run E2E/browser checks: `<fill in>`

## Completion Criteria

A task is complete only when:

- the code matches the OpenSpec artifacts or the user-approved request
- relevant tests/checks pass
- user-facing behavior has been verified when applicable
- gstack review/QA/security checks have been run when the change is product-critical, UI-heavy, security-sensitive, or release-bound
- no unrelated changes were introduced
- the final response reports what changed and what was verified
```

---

## 9. AI 项目接入评估流程

这份文档是通用协议，不应写死任何具体项目的接入结论。

当 AI 拿到一个已有项目或新项目时，必须先做项目评估，再决定：

- 是否初始化 OpenSpec
- 是否启用 Superpowers 作为默认执行纪律
- 是否接入 gstack，以及是“不接入 / 轻接入 / 全接入”
- 是否需要把规则写入项目 `AGENTS.md`

### 9.1 评估前先读取项目上下文

AI 必须先检查：

- `README.md`
- `AGENTS.md` / `CLAUDE.md` / `.cursor/rules` 等现有 AI 指令
- `package.json`、`pyproject.toml`、`Cargo.toml`、`go.mod` 等技术栈文件
- `src/`、`app/`、`pages/`、`components/`、`tests/` 等主要目录
- CI/CD 配置，例如 `.github/workflows/`
- 部署配置，例如 `vercel.json`、`Dockerfile`、`docker-compose.yml`
- 是否已有 `openspec/`
- 是否已有测试、E2E、截图回归、lint/typecheck 命令
- 是否涉及账号、权限、cookie、token、用户数据、抓取、自动发布或第三方平台操作

不要在不了解项目结构和风险面的情况下直接接入 gstack。

### 9.2 输出接入决策

AI 完成评估后，先输出一份简短决策：

```markdown
## AI Workflow Integration Decision

Project: <project-name>

### Summary

- Project type: <library / CLI / web app / automation / data pipeline / editor / internal tool / etc.>
- Lifecycle: <one-off / maintained / long-term product>
- Users: <self / internal / public / customers>
- Risk level: <low / medium / high>

### Decision

- OpenSpec: <not needed / light / required>
- Superpowers: <recommended / required>
- gstack: <none / light / full>

### Reasoning

- <reason 1>
- <reason 2>
- <reason 3>

### Required project rules

- <AGENTS.md rule or "none">

### Verification commands discovered

- Install: `<command or unknown>`
- Test: `<command or unknown>`
- Lint/typecheck: `<command or unknown>`
- E2E/browser: `<command or unknown>`
```

### 9.3 接入级别定义

OpenSpec：

| 级别 | 判断 | 做法 |
|---|---|---|
| 不需要 | 一次性脚本、小 demo、无长期维护 | 不初始化；需要时写普通 notes |
| 轻接入 | 偶尔有中型变更，但不是产品主线 | 只对非平凡变更使用 `/opsx:propose` |
| 必须接入 | 长期产品、复杂业务、多人协作、高风险自动化 | 初始化 `openspec/`，把 OpenSpec 写入 `AGENTS.md` |

Superpowers：

| 级别 | 判断 | 做法 |
|---|---|---|
| 推荐 | 大多数代码项目 | 使用 TDD、debugging、verification 等纪律 |
| 必须 | 长期维护、bug 成本高、测试复杂、AI 经常参与 | 写入 `AGENTS.md`，要求实现前澄清、测试先行、完成前验证 |

gstack：

| 级别 | 判断 | 做法 |
|---|---|---|
| 不接入 | 小脚本、纯库、CLI、无 UI、无发布/安全/账号风险 | 不写入 `AGENTS.md`，偶尔可手动调用 |
| 轻接入 | 有产品、UI、发布、安全或浏览器验证需求，但不是每次都需要 | 在关键节点手动用 `/plan-eng-review`、`/review`、`/qa-only`、`/cso` |
| 全接入 | 长期产品、用户可见、频繁发布、复杂 UI、高安全/账号/平台风险 | 写入 `AGENTS.md`，建立固定 gstack 审查点 |

### 9.4 默认判断

除非项目明显是一次性脚本，否则：

- OpenSpec 至少用于非平凡变更。
- Superpowers 默认推荐。
- gstack 必须先评估，不默认全接入。

如果存在任一高风险项，gstack 至少轻接入：

- 登录、权限、cookie、token、用户数据
- 支付、计费、订阅
- 抓取、自动发布、第三方平台自动化
- 真实用户可见的生产发布
- 复杂编辑器、内容生成、导出、浏览器交互
- 需要 E2E、截图、性能或可访问性验证

---

## 10. 推荐命令速查

OpenSpec：

```text
/opsx:explore
/opsx:propose <change-name>
/opsx:apply
/opsx:verify
/opsx:sync
/opsx:archive
```

常用终端命令：

```bash
openspec init --tools codex
openspec update
openspec config profile
```

Superpowers：

- brainstorming：需求澄清和设计
- writing-plans：实现计划
- test-driven-development：测试先行
- systematic-debugging：根因调试
- requesting-code-review：完成前审查
- verification-before-completion：完成前验证

gstack：

```text
/office-hours
/plan-ceo-review
/plan-eng-review
/plan-design-review
/review
/qa
/qa-only
/cso
/ship
/land-and-deploy
/benchmark
```

---

## 11. 推荐组合方式

### 默认主线

```text
OpenSpec /opsx:propose
→ gstack plan review
→ Superpowers-guided implementation
→ gstack review / QA / CSO when needed
→ OpenSpec /opsx:verify
→ OpenSpec /opsx:archive
```

### 何时用 gstack

| 场景 | gstack 命令 |
|---|---|
| 想法还不清楚 | `/office-hours` |
| 产品方向需要挑战 | `/plan-ceo-review` |
| 架构和测试策略需要审查 | `/plan-eng-review` |
| UI/体验方案需要审查 | `/plan-design-review` |
| 代码已经实现，需要挑 bug | `/review` |
| 需要真实浏览器验收 | `/qa` 或 `/qa-only` |
| 涉及账号、权限、抓取、发布、安全 | `/cso` |
| 准备发 PR/发布 | `/ship`、`/land-and-deploy` |
| 性能敏感 | `/benchmark` |

### 何时不要用 gstack

- 已经有清晰 OpenSpec change 时，不要再用 `/autoplan` 生成另一套主计划。
- 纯拼写、注释、小配置改动，不需要专家团。
- 高风险平台自动化不要让 `/qa` 直接乱操作线上账号；先用 `/qa-only` 或 staging 环境。

---

## 12. 最终原则

把这句话作为所有项目的默认规则：

> OpenSpec manages memory. Superpowers manages behavior. gstack brings specialists.

也就是：

- OpenSpec 让项目不会忘记自己为什么这样设计。
- Superpowers 让 AI 不会因为上下文、兴奋或幻觉而乱写代码。
- gstack 让产品、设计、工程、QA、安全和发布环节有人专门挑刺。
