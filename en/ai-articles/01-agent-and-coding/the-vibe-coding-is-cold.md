# The vibe coding is cold.

[English](./the-vibe-coding-is-cold.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/vibe%20coding%20%E5%87%89%E4%BA%86%EF%BC%8Cwish%20coding%20%E6%9D%A5%E4%BA%86.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-21

In 2025, vibe coding was the hottest word.

After Karpathy came up with it, the whole industry was talking about: you describe demand, AI writes code, you judge, and the results are accepted. This model sounds wonderful and does solve a lot of problems.

But in 2026, the problem began to come to light.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260421152607242.png" alt="image-20260421152607242" style="zoom: 50%;" />

What is the essence of vibe coding? You give AI a general need, AI guess what you want. You said, "Do a login page that feels like a high-end product," and AI gave you a bunch of dark-colour gradients with glass. You said, "Put me a back end," and AI gave you a REST API shelf, and you don't know why.

This way of visualizing, it's fast. But the quality of the code out depends on AI guessing right. That's a surprise. That's a shock.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260421152641388.png" alt="image-20260421152641388" style="zoom: 50%;" />

The fundamental problem with vibe coding is that it's still getting you ** to describe **, rather than **, precisely**. Your message to AI is vague, and the output of AI is naturally vague.

---

Intent is the new syntax

McKinsey, there's one thing I think is true:

> Over the next decade, AI-assisted programming will let developers specify intent through a mix of formal programming languages and natural language

The translation is that for the next 10 years, AI support programming will allow developers to express their intentions through a mix of official programming languages and natural languages.

Note that the core word here is **intent** -- intent.

Everest Group is the new syntax.

Together, these two sentences speak of the same thing: the smallest unit of programming is changing from ** syntax** to ** intention**.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260421152722254.png" alt="image-20260421152722254" style="zoom: 50%;" />

You used to learn programming to express a command in the correct grammar. Now you learn programming, how to describe exactly what you want.

It's not a change in tools. It's a change in the definition of human programming.

---

# the proper name of the wish coding

Someone is giving the phenomenon a proper name: inent-oriented programming, with intent to direct programming.

Its central proposition is that programming language should be infinity to the way people think, not the way machines do it. You're thinking of "seeing the home page after the user logs in" instead of "calling the /mouth/login interface and redirecting it to /home".

This is a very long slide:

- Early: Write machine code.
- Then: write a compilation.
- Then: write advanced languages.
- Now: describe intent in natural language, AI into code

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260421152820950.png" alt="image-20260421152820950" style="zoom: 50%;" />

Each step is programmed in a way that is closer to people's thinking.

So...`wish coding`That name, though it sounds a little ludicrous, is true: you're not writing code, you're making a wish. You said, "I want a login system that works." AI gave you one.

The question of wishing is: you have to make your wish clear.

vibe coding phase, you'll probably say it, AI will guess. Inent-oriented phase, you say it's vague, and AI gives you a vague result.

The difference is that vibe coding is sensory, inent-oriented is specification driven.

---

# Why fire first, inent-oriented later

It's about the evolution of AI capabilities.

The vibe coding can run because the 2024-2025 AI already understands ** probably ** and can generate code that looks like it. This stage of AI's ability is that I guess you might want this, with some tolerance for vague instructions.

But the problem is that it probably doesn't work. The code is often presented with such problems as unresolved border situations, security risks and structures that are not suitable for long-term maintenance. The test runs, and it goes off the line.

What's needed is for AI to understand exactly every word you say and turn it into a strictly corresponding code. You said to consider token's expiry when dealing with co-issues, AI wouldn't miss that detail. You said the error message was to include the original request ID, and AI would not simply write a request to fail.

This precision requires greater AI capacity and more normative expression.

So vibe coding is an AI early product, incent-oriented is an AI mature product. It's not who replaces who, it's AI's ability to step up and the way to make a wish needs to be upgraded.

---

# Augment Code's doing

There's a product called August Code. https://www.augmentcode.com/product/intent, its positioning explains What's happening now?

![image-20260420213142856](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260420213142856.png)

It's the pattern: you give an inent spec, AI dismantles into multiple angent parallel jobs. Auth Token Agent does the authentication module, Gateway Middleware Agent does the gateway validation, and two angents share the same specification document, each of which achieves its own part and ends up in a string.

The key point is not multiple parties, but the instructions you gave are** structured specifications**, not a sentence to add JWT authentication.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260421152935575.png" alt="image-20260421152935575" style="zoom: 50%;" />

Structure means that the format of each field is fixed, the input and output of each interface is fixed and the boundary is fixed. AI does the specifications, and they are accepted when they are completed.

It's not vibe coding, it's inent-oriented.

---

The problem with incent-oriented is that it requires you to figure out what you want first.

The advantage of vibe coding is you can throw a vague idea first, see what AI gives you, and then slowly adjust. This process does not require you to start with all the details.

Incent-oriented requires you to write specifications before AI achieves. This may be a natural process for experienced developers and sometimes a constraint for projects at the exploratory stage.

So it's not a relationship between the two:

- Discovery phase, vibe coding quick validation of ideas
- It's clear. Switch to inent-oriented for solid realization.

That's what McKinsey said.

> For the next 10 years, it's formal programming language + mix of natural languages, not pure natural languages. Formal is part specification and natural language is part expression of intent.

---

## 

When I myself was using the Alcoding tool, it was clear how this transition felt.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260421153016806.png" alt="image-20260421153016806" style="zoom: 50%;" />

First with vibe coding, I dropped to help me make a blog system, AI, give me a run-away shelf. I feel good.

But as it goes on, I find that ** can run** and ** can use** much different things: there's a problem with the classification labels, the boundaries of the search function are not being addressed, and the SEO's meta labels are not standard. AI helped me fast-track a shelf, but I need to recheck every detail.

Then I changed the way I thought about the functional modules of my blog system, the input outputs of each module, how to handle the errors. Think about it, tell AI in a structured way.

The results are completely different. AI gave something right from the start, and I didn't have to fix it.

Not AI changed, my expression changed.

---

## 

vibe coding isn't cold, it's upgraded.

It was not abandoned, it evolved into inent-oriented programming. The way to make a wish has changed from a general description of feelings to a precise description of specifications.

The essence of this shift is not a change in tools, but a change in the way people use AI: the higher the quality of the information you give AI, the higher the quality of the results AI gives you.

Vibe coding is AI to help you explore quickly, inent-oriented is AI to help you achieve exactly.

Both are more practical than either.



Sources:
- [Intent is the New Syntax: Why Vibe Coding Represents a Shift - Everest Group](https://www.everestgrp.com/blog/intent-is-the-new-syntax-why-vibe-coding-represents-a-shift-in-software-development-blog.html)
- [Vibe Coding: Toward an AI‑Native Paradigm - Vinay Bamil](https://arxiv.org/html/2510.17842v1)
- [Build with Intent | Augment Code](https://www.augmentcode.com/product/intent)
- [Intent-Oriented Programming: Bridging Human Thought and AI Machine Execution](https://kotrotsos.medium.com/intent-oriented-programming-bridging-human-thought-and-ai-machine-execution-3a92373cc1b6)
- [Unlocking the value of AI in software development - McKinsey](https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/unlocking-the-value-of-ai-in-software-development)
- [Vibe Coding in 2026: How AI Is Changing the Way Developers Write Code](https://daily.dev/blog/vibe-coding-2026-ai-changing-how-developers-write-code)
