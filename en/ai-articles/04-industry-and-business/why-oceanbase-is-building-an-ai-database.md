# Why Is OceanBase Building an AI Database?

[English](./why-oceanbase-is-building-an-ai-database.md) | [Chinese Original](../../../ai-articles/04-industry-and-business/OceanBase%20%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E5%81%9A%20AI%20%E6%95%B0%E6%8D%AE%E5%BA%93%EF%BC%9F.md)

> Date: 2026-07-08

In the past three years, AI has changed too fast, indeed too fast, causing everyone's demand for AI and token consumption to grow exponentially.

We have been caught up in the leap in model capabilities brought by AI. There is no problem in using AI to design, make PPT, write front-end, write back-end, and write desktop. Coding skills are obvious to everyone. But I feel like there is a link that has been overlooked in the whole process.

There are also some bosses and Internet companies around me. I see their daily interactions with me, and one fact they revealed to me is that the input-output ratio is far less than expected.

The new model is used and the computing power is deployed, but the corresponding value is not realized, which is a headache and anxiety.

I also feel the same way. Although the model defines the boundaries of capabilities, it always feels like something is missing.

It wasn't until recently that I determined what we were missing. What we were missing was actually two words:**data**.

---

The big model is like a supercar, very powerful, but if you don't put gas in it, it won't run, but if you put gas in it, it will be like a performance monster equipped with a V8 engine.

Therefore, what everyone often calls the last mile of AI, especially for enterprises, data is the core.

The database that carries business data is the foundation of everything.

You may be thinking, isn't the database already very mature? There are so many options to choose from, including relational databases, non-relational databases, vector databases, search engines, data warehouses, and data lakes. And can't PostgreSQL also do vector searches by adding a pgvector?

What are you talking about the database for?

This is a very good question.

In the past, when we understood databases, we regarded them more as a place to store things.

For example, orders are stored in the database, user information is stored in the database, and transaction records are stored in the database.

When people want to use it, they write SQL, check data, and read reports.

But Agent is different. Agent does not check data once in a while. It will constantly look for information, write results, change status, and record what happened before.

At this time, the database is not just a warehouse for it, but a testing ground for data.

So now I feel more and more that if enterprise AI really needs to go deeper, it will eventually come back to the database.

Models are important, but models are just brains.

Data is the nutrition that supports the brain's operation.

---

According to data from Gartner, by 2028, about one-third of enterprise software applications will contain agents, compared with less than 1% in 2024, and even more exaggerated analysts believe that 40% of applications will integrate AI agents by the end of 2026.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702081421288.png" alt="image-20260702081421288" style="zoom:50%;" />

Moreover, the form of data has changed. In the past, corporate databases rarely stored data such as text, images, audio and video, because it was incomprehensible to humans and had little meaning. But things are different now. Agent can "visualize" these data and directly become the company's core asset.

Therefore, in the AI era, the database is no longer just a base for storing data, but will become the context of the Agent and the memory and disk of silicon-based life. This meaning is different.

Moreover, we are in a critical period in history. In recent years, Xinchuang and localization substitution have made everyone understand the fact that our neck is stuck.

So based on these two pain points, I did some research and finally focused on `OceanBase`.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702102100824.png" alt="image-20260702102100824" style="zoom:50%;" />

You may ask, OceanBase? Isn't OceanBase a traditional relational database? How can it be linked to an AI database?

First, I need to tell you what an AI database is.

---

## What is an AI database

I didn't understand the concept of AI database well before. I thought it was just an AI database plus a search plug-in. If you understand it like I do, then congratulations, you've gone astray like me.

AI databases need to answer a question again:**In a world driven by AI, how data should be organized, understood, and called**, this is particularly critical.

In the traditional database organization form, this question is easy to answer, of course it is carbon-based life---human beings.

In the AI era, I think Agent should be allowed to answer this question.

If the Agent is to answer this question, I think it has to be approached on two lines.

The first line is: three concepts belonging to Agent.

* context

Context is the memory of the Agent and the lifeblood of the agent. Each answer of the agent is essentially a piece of context plus a model call. Whether the right information can be accurately organized into the context fed to the model directly determines whether it can answer accurately.

* scale

