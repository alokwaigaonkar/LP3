# 🛒 K-Means Clustering on Sales Data Sample
# Tasks: Preprocessing, Elbow Method, Clustering

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1️⃣ Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# 2️⃣ Basic Info
print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Checking for Missing Values ===")
print(df.isnull().sum())

# 3️⃣ Select numerical columns for clustering
num_df = df.select_dtypes(include=[np.number]).dropna()
print("\nNumerical Columns Used for Clustering:\n", num_df.columns.tolist())

# 4️⃣ Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(num_df)

# 5️⃣ Determine optimal K using Elbow Method
wcss = []  # within-cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()

# 6️⃣ Choose number of clusters (based on elbow point, e.g., K=3)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# 7️⃣ Add cluster labels to dataset
num_df['Cluster'] = clusters

print("\n=== Cluster Centers ===")
print(pd.DataFrame(kmeans.cluster_centers_, columns=num_df.columns[:-1]))

print("\n=== Sample Clustered Data ===")
print(num_df.head())