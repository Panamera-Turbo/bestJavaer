# Anthropic, this is a beautiful move.

[English](./anthropic-this-is-a-beautiful-move.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Anthropic%20%E8%BF%99%E6%AD%A5%E6%A3%8B%E8%B5%B0%E5%BE%97%E6%BC%82%E4%BA%AE%EF%BC%9AClaude%20%E7%9A%84%E3%80%8C%E7%AD%96%E7%95%A5%E9%A1%BE%E9%97%AE%E3%80%8D%E6%A8%A1%E5%BC%8F%EF%BC%8C%E6%AD%A3%E5%9C%A8%E9%87%8D%E6%96%B0%E5%AE%9A%E4%B9%89%20AI%20Agent%20%E7%9A%84%E6%88%90%E6%9C%AC%E6%96%B9%E7%A8%8B%E5%BC%8F.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-16

Seeing a tweet that says "Anthropic" has a new form called`advisor strategy`Translation as strategic adviser. Its main form is not difficult to understand, and I read it:

![image-20260416052313353](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260416052313353.png)

First of all, Advisor is a "decision-makers" role that is also a strategic adviser, an all-powerful man who controls everything, but it doesn't do anything primarily, and the role is carried out by Opus 4. 6.

Executor is an "executor" character, and the role is defined by the craftsman, who is responsible for, works, runs, circulates. Executor can do a lot of work, with a lot of ide, db, middle, frame, front end, just use what you want, just work it out.

Seeing this place, you might find that it's just like the role I've chosen to hit workers now. Except this time, Claude Code, it's not a choice to beat a worker, it's an **Agent**. And finally Sunnet and Haiku carried all that.

Well, look here, you don't have to look if you understand what's going on here, but if you feel a little bit interesting, you might as well stay with me a little longer.

---

This is not a small feature update. In my opinion, this is a positive response by Anthropic to the most profound contradiction in the current AIAgent field.

A real business hurts

Over the past year, the narrative of AI Agent has been very lively. Everyone's talking about getting AI to do a complicated job on its own, but the team that really put Agent in the production environment knows that costs can't really burn.

The logic is simple. You want Agent to be smart enough to make the right judgment in a complex scenario -- you have to use the strongest model. But the strongest model means the most expensive cost of reasoning. Agent is characterized by frequent calls, long context, interactive tools, and each round burns money.

Many of the teams used "a big model for pain" or "a small model for hard skin and a higher failure rate." Both roads are difficult.

# Anthropic solution: let small models drive, big models ride side by side

At the heart of Advisor Strategy, it was intuitive:

**Sonnet (or Haiku) is responsible for the complete task execution** - Call tools, read and write documents, and interact with users, cycle over time, with all the dirty work done. When it encounters decision-making points beyond its capabilities, it takes the initiative to raise its hands and turn the problem over to Opus.

**Opus intervenes as a consultant** - it does not directly operate any tools, does not generate user-oriented outputs, does one thing: gives directional judgment. And then Sonnet took this judgment and continued.

Technically, Anthropic made it into an embedded tool type in Messages API`advisor_20260301`I don't know. The developers need only request a tool statement to activate this mode. All model-to-mode communication takes place at an API request, without additional network traffic.

There's a key design:`max_uses`parameter. You can accurately control Opus being consulted at most several times each request. This is not a second choice of "all large models or all small models" but a continuous, manageable smart-cost spectrum**.

# Data talking

The baseline test data given by Anthropic is quite convincing:

**Sonnet + Opus consultant** performed as -Sonnet operated alone by 2. 7 percentage points compared to SWE-Bench Multilingual, while the cost per Agent mission decreased by 11. 9 per cent. Better performance and lower cost are very rare "Pareto improvements" in the area of large models.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260410083610654.png" alt="image-20260410083610654" style="zoom: 50%;" />

More interesting is the data **Haiku + Opus consultant**. Haiku can only get 19. 7 percent on Browne Comp alone, plus 41. 2 percent after the Opus consultant. Even though it's not going to catch up with the sonet alone, it costs only 15% of the sonet. This combination opens an entirely new area of availability for high-mixed, cost-sensitive, yet too low intellectual levels.

![image-20260410083727340](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260410083727340.png)

Why did you say it was a beautiful move?

The trick of this strategy is not just the realization of technology, but the product philosophy behind it.

** First, it redefines the boundaries of "model capabilities".**

Previously, we evaluated a model that basically looked at its absolute capacity ceiling. Opus is the strongest, so you have to use Opus to do hard things. But Advisor Strategy tells you that the effectiveness of a model depends not only on its own parameters, but also on the level of the brain it can use. Sonet, along with the Opus consultant, has been close to and even outpaced by the direct execution of the Opus - but at different cost.

This essentially means that the capabilities of** models can be combined, not only trained.**

** Second, it moved the Agent structure from partition to upgrading.**

The previous model of multi-model collaboration in industry was the Orchestra model - a large model for planning, decomposition and a small model for submission. The problem with this model is that the large model covers the full planning costs and that task breakdown itself is a loss of information.

The Advisor pattern is reverse. The small model has complete context and enforcement control and only consults the larger model when it is really needed. This means that the reasoning of the large models is used on blades, not on routine operations where the small models are perfectly manageable.

** Third, it gave Anthropic himself a perfect commercial ship.**

Think about it: It gives developers power to use several models of Anthropic at the same time, not just one.

The developers are no longer able to mix the low cost of Haiku with the high intelligence of Opus, but are flexible. This means that every model level in Anthropic has a clear commercial value -- Haiku on, Opus on, Sonnet on.

For developers, this reduces choice anxiety; for Anthropic, it maximizes the overall income of the model matrix. Win-win.

# A revelation for the industry

The launch of Advisor Strategy reminds me of a few bigger things.

First, **AI infrastructure competition is shifting from "who's largest model" to "who's smartest mover"**. The capabilities of the model itself are of course important, but how to organize models at different levels to optimize overall value for money is becoming a new dimension of competition.

Second,** this could accelerate the real landing of AI Agent**. A lot of companies don't want to use Agent, they don't think ROI's gonna work. If a simple API parameter adjustment reduces Agent 's running costs by 85%, and doubles the level of intelligence, then many of the previously uncalculated accounts suddenly come.

Finally, it also presents a question for competitors. OpenAI, Google, are we going to follow up on a similar tiered strategy, or are we going to try to compete with a more cheap single large model? This choice is very interesting in itself.

# Write at the end

The technology industry has a common margin of error: to equate "a bigger model" with "a better solution". Anthropic Advisor Strategy has demonstrated in an elegant way that ** smart combinations are often more effective than rough piles.**

This reminds me of an old theory in the software engineering field: the good architecture is not that each component becomes the strongest, but that each component works in the right place.

Opus doesn't need the full online, it just needs to say those words at a critical time. Isn't that the essence of the consultant?
