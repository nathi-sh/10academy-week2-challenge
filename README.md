Task 1: Data Collection & Preprocessing
Scraped 400 latest user reviews from Google Play Store for each bank:

CBE: com.combanketh.mobilebanking

BOA: com.boa.boaMobileBanking

Dashen: com.dashen.dashensuperapp

Used google-play-scraper Python library for scraping.

Cleaned data by removing duplicates and handling missing values.

Normalized dates to YYYY-MM-DD format.

Saved cleaned data to bank_reviews_cleaned.csv.

## Task 2: Sentiment Analysis and Theme Tagging

### Summary
This task analyzes customer feedback for Ethiopian bank apps (CBE, BOA, Dashen) using NLP techniques.

### Scripts
- `task2_sentiment.py`: Performs sentiment analysis using a pre-trained DistilBERT model.
- `task2_keywords_themes.py`: Extracts top keywords using TF-IDF.
- `task2_theme_tagging.py`: Tags each review with a thematic label based on keyword matches.
- `task2_analysis.py`: Generates bar charts for theme frequency and sentiment distribution.

### Key Findings
- **Most common themes**: Account Access Issues, UI/UX, and Transaction Performance.
- **Frequent sentiments**:
  - Negative sentiment is high for App Stability & Bugs.
  - Positive sentiment dominates in General Feedback.
- 115 reviews had no theme match.

### Outputs
- `bank_reviews_with_sentiment.csv`
- `bank_reviews_with_sentiment_and_themes.csv`
- `top_keywords.csv`

