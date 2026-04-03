# Dissertation Scaffold
## Investigating Regional Playstyle Differences in Professional Valorant Esports
**Abdurrahmaan Lakhota | P2799674 | BSc Computer Science | CTEC3451**
**Target: 10,000–12,000 words | Harvard Referencing**

---

## Word Count Targets

| Chapter | Target Words |
|---|---|
| 1. Introduction | 800–1,000 |
| 2. Literature Review | 2,500–3,000 |
| 3. Methodology | 1,500–2,000 |
| 4. Results | 2,000–2,500 |
| 5. Discussion | 2,000–2,500 |
| 6. Conclusion | 500–700 |
| References | (not counted) |
| **Total** | **~10,300–11,700** |

---

## Chapter 1 — Introduction (~800–1,000 words)

### 1.1 Background and Motivation
- Brief intro to Valorant and the VCT ecosystem
- Mention the four regions: Americas, EMEA, Pacific, CN
- Growing size of esports as an industry; data availability
- Personal motivation (active Valorant player, follows VCT)

### 1.2 Research Question
> Do professional Valorant teams from different VCT regions demonstrate statistically
> significant differences in playstyle based on match statistics?

### 1.3 Aims and Objectives
- Restate aim: investigate regional playstyle differences using VCT 2025 international data
- List objectives 1–7 (from project contract — keep concise, 1 sentence each)

### 1.4 Scope and Limitations
- Scope: VCT 2025 international tournaments only (Masters Bangkok, Masters Toronto, Champions 2025)
- 183 professional players across 4 regions
- Data source: VLR.gg (publicly available, web-scraped)
- Limitations: no agent-level breakdown per map, no live patch data, no team-level aggregation

### 1.5 Dissertation Structure
- One paragraph overview of each chapter (standard signposting)

---

## Chapter 2 — Literature Review (~2,500–3,000 words)

> **Note:** Draft already written. Use this structure to organise/expand it.

### 2.1 Esports as an Academic Domain
- Growth of esports analytics as a research area
- Cite: Seif El-Nasr et al. (2013) *Game Analytics* — foundational text
- Why competitive FPS games are valuable for data-driven research
- Contrast with traditional sports analytics (briefly)

### 2.2 Performance Metrics in Competitive Games
- Review of metrics used in esports analytics literature
- Focus on FPS-specific metrics: K/D ratio, damage, utility usage
- Cite studies on CS:GO or similar tactical shooters where available
- Introduce Valorant-specific metrics: ACS, ADR, KAST%, FKPR, FDPR, HS%
- Explain why these are valid proxies for playstyle

### 2.3 Win/Loss Prediction and Match Outcome Research
- Existing work on predicting match outcomes in esports (LoL, Dota 2, CS:GO)
- Gap: limited work on Valorant specifically
- Reference any Valorant-specific analytics papers if available

### 2.4 Regional Differences in Competitive Gaming
- Evidence of regional meta differences in LoL (Korean vs Western playstyle literature)
- Concept of "regional meta" — different strategic tendencies across regions
- Limited academic work on Valorant regional differences — this project fills the gap

### 2.5 Statistical Methods in Esports Analytics
- Non-parametric testing rationale (data not always normally distributed)
- Kruskal-Wallis as regional comparison tool
- Mann-Whitney U for pairwise post-hoc comparisons
- Cite relevant stats methodology sources (e.g., Field, 2018 — *Discovering Statistics Using IBM SPSS*)

### 2.6 Summary and Research Gap
- Summarise what the literature covers
- Identify the gap: no study examines VCT 2025 international data for regional playstyle differences using statistical testing
- Position this project within that gap

---

## Chapter 3 — Methodology (~1,500–2,000 words)

### 3.1 Research Design
- Quantitative, exploratory research design
- Justify: large structured dataset, statistical testing appropriate
- Deductive approach: hypothesise regional differences, test with data

### 3.2 Data Collection
- Source: VLR.gg — publicly available professional match statistics
- Method: web scraping using Python (BeautifulSoup, Requests)
- Events scraped: Masters Bangkok 2025, Masters Toronto 2025, Champions 2025
- Justification for choosing international events only: consistent competition level, all 4 regions represented

