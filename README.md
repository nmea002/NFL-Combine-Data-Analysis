# TE and WR NFL Combine Data Analysis 

Analyzing the relationship between combine performance and career stats for TEs and WRs.

## Table of Contents
- [Dataset](#dataset)
- [Approach](#approach)
- [Results](#results)
- [Dataset Creation Guide](#dataset-creation-guide)
- [Next Steps](#next-steps)
  
## Dataset
First, I scraped [NFL Draft Data](https://www.pro-football-reference.com/years/2020/draft.htm) for career stats and [NFL Combine Data](https://www.pro-football-reference.com/draft/2020-combine.htm) for combine performance stats from 2000 to 2020. Then I merged the two datasets using an inner merge to focus on players who were drafted and performed in the combine. 

## Approach
1. Research Question: Does strong combine performance predict NFL success?
2. Position Focus: Narrowed the scope to Wide Receivers and Tight Ends.
3. Defined Success:
   - NFL Success = Receiving yards per game.
   - Combine Success = 40-yard dash time (for WR and TEs in particular).
4. Methodology:
   - Scraped and merged combine and career data from 2000 - 2020.
   - Focused only on players who participated in both the combine and draft.

## Results 
[Tableau Dashboard](https://public.tableau.com/views/HowNFLCombineResultsPredictReceivingYardsperGameforTEsandWRs/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Dataset Creation Guide
1. Run `careersScrape.py`
2. Run `combineScrape.py`
3. Run all cells of `analysis.ipynb`
4. Have fun conducting you own analysis!

## Next Steps
- Expanding my analysis to players who were drafted but did not perform in the combine and vice versa.
- Adding more career performance stats like receiving yards per reception.
- Expanding my analysis to more positions. 
