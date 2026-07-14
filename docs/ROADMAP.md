# Project Roadmap: Global Health System Performance Diagnostic

## What I'm doing

Building a data-driven diagnostic of health system performance across countries, using public datasets (WHO Global Health Observatory, World Bank). The end deliverable is structured like a consultancy engagement: a defined problem, an evidence base, a set of prioritised findings, and actionable recommendations - not just a dashboard for its own sake.

Concretely, I'll:
1. Pull and clean public health system indicators (e.g. health spend per capita, workforce density, service coverage, outcomes) across a set of countries
2. Load the cleaned data into a SQL database and write queries to surface KPIs and outliers
3. Analyse the data in Python to find patterns, correlations, and underperformers
4. Build a dashboard (Power BI/Tableau) so the findings are explorable, not just static
5. Write a one-page findings briefing with prioritised recommendations, the way I would for a client

## Why I want to do this

Two reasons:

**Skills demonstration.** My CV claims I can diagnose people/process/data problems and turn them into recommendations for senior stakeholders (WHO, Phoenix Futures). A recruiter can't verify that from a bullet point - this project is the evidence. It shows the SQL, Python, and dashboarding tools listed on my CV are real, working skills, not just words.

**Genuine interest.** Global health is where I want to build a career, and this lets me go deeper into system-level performance data than my past roles required, on my own initiative.

## How I plan to achieve it

- **Data sourcing:** WHO Global Health Observatory API / CSV exports, World Bank Open Data API. Starting with a manageable slice (e.g. 15–20 countries, 5–8 indicators) rather than everything, so the analysis stays focused and finishable.
- **SQL:** normalise the data into a simple relational schema (countries, indicators, years), write queries that answer specific questions (e.g. "which countries spend more but see worse outcomes?").
- **Python:** pandas for cleaning/merging, matplotlib/seaborn for exploratory visuals, basic statistical checks (correlation, trend) - not building a novel model, just rigorous analysis.
- **Dashboard:** whichever of Power BI/Tableau I'm faster in, prioritising a small number of clear, interactive views over a cluttered dashboard.
- **Briefing doc:** written last, once findings are clear — forces the analysis to actually produce a "so what," not just charts.
- **Process:** built iteratively, day by day, with a dev diary (`docs/DEVLOG.md`) documenting decisions and learning as I go, and daily commits so progress is visible.

## How this is applicable beyond global health

The method here - diagnose a system using available data, find where performance diverges from expectation, prioritise recommendations by impact and feasibility - is domain-agnostic. The same workflow applies to:
- Retail: store performance vs. spend/staffing
- Operations: service delivery vs. resourcing (directly mirrors my Phoenix Futures KPI work)
- Any consultancy engagement involving a client's operational or performance data

I'm using health data because it's what I know and public data is available, but I want this to read as "I can do this workflow with any dataset," not "I only do healthcare."

## Potential issues I may run into

- **Data quality/gaps:** public health datasets often have missing years or inconsistent country coverage - I'll need to decide how to handle gaps (exclude vs. interpolate) and document that decision rather than hide it.
- **Correlation vs. causation:** with observational cross-country data, it'll be tempting to over-claim ("X causes Y") - I need to be disciplined about stating findings as associations unless there's a clear reason otherwise.
- **Scope creep:** global health data is enormous; the risk is trying to cover too many indicators/countries and never finishing. Mitigation: fix the scope in Day 2 and treat additions as a "future work" list, not mid-project expansions.
- **Tool unfamiliarity:** I'm stronger in some tools than others (per my CV, Power BI/Tableau breadth varies) - budgeting extra time for whichever dashboard tool I'm less fluent in.
- **Time consistency:** the whole point is daily visible progress; the risk is a busy day breaking the chain. Mitigation: even a 10-minute "read data, note next step" commit counts - the diary entry that day can just say so honestly.

## Status
🚧 Planning complete. Day 1–2 spent on repo setup; data sourcing begins Day 3.
