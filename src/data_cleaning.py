import pandas as pd

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Remove duplicates
fake = fake.drop_duplicates()
true = true.drop_duplicates()

# Fill missing values
fake = fake.fillna("Unknown")
true = true.fillna("Unknown")

# Standardize text
for col in fake.select_dtypes(include="object").columns:
    fake[col] = fake[col].str.strip().str.lower()

for col in true.select_dtypes(include="object").columns:
    true[col] = true[col].str.strip().str.lower()

# Save cleaned files
fake.to_csv("Fake_Cleaned.csv", index=False)
true.to_csv("True_Cleaned.csv", index=False)

print("Data cleaning completed!")
