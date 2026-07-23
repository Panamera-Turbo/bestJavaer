# 好家伙，继 Fable 5 系统提示词被扒之后，又一个 Claude 系统提示词被扒了。

[English](../../en/ai-articles/02-models-and-research/claude-design-system-prompt-essential-lessons.md) | [中文](./%E5%A5%BD%E5%AE%B6%E4%BC%99%EF%BC%8C%E7%BB%A7%20Fable%205%20%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E8%A2%AB%E6%89%92%E4%B9%8B%E5%90%8E%EF%BC%8C%E5%8F%88%E4%B8%80%E4%B8%AA%20Claude%20%E7%B3%BB%E7%BB%9F%E6%8F%90%E7%A4%BA%E8%AF%8D%E8%A2%AB%E6%89%92%E4%BA%86%E3%80%82.md)

> 日期：2026-07-22

前两天我看到有人把 Claude Design 的系统提示词整理出来了。

仓库叫 Trystan-SA/claude-design-system-prompt

我花时间看了一遍。

虽然 A 社太 xxx ，但是不妨碍我们研究它的产品，主打就是一个把它给蒸了。

我看完之后，有一个深深的感触，就 A 社这帮 shit ，看来也被 AI 味折磨得够呛啊，基本上大家有 AI 味儿的观感全写进去了。

连最近特别流行的米白底 + 衬线大标题 + 陶土色都写进了违禁清单，说这玩意儿就是去年的紫色渐变。。。。。。就这种。

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/23be3b5b-31ba-494a-82ef-b2b9aadf6da8.png" alt="23be3b5b-31ba-494a-82ef-b2b9aadf6da8" style="zoom: 33%;" />

我估计大家最近也被这种 AI 味儿折磨的不轻。

不过让我纳闷的是，你这用 prompt 去掉 AI 味儿，会不会又变成一种 AI 味儿了？

老实说，把 647 行 prompt 全部贴出来没啥必要。

大部分人也不会逐行看完。

我拎出来了一些我认为不错的细节，给大家过一遍。

这份 prompt 基本把 AI 做设计为什么一股 AI 味儿说清楚了。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/79972377ec548456d43cb25d6389266c6b09083c.png)

*▲ GitHub 仓库首页，截图时间为 2026 年 7 月 7 日*

**这份 prompt 在倒逼着 Claude 别瞎搞。**

不要乱加内容。

不要套默认模板。

不要把静态图当成成原型。

不要一上来就把页面整的跟站长站点似的（整个页面是满的，层次不分明）

---

## 第一件事：身份和职责

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/ca503e136fab5a2f11e47e4ceecc35910ef752e3.png)

*▲ `claude/system-prompt.md` L1-L19*

开头直接来了一句提纲挈领的话：

> You are not a code generator who happens to make designs. You are a designer who happens to use code.

Claude 应该把它自己的身份当是 expert designer，专家设计师。用户则是它的 manager，经理。

除非用户特别指出，Claude 默认用 HTML、CSS、SVG 和 JavaScript 来交付。

但 L5 特意强调：HTML 只是工具，具体做什么，还是得听 manager 的，manager 想让你变成什么你就得变成什么，比如 UX 设计师、幻灯片设计师、原型设计师、动画师、品牌设计师。

L7 这句话的意思

> Generic AI aesthetics are a failure mode, not a default.

它说的是如果一眼能看出是 AI 批量生成的通用式的 AI 审美，就是失败的设计，这种设计不能把它当成默认方案。

然后是全文总纲（L11）：

> You are not a code generator who happens to make designs. You are a designer who happens to use code.

你不是一个碰巧会做设计的生成代码的 AI  ，你是一个会碰巧用代码干活的设计师。

（好一个角色互换）

这俩有什么区别？原文自己解释了三层意思。

生成代码的 AI 会生成看起来还不错的输出结果，把页面填满。而设计师会先问这一页到底干嘛、用户第一眼该注意哪里、哪些可以直接干掉。

生成代码的 AI 容易照抄当下流行的渐变、字体和卡片；而设计师会先确定颜色、字体、间距、组件等规则，然后整套设计都按这套规则来。

生成代码的 AI 会机械性的满足用户需求：当用户说加一个模块，它就加；而设计师如果发现加东西会把作品搞崩了，就应该解释原因并提出反对意见。

