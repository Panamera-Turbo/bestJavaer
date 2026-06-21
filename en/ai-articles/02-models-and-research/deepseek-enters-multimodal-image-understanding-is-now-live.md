# DeepSeek Enters Multimodal: Image Understanding Is Now Live

[English](./deepseek-enters-multimodal-image-understanding-is-now-live.md) | [Chinese Original](../../../ai-articles/02-models-and-research/DeepSeek%20%E5%BC%80%E5%A4%A9%E7%9C%BC%E4%BA%86%EF%BC%8C%E8%AF%86%E5%9B%BE%E5%8A%9F%E8%83%BD%E4%B8%8A%E7%BA%BF%EF%BC%81.md)

> English edition based on the Chinese original.

> Date: 2026-06-19

DeepSeek image understanding is now widely available.

When I first saw people saying DeepSeek had launched image recognition, my first reaction was: didn't it already have that? I had used it before to extract text from images.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260618134619329.png" alt="DeepSeek image feature" style="zoom:50%;" />

That reaction was wrong. OCR is not the same thing as image understanding.

I then saw Chen Xiaokang's post on X.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260618145538661.png" alt="Chen Xiaokang post" style="zoom:50%;" />

Chen Xiaokang leads DeepSeek's multimodal team. DeepSeek's image mode had already been in grayscale testing shortly after V4, but this time it became broadly available on both web and app.

The important point is this: DeepSeek is not just extracting text from images. It is finally recognizing images.

I tested it with a picture right away.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260618143419427.png" alt="DeepSeek image test" style="zoom:50%;" />

The process was fast. It first identified the scene as a night football match, probably in a VIP or box area. It described the person in the image, noticed the beige outfit and sunglasses, and then caught a detail near the lower-right railing: the Portugal team badge.

That detail matters. If you only look at the general composition, anyone can say there is a woman at a stadium. But noticing the badge changes the quality of the answer.

It also avoided overclaiming. It said the stadium might be Lisbon's Estadio da Luz or Dragao Stadium. That uncertainty is important. The problem with AI is not that it can be wrong. The expensive part is when it is wrong while sounding completely certain.

Another interesting point was its judgment that the image might be AI-generated.

![DeepSeek AI image judgment](https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260618150516206.png)

The reasons were concrete: the frame looked too clean, the lighting was too cinematic, and the skin and edges blended a little too smoothly.

This is different from relying only on provenance signals such as SynthID or content credentials.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260618153656695.png" alt="Content credential check" style="zoom: 33%;" />

DeepSeek was reasoning from the image itself.

I also tested it with a more sarcastic AI meme image.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed/image-20260618154038059.png" alt="DeepSeek reasoning test" style="zoom:50%;" />

Its reasoning was strong, but it still made mistakes. It misidentified Claude 3.5 as Fable 5, and it gave an incorrect reason for a model restriction. Those mistakes are not surprising if the model's knowledge is behind recent events.

The useful part is the direction. DeepSeek's multimodal capability is no longer only about reading text in pictures. It can describe scenes, identify visual clues, explain uncertainty, and reason about whether an image may be synthetic.

That makes it much more useful, but also raises the bar for how carefully we should read its answers. Image understanding is powerful. Confident image understanding still needs verification.
