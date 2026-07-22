# Dev Diary - Global Health System Performance Diagnostic

This is my day-by-day build log: what I did, what I decided and why, what I learned, and what confused me. Kept honest and in my own words - this is as much for interviews as it is for the repo.

---

## Day 1 - Project Setup
**Date:** 12 July 2026

**What I did:**
Set up my GitHub account and profile, created the global-health-diagnostic repo, and uploaded the initial README, which frames the project as a consultancy-style diagnostic rather than just a data project - situation to diagnosis to recommendations.

**Why I made that choice:**
I was torn between a pure global health project and something that reads as "business improvement" for consultancy applications. Landed on framing global health data as a consultancy engagement - same skill set (diagnose, quantify, recommend), just applied to health system data instead of a corporate client. Keeps it authentic to my WHO/Phoenix Futures background while still speaking to generalist consultancy/analyst roles.

**What I learned:**
Set up my GitHub profile and started the project repo. Learned that GitHub's browser "Upload files" button creates a commit automatically, even without using Terminal - every save is a snapshot in the project's history. Hadn't touched the actual Git command line yet at this point.

**What confused me / what I'd do differently:**
The difference between uploading files through the browser vs using Git commands in Terminal - wasn't clear at first that both do the same underlying thing (create a commit), just through different interfaces. Also got stuck trying to create a docs/ folder through drag-and-drop upload - ended up using "Create new file" with a full file path instead, which turned out to be the fix.

**Next up:**
Day 2 - source real data from WHO/World Bank into data/raw.

---

## Day 2 - Finishing Repo Setup
**Date:** 13 July 2026

**What I did:**
Uploaded the remaining project files to GitHub via the browser - docs/ROADMAP.md, docs/progress-log.md, and .gitignore at the repo root. Verified the folder structure matches the plan and that links in the README actually resolve.

**Why I made that choice:**
Realised the initial repo only had the README committed - the rest of the planned structure wasn't actually live yet. Wanted the repo in a clean, complete state before starting real analysis work, so anyone visiting it now sees the full picture, not a half-finished shell.

**What I learned:**
GitHub's "Upload files" button doesn't let you specify a folder path, but "Create new file" does - typing a path like docs/ROADMAP.md in the filename box auto-creates the folder. Also learned what .gitignore actually does: it tells Git to permanently ignore certain files (temp files, secrets) so they never get committed by mistake.

**What confused me / what I'd do differently:**
Wasn't sure at first whether .gitignore needed to go inside docs/ or at the root - it's root-level, since it applies to the whole project, not one folder.

**Next up:**
Day 3 - source real WHO/World Bank health data into data/raw.

---

## Day 3 - First Real Data Pull
**Date:** 14 July 2026

**What I did:**
Set up a local Python environment (Python, VS Code, a virtual environment) and wrote my first Python script, which calls the World Bank API to pull four health system indicators (health expenditure per capita, life expectancy, maternal mortality ratio, physicians per 1,000 people) across 15 countries, and saves the result as a clean CSV.

**Why I made that choice:**
Chose the World Bank API over manually downloading CSVs from their website because it's reproducible - anyone (including a future me) can re-run the script and get fresh data, rather than a one-off manual download. That's a stronger, more realistic demonstration of a data pipeline than a static file.

**What I learned:**
What an API actually is (a way for code to request data directly from a service, instead of clicking through a website) and how to call one using Python's requests library. Also learned what a virtual environment is and why it matters (keeps each project's installed packages separate, so projects don't conflict).

**What confused me / what I'd do differently:**
Hit a PowerShell security block when first activating the virtual environment (had to change the execution policy). Also discovered Git wasn't actually installed on this machine yet, despite having pushed files via the GitHub website already - realised browser uploads and local Git are two separate things.

**Next up:**
Day 4 - properly install and connect Git locally, then load this data into SQL.

---

## Day 4 - Git Setup, Debugging, and Loops
**Date:** 15 July 2026

**What I did:**
Properly installed Git and connected this local project to GitHub for the first time (previously all pushes went through the browser). Resolved a real merge conflict between local and GitHub history. Hit a bug in fetch_data.py where the script crashed partway through with a JSON error, diagnosed it by testing the failing API request directly in a browser, and fixed it by adding a short pause between requests plus better error handling.

**Why I made that choice:**
Rather than guessing at a fix for the crash, tested the actual API call outside the script first to isolate whether the problem was the API or the code - that ruled out one possibility before touching anything.

**What I learned:**
How to read a Python error message (from the bottom up), what a for loop actually does (repeats code once per item in a collection), what f-strings are for (inserting variable values into text), and the difference between a list and a dictionary. Also learned, the hard way, that git checkout --ours during a merge conflict discards the other side's changes entirely - which briefly caused some earlier diary entries to be lost before being recovered from Git's history.

**What confused me / what I'd do differently:**
Merge conflicts were genuinely confusing on a first encounter, and resolving one by just picking a side without carefully checking both versions caused real data loss that had to be manually recovered. Next time, would inspect both sides of a conflict properly before choosing one.

**Next up:**
Day 5 - load this data into SQL and start writing queries.

---

## Day 5 - Python Fundamentals
**Date:** 16 July 2026

**What I did:**
Spent time solidifying core Python concepts - loops, dictionaries, f-strings - by reasoning through small examples rather than just running pre-written code. Also made a small README update reflecting the skills being built through the project.

