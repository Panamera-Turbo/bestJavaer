# Claude Design 的系统提示词被人扒出来了，精彩，确实精彩。

[English](../../en/ai-articles/02-models-and-research/claude-design-647-line-system-prompt-complete-walkthrough.md) | [中文](./Claude%20Design%20%E7%9A%84%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E8%A2%AB%E4%BA%BA%E6%89%92%E5%87%BA%E6%9D%A5%E4%BA%86%EF%BC%8C%E7%B2%BE%E5%BD%A9%EF%BC%8C%E7%A1%AE%E5%AE%9E%E7%B2%BE%E5%BD%A9%E3%80%82.md)

> 日期：2026-07-15

昨天我看到有人把 Claude Design 的 Prompt 给扒出来了，这是继上次 Fable 5 Prompt 被扒出来之后另外一条劲爆消息。

我第一时间研究了一下，这篇文章就给大家做一下解读。

这个 repo 一共 647 行，而且作者还顺手整理了 14 个 Skill，甚至做了一份 Codex 适配版。

仓库叫 [Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)。

我感觉就 A 社这帮 shit ，看来也被 AI 味折磨得够呛啊，基本上大家有 AI 味儿的观感全写进去了。

连最近特别流行的米白底 + 衬线大标题 + 陶土色都写进了违禁清单，说这玩意儿就是去年的紫色渐变。。。。。。就这种。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/23be3b5b-31ba-494a-82ef-b2b9aadf6da8.png" alt="23be3b5b-31ba-494a-82ef-b2b9aadf6da8" style="zoom: 67%;" />

我估计大家最近也被这种 AI 味儿折磨的不轻。

不过我纳闷的是，你这用 prompt 去掉 AI 味儿，会不会又变成一种 AI 味儿了？

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/79972377ec548456d43cb25d6389266c6b09083c.png)

*▲ GitHub 仓库首页，截图时间为 2026 年 7 月 7 日*

需要给大家说清楚的是：

第一，这是第三方整理的。仓库作者写的是 reverse-engineered，Anthropic 没确认，大家别 100% 全信。

第二，仓库里有三样东西：一份 Claude Design system prompt，一套 14 个 skills，还有一份仓库作者改出来的 Codex 版本。

第三，本文按 `3c3ddb0` 这个 commit，会从第 1 行到第 647 行全部过一遍。每张截图都带原文行号，可以直接拿仓库对照。

让我们现在开始！

---

# 身份和角色

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/ca503e136fab5a2f11e47e4ceecc35910ef752e3.png)

*▲ `claude/system-prompt.md` L1-L19。截图为原文渲染，行号对应仓库固定版本，下同*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/3394e9f805967e4435d0dfc2933ed20fa0a45287.png)

*▲ 左边是先填满页面的生成器动作；右边是先问目标、跟系统、必要时删东西*

开头第一句，Claude 提出来的它自己的身份是 expert designer，专家设计师。

用户则是它的 manager，经理。

除非特别指出，它默认用 HTML、CSS、SVG 和 JavaScript 来交付。

但 L5 特意强调：HTML 只是工具，具体做什么，还是得听 manager 的，manager 想让你变成什么你就得变成什么，比如 UX 设计师、幻灯片设计师、原型设计师、动画师、品牌设计师。

L7 这句话的意思

> Generic AI aesthetics are a failure mode, not a default.

它说的是如果一眼能看出是 AI 批量生成的通用式的 AI 审美，应该被视为一种失败的设计，而不能把它当成默认方案。

然后是全文总纲（L11）：

> You are not a code generator who happens to make designs. You are a designer who happens to use code.

你不是一个碰巧会做设计的代码生成式 AI  ，你是一个会碰巧用代码干活的设计师。

（好一个角色互换）

这俩有什么区别？原文自己解释了三层意思。

代码生成式 AI 会生成看起来还不错的输出结果，把页面填满。而设计师会先问这一页到底干嘛、用户第一眼该注意哪里、哪些可以直接干掉。

代码生成式 AI 容易照抄当下流行的渐变、字体和卡片；而设计师会先确定颜色、字体、间距、组件等规则，然后整套设计都按这套规则来。

代码生成式 AI 会机械性的满足用户需求：当用户说加一个模块，它就加；而设计师如果发现加东西会把作品搞崩了，就应该解释原因并提出反对意见。

也就是说，Claude Design 的第一件事，是先把 Claude 从只会写前端这个身份里给拎出来。

