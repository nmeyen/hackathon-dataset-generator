import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate dates for 250 days starting from 2023-01-01
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(250)]

# Generate data
data = {
    'Date': [date.strftime('%Y-%m-%d') for date in dates],
    'Total_Emissions': np.random.uniform(4500, 5000, 250).round(2),
    'Emissions_Target': np.random.uniform(4400, 4800, 250).round(2),
    'Cost_Savings': np.random.uniform(10000, 20000, 250).round(2),
    'Sustainability_Goal_Progress': np.linspace(45, 70, 250).round(2)
}

# Create DataFrame and save to CSV
df_dashboard = pd.DataFrame(data)
df_dashboard.to_csv('dashboard_metrics.csv', index=False)
