<h1 align="center">Awesome AI Search Optimization</h1>

<p align="center"><a href="https://airankwp.com"><img src="assets/banner.png" alt="Awesome AI Search Optimization. Click here to check your site free with AIRankWP." width="100%"></a></p>

<p align="center">
<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
<img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs welcome">
<img src="https://img.shields.io/badge/license-CC0--1.0-blue" alt="License CC0 1.0">
<a href="https://github.com/devanasolver/awesome-ai-search-optimization/commits/main"><img src="https://img.shields.io/github/last-commit/devanasolver/awesome-ai-search-optimization" alt="Last commit"></a>
</p>

<p align="center">
<a href="https://github.com/devanasolver"><img src="https://img.shields.io/badge/Follow-@devanasolver-181717?style=for-the-badge&logo=github" alt="Follow on GitHub"></a>
<a href="https://github.com/devanasolver/awesome-ai-search-optimization/stargazers"><img src="https://img.shields.io/github/stars/devanasolver/awesome-ai-search-optimization?style=for-the-badge&logo=github&label=Star%20this%20list" alt="Star this list"></a>
<a href="https://airankwp.com"><img src="https://img.shields.io/badge/Free%20AI%20audit-airankwp.com-4638c8?style=for-the-badge" alt="Free AI audit at airankwp.com"></a>
</p>

> Open-source GitHub repos for AI SEO, AEO and GEO: making your site visible to ChatGPT, Perplexity, Claude, Gemini and Google AI Overviews.

AEO = Answer Engine Optimization. GEO = Generative Engine Optimization. Same idea: get your content found and cited when people ask AI instead of searching Google.

**Rules of this list:** every repo exists, is public, is not archived and has a license or a clear note. Each line is written in plain words. Repos are listed on merit, including the maintainer's own (marked). Star counts are live badges. Details of how entries are checked are in [CONTRIBUTING.md](CONTRIBUTING.md).

Part of a series of use-case directories of GitHub tools. Last full check: 2026-10-17.

## Contents

