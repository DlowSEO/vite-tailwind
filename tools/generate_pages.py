"""Generates every page of claudeseo.co.uk (SEO Agent) into a Vite src dir."""
import html
import json
import os
import sys

SRC = sys.argv[1]
SITE = "https://claudeseo.co.uk"
BRAND = "SEO Agent"
PRICE = "£50"
CHECKOUT_URL = "https://buy.polar.sh/polar_cl_qcL72PBFuDVPWsmHSPnYMhOlt9ReVeisiUBfL277yFD"
SUPPORT_EMAIL = "dan@claudeseo.co.uk"
LITE_REPO = "https://github.com/DlowSEO/seo-agent-lite"
LITE_SLUG = "DlowSEO/seo-agent-lite"
PRO_SLUG = "DlowSEO/seo-agent-pro"
REPO = LITE_REPO
UPDATED = "2026-09-26"

e = html.escape

H2 = "mb-4 text-sm font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400"
P = "text-slate-600 dark:text-slate-400"
PRE = "overflow-x-auto rounded-xl bg-slate-900 p-5 text-sm text-slate-100 dark:bg-black"
CARD = "rounded-xl border border-slate-200 p-5 dark:border-slate-800"
LINK = "font-medium text-slate-900 underline underline-offset-2 dark:text-white"

GITHUB_SVG = (
    '<svg class="h-4 w-4" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">'
    '<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>'
)

NAVLINK = "text-sm font-medium transition"
BTN = 'class="rounded-lg border border-blue-500/30 bg-blue-600 px-5 py-2.5 text-sm font-medium text-white shadow-lg shadow-blue-600/30 transition hover:bg-blue-500 dark:border-blue-400/30 dark:bg-[#040c1f] dark:text-blue-50 dark:shadow-blue-500/20 dark:hover:bg-[#0a1530]"'
BTN2 = 'class="rounded-lg border border-slate-200 px-5 py-2.5 text-sm font-medium text-slate-700 transition hover:border-slate-400 dark:border-slate-700 dark:text-slate-300 dark:hover:border-slate-500"'
NAV_IDLE = "text-slate-600 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white"
NAV_ON = "text-slate-900 dark:text-white"


def header(active):
    def cls(href):
        return f"{NAVLINK} {NAV_ON if active.startswith(href) else NAV_IDLE}"

    def cur(href):
        return ' aria-current="page"' if active == href else ""

    items = "".join(
        f'<a href="/commands/{x["slug"]}/" class="block rounded-lg px-3 py-2 hover:bg-slate-100 dark:hover:bg-slate-800"{cur("/commands/" + x["slug"] + "/")}>'
        f'<span class="flex items-center justify-between gap-2 font-mono text-xs text-slate-900 dark:text-white">{e(x["cmd"])}{tier_tag(x, small=True)}</span>'
        f'<span class="block text-xs text-slate-500 dark:text-slate-400">{e(x["name"])}</span></a>'
        for x in COMMANDS
    )
    return f"""
      <header class="relative z-20 flex flex-wrap items-center justify-between gap-4 py-6">
        <a href="/" class="flex items-center gap-2 font-semibold tracking-tight text-slate-900 dark:text-white">
          <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-slate-900 text-sm text-white dark:bg-white dark:text-slate-900">⌁</span>
          <span>SEO Agent <span class="hidden text-xs font-normal text-slate-500 sm:inline dark:text-slate-400">for Claude Code</span></span>
        </a>
        <nav class="flex flex-wrap items-center gap-x-5 gap-y-3" aria-label="Main">
          <details class="nav-menu relative">
            <summary class="{cls('/commands/')} flex cursor-pointer list-none items-center gap-1">
              Commands
              <svg class="h-3 w-3 transition" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5"/></svg>
            </summary>
            <div class="absolute left-0 z-30 mt-3 w-64 rounded-xl border border-slate-200 bg-white p-2 shadow-xl shadow-slate-900/10 sm:right-0 sm:left-auto dark:border-slate-800 dark:bg-slate-900">
              <a href="/commands/" class="block rounded-lg px-3 py-2 text-sm font-semibold text-slate-900 hover:bg-slate-100 dark:text-white dark:hover:bg-slate-800"{cur("/commands/")}>All commands</a>
              <div class="my-1 border-t border-slate-200 dark:border-slate-800"></div>
              {items}
            </div>
          </details>
          <a href="/integrations/" class="{cls('/integrations/')}"{cur("/integrations/")}>Integrations</a>
          <a href="/pricing/" class="{cls('/pricing/')}"{cur("/pricing/")}>Pricing</a>
          <a href="/install/" class="{cls('/install/')}"{cur("/install/")}>Install</a>
          <a href="/faq/" class="{cls('/faq/')}"{cur("/faq/")}>FAQ</a>
          <a href="/pricing/" class="rounded-lg border border-blue-500/30 bg-blue-600 px-3.5 py-1.5 text-sm font-medium text-white shadow-md shadow-blue-600/30 transition hover:bg-blue-500 dark:border-blue-400/30 dark:bg-[#040c1f] dark:text-blue-50 dark:shadow-blue-500/20 dark:hover:bg-[#0a1530]">Get Pro</a>
        </nav>
      </header>"""


def footer():
    fl = "text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white"
    fh = "mb-3 text-xs font-semibold uppercase tracking-wide text-slate-900 dark:text-white"
    cmds = "".join(f'<li><a href="/commands/{x["slug"]}/" class="{fl}">{e(x["name"])}</a></li>' for x in COMMANDS)
    return f"""
      <footer class="border-t border-slate-200 py-12 text-sm dark:border-slate-800">
        <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-5">
          <div class="lg:col-span-1">
            <a href="/" class="flex items-center gap-2 font-semibold tracking-tight text-slate-900 dark:text-white">
              <span class="flex h-7 w-7 items-center justify-center rounded-lg bg-slate-900 text-xs text-white dark:bg-white dark:text-slate-900">⌁</span>
              SEO Agent
            </a>
            <p class="mt-3 text-slate-500 dark:text-slate-400">Client-ready SEO audits for Claude Code. Built by Dan Lowry.</p>
            <a href="https://linkedin.com/in/dan-lowry-seo" target="_blank" rel="noopener noreferrer" class="mt-3 inline-block {fl}">LinkedIn</a>
          </div>
          <div class="lg:col-span-2">
            <h2 class="{fh}">Commands</h2>
            <ul class="grid grid-cols-2 gap-x-6 gap-y-2">{cmds}</ul>
          </div>
          <div>
            <h2 class="{fh}">Product</h2>
            <ul class="flex flex-col gap-2">
              <li><a href="/pricing/" class="{fl}">Pricing</a></li>
              <li><a href="/download/" class="{fl}">Download Lite</a></li>
              <li><a href="/install/" class="{fl}">Install Pro</a></li>
              <li><a href="/commands/" class="{fl}">All commands</a></li>
              <li><a href="/integrations/" class="{fl}">Integrations</a></li>
              <li><a href="/faq/" class="{fl}">FAQ</a></li>
              <li><a href="{LITE_REPO}" target="_blank" rel="noopener noreferrer" class="{fl}">Lite on GitHub</a></li>
            </ul>
          </div>
          <div>
            <h2 class="{fh}">Legal</h2>
            <ul class="flex flex-col gap-2">
              <li><a href="/terms/" class="{fl}">Terms and licence</a></li>
              <li><a href="/refunds/" class="{fl}">Refund policy</a></li>
              <li><a href="/privacy/" class="{fl}">Privacy policy</a></li>
              <li><a href="mailto:{SUPPORT_EMAIL}" class="{fl}">{SUPPORT_EMAIL}</a></li>
            </ul>
          </div>
        </div>
        <p class="mt-10 text-xs text-slate-400 dark:text-slate-500">SEO Agent is an independent product and is not affiliated with or endorsed by Anthropic. Claude and Claude Code are trademarks of Anthropic.</p>
      </footer>"""


def tier_tag(cmd, small=False):
    size = "px-1.5 py-0 text-[10px]" if small else "px-2.5 py-0.5 text-xs"
    if cmd.get("lite"):
        return f'<span class="rounded-full border border-emerald-500/30 bg-emerald-500/10 font-sans font-medium text-emerald-700 {size} dark:text-emerald-300">Lite + Pro</span>'
    return f'<span class="rounded-full border border-blue-500/30 bg-blue-500/10 font-sans font-medium text-blue-700 {size} dark:text-blue-300">Pro</span>'


def breadcrumbs(crumbs):
    items = [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + path}
        for i, (path, name) in enumerate(crumbs)
    ]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    visible = " / ".join(
        f'<a href="{p}" class="hover:text-slate-900 dark:hover:text-white">{e(n)}</a>' if i < len(crumbs) - 1 else f'<span class="text-slate-700 dark:text-slate-300">{e(n)}</span>'
        for i, (p, n) in enumerate(crumbs)
    )
    return (
        f'<script type="application/ld+json">{json.dumps(ld)}</script>',
        f'<nav class="pt-6 text-xs text-slate-500 dark:text-slate-400" aria-label="Breadcrumb">{visible}</nav>',
    )


