import pandas as pd

# Load raw data
df = pd.read_csv("input_data.csv")

# Clean data
df.dropna(inplace=True)
df["Price"] = df["Price"].astype(float)

# Simple automation logic
df["Total"] = df["Quantity"] * df["Price"]

# Export to Excel
df.to_excel("output_cleaned.xlsx", index=False)

print("Excel automation completed. File saved as output_cleaned.xlsx")
