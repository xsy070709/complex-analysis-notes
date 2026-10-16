# 复变函数讲义
整理自杨晓京老师随堂板书，随课堂进度更新，整理工作由chatgpt完成。
本项目以 `docs/*.md` 作为日常维护的讲义源文件。`source/复变函数讲义.md` 是迁移时的原始快照,不再更新；迁移后的修改应直接写入对应的 `docs` 页面，不要重新运行拆分脚本覆盖修改。

## 阅读与维护

在`https://xsy070709.github.io/complex-analysis-notes/`中查看讲义。
本地预览：`pip install -r requirements.txt && mkdocs serve`。
推送 `main` 后，GitHub Actions 构建并更新 GitHub Pages。阅览只需打开固定的网站地址并刷新。
项目依赖 MathJax CDN 渲染公式，因此离线阅读时公式可能无法显示。源文件中无图片引用；后续图片放入 `docs/assets/` 并使用相对路径引用。

## PDF 同步发布

网页每页顶部提供“下载最新版 PDF”。PDF 从 `nav.yml` 中的同一组 `docs` 章节按导航顺序生成，包含三级书签、可点击目录、页眉和章节的返回目录链接，以及跨章节引用跳转。数学公式和中文字体嵌入 PDF，支持离线阅读。

推送 `main` 或手动运行 `Deploy notes and PDF` 后，构建并验证 PDF，将同一份 PDF 随网页一起部署，然后覆盖固定的 `pdf-latest` Release 附件并将滚动标签移至对应提交。下载地址始终为：

https://github.com/xsy070709/complex-analysis-notes/releases/download/pdf-latest/complex-analysis-notes.pdf

生成失败时停止部署，不用不完整的 PDF 覆盖已发布版本。更新讲义只需修改 `docs` 章节；无需手动维护 PDF、修改版本号或创建新 Release。

本地构建（Debian/Ubuntu）：

```sh
sudo apt-get install pandoc texlive-xetex texlive-lang-chinese texlive-latex-extra fonts-noto-cjk lmodern
pip install -r requirements.txt
python scripts/build_pdf.py
mkdir -p docs/downloads
cp output/pdf/complex-analysis-notes.pdf docs/downloads/
mkdocs build --strict
```

不要运行迁移脚本 `build_notes.py`；它只用于最初迁移，会覆盖现有章节和首页。
