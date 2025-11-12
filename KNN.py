# 💉 K-Nearest Neighbors (KNN) on Diabetes Dataset
# Tasks: Preprocessing, Model Training, Confusion Matrix, Accuracy, Error Rate, Precision, Recall

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# 1️⃣ Load dataset
df = pd.read_csv("diabetes.csv")

# 2️⃣ Basic info and missing values
print("\n=== Dataset Information ===")
print(df.info())

print("\n=== Checking for Missing Values ===")
print(df.isnull().sum())

# 3️⃣ Feature and Target split
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# 4️⃣ Standardize data (important for KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5️⃣ Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 6️⃣ Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 7️⃣ Predictions
y_pred = knn.predict(X_test)

# 8️⃣ Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\n=== Confusion Matrix ===")
print(cm)

# 9️⃣ Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
error_rate = 1 - accuracy
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.3f}")
print(f"Error Rate: {error_rate:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")