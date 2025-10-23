
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 2. Create a Sample Dataset


# Sample data

data = {
    'SquareFeet': [1500, 2000, 2500, 1800, 3000, 1200, 2300, 2200, 1700, 1600],
    'Bedrooms': [3, 4, 3, 3, 5, 2, 4, 3, 3, 2],
    'Age': [10, 15, 20, 15, 10, 30, 5, 8, 12, 25],
    'Price': [300000, 450000, 500000, 400000, 600000, 200000, 480000, 470000, 350000, 300000]
}

# Convert to DataFrame

df = pd.DataFrame(data)

# 3. Split Data into Features and Target Variable



X = df[['SquareFeet', 'Bedrooms', 'Age']]
y = df['Price']

# 4. Split Data into Training and Testing Sets


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train the Model


model = LinearRegression()
model.fit(X_train, y_train)

# 6. Make Predictions

y_pred = model.predict(X_test)

# 7. Evaluate the Model


mse = mean_squared_error(y_test, y_pred)
# print(mse)
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error: {rmse}')