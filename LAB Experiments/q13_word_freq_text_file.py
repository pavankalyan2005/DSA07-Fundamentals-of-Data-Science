"""Q13: Frequency distribution of words in sample_text.txt."""
import os
import re
from collections import Counter

FILE = "sample_text.txt"
if not os.path.exists(FILE):   # create a demo file so the program runs
    with open(FILE, "w") as f:
        f.write("Data science is fun. Data science uses Python, and Python is popular. "
                "Learning data science with Python is fun!")

with open(FILE, "r", encoding="utf-8") as f:
    text = f.read().lower()

words = re.findall(r"\b[a-z']+\b", text)      # strips punctuation
freq = Counter(words)

print(f"Total words: {len(words)}   Unique words: {len(freq)}\n")
print(f"{'Word':<15}{'Frequency'}")
for word, count in freq.most_common():
    print(f"{word:<15}{count}")
