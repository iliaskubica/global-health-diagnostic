# Dev Diary — Global Health System Performance Diagnostic

This is my day-by-day build log: what I did, what I decided and why, what I learned, and what confused me. Kept honest and in my own words — this is as much for interviews as it is for the repo.

---

## Day 1 — Project Setup
**Date:** 12 July 2026

**What I did:**
Set up my GitHub account and profile, created the `global-health-diagnostic` repo, and uploaded the initial README, which frames the project as a consultancy-style diagnostic rather than just a data project — situation → diagnosis → recommendations.

**Why I made that choice:**
I was torn between a pure global health project and something that reads as "business improvement" for consultancy applications. Landed on framing global health data *as* a consultancy engagement — same skill set (diagnose, quantify, recommend), just applied to health system data instead of a corporate client. Keeps it authentic to my WHO/Phoenix Futures background while still speaking to generalist consultancy/analyst roles.

**What I learned:**
Set up my GitHub profile and started the project repo. Learned that GitHub's browser "Upload files" button creates a commit automatically, even without using Terminal — every save is a snapshot in the project's history. Haven't touched the actual Git command line yet.

**What confused me / what I'd do differently:**
The difference between uploading files through the browser vs. using Git commands in Terminal — wasn't clear at first that both do the same underlying thing (create a commit), just through different interfaces. Also got stuck trying to create a `docs/` folder through drag-and-drop upload — ended up using "Create new file" with a full file path instead, which turned out to be the fix.

**Next up:**
Day 2 — source real data from WHO/World Bank into `data/raw`.

---

## Day 2 — Finishing Repo Setup
**Date:** 13 July 2026

**What I did:**
Uploaded the remaining project files to GitHub via the browser — docs/ROADMAP.md, docs/progress-log.md, and .gitignore at the repo root. Verified the folder structure matches the plan and that links in the README actually resolve.

**Why I made that choice:**
Realised the initial repo only had the README committed — the rest of the planned structure wasn't actually live yet. Wanted the repo in a clean, complete state before starting real analysis work, so anyone visiting it now sees the full picture, not a half-finished shell.

**What I learned:**
GitHub's "Upload files" button doesn't let you specify a folder path, but "Create new file" does — typing a path like docs/ROADMAP.md in the filename box auto-creates the folder. Also learned what .gitignore actually does: it tells Git to permanently ignore certain files (temp files, secrets) so they never get committed by mistake.

**What confused me / what I'd do differently:**
Wasn't sure at first whether .gitignore needed to go inside docs/ or at the root — it's root-level, since it applies to the whole project, not one folder.

**Next up:**
Day 3 — source real WHO/World Bank health data into data/raw.
<!-- Copy the block above for each new day -->

## Day 3 — [Title]
**Date:**

**What I did:**


**Why I made that choice:**


**What I learned:**


**What confused me / what I'd do differently:**


**Next up:**
