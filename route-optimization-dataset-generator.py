import pandas as pd
import numpy as np

# origins = ['Los Angeles', 'Hamburg', 'Tokyo', 'Sydney', 'New York', 'Shanghai', 'Dubai', 'Sao Paulo', 'Mumbai', 'Cape Town']
# destinations = ['Chicago', 'Munich', 'Osaka', 'Melbourne', 'Atlanta', 'Beijing', 'London', 'Rio de Janeiro', 'Delhi', 'Nairobi']

# List of companies under John Keells Holdings PLC
company_names = [
    'Keells Supermarkets', 'John Keells Logistics', 'Cinnamon Hotels & Resorts',
    'Mackinnons Travels', 'Keells Food Products', 'Walkers Tours',
    'Union Assurance', 'Lanka Marine Services', 'DHL Keells', 'John Keells Properties'
]

# Adjust origins and destinations relevant to John Keells Holdings PLC operations
# Origins are major Sri Lankan cities/ports
origins = ['Colombo', 'Hambantota', 'Trincomalee', 'Galle', 'Koggala', 'Katunayake']

# Destinations are key international trade and travel destinations
destinations = [
    'Chennai', 'Mumbai', 'Singapore', 'Dubai', 'London', 'Sydney',
    'Shanghai', 'Tokyo', 'Doha', 'Jakarta'
]


data = []
for i in range(1, 500):
    route_id = f'RT-{i:03}'
    company_name = np.random.choice(company_names)
    origin = np.random.choice(origins)
    destination = np.random.choice(destinations)
    current_distance = np.round(np.random.uniform(500, 5000),2)
    optimized_distance = np.round(current_distance * np.random.uniform(0.85, 0.98),2)
    current_emissions = np.round(current_distance * np.random.uniform(0.03, 0.05),2)
    optimized_emissions = np.round(optimized_distance * np.random.uniform(0.03, 0.05) ,2)
    time_saved = np.round((current_distance - optimized_distance) / np.random.uniform(50, 70),2)
    cost_savings = np.round((current_distance - optimized_distance) * np.random.uniform(1.5, 3.0),2)
    capacity_utilization = np.round(np.random.uniform(80, 95) ,2)
    data.append([
         route_id,company_name, origin, destination, current_distance, optimized_distance,
        current_emissions, optimized_emissions, time_saved, cost_savings, capacity_utilization
    ])

# Create DataFrame and save to CSV
df_routes = pd.DataFrame(data, columns=[
    'Route_ID', 'Company Name','Origin', 'Destination', 'Current_Route_Distance', 'Optimized_Route_Distance',
    'Current_Emissions', 'Optimized_Emissions', 'Estimated_Time_Saved', 'Estimated_Cost_Savings',
    'Vehicle_Capacity_Utilization'
])
df_routes.to_csv('route_optimization.csv', index=False)
