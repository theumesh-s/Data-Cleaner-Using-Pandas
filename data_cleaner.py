import pandas as pd      

# Read your CSV file
df = pd.read_csv("messy.csv")  # replace "messy.csv" with your actual file name if needed

# Clean ID
df["ID"].fillna(0, inplace=True)
df["ID"] = df["ID"].astype(int)

# Clean Name
df.dropna(subset=["Name"], inplace=True)
df.drop_duplicates(subset=["Name"], inplace=True)
df["Name"] = df["Name"].str.strip()

# Clean Age
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Age"] = df["Age"].astype(int)

# Clean Score
df["Score"].fillna(df["Score"].mean(), inplace=True)
df["Score"] = df["Score"].round(2)

# Clean City
df["City"].fillna("Delhi", inplace=True)
df["City"] = df["City"].str.strip()

# Add Passed column
df["Passed"] = df["Score"].apply(lambda x: "Yes" if x >= 33 else "No")

# Save cleaned CSV
df.to_csv("mess_cleaned.csv", index=False)

print("Cleaning complete! Saved as mess_cleaned.csv")
