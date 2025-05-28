import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
data = {
    'Age': [23, 45, 25, 34, 45, 36, 37, 28, 23, 24, 26, 27, 40, 50, 55, 22, 21, 30],
    'Salary': [25000, 40000, 27000, 34000, 45000, 36000, 37000, 28000, 24000, 26000, 27000, 27500, 38000, 47000, 50000, 22000, 21500, 30000]
}

df = pd.DataFrame(data)

# Create Age Range
bins_age = [20, 30, 40, 50, 60]
labels_age = ['20-29', '30-39', '40-49', '50-59']
df['AgeRange'] = pd.cut(df['Age'], bins=bins_age, labels=labels_age, right=False)

# Create Salary Range
bins_salary = [20000, 30000, 40000, 50000, 60000]
labels_salary = ['20k-30k', '30k-40k', '40k-50k', '50k-60k']
df['SalaryRange'] = pd.cut(df['Salary'], bins=bins_salary, labels=labels_salary, right=False)

# Frequency Table
frequency_table = df.groupby(['AgeRange', 'SalaryRange']).size().reset_index(name='Frequency')
print(frequency_table)

# Line Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='AgeRange', y='Frequency', data=frequency_table, marker='o')
plt.title('Frequency Line Plot for Age Range and Salary Range')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', bins=bins_age, kde=True)
plt.title('Histogram of Age')
plt.show()

# Frequency Curve
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Age'], shade=True)
plt.title('Frequency Curve of Age')
plt.show()
