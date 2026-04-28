import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#load probabilities
df = pd.read_csv("output/probabilities.csv")

#from min to max
df = df.sort_values("probability", ascending=True).reset_index(drop=True)

#style set
fig, ax = plt.subplots(figsize=(12, 6))

#colors
colors = {
    "Fire type": "#2F312F",
    "County": "#1565C0",
    "Season": "#E65100"
}
bar_colors = [colors.get(cat, "#757575") for cat in df["category"]]

#bar plot horizontal
bars = ax.barh(df["event"], df["probability"], color=bar_colors, edgecolor="white", height=0.6)
for bar, prob in zip(bars, df["probability"]):
    width = bar.get_width()
    if prob < 0.01:
        label = f"{prob*100:.2f}%"
    elif prob < 0.1:
        label = f"{prob*100:.1f}%"
    else:
        label = f"{prob*100:.0f}%"
    ax.text(width + 0.003, bar.get_y() + bar.get_height()/2, label, va='center', fontsize=11, fontweight='bold')


ax.set_xlabel("Probability", fontsize=13)
ax.set_title("Probability scale of fire (2014–2025)", fontsize=15, fontweight='bold', pad=15)

#log scale
ax.set_xlim(0, max(df["probability"]) * 1.25)
#ax.set_xlim(0.0005, 1)


ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x*100:.0f}%' if x < 1 else f'{int(x*100)}%'))

#legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#2F312F", label="Fire type"),
    Patch(facecolor="#1565C0", label="County"),
    Patch(facecolor="#E65100", label="Season")
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=10)

#grid set
ax.grid(axis="x", alpha=0.3, linestyle="--")

plt.tight_layout()
plt.savefig("output/probability_scale.png", dpi=150, bbox_inches="tight")
print("Plot saved in output/probability_scale.png")