# Workflows

`publish.yml` renders the HTML site and deploys it to GitHub Pages on every
push to `main`.

PDF and EPUB are deliberately not built here. TinyTeX in CI is slow, and the
print book only needs regenerating when you decide it does. Build those locally
and attach them to a tagged release:

```bash
quarto render --to pdf --to epub
```

Before this workflow can succeed, enable Pages for the repository and set the
source to **GitHub Actions** under Settings, Pages.
