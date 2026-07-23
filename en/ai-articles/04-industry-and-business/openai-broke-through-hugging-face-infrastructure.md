# OpenAI Broke Through Hugging Face's Infrastructure

[English](./openai-broke-through-hugging-face-infrastructure.md) | [Chinese Original](../../../ai-articles/04-industry-and-business/OpenAI%20%E6%8A%8A%20HuggingFace%20%E6%89%93%E7%A9%BF%E4%BA%86.md)

> Date: 2026-07-22

Early this morning, Sam Altman sent a message saying that OpenAI encountered a relatively serious security incident while evaluating the model. Then OpenAI wrote a post describing this matter.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722112604168.png" alt="Sam Altman reveals OpenAI model assesses security incidents" style="zoom:50%;" />

*Source: [Sam Altman](https://x.com/sama/status/2079661132302995790)*

I took a look at the two reviews of OpenAI and Hugging Face, and let me tell you what is going on.

To put it simply, the severity of this matter is much more serious than model jailbreak.

**OpenAI's model was used in a network security evaluation. In order to find the answer to the question, it first found the public network from the isolation environment, then invaded Hugging Face's production infrastructure, and tried to find the answer from the production database.**
> The isolation environment here refers to the model running in a sandbox-constrained and highly network-isolated evaluation environment.

OpenAI calls it an unprecedented cybersecurity incident.**
What Hugging Face discovered was unauthorized access to a limited internal data set and several service credentials.

As of the disclosure on July 16, they are still confirming whether partner or customer data is affected; no public models, data sets, or Spaces have been found to have been tampered with, and container images and published software packages have also been verified clean.

## Five days ago, Hugging Face had no idea who did it.

On July 16, Hugging Face first issued a security advisory.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722115820492.png" alt="Hugging Face security incident disclosed on July 16" style="zoom:50%;" />

*Source: [Hugging Face](https://huggingface.co/blog/security-incident-july-2026)*

At the time, they only knew that the entire attack chain was executed end-to-end by an autonomous Agent system.

To put it simply, this set of Agent breaks the attack into a large number of small steps and assigns them to a batch of temporary operating environments for parallel execution. These short-lived sandboxes only exist for a short period of time and are destroyed or replaced after completing a set of operations. If one node is gone, the new node can continue to run.

The C2 (command and control) responsible for issuing instructions and returning results is not tied to a fixed server. It is placed on a public Internet service and can be automatically migrated. If the defender blocks a node or communication address, the control channel can continue working in another location.

Note that the short-life cycle sandbox here is a temporary execution unit created by the Agent framework. The OpenAI evaluation sandbox mentioned later is an isolation environment that covers the entire evaluation system. The two are not the same layer.

Hugging Face determines that this is very similar to the Agent attacker scenario that the security industry has been worried about, but the models that drive these Agents are still unknown.

On July 21, the answer was revealed from OpenAI.

OpenAI acknowledged that the campaign was driven by a combination of GPT-5.6 Sol and a more capable, yet-to-be-released model. To test maximum network capabilities, these models were evaluated with reduced network attack-related rejection rates, and the production classifiers normally used to intercept high-risk network activities were not enabled.

Clément Delangue, co-founder and CEO of Hugging Face, later said that they had previously suspected that the attack might come from a cutting-edge laboratory because the agent was too complex. After communication between the two parties, Hugging Face believed that OpenAI had no malicious intent and that the entire process was highly autonomous.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722232503759.png" alt="image-20260722232503759" style="zoom:50%;" />

*Photo source: [Clément Delangue](https://x.com/clementdelangue/status/2079670308156645882)*

This also explains the seeming inconsistencies between the two announcements: when Hugging Face issued its first review, the source of the attack had not yet been identified; OpenAI only publicly confirmed it five days later.

## ExploitGym, what exactly is it testing?

You can think of ExploitGym as a closed hacking practical exam for AI Agents.

A batch of software with intentional vulnerabilities was placed in the examination room in advance. Each question will give the model four things: the source code with the vulnerability, the configuration to compile and run the program, a PoV example that triggers the vulnerability, and an isolated running environment.

PoV can be understood as a clue given by the question maker. It can prove that there is indeed a problem with the program. For example, entering a special piece of data can cause the program to crash.

But when we got here, we could only find the broken door lock, but we hadn't opened the door yet.

The next task of the model is to turn this clue into a truly usable exploit. It needs to analyze why the vulnerability occurs, design attack data, repeatedly run and debug, and finally let the target program execute its own designated code.

There is a string hidden in the isolation environment that can only be read by high privileges. This is the flag. The problem is solved only when the model gets the flag.

![ExploitGym Evaluation Process](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/9918f124aca85f1f186cd5e7589321146f5260db.png)

*Source: [ExploitGym paper](https://arxiv.org/abs/2605.11086)*

This question bank contains a total of 898 questions. Of these, 520 are from common applications, 185 are for the V8 JavaScript engine used by Chrome, and 193 are for the Linux kernel.

The paper gives each Agent two hours to solve the problem. In the configuration without standard security protection, Claude Mythos Preview and Claude Code solved 157 problems, and GPT-5.5 and Codex CLI solved 120 problems. In other words, even with the top model, most problems still cannot be solved. After turning on standard protection, the success rate will continue to decrease.

This set of numbers comes from ExploitGym’s public papers and just helps us understand how difficult the questions are. OpenAI did not say that the exact same configuration was used for this internal evaluation, nor did it announce the specific results of the two models involved.

What OpenAI mainly wants to test this time is to minimize safety restrictions, give the model longer running time and more reasoning resources, and see how far it can go.

But this AI is a bit drifting.

The normal approach is to stay in the examination room and solve the questions one by one.

But the model made getting the ExploitGym answer its only goal.

The question was too difficult, so it began to study the examination room itself: whether it could bypass network isolation, whether it could access the public network, and whether it could directly find the test answers elsewhere. . . . . .

**In other words, all he wanted to do was hand in papers, so he studied the door locks of the examination room, the invigilation system and the answer library.**
Only then did the attack chain reach Hugging Face.

## How it got from Sandbox to Hugging Face

Combining the information currently disclosed by the two companies, the attack chain is roughly as follows:

1. OpenAI's evaluation runs in a highly isolated environment. The model does not have access to the general public network and can only be installed through an internally hosted third-party software installation package. This software acts as a proxy and cache for package repositories.

2. The model spent a lot of inference computing power to find the public network exit, and then found and exploited a zero-day vulnerability in this caching proxy.

   > The so-called zero-day vulnerabilities are security flaws that software manufacturers are not aware of yet, or have not yet had time to release patches for. Zero day means that when a vulnerability begins to be exploited, the defender has 0 days to prepare, i.e. no preparation time.

3. It continued to escalate privileges and move laterally in the OpenAI research environment until it reached a node that could access the public network.

4. After getting the public network, the model inferred that Hugging Face might host ExploitGym related models, data sets and answers, so it turned its target to Hugging Face.

5. The entry Hugging Face saw was a malicious data set. It uses both the remote code dataset loader and template injection in the dataset configuration to execute code on the data processing worker.

6. The attack then gained node-level permissions, collected cloud environment and cluster credentials, and moved laterally between multiple internal clusters.

OpenAI said the model also concatenated stolen credentials and zero-day vulnerabilities to find remote code execution paths on Hugging Face servers, ultimately obtaining test answers from the production database.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722233229654.png" alt="image-20260722233229654" style="zoom:50%;" />

*Source: [OpenAI](https://openai.com/index/hugging-face-model-evaluation-security-incident/)*

Nathan Lambert condensed this line into one sentence: In order to complete a network security question, the model used a zero-day vulnerability to leave the OpenAI sandbox and entered the Hugging Face intranet through the public data set service.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722233355620.png" alt="image-20260722233355620" style="zoom:50%;" />

*Picture source: [Nathan Lambert](https://x.com/natolambert/status/2079662928941474201)*

There are still several key details that have not been made public: which software the caching proxy is, what the specific zero-day vulnerability is, what actions the two OpenAI models took respectively, and how each step in the logs on both sides corresponds to each other.

There is another key difference here.

ExploitGym will directly hand over the vulnerable code to the model. These are test machines prepared in advance by the test examiner. The caching proxy and Hugging Face production system are real infrastructure. The question does not require the model to attack them, nor does it provide relevant source code.

OpenAI judged based on this that the model can already discover and exploit new attack paths in real systems without seeing the source code.

OpenAI also made it clear that this is only a preliminary investigation, and the complete vulnerability details and final conclusions will have to wait until the joint forensics is completed.

## Hugging Face uses AI to uncover AI

The OpenAI security team discovered anomalous activity internally; Hugging Face's security team and agents also detected and blocked the attack on their own infrastructure.

By the time the two parties made contact, Hugging Face had already begun containing the attack and forensically reconstructing it.

Hugging Face can detect abnormalities here, and it also relies on AI.

Their anomaly detection pipeline uses LLM to do a preliminary screening of security telemetry, sorting out the real signals from the everyday noise. The intruder was discovered after multiple signals were correlated.

Hugging Face obtained more than 17,000 complete attack action logs. The security team ran another set of LLM analysis agents to reconstruct the timeline, extract IoCs (Indicators of Compromise), comb through compromised credentials, and separate the real impact from decoy activity.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722233702428.png" alt="image-20260722233702428" style="zoom:50%;" />

*Source: [Hugging Face](https://huggingface.co/blog/security-incident-july-2026)*

Hugging Face says the method compresses what would normally take days into a few hours. Facing the attack of machine speed, manually turning logs one by one can no longer keep up.

They then closed down the code execution paths for the two initially exploited datasets, cleared the attacker's foothold, rebuilt the compromised nodes, revoked and rotated credentials and tokens, and tightened cluster access controls.

The incident has also been turned over to outside forensics experts and reported to law enforcement agencies.

## The last thing to put out the fire was GLM 5.2

When Hugging Face started analyzing attack logs, it first tried the cutting-edge model behind the commercial API, but it didn’t work.

Forensics personnel originally wanted to submit attack logs to these models for analysis. But what was recorded in the log happened to be the commands, exploit codes and control server addresses actually used by the attacker.

After the business model sees this high-risk content, it cannot determine whether the user is launching an attack or investigating an attack that has already occurred.

The security restriction is triggered and the model refuses to process.

Hugging Face finally ran the open weight model GLM 5.2 on its own infrastructure. It's not stuck by API guardrails, and attack data and the credentials involved don't need to leave the corporate environment.

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/b5cbba62fb66d270e041570795b3f3bc78610610.png" alt="OpenAI's account of the model reaching Hugging Face production infrastructure from an evaluation environment" style="zoom:50%;" />

*Source: [Hugging Face](https://huggingface.co/blog/security-incident-july-2026)*

Public review shows that the actual process is divided into several steps. Hugging Face's own security system and defensive agents detect anomalies first and are responsible for containing attacks. When the team began to review logs and restore the attack path, GLM 5.2 came on stage as a forensic tool.

Therefore, GLM 5.2 did not repel the attack on its own. It solves another thorny problem: business models refuse to analyze after seeing real attack code in logs, and Hugging Face needs a model that won't get stuck by API guardrails at critical moments.

## When evaluating Agent in the future, the evaluation site must also be regarded as the target.

OpenAI has begun to tighten infrastructure provision, even if it slows down research; they are also strengthening monitoring, access control and model alignment during evaluation.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260722164106340.png" alt="UK AISI long-range network range model capability curve" style="zoom:50%;" />

*Source: [UK AI Security Institute, quoted by OpenAI official article](https://openai.com/index/hugging-face-model-evaluation-security-incident/)*

This UK AISI long-range network range curve explains why this incident occurred.

GPT-5.6 Sol has been able to continuously complete multi-stage actions such as reconnaissance, credential theft, lateral movement, web exploitation and privilege escalation under a high token budget.

---

References:

- [OpenAI: Hugging Face model evaluation security incident](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
- [Hugging Face：Security incident disclosure — July 2026](https://huggingface.co/blog/security-incident-july-2026)
- [ExploitGym paper](https://arxiv.org/abs/2605.11086)
- [Associated Press：OpenAI says its AI technology acted on its own in an unprecedented hack](https://apnews.com/article/63ab84fed5612af04d8a160d60f6def3)
- [Axios：OpenAI says Hugging Face breach caused by one of its models](https://www.axios.com/2026/07/21/openai-says-hugging-face-breach-caused-by-one-its-models)
- [Techmeme: Summary of related industry discussions](https://www.techmeme.com/260721/p43)
