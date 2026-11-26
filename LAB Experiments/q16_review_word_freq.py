"""Q16: Frequency distribution of words in customer reviews."""
import re
from collections import Counter
import pandas as pd

reviews = pd.DataFrame({"review": [
    "Great product, works well and the battery lasts long!",
    "Terrible quality. Stopped working after a week.",
    "Good value for money, great battery life.",
    "The product is great, but delivery was slow.",
    "Works well, would buy this product again!",
]})
# To use your own file:  reviews = pd.read_csv("reviews.csv")  # column 'review'

all_text = " ".join(reviews["review"]).lower()
words = re.findall(r"\b[a-z']+\b", all_text)
freq = Counter(words)

print(f"{'Word':<15}{'Frequency'}")
for word, count in freq.most_common():
    print(f"{word:<15}{count}")
