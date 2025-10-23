# Step 1: Import Necessary Libraries
# First, import the necessary libraries.


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Step 2: Send a Request to the Webpage
# Send a request to the webpage to get the HTML content.


url = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Parse the HTML Content
# Parse the HTML content to find the table containing the data we want to scrape.


# Find the table containing the Nobel Prize winners' data

table = soup.find('table', {'class': 'wikitable'})
# Step 4: Convert the HTML Table into a pandas DataFrame
# Convert the HTML table into a pandas DataFrame for analysis.
# Extract the table headers

headers = [header.text.strip() for header in table.find_all('th')]

# Extract the table rows

rows = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    cells = [cell.text.strip() for cell in cells]
    rows.append(cells)

# Create a DataFrame

df = pd.DataFrame(rows, columns=headers)

# Display the first few rows of the DataFrame
print(df.head())

# Step 5: Clean the Data

# Clean the data by handling missing values and converting data types if necessary.


# Drop any rows with missing values
df.dropna(inplace=True)

# Display the cleaned DataFrame

print(df.head())

# Step 6: Analyze the Data
# Now that we have the data in a pandas DataFrame, we can perform some basic analysis.


# Display basic information about the DataFrame
print(df.info())

# Display summary statistics
print(df.describe())

# Find the number of Nobel Prize winners by country
country_counts = df['Country'].value_counts()
print(country_counts)