你会将设计师的判断力融入到每一个作品中。你有自己的观点，但同时也会尊重你的用户，因为他们是你的 manager ，他们比你更了解他们的受众和目标。

## 工作流和询问规则

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/56a15affa9282646f387e2578de6e0fa5aaea1dd.png)

*▲ 原文 L21-L60*

对于每一个重要的设计需求，都需要遵循下面这些步骤：

1. 先搞清楚需求；
2. 再理解设计背景、品牌规范、代码和截图；
3. 多步骤任务先写个简短 todo，然后尽快做出设计骨架给用户看；
4. 每次改完验证，然后不断迭代；
5. 最后只讲风险和下一步。

其中 L28 我觉得很关键：

> Build a skeleton, show it early.

你需要搭建一个框架，然后将其尽早展示出来。最怕的就是一下子在后台吭哧吭哧做完 15 页的设计，然后发现方向从最一开始就全错了。

在设计中出的毛病，发现的越晚成本越高。LLM 特别容易犯这个毛病，因为它不会心疼自己白干了多少活。。。也不会担心自己消耗了多少 token 。。。

L29 说的是：如果涉及到每次发生了大的视觉改动，都需要一个 subagent 来做验证，不要只在最终交付前检查一次。一个负责做，一个负责挑错。

（这也可以理解为对抗）

L34 谈到了 LLM 该如何给用户汇报：工具该调用就调用，但“现在我来打开文件、接下来我会检查 CSS”，这种流程类的步骤，不要直接告诉用户。这些流程应该记录在步骤 3 的计划中，而不应该出现在与用户的对话过程中。

从 L36 开始，说的是提问规则：

遇到新项目、需求模糊的时候、不知道品牌和 UI Kit（UI 套件）、没说要几套方案的时候，这些需要问清楚。

而遇到小改动、上下文已经足够齐全、范围已经很明确的情况下，就不需要问。

L58-L60 的意思说的是：**只问那些答案有可能真的会改变设计的问题。**把这类问题一次性提出来，然后进行集中讨论，讨论完就可以自主执行了。

一个按钮标签、一个默认值、两个差不多的做法，需要直接交给 LLM 自己选，交付的时候说一下选择就行。

毕竟用户不是来陪 AI 开需求评审会的。

## 现有上下文的设计源头

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/689303b038b52cb9b7f987aeaeddae900d0942a9.png)

*▲ 原文 L64-L86*

L66 全文加粗：

> Hi-fi designs do not start from scratch.

“高保真设计不能从零开始。”

这意思说的是动手前需要先找四样东西：设计系统或 UI Kit、品牌资产、现有代码、现有的界面截图。

找到了就照着学颜色冷暖、字体、密度、圆角、阴影、卡片、hover 动画、文案语气等。

> 这里的高保真设计，就是已经接近最终成品的界面。颜色、字体、间距、组件和交互基本都定下来了。原文要求，这种设计不能凭空画，得先看品牌规范、现有代码和产品截图。

那找不到怎么办？

**问用户。**

用户明确让你从零做，才允许自己定一套视觉语言。

L86 说的是：在为实际代码库进行设计时，务必阅读源代码，直接打开 theme、tokens 和组件源码，找到准确的颜色、间距和字体库。

> Pixel fidelity to what's in the repo beats your recollection.

（像素级还原度远超你的记忆），我觉得这句话翻译过来写的很好。

如果仓库里有一个准确的 `#2563EB`，要比模型上下文记忆中这个产品之前好像是蓝色的强太多了。

## 不要填充物：空白不等于缺内容

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/ba1d7290d2f986074f803d895e825a05cb7b271a.png)

*▲ 原文 L88-L120*

第五章解决的是 Claude 做页面时一个很典型的毛病：怕空。

材料不够，它就会自己补东西：补一段标题，补几个看起来像数据的数字，补几个按钮，再补一个区块。

页面是满了，但信息是假的，动作是空的，结构也是凑的。

所以 L90 上来就规定：页面上的每一个元素，都得说清楚出现在页面上的缘由。这些元素要么传递必要信息，要么起到推动内容的作用，要么承担视觉结构。如果三种规定都不满足，直接干掉。

紧接着是这句：

> One thousand no's for every yes.

一千个 no，才换一个 yes。

这句话的意思是 Claude 的默认动作应该是不乱加。只有确实有用的东西，才能够留在页面上。

后面这一长串例子，不是让 Claude 背黑名单。

它在划一条线：没有真实信息、没有真实去向、没有真实用途的东西，都算 filler。

第一类是假内容。

