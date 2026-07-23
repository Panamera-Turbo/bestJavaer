# Kimi K3 Stole the Show

[English](./kimi-k3-stole-the-show.md) | [Chinese Original](../../../ai-articles/02-models-and-research/%E5%91%A8%E4%B8%89%E8%B7%9F%E5%A4%A7%E5%AE%B6%E8%AF%B4%E7%9A%84%E4%B8%80%E4%BA%9B%E6%A8%A1%E5%9E%8B%E5%8F%AF%E8%83%BD%E8%A6%81%E5%8F%91%E5%B8%83%EF%BC%8C%E7%BB%93%E6%9E%9C%E4%BB%8A%E5%A4%A9%20Kimi%20%E5%B0%B1%E7%82%B8%E5%9C%BA%E4%BA%86%E3%80%82.md)

> Date: 2026-07-18

Some of the models I told you on Wednesday might be released, but yesterday Kimi exploded.

Today, Kimi officially launched its strongest model, Kimi K3, with 2.8 trillion parameters, the world's first open source 3 trillion-level model, 1 million token context windows, and native support for visual understanding.

Today, the Internet is full of enthusiasm for Kimi K3. It seems that everyone does not think that there is a gap between Kimi K3 and Fable 5 and GPT-5.6-Sol, which is officially recognized by itself.

In the subconscious mind of the public, it seems that if the K3 front end takes first place, it has defeated everything else.

I don’t know if this is the power of money.

However, through Kimi K3’s official blog, you can see two details.

K3 is extremely sensitive to thinking about history.

Unlike Claude and OpenAI, which treat thinking as a disposable scratch paper, the training assumption of K3 is that each round can see the complete thinking of all previous rounds.

This leads to two unconventional constraints:

It is almost impossible to cut the thinking content. Most models will only be slower if they cut thinking. But after K3 cuts it, what is lost is the chain of exploration, elimination, and error correction in the reasoning process.

In the next round of the model, you will not be able to get what you have thought about and excluded before, and the quality will be very unstable.

And it cannot be cut from other models. Even if the original thinking text is passed over, K3 cannot connect it, because the historical thinking seen during training is all in a self-generated style. If it is replaced with the reasoning mode of other models, there will be a serious disconnect when continuing to write.

These two conditions directly lock the context compression and model routing of many Agents (for simple tasks, switch to cheaper models, and for complex tasks, switch to stronger models).

The official attitude is also very clear: if the harness does not completely return the historical thinking, or is cut from other models midway, the generation quality is not guaranteed.

Therefore, the official Harness binding model may become a trend in the future.

This is also why cc does a good job of integrating Harness directly into the model.

Although K3 has open sourced the weights, if they want to make good use of them, third-party Harness has either made major changes or given up.

Harness has the potential to become an ecological moat.

Another very real problem is that K3’s 1M context does not benefit all users.

In the Kimi website and App, the full 1M is currently placed in the Allegro file for 699 yuan per month. Kimi Code is slightly more relaxed: the 99 Yuan range can use K3, but only 256K; the 199 Yuan range only starts to open 1M.

Kimi’s biggest problem is that it’s too expensive.

As for the power of money, that's another topic.
