import pandas as pd
import numpy as np
from datetime import datetime

categories = ['Transportation', 'Warehousing', 'Manufacturing']
subcategories = {
    'Transportation': ['Trucking', 'Air Freight', 'Ocean Freight'],
    'Warehousing': ['Refrigeration', 'Lighting', 'Heating'],
    'Manufacturing': ['Assembly Line', 'Packaging', 'Quality Control']
}
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']

data = []
for _ in range(250):
    date = datetime(2023, 5, 31).strftime('%Y-%m-%d')
    category = np.random.choice(categories)
    subcategory = np.random.choice(subcategories[category])
    region = np.random.choice(regions)
    emissions = np.round(np.random.uniform(100, 1200), 2)
    percentage_of_total = np.round(np.random.uniform(1, 25), 2)
    data.append([date, category, subcategory, region, emissions, percentage_of_total])

# Create DataFrame and save to CSV
df_carbon = pd.DataFrame(data, columns=['Date', 'Category', 'Subcategory', 'Region', 'Emissions', 'Percentage_of_Total'])
df_carbon.to_csv('carbon_footprint_analysis.csv', index=False)