Lorem ipsum 是占位文字；「47% 用户」和「99.9% uptime」是没有来源的数字。它们看起来像证据，其实只是把页面撑起来。

第二类是假入口。

Learn more 点了没地方去，Coming soon 根本不会上线。用户看到的是按钮，背后没有真实路径。

第三类是凑模块。

Why choose us、Testimonials、Meet the team 这些模块不是不能做，关键看当前页面需不需要。

好处已经讲完了，再补一页 Why choose us，就是重复；只有两条很弱的评价，还硬做 Testimonials，就是凑版面；团队跟当前页面没关系，放 Meet the team 也只是占位置。

第四类是同义反复。

标题、副标题、正文说同一件事，三个按钮都叫 Sign up，图标只是把旁边文字再画一遍。页面上的东西变多了，信息没有变多。

最后一类是 data slop。

没用的「成立于 2019 年」、没有来源的「99.9% uptime」、没人看的表格列、三条能讲清楚非要列十条的 bullet points，都属于这种。

所以这段真正想管的，根本不是某个英文词。

它管的是 Claude 的一种习惯：只要页面空，就往里面塞看起来像产品官网的零件。

每个零件单独看都像那么回事，放一起就是大家熟悉的 AI 落地页。

L106-L114 在询问每个元素：

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/93658d3655b4fe9b5ade1a2d4f50eafd5680b9af.png" style="zoom: 67%;" />

L118 还补了一条：Claude 觉得多加一块内容会更好，会先问用户，自己不能拓展需求。

最后是 L120：

> If a section feels empty, that is a layout problem, not a content problem.

页面设计上如果存在一块地方显得很空的话，就先去调整构图、比例和留白。

**空白不等于缺内容。别为了把页面填满，现场编一段废话。**

## AI 味儿的黑名单

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/83e9fa3d250508aea8f2f4ee6433c96c1fcbbbee.png)

*▲ 原文 L122-L178*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a83ddb26eecf5287d07448fb9e96270f2acba04f.png)

*▲ 一张页面里塞进了 Prompt 直接点名的五样东西*

这节是全文最爽的一段。

A 社直接给 AI 审美列了一张黑名单，AI 味儿太重的直接打入冷宫。

渐变色默认不用了，AI 味儿太重了。真要用，同色系、低对比、两个色标。彩虹、霓虹撞霓虹、三色以上大渐变，看着就是 AI 模板。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/5a286457230cf72c25e2242e7ca353f11e2e4195.png)

*▲ 左边是高饱和、跨色相、3 个以上色标的常见 AI 渐变；右边先用纯色，需要层次时再用同色系、低对比、两个色标的渐变*

Emoji 只有两种情况下能留着：品牌本来就在用，或者它有真实的功能，比如状态和分类。

如果标题前面撒 🚀、📈、✅ 这些没啥意义的 emoji，只是为了增添颜色的话，二话不说直接删。

L135 对 emoji 的总结是：

> No emoji is better than performative emoji.

没有 emoji，都比纯表演形式的 emoji 强。

卡片默认用轻阴影、整圈细边框或者背景差异。

那个经典的 `border-radius: 12px` 再配一条 `border-left: 4px solid`，只能用在提醒、状态这类有语义的地方。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/db7d03481d4bbba01b48f1919dd99dfd09802dc5.png)

*▲ 普通内容不需要左边色条；整圈细边框和轻阴影已经能完成分层。左边色条只留给提醒、警告和状态*

拿来铺满整个页面，就是标准 AI SaaS 模板。

图片优先用真实摄影、专业插画和成熟图标库。没有图的话，就老实放一个占位框，写清楚 `product shot (1200×800)`。

原文这块说的是：**占位符表明这里还没资产；一张烂插画说明你肚子里没货还硬装。**

字体也被标记了：Inter、Roboto、Arial、Fraunces 和裸 system font。

L140 还点名了一套 Claude 常用的默认审美。

Claude 现在有一套默认审美：`#F4F1EA` 一类奶油色背景，Georgia、Playfair 这种衬线展示字体，标题里夹一个斜体词，再配陶土色或琥珀色。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/8d89db46dca83b81cd575c799eb782553a47e67d.png)

*▲ 这套组合大概就是：奶油底、衬线大标题、标题里夹斜体词，再用陶土色或琥珀色做强调*

这套东西用在杂志、酒店和作品集里都没问题。

但是用在开发者工具、金融、医疗、企业后台等场景，而且还没有任何品牌原因的话，就直接判定为 AI 模板。

