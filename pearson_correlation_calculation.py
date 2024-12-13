import numpy as np

# Calculate Pearson Correlation
num_medicines = df["num_medicines"]
ages = df["age"]

correlation = np.corrcoef(num_medicines, ages)[0, 1]
print(f"Pearson correlation: {correlation:.2f}")
