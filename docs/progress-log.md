# Progress Log

Daily build log for the Global Health System Performance Diagnostic project.

## Day 1 - Project setup
- Created repo structure (data/sql/notebooks/dashboard/docs)
- Defined project objective and consultancy-style framing
- Set up README and .gitignore

## Day 2 - Repo setup completed
- Uploaded roadmap, progress log, dev diary, and .gitignore
- Verified full folder structure and working links

## Day 3 - First data pull
- Set up Python, VS Code, and a virtual environment locally
- Wrote a script to pull World Bank health indicators via API
- Added first real dataset to the repo

## Day 4 - Git setup and bug fix
- Installed Git locally and connected the project to GitHub for the first time
- Resolved a merge conflict between local and GitHub history
- Fixed a rate-limiting bug in the data fetch script
- Learned to read

## Day 5 - Python fundamentals practice
- Practiced core Python concepts: loops, dictionaries, f-strings
- Small README update

## Day 6 - SQL setup and data quality fix
- Added a unit column to indicator data for clarity (currency, years, per-1000, etc.)
- Started building a script to load data into a SQLite database

## Day 7 - First SQL queries
- Finished loading data into a SQLite database
- Wrote and debugged first real SQL query (top health spenders by country)
- Learned to sanity-check query logic, not just check for errors

## Day 8 - Python analysis and visualization
- Added a second SQL query (lowest life expectancy countries)
- Calculated correlation between health spend and life expectancy (0.59)
- Built and refined a scatter chart (log scale, trend line), embedded in README

## Day 9 - Regression and outlier analysis
- Extended the analysis by fitting a linear regression model
- Calculated predicted life expectancy and residuals for each country
- Identified the top overperforming and underperforming countries relative to health spending
- Learned how residuals can be used to identify meaningful outliers

## Day 10 - Physicians query and a good catch
- Wrote a third SQL query independently (physicians per 1,000 people)
- Caught an incorrect assumption in an explanation and verified it - reinforced good analytical habits

## Day 11 - First independent query
- Wrote a SQL query and Python wrapper largely independently
- Confirmed real data gaps in the physicians indicator (9 of 16 countries missing 2023 data)

## Day 12 - Functions and refactoring
- Learned functions, parameters/arguments, local vs global variables
- Refactored repeated query code into a single reusable function

## Day 13 - If statements and full labeling
- Learned if/else statements and applied them via a new function
- Labeled all 16 countries as over/underperforming, not just the top 3

## Day 14 - Power BI dashboard started
- Exported analysis data to CSV, imported into Power BI
- Built first chart (residuals by country) with color formatting

## Day 15 - Power BI dashboard development
- Started building an interactive Power BI dashboard
- Imported analysed dataset and created first spend vs life expectancy scatter plot
- Began transitioning the project from code-based analysis into a stakeholder-facing diagnostic tool

## Day 16 - Scatter plot sizing, Power BI cache bug, and dashboard review
- Added residual_magnitude column for scatter plot circle sizing
- Colored scatter plot by performance category with custom colors
- Diagnosed and fixed a stubborn Power BI caching bug via filename rename
- Reviewed finished dashboard - two working charts telling a clear diagnostic story

## Day 17 - Dashboard polish and captions
- Cleaned up chart titles and legend labels
- Wrote and refined data-driven captions for both charts through multiple iterations
- Corrected a caption accuracy issue (referencing data not shown on that chart)

## Day 18 - Physician density analysis begins
- Added SQL queries to explore physician density data availability
- Found that only 8 of 16 countries had physician density data available for 2023
- Removed missing values and created a clean physician density vs life expectancy dataset using pandas merge
- Prepared the dataset for correlation and regression analysis

## Day 19 - Physician density residual analysis
- Calculated physician density correlation (0.82) and residuals, largely independently
- Found physician density predicts outcomes more strongly than spend
- Confirmed Nigeria/Bangladesh as consistent outliers across two different indicators

## Day 20 - Back on track, third chart started
- Confirmed retention after a break (4/4 on core concepts)
- Exported physician density analysis, imported into Power BI
- Resized canvas, started building third chart (physician density residuals)

## Day 21 - Third chart formatting
- Applied gradient color formatting to the physician density chart, matching the first bar chart's style

## Day 22 - Third chart complete
- Added title and caption to physician density chart
- Fixed axis labeling and highlighted key countries
- All three dashboard charts now complete (titles, formatting, captions)