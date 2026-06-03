# Now, call cxuan smart!

[English](./now-call-cxuan-smart.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/QClaw%20%E5%AE%9E%E6%B5%8B%EF%BC%8C%E8%BF%99%E7%8E%A9%E6%84%8F%E7%A9%B6%E7%AB%9F%E5%92%8B%E6%A0%B7%EF%BC%9F.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-03-18

[toc]

## V 0. 1. 7



Let's start with the stupid thing. I told you I had applied for eight. I got an internal code at 6: 00 yesterday when I came home, and I tried to forward it to myself. Although I pulled back in seconds, I couldn't protect the wolves.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/9f702a92f5d8c8c0c316b9b9c0b3c109.png" alt="9f702a92f5d8c8c0c316b9b9c0b3c109" style="zoom: 50%;" />



I wanted to reapply, but it turns out I did.



** If there's someone in the group who sees me like this, will you laugh?**



Just as I thought it was out of line with this introspection, the next day I came to work, and I found another cell phone for hot spots, and I got an internal code, and I had to say, thanks to QClaw's love.



What are you waiting for?



---



# QClaw Actual



A few days ago, a text was sent describing the access to WorkBuddy.



[url]



I was wondering why his chat window appeared in client service, which seemed a little low. QClaw, same.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/647c183f-c16c-4924-a6d9-02fff3283be9.png" alt="647c183f-c16c-4924-a6d9-02fff3283be9" style="zoom: 50%;" />



Currently QClaw does not support photo uploads, but only text descriptions.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/8a3deb61-d174-418a-a9a7-a17427853533.png" alt="8a3deb61-d174-418a-a9a7-a17427853533" style="zoom: 50%;" />



Also, the message does not support two-way distribution and synchronization for the time being, only the QClaw client currently communicates with QClaw, which is currently only a medium for the message.



Seeing here, I laughed:** internal editions. Clients take the pit first.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260317085438287.png" alt="image-20260317085438287" style="zoom: 50%;" />



I was going to use it to send a message to my friends, and the result** has been a failure.**



I was going to use it to send a message to a friend of ours, but it always failed, and I asked him why, and it didn't make me happy because it seemed like he was in ** a dead lock.**



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/c0df0ce3-663a-4fc2-a37e-c8b9459776a4.png" alt="c0df0ce3-663a-4fc2-a37e-c8b9459776a4" style="zoom: 50%;" />



It continues to be asked for reasons, and the problem is that now the webhat-access plugin has not materialized ** to the user, only to receive the message **. SendText made me laugh just by writing. Isn't this a waste of server resources that QClaw simply responds to a functionality that is not achieved?



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/d29e99c7-2098-4358-9cb4-e607b442796b.png" alt="d29e99c7-2098-4358-9cb4-e607b442796b" style="zoom: 50%;" />



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/76195e9f-9868-4eeb-bd81-9f52ee52ac96.png" alt="76195e9f-9868-4eeb-bd81-9f52ee52ac96" style="zoom: 50%;" />



This exposes the current QClaw ** ecology of the plugin is still under construction**. But that's what it means to be inside -- to help them find these "written dead" pits.



I also found a phenomenon in the course of the test: QClaw has to be given a solution whenever a problem arises.



Like I said, "Why can't it come out?" And it said, "What do you think you should do?"



I thought: ** Am I checking you or you checking me?



It's like an employee can't work as a leader.



This may reflect a general problem of the current AI - ** will not think of itself, the call chain is too short.** When you encounter a card point, you dump it to the user instead of trying to analyze it.



But QClaw is not nothing. What surprises me most is its **Action capabilities**.



---



I want it to go to the cloud server and look at OpenClaw's configuration, and assign it a temporary account number and access -- it can actually log into the cloud and get the configuration out!



![image-20260317164710464](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260317164710464.png)

** That's what smarts look like! ** Although the basic function is still grinding, this core ability is already interesting.



Yesterday, an article was written on GLM-5 Turbo, the first model to allow me to make my own judgement and decision and then to accomplish my mission. The article is linked below.



[url]



I've come up with another solution, let it **SSH up, grep a little bit about the sendText error in the log, then give three possible solutions based on the error and assess the feasibility of each. ** See what it will do.



I thought it was just going to be SSH up there, and I didn't think I'd tell it ** "OpenClaw didn't write the log file, the log just went to stdout"** ** and I was confused about its performance:



It just told me: ** No logs are needed, code analysis alone can provide solutions!**



And then it really gave us three options, and it struck the star sign with care:



-**Programme I (⭐⭐⭐)**: modified plugin sent via WebSocket

 

API (but my AppSecret is frozen)

 

-**Programme III (⭐⭐⭐⭐)**: until updated by the author

 

When I saw this response, I was down in my mind.



** Is this really thinking?



---



Come on, let's get this straight:



** If it's real thinking**: it should understand what "no log" means, know what it means, ask me for more information, or say, "Well, I'll use SSH."`docker logs`Or...`journalctl`Look at the real time output."



** If it's a false thought**: it's just a combination of the information points that I mentioned in my previous conversation (sendText writes dead, wsUrl is empty, AppSecret freezes), and it's output using a template called Question-Program. Looks rational, actually pretending to think.



Look at the plan it gives:



- Option 1: Based on the code I saw (written dead + wsUrl empty)

 

- Option 2: Based on "AppSecret frozen."

 

- Plan III: A universal bottom-up programme

 

** It didn't bring any new information, just sorting out what I know.**



The real thinking should be:



** "I can go if there's no log file.`/var/log`See if there's any other logs or something.`strace`Track the process output, or modify the startup script to redirect the stdout to the file...**



But it didn't.



So, back to the question at the beginning:** Can it be sure that this is thinking?**



** My conclusion: No, it's not thinking, it's a "high-level fusion."**



It is like a well-reconciled student who has organized the classroom notes, but does not really understand the links between knowledge and will not do anything.



But it's not all bad -- at least it learned to shut up and stop asking me for solutions.



QClaw is like ** "A growing smart body"**, which has good information integration skills, understanding complex commands, implementing cloud operations, and is already operational.



But at the same time, there is something that needs to be worn out:** "false thinking" is a serious phenomenon**: it seems rational, but it's actually collating known information;



** Lack of real reasoning **: no new proposals will be presented, only a summary of old information;



** Plug-in ecological incomplete**: core functions are still dead.



Since it's so good at collage, I'll take it again:



**"Program one says you have to realize WebSocket sent. Can you get SSH up there, please?`tcpdump`Grab the package between the Twitter client and wechat-access and analyze the protocol format for me? If you don't, is there another way?"**



This time I'll see if you really think, or you'll continue to spell...



And he said,



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/d1239c14-16e0-4fae-bdc4-babe0f574a09.png" alt="d1239c14-16e0-4fae-bdc4-babe0f574a09" style="zoom: 50%;" />



** Is it true this time, or is it a superstitious spell?**



Let's break it down:



** If it's a jiggling**, it should only rearrange the information I mentioned earlier (sendText written dead, wsUrl empty, AppSecret frozen).



** But not this time **:



It understands the AGP protocol -- it's not the information I gave, it's from the source code.

 

It found out ** "It's because of another mechanism"** -- this is the reasoning, not the repetition.

 

It gives ** a new breakthrough** - this is a directional proposal, not a bottom-up option.

 

What is most critical is that it admits that the programme is not working, rather than hitting three stars as vaguely as before.



** This is real thinking** - not sorting out known information, but digesting information to draw new conclusions**.



So it really thinks?



This time, it feels like it's true.



The "think" before was a collage, the "think" this time was a reasoning. The difference is:



- ** Collapse**: clean up the debris information and look reasonable, but nothing new.

 

- ** reasoning**: digest information, find contradictions, ask new questions, give new directions

 

It discovered the contradiction of "getting the message but wsUrl is empty" and deduced that "there must be another mechanism at work" -- that's the trace of reasoning.



Of course, its last question was limited: ** It didn't know how wsUrl fit, but asked me.**



The real expert should go through the file, search the configuration, or SSH go up and grep the profile.



But at least,** it learned to find problems, not just to summarize them.**



## V 0. 1. 8



QClaw came back tonight and updated another version, and it's estimated that the internal code has been released.



It is possible to start with a new dialogue.



![image-20260317220534966](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260317220534966.png)



And then we added an inspiration square.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260317220708336.png" alt="image-20260317220708336" style="zoom: 50%;" />



It looks like a series of skills just to make you an UI form out.



If you're talking from an inspiration square, then you can talk from a QClaw client, but you still don't support a direct response if you sync the messages from Twitter. I asked him to explain to me what the Transformer structure was.



![image-20260317221654231](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260317221654231.png)



For example, I told him to check my life story. It's true that the program ended up like ** gossip**.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260317222429673.png" alt="image-20260317222429673" style="zoom: 50%;" />



I wonder if there's something in the back door that's supposed to make me like this QClaw.



**Inspiration Square is equivalent to ClawHub, making a series of Skills into a square that can be browsed, discovered, installed with one key. It's a good direction, and when Skylls is ecologically rich, ordinary users don't have to write their own configurations, just go straight from the square, and the threshold is much lower.**



From the configuration, you can see usage statistics, measured within 4000 w token a day? That's too much.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260318063459963.png" alt="image-20260318063459963" style="zoom: 50%;" />



Skills management allows free access to various skills.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260318063613210.png" alt="image-20260318063613210" style="zoom: 50%;" />



Also, the new memory function, which is still practical, is equivalent to your personal soul.md, just for you to configure from UI.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260318064742135.png" alt="image-20260318064742135" style="zoom: 50%;" />



QClaw's been worrying about traffic since birth, depending on the power of the portal. ** If QClaw is to be the next national application, security and user privacy must be the top priority.



# Write at the end



It's been interesting for two days.



From the moment of hand slips the internal code to the moment of the community's death, to the moment of surprise of the second code; from the drop of the code that it "writes death" to the ability to excite its SSH on the clouds; from the moment of doubt that it "pretends thinking" to the moment that it actually deduces the AGP protocol...



** QClaw is like an extremely slow child.**



It's got talent -- action skills, inspiration squares, memory functions, and these skeletons are already pretty.



However, it is not immune to wrestling - incomplete plugins, hypocritical thinking, response restrictions - which are the pits necessary to grow up.



Most interestingly, in the course of the introspection, I found myself unwittingly turning from a "tester" to an "observer". Instead of simply documenting what it can and cannot do, I started thinking about a bigger question:



** When AI begins to learn to "discover problems" rather than "summarize problems", when it evolves from "mixing information" to "controversial contradiction of reasoning", will our relationship with it change quietly?**



Are we introspecting AI, or are we introspecting human patience and expectations?



I don't know the answer.



But I know that tomorrow, QClaw will probably update another edition.



And I would probably continue to sit in front of the computer and knock on new problems and see if it would surprise me again - or a new slot.



After all, seeing a thing goes from 0. 1 to 1. 0 is an interesting thing in itself.
