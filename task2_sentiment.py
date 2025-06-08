import pandas as pd
from transformers import pipeline

# Load the cleaned data
df = pd.read_csv("bank_reviews_cleaned.csv")

# Load DistilBERT sentiment model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Run sentiment analysis
sentiments = sentiment_pipeline(df["review"].tolist(), truncation=True, padding=True)

# Add sentiment results to dataframe
df["sentiment_label"] = [s["label"] for s in sentiments]
df["sentiment_score"] = [s["score"] for s in sentiments]

# Save results
df.to_csv("bank_reviews_with_sentiment.csv", index=False)

print("✅ Sentiment analysis complete. Results saved to 'bank_reviews_with_sentiment.csv'")
