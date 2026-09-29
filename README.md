# 复变函数讲义

本项目以 `docs/*.md` 作为日常维护的讲义源文件。`source/复变函数讲义.md` 是迁移时的原始快照；迁移后的修改应直接写入对应的 `docs` 页面，不要重新运行拆分脚本覆盖修改。

## 阅读与维护

推送 `main` 后，GitHub Actions 构建并更新 GitHub Pages。平板只需打开固定的网站地址并刷新。上传课堂板书后，请说明所属章节或现有小节；编辑对应页面，检查推导、公式、链接和构建结果，再提交。

本地预览：`pip install -r requirements.txt && mkdocs serve`。发布前检查：`mkdocs build --strict`。

首次发布需要在仓库 Settings → Pages 中将 Build and deployment 的 Source 设为 **GitHub Actions**。之后推送到 `main` 即自动更新。正式地址是 `https://xsy070709.github.io/complex-analysis-notes/`（仓库名改变时同步修改 `mkdocs.yml` 的 `site_url`）。

项目依赖 MathJax CDN 渲染公式，因此离线阅读时公式可能无法显示。源文件中无图片引用；后续图片放入 `docs/assets/` 并使用相对路径引用。
