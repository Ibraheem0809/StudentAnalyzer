# Load And Explore data
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

print("\nShape:",df.shape)
print("\nColumns:")
print(df.columns)

# Basic Information 
print("\nDataSet Info:")
print(df.info())

print("\nSummary Statics:")
print(df.describe())

# Calculate Statistics
print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nStandard Deviation:")
print(df.std(numeric_only=True))

# Create Average Score

# Add a new column:
"""df["Average"] = (
    df["Math"]+df["Science"]+df["English"]
)/3
print(df)"""
df["Average"] = df[
    ["Math", "Science", "English"]
].mean(axis=1).round(2)
print(df)

# Find Top Students
top_students = df.sort_values(by="Average", ascending=False)
print(top_students[["Name","Average"]].head(3))

# Best Performer
best_student = df.loc[df["Average"].idxmax()]
print("\nTop Performer")
print(best_student["Name"])
print("Average:",best_student["Average"])

# Lowest Performer
lowest_student = df.loc[df["Average"].idxmin()]
print("\nNeeds Improvement:")
print(lowest_student["Name"])
print("Average:",lowest_student["Average"])

"""# First Visualization
import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.xticks(rotation=45)

plt.show()"""

"""# Correlational Analysis
print(df.corr(numeric_only=True))

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Average"
)
plt.title("Study Hours vs Average Marks")
plt.show()
"""

"""# Correlation Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

corr_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()"""

"""# Distribution Analysis
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Average"],
    bins=5,
    kde=True
)

plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.show()"""

# BoxPlot
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))

sns.boxplot(
    y=df["Average"]
)

plt.title("Average Score Boxplot")
plt.show()