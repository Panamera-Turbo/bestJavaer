# Claude Code: Real demand or marketing bullshit?

[English](./claude-code-real-demand-or-marketing-bullshit.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Claude%20Code%20100%E4%B8%87%E4%B8%8A%E4%B8%8B%E6%96%87%EF%BC%9A%E5%88%B0%E5%BA%95%E6%98%AF%E7%9C%9F%E9%9C%80%E6%B1%82%E8%BF%98%E6%98%AF%E8%90%A5%E9%94%80%E5%BA%9F%E8%AF%9D.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-16

# Background

The Anthropic official blog published a technical article on how Claude Code managed sessions and how the 1 million Token context was actually being developed.

To be honest, this topic has generated considerable discussion in the developing community. Some people think it's a breakthrough in engineering, and others ask, "Do you really need it?"

---

What do the authorities say?

The core of Anthropic's blog is the architecture for session management. Three phases:

** Session Initialization** → Read project files, scan directories, build initial context

** Dialogue cycle** → User input → Claude reasoning ** Tool call ** ** results back to context, and each cycle recalculates available space

**Constant session** writing`. claude`Directory to support inter-session recovery

The essence of the system is ** context life cycle management**, not simply the history of dialogue. It will dynamically determine what to keep, what to compress and what to discard.

---

What's on the Internet

Reddit has a direct title: ** "1 million contexts are marketing bullshit for 99% of users."**

That view is valid. The core criticisms are:

Most people's day-to-day development scenes, hundreds of lines of single documents, dozens of documents for a project, are inserted into a 1 million context like a tanker to deliver an take-out - no, no, no.

HN discussion is more rational. It was mentioned that the real value scenario of 1 million contexts is:

- One-time digestion of the entire code library (especially taking over old items)
- Large reorganisation mission, Claude.
- Long-line missions, like letting AI remember all the historical decisions you made on your project.

At the same time, however, practical problems were pointed out: the longer the context, the higher the delay in each API call, the higher the cost. Running a simple mission with a 1 million context equals killing a chicken with a cow knife.

---

# A trade-off judgement

Not everyone's dealing with a 1 million context scenario. But some developers do.

For example, you took over an old project three years ago, the code had no documents, no structure. And that's when a million contexts will make you feed Claude the entire code library once and for all, so that it can understand the relationship between modules. This is a qualitative improvement over document-by-file replication.

And for example, you're going to do cross-file reprogramming, and changing a function will affect 20 files. The traditional way you're telling Claude what to change for each file, Claude may forget; a million contexts allow Claude to see the whole picture, and change is completely different.

** But ** if you're changing small functions and writing scripts on a daily basis, 1 million contexts really don't feel good for you.

It's not technology. It's not a match.

---

# Another focus for the community: costs

The title of a YouTube video is true: ** "Don't use Claude's 1 million context unless you see this"**

Cost is a real problem. The longer the context, the greater the consumption of Token per request. While the sense may be weak during the official period, the cost of long-run context session becomes the selection threshold after a formal charge.

And that's why many people are more concerned about when it should be used, and when it should not be.**

---

# Details from official documents

Claude Code's model profile document mentions that 1 million frames are made through Claude 3. 5 Sonnet, supporting direct opening in the code. claude. com project.

Practically, the user can configure whether to enable a 1 million context mode in the project. When enabled, Claude automatically manages the context window, including a summary of the long output, a percentage of the dynamically adjusted dialogue history, and gives priority to maintaining code files over dialogue records.

This means that context space is also officially recognized as a scarce resource that needs to be carefully managed.

---

A judgment

One million words of context are not in vain, but not for everyone.

Its target users are:** AI is needed while understanding a lot of information.** The task of taking over large code repositories, complex re-engineering and cross-module analysis can significantly reduce communication costs.

But if your day-to-day job is to write functions in a single document, to change the API, a million contexts means more to you than psychological consolation, not real efficiency.

At the marketing level, Anthropic promotes that $1 million really attracts eyes. In real value, it is selectively released to developers with corresponding needs.

** Not everyone needs an elephant, but you can't deny that an elephant works better than an ant when it's needed.**

---

Sources:
- [Using Claude Code Session Management and 1M Context](https://claude.com/blog/using-claude-code-session-management-and-1m-context)
- [1M context window is basically marketing BS for 99% of users - Reddit](https://www.reddit.com/r/ClaudeCode/comments/1qxaddx/1m_context_window_is_basically_marketing_bs_for/)
- [HN Discussion on Claude Code 1M Context](https://news.ycombinator.com/item?id=46902427)
- [Claude Code 1M Context Window: Cost, Limits, and When to Use](https://www.claudecodecamp.com/p/claude-code-1m-context-window)
- [Claude 1M Token Context Window: What It Means for AI Agents](https://www.mindstudio.ai/blog/claude-1m-token-context-window-ai-agents/)
