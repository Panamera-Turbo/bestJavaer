# OpenAI's Official Prompting Guide

[English](./openai-official-prompting-guide.md) | [Chinese Original](../../../ai-articles/02-models-and-research/OpenAI%20%E5%AE%98%E6%96%B9%E6%8F%90%E7%A4%BA%E8%AF%8D%E6%8C%87%E5%8D%97.md)

> Date: 2026-07-20

Everyone should know that after GPT-5.6 was fully launched, the Codex also ushered in a major revision. OpenAI initially changed the Codex to ChatGPT Codex, but then there were too many complaints online, so OpenAI had no choice but to change it back to the Codex.

But you may not know that after this revision of Codex, there is a new**"Prompt Guide" in the official manual: writing useful prompt words for Chat, ChatGPT Work and Codex**.

I also read OpenAI's [Prompting official document](https://learn.chatgpt.com/docs/prompting) from beginning to end.

Then there is this article. Without further ado, let's get straight to the point!

## Cue word overview

First of all, the official definition of Prompt is directly given:

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260714152408415.png" alt="image-20260714152408415" style="zoom:50%;" />

Prompt is how you tell ChatGPT what you want to know, make, or modify. Prompt can be a question, an instruction, or a goal. You don't need to use technical syntax or rigid formulas in the field of programming. You only need to describe it in natural language. LLM will execute the relevant steps according to your language. After the execution is completed, you can view the results, and you can adjust and improve the results through multiple rounds of conversations.

This is actually the official definition, which is somewhat textbook-style. But it's actually easier to understand. In the past, when we wrote various codes and learned various languages, we were actually using programmed languages ​​to deal with computers. Now it doesn't have to be so complicated. You only need to use natural language to deal with computers. This method is also commonly known as vibe coding.

Under normal circumstances, Prompt is enough to write a short prompt word.

For example

> Please continue
>
> Start it up
>
> Why did you mess with me again?
>
> Please restore the previous version
>
> OK

But for larger and more important content, some key parts need to be included, such as the following four elements

* `Goal`(target): What should ChatGPT do?
* `Context` (Context): What information and resources would be helpful?
* `Output` (output): What format, length, and level of detail do you need?
* `Boundaries` (boundary conditions): What must remain unchanged? What issues should be avoided with ChatGPT, or things that need to be determined with you before implementation?

These four elements do not require you to add them to all prompts. Just add the corresponding ones for different scenarios.

## Describe the results you need

The first official piece of advice is: start with the results first, and don't rush to arrange every step for AI.

For example, if you get a meeting record and need to synchronize it with the project team, you can write like this:

> Organize these meeting minutes into a brief project progress briefing for the project team to read. Put finalized decisions and next steps at the forefront.

This sentence explains what to do, who to show it to, and how to sequence the content. As for whether to extract decisions first or organize the timeline first, you can leave it to ChatGPT to decide.

For example, when asking Codex to correct a bug, you can ask it to reproduce the bug first, then locate the cause, and then re-execute the reproduction steps and run the test after modification.

Financial analysis can specify the data caliber, and legal materials can limit the source of data.

For ordinary rewriting and summary, you only need to explain the results clearly.

## Add useful context

Context is not about throwing all the data at ChatGPT. You need to provide information that will change the results and explain what each data is used for.

Suppose you uploaded the company brand manual, product feature list, and last year's sales report, and only said one sentence to refer to the attachments to rewrite the product introduction. It would be difficult for ChatGPT to determine which of the three documents should be used as the basis.

But if you use the following Prompt, it is much more efficient

> Check the functional facts against the product feature list; rewrite according to the tone and wording in the brand manual; use last year's sales report only to understand target customers, do not quote out-of-date numbers.

There are also three documents. This Prompt has found its own role for each piece of information. This will let ChatGPT know where to check the facts, which style to refer to, and how to deal with old reports.

Different types of information are provided in different ways: documents, tables, PPT and PDF are suitable for summarizing, comparing and rewriting;

When the task depends on the interface or layout, you can upload a screenshot and point out the specific area;

When answers rely on the latest information, explicitly ask to search the web and cite sources;

When multiple conversations want to share files, they can be put into the same Project.

## Use a connected data source

