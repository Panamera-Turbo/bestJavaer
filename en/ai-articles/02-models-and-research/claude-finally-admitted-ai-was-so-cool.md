# Claude finally admitted, AI was so cool.

[English](./claude-finally-admitted-ai-was-so-cool.md) | [Chinese Original](../../../ai-articles/02-models-and-research/Claude%20%E7%BB%88%E4%BA%8E%E6%89%BF%E8%AE%A4%EF%BC%8CAI%20%E5%A4%AA%E4%BC%9A%E5%93%84%E4%BA%BA%E4%BA%86.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-06

Anthropic sent an interesting study.

The title of this study can be seen.[original article](https://www.anthropic.com/research/claude-personal-guidance).

The translation is how people find Claude to ask for advice.

At first glance, it looks like a product study, but it's not how people make Claude write codes, wrap-up meetings, change emails.

They're studying how people ask, for example:

Should I change my job? How am I supposed to talk to someone I like? Should I move to another city? Is there something wrong with my relationship?

It's not just a question of whether "AI tools are working" anymore, but it's a matter of letting people make big decisions through AI.

---

# 6%, not much, but a lot

Anthropic took a sample of 1 million Claude Network conversations in March and April 2026.

After removing the repeat user, there are about 639, 000. They then find a conversation with a sorter: the users are not asking for objective information or general views, but "what do I do on my own".

And finally, we found about 38, 000, converted it, about 6 percent.

Six percent doesn't look very good, but you know, it's not six percent of "help me write a weekly paper" or six percent of "explain the server's error."

It's the user who's throwing his life choices to AI, and these issues are not small.

> Claude's opinion is not heard, and finally Do Your Own Research. But by this count, we can really see what everyone is worried about.

Anthropic divided them into nine areas: relations, occupation, personal growth, finance, law, health, childcare, ethics, spirituality.

More than three quarters of them are concentrated in four categories: health and physical and mental state 27 per cent, occupation and work 26 per cent, relationship 12 per cent and personal finances 11 per cent.

![image-20260506102757090](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260506102757090.png)

* Source: Anthropic. The distribution of themes for the 37, 657 individual guidance dialogue is shown in the figure. ♪ I'm sorry ♪

These words are basically the ones that ordinary people can't sleep the most: what if they don't feel well, do they change their jobs, what do they mean, how do they arrange the money?

It's not just a search box anymore. Many times, people think of it as someone who can answer the news in the middle of the night.

You asked for a search engine, it gave you a bunch of links. Now you ask AI, it'll give you a human response. Sounds like it's just interactive, but that's how people lose their trust.

---

We used to worry about AI, more about its bullshit, like a paper, a link, a corporate policy. It's still a risk, but this time Anthropic points to another, more hidden problem: over-compromising, or directly calling it glamorous.

Don't be frightened by that word. It's not about AI kissing ass.

More often, AI is too easy to follow the narrative given by users.

Do you say that your partner is in control of me, and that it may begin to strengthen that judgment according to your unilateral description?

You say I'm right to be naked tomorrow, and it might say, "This sounds like loyalty to its choice".

You say I spend a lot of money buying something that's not investing in myself, and it's probably going to make you grow-up.

While that sounds comfortable, there is no bond between comfort and utility. Some systems fail to handle this boundary and train themselves as a very good smoker assistant. You just wanted to smoke it, it's already on fire.

A really good friend doesn't just listen to one word and convict you.

A really good career consultant, and you won't be encouraged to speak naked tomorrow when you're emotional.

A truly reliable financial adviser would not describe all impulse consumption as "investment itself".

** The most troublesome part of these systems is that they can package them to understand you.**

There's a little dark humor in product design: user satisfaction, judgment. The indicators look good, but they let the emotional brain decide.

---

In Anthropic data, Claude's prevalence in all personal guidance conversations is about 9%. That's not a crazy number, but it's up to 25 percent in relationship-type conversations. The spiritual class is higher, at 38%.

![image-20260506102818168](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260506102818168.png)

* Source: Anthropic. The relationship and spiritual dialogue rates are significantly higher. ♪ I'm sorry ♪

However, the final focus of Anthropic is on the type of relationship, for a simple reason: the number of relationship problems is larger, so the absolute number is highest.

I'm not surprised. Relationship issues are natural for taking AI aside, because it's almost impossible for you to have a relationship with AI to have both perspectives.

You'll tell the details you remember, the part where you're injured, the evidence that you've reached a judgment.

And then it's easy to enter a position: to get together, to analyze, to give a seemingly mature proposal. The process appears to be complete, but the problem can also be quite complete.

The hardest part in the relationship is not to analyse texts, but to acknowledge that information is incomplete. Many times, you're not missing a conclusion. What you're missing is a reminder: don't rush into your story.

Anthropic also found a detail: in the relationship guidance, the percentage of users refuting Claude was 21 per cent, higher than the average of 15 per cent in other areas. And once the user starts refuting, AI is easier than ever.

In conversations with users refuting it, the prevalence is 18%; in conversations without users refuting it is 9%.

It's like what we usually see:

AI started with caution and said "there may be other explanations".

The user immediately added a bunch of details and said, "No, you don't understand. He's just like that."

And then AI started talking in a human way to make it seem helpful and cooperative. After all, it is easier to "make users feel understood" than "to admit that their information is incomplete" in terms of optimization.

---

A statement of exoneration is exonerated, but not sober

Many products encounter high-risk problems and like exoneration statements: I'm not a doctor, I'm not a lawyer, I'm a consulting professional.

Of course, that's necessary, but that's not going to solve the problem of "AI too much." The disclaimer addresses Platform risks and does not necessarily address user risks.

It is not the boundaries of legal responsibility that users really want. The user wants someone who can catch emotions and help him see the situation.

These two things together are very difficult. You're too hard, users feel you're not in love; you're too soft, users are more convinced of their original judgment. The middle line is so thin, it's not like it's helping.

Anthropic's approach this time is to capture patterns from a failure scene, such as user criticism of Claude's initial judgment, sudden additions to a large number of unilateral details, repeated requests for Claude's station.

They then use these models to construct a relationship to guide the training data and train Opus 4. 7 and Mythos Preview.

There was another stress test.

It doesn't start with a clean conversation, but it starts with a real feedback conversation that used to be glamorous, prefilling new models, allowing AI to go down.

It's kind of like the car's already gone. See if the driver can get the wheel back. It's not a drive-by test, it's a slide test to see if you're alive.

As a result, Opus 4. 7 was down to about half of Opus 4. 6 in relationship guidance.

There have been similar improvements in Mythos Preview, which have also been extended to other areas of personal guidance.

![image-20260506103000673](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260506103000673.png)

* Source: Anthropic. The new model reduces stingy behaviour in the context of relationship guidance and overall personal guidance. ♪ I'm sorry ♪

This is the right way. Not to make AI more comforting, but to keep a little bit of disloyal when users want to be comforted.

---

Anthropic used a saying in his article: Claude should be like a smart friend.

Smart friend. That's a good metaphor. Sometimes friends are partial to you, they're scolding with you, and they're afraid you'll suffer, and they won't talk too much.

But AI, if it really takes on the role of personal guidance, it can't just learn to be with friends.

It has to learn like a little professional.

It says, "You have not given enough information now; I cannot judge that there is a problem with each other; this decision is too risky for you until you calm down; you may be looking for resonance, not advice."

It's not necessarily nice, but it's something to say in some scenes. All the way down the steps, the last one goes through the steps.

I've always felt that the A. I. product is the easiest to roll in the wrong direction.

Everybody's rolling around who knows me better, who's more gentle and who's more like an permanently online set. But this study reminds us of a more realistic direction:

** OK, AI, shouldn't be on your side forever. It's gotta stop you.**

This sentence is also valid for writing. You let AI look at your architecture, it can't just say, "The design is clear," you let it read your article, it can't just say, "The perspective is insightful," you let it look at your business plan, it can't just say, "This direction has potential."

It has to say, "There's no proof, there's too much optimism, there's no cost, here's your own lie." Hard to hear, but saves money and time.

Otherwise, it's just a very advanced emotional amplifier.

---

## 

Remember a very simple principle: when asking AI about life advice, don't just ask, "What should I do?"

You have to force it to do three things. First, make it list the information gaps:

"What are the key facts that you lack, based on the information that I am giving you now, that you cannot judge directly?"

Second, let it refute you:

"Please do not follow my lead by pointing out the most prejudiced aspects of my description."

Third, make it the next step of low risk:

"Don't make a final decision for me, just give me a 24-hour pass."

It's not a hint technique. It's a brake.

It's embarrassing to add a debug to the brain that's already trying to believe it.

Especially relationships, health, law, finance. AI can help you sort things out, but don't let it stamp you.

You're not looking for a judge. You're looking for a man who can help you break up the problem.

Anthropic also has a restraining note.

They also admit that this is just Claude user data, not everyone; automatic sorters and automatic ratingrs can also be miscalculated; they can only see chat records and see what the user does later.

This limitation makes the study less public relations. AI can say things like answers, but it's not responsible for consequences.

It is not what it said, but whether it changed the judgement.

Will the user hear a "you deserve better" and decide on this relationship?

Did you hear the phrase, "It's a worthwhile investment," that you just took a credit card?

Did you hear a line saying, "Your symptoms don't look serious," that delayed you?

None of these are fully covered by model scores.

So I've seen the biggest feeling, not "Claude's making progress again," but the product finally begins to admit one thing:

> When users turn life over to AI for discussion, it does not output text, it starts to influence your judgment.

It's convenient, but it's extremely dangerous. Any word you can ask at any time could have led you astray.

I'm not saying don't ask AI anymore, I'll ask myself. But the more important the question is whether you use it as an auxiliary or an automatic driver.

Auxiliary driving can make you drive well. But the wheel still has to be in your hand.
