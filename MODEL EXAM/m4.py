import numpy as np

fuel_efficiency = np.array([18.5, 22, 25.5, 30.2, 28.4, 35])
avg = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", avg)
old_model = fuel_efficiency[0]
new_model = fuel_efficiency[5]
improvement = ((new_model - old_model) / old_model) * 100
print("Percentage Improvement:", improvement, "%")