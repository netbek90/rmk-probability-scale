markdown
# RMK Probability Scale

## what
Aim to get some visualisation what clearly shows probability chances: 0.05, 0.41 etc.

## Source
Data is taken from (https://opendata.riik.ee) — ds "Metsa- ja maastikutulekahjud 2014–2025" (Päästeamet) 
`data/fires.csv`

##what counted
- Probability that fire is in forest/landscape
- Probability by counties
- Probability by months
- Mean and median value of fire square

##how to run
```bash
pip install -r requirements.txt
python process.py        # counts probabilities → output/probabilities.csv
python visualize.py      # plot draw → output/probability_scale.png
example
https://output/probability_scale.png

Project structure
text
RMK/
├── data/
│   └── fires.csv                    # raw data
├── output/
│   ├── probabilities.csv            # Probabilities
│   └── probability_scale.png        # plot
├── explore.py                       # data exploration
├── process.py                       # counting of probabilities
├── visualize.py                     # plot draw
├── requirements.txt
├── README.md
└── thoughts.md                      # for future improvements
Contact
[vassi.djakov@gmail.com]

text



---
