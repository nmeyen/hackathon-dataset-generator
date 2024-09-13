import pandas as pd
import numpy as np

recommendations = [
    'Optimize trucking routes using AI algorithms',
    'Switch to biofuel for ocean freight',
    'Upgrade warehouse lighting to LED systems',
    'Partner with suppliers closer to manufacturing sites',
    'Implement telematics for fleet management',
    'Increase load capacity utilization',
    'Use electric vehicles for short-haul deliveries',
    'Adopt just-in-time inventory to reduce storage needs',
    'Implement renewable energy sources in warehouses',
    'Enhance driver training programs for fuel efficiency'
]

priority_levels = ['High', 'Medium', 'Low']

data = []
for i in range(1, 251):
    rec_id = f'R-{i:03}'
    recommendation = np.random.choice(recommendations)
    emission_reduction = np.random.uniform(100, 500).round(2)
    cost_savings = np.random.uniform(5000, 20000).round(2)
    implementation_time = np.random.randint(1, 12)
    priority = np.random.choice(priority_levels)
    data.append([rec_id, recommendation, emission_reduction, cost_savings, implementation_time, priority])

# Create DataFrame and save to CSV
df_ai_recommendations = pd.DataFrame(data, columns=[
    'Recommendation_ID', 'Recommendation', 'Estimated_Emission_Reduction',
    'Estimated_Cost_Savings', 'Implementation_Timeframe', 'Priority_Level'
])
df_ai_recommendations.to_csv('ai_recommendations.csv', index=False)
