import pandas as pd
import numpy as np

variables = ['Shipment Volume', 'Fuel Type', 'Equipment Efficiency', 'Routing', 'Supplier Location']
adjustments = ['Increase by 10%', 'Decrease by 15%', 'Switch to Biofuel', 'AI Optimization', 'Closer Suppliers']
time_periods = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024']

data = []
for i in range(1, 251):
    scenario_id = f'S-{i:03}'
    scenario_name = f'Scenario {i}'
    variable_adjusted = np.random.choice(variables)
    adjustment_detail = np.random.choice(adjustments)
    projected_emissions = np.round(np.random.uniform(4000, 6000),2)
    time_period = np.random.choice(time_periods)
    confidence_level = np.round(np.random.uniform(60, 90),2)
    data.append([scenario_id, scenario_name, variable_adjusted, adjustment_detail, projected_emissions, time_period, confidence_level])

# Create DataFrame and save to CSV
df_predictive = pd.DataFrame(data, columns=[
    'Scenario_ID', 'Scenario_Name', 'Variable_Adjusted', 'Adjustment_Detail',
    'Projected_Emissions', 'Time_Period', 'Confidence_Level'
])
df_predictive.to_csv('predictive_analytics.csv', index=False)
