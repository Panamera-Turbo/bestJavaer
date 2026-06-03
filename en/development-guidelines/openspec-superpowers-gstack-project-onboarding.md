# Project Onboarding: OpenSpec + Superpowers + gstack

This document is used to connect any item to **OpenSpec**, **Superpowers** and **gstack**, so that AI coding delegate works by a single main line.

Core principles:

- ** OpenSpec is the factual source of project change**: records of why, what, acceptance standards, design, tasks and archiving.
- ** Superpowers is AI Enforcement Discipline**: restraining demand clarification, TDD, systematic debugging, code review and validation before completion.
- **gstack is an expert enhancement layer**: for CEO/product review, engineering review, design review, QA, safety audit, release and browser validation.
- ** Do not generate multiple competing schemes**: If OpenSpec already has change plans, Superpowers and gstack implementations, priority must be given to using them.

Recommended division of labour:

|Tools|Role|Main products|
|---|---|---|
| OpenSpec |Factual sources| `openspec/changes/<change>/proposal.md`, `specs/`, `design.md`, `tasks.md` |
| Superpowers |Discipline|TDD, systematic debugging, code review, pre-completion validation|
| gstack |Panel of Experts|CEO/design/engineering/QA/security/publication of the results of the review|

---

## Scope of application

Access is recommended for all long-term maintenance projects.

OpenSpec changes must be taken:

- New function
- Behavioural change
- Structural changes
- User Visible UI/ Interactive Changes
- Data capture, cleaning, distribution, automated chain changes
- High-risk logic such as login, access, account numbers, payments, platform automation
- Changes that are difficult to roll back, that have no clear impact and that require multi-person/multi-agent collaboration

Skip OpenSpec changes:

- Spell fixes
- Comment fixes
- Clarify non-behavioural small configuration adjustments
- Discovery Script

Even if you skip OpenSpec, you still use Superpowers to verify and debug discipline. gstack's counterpart expertise is available when UI, browser, release, safety or product orientation determination is required.

---

## 2. gstack access assessment

gstack should not default on mandatory access to all items. When a new project is received, the level of access is assessed.

### 2. 1 Three levels of access

|Level|Apply scene|Approach|
|---|---|---|
|No access|Small script, one-time tool, pure library internal realization, no UI, no release process, no security/account risk|OpenSpec + Superpowers|
|Light access|A certain complexity, but not a continuous distribution of products; occasional structural, QA, security or design review|Do not write to team enforcement rules, only call gstack manually if needed|
|All access|Long-term products, multi-person collaboration, user visibility, frequency of releases, UI/QA/security/platform risks visible|Writing`AGENTS.md`, create fixed gstack review point|

### 2. 2 Quick judgement

gstack:

- Use with real user or client
- Frontend UI, editor, dashboard, content release page or complex interaction
- A status/project release process
- Account numbers, login, privileges, token, cookies, payments or user data
- In relation to capture, automatic publication, platform automation, third-party website interaction
- Failure to change results in data damage, account risk, online accident or apparent reputational risk
- Need browser real trial receipt, screenshot validation, performance baseline or QA before release

To meet more than three, full access to gstack is recommended.

### 2. 3 Rating Table

Rating of projects:

|Dimensions|0 min|1 min|2 min|
|---|---|---|---|
|Life cycle|One-time|Occasional maintenance|Long-term products|
|User Impact|Only for yourself.|Small-scale use|Real users/clients|
|UI/Experience|None UI|Simple UI|Complex UI/editor/ dashboard|
|Release risk|Do Not Publish|Manually.|Frequently published/staging/project|
|Security/Account|None|Have API key or a few permissions|auth/cookie/token/user data/account risk|
|Platform/automation|None|Call third party API|Automation of capture/automatic release/browser|
|Test difficulty|Unit testing is enough.|Integration test required|Real browser/stop/end to end required|
|Teamwork|Single short-term|Single long term|Multiple or multiple parties|