If ChatGPT is already connected to Drive, Slack, Gmail or GitHub, the Prompt needs to clearly explain where to find it, what to find, and how to use it.

> Prepare a status report using the latest project plan in Drive, as well as key decisions, schedule changes, and risks from the past two weeks in the project Slack channel.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260714174045432.png" alt="ChatGPT uses connected data sources" style="zoom:33%;" />

Specific search actions can be left to ChatGPT. You no longer need to specify which file it opens first or which keywords it searches for.

Whether the connection source can be used depends on whether the corresponding plug-in is installed, whether the account is authorized, as well as the current subscription plan and workspace settings.

### Use plugins

Plugins provide two types of things: reusable instructions and connections to tools like Google Drive, Gmail, Slack, and GitHub.

When using it, say what you ultimately want to accomplish and let ChatGPT choose from the available tools.

If you specifically want to use a certain plug-in, you can enter `@` in the input box and select it from the list.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260717225455925.png" alt="image-20260717225455925" style="zoom:50%;" />

To put it bluntly, the plug-in is responsible for providing capabilities, and you are responsible for describing the results.

### Personalized ChatGPT

Long-term preferences can be placed in the custom instructions of `Settings > Personalization`. For example, use Chinese by default, use less clichés, and retain English when professional terms appear for the first time.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260717225619591.png" alt="image-20260717225619591" style="zoom: 33%;" />

Personalization is not suitable for conditions where a single prompt is useful, only for conventions that have long-term effects.

## Set boundary conditions

Boundaries is the most practical part of the entire guide in my opinion. It gives constraints to the AI, just like Harness.

The official gave four typical examples:

- Already approved dates and budget figures remain unchanged.
- Only use the information provided, mark missing information and don't guess.
- All recommendations must be within the stated budget.
- Write the message as a draft and don't send it.

These four sentences are respectively about protecting confirmed data, information authenticity, budget and operation permissions.

For example, if you let ChatGPT polish the contract, you can write optimized expressions, but do not modify the amount, effective date, and payment term;

Let Codex change the code, you can write it without changing the public API, and don't deploy it to the production environment.

But don't write too many boundary conditions. Officials recommend using one or two places that are most likely to cause actual losses as boundary conditions.

## Make the results available for immediate use

Two words, two results:

"Summarize it for me" and "put it together as a one-page summary for your supervisor to quickly browse before the meeting" will produce much different results.

Officials gave several examples: organizing meeting minutes into emails containing decisions, responsible persons and deadlines;

Tabulate planned expenditures with actual expenditures;

All differences exceeding 10% are highlighted.

If you encounter an important task, you should also add a final check:

> Before completing, check that each follow-up action has an owner and deadline. Please mark the information that cannot be found as "to be confirmed" and do not complete it yourself.

## Improve results with follow-up messages

The first prompt may not achieve what you want. You can look at the output first, and then tell ChatGPT what to change:

> Be more direct at the beginning, retain the evidence, and move the suggestions to the front of the background introduction.

This is more useful than saying "if the writing is not good, correct it again".

### Steering and queuing｜Insert current task and queuing

You can continue sending messages while Codex is working. Steer and Queue determine when this message takes effect.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260715085710471.png" alt="Steer and Queue in Codex" style="zoom:50%;" />

Steer will send new information to the current task, suitable for supplementing missing information or changing direction in time. Queue will leave the message to the next round, which is suitable for processing after the current work is completed.

One jumps in line and the other queues up.

Codex can set default behavior in `Settings > General > Follow-up behavior`. Messages in the queue will be displayed above the input box and can be edited, reordered, sent or deleted.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260715094751069.png" alt="Codex Follow-up behavior settings" style="zoom:33%;" />

In the Codex CLI, pressing `Enter` when the task is running is Steer, and pressing `Tab` is Queue.

## Put the pieces together

The following prompt connects the previous four parts:

```text
A one-page project status report is prepared for the Monday management meeting.

Use the latest project plan in Drive and project-related decision-making and progress on the Slack channel. The decisions and next steps required from management are presented first, followed by a summary of project progress, risks, responsibility and deadlines.

The approved dates and budget figures remain unchanged. If information conflicts or is missing, indicate clearly. Only generate drafts, do not send or publish them.

Before completion, check whether each of the next actions has a responsible person and a deadline.
```

