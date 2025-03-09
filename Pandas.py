# Pandas + Matplotlib Cheatsheet (Exam + Practical Use)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a DataFrame
df = pd.DataFrame({
    "Name": ["Govind", "Isaac", "Einstein", "Newton"],
    "Age": [18, 25, 42, 30],
    "Score": [95, 88, 76, 99]
})

# Read & Write CSV
df.to_csv('data.csv', index=False)  # Save without index
df = pd.read_csv('data.csv')  # Load CSV

# Head, Tail & Summary
df.head(3)  # First 3 rows
df.tail(3)  # Last 3 rows
df.describe()  # Summary stats
df.info()  # DataFrame info
df.shape  # (rows, columns)

df.columns  # Column names
df.dtypes  # Data types

# Filtering Data
df_filtered = df[df['Age'] > 25]  # Age > 25
df_filtered = df[(df['Age'] > 25) & (df['Score'] > 80)]  # Multiple conditions
df_filtered = df[df['Name'] == "Newton"]  # Filter by Name

df.loc[[1, 2], ['Name', 'Score']]  # Select specific rows & columns
df.iloc[0:2, 1:3]  # Select using index position

# Sorting & Indexing
df.sort_values(by='Age', ascending=False)  # Sort by Age descending
df.reset_index(drop=True, inplace=True)  # Reset index
df.set_index('Name', inplace=True)  # Set 'Name' as index

df.rename(columns={'Score': 'Marks'}, inplace=True)  # Rename column

# Handling Missing Data
df.dropna()  # Drop missing values
df.fillna(0)  # Replace NaN with 0
df['Age'].isnull()  # Check missing values

# Drop Columns & Rows
df.drop(columns=['Age'], inplace=True)  # Drop column
df.drop([0], axis=0, inplace=True)  # Drop row 0

df.drop_duplicates(subset=['Name'], keep=False)  # Remove duplicates

# Convert to Numpy & Transpose
df.to_numpy()  # Convert to Numpy array
df.T  # Transpose DataFrame

# Statistical Analysis
df.mean()  # Mean
df.median()  # Median
df.std()  # Standard Deviation
df.corr()  # Correlation Matrix
df.count()  # Count values
df.value_counts(dropna=False)  # Count unique values

# ===========================
# Matplotlib for Data Visualization
# ===========================

# Basic Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label="Sine Wave", color="b")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Line Plot")
plt.legend()
plt.grid()
plt.show()

# Scatter Plot
df.plot(x="Age", y="Score", kind="scatter", color='r')
plt.title("Age vs Score")
plt.show()

# Bar Chart
df.plot(x="Name", y="Score", kind="bar", color='g')
plt.title("Score Bar Chart")
plt.show()

# Histogram
df["Score"].plot(kind="hist", bins=5, color='purple', alpha=0.7)
plt.title("Score Distribution")
plt.show()

# Multiple Line Graph
df.plot(x="Name", y=["Age", "Score"], kind="line", marker="o")
plt.title("Age & Score Comparison")
plt.show()

# Subplots (Multiple Graphs in One)
fig, axs = plt.subplots(2, 2, figsize=(8, 6))
axs[0, 0].plot(x, y, color='b')
axs[0, 1].scatter(np.random.rand(10), np.random.rand(10), color='r')
axs[1, 0].bar(["A", "B", "C", "D"], [10, 20, 15, 30], color='g')
axs[1, 1].hist(np.random.randn(1000), bins=10, color='purple')
plt.tight_layout()
plt.show()

# ===========================
# Advanced Matplotlib Features
# ===========================

# 1️⃣ Twin Axes (Two Y-Axes on Same Graph)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, np.sin(x), 'g-', label='Sine')
ax2.plot(x, np.cos(x), 'b-', label='Cosine')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Sine', color='g')
ax2.set_ylabel('Cosine', color='b')
plt.title("Twin Axes Example")
plt.show()

# 2️⃣ Styling & Themes
plt.style.use('ggplot')  # Using a pre-defined style
plt.plot(x, y, label="Styled Line", linewidth=2, linestyle="--", marker="o")
plt.title("Styled Graph")
plt.legend()
plt.show()

# 3️⃣ Animation Example
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 1)
    return line,

def update(frame):
    line.set_data(x[:frame], np.sin(x[:frame]))
    return line,

ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True)
plt.title("Animated Sine Wave")
plt.show()

# 4️⃣ 3D Plot Example
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Surface Plot")
plt.show()