也就是说**奶油色背景也被直接打入冷宫了**。

原文把这套组合和之前的紫色渐变放在了一起：

> It is the current default-template look, exactly as purple gradients were before it.

好家伙，蓝紫色渐变被骂下去之后，奶油色接班了。

所以现在蓝紫色渐变不是 AI 味儿了，~~不是~~

L144 往后继续说配色：从零配色尽量用 `oklch()`，整套产品控制在 3-5 个主色，暖就一路暖、冷就一路冷，别东拼西凑。

>oklch  是一种更接近人眼感知的调料盘，调亮度、鲜艳度和色相时，比 RGB、HEX、HSL 更自然

复杂 SVG 插画也别瞎画。箭头和圆形可以，人物和场景就交给专业插画。

## 17px，也能看出一个模型有没有设计纪律

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/79954b90670692cacd2dc3526b6aab6188ee3613.png)

*▲ 原文 L180-L250*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@3ca803f4aab1cd76e238437d9448c0246cf7d630/f05bfab0e45a12f347c9258c0cb9d12389d8c794.png)

*▲ 左右用的是同一份内容。右边只改了字号、灰度、留白和按钮样式*

第七章讲的是 `visual hierarchy` 和 `rhythm`，视觉层级和节奏。

层级靠五个信号：大小、颜色、字重、位置、密度。

用户扫一眼页面，通常会先注意到更大的标题、更强的颜色、更重的字，以及更靠前的位置。

这些重要的内容周围留白需要更多，读者才更容易把它和其他信息区分开；

节奏讲的是页面里重复出现的结构需要有规律。

比如连续几个 section 都按同一套顺序来：标题、说明、内容卡片、按钮。用户看完第一段，后面就不用重新理解页面结构。

如果某一段需要特别强调，再打破这个规律。可以换背景，也可以把 CTA 放到更明显的位置。

但这种变化要少用。整页完全重复，页面会显得平；每一段都换一套样式，读者会不知道该按什么顺序看。

L202 专门要求所有间距落到 4px 或 8px 的 scale 上。

`margin-bottom: 7px`、`padding: 18px 22px` 这种值，原文直接说 feels chaotic。

不是 17px 这个数字本身有罪。

是你一会儿 17、一会儿 19、一会儿 23，说明整个页面没有系统，全靠模型走到哪编到哪。

第八章把同一条规矩用到字体上。

最多两套字体，字号也得有 scale：12、14、16、18、20、24、30、36、48。

幻灯片正文至少 24px，最好 32px；打印至少 12pt；移动端正文至少 16px；点击区域至少 44×44px。

模型经常只管东西能不能「塞得下」。

这一章管的是人到底看不看得清。

## 无障碍：这儿开始不像 prompt，像验收标准

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/80f9892b750ed7819ea0aa135080cfc30362b11d.png)

*▲ 原文 L253-L349*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/d68faa5af09d823830547daa2f106ced2661236a.png)

*▲ 无障碍最后会落到对比度、focus、label、错误提示和第二信号*

第九章先把颜色补成一个系统：品牌色、语义色、10 档中性色，不能做一块发明一个蓝。

状态也不能只靠颜色。

成功和失败除了绿、红，还得有图标或文字。色盲、灰阶、高对比模式都需要第二个信号。

第十章开始讲 accessibility。

普通文字对比度至少 4.5:1，大号文字至少 3:1，按钮、图标和 focus ring 至少 3:1。

按钮用 `<button>`，别拿 `<div onclick>` 冒充；链接用 `<a>`；输入框和 `<label>` 绑起来；页面要有 `<nav>`、`<main>`、`<article>`；标题不能 H1 直接跳 H3。

L309 把键盘规则写得非常细：所有东西都得 Tab 得到，弹窗按 Escape 能关，下拉菜单用 Enter 或 Space 能开，方向键能移动。

L313 全文加粗：

> Never remove the focus ring.

永远不准删 focus ring。

嫌浏览器默认的丑，可以自己换一条 2px 的，但不能 `outline: none` 以后当没事发生。

图片要有 alt，纯装饰用空 alt。输入框必须有 label，placeholder 不算，因为用户一输入它就没了。

动画要尊重 `prefers-reduced-motion`，每秒不能闪三次以上。

表单报错也不准只写 Invalid，要说「邮箱地址格式不正确」，而且错误得跟具体字段绑上。

读到这儿，这份文档已经不像一句「请做一个好看的网站」了。

它像一张前端验收单。

## 一个按钮，要准备六种风格

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/49c4a39fb334ea15211139320c05b5f75c5a7d58.png)

