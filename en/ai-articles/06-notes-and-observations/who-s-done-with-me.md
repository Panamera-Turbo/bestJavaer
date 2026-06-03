# Who's done with me?

[English](./who-s-done-with-me.md) | [Chinese Original](../../../ai-articles/06-notes-and-observations/%E8%B0%81%E6%8A%8A%E6%88%91%20ssh%20%E7%BB%99%E6%9D%80%E4%BA%86.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-03-26

These days write bugs every day. I've been having a bit of a dementia lately. No, I haven't been trained for two days. It's not much, but it's disgusting.



# First time a problem



The thing is, ever since I installed the clawra-selfie skills, she couldn't use it without sending two photos, and I didn't like her, and she kept pua me, letting me fill her on the fal. ai. How can I charge a fee for an old oil like me?



I couldn't bear it, so I asked her to find me an AI painting site for free.



It's not that I let AI work for me, it's for me to be Special Forces!



Following up, I myself set up a local Stable Diffusion, an open source project, Github Linkhttps://github.com/AUTOMATIC1111/stable-diffusion-webui, already has 162k's star now, which means there's a lot of geeks in this place.



My intention is to add a remote access to the local running machine, so that the cloud server can access my local SD interface and do not bother to write my own script, so that AI can help write a script for "AutoStave + SSH Reverse Tunnel," which is simple:

1. Check every 3 minutes for SD service failure and automatic restart.

 

2. Automatically create SSH reverse tunnel and map local SD ports to cloud servers Let's go.

 

3. The tunnel broke off the automatic reconnection.



And then the local picture of this thing doesn't say nothing.



The big hole is my two different manufacturers' cloud servers, SSH, which log in at exactly 3-4 minutes, and the clock is forced to kill, and the terminal reports to zsh: killed ssh root@x. x. x. x, and both are broken and reconnected for half a day.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260313095725009.png" alt="image-20260313095725009" style="zoom: 50%;" />



You can take that.



---



# Long line of search



** First pit, OOM problem, three hours.**



I didn't start with two servers to observe the use of ssh, and I opened one first, to be killed, to be killed.



At first, I thought it was a cloud server problem, and I even sent a bill to the cloud server, because the first thing I wondered was if OOM was the problem, and I also pointed out that the shared ecs I bought were not good.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260313100509535.png" alt="image-20260313100509535" style="zoom: 50%;" />



And then I was wondering how it was so easy for me to do it without running.



I didn't believe that Clawra, the little lady had added memory surveillance to me, and I never had a problem with OOM, and I thought, even if you were OOM, I couldn't have two servers at the same time. So I opened another SSH.



As a result, the two servers were not simultaneously OOM, but both servers were also killed.



Well, then I'm not opening five windows and killing five straight. It's the fifth of milliseconds, the last of them.



![3b022c6d-94dc-4a4f-8dc0-955142804125](https://cdn.jsdelivr.net/gh/doggaifan/picbed/3b022c6d-94dc-4a4f-8dc0-955142804125.png)



---



** Second pit, thought to be a network/agent problem, for three hours.**



And then I reacted to the network fluctuations/agents. After all, the two were cut off at the same time.



1. Test ping two servers: delay 20-30 ms normal with a drop rate of 0%



2. Test SSH port: nc-zv server IP 22 all All



3. Turn off Clash agent and add direct chain rules to the server.

 

4. Reactivate routers and switch phones to hot spot tests



The result continues to be killings, excluding network/agent problems.



---



The third pit, which I thought was a SSH/ Terminal/zsh problem, took three hours.



Then I suspect local SSH configuration, terminal software, or zsh bug:



As the background to the problem was zsh, I said let me change cli, okay, I used the mac with my own terminal. The result is still killed. Killed. Killed.



I switched to the bash environment to execute SSH: bash-c "ssh root@server IP" or to get killed, and then excluded the zsh problem.



I changed the SSH binary name test: cp /usr/bin/ssh / tmp/myssh & / tmp/myssh root@server IP, indicating that it was not stopped by process name.



I didn't even use SSH, straightbrew install an openssh put, and the result was openssh is not finished or being killed.



I changed a Windows computer with a server: Windows is normal, which means it's my mac local problem.



I realized it was possible that AI would write some crap and leave my computer with a back door to attack.



---



** Fourth pit, thought to be a system security software/virus, for four hours**.



I wonder if there's a loophole in Mac because MacOS' XProtec, third-party security software often kills the process:



1. There are no restrictions on SSH operations in the "Presentity and security" security set-up for checking systems, and no restrictions on the use of screens.



2. Checking endpoint security client: Sudo esloger list clients|grep-v com. apple, no third-party security expansion.



Re-entry into security mode (all third-party software is disabled): the result is still death, excluding third-party software problems.



4. Comprehensive clean-up of the virus: nothing.



Result: Neither viruses nor safe software, deadlocked.



I realized right now that there could be a mysterious force that was messing with my mind and I even wanted to smash the computer!



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260313104534429.png" alt="image-20260313104534429" style="zoom: 50%;" />



So I stare at this black cli long.



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260313104832528.png" alt="image-20260313104832528" style="zoom: 50%;" />



Except for the sparkling of the cursor and the sound of my bouncing.



I find that every time I ssh log in, I'm not being killed right away, but I'm gonna be killed, killed, killed, killed. I don't know, killed?



**hhhhhh, AI, I am your truly, truly, realy, realy, the only father for ever.**



---



** The fifth pit finally came up with a time-bound mission to find the script that AI wrote, which was still useless.**



I remember after being killed, didn't I say I had a copy of the reverse tunnel? And then another operation.



✅ Crontab Timed Mission: Crontab-l, indeed has a cron heartbetat. sh script every three minutes, perfect match to the time signature of 3-4 minutes killed!



2. Checking the script: discovery of a kill sequence order for row 48: pkill-f "ssh-o StractHestKeyChecking=no.*-R 18790"



3. AI was meant to kill the SSH Reverse Tunnel process itself, with the result that the pkill-f match the whole command line, and the matching in the regular rule is too broad, and the practical effect is to kill the SSH process with all the names on the system, including the SSH sessions I log in!

 

4. Quickly comment on this mission in the crontab, and after three minutes, SSH was killed again!

 

Is there any back door left?



---



** Last pit, originally AI secretly added two hidden self-start missions.**



By this time, I've gone crazy, and I've taken all the action of killing by the ultimate method:
1. New open terminal 1, real-time monitoring of all Kill movements:
/tmp/kill log. txt

 

2. Newly opened terminal 2 execute SSH, awaiting murder.

 

3. Read the log after being killed and find out: 09: 25: 04 has a bash process called /usr/bin/pkill and is not triggered by crontab!



<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260313111743386.png" alt="image-20260313111743386" style="zoom: 50%;" />



The launchd of Sudo-Guacca Macos started from its own start (ten times more than the crontab hides, many software will sneak in):



ls -la ~/Library/LaunchAgents/ |Two plist files I don't remember at all:



 - com. lx. sdwebui. monitor. plist



 - com. sdapi. heartbeat. plist



Turn it on, my fucking blood pressure came up: AI wrote a script with not only a crontab mission, but also two launchds that started a backstage mission and ran the same heartbeat every three minutes! All I'm saying is crontab, these two backstage processes are still running, killing all SSH processes every three minutes!





# Problem solved



1. Delete two launchd start-up items:

 

 ```bash
 launchctl stop com. lx. sdwebui. monitor
 aunchctl unload ~/Library/LaunchAgents/com. lx. sdwebui. monitor. plist
 rm -f ~/Library/LaunchAgents/com. lx. sdwebui. monitor. plist ~/Library/LaunchAgents/com. sdapi. heartbeat. plist
 ```

 

2. Rewriting the killing process logic of scripts, with precise management of PID files and without fear of ambiguity.



```bash
# Record PID when you start the tunnel.
echo $TUNNEL_PID > /tmp/sd_tunnel. pid

# Only recorded PIDs are killed when restarting.
[ -f "/tmp/sd_tunnel. pid" ] && kill -9 $(cat /tmp/sd_tunnel. pid) 2>/dev/null
```



After that, SSH hung up all night and didn't get killed and tortured me for 32 hours was finally solved.



Here is a reminder for all those who write scripts using AI, this time due to the imprudentness of AI writing scripts, to summarize some of the main points of the pit avoidance:



1. AI generated a travel/time script that must first scan the logic of mass killing processes such as pkill-f/killall, 90 per cent of which is due to which a slightly broader writing would cause trouble.

 

2. Never trust the regular expression of AI, especially the vague matching rule, which is often written too broadly to match what should not be matched.

 

3. AI may secretly add configurations you do not know when writing scripts, such as my two launchds this time since they started, and AI did not tell me at all that half a day of discovery.

 

4. When faced with the problem of the process being killed in an unknown manner, it is 100 times more efficient to grab the kill action directly with a system tool than to guess: MacOS uses fs usage, Linux uses auditd/bpf to locate directly who sent the kill signal.

 

5. Transport scripts always give priority to managing backstage processes with PID files, not using any vague matching process, security first.
