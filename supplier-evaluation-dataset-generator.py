# import pandas as pd
# import numpy as np

# supplier_names = [f'Supplier_{i:03}' for i in range(1, 301)]
# countries = ['Germany', 'Canada', 'China', 'Sweden', 'India', 'USA', 'Brazil', 'Japan', 'Australia', 'UK']
# certifications = ['ISO 14001', 'ISO 9001', 'SA8000', 'FairTrade', 'None']
# risk_levels = ['High', 'Medium', 'Low']

# data = []
# for i in range(1, 251):
#     supplier_id = f'SUP-{i:03}'
#     supplier_name = np.random.choice(supplier_names)
#     sustainability_score = np.round(np.random.uniform(60, 100),2)
#     cost_per_unit = np.round(np.random.uniform(10, 20),2)
#     compliance_certifications = ', '.join(np.random.choice(certifications, size=np.random.randint(1, 3), replace=False))
#     country = np.random.choice(countries)
#     risk_assessment = np.random.choice(risk_levels)
#     data.append([supplier_id, supplier_name, sustainability_score, cost_per_unit, compliance_certifications, country, risk_assessment])

# # Create DataFrame and save to CSV
# df_suppliers = pd.DataFrame(data, columns=[
#     'Supplier_ID', 'Supplier_Name', 'Sustainability_Score', 'Cost_Per_Unit',
#     'Compliance_Certifications', 'Country', 'Risk_Assessment'
# ])
# df_suppliers.to_csv('supplier_evaluation.csv', index=False)


import pandas as pd
import numpy as np

# List of suppliers relevant to John Keells Holdings PLC
supplier_names = [
    'Ceylon Agro Industries', 'Lanka Commodities', 'Asian Packaging Ltd.',
    'Sri Lanka Logistics Co.', 'Colombo Steel Traders', 'Southern Timber Suppliers',
    'Oceanic Shipping Lines', 'Eastern Electronics', 'Global Textiles Lanka',
    'Island Fresh Produce', 'Highland Dairy Suppliers', 'Pearl Maritime Services',
    'Green Energy Solutions', 'Lanka Mining Co.', 'Kelani Chemical Suppliers',
    'Sapphire IT Solutions', 'Serendib Construction Materials', 'Lotus Printing Services',
    'Sunshine Pharmaceuticals', 'Gemstone Petroleum Distributors'
]

# Countries where suppliers are likely to be based
countries = ['Sri Lanka', 'India', 'China', 'Singapore', 'Malaysia', 'United Arab Emirates', 'Bangladesh', 'Thailand', 'Indonesia', 'Vietnam']

# Certifications relevant to the region and industries
certifications = ['ISO 14001', 'ISO 9001', 'SA8000', 'FairTrade', 'GMP', 'HACCP', 'None']

# Risk levels adjusted to reflect more nuanced assessments
risk_levels = ['High', 'Medium', 'Low']

data = []
for i in range(1, 500):
    supplier_id = f'SUP-{i:03}'
    supplier_name = np.random.choice(supplier_names)
    sustainability_score = np.round(np.random.uniform(50, 100), 2)  # Adjusted to start from 50
    cost_per_unit = np.round(np.random.uniform(5, 25), 2)  # Adjusted cost range
    compliance_certifications = ', '.join(np.random.choice(certifications, size=np.random.randint(1, 4), replace=False))
    country = np.random.choice(countries)
    risk_assessment = np.random.choice(risk_levels, p=[0.2, 0.5, 0.3])  # Adjusted probabilities
    data.append([
        supplier_id, supplier_name, sustainability_score, cost_per_unit,
        compliance_certifications, country, risk_assessment
    ])

# Create DataFrame and save to CSV
df_suppliers = pd.DataFrame(data, columns=[
    'Supplier_ID', 'Supplier_Name', 'Sustainability_Score', 'Cost_Per_Unit',
    'Compliance_Certifications', 'Country', 'Risk_Assessment'
])
df_suppliers.to_csv('supplier_evaluation_jkh.csv', index=False)
