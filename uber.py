# Uber Fare Prediction – Simple Practical Code
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# 1️⃣ Load dataset
df = pd.read_csv("uber.csv")
df = df.dropna()
df = df[(df['fare_amount'] > 0) & (df['passenger_count'] > 0)]

# 2️⃣ Add distance feature (Haversine formula)
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 6371 * 2 * np.arcsin(np.sqrt(a))

df['distance_km'] = haversine(df['pickup_longitude'], df['pickup_latitude'],df['dropoff_longitude'], df['dropoff_latitude'])
df = df[(df['distance_km'] > 0) & (df['distance_km'] < 100)]

# 3️⃣ Remove outliers
upper = df['fare_amount'].quantile(0.99)
df = df[df['fare_amount'] < upper]

# 4️⃣ Correlation
print("\nCorrelation Matrix:\n", df[['fare_amount', 'distance_km', 'passenger_count']].corr())

# 5️⃣ Prepare data
X = df[['distance_km', 'passenger_count']]
y = df['fare_amount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6️⃣ Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
pred_lr = lr.predict(X_test)

# 7️⃣ Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)

# 8️⃣ Evaluate Models
def evaluate(y_true, y_pred, name):
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"\n{name} Results:\nR² = {r2:.3f} | RMSE = {rmse:.3f}")

evaluate(y_test, pred_lr, "Linear Regression")
evaluate(y_test, pred_rf, "Random Forest Regression")