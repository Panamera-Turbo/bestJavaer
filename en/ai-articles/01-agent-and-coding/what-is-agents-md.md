# What Is AGENTS.md?

[English](./what-is-agents-md.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Agents.md%20%E6%98%AF%E4%BB%80%E4%B9%88.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-06-09


In the real project, Codex doesn't just have to write code, but it also needs to know the rules of the project: what to order, what to run, what to do, what to do first.

If you knock on them manually each time, they are troublesome and easy to miss.

`AGENTS.md`The effect is to write down the rules and make Codex read them automatically every time he enters the project.

It solves the problem of making Codex understand this project better.

It's been a long time, Codex. I haven't really understood it. Pass.`AGENTS.md`What's that?

The article will be broken down in detail.

---

In short,`AGENTS.md`Just give Agent a look at the README.

`README.md`It's for people to see what this warehouse does.

`AGENTS.md`It's for Codex, so that Codex knows what works are in this warehouse before changing the code.

For example:

- How does this project start?
- What test do you run after changing the code?
- Which directories aren't moving?
- With what?
- Do you want to confirm the new dependencies?
- What's in the database, API, front end?

Note that the title of the document suggests that:

```shell
AGENTS.md
```

Do Not Write`Agent.md`, `Agents.md`Or...`agents.md`.

Case does not match, and some scenarios may result in unloading.

# Global AGENTS.md

Global`AGENTS.md`In general:

```shell
~/.codex/AGENTS.md
```

Without this directory you can create:

```shell
mkdir -p ~/.codex
```

Global`AGENTS.md`It's for your long-term personal preference.

For example:

```md
# ~/.codex/AGENTS.md

## Working agreements

- Default reply in Chinese.
- Read the file before changing the code.
- Prioritize the current style of the project.
- Do not automatically cover changes in users.
- Confirmation of new production dependence.
- If it is not possible to run the authentication order, explain why.
```

These rules do not depend on a particular warehouse and any project is established.

So it fits the whole picture.

After writing, the following command can be used to verify:

```shell
codex --ask-for-approval never "Summarize the current instructions."
```

I ran away here:

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260609103020648.png" alt="image-20260609103020648" style="zoom:50%;" />

If there are rules in the output that you're writing in, it means the whole picture.`AGENTS.md`It's in effect.

If there are some English rules in the output, it's normal.

Because this command sums up "all orders in force now," not just yours.`AGENTS.md`It also contains information on Codex's own system rules, current work catalogues, approval strategy, sandbox privileges, etc.

How about the global and project levels min

`AGENTS.md`It can be placed in different places.

These three levels are most common:

```shell
~/.codex/AGENTS.md # Global rules
repo/AGENTS.md # Project rules
repo/apps/web/AGENTS.md # Submodule rules
```

They are not mutually exclusive.

Not that there's a whole picture.`AGENTS.md`, Projects`AGENTS.md`It doesn't work anymore.

They'll load together.

It is simply understood that:

- Global rule: I want Codex to work how it works.
- Project rules: how does this warehouse work?
- Subdirectorial rules: What are the special requirements for this module?

The test is simple:

- Another project is still in place: global
- Only set up in this warehouse: release the project.
- Only in a subdirectories: release catalogue

For example, "prevalence before additional production dependence" is appropriate for global coverage.

For example, run after "Modify Prisma schema"`pnpm db:generate`"Apfits the project.

Because not every project uses Prisma.

Explain here.

`Prisma`It is a common database tool in the Node.js/TypeScript ecology. You can simply understand that it connects the structure, type and query code of the database table to allow you to operate the database in the code in a secure manner.

Many projects using Prisma include:

```shell
prisma/schema.prisma
```

This document describes the tables, fields and relationships in the database.

When you modify this schema, the project usually needs to recreate the database client code.

`pnpm db:generate`Typically, the scripts contained in the project may be executed:

```shell
prisma generate
```

So this rule means:

```text
If you change the definition of the database structure, do not simply change the files and recreate the database client.
```

But not every project, Prisma, not every project.`db:generate`This script.

So it's a typical project-level rule. It's not suitable for global coverage.`~/.codex/AGENTS.md`.

# Project level AGENTS.md

Project level`AGENTS.md`Usually in a warehouse root directory:

```shell
repo/AGENTS.md
```

It should write down a specific contract for the project.

For example:

- Installation orders
- Commence orders.
- Test orders.
- Type check orders.
- Lint Command
- Directory structure
- Generate file boundaries
- Database change requirements
- API Document Synchronization Requirements

In the case of production projects, the template at the end of the text can be used directly and the commands and directories can then be redacted according to the circumstances of the project.

# Verify Project Level AGENTS.md

I followed Project Spope above.`AGENTS.md`A test project was created.

The catalogue is about this:

```shell
agents-md-test/
 AGENTS.md
 apps/
 web/
 packages/
 ui/
 db/
 services/
 payments/
 docs/
 api/
 src/
 generated/
```

In the project root directory:

```shell
codex --ask-for-approval never "List the instruction sources you loaded and summarize the Project commands, Project structure, and Rules sections."
```

You can also test a subdirectorial:

```shell
codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."
```

Output test:

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260609132036337.png" alt="image-20260609132036337" style="zoom:50%;" />

One sentence:

Authentication`AGENTS.md`Whether or not it is effective is not to be seen whether it states that "AGENTS.md has been loaded".

It's best for it to summarize the unique rules inside.

Like in the output:

```text
pnpm dev
src/generated
pnpm db:generate
docs/api
```

These are project levels.`AGENTS.md`It's unique.

To see this, it is clear that the project-level rules do take effect.

# Subdirectories AGENTS.md

In addition to the root directory, submodules can also be used`AGENTS.md`To make a more detailed constraint.

For example:

```shell
repo/
 AGENTS.md
 services/
 payments/
 AGENTS.md
 search/
 AGENTS.md
```

`repo/AGENTS.md`Write the general rules for the entire warehouse.

`services/payments/AGENTS.md`Write the rules for paying for service.

`services/search/AGENTS.md`Write the search service's own rules.

For example, the payment service might say:

```md
# services/payments/AGENTS.md

## Payments Rules

- Do not change billing behavior without updating payment tests.
- Do not log card numbers, tokens, or customer secrets.
- Run `pnpm test payments` after changing payment logic.
```

It's very useful for monorepo.

Since a warehouse may have front-end, back-end, payment, search, data assignments, each module has different risk points.

# AGENTS.override.md #

Except...`AGENTS.md`And there's another file called:

```shell
AGENTS.override.md
```

It's a priority compared to the directory.`AGENTS.md`Higher.

For example:

```shell
repo/
 AGENTS.md # Store Root Rules
 services/
 payments/
 AGENTS.md # It'll be ignored.
 AGENTS.override.md # Effective entry into force
 README.md
 search/
 AGENTS.md
```

Yes.`services/payments/`Under directories, there are also:

```shell
AGENTS.md
AGENTS.override.md
```

And then Cordex will give priority to:

```shell
services/payments/AGENTS.override.md
```

Under the same directory is ignored:

```shell
services/payments/AGENTS.md
```

`AGENTS.override.md`It's suitable for a scene that needs strong coverage.

For example:

- Some subservice has special security rules.
- A directory forbids changes to generate files
- A module must have a special test command
- I'm trying to replace it temporarily.`AGENTS.md`Behaviour

In general, use`AGENTS.md`That's enough.

Only explicitly want to overwrite the same directory`AGENTS.md`Time.`AGENTS.override.md`.

# Custom fallback filename

Some teams may already have their own project description documents.

For example:

```shell
TEAM_GUIDE.md
.agents.md
```

If you don't want to change the name of these files,`AGENTS.md`, you can set the fallback file name in the Codex configuration.

Edit:

```shell
~/.codex/config.toml
```

Accession:

```toml
project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
project_doc_max_bytes = 65536
```

Then restart Codex, or rerun a new one.`codex`Command.

When configured, Codex will find in this order in each directory:

```text
AGENTS.override.md
AGENTS.md
TEAM_GUIDE.md
.agents.md
```

Could not close temporary folder: %s

Like what?`README.md`Not automatically become a Cordex input file because it exists.

`project_doc_max_bytes`Control is exercised over the maximum number of bytes after the consolidation of project description documents.

If there are many rules, they can be appropriately scaled up.

# Switch configuration directory using CODEX HOME

By default, Codex uses:

```shell
~/.codex
```

As your own home directory.

That's why the whole world`AGENTS.md`Default is:

```shell
~/.codex/AGENTS.md
```

If you want to use another configuration on a temporary basis, you can set it up.`CODEX_HOME`: 

```shell
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"
```

This order means:

Do not use default for this execution`~/.codex`, instead using the following under the current project:

```shell
$(pwd)/.codex
```

It suits these scenes:

- Prepare a separate configuration for project automation tasks
- Distinguishing Personal Configuration and CI Configuration
- Temporary tests are different.`AGENTS.md`
- Avoid Pollution Default`~/.codex`

If the rules don't look right, check first:

```shell
echo $CODEX_HOME
```

If it's not empty, it means that Codex is not currently using default.`~/.codex`.

AGENTS.md

The last one I thought was better for the project.`AGENTS.md`.

The template is engineering discipline-oriented and suitable for multi-person collaboration projects, monorepo, projects involving databases, API and CI.

You can copy it directly to the root of the project and then delete it as it is.

```md
# AGENTS.md

Working agreement for AI coding agents in this repository.

On conflict, follow: explicit user instructions > this file > existing code conventions > your defaults.

When the choice is risky or materially affects architecture, data, security, or public behavior, stop and ask rather than guess.

## Orientation

Do this first, every session.

Before writing any code, build a working model of the repo from what is actually there:

- Read `README`, `CONTRIBUTING`, and any root-level `*.md` files for setup and norms.
- Detect the package manager from the lockfile:
 - `pnpm-lock.yaml` -> `pnpm`
 - `yarn.lock` -> `yarn`
 - `package-lock.json` -> `npm`
 - `uv.lock` or `poetry.lock` -> the matching Python tool
- Use the detected package manager. Never introduce a second package manager.
- Find the real commands in `package.json` scripts, `Makefile`, `Taskfile`, `justfile`, or CI config.
- Treat CI config (`.github/workflows`, `.gitlab-ci.yml`, etc.) as the source of truth for what passing means.
- Read the files you are about to change and their tests before editing.
- Do not assume a stack. Verify it from the repo.

## Core Principles

- Make the smallest change that solves the task.
- Do not do drive-by refactors, renames, or reformatting of untouched code.
- Keep unrelated changes out of the diff.
- Match the surrounding code: naming, structure, error handling, and test style.
- Consistency beats personal preference.
- Reuse existing helpers, components, and patterns before adding new ones.
- Do not add speculative abstractions, config, or error handling for cases that do not exist yet.
- Comments should explain non-obvious decisions. Do not comment what the code already says.

## Verification

Required before calling a task done:

- Use the project's defined commands. Prefer focused checks first, then broader checks.
- Run the narrow tests for the file, package, or feature you touched.
- Then run the broader gate that the project defines: lint, typecheck or compile, and tests.
- Mirror CI locally when practical.
- Do not invent unrelated verification commands just to have something to run.
- Fix failures caused by your change.
- Add or update tests for behavior changes.
- If you cannot run a command because of missing services, credentials, network, or time, say so explicitly.
- Never imply tests passed if you did not run them.

## Dependencies

- Do not add a production dependency without asking first.
- When requesting a dependency, explain why the existing tools are not enough.
- Dev-only tooling is lower risk, but still match what the repo already uses.
- Never edit generated files, vendored code, or lockfiles by hand.
- Regenerate generated files and lockfiles through the project's documented command.

## Git And PR

- Commit only when asked.
- If asked to commit and currently on the default branch, create a feature branch or ask before committing.
- Add files by name. Do not use `git add.` or `git add -A`.
- Use conventional commit subjects when committing, such as `feat:`, `fix:`, or `chore:`.
- Keep one logical change per commit.
- Never run `push --force`, `reset --hard`, `branch -D`, `clean -f`, or `--no-verify`.
- Do not amend, squash, or rebase already-pushed commits unless asked.
- Do not revert or overwrite changes you did not make.

## Security

- Never commit secrets, tokens, keys, or credentials.
- Treat `.env*` files as sensitive.
- Do not print secret values or write them to logs.
- Validate external input at trust boundaries.
- When changing access to user-visible data, check the authorization path.
- Do not log PII or customer data.

## Data And Migrations

- Treat schema changes and migrations as high risk.
- Do not create or modify production migrations unless the task explicitly asks for it.
- Flag destructive changes in your summary, including dropped columns, deleted rows, and irreversible backfills.
- Wait for confirmation before applying destructive data changes.

## When To Stop And Ask

Pause and ask before:

- Adding a production dependency or new framework.
- Adding a broad new abstraction.
- Touching production data, schema, or migrations.
- Making a breaking change to a public API or shared interface.
- Editing shared config, CI, or the build pipeline.
- Continuing when the task contradicts the code.
- Choosing between several valid approaches when there is no clear winner.

## Reporting Back

End each task with:

- What changed, by file.
- How it was verified, including commands run and results.
- What was not run, and why.
- Risks or follow-ups.
```

This template doesn't bind a specific technology vault, so it's worse than that.`pnpm`, `Prisma`, `docs/api`.

It focuses on allowing Codex to read the project first, to judge the order, to make minimum modifications, and finally to clarify the certification and risk.

If your project already has a clear technology stack, you can also continue to add project rules.

For example:

```md
- After changing Prisma schema, run `pnpm db:generate`.
- API changes must update files under `docs/api`.
- Frontend changes must pass `pnpm test apps/web`.
```

In other words, this template is suitable for the project level.`AGENTS.md`The bottom seat, fold your own commands and boundaries.

# Summarizing

`AGENTS.md`It's basically a project description for Codex.

Global`~/.codex/AGENTS.md`Put a long-term preference.

Item`repo/AGENTS.md`Put down the rules.

Subdirectories`AGENTS.md`Set the module rules.

`AGENTS.override.md`to overwrite the general rules of the same directory.

If the team already has its own description, it can pass.`project_doc_fallback_filenames`Add the fallback list.

Most importantly,`AGENTS.md`Don't write empty words.

Don't write:

```text
Please keep the code elegant.
Please follow best practices.
```

To write rules that affect Codex behaviour and that can be validated by an order.

This is a truly useful engineering constraint.