The goal is to produce a one-page project report; the context comes from Drive and Slack; the output describes audience, length, and content order; the boundaries protect date, budget, and publishing permissions; and finally, one more check is added.

## Use voice dictation

Codex supports voice dictation. Press and hold `Ctrl + M` while the input box is visible, then speak directly.

It will first convert speech into text in the input box. You can check and modify it to make sure there is no recognition error before sending it. It's more like voice input and doesn't skip you and go straight to it.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260715111534786.png" alt="Voice dictation for ChatGPT desktop app" style="zoom:50%;" />

## Chat prompt word examples

Chat is great for asking questions, discussing ideas, drafting essays, and making everyday decisions.

The entrance to Chat is directly in the Codex, as shown in the example below

![image-20260718150221446](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718150221446.png)

Chat mode is suitable for quick questions and answers.

**Understand a topic**
> Explain what compound interest is to someone who has never invested before, use a specific example, and explain the financial terms that appear in it.

This example gives an audience and a way to explain. It does not stipulate how many paragraphs it must be divided into, nor does it require formulas to be taught first.

**Draft and revise text**
> Draft a friendly email since I'm traveling and need to decline this invitation. Keep the word count within 120, and express your willingness to participate in similar activities in the future.

The tone, reason for rejection, and length of the email are all clearly stated. Once generated, you can basically change the name and send it directly.

**Compare options**
> Compare these two cell phone plans for someone who travels abroad twice a year. Start by tabulating the important differences, then recommend one, and describe the trade-offs you need to accept.

There is no unified answer to which one is best. Taking into account the users and travel frequency, this recommendation is based on evidence.

**Make an executable plan**
> Plan five weeknight dinners, each taking less than 30 minutes to prepare. Avoid the peanuts, reuse ingredients across meals, and finally put together a shopping list.

The practicality of this prompt is that it takes into account time, allergens, procurement and ingredient reuse at the same time. You can use this result to buy groceries directly.

## Prompt words in Work mode

Chat mode is suitable for short questions, simple rewriting, brainstorming, and writing drafts. Work mode is more suitable for tasks that require multiple pieces of information, multiple tools, a series of operations, or ultimately generate larger deliverables.

When using Work mode, state the desired results, provide source material, identify the audience, and tell it how you plan to check the results. You can ask ChatGPT to plan first, then collect data, create files, and check before completion.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718150332453.png" alt="image-20260718150332453" style="zoom:50%;" />

### Use Work Mode effectively

Work mode is suitable for time-consuming tasks, repetitive tasks, and future reusable files.

**Convert raw data into finished documents**
> Using the attached quarterly report, create a management briefing and a set of six-page presentations. The readers are company management. Start by writing the three decisions they need to make, distinguish the reported facts from your analysis, cite the source document for each number, and check that the brief and presentation are consistent before finishing.

This type of task is most likely to cause inconsistencies between the two documents, so cross-checking before completion is critical.

**Do research for decision making**
> Researching three customer service platforms for a 50-person company. Compare pricing, security, integration capabilities, and migration costs with the latest information. Deliver a recommendation memo with links to sources, key assumptions, and questions to confirm before signing the contract.

The research task requires writing out the evaluation dimensions and decision-making, so that what you get is a material that can assist decision-making, not a three-paragraph product introduction.

**Coordinate a release**
> Create a release plan based on the product description in the attachment, including timeline, owners, dependencies, risks, draft announcements, customer FAQs, and release day checklist. Highlight any missing decisions before producing the final document.

There are many people and documents involved in the release plan. If there is a missing person or key decision, things will get stuck later. It is more practical to let Work mode mark the gaps first than to generate a plan that looks complete but cannot be executed.

For repetitive tasks, you can write the Prompt in ordinary Chat first, and then execute the scheduled task after getting the results you want.

## Codex prompt word

The entrance to Codex is the one we are most familiar with.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718150811012.png" alt="image-20260718150811012" style="zoom:50%;" />

Whenever you need to work on code, a code base, or a development tool, just head to Codex.

An excellent Codex Prompt should clarify the target behavior, point out the relevant code or reproduction steps, retain important constraints, and explain how to verify the results.

For multi-step tasks, you can enter `/plan` first, let Codex investigate and propose a solution, and then decide whether to edit it.

