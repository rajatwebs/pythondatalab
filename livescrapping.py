import pandas as pd

# Create a simple dataset
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 4, 5, 6]
}

# Create a DataFrame
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Calculate the necessary values
sum_x = df['x'].sum()
sum_y = df['y'].sum()
sum_xy = (df['x'] * df['y']).sum()
sum_x2 = (df['x'] ** 2).sum()
sum_y2 = (df['y'] ** 2).sum()

print("Sum of x:", sum_x)
print("Sum of y:", sum_y)
print("Sum of xy:", sum_xy)
print("Sum of x^2:", sum_x2)
print("Sum of y^2:", sum_y2)

# Calculate the correlation coefficient
n = len(df)
numerator = n * sum_xy - sum_x * sum_y
denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))**0.5
correlation_coefficient = numerator / denominator

print("Correlation Coefficient:", correlation_coefficient)

# Verify with pandas `corr` method
correlation_matrix = df.corr()
print("Correlation matrix:\n", correlation_matrix)