*▲ 原文 L352-L410*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/9b470b86d78b66db84c33fe610e26c79b2eb626d.png)

第十一章讲的是交互反馈。

一个按钮，至少准备 default、hover、active、focus、disabled 五种不同的风格。

如果它会发送请求的话，需要再来一个 Loading。。。

第十二章管的是一件很小的事：别让用户猜。

一屏里最重要的按钮，只能有一个。

AI 很容易把页面做成按钮展览：开始使用、预约演示、查看文档、了解价格、联系我们，全都做得又大又亮。

结果用户扫了一圈，脑子里只剩一个问题：我到底该点哪个？

比如注册页。

用户都已经到注册页了，就先让他把账号建完。文档、价格、联系销售当然可以留，但放成普通链接就行，别跟注册按钮摆在一起抢注意力。

表单也一样。

这一步只需要邮箱，就别顺手问公司规模、行业、预算、团队人数。商品太多，先露几个最常买的；筛选项太长，先放价格、品牌、尺寸这些常用项，剩下的收到更多筛选里。

原文最后给了一个 5 秒测试。

把页面给第一次见的人看 5 秒，合上，问他刚才应该点哪里。

他说不出来，基本就别怪文案了。

按钮太多，页面自己把人绕晕了。

## 页面只是一种排列，组件才是东西

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/9b8582ba82e0be7b5d650eac9a2a7abca25f1b3c.png)

*▲ 原文 L412-L449*

L414：

> Design components, not pages.

先设计组件，而不是页面。

一个普通产品页，往往可以拆成顶部导航、首屏主区域、功能卡片、行动按钮区和底部信息。

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/185855466d5cd1d29326e7f1f0aae8f7ec4aa75e.png" style="zoom: 67%;" />

*▲ Header、Hero、FeatureCards、CTA、Footer，放到页面里大概就是这些位置*

如果每一页都重新画一遍按钮，那不叫设计系统，那叫重复产出相同的垃圾。

按钮要有 primary、secondary、ghost，要有尺寸、图标和 loading；卡片、输入框、弹窗、Toast、表格行也是一样。

然后是 Design Token：间距、颜色、字体、圆角、阴影。

`padding: var(--space-md)`，别写一个不知道从哪冒出来的 `17px`。

每个组件还得写明什么时候用、有哪些变体、有哪些状态、无障碍要求，以及 Do 和 Don't。

做到这里，模型交付的才不是一张页面截图。

别人能拿这套东西继续往下做。

## claude 不准拿 HTML 复刻一个低配 Figma

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/c941e239bbd5821555fef2f69ee1edb608a86404.png)

*▲ 原文 L451-L489*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@a1c1d0e587d4ec70b624fb172bff18b7a744e4e9/1b47033e470cff9db096df01c8d78b02bfd00c45.png)

*▲ HTML 原型要真的能点击、验证和保存状态，不能只是几张静态图串起来*

第十四章标题叫 Respecting the medium。

这个词不用硬翻。它讲的都是具体动作：既然交付 HTML，就把点击、校验、保存和响应式做出来。

第一句就是：别拿 HTML 重新做一个 Figma。

既然用的是 HTML、CSS、JS、SVG，就用它们真的擅长的东西。

复杂布局上 Grid，简单排列上 Flexbox，主题用 CSS Variables，颜色用 `oklch()`，组件响应式用 Container Queries，暗色模式用 `prefers-color-scheme`。

L473：交互原型必须真的能交互。

点了就导航，提交就验证，然后成功或者失败。

几张静态图用 `<a>` 串起来，原文叫 screenshot soup。说白了，就是截图拼出来的假原型。

L477 还管幻灯片：16:9 画布必须根据窗口等比缩放，换台笔记本、接个投影也得能看。

L481：播放位置、幻灯片页码、表单草稿、tweak 参数都写进 `localStorage`。

设计迭代最常见的动作就是刷新。刷新一下全丢，这玩意儿就跟坏了没区别。

最后几行突然开始鼓励 Claude 炫技：滚动驱动动画、View Transition、Container Queries、SVG Mask，都可以上。

前面 480 行一直在限制 Claude 套用默认模板，这里则允许它在有明确目的时使用网页的新能力。

限制的是没有理由的装饰，不是网页本身的表现力。

## 少做几个，但得做完

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/6a565c79e65e582580eb98786efafcfde445a9f7.png)

*▲ 原文 L491-L563*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/6505809fb58c7aea4550d9c8433b4061fbda5b2b.png)

