# Why did I create another public domain?

[English](./why-did-i-create-another-public-domain.md) | [Chinese Original](../../../ai-articles/03-tools-and-resources/Layweout%20%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8E%92%E7%89%88%E5%B7%A5%E4%BD%9C%E5%8F%B0.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-04-23

[toc]

It's really hard for people to write public numbers.

The article is only half complete. The other half, how do you make it look personal on a cell phone, rather than the instructions coming out of a back-office system?

I didn't make much of it before.

First used **mdnice**. The advantages are obvious, there are lots of templates, one-click rendering, and the initial experience is really good. You put Marktown in there, and the right effect came out, and at first there was a feeling that it was okay.

But after a long time, the problem came up.

The style of the template is fixed and it is difficult to fine-tune; it is easier to slow down every rendering; and, more importantly, it is one thing to preview, and it is another to copy it into the public domain.

Later on **md. gzcx. net**. The advantage of this tool is that it can be self-defined CSS, which is good in the short term. You can write it yourself if you want to dial numbers, space, title style.

But the problem is, the long-term maintenance of a public domain, CSS, is not really easy.

It's a bit of a reference block today, and tomorrow's tables are uncomfortable; it's a lot of code, it's a lot of pictures; and it's a little bit of a filter by the Twitter public editor, and it turns out: ** I'm writing, and I'm doing it every day, and it's like a bug.**

You can take that.

So, in response to the pain of these two tools, you decided to write a copy of my own --`Layweout`.

Project address:[https://github.com/crisxuan/layweout](https://github.com/crisxuan/layweout)

Online address:[https://layweout.vercel.app](https://layweout.vercel.app)

# Layweout what is #

`Layweout`This name is from`layout + we`.

`layout`It's layout.`we`It's a micro-intelligence public sign, which, together, is a tool for the layout and output of the public domain.

I feel a little smart about that name, but it's logical.

It is not a simple Markdown renderer, nor is it a template displayer, but a local desk for the public launch process.

It's like this:

Left is the style area, select the article template.

The middle is the text area, which you can enter`Markdown`, `HTML`, can also paste the rich text directly.

On the right is a phone-end reading preview, which is used to quickly judge the layout.

Last click to copy, the tool recreates an internal connection style HTML that fits the public name editor.

Here's a key point:

** Layweout does not directly copy preview DOM.**

Because browser preview and public number editor is not an environment at all.

The CSS, which can run in the browser, is not necessarily recognized by the public editor. You look at the background, the gradient, the corner, the edge, and it's probably gone.

So the core logic of Layweout is not to copy the right preview, but to:

```text
Input
Zenium
Unified cleaning and rendering
Zenium
Browser Preview
Zenium
Recreate Public ID Compatibility HTML
Zenium
Copy to Public Editor
```

As a matter of fact, the preview is for people, and the output is for the public editor.

These two can't mix.

# Why am I not content with the tools available #

Of course it's not bad.

It's for fast layouts, for people who don't want to mess around. Once the template is selected and the article is posted, it is basically available.

But my problem is that I often write longer things and the type of content is irregular.

Sometimes it's the AI tool experience, sometimes it's the technology, sometimes it's the product thinking. There may be code blocks, tables, references, screenshots, lists, dividing lines.

At this point, the template is not enough if it is just "looking."

It must be able to carry the real content.

My request for layout tools is three:

** First, the text should be comfortable.**

Most of the reading of the public sign takes place on a mobile phone, and the characters, lines and spacing of the text are much more important than a fancy title.

** Second, complex elements cannot explode.**

The code blocks, tables, quotes, and pictures show that once these things are in trouble, the whole article appears to be amateur.

** Thirdly, after copying to the public domain, there can be no major change.**

It's a good preview. It's stuck. It's all in vain.

The biggest problem with ready-made tools is the third point.

They usually place greater emphasis on preview effects, but the matter of whether the public editor recognizes this HTML has not been dealt with sufficiently.

And Layweout thought the other way around.

** Make sure you stick it in, then talk about style.**

This sequence is important.

# How the front-end architecture is designed

Layweout's architecture is not complicated, but the border is clear.

In general, there are several layers:

```text
core for content cleansing and conversion
Data for template data, grouping and schema
ui Responsible for page structure
syles handle desktop UI and browser preview styles
Export for public compatible HTML output
utils for clipboard, statistics, etc.
```

The purpose of this layer is not to be perceived as high.

Instead, it is necessary to avoid searching all over the project for every template that is changed in the future.

I'm sick of this code:

Add a new template today to change the data.

And change UI.

And CSS.

And change the logic.

The logic has to be replicated.

Finally, it was not known whether the other templates had been broken.

It started writing fast, but it was painful to keep the back.

So Layweout took several points of change apart.

# Input Layer: Close your contents first

User input may come from three places:

- `Markdown`
- `HTML`
- Rich Text

These three things appear to be articles, but they are completely different in structure.

Markdown, go through first.`marked`Convert to HTML.

HTML and Rich Text to go through`DOMPurify`Purge, remove dangerous or meaningless properties.

And then the tools do some normative things, like,`b`Convert`strong`Put`i`Convert`em`, wraps the scattered text nodes into paragraphs.

This step appears to be fundamental, but it is particularly important.

** Enter not conditio, all the templates are in the back.**

You can't expect a bunch of DOMs from different sources, and the direct set is stable.

So Layweout's first step is not to be pretty, but to clean up.

Template Layer: Templates are not a bunch of CSS

Layweout now has **22 sets of independently exported templates** grouped by publishing, technology, brand life.

This set of 22 templates is not simply a color change.

Every set of templates has its own.`tokens`For example:

- Page Background
- Text colour.
- Focus on the color.
- Reference block background
- The code block color.
- Table Styles
- Fonts
- Okay.
- Spacing
- Outer packaging background

These things are concentrated in templates.

This is probably the idea:

```text
I'm sorry, presets/
Groups.js Template Grouping and Governance State
template token
schema.js Template Verify and Visible Template pie Fan.
```

This design solves a very practical problem:

** With more templates, governance is needed.**

Not all templates should be exposed to users.

Some of the earlier templates may be available, but they are not independently exported and are not sufficiently stable. Then hide it, not squeeze it into the selection.

The template library is not as good as it is.

It's really good to open every one of them.

# Preview layer: let people judge the reading rhythm

The preview layer is responsible for the display in the browser.

Here you can use the CSS file, you can use the CSS variable, and you can do more comfortable phone reading simulations.

Layweout's preview is not intended to be 100% reset of the public number editor, because this thing is not realistic in itself.

The public-name editor filters styles and may vary from content to content.

So the goal of the preview level is:

** Try to simulate the public phone-end reading effect and allow authors to quickly judge the text.**

The title is not too heavy.

The text is not too crowded.

The quote block is not a game.

The code blocks are not readable.

There was no spill in the form.

These problems should be visible in the preview area.

However, the final copying effect is based on the output module regenerated HTML.

This is where Layweout and many of the layout tools are different.

It does not take the preview as final.

It takes the preview as a middle link.

# Export layers: The real point is here #

Layweout's core, actually.`src/export/wechat.js`.

This module recreates a public domain compatible HTML.

The process is probably this:

```text
HTML after getting rendered
Zenium
Generate inline from current template profile
Zenium
Process links, lists, reference blocks, etc.
Zenium
Supplement to background-color
Zenium
Compatibility of background and reference blocks
Zenium
Return HTML to copyable
```

Why does it have to be internal?

Because the public name editor will not keep the external CSS completely.

You've written it with grace, copy it and probably nothing.

So, when exporting, you write key styles to elements.`style`attribute.

That doesn't sound elegant.

However, the public page is not a front-end architecture grand prix.

** Stable paste is the first goal.**

Layweout also made a few compatible strategies.

First of all, the complex background adds.`background-color`.

Because gradients and complex contexts may be lost, but the pure ones are relatively stable.

Secondly, a background template will make an outer package.

In this way, as much as possible, the white stitches between the paste and the block are avoided.

Thirdly, the reference blocks would be treated extra.

Some of the reference blocks use normal`blockquote`The public sign is unstable, so it changes to a more conservative table structure.

That sounds a little old-fashioned.

But there's no way to do it. It's on the public editor.

Why don't you expose the standard mode to the user

The Standard Mode/ Compatibility Mode was used in the previous tool.

Standard mode output is lighter and compatible mode output is more stable.

Sounds reasonable.

But then I figured out that this button should not be shown to users.

Because users use Layweout, not to study HTML output strategies.

All he wanted to know was, "I'm going to copy it in the public domain.

Then the default should export the most stable compatibility.

The so-called standard model should be retained in internal testing. For example, it's useful to do a snapshot comparison, sort out and export structural changes.

But on the interface, it only creates a choice burden.

The problem with many products is not inadequate functionality, but the complexity of the system, which is left to users.

I'm particularly vigilant about this.

** Users should not understand your compatibility strategy. Users should receive only one stable result.**

# Snapshot test: prevent a template from being changed and a template from blowing up

The template tool is also an easily ignored problem: regression testing.

22 The set of templates, which does not seem to be particularly numerous, is not realistic if it is tested manually every time.

You changed one.`blockquote`, which may affect all templates.

You've changed the context-compatible strategy, which could cause some templates to break.

You've changed the list label, and you might mess up the orderly list with the unsequence table.

So Layweout added the export snapshot test.

The test takes a more comprehensive article sample with titles, text, links, references, lists, code blocks, tables, pictures, and then produces all visible templates to export HTML snapshots.

Change the logic later, just run:

```bash
npm run test: snapshots
```

If the snapshot changes, then the output does change.

At this point in time, it would be expected to be modified or a mistake.

This thing has no visual impact, but it's practical.

Because the most scary thing about layout is not having bugs today.

The worst thing to do is to fix a template today and break the other 21 templates.

# Where is Layweout's advantage

In summary, Layweout does not have the advantage of "more templates".

In fact, 22 templates are not particularly exaggerated.

It's the real advantage in four places.

** First, the local desk.**

It does not have to rely on an online editor ' s status to open it, and input, preview and copy are done in one place.

** Second, wider source of input.**

Markdown, HTML, rich text can come in instead of forcing you to write in one way or another.

** Third, preview and export separation.**

The browser preview is for effects, and the public sign is for compatibility. As soon as the two borders are removed, the problems are much clearer.

** Fourth, the template is governance.**

Templates are not simply stacked on CSS, but are token, profile, group, schema, snapshot tests.

These things come together, and the final experience is:

You can write long letters more comfortably.

There is no need to worry about replicating later.

I don't have to do everything with CSS.

There is no need to waste attention on the question of "why is this quote again out of context"?

# The problem with other layout tools is not bad, but not my long-term scene

And here's the thing: mdnice and md. gzcx. net are not worthless tools.

They solve the problem of fast layout.

These tools are fully adequate if only occasional correspondence is sent or when the details of templates are not required.

But that's not my scene.

I need to write long.

It needs to be repeated.

There is a need to maintain stability in all types of articles.

The complex content of the code, the form, the reference, the picture can be contained.

At this point, the problem of traditional layout tools becomes obvious:

** The results of the preview and reproduction were inconsistent.**

** Templates look at many, but style is fixed.**

** Self-defined CSS pre-spill, post-maintenance.**

** Complex background and layout is easily thrown into the public domain.**

** The longer the article is, the higher the cost of manual repair.**

So I don't want to do a more fancy mdnice.

What I want to do is be a more manageable public launch desk.

Finally

It's a little bit of a story.

It doesn't look like a model, it doesn't look like a product structure, it doesn't look like a database performance, it doesn't look so hard.

But for content creators, it's very realistic.

One article is more serious, and if the layouts are all messed up, the cost of reading will rise immediately.

This is especially the case for the public sign, where most people watch on their cell phones.

The screen is that big.

Squeeze the text a little bit, recapitulate it a little bit, and the reader may have crossed it.

So I'm getting the feeling:

** The layout is not decoration, but delivery of content.**

What Layweout did was essentially stabilize the delivery chain.

From input, to preview, to template, to copy, to public editor, every step is as narrow as possible.

Don't pursue fancy.

The search for stability first.

Once you've stabilized, you'll look good.

And that's one of the judgments I'm making now:

** The good tool is not to spread all options to users, but to digest complexities and then give users the best way.**

Layweout is not perfect now.

But at least it has solved my worst problem:

After the article was finished, I stopped fighting with the public editor.

It's already worth it.
