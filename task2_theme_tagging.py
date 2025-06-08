import pandas as pd
from theme_keywords import theme_keywords  # Import the dictionary

# Load reviews with sentiment labels
df = pd.read_csv("bank_reviews_with_sentiment.csv")

# Define the function to detect themes
def find_themes(text):
    text = str(text).lower()
    themes_found = []
    for theme, keywords in theme_keywords.items():
        if any(keyword in text for keyword in keywords):
            themes_found.append(theme)
    return ', '.join(themes_found) if themes_found else 'No Theme'

# Apply the function to each review
df['identified_theme(s)'] = df['review'].apply(find_themes)

# Save the updated DataFrame
df.to_csv("bank_reviews_with_sentiment_and_themes.csv", index=False)
print("✅ Themes added and saved to 'bank_reviews_with_sentiment_and_themes.csv'")