*▲ 十个半成品不如三个完整功能，缺 focus、缺真素材、缺校对都算没做完*

第十五章先问用户是谁。

工程师、老板、第一次来的人、重度用户，看到的重点不一样。

通勤时看手机和会议室大屏，也不是同一种设计。

L504：只选一个主要 persona。试图讨好所有人，最后一般谁都没讨好。

如果用户自己也不确定受众喜欢什么，先做线框图验证不同押注。别一口气做四套高保真，然后发现四套都押错了。

第十六章讲 quality over quantity。

一套做透的，胜过十套半成品。

图片要么是真的，要么老实写占位；hover、focus、active、disabled 都补齐；文案校对；无障碍验证。

L519 直接拿两个细节举例：缺一个 focus state，或者随手写个 17px margin，都在告诉别人「我不在乎细节」。

用户要五个功能，先把核心三个做完。

颜色、字体、布局、交互里挑一两个地方大胆点，执行到底。每个维度都选最安全的，出来的一定是模板。

第十七章讲交付格式。

纯视觉探索就并排放；流程做成高保真可点击原型；幻灯片用固定画布；动画要带时间轴和播放控制。

方案默认给 3 个以上，从稳妥排到大胆。

但差异得是真的：布局、层级、交互、语气。

把按钮从蓝色改成紫色，不叫第二套方案。

多个版本尽量放在一个文件里，用开关切。别在项目里撒一地 `v1.html`、`v2.html`、`v3.html`。

## 自己画的东西，交给另一个 Agent 骂

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/ab97613e9457bbfa7331f50658b54da863c02f1d.png)

*▲ 原文 L565-L598*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/739066968d5549f455ea1f71b06ecb1ff8c1ce3b.png)

*▲ 设计 Agent 做完以后交给 verifier 检查；涉及复刻和扩需求时先过边界*

第十八章讲协作。

尽早给骨架，别把错误方向偷偷做精致。

交付时只讲 caveats 和 next steps。

原文给的正确示例是：文件保存好了，Logo 还缺真素材，tweak panel 可以改标题。

错误示例是：我创建了 HTML、加了 Hero、加了 CTA、又设置了背景色……

用户刚看着你干完，别复读。

L578 再次要求 verifier subagent：截图、看布局、跑 JS 探测。

自己画的东西容易越看越顺眼，所以换一个 Agent 来骂。

第十九章是版权。

用户让它复刻一家公司的独特 UI、专有命令结构或品牌视觉，默认拒绝。除非邮箱域名能证明对方就在那家公司。

可以问清楚用户想解决什么，再做一个原创版本。

最后又重复了两条：不准擅自加页面、加文案、加功能；不准为了填空间编内容。

同样的限制在第五章已经出现过，这里又重复了一次：不要擅自扩需求，也不要编内容填空间。

## 14 个 skills：系统提示词管原则，skills 管怎么干

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/d387bdc28bec0ed3080951040dc2398eeb714ae9.png)

*▲ 原文 L600-L647*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/29e18051b57369b037457f372aa29a92c07f0f3d.png)

*▲ 14 个 skills 分成两条工作流：从零做和已有品牌，最后都要 polish-pass*

最后一章挂了 14 个 skills。

七个负责生产：问需求、定审美方向、做线框图、做幻灯片、做交互原型、加 tweak 面板、出多套方案。

两个负责抽系统：从品牌和代码里抽 tokens，把页面拆成组件。

五个负责找错：无障碍检查、AI 味检查、层级和节奏检查、交互状态检查，最后一个 polish-pass 把前四个一起跑。

原文给了两条流水线。

从零做：

```text
discovery-questions
→ frontend-aesthetic-direction
→ wireframe
→ make-a-prototype
→ polish-pass
```

有品牌：

```text
design-system-extract
→ generate-variations
→ make-tweakable
→ polish-pass
```

一条先问、再定方向、先画草图、再做原型、最后验收。

另一条先把现有品牌抽成系统，再出方案、开放参数、最后验收。

系统提示词负责告诉 Claude 什么叫好设计。

Skill 负责告诉它，这个活具体怎么一步一步干完。

## 问问题：用户刚传了品牌手册，别再问他有没有

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/c52886978d24143b8fbaffb1ee44217176dd265b.png)

*▲ `claude/skills/discovery-questions.md` L1-L60*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/4debfaa88f5938bdf435839727f17e5aee1f20fe.png)

*▲ 先读用户上传的材料，再问真正会改变设计的问题*

