# Food Delivery Dataset Analysis
import pandas as pd
import json
import re

# Step 1: Load CSV Data
orders_df = pd.read_csv('orders.csv')

# Step 2: Load JSON Data
with open('users.json', 'r') as f:
    users_data = json.load(f)
users_df = pd.DataFrame(users_data)

# Step 3: Load SQL Data (Parsing INSERT statements)
with open('restaurants.sql', 'r') as f:
    sql_content = f.read()

# Using regex to extract (id, name, cuisine, rating)
pattern = r"\((\d+),\s*'([^']*)',\s*'([^']*)',\s*([\d.]+)\)"
matches = re.findall(pattern, sql_content)
restaurants_df = pd.DataFrame(matches, columns=['restaurant_id', 'restaurant_name_sql', 'cuisine', 'rating'])
restaurants_df['restaurant_id'] = restaurants_df['restaurant_id'].astype(int)
restaurants_df['rating'] = restaurants_df['rating'].astype(float)

# Step 4: Merge the Data (Left Joins)
# Joining orders with users
merged_df = orders_df.merge(users_df, on='user_id', how='left')

# Joining with restaurant details
final_df = merged_df.merge(restaurants_df, on='restaurant_id', how='left')

# Step 5: Save Final Dataset
final_df.to_csv('final_food_delivery_dataset.csv', index=False)
print("Final dataset created successfully!")

# --- Analysis & Verification ---

# 1. Total Revenue from Gold members by City
gold_members = final_df[final_df['membership'] == 'Gold']
city_revenue = gold_members.groupby('city')['total_amount'].sum()
print(f"Top Revenue City (Gold): {city_revenue.idxmax()}")

# 2. Average Order Value by Cuisine
cuisine_avg = final_df.groupby('cuisine')['total_amount'].mean()
print(f"Highest AOV Cuisine: {cuisine_avg.idxmax()}")

# 3. Distinct users with > ₹1000 total spend
user_totals = final_df.groupby('user_id')['total_amount'].sum()
print(f"Users spending > 1000: {(user_totals > 1000).sum()}")

# 4. Membership Percentage
gold_perc = (final_df['membership'] == 'Gold').mean() * 100
print(f"Gold Member Order Percentage: {gold_perc:.0f}%")