Now the cost of an AI application is gradually approaching 0, so the number of applications is exploding exponentially. I saw a piece of news that Ant Lingguang already has tens of millions of applications, and Muse also supports tens of thousands of applications within the enterprise, but on average each application only has more than a hundred rows of data.

In everyone's traditional concept, scale means the complexity of the architecture and the magnitude of the code. However, in the field of AI, scale means not a large amount of individual data, but a large number of libraries. 99% of the libraries are sleeping, and a very small number of them have to respond within seconds when they are awakened.

* evolution

The Agent is actually like a child. It will make all kinds of mistakes, but you have to let it try and make mistakes. The Agent needs constant trial and error to grow. You need to set up an environment for it to be tried and tested. Nowadays, the cost of writing AI code has dropped significantly, but the cost of creating a test environment that allows intelligent agents to run safely is still very expensive.

![image-20260702132944211](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702132944211.png)

The second line is: the organizational form of the data.

The massive data accumulated by enterprises in the past, such as documents, emails, product manuals, customer service recordings, and videos. Although these data are very useful, they are basically unstructured and are often archived directly. Because these data cannot be organized, the value is not fully released.

However, in the AI era, these unstructured data can be unified managed, managed, and called together with structured data on the same base to form a context that Agent can call.

For example

A financial investment research agent reads research reports, announcements, market prices, transaction data, and news and public opinion.

A smart driving agent looks at videos, pictures, sensors, GPS, and map locations.

A health agent looks at user conversations, physical examination reports, PDFs, historical consultation records, preferences and risk rules.

So the core of the AI database I understand is not that the database calls the model.

To be more precise, it puts the data used for transactions, analysis and AI into the same system, so that tables, documents, pictures, audio and video, and vectors can be managed, checked, and used together.

![image-20260702132651560](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702132651560.png)

## Why OceanBase

On June 29, OceanBase released the**Hu-database integrated AI database**for the AI era.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260708164405794.png" alt="image-20260708164405794" style="zoom:50%;" />

You may not know much about what an integrated lake-database AI database is.

The two words "Huku" can be taken apart and looked at.

`Database` refers to the things that relational databases are good at, such as the ACID characteristics of transactions, real-time query, and high availability, and are suitable for running core business systems.

`Lake` refers to what data lakes are good at: open storage, massive data, multiple computing engines, multiple media types (text, pictures, videos), logs, vectors and other data.

**The integrated lake-database AI database puts these two types of capabilities into the same system.**
It allows a piece of data to be used for real-time analysis, to serve a variety of data searches, and to provide materials to Agents.

After understanding the concepts of "lake" and "library", the following will be easier to understand.

## What problems does OceanBase solve?

Facing the new demands brought by agents and multi-modal data, the answer given by OceanBase is not to add several AI functions to the traditional database, but to build a data infrastructure for the AI era with the integration of lakes and databases as the core architecture.

![image-20260702133119021](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702133119021.png)

OceanBase unifies the openness and massive storage capabilities of the data lake, the transaction, analysis and real-time processing capabilities of the database, as well as the multi-modal understanding, semantic retrieval and model calling capabilities required by AI, onto the same strongly consistent data base.

The core of this data base is the**OceanBase Lakebase**underlying engine.

I spent two days studying OceanBase's PPT. I found that OceanBase really stood out in a few areas.

The first direction is multi-modal data processing.

A core design of OceanBase Lakebase is to put structured fields, text, pictures, audio and video, JSON, LOB, and vectors into the same multi-mode table.

Note that this does not mean that all files are crammed into database rows.

Small objects can be InRow, large objects can be OutRow, and very large files can be hosted in object storage. The engine can perform adaptive storage based on object size and access characteristics.

What users and upper-layer applications see is still a unified table.

![OceanBase multi-mode representation](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/0748656fee19bc8a56efa9b7e7c7e83b72a45620.png)

The most critical thing here is the AI column.

When many companies do RAG or intelligent search, they will move the original data out to summarize, label, generate embedding, and then write it back to another system.

As long as the process is long, it will be difficult to ensure consistency between the original data and the results of AI processing.

The idea of AI Row is to turn AI processing results such as summaries, labels, features, and vectors into columns in the table. Model capabilities are entered into the database in the form of columns, and raw data and processing results can be managed together.

The second direction is an Agent-friendly database.

In traditional software development, we have Git branches, test environments, and rollback mechanisms.

