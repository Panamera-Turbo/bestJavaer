# SearchNews Optimizing Direction (with WeWrite Comparative Analysis)

[English](./searchnews-optimizing-direction-with-wewrite-comparative-analysis.md) | [Chinese Original](../../../ai-articles/03-tools-and-resources/SearchNews%20%E4%BC%98%E5%8C%96%E6%96%B9%E5%90%91%EF%BC%88%E7%BB%93%E5%90%88%20WeWrite%20%E5%AF%B9%E6%AF%94%E5%88%86%E6%9E%90%EF%BC%89.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.

> Date: 2026-04-07

#SearchNews Optimizing Direction (with WeWrite Comparative Analysis)

After studying WeWrite, I found a lot of similarities between the two projects -- automated writing distribution systems for Chinese content creators. But WeWrite's doing it on a few dimensions, and it's worth it. Here are some of the specific directions of my fine-tuning:

------

One, content quality: from "can write" to "good"

**1. Introduction of a writing framework**

Your current render agent is "Give LLM material to write," lacking structured guidance. WeWrite defines seven writing frameworks (ache points, story type, list type, contrast type, trend analysis type, pure perspective type, double disk type) and automatically recommends the most compatible framework based on the topic, each with an exclusive initial strategy, subsection outline and CTA approach.

I suggest you do.`renderers/`Adds a new frame selection layer that allows LLM to judge which structure the topic is appropriate and then generate an outline by a frame template instead of being free to play.

**2. Establishment of a "human taste testing" mechanism**

WeWrite has an 11-dimensional humanise scring system that assesses whether articles are read like AI from multiple statistical indicators such as sentence length differences, paragraph rhythms, vocabulary richness, emotional distribution, byword density, and also introduces clock curve ratings to prevent "over-optimization".

There is currently no content quality assessment link in your system. It is recommended that a quality check step be added after the rendering has been completed to cover at least those indicators that are easily exposed to AI marks, namely, the diversity of sentences, the distribution of paragraph lengths, and the repetition of connecting words.

**3. Add a writing personality system**

WeWrite defines five writing personalities (cold-faced analysts, industry observers, late-night friends, sharp journalists, warm editors), each of which injects different rhythms, emotional expressions and transition patterns.

Your appliance, Agent, is currently only for formatting, no style injection. Yes.`style/`Sets of personality configurations are defined under the directory by YAML, allowing users to choose or automatically match them by platform (e. g., using "cold-face analysis" and "hot editing" for little red books).

------

# # # # # # # # # # # Two, feedback closed circle: from "open" to "self-evolution" #

**4. Achieve editorial learning wheel (most worthwhile)**

This is the most distinctive feature of WeWrite. It builds confidence and carries 30 days of decline, with automatic updating of writing rules for every 5 traverses. The effect is to gradually reduce the change rate from the initial 30% to 5%.

You can be there.`output/`Save the AI manuscript under a directory and use diff to extract editing mode when the user changes and releases it manually.`style/learned_patterns.yaml`, next rendering is injected as a few-shot example. This is the key to making the system work better.

**. 5. Fingerprint extraction**

WeWrite's.`extract_exemplar.py`Users can be analyzed for existing articles, extracting statistical indicators such as "writing DNA" - including the initial hook style, emotional peak distribution, turning patterns, end-of-service methods, and the difference in sentence length, vocabulary temperature distribution.

I suggest you add one.`style/exemplar_extractor.py`, allow the user to import its own representation, and the system automatically extracts style features, which are used to bind LLM when rendering, to make the resulting article more user-friendly.

------

# Three, material collection floors: from "search to "to "check right"

**6. Hotspot Discovery and SEO Rating**

WeWrite collects the hotspots of the three platforms of microblogging, headlines, 100 degrees, and uses the sub-totaling rating (0-100 per source) for fair cross-platform ranking, and also uses 100 degrees/360 to automatically complete the sEO heat rating (0-10).

Your collection agent is currently passive -- user gives keywords to search. One more.`collectors/hotspot_collector.py`, take the hotspot trend on a regular basis, and automatically recommend the selection in conjunction with the SEO rating, and become active.

**7. Topics over time**

WeWrite tracks the topics covered recently (7 - 3 minutes, 7 - 30 days - 1 minutes) and avoids repeating the selections, while retaining 2 - 3 permanent topics. You're only doing embedding in a single collection, lacking cross-sectional memory. Recommended maintenance of one`data/topic_history.json`, each check to avoid crash.

------

# # Four, release level: from "can send" to "stable hair"

**8. Engineering processing of tweets**

WeWrite has done a number of platform adaptation works on the conversion of Markdown micro-intelligence HTML: external links automatically transact footnotes (micro-screen-shield outlinks), automatic standardization of Chinese/English spacing, self-defined grammatical blocks such as dialogue/timelines/highlights, flexbox list to ensure consistency of rendering, dark mode adaptation (`data-darkmode-*`Properties), summary generation (120 byte UTF-8 security cut).

Yours.`publishing/renderer.py`These logics of treatment can be taken into account, in particular the outward-chain footnotes and the standardization of CJK space, which are the most common pits in the micro-letter release.

**9. Photo-generated multi-supplier disaster**

WeWrite supports 9 photo-generation providers (bean bags, DALL-E, Gemini, generalist, MiniMax, etc.) with automatic fallback mechanisms. You are currently supporting three (DALL-E, dream, Mini Max), suggesting an extension to at least five to six and achieving a chain fallback -- the first failure automatically tries the next, not a direct error.

**10. Theme/template system**

WeWrite has a 16+ layout theme that supports CSS variables and dark colour patterns. Your tweets appear to have only a single style. Yes.`publishing/themes/`Sets of style templates that allow users to choose or automatically match by type of article.

------

# # Five, architecture: From script to product

**11. Consider Skill sealed**

WeWrite is distributed in the form of Claude Code Skill, and the user is installed and driven directly into Claude by natural language. Your SearsNews is an independent CLI tool, installed and used at a higher threshold. Think about sealing the core stream line into a Skill.`SKILL.md` + `toolkit/`) lower the threshold of use while retaining CLI as an advanced usage.

**12. Configuration layer**

WeWrite uses YAML as a configuration (personality, frame, van) more than your purity.`. env`The programme is better suited to the complex configuration scenario. It is recommended that non-sensitive configurations such as LLM parameters, writing styles, platform preferences, etc. be moved to YAML files.`. env`Only keep sensitive information such as API Key.

------

# priority advice #

If resources are limited, I propose to proceed in the following order:

|Priority|Direction|Rationale|
| ------ | ------------------ | -------------------------------------------------------- |
| P0 |Edit Study Wheel (#4)|It's the core difference in moving the system from "tools" to "assets."|
| P0 |Writing frame system (#1)|Small but significant improvement in the quality of the articles|
| P1 |Human taste testing (#2)|Direct decision on whether content can be reviewed and trusted by the Platform|
| P1 |Micro-Intelligence Engineering (#8)|Address the actual high frequency pain points|
| P2 |Hot spot discovery (#6)|Increasing the efficiency of selection from passive to active|
| P2 |Fantamin fingerprints (#5)|Accompanying the study wheel to develop a complete style of personalization.|
| P3 |Other items|Progress towards real needs|

In general, WeWrite has gone further than your project on ** content quality control** and ** self-adaptation learning**, while your project has a greater advantage on ** multi-platform coverage** and ** collection source diversity**. The most valuable way to learn is to bring WeWrite's mass closed-ring capability to the multiple platforms you already have.
