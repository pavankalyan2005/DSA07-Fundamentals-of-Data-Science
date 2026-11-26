"""Q17: Load data.csv, preprocess, word frequency, top-N, bar graph."""
import os
import re
import string
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been", "am", "to", "of",
    "in", "on", "at", "for", "with", "this", "that", "it", "its", "i", "me", "my", "we", "you", "your",
    "they", "he", "she", "as", "by", "from", "so", "not", "no", "have", "has", "had", "do", "does",
    "did", "will", "would", "can", "could", "very", "just", "than", "then", "too", "after", "about",
}

# Create demo file if data.csv is missing
if not os.path.exists("data.csv"):
    pd.DataFrame({"feedback": [
        "Great service and very friendly staff!",
        "The app is slow and keeps crashing.",
        "Love the new design, great update!",
        "Customer service was slow to respond.",
        "Great product, will buy again.",
        "The delivery was fast and the packaging was great.",
    ]}).to_csv("data.csv", index=False)

# 1. Load
df = pd.read_csv("data.csv")

# 2. Preprocess
def preprocess(text):
    text = str(text).lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return [w for w in text.split() if w not in STOP_WORDS]

words = [w for comment in df["feedback"] for w in preprocess(comment)]

# 3. Frequency distribution
freq = Counter(words)

# 4. Top N
n = int(input("Enter N (number of top words to show): "))
top_n = freq.most_common(n)
print(f"\nTop {n} words:")
for word, count in top_n:
    print(f"{word:<15}{count}")

# 5. Bar graph
labels, counts = zip(*top_n)
plt.figure(figsize=(9, 5))
plt.bar(labels, counts, color="steelblue")
plt.title(f"Top {n} Most Frequent Words in Customer Feedback")
plt.xlabel("Word"); plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