Conclusions

- **0-4 minutes**: no access to gstack.
- **5-9 minutes**: light access gstack, used only at key nodes.
- ** 10 minutes or more**: full access to gstack.
- ** Any security/account/automatic release of high-risk items is 2 minutes**: at least light access and priority use`/cso`or`/qa-only`.

### 2. 4 Recommended command choice

|Project status|Suggest gstack command|
|---|---|
|It's not clear.| `/office-hours` |
|The product range expands.| `/plan-ceo-review` |
|Structure, data flow, complexity of testing borders| `/plan-eng-review` |
|UI/interactive/editor/content important| `/plan-design-review` |
|Achieved, production level needs to be identified| `/review` |
|Needs real browser acceptance| `/qa` |
|High-risk line/platform account process| `/qa-only`Report first, no automatic operation|
|Account numbers, privileges, access, issuance, security| `/cso` |
|Prepare to issue PR or release| `/ship`, `/land-and-deploy` |
|It's sensitive.| `/benchmark` |

### 2. 5 Cases where access to gstack is not recommended

- Pure algorithms or small CLIs, test boundaries clear.
- One-time data-processing script.
- Study experiments, demo, throwaway program.
- There is no browser, distribution, safety, product orientation needs.
- The project is not stable and the process costs will be significantly slow to explore.

These items can still use OpenSpec to record larger changes and keep TDD, debug and validate before completion with Superpowers.

---

## 3. Global installation

### 3. 1 Installation of OpenSpec

```bash
npm install -g @fission-ai/openspec@latest
```

Confirm installation:

```bash
openspec --version
```

### 3. 2 Installation of Superpowers

Superpowers should be installed on the AI tier and not recommended for copying to each item.

Codex App: 

1. Opens Plugins of Codex App
2. Search`Superpowers`
3. Install and Enable

Codex CLI: 

```text
/plugins
```

Search and install`superpowers`.

Claude Code: 

```bash
/plugin install superpowers@claude-plugins-official
```

### 3. 3 Installation gstack

Gstack's most natural environment is Claude Code; it also supports a variety of delegates such as Codex CLI, Cursor, OpenCode. It is not dependent on the project ' s operations and does not introduce it as a running time code into the product.

Claude Code global installation:

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack
cd ~/.claude/skills/gstack
./setup
```

Codex CLI installation:

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack
./setup --host codex
```