After the Agent enters the production system, it also needs similar things, but the object changes from code to data, memory, RAG, business status and execution track.

This release of OceanBase repeatedly mentioned Fork Database, Diff/Merge, and Copy-on-Write, which essentially gives the Agent a data sandbox.**
Each Agent can fork an independent environment from the baseline library, where it can evaluate, experiment, write data, and change strategies.

If it fails, discard it directly, and if it succeeds, merge it again.

![OceanBase Agent Friendly Capabilities Instructions](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/62973c5c3a9944b88551c0462fd6fbf72d6b8a0a.png)

This capability is very friendly to AI application iteration.

The information also mentioned that the core competitiveness of production-level health applications such as Ant Afu comes from the continuous discovery of bad cases, repairing problems, and re-evaluation.

During the evaluation phase, the Agent will change processes, strategies, and data, but these operations must not pollute the online data.

And for enterprises, the value of this is not only in development efficiency, but also in whether production-level Agents can form a stable iteration mechanism.

The third direction is the integration of lakes and reservoirs.

In the past, structured data was usually placed in databases, while unstructured data such as documents, pictures, audio and video were placed in object storage or data lakes, and the two relied on external links to correlate.

In the AI era, the context required by agents naturally spans multiple data forms: a transaction, a customer service recording, an invoice picture, and a contract text. Only when understood together can a complete business fact be formed.

OceanBase Lakebase unifies the open format and massive storage capabilities of the data lake, as well as the structured management and online service capabilities of the database through an integrated lake-library architecture, integrating structured, semi-structured and unstructured data into the same set of metadata, permissions, transactions and life cycle management systems.

Therefore, data can directly support online services, real-time analysis and AI application operations without having to repeatedly move and copy between multiple systems.

![OceanBase hybrid search instructions](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/aa72924e0c319b10514b237934c66b71ea409cd0.png)

There are several real benefits here: one is Token saving.

Another factor is real-time performance: in traditional practice, data processing is offline, and the processed results have to be moved back to the online system to serve the application, with a delay of T+1 or even longer.

The integration of lake and database unifies offline processing and online services on the same data: the output of Spark ETL can be immediately checked by the SQL engine; the vectors generated by model inference can be immediately used for hybrid search. There is no longer a window period of "waiting for synchronization after processing".

Real-time is not achieved by accelerating transfers, but by eliminating transfers.

Because data does not need to be moved around, vector retrieval can be performed directly where the data is located, reducing additional storage and network transmission overhead.

## Features of OceanBase

In this release, OceanBase has formed a complete product system, which covers key aspects from the underlying data engine, data production management to business intelligence portal.

The complete product system consists of three parts:

* Lakebase solves the data base problem in the AI era

OceanBase Lakebase, as the underlying engine, carries lake-library integration and multi-modal data capabilities, allowing structured data, unstructured data and vector data to be managed, processed, retrieved and called in a unified architecture.

![image-20260702154502830](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702154502830.png)

* DataStudio solves the problem of how data is produced, managed and service-oriented;

OceanBase DataStudio is a data production, governance, and service workbench running on Lakebase. It covers key aspects such as data access, data processing, task orchestration, semantic modeling, data governance, and agent collaboration. It helps enterprises transform scattered data assets into manageable, understandable, and callable data services.

![image-20260702154419343](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702154419343.png)

* DataPilot solves the problem of how business people can use data intelligence directly.

OceanBase DataPilot is a data intelligence agent for operational analysis and business decision-making. As a unified enterprise business intelligence portal, it allows business personnel to complete analysis reports, data dashboards and credible answer generation through natural language, transforming the analysis process that used to rely on professional data teams into interactive, questionable, and reusable intelligent decision-making capabilities.

![image-20260702154349848](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260702154349848.png)

So finally, we can summarize this release of OceanBase.

OceanBase AI database is a modern data infrastructure designed with lake and database integration as its core architecture and designed for Agent and multi-modal data.

It unifies the transaction, consistency and real-time processing capabilities of the database with the openness, mass storage and diversified computing capabilities of the data lake, integrates structured, semi-structured and unstructured data into a unified management system, connects online services and offline analysis, and eliminates data fragmentation, link redundancy and engineering complexity caused by the assembly of multiple systems.

Provide a reliable, real-time, scalable data base for modern AI applications.
