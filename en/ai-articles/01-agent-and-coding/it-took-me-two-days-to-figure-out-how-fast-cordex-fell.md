# It took me two days to figure out how fast Codex fell!

[English](./it-took-me-two-days-to-figure-out-how-fast-cordex-fell.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E6%88%91%E8%8A%B1%E4%BA%86%E4%B8%A4%E5%A4%A9%E6%97%B6%E9%97%B4%EF%BC%8C%E7%BB%88%E4%BA%8E%E6%8A%8A%20Codex%20%E9%A2%9D%E5%BA%A6%E6%8E%89%E5%A4%AA%E5%BF%AB%E7%9A%84%E9%97%AE%E9%A2%98%E6%95%B4%E6%98%8E%E7%99%BD%E4%BA%86%EF%BC%81%EF%BC%81.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


It's estimated that a lot of people, like me, have recently been troubled by the problem of the Codex scale being too expensive.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260530154325715.png" alt="image-20260530154325715" style="zoom: 50%;" />

I used the Pro 20x package, and the traffic was almost exhausted. The version of 5. 5 was just released, and I've been filling it with a 5. 5 xheigh fast mode, which felt good, working fast and well, and falling too fast.

But about two weeks ago, I found that daily consumption was significantly faster than before. And even more strangely, even if I hadn't touched it at all, the rest of the week would have dropped by 15 to 25 percent. I did not change the project under way, nor did I set up any automated operations, and these consumption records were not visible in the session log.

This situation continued even after the official claim of "Bug repair". Once, my remaining amount fell directly from 76% to 51% overnight.

To figure out what happened, I happened to see this post in OpenAI's developer's community (see end of text):

---

The post reflects a constant consumption of Codex when it is idle and not used voluntarily.

Following this line, I found some discussions, such as "Codex Credits disappearing", "Post-replacement Codex is abnormal," and there are reports that even a small number of missions can cost a lot of money.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260530154429242.png" alt="image-20260530154429242" style="zoom: 50%;" />

Personally, the core issue is not just a large mission that eats a lot of Credits. The point is, even if I didn't start any meaningful new work on my own initiative, as long as Codex is open/operational, Credits seems to have been quiet.

This has been repeated. Every night, as long as I'm open, Codex, the amount will be reduced, until now. Every time I leave the computer for a while, I come back, and there's another amount that disappears. My workflow has not changed in substance, and Codex is used in a similar way, including as a system monitor/monitor for my home.

Since the launch of the 5. 5 version, however, both the weekly grant and the additional Credits purchased themselves have been burned at an extremely rapid and unpredictable rate. I was really surprised by the amount of consumption. In order to be able to continue, I started paying for the additional Credits, but the additional Credits also started to disappear in the same weird way.

Take one example at night: Codex runs as usual, has a surveillance/supervisory mission, and by morning about 20% of Credits is missing. This is no exception. The same thing happens every night as long as I leave the computer open.

The most serious problem here is the amount of leakage under idle/backstage status. If Codex does model calls, retests, summations, surveillance actions, tool calls, context updates, or any other act that does not require my initiative to make a charge, then it should be visible and manageable.

The information currently provided by Codex is not sufficient to allow me to verify where these amounts are spent. I see no clear explanation of why Credits continues to consume only when it opens/ hangs on Codex by task or by session.

------

Later, I saw a solution given:

By saving in`~/.codex/sessions`The session deployment log in the folder to see details about token consumption, and here to check if there is a backstage generated thread at the consumption level.

I've had similar problems before, caused by Codex's memory management mechanism. Every time I open a new Thread, I find that even though the main route is over, it's still falling. The task actually consumed only about 2% of the 5-hour billing window, but it continued to decline by 10% to 12% after the mission was completed. I open it.`.codex`The folder tries to find evidence, and it turns out that there were back-stage threads that were started quietly, which is related to Codex's memory management. When I shut down memory management, the problem was solved.

![image-20260530154121786](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260530154121786.png)

His situation sounded very similar to mine, and he mentioned that the problem disappeared when the memory was disabled. So I finally did two things that seemed to solve my problem:

1. Yes.`/Users/<username>/.codex/config.toml`,`[features]`Below Settings`memories = false`, disable memory functions.
2. So Codex has been able to identify and terminate three seemingly isolated Codex processes (I use mostly command lines, rarely desktop applications because it often goes down in Carden). These processes have been in the background, and seem to have done nothing, but who knows, they may still consume in some way.

Because it was done in the morning, I was afraid to be 100 per cent sure that it would fully address the issue of night consumption, but I did find that my level of availability had been restored to the level that had existed more than two weeks ago. It's been developed recently in a 5. 5 low-intensity (low) mode for one hour, which used to eat more than 5% of the weekly amount, and now I find that it only consumes about 1% of the weekly amount.



Related links:

https://community.openai.com/t/codex-credits-are-draining-while-idle-not-actively-used/1380250

https://www.reddit.com/r/codex/comments/1tnm6ig/i_think_i_fixed_my_rapidly_draining_usage_limits/

https://community.openai.com/t/codex-credits-are-draining-while-idle-not-actively-used/1380250/37