也就是说，Claude Design 的第一件事，是先把 Claude 从只会写前端这个身份里给拎出来。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/3394e9f805967e4435d0dfc2933ed20fa0a45287.png)

你会将设计师的判断力融入到每一个作品中。你有自己的观点，但同时也会尊重你的用户，因为他们是你的 manager ，他们比你更了解他们的受众和目标。

## 第二件事：工作流

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/56a15affa9282646f387e2578de6e0fa5aaea1dd.png)

*▲ 原文 L21-L60*

很多 AI 很爱问问题，比如一般会问：

项目背景是什么？目标用户是谁？品牌调性是什么？喜欢什么风格？需要几套方案？要不要深色模式？

听起来 AI 像是在很正经的向用户询问一些设计方案，但实际上用户经常只想先让它动起来，别问太多问题。

原文这里规定了：**只问那些答案有可能会改变设计的问题。**

需求不清楚、品牌缺失、是否要做多套方向，这些可以向用户询问。

改个按钮样式、改个默认值、做两种差不多的排版，Claude 自己选就行了，只要在交付给用户的时候说一下就行了。

还有一句我觉得很实用：

> Build a skeleton, show it early.

你需要搭建一个框架，然后将其尽早展示出来。最怕的就是一下子在后台吭哧吭哧做完 15 页的设计，然后发现方向从最一开始就错了。

在设计中出的毛病，发现的越晚成本越高。LLM 尤其特别容易犯这个毛病，因为它不会心疼自己白干了多少活。。。也不会担心自己消耗了多少 token 。。。

## 第三件事：别为了塞满页面乱加东西

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/ba1d7290d2f986074f803d895e825a05cb7b271a.png)

*▲ 原文 L88-L120*

第五章叫 No filler。

这是全文最值得给所有 AI 写的前端钉在耻辱柱上的一章。

LLM 做页面有个老毛病了，**那就是有的没的都喜欢一顿乱加。**

材料不够，它就开始自己脑补。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/93658d3655b4fe9b5ade1a2d4f50eafd5680b9af.png)

*▲ 每个页面元素都要过一遍这五个问题*

所以 L90 上来就规定：页面上的每一个元素，都得说清楚出现在页面上的缘由。

这些元素要么传递必要信息，要么起到推动内容的作用，要么承担视觉结构。

如果三种规定都不满足，直接干掉。

## 第四件事：AI 味儿的黑名单

这节是我看完最爽的一段了。

原文直接给 AI 味儿列了一张黑名单。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/83e9fa3d250508aea8f2f4ee6433c96c1fcbbbee.png)

*▲ 原文 L122-L178*

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/a83ddb26eecf5287d07448fb9e96270f2acba04f.png)

*▲ 一张页面里塞进了 Prompt 直接点名的五样东西*

三色以上大渐变，默认别用。

彩虹、霓虹撞霓虹，基本就是 AI 味儿的模板。

真要用渐变，就同色系、低对比、两个色标。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/5a286457230cf72c25e2242e7ca353f11e2e4195.png)

Emoji 也一样。

标题前面为了 emoji 而 emoji ，比如硬加 🚀、📈、✅，这种直接干掉。

（想起来了很多 LLM 的输出，都会直接加上✅ 这种 emoji 了 ）

卡片也逃不过被点名的宿命；

普通内容不需要 `border-radius: 12px` 再加上 `border-left: 4px solid`。

左边状态色条应该留给提醒、警告、状态。

拿它铺满页面，就是标准的 AI SaaS 模板。

还有最近很流行的那模版：奶油色背景，衬线大标题，标题里夹一个斜体词，再配陶土色或琥珀色。

中招了有木有？

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/8d89db46dca83b81cd575c799eb782553a47e67d.png)

*▲ 这套组合大概就是：奶油底、衬线大标题、标题里夹斜体词，再用陶土色或琥珀色做强调*

**好家伙，蓝紫色渐变被骂下去之后，奶油色接班了。**

这套东西用在杂志、酒店、作品集里，没问题。

但你非用在开发者工具、企业后台、金融、医疗等领域，这叫个什么事儿？

（我当时确实认为这种风格应该用在杂志、作品集中，甚至婚纱摄影中。。。）

## 第五件事：视觉结构

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/79954b90670692cacd2dc3526b6aab6188ee3613.png)

*▲ 原文 L180-L250*

