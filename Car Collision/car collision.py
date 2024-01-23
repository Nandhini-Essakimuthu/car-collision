import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('monroe county car crach 2003-2015.csv', encoding='latin1')

# Convert 'Weekend?' to numeric (assuming 'Y' means weekend and 'N' means weekday)
df['Weekend'] = df['Weekend?'].map({'Y': 1, 'N': 0})

# Descriptive Statistics
print(df.describe())

# Visualization
plt.figure(figsize=(12, 6))
sns.histplot(df['Hour'], bins=24, kde=True)
plt.title('Distribution of Collisions by Hour')
plt.xlabel('Hour')
plt.ylabel('Frequency')
plt.show()

# Time Analysis
time_analysis = df.groupby(['Year', 'Month', 'Day']).size().reset_index(name='Collision Count')
print(time_analysis)

# Weekend vs. Weekday Analysis
weekday_weekend_analysis = df.groupby('Weekend')['Collision Type'].value_counts().unstack().fillna(0)
print(weekday_weekend_analysis)

# Collision Type and Injury Type Analysis
collision_injury_analysis = df.groupby('Collision Type')['Injury Type'].value_counts().unstack().fillna(0)
print(collision_injury_analysis)

# Primary Factor Analysis
primary_factor_analysis = df.groupby('Primary Factor')['Collision Type'].value_counts().unstack().fillna(0)
print(primary_factor_analysis)

# Location-based Analysis
location_analysis = df.groupby(['Reported_Location', 'Latitude', 'Longitude']).size().reset_index(name='Collision Count')
print(location_analysis)

# Geospatial Analysis
plt.figure(figsize=(10, 10))
sns.scatterplot(x='Longitude', y='Latitude', data=df, alpha=0.1)
plt.title('Collision Locations')
plt.show()

# Correlation Analysis
# Check unique values in the 'Weekend?' column
print("Unique values in 'Weekend?':", df['Weekend?'].unique())

# Convert 'Weekend?' to numeric (assuming 'Y' means weekend and 'N' means weekday)
df['Weekend'] = df['Weekend?'].map({'Y': 1, 'N': 0})

# Check unique values in the new 'Weekend' column
print("Unique values in 'Weekend':", df['Weekend'].unique())

# Collision Type and Injury Type Analysis
collision_injury_analysis = df.groupby(['Collision Type', 'Injury Type']).size().unstack().fillna(0)

# Display the resulting DataFrame
print(collision_injury_analysis)

# Plot a heatmap for better visualization
plt.figure(figsize=(12, 8))
sns.heatmap(collision_injury_analysis, cmap='viridis', annot=True, fmt='g')
plt.title('Collision Type vs. Injury Type')
plt.xlabel('Injury Type')
plt.ylabel('Collision Type')
plt.show()

# Seasonal Analysis
df['Season'] = pd.to_datetime(df[['Year', 'Month', 'Day']]).dt.month // 3
seasonal_analysis = df.groupby('Season')['Collision Type'].value_counts().unstack().fillna(0)

# Display the resulting DataFrame
print("Seasonal Analysis:")
print(seasonal_analysis)

# Road Conditions Analysis
# (Add your code for road conditions analysis here)

# Display the resulting DataFrames

# Plot heatmaps for better visualization
plt.figure(figsize=(15, 8))

plt.subplot(2, 2, 1)
sns.heatmap(seasonal_analysis, cmap='viridis', annot=True, fmt='g')
plt.title('Seasonal Analysis')

# Convert 'Weekend?' to numeric (assuming 'Y' means weekend and 'N' means weekday)
df['Weekend'] = df['Weekend?'].map({'Y': 1, 'N': 0})

# Collision Type, Primary Factor, and Location Analysis
collision_primary_factor_location_analysis = df.groupby(['Collision Type', 'Primary Factor', 'Reported_Location']).size().unstack().fillna(0)

# Display the resulting DataFrame
print("Collision Type, Primary Factor, and Location Analysis:")
print(collision_primary_factor_location_analysis)

# Plot a heatmap for better visualization
plt.subplot(2, 2, 2)
sns.heatmap(collision_primary_factor_location_analysis, cmap='viridis', annot=True, fmt='g', cbar_kws={'label': 'Collision Count'})
plt.title('Collision Type, Primary Factor, and Location Analysis')
plt.xlabel('Reported Location')
plt.ylabel('Collision Type - Primary Factor')

plt.tight_layout()
plt.show()