### 3.3 Dataset Description
- 183 player records, 24 variables
- Variables collected: ACS, ADR, KAST%, KPR, APR, FKPR, FDPR, HS%, K:D, Agents, Team, Region, Event, Rounds
- Regional distribution: Americas (45), EMEA (47), Pacific (46), CN (45) — near-balanced

### 3.4 Data Cleaning and Preprocessing
- Removal of non-VCT rows (e.g., content creator scrimmage data)
- Type conversion: percentage strings → floats (KAST%, HS%)
- Handling missing values: ~25 cells (mostly CL% — excluded from analysis)
- Region mapping: hard-coded team-to-region dictionary, validated manually

### 3.5 Analytical Approach
- Stage 1 — Exploratory Data Analysis (EDA): regional means, distributions, correlation
- Stage 2 — Statistical Testing:
  - Kruskal-Wallis H-test: non-parametric one-way ANOVA across 4 regions
  - Mann-Whitney U: pairwise post-hoc comparisons between region pairs
  - Significance threshold: α = 0.05
- Justify non-parametric choice: Shapiro-Wilk test / visual inspection showed non-normal distributions

### 3.6 Visualisation Tools
- Matplotlib and Seaborn: bar charts, box plots, violin plots, heatmaps
- scikit-learn MinMaxScaler: normalised heatmap (0–1 scale for cross-metric comparison)
- ipywidgets + Plotly: interactive notebook dashboard

### 3.7 Ethical Considerations
- All data publicly available on VLR.gg — no personal data collected
- No player identifiers beyond professional alias (publicly known)
- No commercial use; academic research only

---

## Chapter 4 — Results (~2,000–2,500 words)

> **Tip:** Let the data lead. Report findings objectively — save interpretation for Chapter 5.

### 4.1 Descriptive Statistics
- Table: mean ± std dev for each metric by region (ACS, ADR, KAST%, KPR, APR, FKPR, FDPR, HS%)
- Highlight notable patterns (e.g., Pacific leads ACS, CN lowest KAST%)
- Reference: regional heatmap figure (regional_heatmap.png)

### 4.2 Exploratory Data Analysis
- Box plots: KAST% and HS% by region — show spread and outliers
  - Reference: kast_hs_boxplots.png
- Violin plots: distribution shape by region
  - Reference: violin_plots.png
- Bar charts: all 8 metrics by region
  - Reference: all_metrics_bar.png
- Key observations to note:
  - CN shows lower KAST% median with higher variance
  - Americas shows lower HS% consistently
  - Pacific shows highest ACS and KPR
  - EMEA shows most balanced profile across metrics

### 4.3 Statistical Testing — Kruskal-Wallis Results
Present as a table:

| Metric | H-statistic | p-value | Significant? |
|---|---|---|---|
| ACS | — | — | — |
| ADR | — | — | — |
| KAST% | 23.092 | <0.001 | Yes |
| KPR | — | — | — |
| APR | — | — | — |
| FKPR | — | — | — |
| FDPR | — | — | — |
| HS% | 15.314 | 0.0016 | Yes |

*(Fill in remaining values from notebook output)*

### 4.4 Post-Hoc Pairwise Comparisons (Mann-Whitney U)
- For KAST%: which region pairs are significantly different?
  - CN vs Americas, CN vs EMEA, CN vs Pacific (expected significant)
- For HS%: which region pairs differ?
  - Americas vs others (expected significant)
- Present as pairwise table or bullet points with p-values

### 4.5 Summary of Findings
- KAST% and HS% show statistically significant regional differences
- Most other metrics (ACS, ADR, KPR) show descriptive differences but not statistically significant at α=0.05
- CN and Americas are most distinct from the overall group

---

## Chapter 5 — Discussion (~2,000–2,500 words)