这一段可谓是直接把 Claude 拴起来拿鞭子抽了。

卡片之间留空多少，按钮里面留多少，标题用多大的，Claude 都得恭恭敬敬的照着执行。

比如上面留空 `17px`，下面留空 `19px`，换张卡片又冒出一个 `23px`。

每张卡片大小单独用都没事儿，但如果乱用，直接一团麻了。

原文要求间距尽量从 4px 或 8px 的倍数里选，8、16、24、32 都可以。

字体也是一样的。正文固定 16 px，说明文字固定 14 px，标题从 24、30、36 里选。别这会儿用 19 px，下一次又变成 21 px。

后面复制一张卡片、增加一个表单，直接沿用前面样式即可。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@3ca803f4aab1cd76e238437d9448c0246cf7d630/f05bfab0e45a12f347c9258c0cb9d12389d8c794.png)

*▲ 左右用的是同一份内容。右边只改了字号、灰度、留白和按钮样式*

原文里的 `visual hierarchy`，说的是用户打开页面以后能先看到什么。

标题、说明和按钮如果差不多大，两个按钮又是一个颜色，没有明显的层次感，用户的关注点不知道首先应该放在哪里。

但你如果把标题字号拉开，只留一个蓝色主按钮，查看文档改成普通入口，层次感就来了：先看标题，再看说明，然后决定要不要点按钮。

`rhythm` 管的是页面往下滚时，页面排版能否保持统一性。

假设页面连续介绍三个功能。第一段左边放文字、右边放截图，滚动到下一页的时候，应该也保持这样。

等三个功能介绍完，页面开始讲价格等商业案例时，再换背景或版式。

这样便于用户能看出内容已经到了下一部分。

## 第六件事：交互和反馈

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/49c4a39fb334ea15211139320c05b5f75c5a7d58.png)

*▲ 原文 L352-L410*

第十一章讲的是交互反馈。

一个按钮，至少准备 default、hover、active、focus、disabled 五种不同的风格。

如果它会发送请求的话，需要再来一个 Loading。。。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/9b470b86d78b66db84c33fe610e26c79b2eb626d.png)

第十二章说的是一件很小的事情：别让用户猜。

**一个页面中最重要的按钮应该只有一个。**

AI 很容易把页面做成按钮展览：开始使用、预约演示、查看文档、了解价格、联系我们，全都做得又大又亮。

结果用户扫了一圈，脑子里只剩一个问题：我到底该点哪个？

最后给了一个 5 秒测试。

把页面展示给用户，让他观看五秒钟，然后把页面关了，问他刚才应该点哪里。

他说不出来，基本上这个设计就可以直接干掉了。

## 第七件事：组件才是资产

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/9b8582ba82e0be7b5d650eac9a2a7abca25f1b3c.png)

*▲ 原文 L412-L449*

原文有一句：

> Design components, not pages.

这句容易听起来很抽象。

翻译成人话就是：先把能复用组件做好，再用这些组件去填充页面。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/185855466d5cd1d29326e7f1f0aae8f7ec4aa75e.png)

*▲ Header、Hero、FeatureCards、CTA、Footer，放到页面里大概就是这些位置*

一个普通的产品页，往往可以拆成顶部导航、首屏主区域、功能卡片、行动按钮区和底部信息。

每一页都重新画一遍按钮，那不叫设计系统，那叫克鲁苏。

按钮要有 primary、secondary、ghost，要有尺寸、图标和 loading。

卡片、输入框、弹窗、表格行也是一样。

间距、颜色、字体、圆角、阴影，这些都应该能复用。

做到这里，模型交付的东西才能考虑复用性和拓展性。

其他人才能拿这套东西继续复用。

## 第八件事：别拿 HTML 串几张静态图

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/c941e239bbd5821555fef2f69ee1edb608a86404.png)

*▲ 原文 L451-L489*

第十四章：别拿 HTML 重新做一个 Figma。

假设 Claude 设计的是一张注册页。

用户填完邮箱，点继续后，如果邮箱写错了，输入框下面要显示错误，完成之后，页面会进入下一步。这是真实发生的业务事件。

而 Figma 虽然能够用来画界面、做设计稿，也能制作可点击的演示原型，但 Figma 不会发生真正的业务事件。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@a1c1d0e587d4ec70b624fb172bff18b7a744e4e9/1b47033e470cff9db096df01c8d78b02bfd00c45.png)

