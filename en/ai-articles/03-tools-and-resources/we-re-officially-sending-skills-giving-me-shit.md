# We're officially sending Skills, giving me shit.

[English](./we-re-officially-sending-skills-giving-me-shit.md) | [Chinese Original](../../../ai-articles/03-tools-and-resources/%E7%BB%99%E5%A4%A7%E5%AE%B6%E8%AF%A6%E7%BB%86%E4%BB%8B%E7%BB%8D%E4%B8%8B%20weread%20skills.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-19

On weekends, Weibo officially released a list of them.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260517222659274.png" alt="image-20260517222659274" style="zoom: 33%;" />

I have to say that the wave of wi-fi reading is at the forefront.

This is the one where you talk about how to configure a Twitter book -- the ones that are going to write.

First you need to log in. https://weread.qq.com/r/weread-skills, click Quick Setup.

![image-20260517223220703](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260517223220703.png)

And then, "Down!"https://cdn.weread.qq.com/skills/weread-skills.zipInstall the skill command to throw directly to your AI.

I'm here to get Codex to help me finish.

After downloading, it's actually a skills bag that includes these skills.

![image-20260517224136911](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260517224136911.png)

In short, these skills are the kind of things that can help you do:

1. **Log search / content search**
Supporting search of e-books, web pages, audio/monographs, authors, full text, book lists, public signs, articles, etc.

2. ** Read books**
Read book details, catalogue chapters, reading progress, cumulative reading time.
3. ** Bookcase**
Draws your bookcase list, statistics ebooks, audio/monographs, article collections, public/private readings.
4. ** Reading statistics**
This week, this month, this year, total reading time, number of reading days, most read books, preference classification, preference time, preference for author, etc.
5.** Export/view notes underlined**
All books with notes, single book lines, personal ideas/points, hot lines, underlined ideas, etc. can be viewed.
6. ** Open book reviews**
Check the full, recommended, up-to-date, positive and general points of a book.
7.** Recommendation**
Get personalized recommendations, or find similar books based on a book.
8.** Generating Micro-Learning App Jump Link**
Can you spell "reading"?

The limitations are also clear: it is currently primarily ** reading/search type capability** and does not see such writing exercises as adding books, deleting books, writing notes, modifying book reviews; and ** cannot export bookmarks**, only counting the number of bookmarks, underlineding and ideas that can be exported.

In other words, basically, you've got the ability to read and query on Twitter, and this skills is all set for you.

After downloading, you need to log in and read.`api-key`.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260517233059072.png" alt="image-20260517233059072" style="zoom: 50%;" />

For security reasons, it would be preferable not to throw api-key directly to AI, so it would be better to configure api-key for this step.

```
Report WEREAD API KEY
```

Add one directly to ~/.zshrc and then source ~/.zshrc on it.

When the configuration is complete, you can get AI to help you count, or you can count directly in the cli.

For example, I can ask AI:

```prompt
Search some big model books. Ten.
```

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518065923701.png" alt="image-20260518065923701" style="zoom: 50%;" />

For example, I could show him how far I've been reading The Man's Book:

```prompt
Let's see how far I'm going to go in reading the phantom.
```

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518071508740.png" alt="image-20260518071508740" style="zoom: 67%;" />

Note in brackets.

He can also read your bookcase information.

I can read this year.

```prompt
Let's take a look at my readings this year.
```

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518072029382.png" alt="image-20260518072029382" style="zoom: 67%;" />

Uh, uh, it's a little embarrassing to see the result.

It's not a very good year to read books, it's been on AI now, and it's still with the baby.

No more external reasons. No, no, no, no, no. Plan. Can't just output, no input.

I could show him the book reviews.

```prompt
Check all book notes underlined
```

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518072449985.png" alt="image-20260518072449985" style="zoom: 50%;" />

I can even show him some book reviews.

```prompt
Take a look at the public review of Lu's Episode.
```

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518073339078.png" alt="image-20260518073339078" style="zoom: 50%;" />

You can also get him to recommend some good books in different directions.

```prompt
It's not just AI LLM.
```

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518081838985.png" alt="image-20260518081838985" style="zoom: 50%;" />

That's a pretty good recommendation. I'm really interested in these books.

The last skill skills are kind of interesting.

This function is essentially: ** to spell a location in a Twitter book as a deep link to the beginning of the app.**

If you click this link, the system will try to open micro-intelligence app and jump to the corresponding book, chapter, or even a underlined position.

I'm telling you, it's a little bit of a function, but it's a function that can achieve a URL-level fission effect and drive all traffic into micro-intelligence.

For example, I can make a URL share of book reviews.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518085410635.png" alt="image-20260518085410635" style="zoom: 50%;" />

Indeed, this url can open directly.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260518085457292.png" alt="image-20260518085457292" style="zoom: 50%;" />

This is a way for ordinary people to play in their own language.

If you want to play more, Geek, some, there's progress.

---

CLI is an advanced game, not an option

And of course, if you're a programmer, you can do it directly in the command line.

The official skill is actually a unified gateway:

```text
https://i.weread.qq.com/api/agent/gateway
```

When requested:

```text
Authorization: Bearer $WEREAD_API_KEY
```

♪ And then body ♪

```json
{
 "api_name": "/shelf/sync",
 "skill_version": "1. 0. 3"
}
```

You can check the bookshelf.

Like a bookcase.

```bash
curl -sS -X POST "https://i.weread.qq.com/api/agent/gateway" \
 -H "Authorization: Bearer $WEREAD_API_KEY" \
 -H "Content-Type: application/json" \
 -d '{"api_name":"/shelf/sync","skill_version":"1. 0. 3"}'
```

Read statistics:

```bash
curl -sS -X POST "https://i.weread.qq.com/api/agent/gateway" \
 -H "Authorization: Bearer $WEREAD_API_KEY" \
 -H "Content-Type: application/json" \
 -d '{"api_name":"/readdata/detail","mode":"overall","skill_version":"1. 0. 3"}'
```

Search:

```bash
curl -sS -X POST "https://i.weread.qq.com/api/agent/gateway" \
 -H "Authorization: Bearer $WEREAD_API_KEY" \
 -H "Content-Type: application/json" \
 -d '{"api_name":"/store/search","keyword":"The Three-Body Problem","scope": 10,"count": 5,"skill_version":"1. 0. 3"}'
```

But to be honest, I don't recommend it for ordinary users.

Because it's cumbersome.

It is more suitable for two categories of people:

Number one, you want to get your Twitter data into your script.

Second, you want to make your own reading board, for example, by counting how much you read every month, which books you've read and which ones you read most.

If it's just a temporary check, it's enough to just get AI transferred to skill.

---

I think this thing makes a lot of sense. After all, it's not a complex thing.

It didn't help you write.

No automatic reading for you.

And there's no wonder you can understand a book.

But it did a crucial thing:

** It opened your reading data to AI.**

This is different.

Because the data used to be in Twitter were locked in App.

You can see, but it's hard to double.

You can turn, but it's hard to count in bulk.

You can draw lines, but it's hard to turn them into structured notes.

Now with skills, AI can do a lot around your reading data.

It can help you reset.

I can help you clean up.

You can find your own reading preferences.

It'll help you turn fragmentation lines into articles.

It'll help you reconnect the ideas in a book.

That's where I think it's really valuable.

Now your reading records are also connected to the AI workflow.



If this article inspires you to welcome the triads, it can also be forwarded to friends who are equally interested in AI/ Technology/ Development Efficiency.
I'm cxuanAI, which keeps track of AI tools, technology trends, and changes in technology that are of interest.