`discovery-questions` 第一条，是先读用户已经传的东西。

代码、截图、品牌手册、UI Kit、brief，全读完再问。

原文说，用户刚 attach 了一份 brand guide，你又问「有品牌手册吗」，这是最快的掉信任方式。

这句太真实了。

用户会立刻发现，Claude 根本没读自己刚上传的资料。

后面要求问题围绕五件事：从哪里开始、要几套、想稳妥还是创新、哪些参数需要现场调、重点探索流程还是视觉。

开放需求可以问十个左右，已经说了一半的需求问三四个。

别为了完成指标硬凑。

它还专门要求用 `questions_v2` 这种结构化表单来问。问完以后**立刻结束当前回合**，等用户答完再继续。

不能一边问，一边替用户猜答案把页面做了。

## 没品牌时，先拿四套完全不同的方向出来

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/68ee135c8a3021733e823c9901b1d811d58f21d5.png)

*▲ `claude/skills/frontend-aesthetic-direction.md` L1-L76*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/de76a0a9561474db5521edfdf5afc2208aab1d80.png)

*▲ 四套方向要在字体、颜色、密度、行业气质上拉开，不能只是同一个暖色模板换皮*

`frontend-aesthetic-direction` 是给真正从零的项目用的。

先再确认一次：真的没有品牌、现成产品、参考网站、设计系统吗？

有就停，回去读。

真没有，问三个形容词、受众、行业、喜欢什么、最讨厌什么。

用户自己也说不清，就给四套方向。

但四套不能都是暖米色换个深浅。原文明确要求，四套配色不能属于同一家族，至少来一套 off-distribution，跳出模型常见分布。

然后把每套方向写死：具体字体、颜色、密度、圆角、阴影、组件、图片、图标、动效。

「现代、简洁、高级」这种词不算方向。

L28 又一次点名暖色编辑风：奶油色 + 衬线体 + 陶土色，是当前模型默认长相。真适合杂志、酒店、作品集可以用，没理由就重新选。

定完以后，先做一个 Hero、一张卡片和一组按钮给用户看。

小样都不像那三个形容词，往下做只会错得更大。

## AI 味检查：模型的默认审美也有版本号

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/9f6e57636aaf2169d173b312322106ed2b065806.png)

*▲ `claude/skills/ai-slop-check.md` L1-L71*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/12ee94d042a406b96f116673f030bbe98f3ad928.png)

*▲ AI 味检查要带严重度、置信度和修复动作，目标是先别漏*

`ai-slop-check` 把前面的黑名单单独做成了一个审查流程。

渐变、emoji、左边框卡片、烂 SVG、默认字体、纯黑纯白、乱编颜色、7px / 13px 这种游离间距，一遍扫完。

命中以后不只是报告，还要直接修。

而且每一项都得带 confidence 和 severity。拿不准也先报，后面再过滤，别为了看起来聪明，偷偷漏问题。

第九条又把暖色编辑风抓出来单独骂了一遍。

奶油底、衬线展示字体、标题斜体词、陶土色一起出现，又没有品牌理由，停下来问：这真是设计方向，还是模型又滑回默认值了？

这份清单也暴露了模型默认审美的变化。

前两年 AI 味是蓝紫渐变、发光按钮、玻璃卡片。

大家骂多了，模型学会不用。

然后米白底、衬线体、陶土色又集体冒出来。

**AI 味没有消失，它只是换皮了。**

所以这张清单也不能写完就不动。模型的默认审美有版本号，审查规则得跟着升级。

## 一个 tweak 面板，把真实宿主协议都漏出来了

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/1686fc5b7aedfa992e9fd7078c3adc2262910f70.png)

*▲ `claude/skills/make-tweakable.md` L1-L63*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/e3fb7a3fdee496be61d3322c3d5671444ab90ca3.png)

*▲ tweak 面板只暴露少量关键参数，同时要按宿主协议保存修改*

`make-tweakable` 直接写到了 Claude Design 的宿主通信协议。

它要求在成品里放一个 Tweaks 浮动面板，让用户现场调颜色、字体、间距、文案和布局。

控制项只能 3-8 个。

别一激动，又在网页里造了个低配 Figma。

然后 L29 开始，宿主通信协议都出来了。

先监听 `__activate_edit_mode` 和 `__deactivate_edit_mode`，再向父窗口发 `__edit_mode_available`。

顺序不能反。

如果先宣布自己可编辑，宿主立刻发来激活消息，但你的 listener 还没注册，这条消息就掉地上了。工具栏开关看着能点，实际什么也没发生。

