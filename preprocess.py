import pandas as pd

# Load your scraped data CSV
df = pd.read_csv('bank_reviews.csv')

# Remove duplicates based on review text (you can customize columns if needed)
df = df.drop_duplicates(subset=['review'])

# Drop rows with missing critical fields
df = df.dropna(subset=['review', 'rating', 'date', 'bank'])

# Save cleaned data to a new CSV file
df.to_csv('bank_reviews_cleaned.csv', index=False)

print("Preprocessing done. Cleaned data saved to bank_reviews_cleaned.csv")
print(f"Total reviews after cleaning: {len(df)}")
print(df['bank'].value_counts())
