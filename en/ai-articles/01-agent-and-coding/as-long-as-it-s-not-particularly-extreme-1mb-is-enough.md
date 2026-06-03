# As long as it's not particularly extreme, 1MB is enough.

[English](./as-long-as-it-s-not-particularly-extreme-1mb-is-enough.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Node.js%2022%20ESM%20%E5%8A%A0%E8%BD%BD%20bug%20%E5%AF%BC%E8%87%B4%20OpenClaw%20%E6%9C%8D%E5%8A%A1%E5%AE%95%E6%9C%BA%E5%85%A8%E7%A8%8B%E5%A4%8D%E7%9B%98.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.

> Date: 2026-03-31

# Node.js 22 ESM load bug resulting in the OpenClaw server redisclub

[toc]



Here's the thing. I told you I had OpenClaw connected to my personal Twitter page.



You can read this article.



And then just yesterday afternoon, my Clawra suddenly collapsed, and the service was useless, and it just gave this guy a rough estimate.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260327221151372.png" alt="image-20260327221151372" style="zoom: 50%;" />



I'll use the details next.

---



The service's gone. I'm going to get on the server.| grep node`



Output: root 555293 0. 1 2. 0 1181600 83864? Ssl Mar25 3: 59 Node/root/wechat-bridge/index.js

 

Good news: Wechat-bridge (this is a node service I wrote for a Twitter bridge to connect to a Twitter public and remote server) is still running, listening at 5, 000 ports and receiving requests for tweets. Bad news: OpenClaw process not found.

 

** Step one: confirm that OpenClaw did not rise**



OpenClaw, I'll use systemmd. Look at the state:`systemctl --user status openclaw-gateway`



Output: openclaw-gateway.service - OpenClaw Gateway (v2026. 3. 13)
Loeded: Loeded (/ root/.config/system/user/openclaw-gateway.service; availabled;
Activation (Auto-restart)
Process: 776260 ExecStart=/usr/bin/node/usr/lib/node modules/openclaw/dist/index.js gateway-port 18789 (code=exaid, status=1/FAILURE)
Main PID: 776260

 

It's true that the process exits together, exit code 1. Systemd has been automatically restarting, but falling together.



Why, look for the log.



`journalctl --user -u openclaw-gateway.service -n 50 --no-pager`

 

No journal files were found.



-- No entries --

 

Oh, yes. Our system log may not be configured. See OpenClaw's own file log:



`tail -50 /tmp/openclaw/openclaw-$(date +%Y-%m-%d). log`



This time there's content, but... the log only prints to start loading plugins and it's broken:



{"0":"{\"subsystem\":\"plugins\"}","1":"[plugins] plugins. allow is empty; discovered non-bundled plugins may auto-load:
 openclaw-weixin (/root/.openclaw/extensions/openclaw-weixin/index.ts). Set plugins. allow to explicit trusted
 ids.","_meta":...}
 {"0":"gateway/channels/openclaw-weixin","1":"[runtime] setWeixinRuntime called, runtime set successfully","_meta":...}



Then... it's gone. No mistakes, no anomalies, straight out. That's weird. Why is it half gone? Let me run straight to the front desk.



```shell
cd /root
 
node /usr/lib/node_modules/openclaw/dist/index.js gateway --port 18789

file:///usr/lib/node_modules/openclaw/dist/reply-Bm8VrLQh.js: 162924
export { resolveCommandSecretRefsViaGateway as $, formatSlackStreamModeMigrationMessage as $_,
markGatewaySigusr1RestartHandled as $a,...
...
... (thousands of repeated lines)
RangeError: Maximum call stack size exceeded
 at compileSourceTextModule (node: internal/modules/esm/utils: 346: 16)
 at ModuleLoader. moduleStrategy (node: internal/modules/esm/translators: 107: 18)
 at #translate (node: internal/modules/esm/loader: 546: 20)
 at afterLoad (node: internal/modules/esm/loader: 596: 29)
 at ModuleLoader. loadAndTranslate (node: internal/modules/esm/loader: 601: 12)
 at #createModuleJob (node: internal/modules/esm/loader: 624: 36)
 at #getJobFromResolveResult (node: internal/modules/esm/loader: 343: 41)
 at ModuleLoader. getModuleJobForImport (node: internal/modules/esm/loader: 311: 41)
```



Seeing it here, I understand -- it's called out of the inn, and it's spilled into Node.js' own ESM module loader, not the OpenClaw business code.

 

The first guess is, why don't we just make it bigger?



Seeing Maximum call stock size excepted, the first reaction must have been -- the default bar is not big enough.



Node js starts with --stack-size to specify the size of the bar (in KB), as if the default was 984 or thousands, and I doubled it:



Edit ssystemd service file:`vim ~/.config/systemd/user/openclaw-gateway.service`

 

was replaced by:

 

ExecStart=/usr/bin/node --stack-size=32768 /usr/lib/node_modules/openclaw/dist/index.js gateway --port 18789



32768 KB is 32MB, not one MB, is that enough?

 

Reload restart:



```shell
systemctl --user daemon-reload 
systemctl --user restart openclaw-gateway.service
```



Wait 10 seconds to see state:



`systemctl --user status openclaw-gateway.service --no-pager`



The same thing: code=exited, status=1/FAILURE, drop together. I'll add you to 64 MB.

 

ExecStart=/usr/bin/node --stack-size=65536 /usr/lib/node_modules/openclaw/dist/index.js gateway --port 18789



Try again, or not. Bite your teeth.



ExecStart=/usr/bin/node --stack-size=131072 /usr/lib/node_modules/openclaw/dist/index.js gateway --port 18789

 

Or fail.



I realized something was wrong. It's not the size of a bar, it's the truth. It's the infinity. You're the big one, it's the depth. It always explodes.



Second guess: the package is broken. Reload OpenClaw.

 

Could it have been when I installed the network, the package was missing, or the cache was broken? It's no trouble reloading anyway:

 

`npm install -g openclaw --force`

 

Waiting for installation to be completed... and then start:

 

`systemctl --user restart openclaw-gateway.service`

 

I'll wait a little longer this time.

 

`systemctl --user status openclaw-gateway.service --no-pager`

 

Then just.



openclaw-gateway.service - OpenClaw Gateway (v2026. 3. 13)
 Loaded: loaded (/root/.config/systemd/user/openclaw-gateway.service; enabled; vendor preset: enabled)
 Active: active (running) since Fri 2026-03-27 19: 26: 04 CST; 21s ago
 Main PID: 787646 (openclaw-gatewa)
 Tasks: 11 (limit: 4559)
 Memory: 455. 3M
 CPU: 8. 836s

Activate!



Let's see if you're listening.| grep 18789



![image-20260327223349949](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260327223349949.png)



```shell
curl -s --connect-timeout 5 http://localhost: 18789/v1/chat/completions \
 -H "Authorization: Bearer b981b9c0226c262ad740c20506fdb81db913c73e356ead14" \
 -H "Content-Type: application/json" \
 -X POST -d '{"model":"openclaw: main","messages":[{"role":"user","content":"hello"}]}'

The response came back: 

{
 "id":"chatcmpl_8f902dd8-885a-48df-beb4-517e3fdbee28",
 "object":"chat. completion",
 "created": 1774610855,
 "model":"openclaw: main",
 "choices":[{
 "index": 0,
 "message":{
 "role":"assistant",
 "content":"Hi! I am Clawra. How can I help you?"
 },
 "finish_reason":"stop"
 }],
 "usage":{
 "prompt_tokens": 0,
 "completion_tokens": 0,
 "total_tokens": 0
 }
}
```



** Perfect. Reloading will solve 99. 99% of the problem.**



Why is this a problem? Depth Analysis



Now that we're in service, we need to get back to work. Is it really Node.js' bug? Or is OpenClaw wrong?



At what stage does the problem arise?

 

From the wrong cage:



```js
RangeError: Maximum call stack size exceeded
 at compileSourceTextModule (node: internal/modules/esm/utils: 346: 16)
 at ModuleLoader. moduleStrategy (node: internal/modules/esm/translators: 107: 18)
 at #translate (node: internal/modules/esm/loader: 546: 20)
 at afterLoad (node: internal/modules/esm/loader: 596: 29)
 at ModuleLoader. loadAndTranslate (node: internal/modules/esm/loader: 601: 12)
 at #createModuleJob (node: internal/modules/esm/loader: 624: 36)
 at #getJobFromResolveResult (node: internal/modules/esm/loader: 343: 41)
 at ModuleLoader. getModuleJobForImport (node: internal/modules/esm/loader: 311: 41)
```



See? All call pads are in the code of the Node.js' own ESM module loading, and none of the lines are OpenClaw business codes. It means that when you go into unlimited regression, the OpenClaw code is not executed, and the loading phase blows.



** Why infinity?**



The current npm package distribution CLI tool has a common way of packing: Put the whole application on + all dependencies, wrap it into a huge single file ESM, then release it directly.



The advantage is...

- The user installation is a file, saves the next pile.
- No, node your-cli.js.
- CLI tool for global installation



However, this type of packing has one feature: all modules are in one file, and the packing tool generates many loops of re-export-A export B, B export A, or index export all submodules, and re-export back to index.



On the top of Node.js 20, this logic runs fine. Why is there a problem with Node.js 22?



Must have been Node. js22 modified to load the ESM module. I went to changelog, Node. js22 did make a lot of changes in the ESM loading, modular analysis.



The probability is:



- New realization is bad for "single file multimodules" + re-export
- Every time I've seen an I. M. Report, I'm going back to the full resolution.
- And then it's creating a back-up call -- A, quote B, trigger resolution B, B, quote A, trigger resolution A, so it's endlessly circular.



****



** Why can a MB run after reloading?**



After reloading OpenClaw, I found out that even the default 1MB inn could run! The initial failure was expected to be damage to the old installation package.



Reloaded with the latest package output, the packing tool may be better suited to recycling dependence in the new version, and the regression depth is just down to 1MB. Plus the ban on rebooting avoids double loading.



If you have this problem, press this:



Option one: Go straight through (recommended, I'm using it now)



Modify your ssystemd service file:



```shell
# As long as it's not particularly extreme, 1MB is enough.
ExecStart=/usr/bin/node --stack-size=1024 /usr/lib/node_modules/openclaw/dist/index.js gateway --port 18789
# Add this environment variable to be disabled from restart and avoid double loading of wastehouses
Environment=OPENCLAW_NO_RESPAWN=1
```



Then restart:

 

```shell
systemctl --user daemon-reload 
systemctl --user restart openclaw-gateway
```



Authentication:



```shell  
curl -s http://localhost: 18789/v1/chat/completions \
 -H "Authorization: Bearer <your-token>" \
 -H "Content-Type: application/json" \
 -d '{"model":"openclaw: main","messages":[{"role":"user","content":"hello"}]}'
```



I can get an AI response and it works.



Option II: Resolved - downgraded Node 20



If you touch a bigger bag, 1MB or explode, cut back to Node 20: 30.



```shell
# The nvm management version is easy
nvm install 20
nvm alias default 20
npm install -g openclaw --force
systemctl --user restart openclaw-gateway
```



# Rewind it



I've been inspired by the fallout:



Be careful with big upgrades - Node.js, a bottom-up tool, new projects, running services in the production environment, major upgrades, and not later than a few releases.

 

The error vault is telling the truth - this error directly points to the inside of Node, the ESM loader, and the OpenClaw code was wrong at first, saving a lot of time.

 

From being a kid to trying -- starting at the minimum inn, you'll find it's not as bad as you think.

 

Since restarting, OpenClaw can sometimes be confusing -- it's not necessary to start up with the system, but rather to solve the problem.

 

Node 22 has to write down the pit - it has run into an inexhaustible plume, first thinking about whether it hit the bug.



Is it a miscalculation?



I've been wondering if there's a miscalculation, because the memory leaks caused by this regression sound too low and too serious, and if it were a Node.js bug, it would have been discovered long ago.



And then I looked online and found that Node.js' official warehouse had exactly the same problem.



Links: https://github.com/nodejs/node/issues/52864

Submitted: May 2024

Status: officially confirmed and processed



The ESM module loader of **Node.js 22, when dealing with `cycle reference/ loop export ', triggers unlimited regression, which eventually leads to a collapse of the stack.**



This bug has been officially repaired.



And I showed up with this bug and it wasn't like that.



This Bug specifically triggers at:



** Large Single File ESM + Large Cycle Re-export**



This is the CLI tool webpack/rollup to pack.



To date (2026-03),** the official has not been repaired.**



I've submitted the issue to the Node.js official, the issue here, https://github.com/nodejs/node/issues/62457Wait for official confirmation.



If you have any new information, I will update you in time.
