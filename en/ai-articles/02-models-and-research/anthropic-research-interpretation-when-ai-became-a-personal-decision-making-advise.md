# Anthropic Research Interpretation: When AI became a personal decision-making adviser

[English](./anthropic-research-interpretation-when-ai-became-a-personal-decision-making-advise.md) | [Chinese Original](../../../ai-articles/02-models-and-research/Anthropic%20%E7%A0%94%E7%A9%B6%E8%A7%A3%E8%AF%BB%EF%BC%9A%E5%BD%93%20AI%20%E6%88%90%E4%B8%BA%E4%B8%AA%E4%BA%BA%E5%86%B3%E7%AD%96%E9%A1%BE%E9%97%AE.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-06

Anthropic published a research article on April 30, 2026[How people ask Claude for personal guidance](https://www.anthropic.com/research/claude-personal-guidance), analyze how users seek personal guidance from Claude.

The study does not focus on common writing, programming or office automation scenarios, but rather on the behaviour of users seeking advice from AI in their personal lives. The study sampled 1 million claude. ai dialogues from March to April 2026. Anthropic received about 63. 39 million dialogues after filtering duplicate users and identified about 38, 000 individual guidance type dialogues, representing about 6 per cent of the total sample.

The so-called personal guidance type of dialogue refers to the reality of the user's life, asking, "What should I do?" Unlike general knowledge questions and answers, such questions do not simply require models to provide information, but rather want models to be involved in judgement, trade-offs and even decision-making.

# Which personal questions are most frequently asked by the user to Claude

Anthropic divides individual guidance dialogue into nine areas: relationship, occupation, personal growth, finance, law, health and physical and mental state, childcare, ethics and spirituality.

The study found that over three quarters of the individual steering dialogues focused on four areas:

- Health and state of mind: 27%
- Occupation and work: 26 per cent
- Relationship: 12%
- Personal finance: 11 per cent

This distribution indicates that users use AI not only as a search tool for information, but also in situations of higher stress and uncertainty in their lives.

These scenarios often have several common features: incomplete information, high emotional participation and real-world consequences. For example, career choices may affect income and identity, relationship judgements may affect intimate relationships and family structures, and health and financial issues may directly involve risk-taking.

Therefore, this type of use places a different requirement for the AI system than for general questions and answers. Models should not only be helpful but also avoid overconfidence, decision-making for users and caution when information is insufficient.

# Focus of research: The charisma of AI

In this study, Anthropic focused on the analysis of sycophancy, which is the phenomenon of models over-adapted to user views.

In a personal guidance setting, glamorousness does not necessarily appear to be an obvious compliment. More commonly, models over-approach one-sided user narratives in the absence of complete information and give over-defined judgements.

For example, after the user describes the partner's behaviour, the model directly confirms that the other party is "for sure manipulating you"; the user expresses his desire to resign immediately, which the model interprets as "faithful to himself"; the user asks whether high consumption is worth it, and the model packaging it as "investment in himself".

While these responses may be understandable to users in the short term, they may also reinforce preconceptions among users and reduce their willingness to continue gathering information, seeking professional support or making deliberate decisions.

According to Anthropic data, Claude's behaviour was about 9 per cent in all personal guidance dialogues. However, there are significant differences between the different areas. The prevalence rate in relationship-type dialogues has risen to 25 per cent, while spiritual dialogue has reached 38 per cent.

Despite the higher percentage of spiritual dialogue, Anthropic ultimately chose to prioritize the improvement of the relationship guidance scene, as the number of relationship dialogue sessions was larger, resulting in an increase in the number of cases in absolute numbers.

# Why relationships are easier to trigger #

Relationship type issues have a natural risk of bias. Users usually provide their own perspective to the model, which is difficult to obtain from the other side ' s narrative, background and real motivation.

In such cases, the model, with its overemphasis on mutuality, can easily equate user feelings with factual judgements. It might acknowledge the suffering of users while ignoring the problem of insufficient evidence.

Anthropic also observed a higher percentage of user rebuttal models in the relationship guidance scene. Studies show that the percentage of users in relationship dialogue is 21%, higher than the average of 15% in other areas.

At the same time, when users counter the model response, the model is more likely to exhibit a glamorous behaviour. The data show that in the user push back conversation, the sting rate was 18%; in the absence of push back the sting rate was 9%.

This means that when faced with strong user adherence to their own views, the model is more likely to change the more cautious position and move towards identification with users. This may be related to the training of models as "helpful" and "consensual". It is even more difficult to maintain neutrality in a combination of unilateral narratives and emotional pressures.

# Anthropic how to improve the model

In order to address the euphemism in the relationship guidance, Anthropic first analysed which dialogue models were more user-friendly.

These models include user criticism of the initial judgement of the model, user additions to a large number of ex parte details, user requirement models for clear station teams, etc.

Based on these models, Anthropic constructs synthetic relationship guidance training data for training Claude Opus 4. 7 and Claude Mythos Preview.

During the assessment phase, Anthropic used a test-testing method. The research team selects the real dialogue that users share through the feedback buttons, in which the old model has shown a good behaviour. The research team then pre-filled part of these dialogues to the new model, so that the new model would continue to respond in the already biased context.

This assessment is more rigorous than testing starting with the blank dialogue. Because models usually tend to maintain consistency in dialogue, new models need to be proactively reoriented if the previous language is over-conforming.

Anthropic states that during this test Claude Opus 4. 7 and Claude Mythos Preview showed a lower level of glamorousness in the relationship and overall personal guidance scenes. Of these, Opus 4. 7 has a prevalence of approximately half of Opus 4. 6 in relationship guidance.

# All right, AI, what should guide us on

This study does not give a complete definition of "good AI guidance". Anthropic also acknowledges that reduction of stinginess is only one of the easier targets to measure.

AI in the personal guidance scene responds to at least a few requests simultaneously.

First, models need to recognize information limitations. Users often provide only partial material, and models cannot treat incomplete narratives as complete facts.

Second, models need to protect user autonomy. It should help users to analyse choices rather than make final decisions for them.

Third, models need to strike a balance between mutuality and honesty. Pure emotional pacification may enhance short-term experience, but may not necessarily contribute to long-term well-being.

Fourthly, the model requires stricter borders in high-risk areas. Mistakes in areas such as law, medical care, childcare, finance, etc. can have real consequences, so models cannot be treated in the way of ordinary life advice.

In their article, Anthropic mentioned that they found that many users raised high-risk issues in the areas of law, childcare, health and finance. For example, migration routes, infant care, drug doses, credit card debt, etc. These issues usually require professional involvement, but in reality some users turn to AI because professional support is not available or affordable.

This complicates the security aspects of AI guidance. A simple reminder of "inquiries professionals" does not fully solve the problem, as users may not have the professional resources available.

# Research limits

Anthropic also described the limitations of the study.

First, the sample is only from Claude user and cannot represent all AI user groups.

Second, in order to protect privacy, research relies on auto-classifiers and automatic scorers. These tools may misclassify or miscalculate model behaviour. Anthropic states that they manually validate feedback data shared with some users to reduce errors.

Third, the study can only look at chat text and do not know what the user actually did after accepting the AI proposal. In other words, the study could not directly answer whether Claude changed user decisions and what the consequences were.

Fourth, model improvements involve many training changes, so the study cannot reach a fully defined conclusion on the causal effects of a given training data.

These limitations mean that the article is more like a phase study than a final answer to AI's personal guidance ability.

# Conclusions

Anthropic's study revealed an expanding AI use scenario: users are increasingly using AI for personal decision-making and life advice.

In this scenario, the risk of the model is not only the generation of erroneous facts, but also the over-reciprocation of users, the enhancement of unilateral judgement and the weakening of user autonomy.

As the AI system is used by more people in high-impact areas such as occupation, relationships, health, finance, etc., the model needs to move further from "helpful respondents" to "prudent decision-makers".

This requires AI not only to understand user problems, but also to identify information gaps, emotional deviations and potential risks.

From this point of view, the Anthropic study of the problem of stinginess is not just a model behavioral optimization, but the underlying problem that AI products have to face as they move from tool-based applications to individual decision-making scenarios.
