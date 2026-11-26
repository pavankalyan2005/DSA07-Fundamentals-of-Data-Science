import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Arjun Rao', 'Luis Ortega', 'Karim Nasser',
             'Tom Becker', 'Ravi Menon', 'Diego Silva',
             'Sam Carter', 'Ali Hassan', 'Jon Eriksen',
             'Kevin Dube', 'Pedro Alves', 'Yusuf Demir'],
    'Age': [24, 31, 28, 35, 22, 27, 29, 26, 33, 21, 30, 25],
    'Position': ['Forward', 'Midfielder', 'Forward', 'Defender',
                 'Midfielder', 'Forward', 'Goalkeeper', 'Midfielder',
                 'Defender', 'Forward', 'Midfielder', 'Defender'],
    'Goals': [18, 7, 22, 2, 9, 15, 0, 11, 3, 12, 6, 4],
    'Weekly Salary': [45000, 38000, 62000, 30000, 25000, 55000,
                      40000, 42000, 35000, 28000, 47000, 33000]
}

df = pd.DataFrame(data)
df.to_csv('players.csv', index=False)
print("Top 5 Players by Goals:")
print(df.nlargest(5, 'Goals'))
print("\nTop 5 Players by Salary:")
print(df.nlargest(5, 'Weekly Salary'))
avg_age = df['Age'].mean()
print("\nAverage Age:", avg_age)
print("\nPlayers Above Average Age:")
print(df[df['Age'] > avg_age])
df['Position'].value_counts().plot(kind='bar')
plt.title('Players by Position')
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.show()