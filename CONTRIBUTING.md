# 投稿内容质量规则

这个仓库不接收只有一句话、几句话或缺少完整文章逻辑的 Markdown 文章。

新增或修改 `ai-articles/`、`archive-bestjavaer/` 下的文章时，需要至少满足：

- 正文有效内容不少于 600 个字符；
- 至少 5 个有效段落；
- 至少 8 个有效句子；
- 图片、链接、日期、代码块不能替代正文论述。

本地提交前会运行：

```sh
python3 scripts/check_article_quality.py --staged
```

PR 和 GitHub Pages 部署也会运行同一套检查。若检查失败，请先把文章补成完整内容，再重新提交。
