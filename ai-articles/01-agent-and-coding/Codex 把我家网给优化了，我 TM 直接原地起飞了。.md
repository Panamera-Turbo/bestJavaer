# Codex 把我家烂网给优化后，我 TM 直接原地起飞了。

> 日期：2026-05-24

昨天看到一个非常有意思的事情，有人研究了一下用 Codex 直接把家里网络修复了一下，修复之后的网络直接原地起飞，实测速度堪比光速。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260524111109592.png" alt="image-20260524111109592" style="zoom:50%;" />

这本来没啥可说的。

但后面有意思的是，另外一个网友直接把原贴扔给了 Codex ，随后附上了自己的 prompt 

```prompt
Hey my friend says he improved his internet speed and here is what happened. Can you check if there are any improvements we can make for our internet? My provider says they're sending 1.2k gbps and anything I get is a result of hardware. I'm getting 55mbps right now pls fix make no mistakes.
```

这句话的意思是说。

>我朋友说他的网速提高了，情况是这样的。你能帮我看看我们家的网络有什么可以改进的地方吗？我的网络供应商说他们提供的带宽是 1.2k Gbps，而我实际的网速是硬件问题导致的。我现在只有 55Mbps，请帮我解决这个问题，别出任何差错。

然后放了一下优化前和优化后的实测对比图。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260524070446799.png" alt="image-20260524070446799" style="zoom:50%;" />

这哥们的聪明之处在于，他直接把“别人成功优化的真实案例”当作上下文喂给 Codex，让 Codex 参考那个案例，给自己当前的烂网速做针对性诊断和修复。

也就是说，只要有人从 0 -> 1 真实跑通一个案例，你发出来之后其他人就可以很方便的裂变，变成 1 -> N。

>这里我有个问题，为什么这个人的成功经验不是直接让 LLM 来直接回答呢（手动狗头）

然后 x 上确实有很多人通过这种方式优化了网络性能。

我自己也根据这个 prompt 进行了实操，确实网络直接原地起飞了。一条要求 Codex 针对网速改善的对比的请求，工作了 25s 就完成了。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/503bd396-8462-490f-afd7-5279e99964d8.png" alt="503bd396-8462-490f-afd7-5279e99964d8" style="zoom:50%;" />

然后这是优化之后的直观对比。

![image-20260524070258122](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260524070258122.png)

看起来效果提升的并不是特别明显，但我从用户亲身体验的角度来说，确实达到了直接原地起飞的效果。

要知道，我肉身是在国内。。。。。。

使用这种方式记得有一点，先评估再进行操作，先让 LLM 做好执行备份。否则容易把你的 xx 给直接 kill 掉。

比如这个哥们的操作就直接给我笑麻了。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260524102218162.png" alt="image-20260524102218162" style="zoom: 33%;" />

我自己实测的过程中也出现过 codex 乱杀的情况，但是幸好我这个影响不太大。

---

直接给出大家 prompt 好了，你可以直接去 agent 上（任何 LLM 都可以尝试）进行修复。

```prompt
诊断问题：首先运行了 speedtest-cli。
> 检查了 DNS 解析时间，
> 检查了 MTU、数据包丢失、Wi-Fi 信号/干扰。
> 发现了 3 个问题。
> 删除了过期的网络位置/配置文件。
> 终止或限制了占用带宽的后台进程。
> 优化了 mDNS。
> 运行了前后速度测试和延迟检查。
```

有人使用 `/goal` 命令直接修复，我没有使用 /goal 命令，不过修复的也不错。

希望大家都能体会到网速起飞的酥麻感，简直太爽了。
