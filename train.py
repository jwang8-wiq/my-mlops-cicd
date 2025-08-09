import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# --- 1. Load Data ---
# In a real scenario, this data would come from BigQuery or a GCS bucket.
# For this example, we'll create a dummy DataFrame.
data = {
    'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'ad_spend': [1000, 1200, 1500, 1100, 1800, 2000, 2200, 2100, 2300, 2500, 2800, 3000],
    'sales': [50, 55, 65, 58, 75, 85, 95, 90, 105, 115, 130, 150]
}
df = pd.DataFrame(data)

X = df[['month', 'ad_spend']]
y = df['sales']

# --- 2. Train the Model ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
print("Model training complete.")

# --- 3. Save the Model Artifact ---
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")

#test1