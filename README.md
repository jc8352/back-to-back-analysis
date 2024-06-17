# Analysis of Statistical Changes in Back-to-Back NBA Games

## Overview

This project aims to analyze whether there's a statistically significant change in four key metrics—3-point percentage, offensive rating, defensive rating, and win percentage—when NBA teams play back-to-back games. 

## Data Sources

- `data/2023_24_team_game_logs.csv`: Contains game logs for the 2023-2024 NBA season.
- `data/2023_24_team_rtgs.csv`: Contains advanced game logs for the 2023-2024 NBA season.

## Scripts

- `src/data_to_csv_nbacom.py`: Script to save data from NBA.com to CSV files. Script generates `data/2023_24_team_game_logs.csv` and `data/2023_24_team_rtgs.csv`.
- `src/team_3s_b2bs.py`: Script to analyze 3-point percentages for back-to-back games.
- `src/team_rtgs.py`: Script to analyze offensive and defensive ratings for back-to-back games. Script also generates:
    - `data/result/b2bs_rtgs_2023_24.csv`: Contains advanced game logs for back-to-back games.
    - `data/result/non_b2bs_rtgs_2023_24.csv`: Contains advanced game logs for non-back-to-back games.
- `src/team_winpct_b2bs.py`: Script to analyze win percentages for back-to-back games. Script also generates:
    - `data/result/b2bs_2023_24.csv`: Contains game logs for back-to-back games.
    - `data/result/non_b2bs_2023_24.csv`: Contains game logs for non-back-to-back games.

## Results

### Three-Point Shooting Analysis
- **Total 3s attempted on back-to-backs:** 14,818
- **Total 3s attempted on non back-to-backs:** 71,537
- **3pt shooting percentage on back-to-backs:** 36.58%
- **3pt shooting percentage on non back-to-backs:** 36.57%
- **Z-score:** 0.0231
- **P-value:** 0.4908

### Offensive and Defensive Ratings Analysis
- **Average defensive rating (dRTG) of teams on back-to-backs:** 115.72
- **Average offensive rating (oRTG) of teams on back-to-backs:** 113.61
- **Average non back-to-back dRTG:** 114.34
- **Average non back-to-back oRTG:** 114.77
- **Back-to-back dRTG variance:** 153.06
- **Back-to-back oRTG variance:** 143.54
- **Non back-to-back dRTG variance:** 136.84
- **Non back-to-back oRTG variance:** 138.90
- **dRTG Z-score:** 2.1082
- **oRTG Z-score:** -1.8303
- **dRTG P-value:** 0.0175
- **oRTG P-value:** 0.0336

### Win Percentage Analysis
- **Overall record of teams playing back-to-back games:** 186 - 236
- **Overall record of teams not playing back-to-back games:** 1044 - 994
- **Win percentage on back-to-backs:** 44.08%
- **Win percentage on non back-to-backs:** 51.23%
- **Z-score:** -2.6899
- **P-value:** 0.0036

## Conclusions

1. **Three-Point Shooting**: The 3-point shooting percentages for teams on back-to-back games (36.58%) and non-back-to-back games (36.57%) are nearly identical. The p-value (0.4908) indicates that the difference is not statistically significant.

2. **Offensive and Defensive Ratings**: 
    - The defensive rating (dRTG) for teams on back-to-backs (115.72) is higher than for non-back-to-back games (114.34), with a p-value of 0.0175, suggesting a statistically significant difference.
    - The offensive rating (oRTG) for teams on back-to-backs (113.61) is lower than for non-back-to-back games (114.77), with a p-value of 0.0336, also indicating a statistically significant difference.

3. **Win Percentage**: Teams playing back-to-back games have a win percentage of 44.08%, compared to 51.23% for non-back-to-back games. The p-value (0.0036) shows that this difference is statistically significant, indicating that teams are more likely to win when not playing on back-to-back days.

## Usage

1. **Save Data**:
    - Run `data_to_csv_nbacom.py` to save the game logs to CSV files in the data folder.

    ```bash
    cd src
    python3 data_to_csv_nbacom.py
    ```

2. **Analyze 3-Point Percentages**:
    - Run `team_3s_b2bs.py` to analyze the 3-point percentages for back-to-back games.

    ```bash
    cd src
    python3 team_3s_b2bs.py
    ```

3. **Analyze Offensive and Defensive Ratings**:
    - Run `team_rtgs.py` to analyze offensive and defensive ratings for back-to-back games.

    ```bash
    cd src
    python3 team_rtgs.py
    ```

4. **Analyze Win Percentages**:
    - Run `team_winpct_b2bs.py` to analyze win percentages for back-to-back games.

    ```bash
    cd src
    python3 team_winpct_b2bs.py
    ```


