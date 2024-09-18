import pandas as pd
import numpy as np

supplier_names = [f'Supplier_{i:03}' for i in range(1, 301)]
countries = ['Germany', 'Canada', 'China', 'Sweden', 'India', 'USA', 'Brazil', 'Japan', 'Australia', 'UK']
certifications = ['ISO 14001', 'ISO 9001', 'SA8000', 'FairTrade', 'None']
risk_levels = ['High', 'Medium', 'Low']

data = []
for i in range(1, 251):
    supplier_id = f'SUP-{i:03}'
    supplier_name = np.random.choice(supplier_names)
    sustainability_score = np.round(np.random.uniform(60, 100),2)
    cost_per_unit = np.round(np.random.uniform(10, 20),2)
    compliance_certifications = ', '.join(np.random.choice(certifications, size=np.random.randint(1, 3), replace=False))
    country = np.random.choice(countries)
    risk_assessment = np.random.choice(risk_levels)
    data.append([supplier_id, supplier_name, sustainability_score, cost_per_unit, compliance_certifications, country, risk_assessment])

# Create DataFrame and save to CSV
df_suppliers = pd.DataFrame(data, columns=[
    'Supplier_ID', 'Supplier_Name', 'Sustainability_Score', 'Cost_Per_Unit',
    'Compliance_Certifications', 'Country', 'Risk_Assessment'
])
df_suppliers.to_csv('supplier_evaluation.csv', index=False)
