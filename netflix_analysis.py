import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("netflix_data.csv")

# Show first rows
print(df.head())

# 1. Count of Movies vs TV Shows
type_count = df['Type'].value_counts()
print(type_count)

# Plot
type_count.plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# 2. Genre Distribution
genre_count = df['Genre'].value_counts()
print(genre_count)

genre_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Genre Distribution")
plt.show()

# 3. Trend over Years
year_trend = df['Year'].value_counts().sort_index()
print(year_trend)

year_trend.plot(kind='line', marker='o')
plt.title("Content Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()