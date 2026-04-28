import pandas as pd

#load df
df = pd.read_csv("data/fires.csv", sep="\t", encoding="utf-8")
print(f"rows loaded: {len(df)}")

#metsatulekhaju probability
#mis_poles empty remove
known_type = df[df["mis_poles"].notna()]
total_known = len(known_type)
forest_fires = len(known_type[known_type["mis_poles"] == "Mets"])
landscape_fires = len(known_type[known_type["mis_poles"] == "Maastik"])

prob_forest = forest_fires / total_known
prob_landscape = landscape_fires / total_known

print(f"\nfire_type")
print(f"Forest: {forest_fires}, Landscape: {landscape_fires}")
print(f"Probabilty of Forest fire: {prob_forest:.4f}")
print(f"Probabilty of Landsvape fire: {prob_landscape:.4f}")

#Probability by county
county_counts = df["maakond"].value_counts()
total_fires = len(df)
county_probs = county_counts / total_fires

print(f"\ntop5countiesbyfire")
for county, prob in county_probs.head(5).items():
    print(f"{county}: {prob:.4f} ({int(county_counts[county])} fires)")

#monthly probabilities
df["date"] = pd.to_datetime(df["sundmuse_kuupaev_dt"], errors="coerce")
df["month"] = df["date"].dt.month
month_counts = df["month"].value_counts().sort_index()
month_probs = month_counts / month_counts.sum()

month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

print(f"\nmonthly probabilities")
for m, prob in month_probs.items():
    name = month_names.get(int(m), f"Month {m}")
    print(f"{name}: {prob:.4f}")

#avrage square of fire
forest_data = df[df["mis_poles"] == "Mets"].copy()
avg_forest_area = forest_data["metsa_polenud_pind_alates_25_05_2021"].mean()
median_forest_area = forest_data["metsa_polenud_pind_alates_25_05_2021"].median()

print(f"\nsquare of fires")
print(f"Mean: {avg_forest_area:.1f} га")
print(f"median: {median_forest_area:.1f} га")

#results
#table of probabilities
results = []

results.append({
    "event": "Forest fire",
    "probability": round(prob_forest, 4),
    "category": "Type of fire"
})
results.append({
    "event": "Lanscape fire",
    "probability": round(prob_landscape, 4),
    "category": "Type of fire"
})

#from counties
for county, prob in county_probs.head(3).items():
    results.append({
        "event": f"Fire in county {county}",
        "probability": round(prob, 4),
        "category": "County"
    })

#most rare(small?) county
for county, prob in county_probs.tail(1).items():
    results.append({
        "event": f"Fire in county {county} rarest",
        "probability": round(prob, 4),
        "category": "County"
    })

#by months
most_dangerous_month = month_probs.idxmax()
safest_month = month_probs.idxmin()
results.append({
    "event": f"Fire in {month_names[int(most_dangerous_month)]} most dangerous season",
    "probability": round(month_probs.max(), 4),
    "category": "Season"
})
results.append({
    "event": f"Fire in {month_names[int(safest_month)]} least dangerous season",
    "probability": round(month_probs.min(), 4),
    "category": "Season"
})

#save df
results_df = pd.DataFrame(results)
results_df.to_csv("output/probabilities.csv", index=False)
print(f"\nSaved {len(results_df)} probabilities output/probabilities.csv")
print("Done!")