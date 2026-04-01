# Investigating Regional Playstyle Differences in Professional Valorant Esports

**Author:** Abdurrahmaan  
**Module:** CTEC3451 Development Project  
**Supervisor:** Aisha  
**Institution:** De Montfort University  

---

## Project Overview

This project investigates whether professional Valorant teams from different VCT regions demonstrate statistically significant differences in playstyle based on match statistics.

Data was scraped from VLR.gg covering three VCT 2025 international tournaments:
- Masters Bangkok 2025
- Masters Toronto 2025
- Champions 2025

The dataset contains **183 professional players** across four VCT regions: **Americas, EMEA, Pacific, and CN**.

---

## Research Question

> Do professional Valorant teams from different VCT regions demonstrate statistically significant differences in playstyle based on match statistics?

---

## Key Findings

- **KAST%** showed statistically significant regional differences (Kruskal-Wallis: H=23.092, p=0.0000)
- **HS%** showed statistically significant regional differences (Kruskal-Wallis: H=15.314, p=0.0016)
- **CN** is the most distinct region — significantly lower KAST% than all other regions
- **Americas** has significantly lower HS% compared to all other regions
- **Pacific** leads in ACS and KPR — highest raw fragging output

---

## Repository Structure

| File | Description |
|---|---|
| `VCT_Data_Collection.ipynb` | Data scraping, cleaning and statistical analysis pipeline |
| `VCT_Interactive_Explorer.ipynb` | Interactive analysis notebook with filters and visualisations |
| `vct_2025_clean.csv` | Cleaned dataset — 183 players, 24 columns |
| `vct_2025_stats.csv` | Raw scraped stats before cleaning |
| `regional_heatmap.png` | Normalised regional performance heatmap |
| `kast_hs_boxplots.png` | KAST% and HS% box plots by region |
| `violin_plots.png` | KAST% and HS% violin plots by region |
| `all_metrics_bar.png` | All metrics bar charts by region |

---

## Technologies Used

- **Python 3** — core language
- **Pandas** — data manipulation
- **Matplotlib / Seaborn** — visualisation
- **SciPy** — statistical testing (Kruskal-Wallis, Mann-Whitney U)
- **BeautifulSoup / Requests** — web scraping
- **ipywidgets** — interactive notebook widgets
- **scikit-learn** — data normalisation
- **Jupyter Notebook** — development environment

---

## How to Run

### Local (Jupyter)
1. Clone the repository
2. Install dependencies: `pip install pandas matplotlib seaborn scipy requests beautifulsoup4 ipywidgets scikit-learn adjustText`
3. Open `VCT_Interactive_Explorer.ipynb` in Jupyter Notebook
4. Run all cells

### Google Colab
Open the notebook directly in Google Colab — the first cell automatically downloads the dataset from GitHub.

---

## Performance Metrics Explained

| Metric | Full Name | Description |
|---|---|---|
| ACS | Average Combat Score | Overall round impact score |
| ADR | Average Damage per Round | Damage dealt per round |
| KAST% | Kill/Assist/Survive/Trade % | Round contribution consistency |
| KPR | Kills per Round | Average kills per round |
| APR | Assists per Round | Average assists per round |
| FKPR | First Kills per Round | Aggression/entry fragging rate |
| FDPR | First Deaths per Round | Entry risk rate |
| HS% | Headshot Percentage | Aiming style indicator |