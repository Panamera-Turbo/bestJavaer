# 瑞幸出 CLI 了，这会是迈向 AGI 的第一步吗？

> 日期：2026-06-10


昨天晚上刷到一个东西，瑞幸开放了 CLI，我第一反应是：这年头点杯咖啡也要进终端了？

瑞幸出了 AI 开放平台，里面有 MCP、CLI、Skill。

作为一个咖啡爱好者，同时也是一个没事就喜欢折腾 Agent 的人，这种东西不试一下，多少有点对不起自己。

![image-20260609195425082](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260609195425082.png)

我马上安装了一下。

流程倒是不复杂，CLI 会提示你先登录。

然后我登录了一下，结果？？？？？？

![image-20260609195951420](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260609195951420.png)

我还没开始点咖啡，先被排队的人教育了一下。

然后，我换了个手机号，就又行了？？？？

![image-20260609200431091](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260609200431091.png)

这什么蜜汁操作。

我换了个号，就不限购了？

还是瑞幸官方，把我手机号给我拉黑了？？

## Token 到手

登录之后，核心动作就变成了拿 token。

这个 token 很关键。官方页面里也写得很直接：这个 Token 在 MCP 与 CLI 共用，并且跟瑞幸账号会话绑定，严禁泄露或分享。

所以这里别搞错。

这不是一个随便贴在群里的 demo key。

它背后是你的瑞幸账号，是可以查门店、搜商品、预览订单、创建订单的真实权限。

我把 token 加到配置文件里，让 Coding Agent 给我创建一个订单。

然后就，上号！！

![image-20260609224050342](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260609224050342.png)

## 真能下单

后面就比较丝滑了。

Agent 拿着 token，先查门店，再查商品，再预览订单，最后创建订单。

你看着像是在聊天，其实背后已经不是聊天了。

它是在调接口。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610093245837.png" alt="image-20260610093245837" style="zoom:50%;" />

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610111822394.png" alt="image-20260610111822394" style="zoom:50%;" />

最后咖啡也确实出来了。

这事儿有点好笑。

以前是我打开手机 App，选门店，选商品，选冰热甜度，再确认订单。

现在变成我在电脑上跟 Agent 说一句，它自己去找店、找商品、组订单，然后把关键确认节点甩给我。

不过目前还是 V0.0.1 版本，相当于就是个裸机版本，很多 bug 。

比如它接入 xiaomi 模型的时候，竟然出现了问 `luckin 0.0.1` 和 MiMo 的流式 tool calling 兼容性。

![image-20260610112033778](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610112033778.png)

于是我还得让 Codex 给我修复下，因为确实没时间等官方的修复步骤了。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610112128370.png" alt="image-20260610112128370" style="zoom:50%;" />

---

## 官方到底开放了什么

别忘了我是一个技术号，所以不能只说“哇，AI 帮我点咖啡了”。

我去看了一下瑞幸官方文档：https://open.lkcoffee.com/docs

官方站点里写得很清楚，瑞幸这次不是只做了一个 CLI 页面，它同时给了 MCP Server、CLI 和 Skill 三条线。

![image-20260610111114670](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610111114670.png)

其中 MCP 文档里列出来的工具也比较完整，至少包括：

1. `queryShopList`：查询门店列表。
2. `searchProductForMcp`：根据用户 query 匹配商品。
3. `queryProductDetailInfo`：查商品详情。
4. `previewOrder`：订单预览。
5. `createOrder`：创建订单。
6. `queryOrderDetailInfo`：查询订单详情。
7. `cancelOrder`：取消订单。

![image-20260610111227885](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610111227885.png)

说白了，瑞幸把原来藏在 App 里的点单流程，拿出来了一部分，变成了 Agent 可以调用的工具。

---

你可能会说，点杯咖啡至于这么麻烦吗？

确实不至于。

我自己打开 App 点一杯生椰拿铁，也就几十秒。

但是这件事真正有意思的地方，不在点这一杯咖啡。

它说明一个变化：**很多原来只能在手机 App 里完成的动作，正在被拆成 API、MCP 和 Skill 这类工具能力。**

以前我们说手机是入口，因为所有服务都在 App 里。

打车在 App 里。

点咖啡在 App 里。

点外卖在 App 里。

买票、订酒店、查订单，也都在 App 里。

但是 Agent 出来之后，入口这件事开始变得有点微妙。

人不一定非要进 App。

人可以说一句话，Agent 去调工具，工具再去调用服务。

最后你只在关键地方确认一下，比如支付、取消、改地址、换门店。

这时候手机还重要，但它更像一个确认器、支付器、通知器。

我这次的感受就挺明显。

下单是在 Mac 上跑的。

token 在配置里。

Agent 在终端里干活。

至于我的手机？我的手机没用了，以后就是一个**电子遥控器了**。

---

虽然瑞幸自古以来很能整活，但我觉得还不够，瑞幸可以区分一下渠道，如果是 CLI 点餐的渠道，可以给一个独立的赛博朋克的包装，就像这一样。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/026eabaa574d2388e5b5a7ac138dbfe9.png" alt="026eabaa574d2388e5b5a7ac138dbfe9" style="zoom:50%;" />

甚至瑞幸可以这么干，和国内大模型厂商联动一下，买咖啡，送 token，这样一来，销量会再翻三番，不信你试试看。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260610124738607.png" alt="image-20260610124738607" style="zoom:50%;" />

这篇文章就到这里，我们下期再见。