When Goal mode is available, use `/goal` to set ongoing goals after plan confirmation.

### How to read these examples

Each example at the back of the official website explains four things: when to use it, which interface in IDE/CLI/Cloud it is suitable for, what context the user needs to provide, and finally how to verify.

IDE extensions automatically bring open files with them. It is best to write the path explicitly in the CLI, or attach the file via `@` and `/mention`.

Codex runs in a sandbox. When local files, networks or external operations exceed permission boundaries, they will be processed according to the current approval policy.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718151137613.png" alt="image-20260718151137613" style="zoom: 67%;" />

### Understand the code base

When you have just taken over a project, read about a service you are not familiar with, or need to understand the protocol, data model, and request process, you can let Codex explain the code first.

#### IDE extension workflow (fastest way to explore locally)

Open the relevant file, select the code of interest if necessary, and enter:

```text
Explains the full flow of the request in the selected code.

Please include:
- What's in charge of every relevant module?
- Where is the data verified?
- One or two questions that need attention when changing these codes.
```

**Verification:**Let Codex organize the request process into numbered steps and list the documents involved.

#### CLI workflow (good for keeping records of conversations and commands)

Run `codex` in the project root directory and tell it explicitly which files to read:

```text
I need to understand the protocol for this service. Read @foo.ts and @schema.ts, explain the schema and the request and response process. Focus on distinguishing between mandatory fields, optional fields and backward compatibility rules.
```

The CLI retains conversation and command output. If the path is long, you can use `@` to automatically complete it, or you can use `/mention` to attach the file.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718151552759.png" alt="image-20260718151552759" style="zoom: 67%;" />

### Fix bug

When a bug can be reproduced locally, the most useful information is the reproduction steps and constraints.

#### CLI workflow (closed loop of reproduction and verification)

There is a bug below: the page save button cannot be used after refreshing.

```text
Bug: Sets the page to " save " to show success, but replaces the switch with a new page.

Revert:
1. Run npm run dev
Open /settings
3. Modifications
4. Click Save
5. Refresh pages and observe switches

Binding:
- Don't change the API structure.
- Try to make minimum modifications.
- A return test when conditions permit.

Re-emerge the problem, reposition the cause and modify it. After completion, re-execut the recurrence step, run the smallest relevant set of tests and report the commands and results.
```

The user is responsible for providing reproduction steps and constraints. Codex is supplemented with command output, discovered call locations, and stack information.

**Verification**: After modifying the code, re-operate the original error process to confirm that the bug has disappeared; then run the code inspection and related tests; finally, tell me which commands were actually run, whether each command was successful, and how many tests were passed.

#### IDE extension workflow

Open the file you suspect is problematic and its most recent caller, then type:

> Find out why the interface says saved, but the data is not persisted. Once fixed, tell me how to verify in UI.

This type of prompt is suitable for when the scope of the problem is already relatively small and only specific code needs to be located.

### Write tests

When writing tests, first clearly explain the test objects and scope. Codex will refer to existing testing habits in the code base.

#### IDE extended workflow (based on selected code)

Open the file containing the target function, select the function code, select "Add to Codex Thread" through the command panel, and then enter:

> Write unit tests for this function, following the conventions used by other tests in the project.

The selected line of code and the currently open file will be used as context and do not need to be copied again.

#### CLI workflow (state path and scope in Prompt)

You can directly write the function name and path in the CLI:

> Add tests for the `invert_list` function in @transform.ts, covering both normal paths and edge cases.

If there are multiple functions with the same name or similar names in a file, add the line number range or calling location.

### Prototype based on screenshots

A screenshot can show layout, fonts, and spacing, but it doesn't tell Codex what technology stack it should use, nor does it show hover, validation, and keyboard interaction.

Send the image and text to Codex together, and it will get the complete input.

#### CLI workflow (picture + prompt)

Save the screenshot to the project, for example `./specs/ui.png`, start Codex, drag in the image, and then enter:

```text
Create a new dashboard based on this picture.

Binding:
- Use React, Vite and Tailwind
- Use TypeScript
- Try to match space, font and layout in screenshot

Output:
- A new route or page that can render the UI Noodles.
- Small components required
- A README.md with local running methods
```

