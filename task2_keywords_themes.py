import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load sentiment-tagged reviews
df = pd.read_csv("bank_reviews_with_sentiment.csv")

# TF-IDF Keyword Extraction
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=100)
X = vectorizer.fit_transform(df["review"])
keywords = vectorizer.get_feature_names_out()

# Print top keywords
print("Top Keywords:")
print(keywords)

# OPTIONAL: Manual grouping into themes (you'll need to inspect and assign themes)
# For now, just save keywords
pd.DataFrame({"keyword": keywords}).to_csv("top_keywords.csv", index=False)
print("✅ Keywords saved to 'top_keywords.csv'")
