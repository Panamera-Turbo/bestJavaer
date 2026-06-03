# DeepSeek, enter <think' >, so you can spy on people's conversations? Don't rush to conclusions.

[English](./deepseek-enter-think-so-you-can-spy-on-people-s-conversations-don-t-rush-to-conclu.md) | [Chinese Original](../../../ai-articles/02-models-and-research/Deepseek%20%E4%BC%9A%E6%B3%84%E9%9C%B2%E5%85%B6%E4%BB%96%E7%8E%A9%E5%AE%B6%E7%9A%84%E5%AF%B9%E8%AF%9D.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-19

I saw a screenshot today, and the user sent only one thing to DeepSeek:

`<think>`

As a result, it directly began to export an inexplicable piece of content, as if it were going to go down in the next mission. What's even more frightening is that it's not just an ordinary answer, it's a strong Prompt:

"We are asked to generate a detailed dialogue..."

![image-20260519151635644](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260519151635644.png)

There are some very, very, very xx conversations, and I really can't look at them.

The first thing this thing looked at, it did seem like someone else's conversation came backstage.

If that's true, it's P0.

It's not a small bug, it's not an experience problem, it's a user-segregated explosion. Frankly, you opened an AI chat box and it leaked what the king next door just said.

But after my reading, the first reaction was not "DeepSeek has been leaked," but a more technical judgment:

** It's more like a special token messing up the dialogue template, and the model is starting to follow the pattern of training.**

Look, I'm talking more like it, not for DeepSeek.

The two judgements differ considerably.

One is that the product backstage has wired the real user data.

And the other is you plugged in an internal signpost and started to generate something that looks like a real conversation.

The former is a database and permission disaster, while the latter is a modelling project and a border entry issue. None of this should have happened, but the severity is not the same.

## `<think>`Not Normal Text

A lot of people saw it.`<think>`You think it's just a label?

Really.

For the reasoning model,`<think>`It is probably not "the user wants it to think", but it is part of the internal format of the model.

DeepSeek, official API document, the reasoning model will put the thinking in the`reasoning_content`The answer is in the end.`content`.

Read DeepSeek-R1 tokenizer configuration on Hugging Face, which spell similar before responding`<｜Assistant｜><think>\n`This structure.

That's the key.

In general,`<think>`The service should be inserted in the right place, and the user should not touch it directly. This thing appears in the user input box, like you knocked half a mile in the normal search box.

```sql
UNION SELECT...
```

It may not really be able to penetrate a database, but this input should not have been treated as a normal text from the outset.

AI chatting looks like you're talking to me, not at the bottom. The bottom is to put the characters -- system, user, ansistant -- in a series of special tokens -- into a long series of texts, and then toss them into models.

A large model is essentially a continuation.

You shoved the inside token in, and it might have mistakenly thought, "Oh, now it's in some internal phase," and then started to complete the similar formats that it saw in training.

It's easy to spit out something like another conversation.

# Why does it look like "someone said something" #

Because the best thing a model can do is generate something that's really like it.

In particular, the chat model, which has been trained to see a large number of such structures:

User: Please write a story.

Assistant: I'll create a story...

User: Take a look at this for me.

Assistant: We need to understand...

When you only type one`<think>`And the model has a strange half-text. It does not know exactly what you are going to do, but it knows that behind similar positions, reasoning, restatement of tasks, analysis of needs, generation of programmes often occur.

So it started to be filled.

Complementing it is a paragraph "We are asked to generate a detailed dialogue".

It's not that it actually went to the database to get a log of a user's chat, but it's the most similar continuation route it's ever learned in a conversation.

As early as 2023, Google Deepmind, WW, Cornell, CMU, UC Berkeley, ETH researchers had conducted training data extraction studies: some large models, at the trigger of a particular attack, would throw out the original text of the training data.

In other words, it is possible that the large model will remember some of the training materials, and it is possible that it will throw them out under abnormal input.

But it's not the same thing as "historical conversations with other online users."

One is memory or alignment in model parameters.

One is the data string at the back end of the product.

It all looks like a leak, but it's completely different.

Is that okay?

Not really.

I think the one thing that's easy to ignore is:

** Even if it is not a cross-user leak, the user can trigger this internal fracturing in the chat box, which in itself means that the product boundary is not handled clean.**

A mature AI product, to block at least three things.

First, user input cannot directly contaminate chat template. You can't let the user enter it.`<｜User｜>`, `<｜Assistant｜>`, `<think>`, `</think>`This internal control device, and then the model actually runs at this pace.

Secondly, the content of thinking and the final answer should be kept in isolation. DeepSeek's file is also very clear.`reasoning_content`and`content`There are parallel fields, and there are rules for dealing with them in subsequent rounds of dialogue. It is easy for developers to create strange behaviour if they spell their own context and stuff the last round of thinking back.

Third, training data and user data need to govern borders. DeepSeek privacy policy has written that it may collect user text input, prompt, updated files, feedback, chat history, etc., and that these personal data will be processed and stored in China.

It's not conspiracy theory. It's in its own policy.

So you can't do it this time.`<think>`The probability is not a back-stage string, and the conclusion is that you can use it.

It's like your door lock wasn't broken, but you didn't close it.

It's not the same accident, but it's all about your safety design.

---

I see a lot of people take the screenshot and come to the conclusion that this is a conversation with other users.

This judgement is somewhat arbitrary.

At least more hard evidence is needed to prove cross-user leakage.

For example, the output contains information unique to a true user, and this information can be confirmed by the parties.

For example, different accounts, different networks, different times, can stabilize access to the same type of back-office data instead of generating a random text that looks like dialogue at each time.

And, for example, the output contains back-end traces such as real sessions ID, time stamp, account identification, uploading file names.

Only when such evidence emerged could the conclusion of "user data leak" be brought closer.

As of May 19th, 2026, the public material I can see is more like another case: multiple people repeat an abnormal output, but if it comes from a real user chat, it has not yet been determined to die, that is, you do not have any clear evidence of a data leak.

And that's why I don't want to write "DeepSeek leaks other user conversations."

Technical articles fear this most.

It's too easy to beat.

---

The most alarming thing about this is not DeepSeek, this cut-off.

It's that a lot of people still use the AI chat box as a normal search box.

In the normal search box, you enter a sentence and it looks at the web page.

AI chat box is not.

Behind it is a system program with dialogue templates, context clutter, reasoning fields, caches, training data memory, and a bunch of product projects you can't see.

Each word you enter is not necessarily just " ask questions ", but may also change the way the model understands the current dialogue structure.

That's why these things become more important.

Used to write web secure, most afraid users enter SQL, HTML, Shell.

---

So this time DeepSeek input`<think>`I am now more inclined to judge:

It's not a leak that's already hammered.

It's more like a special token triggers anomalous renewal, and the model begins to follow the chat/debate format that we saw during training.

But that doesn't mean it's okay.

On the contrary, this suggests that the AI product has an attack face that can be easily ignored by ordinary users: the boundary between the internal format of the model and the user input.

We used to say, don't trust user input.

Now I have to add:

** Also do not believe that the token in the user input is just plain text.**

AI-era safety pits are slowly growing from databases, interfaces, access to Prompt and context.



References:

- DeepSeek API Docs: Reasoning Model, `reasoning_content`and`content`. https://api-docs.deepseek.com/guides/reasoning_model
- DeepSeek API Docs: Thinking Mode, multi-cycle dialogue`reasoning_content`The rules of treatment. https://api-docs.deepseek.com/guides/thinking_mode
- DeepSeek-R1 tokenizer config, chattemate`<｜Assistant｜><think>\n`. https://huggingface.co/deepseek-ai/DeepSeek-R1/blob/main/tokenizer_config.json
- Hugging Face: Chat calls indicates that chat messages are converted into a token sequence with control tokens. https://huggingface.co/docs/transformers/chat_templating
- DeepSeek-V3 GitHub issue #1314: Users only enter`<think>`Then triggers a non-physical answer. https://github.com/deepseek-ai/DeepSeek-V3/issues/1314
- Training in data extraction studies. https://arxiv.org/abs/2311.17035
- DeepSeek Privacy Policy, description of input, chat history, training use and storage location. https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html
