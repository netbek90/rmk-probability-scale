import pandas as pd
import numpy as np

# ========== LOAD DATA ==========
df = pd.read_csv("data/fires.csv", sep="\t", encoding="utf-8")
df = df[df["mis_poles"].notna()].copy()
df["is_forest"] = df["mis_poles"] == "Mets"
df["date"] = pd.to_datetime(df["sundmuse_kuupaev_dt"], errors="coerce")
df["month"] = df["date"].dt.month

p_forest = df["is_forest"].mean()

# ========== BAYESIAN UPDATE FUNCTION ==========
def bayesian_update(df, condition_col, condition_value, target_col="is_forest"):
    """
    P(A|B) = P(B|A) * P(A) / P(B)
    A = target event (forest fire)
    B = condition (month, county, etc.)
    """
    p_a = df[target_col].mean()
    p_b = (df[condition_col] == condition_value).mean()
    true_subset = df[df[target_col] == True]
    p_b_given_a = (true_subset[condition_col] == condition_value).mean()
    p_a_given_b = (p_b_given_a * p_a) / p_b if p_b > 0 else 0
    return p_a_given_b, p_b_given_a, p_a, p_b

# ========== COLLECT RESULTS ==========
results = []

# Baseline
results.append({
    "condition": "BASELINE",
    "value": "—",
    "p_forest": round(p_forest, 4),
    "change": 0.0
})

# By month
month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}
for month in sorted(df["month"].dropna().unique()):
    month_name = month_names.get(int(month), f"Month {month}")
    p_upd, _, _, _ = bayesian_update(df, "month", month)
    results.append({
        "condition": "Month",
        "value": month_name,
        "p_forest": round(p_upd, 4),
        "change": round(p_upd - p_forest, 4)
    })

# By county (top 6)
for county in df["maakond"].value_counts().head(6).index:
    p_upd, _, _, _ = bayesian_update(df, "maakond", county)
    results.append({
        "condition": "County",
        "value": county,
        "p_forest": round(p_upd, 4),
        "change": round(p_upd - p_forest, 4)
    })

# ========== SAVE ==========
results_df = pd.DataFrame(results)
results_df.to_csv("output/bayes_results.csv", index=False)
print(f"Saved {len(results_df)} Bayesian estimates to output/bayes_results.csv")
print("Done!")