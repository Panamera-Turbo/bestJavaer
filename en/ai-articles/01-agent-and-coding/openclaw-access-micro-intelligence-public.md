# OpenClaw Access Micro-Intelligence Public

[English](./openclaw-access-micro-intelligence-public.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E4%BB%8A%E5%A4%A9%E6%88%91%E7%9A%84%E7%9B%AE%E6%A0%87%E5%B0%B1%E6%98%AF%EF%BC%8C%E6%88%91%E8%A6%81%E6%8A%8A%20QClaw%20%E6%8E%A5%E5%85%A5%E5%88%B0%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7%E4%B8%AD%E3%80%82.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-03-23

[toc]



In fact, if you were a friend of new interest these past two days, you would have found out by the time you responded to the private letter, that the content of the public reply is no longer a cold key link.



It's a lively, naughty little AI hiding behind the public call to respond to your message.



![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/c65e98f3-8e63-416b-8b57-199af6fd3ac2.png)



That's right. ** I've got OpenClaw on the Twitter public.**



Just yesterday, we posted the message that Clawbot (which is actually OpenClaw) was connected to the micro-mail, and once it was released, it went directly into the pot. Because Twitter is a huge source of ecological flows, it will grow with Clawbot's access.



I have to say, the logic of micro-mail access to OpenClaw is exactly what I thought it was, except that he had access to the micro-letter, and I had **OpenClaw access to the Micro-Intelligence Public.**



Why would you do that?



People who have used AI assistants know that the most trouble is not AI itself, but the entrance.**



Opens web pages, log-in accounts, finds dialogue boxes... each time it takes so many steps, it takes too long.



We believe differently. It's an app that I have to open every day. If AI is in the public domain, it'll be much more frequent to send a message at any time.



However, the MSC itself cannot be directly connected to AI, requiring a protocol conversion at an intermediate level - to convert the MSL/JSON message format to OpenAI compatible format, then to transfer the output of the large model back to the MS message format and push it back through the client service interface.



This middle level is a small service that wrote a Node.js.



The entire call process is as follows:



```
Can not open message
Zenium
We believe in the public platform cloud
Zenium
My Server (nginx + Node.js)
Zenium
Request Queue
Zenium
OpenClaw (AI gateway)
Zenium
Large model generation response
Zenium
Actively delivered via micro-letter client message interface (access token required)
Zenium
Reply to User
```



Since I used V1. 0 synchronized methods before I wrote to the public before I certified, I had to reply only because I had to limit ** private messages to 5s.



If you're dealing with a process that receives a message, calls a big model, returns the results, then five seconds is not enough -- the big model is growing back and forth in just ten seconds. The consequences are:



* Request timeout, micro-mail retest, call again a big model, timeout
- Users receive duplicate responses or simply do not receive them
- Suffering of the author ' s wallet: waste of repeated calls token



This experience, I'm a reader and I'm taking it directly.

![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260322102933103.png)



The scheme is therefore not available until the certification is approved. And that's one of the key reasons why I have to authenticate a public number, get AppSecret in order to use the V2. 0 walk.



---



Once the authentication public has access to AppSecret, we can walk:



** Core idea: Once the message has been sent, the message is sent back to the empty successful answer (to inform the message "I got it" ) and then the backstage step, which is processed, is sent ** to the user via the letter "The client message interface"**. This way the 5-second limit is completely avoided.



![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/c38fffdb-c74d-437e-93ba-0eb9b4695ceb.png)



Key process codes are probably the following (simplified version):



```js
// Wireless Public Access.
app. post('/wechat/callback', async (req, res) => {
 const message = parseWechatMessage(req. body);

 // Critical point: Return immediately to success and release the connection
 res. status(200). send('');

 // Step into queue
 messageQueue. add(message);
});
```



Then backstage consumers handle:



```js
async function processMessage(message) {
 // 1. Speed limit inspections
 if (! rateLimiter. check(message. fromUser)) {
 await sendWechatMessage(message. fromUser,
 "Requests are too frequent. Please try again in one minute.");
 return;
 }

 // 2. Call OpenClaw to get AI responses
 const aiReply = await openClaw. chat(message. content, message. fromUser);

 // 3. Promotion to users through client service interfaces
 await sendWechatMessage(message. fromUser, aiReply);
}
```



Access token manage pits:



![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260322211855592.png)

This means that the access token interface is called only a limited number of times a day



- Access token valid 2 hours. Expiry requires refreshing

 

- If multiple cases are deployed, one access token must be shared across the board



So my approach here is to maintain single-case mode + auto-renew:



```js
class WechatTokenManager {
 private accessToken: string = '';
 private expireTime: number = 0;

 async getToken(): Promise<string> {
 // If it's not expired, go straight back.
 if (Date. now() < this. expireTime && this. accessToken) {
 return this. accessToken;
 }

 // Expired reacquiring
 const response = await fetch(`https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${APPID}&secret=${APPSECRET}`);
 const data = await response.json();

 this. accessToken = data. access_token;
 // Five minutes ahead to prevent criticality.
 this. expireTime = Date. now() + (data. expires_in - 300) * 1000;

 return this. accessToken;
 }
}
```



This ensures that what is available at any time is valid token and will not be called frequently.



As a personal site, with limited resources, it is important to limit flow. I designed two layers:



---



# First tier: user-level rate limit





The rules are simple:



- Up to 15 requests per user: 1 minute
- Right over the limit: "Please try again in a minute.
- Fixed time window (zero per minute)



A Map save user count is achieved and timers are regularly cleared:



```js
class RateLimiter {
 private userRequests = new Map<string, number[]>();

 check(userId: string): boolean {
 const now = Date. now();
 const window = 60 * 1000; // One minute window

 // Clear expired records
 const requests = (this. userRequests. get(userId) || [])
. filter(time => now - time < window);

 if (requests. length >= 15) {
 return false;
 }

 requests. push(now);
 this. userRequests. set(userId, requests);
 return true;
 }

 // Regular clean-up of obsolete data to prevent leakage of memory
 cleanup() {
 const now = Date. now();
 const window = 60 * 1000;
 for (const [userId, times] of this. userRequests) {
 const valid = times. filter(t => now - t < window);
 if (valid. length === 0) {
 this. userRequests. delete(userId);
 } else {
 this. userRequests. set(userId, valid);
 }
 }
 }
}
```



---



# 2nd Layer: Parallel + Queue Control



The large model reasoning is resource-consuming and cannot be carried out in an unlimited manner, so it is addressed as follows:



- Up to 32 requests processed simultaneously
- Queue to wait: 100 requests
* In excess of the queue: "Please try again later with the current high queue."



This can be done with the Bull or the Node.js' own queue, which I use here is a simple queue by the original Node.js array + setImmediate.



```js
const requestQueue = [];
let currentConcurrent = 0;
function processNext() {
 if (currentConcurrent < MAX_CONCURRENT && requestQueue. length > 0) {
 const task = requestQueue. shift();
 currentConcurrent++;
 process(task). finally(() => {
 currentConcurrent--;
 setImmediate(processNext);
 });
 }
}
```



I don't think it's that big in terms of my current traffic, and that's enough.



![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/11656222-8192-4b91-9e02-322572376f20.png)

![](https://cdn.jsdelivr.net/gh/doggaifan/picbed/552415dd-32a4-4c4b-957b-247e70ddcf5d.png)



---



# How do you keep the memory of multiple sessions? How can we guarantee that we're isolated?



In order for AI to be able to talk to people on a continuous basis, the context must be preserved. My approach is:



- Use the user ' s only OpenID as the history of Key storage conversations, with different users completely isolated.

- Maintain the latest N round for each dialogue (control of the length of context, savings token)

- Over 24 hours of inactive automatic clean-up

* uschat-bridge Local Management History + uniqueUser



So you can guarantee that your conversation with Clawra will only be visible to you and will never be associated with other users.



Now there's an AI that really talks, remembers, has personality, answers questions and cares about you.



Most importantly - ** The entrance has become simpler.**



Open micro-mail boom find "cxuanAI" send a message to finish.



Now cxuanAI can be used as an ** smart body.**



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/b9babc8a-ebc0-4631-8b96-daf0ec39b0fa.png" alt="b9babc8a-ebc0-4631-8b96-daf0ec39b0fa" style="zoom: 50%;" />



---



# About context limits



I have measured that in multiple rounds of dialogue, the preservation of the context is key to allowing AI to understand the history of chat, but the length of the context cannot grow indefinitely - the big model has token limits (generally between 4K-128K), and the long history of dialogue leads to the following problems:



- Token Excess: Each model has the maximum context length (Context Windows). For example, I'm using a code plan:
* Input limit: about 6K characters (≈3K Token)
- General limit: 4K Token (including user input + system hint + history)



Over the limit, the interface returns 400 total tokens of image and text except max message tokens.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/1fa74aeb-ae73-4a28-8d8f-20a6c4e2da45.png" alt="1fa74aeb-ae73-4a28-8d8f-20a6c4e2da45" style="zoom: 50%;" />



Achievement programme:



I've made strict context management in the middle of Node.js:



```js
// Dialogue History Storage
const userHistories = new Map(); // key: openid, value: Array<{role, content}>

// Keep the latest 8 rounds (16 messages, 8 user+assist)
const MAX_HISTORY_ROUNDS = 8;

async function processMessage(fromUser, content) {
 // Getting or Initializing User History
 if (! userHistories. has(fromUser)) {
 userHistories. set(fromUser, []);
 }

 const history = userHistories. get(fromUser);

 // Join Current Round
 history. push({ role: 'user', content: content });

 // Crop History (retain the latest N round)
 if (history. length > 2 * MAX_HISTORY_ROUNDS) {
 history. splice(0, history. length - 2 * MAX_HISTORY_ROUNDS);
 }

 // Details of messages sent to large models
 console. log(`Sending to OpenClaw: user ${fromUser}, ${history. length} messages`);

 // Call Big Model...
}
```



**/new command pit**



The original /new command only cleaned up local userHistories, but OpenClaw/BigMix still has an internal history of dialogue. The resulting sentence is still token beyond limit.



Solution: every time OpenClaw API is called, add a time stamp suffix to the user parameter and completely bypass the cache:



const uniqueUser = `${fromUser}_${Date. now()}`;



Now use /new to clear the session window again.



>Note: This is not about emptying the chat window for private communications from the public, but about emptying the historical records of OpenClaw. Because of the public number limitations, it is not possible to empty chat window information like /clar.



So when you use the /new, it's like starting a new session.





# About costs and the use of alarms



Now, Clawra's using a big model that I buy token to serve, so:



* Normal use is totally fine, though.

- Try not to make frivolous repeated requests and save token for everyone.

- One minute if you have a restricted flow problem.



It was supposed to be an 18-year-old sweet Korean girl, but with this look now it looks like a scoundrel is responding. Don't get me wrong. I'm actually a good-looking guy.



And from now on, Clawra is all shared, so please treat her well, and every time you use it, you're helping her grow up.



Finally, I have produced an information document to collect your comments and leave your valuable response.
