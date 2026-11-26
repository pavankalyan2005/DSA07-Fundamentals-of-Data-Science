import matplotlib.pyplot as plt

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales = [42000, 45500, 51000, 48000, 53500, 58000,
         61000, 59500, 64000, 68500, 72000, 80000]

plt.bar(month, sales)
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales (Rs)')
plt.grid(axis='y')
plt.show()