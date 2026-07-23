# Grok Build Was Widely Criticized, Then Elon Open-Sourced It

[English](./grok-build-was-criticized-then-open-sourced.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Grok%20Build%20%E8%A2%AB%E4%BC%97%E4%BA%BA%E5%94%BE%E9%AA%82%EF%BC%8C%E7%BB%93%E6%9E%9C%E8%80%81%E9%A9%AC%E6%8A%8A%E5%AE%83%E5%BC%80%E6%BA%90%E4%BA%86.md)

> Date: 2026-07-22

Grok Build was really at the forefront of the trend in the past two days.

Let me first review the whole thing for you.

A [Traffic Analysis](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) for `grok 0.2.93` showed that Grok Build uploaded the entire Git repository during the test, including files and Git history that were not read by the Agent; the researcher also found the `.env` string used for testing in the uploaded content.

This analysis does prove data transmission, server reception and storage, but it does not prove that xAI must have used these data to train the model.

It is normal for cloud AI programming tools to send the code required for the task to the model.

The controversy lies in the fact that the scope of the code it passes out far exceeds the current task needs, and the installation and quick start documents at that time did not clearly explain the entire library upload mechanism.

This is what makes everyone upset and reviled.

SpaceXAI subsequently announced that it would add `/privacy` in the Grok Build CLI in response. This command is used to view or toggle privacy and data retention status.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716081611791.png" alt="SpaceXAI responds to Grok Build data issues" style="zoom:50%;" />

*Source: SpaceXAI official response screenshot*

When you type `/privacy` on the command line, the interface will clearly mark that the code will not be used for model training.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716081959745.png" alt="Grok Build CLI privacy status" style="zoom:50%;" />

*Source: Grok Build CLI screenshot*

Here is a reminder for everyone:**will not be used for training, which does not mean that the data will not leave the machine at all.**
To understand the code, the cloud model always needs to receive some context. The previous traffic analysis also found that in the version tested at that time, after turning off Improve the model, the entire database upload still occurred.

---

Then, today, July 15, SpaceXAI announced that it would open source Grok Build and reset the usage quotas of all users.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716082108557.png" alt="SpaceXAI announces open source Grok Build" style="zoom:33%;" />

*Source: SpaceXAI official account screenshot*

Lao Ma also responded positively to this matter.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083825776.png" alt="Elon Musk responds to Grok Build privacy concerns" style="zoom:50%;" />

*Source: Screenshot of Elon Musk’s public response*

This open source seems to involve a large number of open source enthusiasts. From another perspective, it is also clearly tinged with crisis response and trust repair.

Because the time for scolding and public relations repair is too close.

The default retention is turned off, historical data is deleted, the source code is disclosed, and the quota is reset. Several measures appear at the same time. I don’t believe it if you say this has nothing to do with the previous privacy controversy.

---

Many people see that Grok Build is open source, and it is easy to understand that the Grok model is also open source. Still different.

[Official warehouse](https://github.com/xai-org/grok-build) is open to Grok Build's Rust CLI/TUI, Agent runtime and tool framework, and the first-party code adopts the Apache 2.0 license.**Grok 4.5’s model weights, training code, and xAI cloud services are not subsequently released.**
![Grok Build GitHub repository and license](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716082850739.png)

*Photo source: Grok Build homepage*

Strictly speaking, this is truly open source. Apache 2.0 permits use, modification, distribution, and commercial derivatives.

And it doesn’t just throw out an empty shell. You can build the CLI from source code and view the implementation of file reading, command execution, sandboxing, tool invocation, and uploading.

The official documentation also supports configuring custom models and `base_url`, so you can connect this Harness to other APIs, or to local inference services with compatible interfaces.

I took a look at Grok Build’s open source repository, and the official website has made it very clear:

![Grok Build repository contribution policy](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083124561.png)

*Source: Grok Build GitHub warehouse screenshot*

- The warehouse currently only has one historical commit;
- The official stated clearly that it does not accept external Pull Requests and proactively submitted security patches;
- There is no official Release corresponding to the source code repository on GitHub;
- Whether the open source code corresponds verbatim to the official binary downloaded by users also needs to be proven by reproducible builds, version labels, and signature mechanisms.

The official statement is very clear directly in [CONTRIBUTING.md](https://github.com/xai-org/grok-build/blob/main/CONTRIBUTING.md).

![image-20260716095816563](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716095816563.png)

So I understand Grok’s current route is this: you can read it, compile it locally, fork it, or make your own version based on Apache 2.0;

However, the official does not plan to develop the main warehouse together with the community for the time being.

This also explains why the repository does not open the usual public issue and PR processes.

There is a separate `SECURITY.md` channel for security issues, and general feature suggestions and code contributions cannot enter the main warehouse for the time being.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716100013245.png" alt="image-20260716100013245" style="zoom:50%;" />

Let me be harsh: I’ll show you the code, and you can fork it as you please, but the official doesn’t want to accept your shit code for the time being. . .

---

Grok Build's open source this time is not a precedent. There have been [Codex CLI](https://github.com/openai/codex) and [Gemini CLI](https://github.com/google-gemini/gemini-cli) before. They also have no model weight behind the openness. What is open are Agent CLI and running framework.

**Codex CLI：**
![Codex CLI GitHub repository](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083543195.png)

*Source: OpenAI Codex GitHub repository screenshot*

**Gemini CLI：**
<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716083626387.png" alt="Gemini CLI GitHub repository" style="zoom:50%;" />

*Source: Google Gemini CLI GitHub repository screenshot*

The difference is mainly in community governance.

Both Codex and Gemini CLI maintain a complete public submission history, and also open Issues, Pull Requests, and discussion forums.

The Gemini CLI's README even explicitly invites the community to submit code improvements.

In other words, when you should raise an issue, raise an issue, and when you should raise a PR, raise a PR.

As for Company A’s Claude Code, the source code has indeed been dug out. I believe everyone has a copy.

So this time Grok build is indeed open source, but currently, they don’t want to be a community.

However, I saw that almost all of the posts on a well-known social platform were boasting, and few people mentioned that the official did not accept public PR. This is one of the few comments I've seen that directly addresses the issue.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716091457691.png" alt="Comments about Grok Build not accepting external contributions" style="zoom:50%;" />

*Source: Screenshot of public comments on social platforms*

---

These are sweet times indeed these days if you use Cursor.

Cursor directly doubled the model usage. Grok Build then chooses to directly reset the user's quota.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260716090038075.png" alt="Cursor offers double the amount of Grok 4.5" style="zoom:50%;" />

Lao Ma's set of operations does sound very tempting. It opens the source code, resets the quota, and the Cursor directly doubles the quota.

So I firmly believe that this open source is indeed a public relations victory. It quickly diverted public attention.

So the biggest value of open source this time, I think, is actually changing part of the trust from company commitments to inspectable source code.

However, it can neither erase the upload behavior that has been caught before, nor can it independently prove that the current official binary has completely stopped uploading the entire library.
