# 复变函数讲义
整理自杨晓京老师随堂板书，随课堂进度更新，整理工作由chatgpt完成。
本项目以 `docs/*.md` 作为日常维护的讲义源文件。`source/复变函数讲义.md` 是迁移时的原始快照,不再更新；迁移后的修改应直接写入对应的 `docs` 页面，不要重新运行拆分脚本覆盖修改。

## 阅读与维护

在`https://xsy070709.github.io/complex-analysis-notes/`中查看讲义。
本地预览：`pip install -r requirements.txt && mkdocs serve`。
推送 `main` 后，GitHub Actions 构建并更新 GitHub Pages。阅览只需打开固定的网站地址并刷新。
项目依赖 MathJax CDN 渲染公式，因此离线阅读时公式可能无法显示。源文件中无图片引用；后续图片放入 `docs/assets/` 并使用相对路径引用。
