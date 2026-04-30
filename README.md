# RMK Probability Scale

Test assignment for RMK Data Team Internship 2026.

## What is this

A probability scale for forest and landscape fires in Estonia (2014-2025).
The goal is to help readers intuitively understand probability values like 0.05, 0.41, etc.

## Data source

Data from [Estonian Open Data Portal](https://opendata.riik.ee) — dataset "Metsa- ja maastikutulekahjud 2014-2025" (Päästeamet, Estonian Rescue Board).
File: `data/fires.csv`, 11 757 fire incident records.

## What was calculated

- Probability that a fire is forest vs. landscape
- Probability of fire by county (Harju, Ida-Viru, etc.)
- Probability of fire by month (seasonality)
- Mean and median burned area of forest fires

## How to run

```bash
pip install -r requirements.txt
python process.py        # calculates probabilities → output/probabilities.csv
python visualize.py      # draws scale → output/probability_scale.png
Example result
https://output/probability_scale.png

Project structure
text
RMK/
├── data/
│   └── fires.csv                    # raw data
├── output/
│   ├── probabilities.csv            # calculated probabilities
│   └── probability_scale.png        # finished scale
├── explore.py                       # data exploration
├── process.py                       # probability calculations
├── visualize.py                     # scale visualization
├── bayes.py                     # bayes apply
├── README.md
└── thoughts.md                      # future improvements

Contact
vassi.djakov@gmail.com