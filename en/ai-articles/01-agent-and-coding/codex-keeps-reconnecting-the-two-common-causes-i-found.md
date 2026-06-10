# Codex Keeps Reconnecting? The Two Common Causes I Found

[English](./codex-keeps-reconnecting-the-two-common-causes-i-found.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Codex%20%E4%B8%80%E7%9B%B4%20Reconnecting%EF%BC%9F%E6%88%91%E6%9C%80%E5%90%8E%E5%8F%91%E7%8E%B0%EF%BC%8C%E5%B8%B8%E8%A7%81%E5%B0%B1%E4%B8%A4%E4%B8%AA%E5%9D%91.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-06-05


I'm sure you're all familiar with this scene when you're using Codex.

When you're going to get Codex to work.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260602220945257.png" alt="image-20260602220945257" style="zoom:50%;" />

When you want Codex to give effective guidance.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260602220945257.png" alt="image-20260602220945257" style="zoom:50%;" />

When you want to run a mission with Codex.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260602220945257.png" alt="image-20260602220945257" style="zoom:50%;" />

What the hell is this?

Take it easy, this Reconnecting, there's a story.

---

In general, the emergence of this Reconnecting is in two ways:

Codex did not leave the agency.
2. Accessed to server but rejected by server

First of all, we should all understand this. After all, you're using Codex. You'll understand what's going on.

But this doesn't fit, and it's directly reflected in the log as **WebSocket handshake timed out.**

Why? Because Codex Desktop is a desktop application that does not automatically eat system agents like a browser. When it starts, it needs to read the environment variable.`HTTP_PROXY`, `HTTPS_PROXY`That's why I left. If these variables are not set, it thinks that it can reach straight, and the result is half a day without a response, it's going into a reconnective cycle.

This situation is handled directly.`~/.codex/.env`.

For example, Mac, if you use a Clash or similar tool, the common HTTP/SOCKS5 hybrid port is`7890`But the actual ports may be different for everyone, so it would be better to check before we do it. You can just look at the proxy setup or run at the terminal|Look what she's using.

You can use the Prompt directly below me, and you can add it directly to Codex, if you can't get it, with the other Agents.

```prompt
Help me fix Codex Desktop's been reconnecting problem.

Please locate the proxy port and proxy protocol that I am using and then create or update ~/.codex/.env to write the following proxy configuration. Do not write to die 7890, replace it with the actual port; if the file already exists, keep other configurations.

HTTP_PROXY="http://127.0.0.1: <HTTP or mixed port>"
HTTPS_PROXY="http://127.0.0.1: <HTTP or mixed port>"
ALL_PROXY="socks5h://127.0.0.1: <SOCKS5 or mixed port>"
NO_PROXY="localhost,127.0.0.1,::1"

Checks if the configuration is correct after writing and tells me how to restart Codex Desktop.
```

If you want to rub your hand, open it with an editor.`~/.codex/.env`, writes:

> HTTP_PROXY="http://127.0.0.1:<port, usually 7890>"
> HTTPS_PROXY="http://127.0.0.1:<port, usually 7890>"
> ALL_PROXY="socks5h://127.0.0.1:<port, usually 7890>"
> NO_PROXY="localhost,127.0.0.1,::1"

Here, the first situation is basically settled.

---

The second scenario is more subtle, and I myself have encountered it.

The request reached the server, but the server refused.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260602223806959.png" alt="image-20260602223806959" style="zoom:50%;" />

Why not? If you use the ChatGPT account, which opens the Multifactor Authentication (MFA), Codex does not follow the full MFA process at the time of the initial authentication, the server will determine the subsequent connection as unauthorized and will be disconnected.

This is not Codex's Bug, but OpenAI's security strategy works: after the MFA has been activated, some old Ssession or a connection without secondary authentication information will be forcibly disabled. Codex Desktop's login status may have been kicked for lack of MFA verification, but it would not have re-emerged the authentication hint like the web page, so it was stuck in this dead cycle.

This is how it's done.

> Start ChatGPT MFA, then press Cmd + Q to exit Codex completely and reopen again.

The steps are as follows:

1. Open ChatGPThttps://chatgpt.com/.
2. Enter Settings → Security.
3. Enables a authentication method under Multi-factor accreditation, such as a certifier App or Passkey.
4. Quit Codex Desktop: press Cmd+Q.

Don't doubt it. That's what the official said.

![image-20260602224416532](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260602224416532.png)

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260602231638652.png" alt="image-20260602231638652" style="zoom:50%;" />

I set up the MFA, and then I pulled Codex out of the restart and it was done.

The Reconnecting hint never appeared again.

Quick, very silky.