**Validation:**Let Codex start the development server and tell you the local URL and route to view the prototype.

#### IDE extended workflow (image + existing file)

Drag the image into the task, open the page with the closest style in the project, and then enter:

> Create a new settings page, targeting the attached screenshot, and following the design and visual patterns used by the other files in this project.

This way Codex can see the target diagram and refer to the components and styles of the existing project.

### Iterate the UI with real-time updates

After the page is running, you can ask Codex to change only a small piece of content at a time, and refresh the browser each time to see the results.

#### CLI workflow (run Vite, then iterate with short prompt)

Run `npm run dev` in a separate terminal and let Codex come up with two or three style improvements first. After selecting a direction, narrow the range:

```text
Adopt programme 2.

Change header only:
- The font is more editorial.
- I'll add a note.
- Make sure it's still moving.
```

You can continue writing in the next round:

> Keep the layout the same, simplify colors, remove redundant borders, and reduce visual distractions.

**Verification:**Refresh the browser after each modification. Submit modifications that you are satisfied with in a timely manner and revoke those that are not satisfactory. If you have manually modified or rolled back a file, you must also tell Codex to avoid being overwritten in the next round.

### Leave refactoring to the cloud

For complex refactorings, you can first understand the code and determine the solution locally, and then transfer the time-consuming implementation to the cloud.

I didn't know about the cloud function before, but I only found out about it this time.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718160236390.png" alt="image-20260718160236390" style="zoom:50%;" />

After connecting to GitHub, your GitHub projects will be synchronized, and then a cloud environment will be created based on the projects on GitHub.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718160426299.png" alt="image-20260718160426299" style="zoom:50%;" />

Once connected, the option to work in the cloud will appear on your local machine.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260718160901345.png" alt="image-20260718160901345" style="zoom:50%;" />

#### Local Planning (IDE)

Submit or temporarily save the current modifications first to ensure that the differences can be seen clearly later. Then let Codex plan:

```text
$plan

Reconstruct the authentication subsystem:
- Split token resolution, session loading and permission determination
- Reduce recycling dependence
- Improve testability

Binding:
- Don't change the user's visible behavior.
- Public API, steady.
- A phased relocation plan.
```

After the plan is out, continue to ask: Which files will be moved specifically for each milestone? How to roll back on failure? What is most needed in the local planning phase are entry files, module boundaries and dependencies.

#### Cloud delegation (IDE → Cloud)

After you set up the Codex cloud environment, select the cloud environment below the input box, and then send Milestone 1 in the implementation plan. New cloud tasks will bring the plan and context of the current task.

Check the diff after the implementation is complete and continue to modify if necessary. You can create PRs from the cloud and pull changes back for local testing.

Cloud tasks run in an isolated environment. The Agent stage has no Internet access by default unless you explicitly enable it in the environment settings.

### Conduct local code review

Before committing code or creating a PR, you can ask Codex to check the current working tree.

#### CLI workflow (review work tree)

Start Codex in the project root directory and run:

```text
/review
```

You can also add points of interest:

```text
Focus on extremes and security issues
```

After repairing based on feedback, run `/review` again to confirm that the related issues have been resolved.

### Review GitHub Pull Request

If you don't want to pull the branch locally, you can trigger the Codex review directly on GitHub. The premise is that the repository has enabled Codex Code review.

#### GitHub workflow (triggered by comments)

Open a Pull Request and leave a comment:

```text
@codex review
```

When you need to pay attention to security issues, you can write more clearly:

```text
@codex Examine security gaps and security risks
```

### Update documentation

Documentation tasks should also clearly state the modification scope and verification method. Just talking about updating documents, Codex can easily rewrite a large piece of it.

#### IDE or CLI workflow (local editing and verification)

Determine the document that needs to be modified, open it in the IDE, or use `@` to specify the file in the CLI, and then enter:

> Updated advanced functionality documentation to add authentication troubleshooting instructions and verify that all links are accessible.

After the Codex is complete, the final step is to read the rendered page.

References:

- [OpenAI: Prompting](https://learn.chatgpt.com/docs/prompting)
- [OpenAI: Plugins](https://learn.chatgpt.com/docs/plugins)
- [OpenAI: Personalization settings](https://learn.chatgpt.com/docs/reference/settings#personalization)