### 5.1 Interpretation of KAST% Findings
- CN's significantly lower KAST% suggests more aggressive, trade-heavy playstyle
- Lower KAST% = players more willing to die without contributing a kill/assist/trade/survive
- Links to CN regional meta reputation for aggressive duelling
- Compare to literature on aggressive vs utility-focused playstyles in tactical shooters

### 5.2 Interpretation of HS% Findings
- Americas' lower HS% may reflect greater reliance on utility/body damage (spray control, smokes)
- Alternatively: Americas teams may use spray-heavy weapons more (operator, rifles at close range)
- CN's higher HS% could reflect aim-training culture emphasis
- Link to player development culture differences across regions

### 5.3 Non-Significant Metrics
- ACS, ADR, KPR, FKPR, FDPR show no statistically significant regional differences
- Interpretation: raw fragging output is similar across regions at international level
- Suggests top-tier players globally converge on similar mechanical output
- Regional differences emerge in *style* (KAST, HS) rather than *volume* (ACS, ADR)

### 5.4 Contextual Factors
- Sample size: 183 players across 3 events — moderate; results should be interpreted cautiously
- Tournament format: single-elimination stages may inflate variance (less data per player)
- Patch differences: VCT 2025 had agent balance changes between Bangkok and Champions — may affect metrics
- Agent pool: different regions favour different agents which may skew metrics (e.g., support agents inflate APR)

### 5.5 Relation to Existing Literature
- Findings partially consistent with LoL regional meta literature (Kim et al.) — regional styles do differ
- Inconsistent with studies suggesting top-level competition homogenises playstyle
- No direct prior Valorant comparison available — this project's findings are novel

### 5.6 Limitations
- Web-scraped data: VLR.gg may have minor inconsistencies (noted ~25 missing cells)
- Per-map granularity not captured — map pool affects playstyle
- No agent-level analysis — agent selection likely confounds HS% and APR
- Cross-sectional snapshot: one year of data; trends over time not examined

---

## Chapter 6 — Conclusion (~500–700 words)

### 6.1 Summary of Work
- Restate research question and approach (1–2 sentences each)
- Data collected, cleaned, and analysed for 183 players across 3 VCT 2025 international events

### 6.2 Key Findings
- Two metrics (KAST% and HS%) show statistically significant regional differences
- CN most distinct: lower KAST%, higher HS% — aggressive, aim-focused playstyle
- Americas most distinct on HS%: lower headshot rate — utility/spray playstyle
- Pacific leads raw fragging metrics (ACS, KPR) but differences not statistically significant

### 6.3 Contributions
- First study to apply statistical testing to VCT 2025 international tournament data
- Provides evidence that regional playstyle differences exist in professional Valorant
- Interactive Jupyter Notebook provides reusable tool for ongoing VCT analysis

### 6.4 Future Work
- Extend dataset to include regional league data (not just international events)
- Incorporate agent-level analysis to control for role confounding
- Longitudinal analysis: track regional metric trends across VCT 2023, 2024, 2025
- Apply clustering (e.g., k-means) to identify playstyle archetypes beyond region

### 6.5 Reflection
- Brief personal reflection on challenges (scraping, region mapping, statistical choices)
- What would be done differently (e.g., collect map-level data from the start)

---

## References

> Use Harvard referencing throughout. Minimum 15 sources with valid DOIs.
> Suggested sources to include:

- Seif El-Nasr, M., Drachen, A. and Canossa, A. (eds.) (2013) *Game Analytics: Maximising the Value of Player Data*. London: Springer. 
- McKinney, W. (2022) *Python for Data Analysis*. 3rd edn. Sebastopol: O'Reilly Media.
- Field, A. (2018) *Discovering Statistics Using IBM SPSS Statistics*. 5th edn. London: SAGE.
- [IEEE CIG papers on esports analytics — search Google Scholar]
- [FDG / AAAI AIIDE papers on player behaviour — search Google Scholar]
- [CS:GO or LoL regional playstyle papers — search IEEE Digital Library]

---

## Appendices (if needed, not counted in word count)

- A: Full statistical test output tables
- B: Data cleaning pipeline code (key sections)
- C: Kruskal-Wallis and Mann-Whitney U full results
