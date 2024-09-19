import pandas as pd
import numpy as np
from datetime import datetime

# List of districts in Sri Lanka
districts = [
    'Ampara', 'Anuradhapura', 'Badulla', 'Batticaloa', 'Colombo', 'Galle', 'Gampaha', 'Hambantota',
    'Jaffna', 'Kalutara', 'Kandy', 'Kegalle', 'Kilinochchi', 'Kurunegala', 'Mannar', 'Matale',
    'Matara', 'Moneragala', 'Mullaitivu', 'Nuwara Eliya', 'Polonnaruwa', 'Puttalam', 'Ratnapura',
    'Trincomalee', 'Vavuniya'
]

# Categories and subcategories for John Keells Holdings PLC
categories = [
    'Transportation', 'Leisure', 'Property', 'Consumer Foods', 'Retail',
    'Financial Services', 'Information Technology', 'Plantation Services'
]

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

data = []
for _ in range(250):
    date = datetime(2023, 5, 31).strftime('%Y-%m-%d')
    category = np.random.choice(categories)
    subcategory = np.random.choice(subcategories[category])
    company = np.random.choice(companies[category])
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
df_carbon.to_csv('carbon_footprint_analysis_jkh.csv', index=False)
