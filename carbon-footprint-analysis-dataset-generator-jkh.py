import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# List of districts in Sri Lanka
districts = [
    'Ampara', 'Anuradhapura', 'Badulla', 'Batticaloa', 'Colombo', 'Galle', 'Gampaha', 'Hambantota',
    'Jaffna', 'Kalutara', 'Kandy', 'Kegalle', 'Kilinochchi', 'Kurunegala', 'Mannar', 'Matale',
    'Matara', 'Moneragala', 'Mullaitivu', 'Nuwara Eliya', 'Polonnaruwa', 'Puttalam', 'Ratnapura',
    'Trincomalee', 'Vavuniya'
]

# Categories and subcategories for John Keells Holdings PLC
categories1 = [
    'Transportation', 'Leisure', 'Property', 'Consumer Foods', 'Retail',
    'Financial Services', 'Information Technology', 'Plantation Services'
]

categories = ['Transportation', 'Warehousing', 'Manufacturing']

subcategories = {
    'Transportation': ['Ports & Shipping', 'Logistics'],
    'Leisure': ['Destination Management', 'Hotel Management', 'Hotel Ownership'],
    'Property': ['Property Development', 'Property Management'],
    'Consumer Foods': ['Beverages', 'Frozen Confectionery', 'Convenience Foods'],
    'Retail': ['Supermarkets'],
    'Financial Services': ['Banking', 'Insurance', 'Other Financial Services'],
    'Information Technology': ['Business Process Outsourcing', 'Software Services'],
    'Plantation Services': ['Tea Plantations', 'Rubber Plantations']
}

# Business units (companies) of John Keells Holdings PLC
companies = {
    'Transportation': ['John Keells Logistics', 'South Asia Gateway Terminals'],
    'Leisure': ['Cinnamon Hotels & Resorts', 'Walkers Tours', 'Whittall Boustead Travel'],
    'Property': ['John Keells Properties'],
    'Consumer Foods': ['Ceylon Cold Stores', 'Keells Food Products'],
    'Retail': ['Keells Super'],
    'Financial Services': ['Union Assurance', 'Nations Trust Bank'],
    'Information Technology': ['John Keells IT', 'Infomate'],
    'Plantation Services': ['Keells Plantations', 'Tea Smallholder Factories PLC']
}

# Define the date range for one year
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

data = []
for _ in range(600):
    # Generate a random date within the date range
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
    category = np.random.choice(categories)
    category1 = np.random.choice(categories1)
    subcategory = np.random.choice(subcategories[category1])
    company = np.random.choice(companies[category1])
    district = np.random.choice(districts)
    emissions = np.round(np.random.uniform(100, 1200), 2)
    percentage_of_total = np.round(np.random.uniform(1, 25), 2)
    data.append([
        date, category, subcategory, company, district, emissions, percentage_of_total
    ])

# Create DataFrame and save to CSV
df_carbon = pd.DataFrame(data, columns=[
    'Date', 'Category', 'Subcategory', 'Company', 'District', 'Emissions', 'Percentage_of_Total'
])
df_carbon.to_csv('carbon_footprint_analysis_jkh_v2.csv', index=False)
