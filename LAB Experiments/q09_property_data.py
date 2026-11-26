"""Q9: Pandas operations on property_data."""
import pandas as pd

property_data = pd.DataFrame({
    "property_id": [1, 2, 3, 4, 5, 6, 7],
    "location": ["Chennai", "Mumbai", "Chennai", "Delhi", "Mumbai", "Delhi", "Chennai"],
    "bedrooms": [3, 5, 2, 4, 6, 5, 4],
    "area_sqft": [1500, 3200, 900, 2100, 4000, 2800, 1800],
    "listing_price": [6500000, 21000000, 4000000, 15000000, 30000000, 18000000, 8000000],
})
print(property_data, "\n")

# 1. Average listing price per location
print("1. Average listing price by location:\n", property_data.groupby("location")["listing_price"].mean(), "\n")

# 2. Number of properties with more than four bedrooms
print("2. Properties with more than 4 bedrooms:", (property_data["bedrooms"] > 4).sum(), "\n")

# 3. Property with the largest area
print("3. Property with the largest area:\n", property_data.loc[property_data["area_sqft"].idxmax()])