**Why I made that choice:**
Realised understanding the code well enough to explain it matters more than just having it run - especially for interviews where I might be asked to walk through logic I've written.

**What I learned:**
How a for loop steps through a dictionary's items() one pair at a time, and how f-strings insert variable values into text.

**What confused me / what I'd do differently:**


## Day 6 - SQL Setup Begins
**Date:** 17 July 2026

**What I did:**
Started building load_to_sql.py to load the CSV data into a proper SQLite database, ready for writing SQL queries. Also went back and fixed a data quality gap in fetch_data.py - added a unit column so every value states what it's measured in (e.g. current US$, years, per 1,000 people), instead of just a bare number.

**Why I made that choice:**
Noticed the value column had no unit attached, which is a real gap - a recruiter or interviewer could reasonably ask "what currency/unit is this in," and the data itself should answer that, not just my memory of the source.

**What I learned:**
The difference between pd.to_csv() (save data to a file) and pd.read_csv() (load it back in) - they're mirror opposites. Also learned that a CSV is a flat, static file, while a SQL database is what actually lets you ask structured questions of the data (filter, sort, group).

**What confused me / what I'd do differently:**
Hit another transient API error partway through re-fetching data (same rate-limiting pattern as Day 4) - handled it calmly this time by just retrying, rather than treating it as a crisis.

**Next up:**
Day 7 - finish load_to_sql.py, write first real SQL queries.

---

## Day 7 - First Real SQL Queries
**Date:** 18 July 2026

**What I did:**
Finished load_to_sql.py - it now loads the CSV data into a real SQLite database (data/processed/health_data.db). Wrote my first SQL query to find the countries with the highest health expenditure per capita.

**Why I made that choice:**
My first version of the query technically ran without errors but wasn't actually useful - it returned the same country five times (different years) instead of comparing different countries. Fixed it by filtering to a single year, since "top 5 countries" only makes sense when comparing the same point in time.

**What I learned:**
The basic shape of a SQL query - SELECT (which columns), FROM (which table), WHERE (filter conditions), ORDER BY (sort), LIMIT (how many results). Also learned that a query running successfully doesn't mean it's answering the right question - the logic has to match what you're actually trying to find out, not just execute without errors.

**What confused me / what I'd do differently:**
Didn't immediately notice my first query's flaw until I looked closely at the actual output - a reminder to always sanity-check results, not just check that code ran.

**Next up:**
Day 8 - write a few more SQL queries covering the other indicators, then start comparing indicators against each other (e.g. spend vs life expectancy).

---

## Day 8 - Python Analysis and First Chart
**Date:** 20 July 2026

**What I did:**
Wrote a second SQL query (lowest life expectancy countries), then moved into real Python analysis - merged two query results together using pandas, calculated the correlation between health spend and life expectancy (0.59, a moderate positive relationship), and built a scatter chart with a trend line and log scale to visualise it. Embedded the chart directly in the README so it's visible on the repo homepage.

**Why I made that choice:**
A raw correlation number is hard to feel intuitively - visualising it makes the finding much clearer, and having it live in the README means anyone visiting the repo sees a real result immediately, not just code.

**What I learned:**
How pandas .merge() joins two tables together on a shared column (similar idea to a SQL JOIN, just done in Python). How .corr() calculates a correlation coefficient in one line. That a scatter plot's shape can be misleading if one outlier dominates the scale - fixed by using a log scale and adding a trend line, rather than trusting the first plain version.

**What confused me / what I'd do differently:**
Ran the script once before actually saving my code changes, which meant an early commit had zero real changes in it - a reminder to always double check the file is saved (no dot on the VS Code tab) before running or committing.

**Next up:**
Day 9 - identify specific countries that deviate from the spend/life-expectancy trend (over- and under-performers), and keep building out the SQL query set.

---

## Day 9 - Regression and Outlier Analysis
**Date:** 23 July 2026

**What I did:**
Extended the spend vs life expectancy analysis by using the regression line to calculate a predicted life expectancy for every country. Compared the predicted values with the actual values by calculating residuals, then ranked countries to identify the biggest overperformers and underperformers relative to their healthcare spending. The analysis highlighted countries such as Japan and Bangladesh as outperforming expectations, while the United States and Nigeria underperformed.

**Why I made that choice:**
The chart and correlation showed the overall relationship between spending and life expectancy, but they didn't explain which countries stood out from that trend. Calculating residuals turned the visual pattern into something measurable, making it possible to identify countries that may warrant further investigation.

**What I learned:**
What a linear regression actually represents - a line of best fit that predicts one variable from another. Also learned that a residual is simply the difference between the predicted value and the actual value, and that large positive or negative residuals are useful for identifying outliers. Began thinking more about interpreting results than simply producing charts.

**What confused me / what I'd do differently:**
Initially wasn't sure where to add the new code because the regression model had to exist before predictions and residuals could be calculated. Once I understood the order of the script, the logic became much clearer.

**Next up:**
Day 10 - expand the analysis using additional health indicators (such as maternal mortality and physician density), explore stronger visualisations, and begin developing evidence-based recommendations from the findings.

---

## Day 10 - [Title]
**Date:**

**What I did:**


**Why I made that choice:**


**What I learned:**


**What confused me / what I'd do differently:**


**Next up:**