- [Site audit and AI-readiness checkers](#site-audit-and-ai-readiness-checkers)
- [AI visibility and citation trackers](#ai-visibility-and-citation-trackers)
- [llms.txt and machine-readable content](#llmstxt-and-machine-readable-content)
- [WordPress, WooCommerce and framework plugins](#wordpress-woocommerce-and-framework-plugins)
- [Agent skills and MCP servers](#agent-skills-and-mcp-servers)
- [Self-hosted SEO platforms](#self-hosted-seo-platforms)
- [Research, playbooks and specs](#research-playbooks-and-specs)
- [Other awesome lists](#other-awesome-lists)
- [How to choose](#how-to-choose)
- [Contributing](#contributing)

## Site audit and AI-readiness checkers

Point these at a website and get a list of problems. Some score AI-search readiness (can AI crawlers read you, do you have schema and llms.txt). Others are classic technical SEO crawlers.

- [adityaarsharma/sitewalk](https://github.com/adityaarsharma/sitewalk) ![stars](https://img.shields.io/github/stars/adityaarsharma/sitewalk?style=flat&label=%E2%98%85) - Self-hosted technical SEO crawler and MCP server. 50+ checks, PDF and CSV reports. _(MIT)_
- [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) ![stars](https://img.shields.io/github/stars/Auriti-Labs/geo-optimizer-skill?style=flat&label=%E2%98%85) - Checks if AI engines can cite your site, then helps you fix it. CLI, Python and MCP. _(MIT)_
- [devanasolver/ai-seo-toolkit](https://github.com/devanasolver/ai-seo-toolkit) ![stars](https://img.shields.io/github/stars/devanasolver/ai-seo-toolkit?style=flat&label=%E2%98%85) - Free CLI: AI-search visibility audit, keyword ideas and Search Console data. No paid keys. (By the maintainer of this list.) _(MIT)_
- [Houseofmvps/claude-rank](https://github.com/Houseofmvps/claude-rank) ![stars](https://img.shields.io/github/stars/Houseofmvps/claude-rank?style=flat&label=%E2%98%85) - Claude Code plugin that finds why AI won't cite your site and fixes the discoverability files. 170+ rules. _(MIT)_
- [houtini-ai/seo-audit](https://github.com/houtini-ai/seo-audit) ![stars](https://img.shields.io/github/stars/houtini-ai/seo-audit?style=flat&label=%E2%98%85) - MCP server for Claude that merges Search Console, a crawl, DataForSEO and Majestic data into one audit. Some data sources need their own accounts. _(Apache-2.0)_
- [jianruntech/geo-score](https://github.com/jianruntech/geo-score) ![stars](https://img.shields.io/github/stars/jianruntech/geo-score?style=flat&label=%E2%98%85) - Gives your site a 0-100 AI-readiness score. Can also track citations weekly with your own API keys. CLI, GitHub Action, MCP. _(MIT)_
- [mverab/eGEOagents](https://github.com/mverab/eGEOagents) ![stars](https://img.shields.io/github/stars/mverab/eGEOagents?style=flat&label=%E2%98%85) - GEO and AEO toolkit for improving content so AI answer engines pick it up. CLI, Claude Code and MCP. _(MIT)_
- [OranAi-Ltd/orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) ![stars](https://img.shields.io/github/stars/OranAi-Ltd/orangeo-ai-visibility-skill?style=flat&label=%E2%98%85) - Agent skill that checks robots.txt, llms.txt, schema and citation signals, and finds gaps against competitors. _(MIT)_
- [puneetindersingh/open-seo-crawler](https://github.com/puneetindersingh/open-seo-crawler) ![stars](https://img.shields.io/github/stars/puneetindersingh/open-seo-crawler?style=flat&label=%E2%98%85) - Self-hosted crawler for technical SEO. Also checks that Googlebot and AI crawlers (GPTBot, PerplexityBot) see the same page. _(MIT)_
- [seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill) ![stars](https://img.shields.io/github/stars/seo-skills/seo-audit-skill?style=flat&label=%E2%98%85) - Command-line SEO audit with 332 rules: Core Web Vitals, security headers, structured data and more. _(MIT)_
- [spronta/crawlie](https://github.com/spronta/crawlie) ![stars](https://img.shields.io/github/stars/spronta/crawlie?style=flat&label=%E2%98%85) - Fast, free crawler for technical SEO and AI-search checks. Made for people and agents. _(check repo)_
- [squirrelscan/squirrelscan](https://github.com/squirrelscan/squirrelscan) ![stars](https://img.shields.io/github/stars/squirrelscan/squirrelscan?style=flat&label=%E2%98%85) - Website audit tool for coding agents. 300+ rules across SEO, speed, security and accessibility. _(MIT)_

## AI visibility and citation trackers

These ask AI engines questions and record whether your brand is mentioned or cited. Most need your own API keys for the AI models. Results from AI engines change from run to run, so treat the numbers as trends.

- [AI2HU/gego](https://github.com/AI2HU/gego) ![stars](https://img.shields.io/github/stars/AI2HU/gego?style=flat&label=%E2%98%85) - Tracks how your brand shows up across many LLMs. _(GPL-3.0)_
- [AKzar1el/mcp-geo](https://github.com/AKzar1el/mcp-geo) ![stars](https://img.shields.io/github/stars/AKzar1el/mcp-geo?style=flat&label=%E2%98%85) - Tracks brand citations across seven AI search surfaces. Free to self-host. The author also sells an optional paid audit. _(MIT)_
- [ansvisor/ansvisor](https://github.com/ansvisor/ansvisor) ![stars](https://img.shields.io/github/stars/ansvisor/ansvisor?style=flat&label=%E2%98%85) - Open-source platform to track AI visibility, citations, prompts and competitors across major AI search engines. _(MIT)_
- [Canonry/canonry](https://github.com/Canonry/canonry) ![stars](https://img.shields.io/github/stars/Canonry/canonry?style=flat&label=%E2%98%85) - Agent-first platform for AI SEO (AEO/GEO). _(MIT)_
- [danishashko/geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) ![stars](https://img.shields.io/github/stars/danishashko/geo-aeo-tracker?style=flat&label=%E2%98%85) - Local-first dashboard that tracks your brand across 6 AI models. _(MIT)_
- [databluedev/searchmirror](https://github.com/databluedev/searchmirror) ![stars](https://img.shields.io/github/stars/databluedev/searchmirror?style=flat&label=%E2%98%85) - Self-hosted rank tracker and AI visibility monitor. Needs your own DataBlue SERP API key. _(AGPL-3.0)_
- [elmohq/elmo](https://github.com/elmohq/elmo) ![stars](https://img.shields.io/github/stars/elmohq/elmo?style=flat&label=%E2%98%85) - Self-hostable platform that tracks how ChatGPT, Claude, Perplexity, Gemini, Copilot, Grok and Google AI Overviews mention your brand. _(MIT)_
- [limelit-co/open](https://github.com/limelit-co/open) ![stars](https://img.shields.io/github/stars/limelit-co/open?style=flat&label=%E2%98%85) - Self-hosted AI visibility tracker. One Go binary with SQLite. Bring your own API keys. _(Apache-2.0)_
- [oneglanse/oneglanse](https://github.com/oneglanse/oneglanse) ![stars](https://img.shields.io/github/stars/oneglanse/oneglanse?style=flat&label=%E2%98%85) - Tracks brand mentions and citations in AI answers by using the real product interfaces. Self-hostable. _(MIT)_
- [onism1767-creator/potato](https://github.com/onism1767-creator/potato) ![stars](https://img.shields.io/github/stars/onism1767-creator/potato?style=flat&label=%E2%98%85) - Simple local check of how often a brand is mentioned in Claude's web-search answers. Runs offline in mock mode. _(MIT)_

## llms.txt and machine-readable content

Tools that publish an llms.txt file or Markdown copies of your pages so AI agents can read your site more easily. llms.txt is a proposed standard. Support by AI providers varies, so do not count on it for results.

- [4hse/astro-llms-txt](https://github.com/4hse/astro-llms-txt) ![stars](https://img.shields.io/github/stars/4hse/astro-llms-txt?style=flat&label=%E2%98%85) - Generates llms.txt for Astro sites. _(check repo)_
- [apify/actor-llmstxt-generator](https://github.com/apify/actor-llmstxt-generator) ![stars](https://img.shields.io/github/stars/apify/actor-llmstxt-generator?style=flat&label=%E2%98%85) - Apify Actor that reads a website and builds an llms.txt file. Runs on the Apify platform, which has its own pricing. _(Apache-2.0)_
- [dodopayments/dualmark](https://github.com/dodopayments/dualmark) ![stars](https://img.shields.io/github/stars/dodopayments/dualmark?style=flat&label=%E2%98%85) - Serves a Markdown copy of each page to AI agents and HTML to humans, chosen by content negotiation. _(Apache-2.0)_
- [jdillard/sphinx-llms-txt](https://github.com/jdillard/sphinx-llms-txt) ![stars](https://img.shields.io/github/stars/jdillard/sphinx-llms-txt?style=flat&label=%E2%98%85) - Generates llms.txt for Sphinx documentation sites. _(MIT)_
- [rubenmarcus/aeo.js](https://github.com/rubenmarcus/aeo.js) ![stars](https://img.shields.io/github/stars/rubenmarcus/aeo.js?style=flat&label=%E2%98%85) - Generates llms.txt, robots.txt, sitemap and JSON-LD to make a site easier for AI search to read. _(check repo)_
- [thedaviddias/llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) ![stars](https://img.shields.io/github/stars/thedaviddias/llms-txt-hub?style=flat&label=%E2%98%85) - Big directory of sites and tools that use the llms.txt standard. Good place to see real examples. _(check repo)_
- [yazinsai/site-md](https://github.com/yazinsai/site-md) ![stars](https://img.shields.io/github/stars/yazinsai/site-md?style=flat&label=%E2%98%85) - Next.js helper that serves clean Markdown of your pages to AI agents while people get normal HTML. _(MIT)_

## WordPress, WooCommerce and framework plugins

Drop-in plugins and packages for popular platforms.

- [AEO-God-Mode/aeo-god-mode](https://github.com/AEO-God-Mode/aeo-god-mode) ![stars](https://img.shields.io/github/stars/AEO-God-Mode/aeo-god-mode?style=flat&label=%E2%98%85) - Free WordPress plugin: schema, llms.txt, AI crawler controls and citation tracking. _(GPL-2.0)_
- [GitHiteshZope/aigeo](https://github.com/GitHiteshZope/aigeo) ![stars](https://img.shields.io/github/stars/GitHiteshZope/aigeo?style=flat&label=%E2%98%85) - GEO package for Laravel to help products appear in AI-generated answers. _(MIT)_
- [madeburo/GEO-AI-Woo](https://github.com/madeburo/GEO-AI-Woo) ![stars](https://img.shields.io/github/stars/madeburo/GEO-AI-Woo?style=flat&label=%E2%98%85) - WordPress and WooCommerce plugin that generates llms.txt, AI crawler rules and metadata. _(GPL-2.0)_

## Agent skills and MCP servers

Skills and MCP servers that let a coding agent (Claude Code, Codex, Cursor and similar) run SEO and AI-search work for you.

- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) ![stars](https://img.shields.io/github/stars/AgriciDaniel/claude-seo?style=flat&label=%E2%98%85) - Big SEO skill for Claude Code: technical SEO, schema, GEO/AEO, llms.txt, local and e-commerce SEO, reports. _(MIT)_
- [Akxan/google-seo-mcp](https://github.com/Akxan/google-seo-mcp) ![stars](https://img.shields.io/github/stars/Akxan/google-seo-mcp?style=flat&label=%E2%98%85) - MCP server with 100+ tools: Search Console, GA4, PageSpeed, structured data, llms.txt and AI crawler checks. _(MIT)_
- [AminForou/mcp-gsc](https://github.com/AminForou/mcp-gsc) ![stars](https://img.shields.io/github/stars/AminForou/mcp-gsc?style=flat&label=%E2%98%85) - Connects Google Search Console to Claude through MCP so you can ask questions about your data. _(MIT)_
- [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) ![stars](https://img.shields.io/github/stars/Bhanunamikaze/Agentic-SEO-Skill?style=flat&label=%E2%98%85) - SEO analysis skill for Antigravity, Codex and Claude, with 16 sub-skills and helper scripts. _(MIT)_
- [bzsasson/screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp) ![stars](https://img.shields.io/github/stars/bzsasson/screaming-frog-mcp?style=flat&label=%E2%98%85) - MCP server that runs Screaming Frog crawls and reads the results. Needs a Screaming Frog install, which has its own licence terms. _(MIT)_
- [deepakness/google-ai-search-optimization](https://github.com/deepakness/google-ai-search-optimization) ![stars](https://img.shields.io/github/stars/deepakness/google-ai-search-optimization?style=flat&label=%E2%98%85) - Unofficial agent skill built from Google's guidance on AI Overviews and AI Mode. _(check repo)_
- [Hainrixz/claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) ![stars](https://img.shields.io/github/stars/Hainrixz/claude-seo-ai?style=flat&label=%E2%98%85) - Claude Code toolkit with a two-score audit (SEO and AI search) and an opt-in fixer. _(MIT)_
- [leopard627/fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) ![stars](https://img.shields.io/github/stars/leopard627/fire-your-seo-agency?style=flat&label=%E2%98%85) - Claude Code skill that audits SEO, AEO, GEO and Naver search by itself. README is partly in Korean. _(MIT)_
- [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) ![stars](https://img.shields.io/github/stars/onvoyage-ai/gtm-engineer-skills?style=flat&label=%E2%98%85) - Claude Code skill that scores a site for AEO and GEO and suggests fixes for your framework. _(MIT)_
- [Ryze-AI-Adgent/open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) ![stars](https://img.shields.io/github/stars/Ryze-AI-Adgent/open-seo-mcp-skills?style=flat&label=%E2%98%85) - Free SEO MCP server and skills for keyword research, audits and AI visibility. The MCP endpoint is hosted by the author. _(MIT)_
- [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) ![stars](https://img.shields.io/github/stars/zubair-trabzada/geo-seo-claude?style=flat&label=%E2%98%85) - Claude Code skill focused on AI search: citability scoring, AI crawler checks, schema and PDF reports. _(MIT)_

## Self-hosted SEO platforms

Bigger open-source alternatives to paid SEO suites. Some cover AI search, some do not. Check what each actually ships.

- [beyondtahir/beyondseo](https://github.com/beyondtahir/beyondseo) ![stars](https://img.shields.io/github/stars/beyondtahir/beyondseo?style=flat&label=%E2%98%85) - SEO suite with native crawling, SEO/AEO/GEO checks, content and competitor tools. The native engine needs no API keys. _(MIT)_
- [CorgiCorner/bisibility](https://github.com/CorgiCorner/bisibility) ![stars](https://img.shields.io/github/stars/CorgiCorner/bisibility?style=flat&label=%E2%98%85) - Open-source SEO platform: Google rank tracking, keyword research and backlink checks. _(AGPL-3.0)_
- [crawlseo/crawlseo](https://github.com/crawlseo/crawlseo) ![stars](https://img.shields.io/github/stars/crawlseo/crawlseo?style=flat&label=%E2%98%85) - Open-source SEO monitoring: Search Console, site crawler and Core Web Vitals in one dashboard. _(MIT)_
- [every-app/open-seo](https://github.com/every-app/open-seo) ![stars](https://img.shields.io/github/stars/every-app/open-seo?style=flat&label=%E2%98%85) - Open-source alternative to Semrush and Ahrefs. _(MIT)_
- [karust/openserp](https://github.com/karust/openserp) ![stars](https://img.shields.io/github/stars/karust/openserp?style=flat&label=%E2%98%85) - Self-hosted search results API for Google, Bing, DuckDuckGo and others. Useful as a building block for SEO tools. _(MIT)_
- [SelmiAbderrahim/rankme.fast](https://github.com/SelmiAbderrahim/rankme.fast) ![stars](https://img.shields.io/github/stars/SelmiAbderrahim/rankme.fast?style=flat&label=%E2%98%85) - Self-hosted SEO platform. _(AGPL-3.0)_

## Research, playbooks and specs

Reading material and research code. Good for learning what actually moves AI citations.

- [AgriciDaniel/flow](https://github.com/AgriciDaniel/flow) ![stars](https://img.shields.io/github/stars/AgriciDaniel/flow?style=flat&label=%E2%98%85) - Documentation playbook for SEO in the AI-search era: 72 docs, prompts and diagrams. CC BY 4.0. _(check repo)_
- [AIcling/agentic_geo](https://github.com/AIcling/agentic_geo) ![stars](https://img.shields.io/github/stars/AIcling/agentic_geo?style=flat&label=%E2%98%85) - Research code for AgenticGEO, a self-improving system for generative engine optimization. _(Apache-2.0)_
- [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) ![stars](https://img.shields.io/github/stars/cxcscmu/AutoGEO?style=flat&label=%E2%98%85) - ICLR 2026 research code that learns what generative engines prefer and rewrites content to match. _(MIT)_
- [jdevalk/specification.website](https://github.com/jdevalk/specification.website) ![stars](https://img.shields.io/github/stars/jdevalk/specification.website?style=flat&label=%E2%98%85) - Sourced website spec covering HTML, accessibility, security, SEO and agent-readiness. _(check repo)_
- [TraceCohenTech/ai-seo-playbook](https://github.com/TraceCohenTech/ai-seo-playbook) ![stars](https://img.shields.io/github/stars/TraceCohenTech/ai-seo-playbook?style=flat&label=%E2%98%85) - Playbook with scripts and methods from one site's SEO and GEO results. Numbers are the author's own claims. _(MIT)_

## Other awesome lists

Related lists worth a look. This list does not try to replace them.

- [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) ![stars](https://img.shields.io/github/stars/amplifying-ai/awesome-generative-engine-optimization?style=flat&label=%E2%98%85) - Curated GEO guides, tools and research. _(check repo)_
- [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) ![stars](https://img.shields.io/github/stars/DavidHuji/Awesome-GEO?style=flat&label=%E2%98%85) - Awesome list focused on GEO research papers. _(check repo)_
- [discoveredlabs/awesome-aeo-seo](https://github.com/discoveredlabs/awesome-aeo-seo) ![stars](https://img.shields.io/github/stars/discoveredlabs/awesome-aeo-seo?style=flat&label=%E2%98%85) - Curated AEO and SEO resources for engineers and growth people. _(check repo)_
- [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) ![stars](https://img.shields.io/github/stars/luka2chat/awesome-geo?style=flat&label=%E2%98%85) - Curated list of GEO resources for ChatGPT, Perplexity, Claude and Google AI Overviews. _(CC0-1.0)_
- [RankSpotAI/awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools) ![stars](https://img.shields.io/github/stars/RankSpotAI/awesome-geo-tools?style=flat&label=%E2%98%85) - GEO and AI visibility tools compared by engines tracked, refresh rate, cost and data export. Includes paid tools. _(CC0-1.0)_
- [serpapi/awesome-seo-tools](https://github.com/serpapi/awesome-seo-tools) ![stars](https://img.shields.io/github/stars/serpapi/awesome-seo-tools?style=flat&label=%E2%98%85) - Curated list of SEO tools, from the SerpApi team. _(check repo)_

## How to choose

- **I just want to know if my site is OK for AI search:** start with an audit tool from the first section. Run two and compare.
- **I want to know if AI actually mentions my brand:** use a tracker. Budget for API costs, and run it weekly, not once.
- **I use WordPress:** try a plugin from the plugins section, but read what it changes before you enable it.
- **I already use a coding agent:** install one skill, not five. Skills overlap a lot.
- **I run a docs site:** an llms.txt generator for your framework is a cheap, low-risk step.
- **Be careful:** many repos here are young and move fast. Check the last commit, read the open issues, and test on a staging copy before pointing any auto-fixer at a live site.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md). Short version: open a pull request, one repo per PR, use the template. Real repos only, written in plain words.

## About

Maintained by [@devanasolver](https://github.com/devanasolver), who also builds [AIRankWP](https://airankwp.com), a WordPress plugin for AI-search visibility. Listings are decided by the criteria in CONTRIBUTING, not by who owns the repo.

## Support

If you find this project useful, [buy me a coffee](https://buymeacoffee.com/isaac49).