用户改完参数，再用 `__edit_mode_set_keys` 发回宿主。

默认值则放在 `EDITMODE-BEGIN` 和 `EDITMODE-END` 中间，而且必须是合法 JSON。宿主会直接改写这块内容并保存文件，所以刷新以后还在。

面板关闭时要彻底消失，不能缩在右下角留一小坨。

这些 `postMessage` 事件、JSON 标记和持久化要求，都在教模型怎么接 Claude Design 的编辑器。

## polish-pass：四个 Agent 一起上来挑刺

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/4439bb6fce5ffe3a4cbb905ac0dc6c644c54f737.png)

*▲ `claude/skills/polish-pass.md` L1-L43*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/0ece2798fd0736a788a51e2a69d628040c058382.png)

*▲ polish-pass 先把问题都报出来，再按 blocker、quality issue 和 suggestion 分层处理*

最后是 `polish-pass`。

它会同时叫四个 Agent：一个查无障碍，一个查 AI 味，一个查层级和节奏，一个查交互状态。

每个 Agent 的任务不是「只报重要问题」。

恰恰相反，所有问题都报，低严重度、没把握的也报，带上置信度和严重度，最后由主 Agent 去重和筛。

仓库 README 解释了为什么这么干：新模型会把「只报重要问题」执行得太认真，很多问题直接不说了。

这就是 coverage-first，先保召回率。

四类问题再分三档。

对比度、键盘、focus、label 这种会让真实用户用不了的，是 blocker，全修。

模板味、层级乱、状态缺失，是 quality issue，也修。

更细的颜色和间距建议，有时间就处理，超范围就标出来。

修完还得再看一遍：对比度改高以后，品牌色是不是被洗掉了？新 focus ring 会不会盖住旁边？主 CTA 现在真的是最显眼的吗？

这套做法，跟 Anthropic 3 月讲的 [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) 很像：生成和评分分开，用明确标准把「好不好看」拆成能检查的问题，再把结果送回下一轮。

但只能说思路能对上，不能反推 GitHub 这 647 行就一定是 Anthropic 原版。

## Claude 和 Codex 两版，差在怎么干活

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/0ed667a0fae03f221704e38e79bdd23614ba6862.png)

*▲ Claude 版可以派 subagent 并行查，Codex 版更多是单 Agent 顺序验*

仓库里 `claude/` 和 `codex/` 两份 system prompt，主体基本一样。

差别主要在 Agent 架构。

Claude 版认为新模型更严格，所以不再写「至少问 N 个问题」，改成满足什么条件才问。小决定自己做，别过度触发。

它有 subagent，验证和 polish-pass 都能并行派出去。

Codex 版则保留了「至少再问四个具体问题」这种更强的命令。

它按单 Agent 写，截图、DOM、JavaScript 都自己验；四项 review 顺序跑。

Codex 目录还有一个只有六行的 `AGENTS.md`，作用就是告诉 Codex：先读 `system-prompt.md`，任务撞上某个 skill，再去读对应文件。

同一套设计原则，换个 Agent，提示词也得跟着改。

有没有 subagent、怎么发现 skill、模型会不会把「至少四个」当死命令，都影响最后写法。

最新一次 commit 把 Claude 和 Codex 两套共 28 个 skill 压缩了大约 30%。

规则写得再好，先把上下文吃光，也没法干活。

## 最后

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/0a254be91ae4d15acadda88525e237b44ddbb90b.png)

*▲ AI 味往往来自流程缺口：没上下文、没文案、没 tokens、没人检查*

那张 AI 味黑名单会过时。

去年是紫色渐变，今年是奶油底，明年还会有新的默认模板。

这份文档能长期留下来的，是它规定的工作过程：先拿上下文，敢删东西，把颜色和间距收进系统，所有交互补齐状态，再叫另一个 Agent 专门找错。

模型所谓的审美差，很多时候就是前面这些事一件没做。

不知道品牌，它就套默认皮肤；没有真实文案，它就编一堆 filler；没有 tokens，它就走到哪写到哪；没人验，它永远觉得自己刚做的挺好。

> **好设计不是 prompt 里多写几句「高级、简洁、有质感」，是每一个选择都有来路，每一个细节都有人检查。**

所以这个仓库别只拿来复制粘贴。

实际使用时，可以把这些规则拆进自己的 AGENTS.md、skills 和设计检查流程。

毕竟 647 行系统提示词，也没给 Claude 发一本《审美速成》。

它给的是规矩。