## 第九件事：功能不需要太多

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/6a565c79e65e582580eb98786efafcfde445a9f7.png)

*▲ 原文 L491-L563*

比如用户要做五个功能，Claude 很容易先搭五个空壳，而且搭建速度很快。

原文要求它先找出最重要的三个，把入口、操作、错误状态和最终结果全部做完。

比如结账，用户要能填写地址、选择付款方式、提交订单。支付过程中要有 loading，填错以后要显示错误，成功和失败也能跳转到相关结果页。

优惠券、会员积分、邀请好友等功能不着急加。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@88dc87e02b370cce62533655e43d9a51177f0475/e94dd46330754bdc2fc3bf4a2b0d1a0ba1e072bc.png)

用户如果真要多套方案，差别也得落在布局、内容顺序或交互上。

把蓝色按钮改成紫色，不能算是第二套方案。

## 第十件事：另外一个 Agent 挑错

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/ab97613e9457bbfa7331f50658b54da863c02f1d.png)

*▲ 原文 L565-L598*

第十八章要求 Claude 每完成一次明显的视觉修改，就需要把页面交给 verifier 检查。

（verifier 就是另外一个 Agent ，专门负责验证和挑错用的）

这个 verifier 不负责重新设计。它截图、查看布局、用键盘走一遍页面，再检查 JavaScript 有没有报错。

发现输入框没有 label、按钮对比度太低、focus 看不见，就会把问题抛出来。等主 Agent 改完之后，再检查一次。

后面的 `polish-pass` 又会叫过来四个负责检查的 Agent，检查有无视觉阻碍、AI 模板味、页面层级和交互状态。

这更像分工验收，做页面的 Agent 负责改页面，检查 Agent 只管找视觉缺陷。

## Available skills：14 个工具该怎么用

最后一章列了 14 个 skills。

![](https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/d387bdc28bec0ed3080951040dc2398eeb714ae9.png)

*▲ 原文 L600-L647*

Available skills 就是一张工具的使用清单：

Claude 接到任务以后，不需要把 14 份说明全部读一遍。它先判断现在要做什么，再打开对应的 skill。

从零开始做页面，会用到 `discovery-questions`、`frontend-aesthetic-direction`、`wireframe` 和 `make-a-prototype`。

先根据用户提供的材料，再问缺少的信息；确定字体、颜色和页面密度；画线框图；最后把交互原型做出来。

如果用户已经有网站或品牌系统，Claude 会先用 `design-system-extract` 明确颜色、字体、间距和组件规则。

需要把现有页面整理成一套可复用组件时，再用 `component-extract` 拆按钮、卡片和表单；接着用 `generate-variations` 给出不同方案，需要现场调参数时，再加 `make-tweakable`。

做幻灯片则单独调用 `make-a-deck`。

剩下五个负责检查。

`accessibility-audit` 会检查对比度、键盘和 label 标识；`ai-slop-check` 会检查渐变、emoji 和模板味；`hierarchy-rhythm-review` 会先看页面应该从哪里开始；`interaction-states-pass` 会检查 hover、focus、loading 和 disabled 的交互情况。

`polish-pass` 会把前面四项一起跑完，收集问题，修完以后再检查一次。

所以从零做一张页面，大概是这条顺序：

```text
discovery-questions
→ frontend-aesthetic-direction
→ wireframe
→ make-a-prototype
→ polish-pass
```

已经有品牌和现成页面，则会使用另外一条路线：

```text
design-system-extract
→ generate-variations
→ make-tweakable
→ polish-pass
```

Available skills 只负责告诉 Claude 该打开哪份操作手册。具体怎么问、怎么画、怎么检查，都写在对应的 skill 文件里。

---

我看完以后，我觉得 Claude Design 的做事是有点套路的。

先把用户给的截图、品牌手册和代码读完，缺什么再问你的 manager 。先把方向确定，把骨架图画出来，错了就及时修复。

页面开始设计之后，页面上的每个元素都要有交代：按钮点到哪里，数字从哪来，组件能不能复用，表单提交后会发生什么。

甚至少了一个 focus 状态，都算没做完。

而且就算做完设计之后。还得经过层层检查：verifier 再把对比度、label、页面层级和交互状态查一遍。发现问题就让 Claude 改，改完再做最终确认。

这才是一个生产级的设计方案。
