# Vercel was hacked, this time from an AI tool.

[English](./vercel-was-hacked-this-time-from-an-ai-tool.md) | [Chinese Original](../../../ai-articles/04-industry-and-business/Vercel%20%E8%A2%AB%E9%BB%91%E4%BA%86%EF%BC%8C%E8%BF%99%E6%AC%A1%E6%98%AF%E4%BB%8E%E4%B8%80%E4%B8%AA%20AI%20%E5%B7%A5%E5%85%B7%E7%AA%81%E7%A0%B4%E7%9A%84.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-21

# Event

On April 19, Vercel confirmed a security incident, Vercel's statement report. https://vercel.com/kb/bulletin/vercel-april-2026-security-incident.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260420122614051.png" alt="image-20260420122614051" style="zoom: 50%;" />

The hackers claimed to have obtained internal data from Vercel, which was being sold at $2 million. Vercel subsequently issued a bulletin acknowledging that the system had been invaded and that the impact had affected some of its clients.

OpenAI, Cursor, Pinterst and Bose are all on Vercel's customer list. If the data were leaked, the impact would not be small.

---

How did it break

Vercel CEO Guillermo Rauch discloses details on X:

The starting point of the attack is an ** third party AI tool**.

A Vercel employee used a third-party AI tool whose Google Workspace Outlook application was invaded. Through this OAuth-applied access access, the assailant entered the employee ' s Google account, thus penetrating the Vercel internal system.

The whole link is:

**Third party AI tool ** Contaminated OAuth application ** Employees Google account ** Vercel internal system**

It's not a hole in Vercel's own code. It's a third-party tool security problem that drags Vercel together.

![image-20260420133158746](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260420133158746.png)

Vercel subsequently released CVE-2026-23869 to record the event and advised all clients to check their own environment variables, open sensitive environment variables and rotate keys as necessary.

---

# Encryption developer panics first

And when this came out, the first move was on encryption developers.

Since Vercel hosts a large number of Web3 applications, they usually rely on API keys to access block nodes and wallet services. If these keys are leaked, the attackers can directly manipulate the user ' s funds.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260420131304599.png" alt="image-20260420131304599" style="zoom: 50%;" />

So as soon as the message came out, a lot of encrypted projectors immediately started rotating API keys. The impact of this matter is not only in the technical circles; it is directly related to asset security.

Vercel highlighted a technical detail in his communication:

> > > The assailant was able to access part of the Vercel environment and ** an environmental variable not marked `sensitive'**. In Vercel, environment variables marked `sensitive' will be stored in a way that cannot be readable, and there is currently no evidence that these sensitive values have been accessed."

However, many developers, out of convenience, did not turn on the "sensitive environmental variables protection" function. This means that stored as explicit environmental variables (e. g. API keys, database passwords, signature private keys) are high-risk exposures in this event.

---

A point worth thinking about

Vercel is an infrastructure company. Next.js was developed by them, EdgeFunctions, Servers, CI/CDs, which are standard products in the developers' circles.

But the stronger infrastructure does not hold the third-party AI tool for the employee computer.

It's not about Vercel. It's a whole industry problem.

How many developers are using various AI tools now? Writing assistant, code completion, translation, summary generation. These tools increasingly get your OAuth privileges -- access to your Google account, GitHub account, desk mail.

The depth of penetration of these powers may not even be clear to you.

Vercel was not punched in by a frontal attack, but brought in by a third-party tool on the flank. This is the path of the attack, and there's a name in the circle called ** Supply Chain Attack.**

** You're safe, but your tools are not safe, and you're not safe.**

Remember that.

---

Who's Shiny Hunters?

It was Shiny Hunters who claimed responsibility for the incident.

![Hacker Forum Post](https://cdn.jsdelivr.net/gh/doggaifan/picbed/vercel-hacking-forum-post.jpg)

This hacker organization has been active recently, with the front foot attacking the GTA developer Rockstar Gomes, and now breaking Vercel. Their style is to invade large companies, steal data and sell publicly.

Two million dollars is not a bluff. If Vercel's data really contain the source code or key of a large customer, the price is not abnormal.

According to Vercel,** no sensitive data were accessed** and the services themselves were not affected, but only some clients.

But that would require a question mark.

Such cases of data disclosure usually take weeks from discovery to confirmation of the extent of the impact. Vercel says no now, doesn't mean no really.

For Vercel's clients, the time has come not to wait for official conclusions, but to check their own environment variables, rotate key, and confirm that there is no unusual access.

Vercel is a company that eats on a safety watch. The damage to brand confidence in this event is not a matter of how much it costs.

But the deeper question is, it's not the last company to be broken by "third party AI tool."

As AI tools increasingly permeate the day-to-day work of developers, their security risks are magnified simultaneously. These tools have the same level of security as your own code library.

Do you trust your AI assistant? Do you know what's behind that AI tool you used?

Most developers do not know.

This is a reminder for the whole industry: **AI tool security, not just AI. Enterprises using these tools also have to include AI tools in their own security audit.**

Otherwise, the next person to be dragged down by a third party will not be only Vercel.

---

Sources:
- [Vercel confirms breach as hackers claim to be selling stolen data - BleepingComputer](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/)
- [Vercel hacked, hacker using ShinyHunters name to sell data for $2 million - India Today](https://www.indiatoday.in/amp/technology/news/story/vercel-hacked-hacker-using-shinyhunters-name-to-sell-data-for-2-million-2898719-2026-04-20)
- [Hack at Vercel sends crypto developers scrambling to lock down API keys - CoinDesk](https://www.coindesk.com/tech/2026/04/20/hack-at-vercel-sends-crypto-developers-scrambling-to-lock-down-api-keys)
- [Vercel April 2026 security incident - Hacker News](https://news.ycombinator.com/item?id=47824463)
- [Summary of CVE-2026-23869 - Vercel](https://vercel.com/changelog/summary-of-cve-2026-23869)
