# Pinyuan Li Website


https://brandeispatrick.github.io/coding-bat/


This repository contains the source code for **Pinyuan Li's personal website**. The site is powered by [Jekyll](https://jekyllrb.com/) and the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme. Posts, pages and configuration files are kept here so that the website can be built locally or automatically deployed to GitHub Pages.

## Getting Started

### Prerequisites
- Ruby 3.1 or later
- [Bundler](https://bundler.io/) for managing Ruby gems

### Installation
1. Clone this repository.
2. Run `bundle install` to install dependencies.
3. Start a local server with `bundle exec jekyll s` and visit <http://localhost:4000/coding-bat/>.

## Repository Layout

- `_posts` &ndash; blog posts written in Markdown
- `_tabs` &ndash; standalone pages such as the About page
- `_config.yml` &ndash; site configuration
- `assets` &ndash; images and other static files
- `.github/workflows` &ndash; GitHub Actions used to build and deploy the site

## Deployment

Changes pushed to the `main` branch trigger the workflow defined in
`.github/workflows/pages-deploy.yml`, which builds the site and deploys it to GitHub Pages automatically.

## License

This project is licensed under the [MIT License](LICENSE). The design is based on the [Chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy).
