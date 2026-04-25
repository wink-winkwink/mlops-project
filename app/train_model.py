import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    'area': [50, 70, 100, 120, 150],
    'rooms': [1, 2, 2, 3, 3],
    'price': [500000, 750000, 1100000, 1300000, 1600000]
}
df = pd.DataFrame(data)

X = df[['area', 'rooms']]
y = df['price']
model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'app/house_model.joblib')
print("Model saved!")