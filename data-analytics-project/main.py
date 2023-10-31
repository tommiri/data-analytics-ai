import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read csv file into dataframe
df = pd.read_csv("data/spotify-2023.csv", encoding="iso-8859-1")

# Get some basic information about the data
df.describe()
df.head()
df.info()
df.isnull().sum()

## Clean up data to get a more accurate analysis
# Remove unnecessary columns
df = df[
    [
        "artist_count",
        "released_year",
        "released_month",
        "released_day",
        "streams",
        "bpm",
        "key",
        "mode",
    ]
]

# Drop all rows with NaN values
df.dropna(inplace=True)

# Remove rows with non-numeric values in streams column
df = df[df["streams"].str.isnumeric()]


# Convert key and mode columns to numeric values for easier analysis
key_dummies = pd.get_dummies(df["key"], prefix="key")
mode_dummies = pd.get_dummies(df["mode"], prefix="mode")
df = pd.concat([df, key_dummies, mode_dummies], axis=1)
df = df.drop(["key", "mode"], axis=1)

# Get number of songs released by month and plot it
release_months = df["released_month"].value_counts().sort_index()
sns.barplot(x=release_months.index, y=release_months.values)
plt.title("Number of songs released by month")
plt.xlabel("Month")
plt.ylabel("Number of songs")
plt.show()

# Get number of songs released by day of month and plot it
release_days = df["released_day"].value_counts().sort_index()
sns.lineplot(x=release_days.index, y=release_days.values)
plt.title("Number of songs released by day of month")
plt.xlabel("Day")
plt.ylabel("Number of songs")
plt.show()

# Get correlation between variables and round to 2 decimal places
corr = df.corr().round(2)

# Plot correlation heatmap
sns.heatmap(corr, cmap="coolwarm", annot=True, annot_kws={"size": 6})
plt.title("Correlation between all variables")
plt.show()