def page(path, title, desc, active, crumbs, body, noindex=False, extra_ld=None):
    ld, crumb_html = breadcrumbs(crumbs) if crumbs else ("", "")
    if extra_ld:
        ld += f'<script type="application/ld+json">{json.dumps(extra_ld)}</script>'
    robots = '<meta name="robots" content="noindex" />\n    ' if noindex else ""
    doc = f"""<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{e(desc)}" />
    {robots}<link rel="canonical" href="{SITE}{path}" />
    <meta property="og:title" content="{e(title)}" />
    <meta property="og:description" content="{e(desc)}" />
    <meta property="og:url" content="{SITE}{path}" />
    <meta property="og:type" content="website" />
    <script>document.documentElement.classList.add("js")</script>
    <link rel="stylesheet" href="/style.css" />
    <script type="speculationrules">{{"prerender":[{{"where":{{"and":[{{"href_matches":"/*"}},{{"not":{{"href_matches":"/thanks/*"}}}}]}},"eagerness":"moderate"}}]}}</script>
    <meta name="google-site-verification" content="P4cbHF4VZsLHwY0dEidj9pTNeCHEstbpvItpHZT1vc0" />
    <script defer src="https://cloud.umami.is/script.js" data-website-id="bea2206c-f922-4e5a-a74a-1ec89a546785"></script>
    <title>{e(title)}</title>
    {ld}
  </head>
  <body class="min-h-screen bg-white font-inter text-base font-normal text-slate-800 dark:bg-slate-950 dark:text-slate-200">
    <div id="cursor-glow" class="pointer-events-none fixed inset-0 -z-10" aria-hidden="true"></div>
    <div class="mx-auto flex max-w-5xl flex-col px-6">
      {header(path)}
      <main>
      {crumb_html}
      {body}
      </main>
      {footer()}
    </div>
    <script type="module" src="/main.js"></script>
  </body>
</html>
"""
    out = os.path.join(SRC, path.strip("/"), "index.html") if path != "/" else os.path.join(SRC, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(doc)
    return None if noindex else path


def hero(eyebrow, h1, lead, tag=""):
    return f"""
      <section class="flex flex-col gap-5 py-14 sm:py-20">
        <div class="flex flex-wrap items-center gap-2"><span class="w-fit rounded-full border border-slate-200 px-3 py-1 font-mono text-xs text-slate-500 dark:border-slate-700 dark:text-slate-400">{e(eyebrow)}</span>{tag}</div>
        <h1 class="max-w-3xl text-4xl font-semibold tracking-tight text-slate-900 sm:text-5xl dark:text-white">{e(h1)}</h1>
        <p class="max-w-2xl text-lg {P}">{lead}</p>
      </section>"""


def section(title, inner, sid=None):
    idattr = f' id="{sid}"' if sid else ""
    return f"""
      <section{idattr} class="reveal scroll-mt-10 pb-16">
        <h2 class="{H2}">{e(title)}</h2>
        {inner}
      </section>"""


def code(text):
    return f'<pre class="{PRE}"><code>{e(text)}</code></pre>'


def ul(items):
    lis = "".join(f'<li class="flex gap-3"><span class="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-emerald-500"></span><span>{i}</span></li>' for i in items)
    return f'<ul class="flex flex-col gap-3 {P}">{lis}</ul>'


def table(rows, head=None, mono_first=True):
    # Two column tables stack into label/value pairs on phones; wider tables
    # tighten their padding and wrap instead of forcing the page wider.
    stack = len(rows[0]) == 2
    cell = "block px-5 sm:table-cell sm:py-3" if stack else "px-3 py-3 sm:px-5"
    thead = ""
    if head:
        ths = "".join(f'<th class="px-3 py-3 font-semibold text-slate-900 sm:px-5 dark:text-white">{e(h)}</th>' for h in head)
        hide = " hidden sm:table-header-group" if stack else ""
        thead = f'<thead class="border-b border-slate-200 bg-slate-50 dark:border-slate-800 dark:bg-slate-900{hide}"><tr>{ths}</tr></thead>'
    trs = []
    for i, row in enumerate(rows):
        border = "" if i == len(rows) - 1 else ' class="border-b border-slate-200 dark:border-slate-800"'
        tds = []
        for j, val in enumerate(row):
            pad = (" pt-3 pb-0.5" if j == 0 else " pt-0.5 pb-3") if stack else ""
            if j == 0 and mono_first:
                tds.append(f'<td class="{cell}{pad} font-mono break-words text-slate-900 sm:whitespace-nowrap dark:text-white">{val}</td>')
            elif j == 0 and stack:
                tds.append(f'<td class="{cell}{pad} font-medium text-slate-900 sm:font-normal sm:text-slate-600 dark:text-white sm:dark:text-slate-400">{val}</td>')
            else:
                tds.append(f'<td class="{cell}{pad} text-slate-600 dark:text-slate-400">{val}</td>')
        trs.append(f"<tr{border}>{''.join(tds)}</tr>")
    return f'<div class="overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800"><table class="w-full border-collapse text-left text-sm">{thead}<tbody>{"".join(trs)}</tbody></table></div>'


def steps(items):
    out = []
    for n, (t, d) in enumerate(items, 1):
        out.append(f"""<li class="{CARD} flex gap-4">
          <span class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-slate-900 text-xs font-semibold text-white dark:bg-white dark:text-slate-900">{n}</span>
          <div><h3 class="font-semibold text-slate-900 dark:text-white">{e(t)}</h3><p class="mt-1 text-sm {P}">{d}</p></div>
        </li>""")
    return f'<ol class="grid gap-4 sm:grid-cols-2">{"".join(out)}</ol>'


def faq_list(items):
    out = []
    for q, a in items:
        out.append(f"""<details class="group rounded-xl border border-slate-200 p-5 dark:border-slate-800">
          <summary class="flex cursor-pointer list-none items-center justify-between gap-4 font-medium text-slate-900 dark:text-white">{e(q)}<span class="text-slate-400 transition group-open:rotate-45">+</span></summary>
          <div class="mt-3 text-sm leading-relaxed {P}">{a}</div>
        </details>""")
    return f'<div class="flex flex-col gap-3">{"".join(out)}</div>'


def cta():
    return f"""
      <section class="mb-20 rounded-2xl border border-slate-200 p-8 text-center dark:border-slate-800 dark:bg-slate-900/40">
        <h2 class="text-2xl font-semibold tracking-tight text-slate-900 dark:text-white">Client-ready audits for a one-time payment</h2>
        <p class="mx-auto mt-3 max-w-xl {P}">SEO Agent Pro unlocks all eight commands, full audits and branded PDF reports. No subscription, and a 14-day refund if it is not for you.</p>
        <div class="mt-6 flex flex-wrap justify-center gap-3">
          <a href="/pricing/" {BTN}>Get SEO Agent Pro</a>
          <a href="/download/" {BTN2}>Try Lite free</a>
        </div>
      </section>"""


def c(t):
    return f'<code class="rounded bg-slate-100 px-1.5 py-0.5 font-mono text-[0.85em] text-slate-900 dark:bg-slate-800 dark:text-slate-100">{e(t)}</code>'


# ---------------------------------------------------------------- commands
COMMANDS = [
    {
        "slug": "audit",
        "lite": "Lite runs Snapshot audits of up to 10 pages. Pro unlocks Full audits of up to 500 pages, every specialist and the PDF report.",
        "cmd": "/seo audit <url>",
        "name": "Full site audit",
        "short": "Full site audit: crawl, parallel specialists, health score, action plan",
        "title": "/seo audit: full website SEO audit in Claude Code | SEO Agent",
        "desc": "Run a full website SEO audit from Claude Code. Crawls up to 500 pages, runs specialist agents in parallel and returns a 0 to 100 health score with a prioritised action plan.",
        "h1": "A full SEO audit, from crawl to action plan",
        "lead": "One command renders your homepage, crawls the site, hands each area to a specialist agent and brings everything back as a scored report with a prioritised list of fixes.",
        "usage": "/seo audit https://example.com\n/seo audit https://example.com --mode snapshot\n/seo audit https://example.com --mode full",
        "when": [
            "You are taking on a new site and need the whole picture before deciding where to start.",
            "You want a repeatable baseline to measure improvements against after a round of fixes.",
            f"You only need one page checked? Use {c('/seo analyse')} instead, it is faster and more focused.",
        ],
        "steps": [
            ("Render", "Captures raw HTML, rendered HTML, extracted text and whether the site is a JavaScript single page app."),
            ("Detect and crawl", "Works out the business type from homepage signals, then follows internal links up to the page cap while respecting robots.txt."),
            ("Delegate", "Hands technical, content, performance, visual and AI search checks to specialist agents running in parallel. Local, Google and backlink specialists join when the site or your credentials call for them."),
            ("Score", "Rolls findings up into seven weighted categories and a single 0 to 100 health score."),
            ("Save", f"Writes the report, action plan, structured data and screenshots into a {c('{domain}-audit/')} folder."),
            ("Report", "Produces an action plan ordered Critical, High, Medium, Low, with an optional PDF for sharing."),
        ],
        "extra": lambda: section(
            "Snapshot or full audit",
            table(
                [
                    ["Best for", "A quick read on a smaller site", "Larger or e-commerce sites"],
                    ["Crawl cap", "50 pages", "500 pages"],
                    ["Findings", "Top 3 to 5 per specialist", "Complete findings list"],
                    ["Report length", "Up to 10 pages", "No cap"],
                    ["Action plan", "Critical and High items", "All four phases"],
                ],
                head=["", "Snapshot", "Full"],
                mono_first=False,
            )
            + f'<p class="mt-3 text-sm {P}">If you do not pass {c("--mode")}, the audit asks which one you want before it starts crawling.</p>',
        )
        + section(
            "How the health score is weighted",
            table(
                [
                    ["Content quality", "23%"],
                    ["Technical SEO", "22%"],
                    ["On-page SEO", "20%"],
                    ["Schema and structured data", "10%"],
                    ["Performance (Core Web Vitals)", "10%"],
                    ["AI search readiness", "10%"],
                    ["Images", "5%"],
                ],
                head=["Category", "Weight"],
                mono_first=False,
            )
            + f'<p class="mt-3 text-sm {P}">The score is a way to prioritise work, not a prediction of how Google will rank the site.</p>',
        ),
        "outputs": [
            ["FULL-AUDIT-REPORT.md", "Executive summary, health score and findings by category"],
            ["ACTION-PLAN.md", "Fixes grouped by priority and phase"],
            ["audit-data.json", "Structured data used to build the PDF report"],
            ["findings/*.md", "Evidence from each specialist"],
            ["screenshots/", "Desktop and mobile captures, when Chromium is available"],
            ["PDF report", "Optional A4 report with charts and a roadmap"],
        ],
        "notes": [
            "Every finding must name the affected URLs and show the value actually found. Generic advice that would apply to any site is cut.",
            "The audit reads your public site and writes local files only. It never changes the site being audited.",
            "Core Web Vitals from a crawl are lab data. Connect Google APIs for real field data.",
            "Pages blocked by robots.txt, logins or bot protection cannot be assessed.",
        ],
        "related": ["analyse", "content", "google"],
    },
    {
        "slug": "analyse",
        "lite": "Lite runs the standard single-page analysis. Pro adds every focus mode: technical, schema, sitemap, images and hreflang.",
        "cmd": "/seo analyse <url>",
        "name": "Page and technical analysis",
        "short": "Page and technical analysis (technical, schema, sitemap, images, hreflang)",
        "title": "/seo analyse: page and technical SEO analysis | SEO Agent",
        "desc": "Analyse a single URL for on-page and technical SEO in Claude Code, or focus on technical SEO, schema, XML sitemaps, images or hreflang with one flag.",
        "h1": "Page and technical SEO, one URL at a time",
        "lead": "A focused inspection of a single page covering on-page elements, technical health, structured data, images and performance. Add a focus flag to go deep on one area.",
        "usage": "/seo analyse https://example.com/pricing\n/seo analyse https://example.com --focus technical\n/seo analyse https://example.com --focus schema",
        "when": [
            "You have just published or changed a page and want to check it before it is crawled.",
            "An audit flagged a problem area and you want the detail for one page.",
            "You need JSON-LD generated, a sitemap reviewed or hreflang validated.",
        ],
        "extra": lambda: section(
            "Focus modes",
            table(
                [
                    ["--focus technical", "Crawlability, indexability, security, URL structure, mobile, Core Web Vitals, structured data, JavaScript rendering and IndexNow"],
                    ["--focus schema", "Detects and validates Schema.org markup against Google's requirements and generates JSON-LD"],
                    ["--focus sitemap", "Reviews XML sitemaps and generates new ones from industry templates"],
                    ["--focus images", "Alt text, file formats, responsive images, lazy loading and layout shift prevention"],
                    ["--focus hreflang", "Audits, validates and generates hreflang for international sites"],
                ],
                head=["Flag", "What it covers"],
            ),
        ),
        "checks": [
            "Title tag, meta description, headings and internal links",
            "Canonical tags, indexability and robots directives",
            "Security headers, HTTPS and mobile rendering",
            "Existing schema, validation errors and missing opportunities",
            "Image weight, format and alt text",
        ],
        "outputs": [
            ["Single report", "Findings ordered Critical, High, Medium, Low"],
            ["Evidence", "The exact values found on the page for every issue"],
            ["Fixes", "Specific changes, including ready to paste JSON-LD where relevant"],
        ],
        "notes": [
            "One command covers what would otherwise be six separate checks: page, technical, schema, sitemap, images and hreflang.",
            f"For a whole site, run {c('/seo audit')} first and use this command to dig into individual pages.",
        ],
        "related": ["audit", "content", "geo"],
    },
    {
        "slug": "content",
        "cmd": "/seo content <url>",
        "name": "Content quality and briefs",
        "short": "E-E-A-T content analysis, plus content briefs by topic",
        "title": "/seo content: E-E-A-T analysis and content briefs | SEO Agent",
        "desc": "Assess content quality against Google's E-E-A-T guidelines, find thin content and check AI citation readiness, or generate a competitive content brief for any topic.",
        "h1": "Judge the content you have, brief the content you need",
        "lead": "Two modes of one job. Point it at a URL to assess experience, expertise, authority and trust. Give it a topic to get a competitive brief with word counts for each section.",
        "usage": "/seo content https://example.com/blog/guide\n/seo content brief \"best running shoes for flat feet\"\n/seo content brief \"pricing page\" https://example.com/pricing",
        "when": [
            "A page is indexed but not ranking and you suspect the content is the problem.",
            "You are planning new content and want a brief based on what currently ranks.",
            "You want to improve an existing page, pass the URL and a topic for an improvement brief.",
        ],
        "checks": [
            "E-E-A-T signals based on Google's Search Quality Rater Guidelines",
            "Thin and duplicate content",
            "Readability and depth compared with competing pages",
            "AI citation readiness: clear, quotable, self-contained answers",
        ],
        "outputs": [
            ["Content report", "Scores and evidence for each quality signal"],
            ["Content brief", "Outline with per-section word counts, keywords and competitor scoring"],
            ["Page templates", "Structures for common page types"],
        ],
        "notes": [
            "When an analysis finds gaps, it offers an improvement brief for the same URL. That loop is the intended workflow.",
            "Briefs guide writers. They are not a substitute for first-hand expertise on the topic.",
        ],
        "related": ["audit", "geo", "strategy"],
    },
    {
        "slug": "local",
        "cmd": "/seo local <url>",
        "name": "Local SEO and maps",
        "short": "Local SEO: GBP, NAP, citations, reviews, geo-grid",
        "title": "/seo local: local SEO and Google Business Profile audit | SEO Agent",
        "desc": "Audit local SEO from Claude Code: Google Business Profile, NAP consistency, citations, reviews, local schema, location pages and geo-grid rank tracking.",
        "h1": "Local SEO and map pack visibility",
        "lead": "Everything location based in one command, from Google Business Profile completeness and NAP consistency to reviews, citations and geo-grid rankings.",
        "usage": "/seo local https://example.com\n/seo local \"Example Plumbing Manchester\"",
        "when": [
            "The business serves customers in a physical area: shops, trades, clinics, offices.",
            "Map pack rankings have dropped or vary a lot across the service area.",
            "You manage several locations and need to check consistency between them.",
        ],
        "checks": [
            "Google Business Profile completeness",
            "Name, address and phone consistency across the web",
            "Citation health and review signals, including sentiment",
            "LocalBusiness schema and location page quality",
            "Geo-grid rank tracking and competitor radius mapping, where API access allows",
        ],
        "outputs": [
            ["Local SEO report", "Findings with evidence, ordered by severity"],
            ["Map data", "Grids and radius maps included as evidence within the report"],
        ],
        "notes": [
            f"Also runs automatically inside {c('/seo audit')} when a local business is detected.",
            "Deeper review intelligence and geo-grid data depend on the APIs you connect.",
        ],
        "related": ["audit", "google", "backlinks"],
    },
    {
        "slug": "geo",
        "cmd": "/seo geo <url>",
        "name": "AI search readiness",
        "short": "AI Overviews, ChatGPT and Perplexity readiness",
        "title": "/seo geo: AI search and generative engine optimisation | SEO Agent",
        "desc": "Check how ready a site is to be cited by Google AI Overviews, ChatGPT search and Perplexity. Scores citability, structure, AI crawler access and brand signals.",
        "h1": "Get cited in AI answers",
        "lead": "Generative engine optimisation checks for Google AI Overviews, AI Mode, ChatGPT search and Perplexity. It treats AI search as SEO fundamentals applied to new surfaces, which is Google's own position.",
        "usage": "/seo geo https://example.com\n/seo geo https://example.com/guides/topic",
        "when": [
            "Traffic from classic results is flat while AI answers take more space on the results page.",
            "Competitors are being cited in AI answers for your topics and you are not.",
            "You want to know whether AI crawlers can reach your content at all.",
        ],
        "checks": [
            "Citability: self-contained passages, clear definitions and specific facts",
            "Structure: heading hierarchy, question led headings, lists and tables",
            "Multi-modal content: images, video and data visuals",
            "Authority and brand mention signals across the web",
            "AI crawler access in robots.txt and llms.txt status",
        ],
        "outputs": [
            ["GEO report", "Scores for each criterion with passage level evidence"],
            ["Rewrites", "Suggested changes to make key passages easier to cite"],
        ],
        "notes": [
            "Where community advice contradicts Google's published guidance, the report follows Google and notes the difference.",
            "Nobody can guarantee a citation. The aim is to remove the reasons a page would be passed over.",
        ],
        "related": ["content", "analyse", "audit"],
    },
    {
        "slug": "backlinks",
        "cmd": "/seo backlinks <url>",
        "name": "Backlink analysis",
        "short": "Backlink profile via free APIs",
        "title": "/seo backlinks: backlink profile analysis | SEO Agent",
        "desc": "Analyse a backlink profile in Claude Code using free data from Moz, Bing Webmaster Tools and Common Crawl: referring domains, anchor text, toxic links and competitor gaps.",
        "h1": "Backlink analysis without another subscription",
        "lead": "Referring domains, anchor text balance, toxic links and competitor gaps, built on free data sources. Add free Moz and Bing keys for richer data.",
        "usage": "/seo backlinks https://example.com\n/seo backlinks gap https://example.com https://competitor.com\n/seo backlinks toxic https://example.com\n/seo backlinks setup",
        "when": [
            "You want to understand why a competitor outranks you despite similar content.",
            "You suspect spammy or unnatural links and need a disavow shortlist.",
            "You are planning link building and need to know where the gaps are.",
        ],
        "extra": lambda: section(
            "Data sources",
            table(
                [
                    ["Common Crawl", "Always on", "Domain level rank and presence data"],
                    ["Verification crawler", "Always on", "Checks that known backlinks still exist"],
                    ["Moz API", "Free sign up", "Domain Authority, Page Authority, Spam Score, linking domains, anchors"],
                    ["Bing Webmaster Tools", "Free sign up", "Inbound links and anchor text"],
                ],
                head=["Source", "Access", "Provides"],
                mono_first=False,
            ),
        ),
        "outputs": [
            ["Profile overview", "Referring domains, follow ratio, diversity and trend"],
            ["Anchor text", "Distribution against healthy benchmarks"],
            ["Toxic links", "Flagged domains with disavow recommendations"],
            ["Link gap", "Domains linking to competitors but not to you"],
        ],
        "notes": [
            f"Run {c('/seo backlinks setup')} for step by step instructions on adding free API keys.",
            "Free sources see fewer links than paid tools, so treat counts as a floor rather than a total.",
        ],
        "related": ["audit", "strategy", "local"],
    },
    {
        "slug": "strategy",
        "cmd": "/seo strategy [mode]",
        "name": "SEO strategy and planning",
        "short": "Planning: cluster, programmatic, competitor pages, ecommerce",
        "title": "/seo strategy: SEO plans, topic clusters and programmatic SEO | SEO Agent",
        "desc": "Plan what to build next: industry SEO strategies and roadmaps, SERP overlap topic clusters, programmatic SEO, competitor comparison pages and e-commerce SEO.",
        "h1": "Plan what to build next",
        "lead": "Audits look at what exists. Strategy plans what to create: roadmaps, topic clusters, pages at scale, comparison pages and product SEO.",
        "usage": "/seo strategy plan saas\n/seo strategy cluster \"project management software\"\n/seo strategy programmatic\n/seo strategy competitor-pages\n/seo strategy ecommerce https://shop.example.com",
        "when": [
            "You have fixed the technical basics and need a content and growth roadmap.",
            "You want to build topical authority with a hub and spoke structure.",
            "You are considering hundreds of templated pages and want to avoid thin content.",
        ],
        "extra": lambda: section(
            "Modes",
            table(
                [
                    ["plan &lt;type&gt;", "Industry specific strategy, competitive analysis and an implementation roadmap"],
                    ["cluster &lt;seed&gt;", "Groups keywords by shared search results into hub and spoke clusters with internal linking"],
                    ["programmatic", "Templates, URL patterns and safeguards against thin content and index bloat"],
                    ["competitor-pages", "\"X vs Y\" and \"alternatives to X\" pages with feature comparisons"],
                    ["ecommerce &lt;url&gt;", "Product schema, Google Shopping visibility and marketplace keyword gaps"],
                ],
                head=["Mode", "What it produces"],
            ),
        ),
        "outputs": [
            ["Strategy documents", "Plan, site structure, content calendar and roadmap"],
            ["Cluster map", "Visual map of topics and how pages should link"],
        ],
        "notes": [
            "Modes are designed to chain: cluster output feeds a plan, and a plan can hand off to programmatic or competitor pages.",
            f"Audits recommend {c('/seo strategy')} rather than running it, so strategy stays a deliberate step.",
        ],
        "related": ["content", "audit", "backlinks"],
    },
    {
        "slug": "google",
        "cmd": "/seo google [cmd]",
        "name": "Google SEO APIs",
        "short": "GSC, PageSpeed Insights, CrUX, GA4, Indexing APIs",
        "title": "/seo google: Search Console, PageSpeed, CrUX and GA4 in Claude Code | SEO Agent",
        "desc": "Pull real Google data into Claude Code: Search Console performance and URL inspection, PageSpeed Insights, CrUX field data with 25 week history, GA4 organic traffic and the Indexing API.",
        "h1": "Real Google data, straight into your terminal",
        "lead": "Crawls tell you what a page looks like. Google's own APIs tell you how it performs: real Chrome user metrics, index status, search clicks and organic traffic. Google does not charge for these APIs.",
        "usage": "/seo google setup\n/seo google pagespeed https://example.com\n/seo google gsc sc-domain:example.com\n/seo google inspect https://example.com/page\n/seo google ga4",
        "when": [
            "You need field data for Core Web Vitals rather than a lab estimate.",
            "Pages are not appearing in search and you want Google's view of why.",
            "You want clicks, impressions and organic landing pages alongside audit findings.",
        ],
        "extra": lambda: section(
            "Access levels",
            table(
                [
                    ["API key", "PageSpeed, CrUX, CrUX history, YouTube, NLP, Knowledge Graph and Web Risk checks"],
                    ["+ service account", "Search Console performance, URL inspection, sitemaps and the Indexing API"],
                    ["+ GA4 property", "Organic traffic and top organic landing pages"],
                    ["+ Google Ads", "Keyword ideas and search volume from Keyword Planner"],
                ],
                head=["Credentials", "Unlocks"],
                mono_first=False,
            )
            + f'<p class="mt-3 text-sm {P}">Run {c("/seo google setup")} for step by step instructions to create a Google Cloud project and credentials.</p>',
        ),
        "outputs": [
            ["Performance data", "Lab and field Core Web Vitals for mobile and desktop"],
            ["Search data", "Clicks, impressions, CTR and position by query and page"],
            ["Index status", "Canonical, crawl and coverage details per URL"],
            ["Traffic data", "Organic sessions and landing pages from GA4"],
        ],
        "notes": [
            f"When credentials are present, {c('/seo audit')} brings in Google data automatically.",
            "Submitting URLs through the Indexing API does not guarantee they will be indexed.",
        ],
        "related": ["audit", "analyse", "local"],
    },
]
BY_SLUG = {x["slug"]: x for x in COMMANDS}


def command_page(cmd):
    body = hero(cmd["cmd"], cmd["h1"], cmd["lead"], tier_tag(cmd))
    body += section("Usage", code(cmd["usage"]))
    note = cmd.get("lite") or f"This command is part of SEO Agent Pro, a one-time purchase. <a href=\"/pricing/\" class=\"{LINK}\">Compare Lite and Pro</a>."
    if cmd.get("lite"):
        note += f' <a href="/pricing/" class="{LINK}">Compare Lite and Pro</a>.'
    body += f'<div class="-mt-8 mb-16 rounded-xl border border-blue-500/20 bg-blue-500/5 px-5 py-4 text-sm {P}">{note}</div>'
    body += section("When to use it", ul(cmd["when"]))
    if "steps" in cmd:
        body += section("What happens when it runs", steps(cmd["steps"]))
    if "checks" in cmd:
        body += section("What it checks", ul(cmd["checks"]))
    if "extra" in cmd:
        body += cmd["extra"]()
    body += section("What you get", table(cmd["outputs"], head=["Output", "Contents"]))
    body += section("Good to know", ul(cmd["notes"]))
    rel = "".join(
        f'<a href="/commands/{r}/" class="{CARD} block transition hover:border-slate-400 dark:hover:border-slate-600"><span class="font-mono text-sm text-slate-900 dark:text-white">{e(BY_SLUG[r]["cmd"])}</span><p class="mt-1 text-sm {P}">{e(BY_SLUG[r]["name"])}</p></a>'
        for r in cmd["related"]
    )
    body += section("Related commands", f'<div class="grid gap-4 sm:grid-cols-3">{rel}</div>')
    body += cta()
    return page(
        f"/commands/{cmd['slug']}/",
        cmd["title"],
        cmd["desc"],
        "/commands/",
        [("/", "Home"), ("/commands/", "Commands"), (f"/commands/{cmd['slug']}/", cmd["name"])],
        body,
    )


def commands_hub():
    cards = "".join(
        f"""<a href="/commands/{x['slug']}/" class="{CARD} group flex flex-col gap-2 transition hover:border-slate-400 dark:hover:border-slate-600">
          <span class="flex items-center justify-between font-mono text-xs text-slate-400">{i:02d}{tier_tag(x, small=True)}</span>
          <span class="font-mono text-sm font-semibold text-slate-900 dark:text-white">{e(x['cmd'])}</span>
          <span class="text-sm {P}">{e(x['lead'].split('. ')[0].rstrip('.'))}.</span>
          <span class="mt-auto pt-2 text-xs font-semibold uppercase tracking-wide text-blue-600 dark:text-blue-400">Learn more →</span>
        </a>"""
        for i, x in enumerate(COMMANDS, 1)
    )
    body = hero(
        "8 commands · 8 skills · 8 agents",
        "Every SEO Agent command",
        "Eight commands cover the whole job, from a full audit to strategy and Google data. Lite includes Snapshot audits and page analysis; Pro unlocks everything.",
    )
    body += section("All commands", f'<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">{cards}</div>')
    body += section(
        "Where to start",
        ul(
            [
                f"New to a site? Start with {c('/seo audit')} for the full picture and a prioritised action plan.",
                f"Checking one page? Use {c('/seo analyse')}, with a focus flag if you already know the problem area.",
                f"Planning growth? Use {c('/seo strategy')} once the technical basics are in place.",
                f"Have Google access? Run {c('/seo google setup')} so audits can use real field and search data.",
            ]
        ),
    )
    body += section(
        "Why SEO Agent",
        f'<p class="{P}">Other Claude SEO tools tend to grow into long lists of overlapping skills, and their output usually needs reworking before a client sees it. SEO Agent takes a different approach. It is built by an SEO with more than 12 years in the industry, keeps the whole job to eight commands, and produces audits that are ready to present: evidence-backed findings, a health score, a prioritised action plan and an optional PDF report.</p>',
    )
    body += cta()
    return page(
        "/commands/",
        "SEO Agent commands: 8 SEO commands for Claude Code",
        "All eight SEO Agent commands for Claude Code: full site audits, page and technical analysis, content, local SEO, AI search, backlinks, strategy and Google APIs.",
        "/commands/",
        [("/", "Home"), ("/commands/", "Commands")],
        body,
    )


# ---------------------------------------------------------------- install
CHIP = "rounded-full border px-2.5 py-0.5 text-xs font-medium"
CHIP_PLAT = f"{CHIP} border-slate-200 text-slate-600 dark:border-slate-700 dark:text-slate-300"
CHIP_REC = f"{CHIP} border-emerald-500/30 bg-emerald-500/10 text-emerald-700 dark:text-emerald-300"
ICON_APPLE = '<svg class="h-3 w-3" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M11.2 8.5c0-1.5 1.2-2.2 1.3-2.3-.7-1-1.8-1.2-2.2-1.2-.9-.1-1.8.6-2.3.6-.5 0-1.2-.5-2-.5-1 0-2 .6-2.5 1.6-1.1 1.9-.3 4.6.8 6.1.5.7 1.1 1.6 1.9 1.5.8 0 1.1-.5 2-.5s1.2.5 2 .5c.8 0 1.4-.8 1.9-1.5.6-.9.8-1.7.8-1.7s-1.7-.6-1.7-2.6ZM9.7 4c.4-.5.7-1.2.6-1.9-.6 0-1.4.4-1.8.9-.4.4-.7 1.1-.6 1.8.7.1 1.4-.3 1.8-.8Z"/></svg>'
ICON_LINUX = '<svg class="h-3 w-3" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="2" y="3" width="12" height="10" rx="2"/><path d="m5 7 2 1.5L5 10M8.5 10.5H11"/></svg>'
ICON_WIN = '<svg class="h-3 w-3" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M1 3.2 6.7 2.4v5.3H1V3.2Zm6.4-.9L15 1.2v6.5H7.4V2.3ZM1 8.3h5.7v5.3L1 12.8V8.3Zm6.4 0H15v6.5l-7.6-1.1V8.3Z"/></svg>'
ICON_CLAUDE = '<svg class="h-3 w-3" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="m4 5 3 3-3 3M8.5 11H12"/></svg>'


def chip(label, icon=""):
    return f'<span class="{CHIP_PLAT} inline-flex items-center gap-1.5">{icon}{label}</span>'


def homebrew_box():
    brew_install = code('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    brew_reqs = code("brew install git python\nbrew install --cask claude-code")
    return f"""<div class="rounded-2xl border border-slate-200 bg-slate-50 p-6 dark:border-slate-800 dark:bg-[#040c1f]">
      <div class="flex flex-wrap items-center gap-2">{chip("macOS", ICON_APPLE)}<span class="{CHIP} border-blue-500/30 bg-blue-500/10 text-blue-700 dark:text-blue-300">Optional</span></div>
      <h2 class="mt-3 text-xl font-semibold tracking-tight text-slate-900 dark:text-white">Recommended for Mac users: Homebrew</h2>
      <p class="mt-4 {P}">If you are on a Mac and do not already have Python, Git or Claude Code, <a href="https://brew.sh/" target="_blank" rel="noopener noreferrer" class="{LINK}">Homebrew</a> is the simplest way to get them. It is a free package manager that installs and updates tools with one short command each, which is especially handy if you do not use the terminal often.</p>
      <p class="mt-5 mb-2 text-sm font-medium text-slate-900 dark:text-white">1. Install Homebrew</p>
      {brew_install}
      <p class="mt-2 text-sm {P}">The installer explains what it will do before it starts. When it finishes, run the commands it shows under "Next steps" so the {c("brew")} command works in new terminal windows.</p>
      <p class="mt-5 mb-2 text-sm font-medium text-slate-900 dark:text-white">2. Install the requirements</p>
      {brew_reqs}
      <p class="mt-2 text-sm {P}">Then open Claude Code with {c("claude")}, sign in, and follow Option 1 or Option 2 below.</p>
      <p class="mt-5 border-t border-slate-200 pt-4 text-xs text-slate-500 dark:border-slate-800 dark:text-slate-400">Homebrew is a personal recommendation only. SEO Agent has no affiliation with Homebrew, and Homebrew is not needed to use SEO Agent. Current system requirements are listed on <a href="https://brew.sh/" target="_blank" rel="noopener noreferrer" class="underline underline-offset-2">brew.sh</a>.</p>
    </div>"""


OPTION_STYLE = os.environ.get("OPTION_STYLE", "terminal")


def option_head_chips(o):
    rec = f'<span class="{CHIP_REC}">Recommended</span>' if o["rec"] else ""
    return rec + "".join(chip(l, i) for l, i in o["plats"])


def render_option(o):
    body = o["body"]()
    chips = option_head_chips(o)
    if OPTION_STYLE == "terminal":
        return f"""<section id="{o['id']}" class="scroll-mt-10 pb-12">
        <div class="overflow-hidden rounded-2xl border border-slate-200 dark:border-slate-800">
          <div class="flex flex-wrap items-center gap-3 border-b border-slate-200 bg-slate-100 px-5 py-3 dark:border-slate-800 dark:bg-[#040c1f]">
            <span class="flex gap-1.5" aria-hidden="true"><span class="h-3 w-3 rounded-full bg-rose-400/80"></span><span class="h-3 w-3 rounded-full bg-amber-400/80"></span><span class="h-3 w-3 rounded-full bg-emerald-400/80"></span></span>
            <h2 class="font-mono text-sm text-slate-900 dark:text-white"><span class="text-slate-400">~/option-{o['n']}</span> {e(o['title'])}</h2>
            <div class="flex flex-wrap gap-2 sm:ml-auto">{chips}</div>
          </div>
          <div class="p-5 sm:p-6">{body}</div>
        </div>
      </section>"""
    if OPTION_STYLE == "rail":
        return f"""<section id="{o['id']}" class="scroll-mt-10 pb-14">
        <div class="border-l-2 border-blue-500/70 pl-5 sm:pl-7">
          <p class="font-mono text-xs font-medium tracking-wide text-blue-600 dark:text-blue-400">Option {o['n']}</p>
          <h2 class="mt-1 text-2xl font-semibold tracking-tight text-slate-900 dark:text-white">{e(o['title'])}</h2>
          <div class="mt-3 mb-5 flex flex-wrap gap-2">{chips}</div>
          {body}
        </div>
      </section>"""
    # default: numbered cards
    return f"""<section id="{o['id']}" class="scroll-mt-10 pb-8">
        <div class="rounded-2xl border border-slate-200 p-5 sm:p-7 dark:border-slate-800 dark:bg-slate-900/40">
          <div class="mb-5 flex flex-wrap items-start gap-4">
            <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl border border-blue-500/30 bg-blue-600 font-mono text-sm font-semibold text-white shadow-lg shadow-blue-600/30 dark:bg-[#040c1f] dark:text-blue-200 dark:shadow-blue-500/20">0{o['n']}</span>
            <div class="min-w-0 flex-1">
              <h2 class="text-xl font-semibold tracking-tight text-slate-900 dark:text-white">{e(o['title'])}</h2>
              <div class="mt-2 flex flex-wrap gap-2">{chips}</div>
            </div>
          </div>
          {body}
        </div>
      </section>"""


def install_options_for(product):
    """Install options for 'pro' (zip download) or 'lite' (public GitHub)."""
    if product == "pro":
        key_line = " At the end it asks for the licence key from your purchase email; you can also enter it later with " + c("/seo setup") + "."
        return [
            {
                "id": "unix", "n": 1, "title": "Install on macOS and Linux", "rec": True,
                "plats": [("macOS", ICON_APPLE), ("Linux", ICON_LINUX)],
                "body": lambda: f'<p class="mb-4 {P}">Download {c("seo-agent-pro.zip")} from your purchase email and unzip it (a Mac does this for you in Downloads). Then run these in your normal terminal (Terminal on a Mac):</p>'
                + code("cd ~/Downloads/seo-agent-pro\nbash install.sh")
                + f'<p class="mt-3 text-sm {P}">The installer copies SEO Agent into Claude Code\'s folders using {c("bash")}, which is built into macOS and Linux, so you can delete the download afterwards. It does not need Homebrew.{key_line}</p>',
            },
            {
                "id": "windows", "n": 2, "title": "Install on Windows", "rec": False,
                "plats": [("Windows PowerShell", ICON_WIN)],
                "body": lambda: f'<p class="mb-4 {P}">Download {c("seo-agent-pro.zip")} from your purchase email, right-click it and choose Extract All. Then run these in PowerShell:</p>'
                + code("cd $HOME\\Downloads\\seo-agent-pro\npowershell -ExecutionPolicy Bypass -File install.ps1")
                + f'<p class="mt-3 text-sm {P}">Have a look through {c("install.ps1")} before running it if you like.{key_line}</p>',
            },
            {
                "id": "plugin", "n": 3, "title": "Plugin install from the folder", "rec": False,
                "plats": [("Inside Claude Code", ICON_CLAUDE), ("macOS", ICON_APPLE), ("Linux", ICON_LINUX), ("Windows", ICON_WIN)],
                "body": lambda: f'<p class="mb-4 {P}">Prefer Claude Code\'s plugin manager? Move the unzipped {c("seo-agent-pro")} folder somewhere permanent, such as your home folder, then type these into Claude Code, using the folder\'s full path:</p>'
                + code(f"/plugin marketplace add /Users/yourname/seo-agent-pro\n/plugin install seo-agent-pro@{PRO_SLUG.lower().replace('/', '-')}\n/seo setup")
                + f'<p class="mt-3 text-sm {P}">Claude Code reads the plugin from that folder, so keep it where it is. {c("/seo setup")} creates the Python environment and asks for your licence key.</p>',
            },
        ]
    slug = LITE_SLUG
    name = slug.split("/")[1]
    plugin_id = f"{name}@{slug.lower().replace('/', '-')}"
    return [
        {
            "id": "plugin", "n": 1, "title": "Plugin install", "rec": True,
            "plats": [("Inside Claude Code", ICON_CLAUDE), ("macOS", ICON_APPLE), ("Linux", ICON_LINUX), ("Windows", ICON_WIN)],
            "body": lambda: f'<p class="mb-4 {P}">The quickest route, for Claude Code 1.0.33 and later. Type these into Claude Code itself, not your normal terminal:</p>'
            + code(f"/plugin marketplace add {slug}\n/plugin install {plugin_id}\n/seo setup")
            + f'<p class="mt-3 text-sm {P}">Installing the plugin does not run any package managers. {c("/seo setup")} is a one time step that creates the Python environment and browser in Claude\'s plugin data folder.</p>',
        },
        {
            "id": "unix", "n": 2, "title": "Manual install on macOS and Linux", "rec": False,
            "plats": [("macOS", ICON_APPLE), ("Linux", ICON_LINUX)],
            "body": lambda: f'<p class="mb-4 {P}">Run these in your normal terminal (Terminal on a Mac):</p>'
            + code(f"git clone --depth 1 https://github.com/{slug}.git\nbash {name}/install.sh")
            + f'<p class="mt-3 text-sm {P}">The first line downloads a copy of {BRAND} Lite into a folder called {c(name)}. The second runs the installer script inside that folder using {c("bash")}, which is built into macOS and Linux. Neither line needs Homebrew.</p>',
        },
        {
            "id": "windows", "n": 3, "title": "Manual install on Windows", "rec": False,
            "plats": [("Windows PowerShell", ICON_WIN)],
            "body": lambda: f'<p class="mb-4 {P}">Run these in PowerShell:</p>'
            + code(f"git clone --depth 1 https://github.com/{slug}.git\npowershell -ExecutionPolicy Bypass -File {name}\\install.ps1")
            + f'<p class="mt-3 text-sm {P}">The Windows installer uses a local copy rather than piping a remote script, because Claude Code\'s own safety checks flag that pattern. Have a look through {c("install.ps1")} before running it.</p>',
        },
    ]


def install_options(product):
    opts = install_options_for(product)
    jump = "".join(
        f'<a href="#{o["id"]}" class="{CARD} block transition hover:border-slate-400 dark:hover:border-slate-600"><span class="font-mono text-xs text-blue-600 dark:text-blue-400">Option {o["n"]}</span><span class="mt-1 block font-semibold text-slate-900 dark:text-white">{e(o["title"])}</span><span class="mt-1 block text-xs {P}">{"Recommended for most people" if o["rec"] else ", ".join(l for l, _ in o["plats"])}</span></a>'
        for o in opts
    )
    intro = section("Choose how to install", f'<div class="grid gap-4 sm:grid-cols-3">{jump}</div>', sid="options")
    return intro + "".join(render_option(o) for o in opts)


def requirements(extra_row=None, git=True):
    rows = [
        ["Claude Code", "Anthropic's command line tool, installed and signed in", "claude --version"],
        ["Python 3.10+", "Runs the analysis scripts in an isolated environment", "python3 --version"],
    ]
    if git:
        rows.append(["Git", "Used to download and update the files", "git --version"])
    if extra_row:
        rows.append(extra_row)
    return section(
        "Requirements",
        table(rows, head=["What", "Why it is needed", "Check"], mono_first=False)
        + f'<p class="mt-3 text-sm {P}">Chromium is optional. The installer tries to add it for screenshots and JavaScript rendering, and everything else still works if that step fails.</p>',
    )


def link_cards(items):
    return '<div class="grid gap-4 sm:grid-cols-3">' + "".join(
        f'<a href="{href}" class="{CARD} block hover:border-slate-400 dark:hover:border-slate-600"><span class="font-semibold text-slate-900 dark:text-white">{e(t)}</span><p class="mt-1 text-sm {P}">{d}</p></a>'
        for href, t, d in items
    ) + "</div>"


def install_page():
    body = hero(
        "macOS · Linux · Windows",
        "Install SEO Agent Pro",
        f'Bought Pro? These steps take a few minutes. Looking for the free version? <a href="/download/" class="{LINK}">Download Lite</a>.',
        f'<span class="{CHIP} border-blue-500/30 bg-blue-500/10 text-blue-700 dark:text-blue-300">Pro</span>',
    )
    body += section(
        "Before you start",
        f'<div class="rounded-2xl border border-blue-500/20 bg-blue-500/5 p-6"><p class="{P}">Your purchase email from Polar, our reseller, contains your receipt, your <strong class="text-slate-900 dark:text-white">licence key</strong> and a link to download <strong class="text-slate-900 dark:text-white">seo-agent-pro.zip</strong>. Download and unzip it, and keep the key handy.</p><p class="mt-3 text-sm {P}">Cannot find the email? Check your spam folder, or contact <a href="mailto:{SUPPORT_EMAIL}" class="{LINK}">{SUPPORT_EMAIL}</a>.</p></div>',
    )
    body += requirements(["Licence key", "Unlocks Pro on up to 3 of your computers", "In your purchase email"], git=False)
    body += f'<section id="homebrew" class="scroll-mt-10 pb-16">{homebrew_box()}</section>'
    body += install_options("pro")
    body += section(
        "Check it worked",
        steps(
            [
                ("Start Claude Code", f"Open a terminal and run {c('claude')}."),
                ("Run /seo", f"Type {c('/seo')}. You should see the list of commands or a prompt for a URL."),
                ("Run the health check", f"Use {c('/seo doctor')}. It confirms the Python environment, the browser and your licence."),
                ("Run your first audit", f"Try {c('/seo audit https://your-site.com')} and choose a Snapshot or Full audit."),
            ]
        ),
    )
    body += section(
        "Where files are installed",
        table(
            [
                ["~/.claude/skills/seo/", "Main skill"],
                ["~/.claude/skills/seo-*/", "Command skills"],
                ["~/.claude/agents/seo-*.md", "Specialist agents"],
                ["~/.claude/skills/seo/.venv/", "Isolated Python environment"],
            ],
            head=["Path", "Contents"],
        )
        + f'<p class="mt-3 text-sm {P}">Paths apply to manual installs. The installer never installs packages globally or into your user Python.</p>',
    )
    body += section(
        "Common fixes",
        faq_list(
            [
                ("My licence key is not accepted", f"Copy the key again from your purchase email, with no spaces at either end. Each key works on up to 3 computers; if you have replaced a computer, email {SUPPORT_EMAIL} and the old activation can be cleared."),
                ("I cannot find the download link", f"It is in your purchase email from Polar, and on your Polar purchase page, which the email links to. Email {SUPPORT_EMAIL} if you cannot find either."),
                ("/seo is not recognised", f"For plugin installs, check {c('/plugin list')} and reinstall if needed. For manual installs, confirm {c('~/.claude/skills/seo/SKILL.md')} exists, restart Claude Code and re-run the installer."),
                ("ModuleNotFoundError or other Python errors", f"Run {c('/seo setup')} again. Avoid installing individual packages by hand; SEO Agent uses its own isolated environment."),
                ("Python not found on Windows", "Install Python from python.org with \"Add to PATH\" ticked, then run install.ps1 again. The installer tries py -3, python3 and python in turn."),
                ("Audits are slow", f"Full audits crawl up to 500 pages with a polite delay between requests, so large sites take a while. Use a Snapshot audit or {c('/seo analyse')} for quicker checks."),
            ]
        ),
    )
    body += section(
        "Update or uninstall",
        f'<p class="mb-4 {P}">Updates are included for all 3.x versions. To update, download the latest zip from your Polar purchase page and run the installer again; your licence stays active. To remove a plugin install:</p>'
        + code(f"/plugin uninstall seo-agent-pro@{PRO_SLUG.lower().replace('/', '-')}\n/plugin marketplace remove {PRO_SLUG}")
        + f'<p class="mt-4 mb-4 {P}">Manual installs: run the uninstaller from the unzipped folder.</p>'
        + code("bash seo-agent-pro/uninstall.sh"),
    )
    body += section(
        "Next steps",
        link_cards([
            ("/commands/", "Browse the commands", "What each of the eight commands does."),
            ("/commands/audit/", "Run a full audit", "How the audit works and what it produces."),
            ("/commands/google/", "Connect Google data", "Add Search Console, PageSpeed and GA4."),
        ]),
    )
    return page(
        "/install/",
        "Install SEO Agent Pro: setup guide for Claude Code",
        "How to install SEO Agent Pro on macOS, Linux or Windows: requirements, plugin and manual install, activating your licence key and fixes for common problems.",
        "/install/",
        [("/", "Home"), ("/install/", "Install")],
        body,
    )


# ---------------------------------------------------------------- pricing
LITE_FEATURES = [
    "Snapshot audits of up to 10 pages",
    f"Single-page analysis with {c('/seo analyse')}",
    "Health score and top findings",
    "Markdown summary report",
]
PRO_FEATURES = [
    "All 8 commands and every mode",
    "Full audits of up to 500 pages",
    "Every specialist agent, run in parallel",
    "Client-ready branded A4 PDF reports",
    "Google, backlink, local, AI search and strategy tools",
    "All 3.x updates included",
    "Use it for client work",
    "Up to 3 of your computers",
]


def tick_list(items, accent=False):
    colour = "text-blue-600 dark:text-blue-400" if accent else "text-emerald-600 dark:text-emerald-400"
    lis = "".join(
        f'<li class="flex gap-3"><svg class="mt-1 h-4 w-4 shrink-0 {colour}" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m3.5 8.5 3 3 6-7"/></svg><span>{i}</span></li>'
        for i in items
    )
    return f'<ul class="flex flex-col gap-2.5 text-sm {P}">{lis}</ul>'


def pricing_cards(buy_href="/pricing/#buy", show_price=False):
    pro_price = (
        f'<span class="text-4xl font-semibold tracking-tight text-slate-900 dark:text-white">{PRICE}</span><span class="text-sm {P}">one-time, VAT included</span>'
        if show_price
        else f'<span class="text-4xl font-semibold tracking-tight text-slate-900 dark:text-white">One-time</span><span class="text-sm {P}">no subscription</span>'
    )
    return f"""<div class="grid gap-6 md:grid-cols-2">
      <div class="flex flex-col rounded-2xl border border-slate-200 p-7 dark:border-slate-800">
        <h3 class="text-lg font-semibold text-slate-900 dark:text-white">SEO Agent Lite</h3>
        <p class="mt-1 text-sm {P}">Try the approach on a small site.</p>
        <p class="mt-5 text-4xl font-semibold tracking-tight text-slate-900 dark:text-white">Free</p>
        <div class="mt-6 flex-1">{tick_list(LITE_FEATURES)}</div>
        <a href="/download/" {BTN2.replace('px-5', 'px-5 text-center mt-8')}>Download Lite</a>
      </div>
      <div class="glow-border relative flex flex-col rounded-2xl border-2 border-blue-500/40 p-7 shadow-xl shadow-blue-600/10 dark:bg-[#040c1f]">
        <span class="absolute -top-3 left-7 rounded-full bg-blue-600 px-3 py-0.5 text-xs font-medium text-white">Most popular</span>
        <h3 class="text-lg font-semibold text-slate-900 dark:text-white">SEO Agent Pro</h3>
        <p class="mt-1 text-sm {P}">Client-ready audits for any size of site.</p>
        <p class="mt-5 flex items-baseline gap-2">{pro_price}</p>
        <div class="mt-6 flex-1">{tick_list(PRO_FEATURES, accent=True)}</div>
        <a href="{buy_href}" {BTN.replace('px-5', 'px-5 text-center mt-8')}>{'Buy SEO Agent Pro' if show_price else 'See Pro pricing'}</a>
        <p class="mt-3 text-center text-xs text-slate-500 dark:text-slate-400">14-day refund, no questions asked</p>
      </div>
    </div>"""


def pricing_page():
    body = hero(
        "One-time payment · No subscription",
        f"Simple pricing: free Lite, or Pro for {PRICE}",
        "Pay once and keep it. Pro includes every command, full audits, client-ready PDF reports and all 3.x updates.",
    )
    body += f'<section id="buy" class="scroll-mt-10 pb-16">{pricing_cards(CHECKOUT_URL, show_price=True)}</section>'
    body += section(
        "Compare Lite and Pro",
        table(
            [
                ["Commands", f"{c('/seo audit')} (Snapshot) and {c('/seo analyse')}", "All 8 commands, every mode and flag"],
                ["Audit size", "Up to 10 pages", "Up to 500 pages"],
                ["Findings", "Top findings", "Complete findings with evidence"],
                ["Reports", "Markdown summary", "Full report, action plan and branded A4 PDF"],
                ["Specialists", "Core checks", "Technical, content, performance, visual, AI search, local, Google and backlinks"],
                ["Updates", "Occasional", "All 3.x updates"],
                ["Client work", "Personal evaluation", "Yes"],
                ["Computers", "Any", "Up to 3"],
                ["Price", "Free", f"{PRICE} one-time"],
            ],
            head=["", "Lite", "Pro"],
            mono_first=False,
        ),
    )
    body += section(
        "How buying works",
        steps(
            [
                ("Checkout", "Pay securely on Polar's checkout page. Card details never touch this website."),
                ("Check your email", "Polar sends your receipt, your licence key and a link to download the files."),
                ("Install", f'Follow the <a href="/install/" class="{LINK}">Pro install guide</a>. It takes a few minutes.'),
                ("Activate", f"Paste your licence key when {c('/seo setup')} asks for it. That is it."),
            ]
        ),
    )
    body += section(
        "Pricing questions",
        faq_list(
            [
                ("Is this a subscription?", f"No. You pay {PRICE} once and keep using the version you bought. All 3.x updates are included."),
                ("Do you charge VAT?", f"The {PRICE} price includes any VAT. Our reseller, Polar, is the merchant of record: it handles payment, sales tax and your receipt. Prices may be shown in your local currency at checkout."),
                ("Can I use it for client work?", "Yes. Pro is licensed to you for your own work, including audits and reports you deliver to clients. The reports you produce are yours."),
                ("How many computers can I use?", "Up to 3 computers that you use yourself. If you replace one, get in touch and the old activation can be cleared."),
                ("What if it is not for me?", f'Email {SUPPORT_EMAIL} within 14 days for a full refund. See the <a href="/refunds/" class="{LINK}">refund policy</a>.'),
                ("Do I need anything else?", "Claude Code with your own Anthropic account, which you pay for separately. Optional data sources, such as Google APIs or Moz, have their own terms."),
            ]
        ),
    )
    ld = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "SEO Agent Pro",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "macOS, Linux, Windows",
        "offers": {"@type": "Offer", "price": "50.00", "priceCurrency": "GBP", "url": f"{SITE}/pricing/"},
    }
    return page(
        "/pricing/",
        f"Pricing: SEO Agent Pro for a one-time {PRICE} | SEO Agent",
        f"SEO Agent pricing: free Lite with Snapshot audits, or Pro for a one-time {PRICE} with all 8 commands, full audits, client-ready PDF reports and all 3.x updates.",
        "/pricing/",
        [("/", "Home"), ("/pricing/", "Pricing")],
        body,
        extra_ld=ld,
    )


def download_page():
    body = hero(
        "Free · MIT licensed",
        "Download SEO Agent Lite",
        "Lite runs Snapshot audits and single-page analysis in Claude Code, free. It is the quickest way to see how SEO Agent works before upgrading.",
        f'<span class="{CHIP} border-emerald-500/30 bg-emerald-500/10 text-emerald-700 dark:text-emerald-300">Lite</span>',
    )
    body += section(
        "What Lite includes",
        '<div class="grid gap-6 md:grid-cols-2">'
        + f'<div class="{CARD}"><h3 class="mb-4 font-semibold text-slate-900 dark:text-white">Included</h3>{tick_list(LITE_FEATURES)}</div>'
        + f'<div class="{CARD}"><h3 class="mb-4 font-semibold text-slate-900 dark:text-white">Pro only</h3>{tick_list(["Full audits of up to 500 pages", "Client-ready PDF reports", "Content, local, AI search, backlinks, strategy and Google commands", "Focus modes for technical, schema, sitemap, images and hreflang", "Screaming Frog, Ahrefs, Semrush and Sitebulb integrations"], accent=True)}<a href="/pricing/" class="mt-5 inline-block text-sm {LINK}">See Pro pricing</a></div>'
        + "</div>",
    )
    body += requirements()
    body += f'<section id="homebrew" class="scroll-mt-10 pb-16">{homebrew_box()}</section>'
    body += install_options("lite")
    body += section(
        "Check it worked",
        steps(
            [
                ("Start Claude Code", f"Open a terminal and run {c('claude')}."),
                ("Run your first Snapshot audit", f"Try {c('/seo audit https://your-site.com')}. Lite reviews up to 10 pages and reports the top findings."),
            ]
        ),
    )
    body += cta()
    return page(
        "/download/",
        "Download SEO Agent Lite: free SEO audits for Claude Code",
        "Download SEO Agent Lite, the free version of SEO Agent for Claude Code. Snapshot audits of up to 10 pages and single-page SEO analysis, with install steps for macOS, Linux and Windows.",
        "/download/",
        [("/", "Home"), ("/download/", "Download Lite")],
        body,
    )


def thanks_page():
    body = hero(
        "Order complete",
        "Thank you for buying SEO Agent Pro",
        "Your receipt and licence key are on their way from Polar, our reseller. Here is what to do next.",
    )
    body += section(
        "Next steps",
        steps(
            [
                ("Check your email", f"Look for the email from Polar. It holds your receipt, your licence key and access to the files. Check spam if it has not arrived within a few minutes."),
                ("Get the files", "Download seo-agent-pro.zip from the email and unzip it."),
                ("Install Pro", f'Follow the <a href="/install/" class="{LINK}">Pro install guide</a> for your computer.'),
                ("Activate your licence", f"Paste your key when {c('/seo setup')} asks for it, then run your first audit."),
            ]
        ),
    )
    body += section(
        "Need a hand?",
        f'<p class="{P}">Email <a href="mailto:{SUPPORT_EMAIL}" class="{LINK}">{SUPPORT_EMAIL}</a> with your order email address and a short description, and Dan will get back to you.</p>',
    )
    return page("/thanks/", "Thank you | SEO Agent", "Your SEO Agent Pro order is complete. Next steps to install and activate Pro.", "/thanks/", [], body, noindex=True)


# ---------------------------------------------------------------- legal
def prose(sections_):
    out = []
    for h, paras in sections_:
        out.append(f'<h2 class="mt-10 mb-3 text-xl font-semibold tracking-tight text-slate-900 dark:text-white">{e(h)}</h2>')
        for para in paras:
            if isinstance(para, list):
                out.append(f'<div class="mb-4">{ul(para)}</div>')
            else:
                out.append(f'<p class="mb-4 leading-relaxed {P}">{para}</p>')
    return f'<div class="max-w-3xl pb-20">{"".join(out)}</div>'


def legal_page(path, title, h1, desc, sections_):
    body = hero(f"Last updated {UPDATED}", h1, desc)
    body += prose(sections_)
    return page(path, f"{title} | SEO Agent", desc, path, [("/", "Home"), (path, title)], body)


SELLER = "Daniel Lowry, a sole trader based in the United Kingdom, trading as SEO Agent"


def terms_page():
    return legal_page(
        "/terms/", "Terms and licence", "Terms of sale and licence",
        "The terms that apply when you buy SEO Agent Pro, and the licence for using it.",
        [
            ("Who we are", [f"SEO Agent is made by {SELLER} (\"we\", \"us\"). Contact: <a href=\"mailto:{SUPPORT_EMAIL}\" class=\"{LINK}\">{SUPPORT_EMAIL}</a>."]),
            ("How you buy", [
                "Orders are processed by Polar, our online reseller and merchant of record. Polar takes payment, charges any sales tax or VAT and issues your receipt. Polar's own terms also apply to the purchase.",
                f"The price is shown on the pricing page and at checkout, and includes any VAT. It is a one-time payment in pounds sterling or the local equivalent, not a subscription.",
            ]),
            ("Your licence", [
                "When you buy SEO Agent Pro, we grant you a personal, non-exclusive, non-transferable licence to install and use it, on up to 3 computers that you use yourself.",
                [
                    "You may use it for your own work and for work you do for clients, including audits and reports you deliver to them.",
                    "The reports and other output you create belong to you.",
                    "You may not share, resell, sublicense or publish the Pro files or your licence key, or make them available to others.",
                    "You may not remove or bypass the licence check, or use SEO Agent Pro to build a competing product.",
                ],
                "If you break these licence terms, we may revoke your licence key.",
            ]),
            ("Updates and support", [
                "Your purchase includes all updates to version 3.x of SEO Agent Pro. A future major version may be sold separately; the version you have keeps working.",
                f"Support is by email at {SUPPORT_EMAIL}. We aim to reply within two working days.",
            ]),
            ("Third-party components and services", [
                "SEO Agent includes open-source components that are licensed under their own terms, including the MIT License. Those notices are included with the files and are not changed by this licence.",
                "SEO Agent runs inside Claude Code, which needs your own account with Anthropic and is subject to Anthropic's terms and charges. Optional data sources you connect, such as Google APIs, Moz or Bing Webmaster Tools, are subject to their own terms. SEO Agent is not affiliated with or endorsed by Anthropic.",
            ]),
            ("Refunds and cancellation", [f'You can ask for a full refund within 14 days of purchase. See the <a href="/refunds/" class="{LINK}">refund policy</a>. When a refund is made, the licence key is revoked.']),
            ("No guarantees of results", [
                "SEO Agent identifies issues and recommends improvements. It cannot guarantee rankings, traffic, indexing or AI citations, which depend on search engines and many other factors. Check important findings before acting on them.",
                "The software is provided as it is. We do not promise that it will be error free or work with every website.",
            ]),
            ("Our liability", [
                "Nothing in these terms limits liability for death or personal injury caused by negligence, for fraud, or for anything else that cannot be limited by law. Your statutory rights as a consumer are not affected.",
                "Otherwise, our total liability to you is limited to the amount you paid for SEO Agent Pro. We are not responsible for indirect or consequential loss, or for business losses such as lost profit or lost clients.",
            ]),
            ("Changes and law", [
                "We may update these terms from time to time. The terms that applied when you bought still apply to that purchase.",
                "These terms are governed by the law of England and Wales. If you live elsewhere in the UK or in another country, you keep any consumer protections that the law of your home country gives you.",
            ]),
        ],
    )


def refunds_page():
    return legal_page(
        "/refunds/", "Refund policy", "Refund policy",
        "If SEO Agent Pro is not right for you, ask within 14 days for a full refund.",
        [
            ("14-day refund", [
                f"Email <a href=\"mailto:{SUPPORT_EMAIL}\" class=\"{LINK}\">{SUPPORT_EMAIL}</a> within 14 days of your purchase with the email address you used at checkout. You do not need to give a reason.",
                "The refund goes back to your original payment method through Polar, our reseller. Your bank may take a few working days to show it.",
            ]),
            ("What happens to your licence", ["When a refund is made, your licence key is revoked and Pro stops working at its next licence check. Please delete your copy of the Pro files."]),
            ("After 14 days", ["We may still help if something has gone wrong, for example if Pro does not work as described and we cannot fix it. Get in touch and explain what happened."]),
            ("Your legal rights", ["This policy is in addition to your rights under consumer law, which it does not reduce."]),
        ],
    )


def privacy_page():
    return legal_page(
        "/privacy/", "Privacy policy", "Privacy policy",
        "What personal data SEO Agent collects, why, and your rights over it.",
        [
            ("Who is responsible", [f"The data controller is {SELLER}. Contact: <a href=\"mailto:{SUPPORT_EMAIL}\" class=\"{LINK}\">{SUPPORT_EMAIL}</a>."]),
            ("This website", [
                "This website uses Umami, a privacy-focused analytics service, to count visits, see which pages and links are used and understand where visitors come from. It does not use cookies, does not collect personal data, does not build profiles of individual visitors and does not track you across other sites.",
                "Our hosting provider, IONOS, keeps standard server logs, such as IP addresses and the pages requested, to run and protect the service.",
            ]),
            ("When you buy", [
                "Polar, our reseller and merchant of record, collects your name, email address, billing country and payment details to process your order and meet its tax obligations. Polar handles your payment details; we never see your full card number.",
                "Polar shares with us your name, email address, country and order details. We use them to deliver your licence and files, provide support, handle refunds and keep the records the law requires.",
            ]),
            ("When you use SEO Agent", [
                "SEO Agent runs on your own computer. Audit results are saved to your computer and are not sent to us.",
                "When it runs, it makes requests to the websites you ask it to audit and to any services you connect yourself, such as Google APIs, Moz or Bing Webmaster Tools. Claude Code sends your prompts and the content it works with to Anthropic under your own Anthropic account.",
                "SEO Agent Pro checks your licence with Polar when you activate it and from time to time afterwards. The check sends your licence key and a label for your computer; it does not send audit data.",
            ]),
            ("Legal basis and retention", [
                "We process purchase data to perform our contract with you and to meet legal obligations, such as keeping tax and accounting records. We keep these records for as long as the law requires, usually six years, and support emails for as long as they are useful for helping you.",
            ]),
            ("Your rights", [
                "Under UK data protection law you can ask for a copy of your data, ask us to correct or delete it, or object to how it is used. Email us to make a request.",
                "If you are unhappy with how we handle your data, you can complain to the Information Commissioner's Office at ico.org.uk.",
            ]),
        ],
    )


# ---------------------------------------------------------------- faq
FAQS = [
    ("General", [
        ("What is SEO Agent?", "SEO Agent adds eight SEO commands to Claude Code. They run specialist agents that crawl a site, diagnose technical, content and AI search issues, and return a health score with a prioritised action plan and a client-ready report."),
        ("How much does it cost?", f'Lite is free. Pro is a one-time payment, with no subscription, and includes all 3.x updates. See <a href="/pricing/" class="{LINK}">pricing</a>.'),
        ("What is the difference between Lite and Pro?", f'Lite runs Snapshot audits of up to 10 pages and single-page analysis. Pro unlocks all eight commands, full audits of up to 500 pages, every specialist and branded PDF reports. The <a href="/pricing/" class="{LINK}">pricing page</a> compares them side by side.'),
        ("How is SEO Agent different from other Claude SEO tools?", "There are a few SEO toolkits for Claude Code, and most produce raw output that needs tidying before anyone else sees it. SEO Agent is built by an SEO with more than 12 years in the industry, and its audits are designed to be client-ready from the start: evidence for every finding, a clear health score, a prioritised action plan and a branded PDF report. It also keeps the whole job to 8 commands rather than a long menu of overlapping skills."),
        ("Are the audits ready to send to clients?", "Yes, that is what they are built for. Each Pro report opens with an executive summary and health score, every issue is backed by the URLs and values found, and fixes are grouped by priority so a client can see what matters first. The PDF adds charts and a roadmap for presenting."),
        ("Who built SEO Agent?", f'Dan Lowry, an SEO with more than 12 years of experience. The commands, scoring and report structure reflect how audits are actually used with clients. You can find Dan on <a href="https://linkedin.com/in/dan-lowry-seo" target="_blank" rel="noopener noreferrer" class="{LINK}">LinkedIn</a>.'),
        ("Does it replace tools like Ahrefs or Semrush?", "Not entirely. Paid platforms hold large keyword and link databases built over years. SEO Agent is strongest at auditing and diagnosing a site you can crawl, explaining the problems in plain language and turning them into an action plan. Many people use both."),
        ("Is SEO Agent made by Anthropic?", "No. SEO Agent is an independent product that runs inside Claude Code. It is not affiliated with or endorsed by Anthropic."),
    ]),
    ("Buying and licence", [
        ("Is it a subscription?", f"No. Pro is a one-time payment. You keep the version you bought, and all 3.x updates are included."),
        ("Can I use it for client work?", "Yes. Your Pro licence covers audits and reports you produce for clients, and the reports are yours."),
        ("How many computers can I use it on?", "Up to 3 computers that you use yourself."),
        ("Do you charge VAT?", f"The price includes any VAT. Polar, our reseller and merchant of record, handles payment and tax and sends your receipt."),
        ("What is the refund policy?", f'A full refund within 14 days, no questions asked. See the <a href="/refunds/" class="{LINK}">refund policy</a>.'),
        ("Do I need a GitHub account?", "No. Pro is delivered as a zip download from your purchase email, and updates are downloaded the same way."),
    ]),
    ("Audits and scoring", [
        ("How long does an audit take?", "It depends on the size and speed of the site. A Snapshot audit of a small site is usually quick. A Full audit can crawl up to 500 pages with a one second delay between requests, so large sites take longer."),
        ("What does the health score mean?", f"It is a 0 to 100 score weighted across content quality, technical SEO, on-page SEO, schema, performance, AI search readiness and images. It is a way to prioritise work, not a prediction of rankings. See the <a href=\"/commands/audit/\" class=\"{LINK}\">audit page</a> for the weightings."),
        ("What is the difference between a Snapshot and a Full audit?", "A Snapshot reports only the top findings in a short report. A Full audit, in Pro, crawls up to 500 pages and reports everything. Both use the same evidence standard."),
        ("Can I trust the findings?", "Every finding has to name the affected URLs and show the value actually found on the page. Anything that would apply to any site without evidence is cut before the report is written. As with any automated tool, it is worth checking critical findings before acting on them."),
        ("Does it change my website?", "No. It reads the public site and writes files to your own computer only."),
    ]),
    ("Setup and data", [
        ("What do I need to install it?", f"Claude Code and Python 3.10 or later, plus Git for Lite. The full steps are on the <a href=\"/install/\" class=\"{LINK}\">install page</a> for Pro and the <a href=\"/download/\" class=\"{LINK}\">download page</a> for Lite."),
        ("Does it work on Windows?", "Yes. There is a PowerShell installer alongside the macOS and Linux script, and the plugin install works on every platform Claude Code supports."),
        ("Do I need API keys?", "No, the core commands work without any. Free Google, Moz and Bing Webmaster keys add real search data, field Core Web Vitals and richer backlink data in Pro."),
        ("Where does my data go?", f'Audit files are saved on your computer. Requests go to the site being audited and to any services you connect. See the <a href="/privacy/" class="{LINK}">privacy policy</a>.'),
        ("What kinds of sites does it support?", "It detects the business type, such as SaaS, local service, e-commerce, publisher or agency, and adjusts its recommendations. Local SEO checks switch on automatically for location based businesses."),
    ]),
    ("AI search", [
        ("What is generative engine optimisation?", f"GEO is the practice of making content easy for AI search features, such as Google AI Overviews, ChatGPT search and Perplexity, to find, understand and cite. Google's position is that this is still SEO, applied to new surfaces. The <a href=\"/commands/geo/\" class=\"{LINK}\">geo command</a> checks it."),
        ("Do I need an llms.txt file?", "Google has said llms.txt is not needed for its AI features. The geo command reports whether one exists, but does not treat a missing file as a serious problem."),
    ]),
]


def faq_page():
    body = hero("FAQ", "Frequently asked questions", "Answers to the questions people ask most about buying SEO Agent, installing it, running audits and reading the results.")
    for group, items in FAQS:
        body += section(group, faq_list(items))
    body += cta()
    return page(
        "/faq/",
        "SEO Agent FAQ: pricing, licence, audits and setup",
        "Answers to common questions about SEO Agent: pricing, Lite vs Pro, licence and refunds, installation, how audits and the health score work, and data privacy.",
        "/faq/",
        [("/", "Home"), ("/faq/", "FAQ")],
        body,
    )


# ---------------------------------------------------------------- home
def home_page():
    rows = "".join(
        f'<tr class="border-b border-slate-200 last:border-0 dark:border-slate-800"><td class="block px-5 pt-3 pb-0.5 font-mono text-slate-900 sm:table-cell sm:w-64 sm:py-3 sm:whitespace-nowrap dark:text-white"><a href="/commands/{x["slug"]}/" class="underline decoration-slate-300 underline-offset-4 hover:decoration-slate-900 dark:decoration-slate-600 dark:hover:decoration-white">{e(x["cmd"])}</a></td><td class="block px-5 pt-0.5 pb-3 text-slate-600 sm:table-cell sm:py-3 dark:text-slate-400">{e(x["short"])}</td><td class="hidden px-5 py-3 text-right sm:table-cell">{tier_tag(x)}</td></tr>'
        for x in COMMANDS
    )
    body = f"""
      <section class="relative isolate flex flex-col items-center gap-6 overflow-hidden py-20 text-center sm:py-28">
        <canvas id="snake-canvas" class="pointer-events-none absolute inset-0 -z-10 h-full w-full" aria-hidden="true"></canvas>
        <span class="rounded-full border border-slate-200 bg-white/70 px-3 py-1 text-xs font-medium text-slate-500 dark:border-slate-700 dark:bg-slate-950/70 dark:text-slate-400">One-time payment &middot; Runs locally &middot; Client-ready audits</span>
        <h1 class="max-w-2xl text-4xl font-semibold tracking-tight text-slate-900 sm:text-5xl dark:text-white">Your SEO team, in the terminal</h1>
        <p class="max-w-xl text-lg text-slate-600 dark:text-slate-400">SEO Agent turns Claude Code into a full SEO department. Eight commands run specialist agents that crawl a site, diagnose technical, content and AI search issues, then hand you a health score, a prioritised action plan and a report ready to send to a client.</p>
        <div class="flex flex-wrap items-center justify-center gap-3 pt-2">
          <a href="/pricing/" {BTN}>Get Pro</a>
          <a href="/download/" {BTN2}>Try Lite free</a>
        </div>
      </section>
      <section class="reveal -mt-6 pb-20" aria-label="Example audit run">
        <div class="terminal mx-auto max-w-3xl overflow-hidden rounded-2xl border border-slate-800 bg-[#030712] text-left shadow-2xl shadow-blue-900/30">
          <div class="flex items-center gap-3 border-b border-slate-800 bg-[#040c1f] px-4 py-2.5">
            <span class="flex gap-1.5" aria-hidden="true"><span class="h-3 w-3 rounded-full bg-rose-400/80"></span><span class="h-3 w-3 rounded-full bg-amber-400/80"></span><span class="h-3 w-3 rounded-full bg-emerald-400/80"></span></span>
            <span class="font-mono text-xs text-slate-400">claude · seo agent pro</span>
            <button type="button" class="terminal-replay ml-auto rounded-md border border-slate-700 px-2 py-0.5 font-mono text-[11px] text-slate-300 hover:border-slate-500">replay</button>
          </div>
          <div id="terminal-demo" class="terminal-body font-mono text-[12.5px] leading-6 text-slate-200 sm:text-sm" aria-live="off"></div>
        </div>
        <p class="mt-3 text-center text-xs text-slate-500 dark:text-slate-400">Illustrative run on a demo site. Real audits take longer and report the actual pages found.</p>
      </section>"""
    body += section(
        "How it works",
        steps(
            [
                ("Install", f'Add SEO Agent to Claude Code in a few minutes. <a href="/install/" class="{LINK}">Install guide</a>.'),
                ("Run an audit", f"Type {c('/seo audit https://client-site.com')}. Specialist agents crawl and check the site in parallel."),
                ("Review the findings", "Every issue comes with the affected URLs and the values found, ranked Critical to Low."),
                ("Send the report", "Hand the client a branded PDF with a health score, action plan and roadmap."),
            ]
        ),
    )
    body += section(
        "Commands",
        f'<div class="overflow-hidden rounded-xl border border-slate-200 dark:border-slate-800"><table class="w-full border-collapse text-left text-sm"><tbody>{rows}</tbody></table></div>'
        f'<p class="mt-3 text-sm text-slate-500 dark:text-slate-400"><a href="/commands/" class="font-medium text-slate-700 underline underline-offset-2 dark:text-slate-300">See every command in detail</a></p>',
    )
    body += section(
        "Works with your SEO stack",
        f'<p class="mb-5 max-w-2xl {P}">Plug in the crawler and data tools your team already pays for. Crawl faster, use less of Claude\'s context and put trusted data in front of the client.</p>'
        + integration_cards()
        + f'<p class="mt-4 text-sm"><a href="/integrations/" class="{LINK}">See how the integrations work</a></p>',
    )
    # ---- Real test audit (site name hidden) -------------------------------
    AUDIT_CATS = [
        ("Technical SEO", 45), ("Content quality", 58), ("On-page SEO", 60), ("Schema", 10),
        ("Performance", 38), ("AI search", 48), ("Images", 55),
    ]
    AUDIT_SCORE = 48
    SEV = [("Critical", 2, "rose"), ("High", 5, "amber"), ("Medium", 6, "blue"), ("Low", 2, "slate")]
    REDACT = '<span class="redact" aria-label="site name hidden">clientwebsite.co.uk</span>'

    def tone(v):
        return "bad" if v < 40 else "warn" if v < 65 else "good"

    bars = "".join(
        f'<div class="grid grid-cols-[7.5rem_1fr_2rem] items-center gap-3 text-xs"><span class="text-slate-500 dark:text-slate-400">{n}</span><span class="h-1.5 overflow-hidden rounded-full bg-slate-200 dark:bg-slate-800"><span class="score-bar tone-{tone(v)} block h-full rounded-full" style="--w:{v}%"></span></span><span class="text-right font-mono text-slate-700 dark:text-slate-300">{v}</span></div>'
        for n, v in AUDIT_CATS
    )
    sev_tiles = "".join(
        f'<div class="rounded-lg bg-{c}-500/10 py-2"><p class="font-semibold text-{c}-600 dark:text-{c}-300">{n}</p><p class="text-slate-500 dark:text-slate-400">{label}</p></div>'
        for label, n, c in SEV
    )
    features = "".join(
        f'<li class="flex gap-4"><span class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-blue-500/10 text-xs font-semibold text-blue-600 dark:text-blue-300">{i}</span><div><h3 class="font-semibold text-slate-900 dark:text-white">{t}</h3><p class="mt-1 text-sm {P}">{d}</p></div></li>'
        for i, (t, d) in enumerate([
            ("A score anyone gets", "One number out of 100, weighted across seven categories. Clients understand it in seconds."),
            ("Evidence on every issue", "The URL, the value found and why it costs rankings. No guesswork. No filler."),
            ("A plan, not a pile of problems", "Fixes ranked Critical to Low and grouped into four phases, so everyone knows what happens first."),
            ("A PDF worth forwarding", "Colour-coded, charted and ready to present the moment the audit finishes."),
        ], 1)
    )
    body += f'''
      <section class="reveal scroll-mt-10 pb-24">
        <h2 class="{H2}">What you and your clients receive</h2>
        <p class="max-w-2xl text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl dark:text-white">Proof, not opinions.</p>
        <p class="mt-4 max-w-2xl text-lg {P}">Every finding arrives with the URL, the evidence and the fix. Below is a real test audit of a UK events company. Their name is hidden. The problems are real.</p>
        <div class="mt-10 grid items-center gap-10 md:grid-cols-2">
          <div class="report-card rounded-2xl border border-slate-200 bg-white p-6 shadow-xl shadow-slate-900/5 dark:border-slate-800 dark:bg-[#040c1f] dark:shadow-blue-900/20">
            <div class="flex items-start justify-between gap-4">
              <div><p class="text-xs font-semibold uppercase tracking-wide text-slate-500 dark:text-slate-400">SEO audit</p><p class="mt-1 font-semibold text-slate-900 dark:text-white">{REDACT}</p><p class="text-xs text-slate-500 dark:text-slate-400">Events company · Full audit · 40 pages checked</p></div>
              <div class="relative h-24 w-24 shrink-0">
                <svg viewBox="0 0 100 100" class="h-24 w-24 -rotate-90" aria-hidden="true"><circle cx="50" cy="50" r="42" fill="none" stroke-width="9" class="stroke-slate-200 dark:stroke-slate-800"/><circle cx="50" cy="50" r="42" fill="none" stroke-width="9" stroke-linecap="round" class="score-ring stroke-amber-500" pathLength="100" style="--score:{AUDIT_SCORE}"/></svg>
                <span class="absolute inset-0 flex flex-col items-center justify-center"><span class="score-count text-2xl font-semibold text-slate-900 dark:text-white" data-target="{AUDIT_SCORE}">{AUDIT_SCORE}</span><span class="text-[10px] text-slate-500 dark:text-slate-400">/ 100</span></span>
              </div>
            </div>
            <div class="mt-6 flex flex-col gap-2.5">{bars}</div>
            <div class="mt-6 grid grid-cols-4 gap-2 text-center text-xs">{sev_tiles}</div>
            <p class="mt-4 text-[11px] text-slate-400 dark:text-slate-500">Test audit of a live site, September 2026. Site name hidden.</p>
          </div>
          <ul class="flex flex-col gap-6">{features}</ul>
        </div>
      </section>'''

    # ---- PDF preview ---------------------------------------------------------
    def pdf_head(title, n):
        return f'<div class="pdf-runner"><span class="pdf-brand"><i></i>SEO Agent Pro</span><span>{title}</span><span>{n} / 4</span></div>'

    ring = lambda size, stroke: f'<svg viewBox="0 0 100 100" class="pdf-ring" style="width:{size}px;height:{size}px" aria-hidden="true"><defs><linearGradient id="pdfg{size}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f59e0b"/><stop offset="1" stop-color="#ef4444"/></linearGradient></defs><circle cx="50" cy="50" r="42" fill="none" stroke="rgba(148,163,184,.25)" stroke-width="{stroke}"/><circle cx="50" cy="50" r="42" fill="none" stroke="url(#pdfg{size})" stroke-width="{stroke}" stroke-linecap="round" pathLength="100" class="pdf-arc" style="--score:{AUDIT_SCORE}"/></svg>'

    cover = f'''<div class="pdf-page" data-page="0">
          <div class="pdf-cover-band"><div class="pdf-mesh"></div>
            <p class="pdf-kicker">SEO audit report</p>
            <p class="pdf-cover-title">{REDACT}</p>
            <p class="pdf-cover-sub">Full audit · 30 September 2026</p>
          </div>
          <div class="pdf-cover-body">
            <div class="pdf-cover-score">{ring(150, 10)}<div class="pdf-ring-label"><b class="pdf-count" data-target="{AUDIT_SCORE}">{AUDIT_SCORE}</b><span>Health score</span></div></div>
            <div class="pdf-cover-stats">
              <div><b class="pdf-count" data-target="15">15</b><span>issues found</span></div>
              <div><b class="pdf-count" data-target="2">2</b><span>critical</span></div>
              <div><b class="pdf-count" data-target="40">40</b><span>pages checked</span></div>
            </div>
            <p class="pdf-cover-verdict">Strong content foundations, held back by crawl and duplication problems. Fix the two critical issues first: both are quick wins.</p>
            <p class="pdf-label" style="margin-top:22px">Category scores</p>
            <div class="pdf-chips">{"".join(f'<span class="pdf-chip chip-{tone(v)}"><b>{v}</b>{n}</span>' for n, v in AUDIT_CATS)}</div>
          </div>
          <div class="pdf-foot"><span>Prepared with SEO Agent Pro</span><span>Confidential</span></div>
        </div>'''

    cat_rows = "".join(
        f'<div class="pdf-cat"><span>{n}</span><span class="pdf-track"><i class="pdf-fill tone-{tone(v)}" style="--w:{v}%"></i></span><b>{v}</b></div>'
        for n, v in AUDIT_CATS
    )
    total = sum(n for _, n, _ in SEV)
    acc = 0
    stops = []
    colours = {"rose": "#f43f5e", "amber": "#f59e0b", "blue": "#3b82f6", "slate": "#94a3b8"}
    for _, n, col in SEV:
        start = acc / total * 100
        acc += n
        stops.append(f"{colours[col]} {start:.1f}% {acc / total * 100:.1f}%")
    legend = "".join(f'<li><i style="background:{colours[c]}"></i>{label}<b>{n}</b></li>' for label, n, c in SEV)
    summary = f'''<div class="pdf-page" data-page="1">
          {pdf_head("Executive summary", 2)}
          <p class="pdf-h">Executive summary</p>
          <p class="pdf-lead">The site is crawlable and content-rich, but duplicate signals and missing technical basics are capping its visibility.</p>
          <div class="pdf-two">
            <div class="pdf-panel"><p class="pdf-label">Scores by category</p>{cat_rows}</div>
            <div class="pdf-panel pdf-center"><p class="pdf-label">Issues by severity</p><div class="pdf-donut-wrap"><div class="pdf-donut" style="--donut:conic-gradient({', '.join(stops)})"></div><span class="pdf-donut-label"><b class="pdf-count" data-target="{total}">{total}</b>issues</span></div><ul class="pdf-legend">{legend}</ul></div>
          </div>
          <p class="pdf-label" style="margin-top:18px">Top priorities</p>
          <ol class="pdf-top">
            <li><em class="sev sev-critical">Critical</em>robots.txt returns the homepage, not crawl rules</li>
            <li><em class="sev sev-critical">Critical</em>No canonical tags on any page checked</li>
            <li><em class="sev sev-high">High</em>Internal links and redirects mix http and https</li>
          </ol>
          <div class="pdf-strip"><div><b>246</b>URLs in sitemap</div><div><b>40</b>pages checked</div><div><b>7</b>categories scored</div><div><b>0</b>pages with schema</div></div>
          <div class="pdf-foot"><span>SEO Agent Pro</span><span>Page 2</span></div>
        </div>'''

    findings_data = [
        ("critical", "robots.txt serves the homepage", "GET /robots.txt → 200 · text/html", "Search engines receive a web page instead of crawl rules, so there is no pointer to the 246-URL sitemap.", "Serve a plain-text robots.txt that references /sitemap.xml."),
        ("critical", "No canonical tags", "0 of 40 pages · rel=\"canonical\" missing", "With www, non-www, http and https versions in play, Google has to guess which URL to rank.", "Add a self-referencing canonical to every template."),
        ("high", "Mixed http and https signals", "href=\"http://…/use-of-cookies\" · no HSTS header", "Links and first visits start on insecure URLs, wasting redirects and diluting signals.", "Point every internal link at https://www and enable HSTS."),
        ("high", "One title shared by 9 pages", "\"Gallery | Corporate Events…\" ×9", "Nine gallery pages compete for the same search, so none of them wins it.", "Write a unique title and description for each gallery."),
    ]
    finding_cards = "".join(
        f'''<div class="pdf-finding"><div class="pdf-finding-top"><em class="sev sev-{s}">{s.title()}</em><b>{t}</b></div><code>{e(ev)}</code><p><span>Impact</span>{imp}</p><p><span>Fix</span>{fix}</p></div>'''
        for s, t, ev, imp, fix in findings_data
    )
    findings = f'''<div class="pdf-page" data-page="2">
          {pdf_head("Findings", 3)}
          <p class="pdf-h">Findings with evidence</p>
          <p class="pdf-lead">Every issue shows what was found, where, and exactly what to change.</p>
          <div class="pdf-findings">{finding_cards}</div>
          <p class="pdf-label" style="margin-top:16px">Also found</p>
          <div class="pdf-more">
            <div><em class="sev sev-medium">Medium</em><span>28 homepage images with no width or height</span><code>CLS risk</code></div>
            <div><em class="sev sev-medium">Medium</em><span>Social share image URL is missing https://</span><code>og:image</code></div>
          </div>
          <div class="pdf-foot"><span>SEO Agent Pro</span><span>Page 3</span></div>
        </div>'''

    phases = [
        ("Week 1", "Critical fixes", 18, ["Fix robots.txt", "Add canonical tags", "Force https://www"], "rose"),
        ("Weeks 2 to 3", "High impact", 38, ["Unique gallery titles", "LocalBusiness schema", "Defer 8 blocking scripts"], "amber"),
        ("Month 2", "Content and speed", 62, ["Compress 2.8 MB of images", "Expand 11 thin pages"], "blue"),
        ("Ongoing", "Monitor", 100, ["Re-audit monthly", "Track Core Web Vitals"], "emerald"),
    ]
    phase_rows = "".join(
        f'''<div class="pdf-phase"><div class="pdf-phase-when"><b>{w}</b><span>{name}</span></div><div class="pdf-phase-main"><span class="pdf-track pdf-track-lg"><i class="pdf-fill phase-{col}" style="--w:{pct}%"></i></span><ul>{"".join(f"<li>{it}</li>" for it in items)}</ul></div></div>'''
        for w, name, pct, items, col in phases
    )
    plan = f'''<div class="pdf-page" data-page="3">
          {pdf_head("Action plan", 4)}
          <p class="pdf-h">Action plan</p>
          <p class="pdf-lead">Fifteen fixes in four phases, ordered by impact and effort.</p>
          <div class="pdf-phases">{phase_rows}</div>
          <div class="pdf-callout"><b>Quick win.</b> The two critical fixes are small jobs, and they unblock most of this plan.</div>
          <div class="pdf-strip"><div><b>15</b>fixes in total</div><div><b>3</b>this week</div><div><b>4</b>phases</div><div><b>1</b>re-audit a month</div></div>
          <div class="pdf-foot"><span>SEO Agent Pro</span><span>Page 4</span></div>
        </div>'''

    thumbs = "".join(
        f'<button type="button" class="pdf-tab{" is-active" if i == 0 else ""}" data-go="{i}"><span class="pdf-tab-n">0{i + 1}</span><span class="pdf-tab-t">{t}</span><span class="pdf-tab-d">{d}</span><i class="pdf-tab-bar"></i></button>'
        for i, (t, d) in enumerate([
            ("Cover", "Score, headline numbers and the verdict in one line."),
            ("Summary", "Category scores and severity at a glance."),
            ("Findings", "Evidence, impact and the fix for every issue."),
            ("Action plan", "Four phases, ready to quote from."),
        ])
    )
    body += f'''
      <section class="reveal scroll-mt-10 pb-20" id="pdf-preview">
        <h2 class="{H2}">The PDF report</h2>
        <div class="grid items-center gap-12 lg:grid-cols-[1.1fr_1fr]">
          <div class="pdf-stage" aria-label="Preview of an SEO Agent Pro PDF report">
            <div class="pdf-sheet pdf-sheet-back2" aria-hidden="true"></div>
            <div class="pdf-sheet pdf-sheet-back1" aria-hidden="true"></div>
            <div class="pdf-frame"><div class="pdf-scaler">{cover}{summary}{findings}{plan}</div></div>
          </div>
          <div>
            <p class="text-3xl font-semibold tracking-tight text-slate-900 sm:text-4xl dark:text-white">The report that wins the meeting.</p>
            <p class="mt-4 text-lg {P}">Pro turns every audit into a colour-coded PDF with charts, evidence and a four-phase plan. Send it as it is, or walk the client through it page by page.</p>
            <div class="mt-8 flex flex-col gap-2">{thumbs}</div>
            <div class="mt-8 flex flex-wrap gap-3"><a href="/pricing/" {BTN}>Get Pro</a><a href="/commands/audit/" {BTN2}>See how audits work</a></div>
            <p class="mt-3 text-xs text-slate-500 dark:text-slate-400">Colour PDF reports are included in SEO Agent Pro.</p>
          </div>
        </div>
      </section>'''

    body += section("Pricing", pricing_cards())
    body += section(
        "Built by an SEO, for client work",
        f'<div class="{CARD} flex flex-col gap-3 sm:flex-row sm:items-center sm:gap-6"><span class="flex h-14 w-14 shrink-0 items-center justify-center rounded-full bg-slate-900 text-lg font-semibold text-white dark:bg-white dark:text-slate-900">DL</span><p class="{P}">SEO Agent is built by Dan Lowry, an SEO with more than 12 years in the industry. It reflects how audits are really used: to show a client what is wrong, why it matters and what to fix first. <a href="https://linkedin.com/in/dan-lowry-seo" target="_blank" rel="noopener noreferrer" class="{LINK}">Connect on LinkedIn</a>.</p></div>',
    )
    body += cta()
    return page(
        "/",
        "SEO Agent: client-ready SEO audits for Claude Code",
        f"SEO Agent turns Claude Code into an SEO department: 8 commands, parallel specialist agents, a health score, a prioritised action plan and client-ready PDF reports. Free Lite, or Pro for a one-time payment.",
        "/",
        [],
        body,
    )


INTEGRATIONS = [
    {
        "name": "Screaming Frog", "badge": "Built in", "kind": "Crawling",
        "short": "SEO Agent runs the crawl on your own machine, then reads a compact summary of the results instead of fetching every page.",
        "points": [
            "One command starts a headless crawl and exports the data.",
            "Counts and example URLs for titles, descriptions, headings, thin content, slow pages, orphan pages and indexability.",
            "Cuts the amount Claude has to read on larger sites, so audits finish faster and use less context.",
        ],
        "needs": "Your own Screaming Frog installation and licence.",
    },
    {
        "name": "Ahrefs", "badge": "Official MCP", "kind": "Backlinks and keywords",
        "short": "Connect Ahrefs through its official MCP server and bring link and keyword data straight into backlink and strategy work.",
        "points": [
            "Referring domains, anchors and competitor link gaps.",
            "Keyword and ranking data for content and strategy plans.",
            "Uses your Ahrefs plan's monthly API units.",
        ],
        "needs": "An Ahrefs plan with API access (Lite and above).",
    },
    {
        "name": "Semrush", "badge": "Official MCP", "kind": "Backlinks and keywords",
        "short": "Connect Semrush through its remote MCP server for domain, keyword and backlink data alongside your audit.",
        "points": [
            "Domain analytics and competitor research.",
            "Keyword research and backlink data.",
            "Uses the API units on your Semrush plan.",
        ],
        "needs": "A Semrush plan that includes API units.",
    },
    {
        "name": "Sitebulb", "badge": "MCP or export", "kind": "Crawling",
        "short": "Bring Sitebulb audit data into SEO Agent through Sitebulb's MCP connection or an export, and turn it into a client-ready report.",
        "points": [
            "Analyse your Sitebulb exports with the same scoring and action plans.",
            "Useful when you already crawl in Sitebulb and want the report written for you.",
        ],
        "needs": "Your own Sitebulb licence.",
    },
]
BADGE = "rounded-full border border-blue-500/30 bg-blue-500/10 px-2.5 py-0.5 text-xs font-medium text-blue-700 dark:text-blue-300"


def integration_cards(detail=False):
    out = []
    for x in INTEGRATIONS:
        pts = ul(x["points"]) if detail else ""
        needs = f'<p class="mt-4 text-xs text-slate-500 dark:text-slate-400">Needs: {e(x["needs"])}</p>' if detail else ""
        out.append(
            f'<div class="{CARD}"><div class="flex flex-wrap items-center justify-between gap-2"><h3 class="text-lg font-semibold text-slate-900 dark:text-white">{e(x["name"])}</h3><span class="{BADGE}">{e(x["badge"])}</span></div>'
            f'<p class="mt-1 font-mono text-xs text-slate-500 dark:text-slate-400">{e(x["kind"])}</p><p class="mt-3 text-sm {P}">{e(x["short"])}</p>{pts}{needs}</div>'
        )
    return f'<div class="grid gap-4 sm:grid-cols-2">{"".join(out)}</div>'


def integrations_page():
    body = hero(
        "Integrations",
        "Works with the SEO tools you already pay for",
        "Plug your crawler and your data tools into SEO Agent Pro. Crawl faster, use less of Claude's context and fill your client reports with the data you trust.",
        tier_tag({"lite": False}),
    )
    body += section("Supported tools", integration_cards(detail=True))
    body += section(
        "Why connect a crawler",
        ul(
            [
                "<strong>Faster audits.</strong> A desktop crawler is built to fetch thousands of URLs. SEO Agent reads its results instead of fetching every page itself.",
                "<strong>Lower token use.</strong> Claude reads counts and examples, not raw HTML, so large sites fit comfortably.",
                "<strong>Data you trust.</strong> Findings are based on the same crawl data your team already uses and understands.",
            ]
        ),
    )
    body += section(
        "How it works",
        steps(
            [
                ("Install the tool", "Use your existing Screaming Frog, Ahrefs, Semrush or Sitebulb account. SEO Agent does not resell or bundle them."),
                ("Run an audit", f"Type {c('/seo audit https://client-site.com')}. If a supported crawler is installed, SEO Agent offers to use it."),
                ("Get the report", "Findings, scores and the action plan are built from the connected data and delivered as a client-ready PDF."),
                ("Keep control", "Everything runs on your computer with your own accounts and licences."),
            ]
        ),
    )
    body += section(
        "Questions",
        faq_list(
            [
                ("Do I need these tools to use SEO Agent?", "No. SEO Agent crawls and audits on its own. Integrations are optional and available in Pro."),
                ("Are the tools included in the price?", "No. You use your own accounts and licences, so you stay in control of those costs."),
                ("Can you add another tool?", f'Probably. Email <a href="mailto:{SUPPORT_EMAIL}" class="{LINK}">{SUPPORT_EMAIL}</a> with the tool you use and what you would want from it.'),
            ]
        ),
    )
    body += '<p class="pb-10 text-xs text-slate-400 dark:text-slate-500">Screaming Frog, Ahrefs, Semrush and Sitebulb are trademarks of their respective owners. SEO Agent is an independent product and is not affiliated with or endorsed by them.</p>'
    body += cta()
    return page(
        "/integrations/",
        "Integrations: Screaming Frog, Ahrefs, Semrush and Sitebulb | SEO Agent",
        "Connect Screaming Frog, Ahrefs, Semrush and Sitebulb to SEO Agent Pro to crawl faster, use less context and build client-ready reports from the data you trust.",
        "/integrations/",
        [("/", "Home"), ("/integrations/", "Integrations")],
        body,
    )



paths = []
paths.append(home_page())
paths.append(pricing_page())
paths.append(download_page())
paths.append(commands_hub())
paths.append(integrations_page())
for cmd in COMMANDS:
    paths.append(command_page(cmd))
paths.append(install_page())
paths.append(faq_page())
paths.append(terms_page())
paths.append(refunds_page())
paths.append(privacy_page())
thanks_page()
paths = [p for p in paths if p]

os.makedirs(os.path.join(SRC, "public"), exist_ok=True)
with open(os.path.join(SRC, "public", "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for p in paths:
        f.write(f"  <url><loc>{SITE}{p}</loc><lastmod>{UPDATED}</lastmod></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(SRC, "public", "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print("\n".join(paths))