Cursor installation:

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack
./setup --host cursor
```

Team mode is only recommended to be enabled after the team has decided to use gstack:

```bash
(cd ~/.claude/skills/gstack &&./setup --team)
~/.claude/skills/gstack/bin/gstack-team-init optional
```

If you want to force a team to use, put`optional`Replace with`required`I don't know. Individual project proposal first`optional`.

---

## 4. Initialization of single items

In the project root directory:

```bash
cd <your-project>
openspec init --tools codex, claude, cursor
```

If only Codex:

```bash
openspec init --tools codex
```

If team members use different AI tools:

```bash
openspec init --tools all
```

After initialization, a similar structure should emerge in the project:

```text
openspec/
├── changes/
├── specs/
└── config.yaml
```

If you want to enable a more complete OpenSpec workflow, for example`/opsx: verify`, `/opsx: new`, `/opsx: continue`, `/opsx: ff`: 

```bash
openspec config profile
openspec update
```

---

## 5. Recommended project structure

```text
<project>/
├── AGENTS.md
├── openspec/
│ ├── config.yaml
│ ├── specs/
│ └── changes/
├── docs/
├── src/
├── tests/
└── package.json / pyproject.toml / etc.
```

`openspec/`Managing long-term specifications and changing history.
`AGENTS.md`Manage the AI work agreement for this project.
`docs/`Releases non-OpenSpec mainline information such as user files, technical instructions, operational manuals, etc.

---

## Standard workflow

### 6. 1 Medium and large functions

```text
Idea.
/opsx: explore
/opsx: propose <change-name>
• Manual/specs/design/tasks
gstack for product/engineering/design pre-review and update OpenSpec technologies as necessary
→ AI Press OpenSpec Tasks
Superpowers execute TDD / stymatic debugging / review / protection
gstack do review / QA / security / request checks
/opsx: verify
PR / request
/opsx: archive
```

### 6. 2 Small functions identified

```text
/opsx: propose <change-name>
Reviews
→ Options: gstack /plan-eng-review or /plan-design-review
Achieved
Test
/opsx: archive
```

### 6. 3 Bug Rehabilitation

```text
Recurrence
Superpowers systematic-debugging
• Create OpenSpec change if influencing behaviour or requiring long-term records
→ Writing failed test
Rehabilitation
Validation
OpenSpec Change
```

### 6. 4 Minor changes

```text
Direct Changes
• Run relevant tests
Report validation results
```

---

## AI Enforcement rules

All AI parties must comply with:

1. ** Check if OpenSpec**
 - Extraordinary changes must be created or updated first`openspec/changes/<change-name>/`.
 - Default is required when it is uncertain whether it is necessary.

2. **OpenSpec priorities**
 - If current`proposal.md`, `design.md`, `tasks.md`They must be read in their implementation.
 - No further independent plans are created unless explicitly requested by the user.

3. ** Superpowers is responsible for enforcing discipline**
 - New function and bugfix priority TDD.
 - Bug has to find a cause, don't guess.
 - Validation is required before completion.
 - When review is required, priority begins with behavioural risk, missing testing, regression risk.

4. ** Achieved only for current change**
 - Don't do the unrelated remodeling.
 - Unrelaged files.
 - If it is found that the scope must be expanded, it should be updated first and then continued.

5. ** Receiving and inspection must be documented**
 - Unit tests, integration tests, end-to-end tests, screenshots, logs, manual recurrence steps, providing at least one clear piece of evidence.
 - One cannot simply say "should".

6. **gstack only as specialist reinforcement, not second line**
 - OpenSpec does not use gstack when there already exist artifices`/autoplan`Regenerated another master plan.
 - Use gstack`/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`OpenSpec reviews.
 - Use gstack`/review`, `/qa`, `/cso`, `/ship`Do the quality door after realization.
 - If the gstack review finds that there is a need for a change of direction, it will be possible to update OpenSpec technologies before they continue.

---

## 8. AGENTS.md template that can be copied directly

Put the following in each item's root directory.`AGENTS.md`, to supplement the order with the actual circumstances of the project.

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

## 9. AI Project access assessment process

This document is a generic agreement and should not contain access conclusions for any specific project.

When AI obtains an existing project or a new project, it must assess the project before deciding:

- Initialize OpenSpec
- Whether to enable Superpowers as default discipline
- Whether to access gstack, and "no access/ light access/ full access"
- Need to include rules in the project`AGENTS.md`

### 9. 1 Read project context before assessment

AI must first check:

- `README.md`
- `AGENTS.md` / `CLAUDE.md` / `. cursor/rules`Wait for existing AI commands
- `package.json`, `pyproject.toml`, `Cargo.toml`, `go. mod`Wait for the technology stack file
- `src/`, `app/`, `pages/`, `components/`, `tests/`Main Directory
- CI/CD configuration, e. g.`. github/workflows/`
- Deployment configuration, for example`vercel.json`, `Dockerfile`, `docker-compose.yml`
- Did you have one?`openspec/`
- Tests, E2E, intercept regression, Lint/ typecheck command
- Whether it involves account numbers, privileges, cookies, token, user data, capture, automatic release or third-party platform operations

No direct access to gstack without knowledge of the project structure and risks.

### 9. 2 Output access decision-making

AI After completing the assessment, output a short decision:

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

### 9. 3 Definition of level of access

OpenSpec: 

|Level|Decision|Approach|
|---|---|---|
|No need.|One-time script, small demo, no long-term maintenance|Not initialized; plain when needed notes|
|Light access|Sometimes there's a medium change, but not the main line.|Use only for extraordinary changes`/opsx: propose` |
|Must access|Long-term products, complex operations, multi-person collaboration, high-risk automation|Initialize`openspec/`, write OpenSpec`AGENTS.md` |

Superpowers: 

|Level|Decision|Approach|
|---|---|---|
|Recommendations|Most code items|Using disciplines such as TDD, debugging, verification|
|Yes.|Long-term maintenance, bug cost, complex testing, AI participation|Writing`AGENTS.md`, require clarification before realization, testing first, validation before completion|

gstack: 

|Level|Decision|Approach|
|---|---|---|
|No access|Small scripts, pure libraries, CLI, no UI, no release/security/account risk|Do Not Write`AGENTS.md`, can be called manually from time to time|
|Light access|Product, UI, release, safety or browser validation requirements, but not every time|Use it at key nodes`/plan-eng-review`, `/review`, `/qa-only`, `/cso` |
|All access|Long-term products, user visibility, frequent releases, complex UI, high security/account/platform risk|Writing`AGENTS.md`, create fixed gstack review point|

### 9. 4 Default judgement

Unless the project is clearly a one-time script:

- OpenSpec at least for extraordinary changes.
- Superpowers default recommended.
- gstack must be evaluated first, without default full access.

If any high-risk item exists, gstack at least light access:

- Login, permissions, cookies, token, user data
- Payment, billing, subscription
- Capture, autopublishing, automoting third-party platforms
- Production release visible to real users
- Complex editor, content generation, export, browser interaction
- E2E, screenshot, performance or accessibility verification required

---

## 10. Summary of recommended orders

OpenSpec: 

```text
/opsx: explore
/opsx: propose <change-name>
/opsx: apply
/opsx: verify
/opsx: sync
/opsx: archive
```

Common terminal command:

```bash
openspec init --tools codex
openspec update
openspec config profile
```

Superpowers: 

- brainstorming: needs clarification and design
- Working-plans: implementation plan
- Test first.
- sestematic-debugging: root debugging
- request-code-review: pre-review
- Verification-before-complement: Before validation

gstack: 

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

## 11. Recommended cluster approach

### Default Main

```text
OpenSpec /opsx: propose
→ gstack plan review
→ Superpowers-guided implementation
→ gstack review / QA / CSO when needed
→ OpenSpec /opsx: verify
→ OpenSpec /opsx: archive
```

### When to use gstack

|scene|gstack command|
|---|---|
|I don't know yet.| `/office-hours` |
|Product direction requires challenges| `/plan-ceo-review` |
|Structure and testing strategy to be reviewed| `/plan-eng-review` |
|UI/Empirical programme needs review| `/plan-design-review` |
|The code has been achieved. You need to pick the bug.| `/review` |
|Needs real browser acceptance| `/qa`or`/qa-only` |
|Account numbers, privileges, access, issuance, security| `/cso` |
|Preparation for PR/publishing| `/ship`, `/land-and-deploy` |
|It's sensitive.| `/benchmark` |

### When do not use gstack?

- When OpenSpec Change is clear, stop using it.`/autoplan`Generate another master plan.
- Pure spelling, notes, minor configuration changes do not require panels of experts.
- The high-risk platform is automated.`/qa`Directly disrupting accounts on line; first`/qa-only`or statusing environment.

---

## 12. Final principles

As the default rule for all items:

> OpenSpec manages memory. Superpowers manages behavior. gstack brings specialists.

That is:

- OpenSpec lets the project not forget why it was designed.
- Superpowers let AI not write code out of context, excitement or hallucinations.
- gstack allows for specialized stinging of products, design, engineering, QA, security and distribution.
