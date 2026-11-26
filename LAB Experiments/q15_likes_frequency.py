"""Q15: Frequency distribution of likes among posts."""
import pandas as pd
import matplotlib.pyplot as plt

posts = pd.DataFrame({
    "post_id": range(1, 16),
    "likes": [10, 25, 10, 40, 25, 10, 55, 40, 25, 70, 10, 55, 25, 40, 10],
})

freq = posts["likes"].value_counts().sort_index()
print("Frequency distribution of likes:\n")
print(freq.rename_axis("likes").reset_index(name="number_of_posts"))

freq.plot(kind="bar", color="purple")
plt.title("Frequency Distribution of Likes")
plt.xlabel("Number of likes"); plt.ylabel("Number of posts")
plt.show()
