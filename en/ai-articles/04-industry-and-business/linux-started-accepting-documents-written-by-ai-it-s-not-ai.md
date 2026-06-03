# Linux started accepting documents written by AI? It's not AI.

[English](./linux-started-accepting-documents-written-by-ai-it-s-not-ai.md) | [Chinese Original](../../../ai-articles/04-industry-and-business/Linux%20%E5%BC%80%E5%A7%8B%E6%8E%A5%E5%8F%97%20AI%20%E5%86%99%E7%9A%84%E4%BB%A3%E7%A0%81%E4%BA%86.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-21

I saw a lot of talk today about Linux finally accepting the code submitted by AI. What does the worst master of AI think about this?

The reaction seems to be that the Linux kernel community finally lets itself go, and even the ones that AI wrote can get to the main line.

I looked into some of the information and found that that was not the case.

What the Linux community really accepts is not "Ai wrote something natural and credible," but a more realistic logic:

** You can use AI, but you have to take full responsibility for it like you do with your own code and document.**

![image-20260413100845147](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260413100845147.png)

In other words, it's not AI, it's "AI as a productivity tool." Communities have never handed over responsibility to models, and responsibility remains firmly anchored.

---

If you change the question to "Linux can't accept AI-assisted documents, patches, and even codes," the answer is clear:** Yes.**

But there's only one condition and there's no ambiguity:

** The person submitting the report must have personally examined it, understood it and signed it.**

![image-20260413100743818](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260413100743818.png)

It looks conservative, but it's advanced. Because it is not caught in two common error zones:

1. To turn AI into a flood beast and try to shut it down completely.
To use AI as an exoneration tool, as if it were "not I wrote it, it was modeled" to throw the pot out.

The Linux community has no choice. It chooses the third path: ** It is allowed, but it is your responsibility.**

---

# Why "document acceptable" does not mean lower threshold

A lot of people get the wrong idea, they think the document is less risky than the code, so it's easier for AI to write the document.

Of course, that is true, but remember, documents enter a high-threshold engineering community and are not just as simple as words.

In Linux, the document has at least three layers:

![image-20260413100718346](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260413100718346.png)

- It explains the design intent.
- It binds subsequent defenders to understand borders.
- It will in turn affect code review and community collaboration.

That is to say, a low-quality document does not necessarily destroy the system as directly as a bad code, but it may well lead the discussion in the direction of slowly raising maintenance costs.

So in terms of governance logic,** AI writing documents and AI writing codes are not two completely different sets of questions.** They share the same bottom line:

> As long as content enters the formal chain of collaboration, there must be a subject of human responsibility.

This is the most interesting part of Linux's change of attitude.

---

# The community really cares, never "Is it AI wrote"

If you look only at the surface, you think the community is arguing about whether to mark AI generation.

But the deeper contradictions are simply not labeled.

Linus' attitude has been quite straightforward: ** Document regulation does not stop those who were otherwise unorthodox.**

The meaning behind this sentence is really heavy.

Because a community is really scared, it's never "someone uses AI." The community is afraid of the following:

- The submitr gives it up without reading it.
- AI repackaged old bugs, wrong patterns, licence risks.
- Maintainers need to devote more energy to identifying patches and instructions that simply "look like that".

So don't interpret the question as "Ai documentation fit." More precisely:

** Linux is accepting AI participation in the contribution process, but rejecting unaccountable AI outputs.**

---

# That malicious submission in 2021, why is it still affecting community judgment today #

This is not the case with the University of Minnesota.

It was not "bugs for patches" that made the community the most angry at the time, but rather a deliberate attempt to disguise leaky submissions as normal repairs and then to package them as research results.

The legacy of this is very deep:

![image-20260413100651125](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260413100651125.png)

- It makes the community aware that the review mechanism itself will be used.
- It proves that the submission is "proximate" and does not mean that it is really safe.
- It makes defenders naturally unsatisfied with explanations like "you say you're good."

And that's why today when I was talking about AI, the Linux community almost instinctively brought responsibility back to people.

As history has proven:

** The real danger is not the instrument itself, but the author of the instrument to escape responsibility.**

---

# Linux's answer to governance is modern

In many organizations, the first reaction to AI is usually two:

- Either completely disabled.
- Either let it go completely and leave it to the front-line team.

Linux didn't do it.

Its approach is more like a governance model for mature engineering organizations:

![image-20260413100631597](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260413100631597.png)

1. Acceptance of AI has entered a reality stream.
"Whether or not to use AI" is not considered the sole test.
3. To maintain accountability, signature, censorship and traceability mechanisms on human developers.

Why is this mechanism important?

Because it brought the problem back from the "tool ethics debate" to "the distribution of engineering responsibilities".

That's what a big open source project really cares about.

---

# Real interesting change: AI is not just writing, it's beginning to be reviewed

If things stop at "AI to help people write patches, notes, documents," it's not really a turning point.

More importantly, AI is now entering another role:

** It's not just a content generator, it's starting to be a review layer.**

Sashiko of Google Engineer Open Source is typical. It does not automatically submit codes, but does multi-stage reviews for Linux kernel patches to dissect the structure, security and risk.

This is a very important signal:

The probability of a truly sustainable stream of work in the future is not "AI writing, human passivity" but:

**AI writes first floor, AI reviews first floor and humans make final judgements.**

![image-20260413100429807](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260413100429807.png)

It's like a scale-operated production system.

---

What's the most realistic revelation for developers

If you're an ordinary developer, this is actually a very clear test.

From now on, you'll be using AI to write code, comment, document, and it's not "Is AI useful" but these three things:

- You haven't examined it yourself.

- Can you explain why it's written like that.

- Something's wrong. This is not what you're willing to sign for.

As long as these three do not pass, the more AI is involved, the greater the risk.

On the other hand, if you can get through all three levels, then it's less important for AI to write codes, submit instructions, or design documents.

Because at the time it was an instrument, not an author.

---

# Write at the end

So, "Linux can accept the documents written by AI?" The most accurate answer is:

** Linux can accept AI ' s involvement in writing, but not without the responsible person.**

That doesn't sound radical, but it has a lot of weight.

It means that a mature community has finally moved away from "AI should or should not come" and has started to design "how, how, how, how, how, and how, the quality of the responsibilities after AI has arrived".

This is more important than mere support or opposition.

Thus, AI ' s entry into open-source communities is no longer a trend judgement, but a governance capacity issue.

The real watershed is not about who uses AI first, but who builds a collaborative approach that is accountable to people, that processes can be traced and that risks can be stopped.

Linux now gives one answer.
