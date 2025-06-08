Task 1: Data Collection & Preprocessing
Scraped 400 latest user reviews from Google Play Store for each bank:

CBE: com.combanketh.mobilebanking

BOA: com.boa.boaMobileBanking

Dashen: com.dashen.dashensuperapp

Used google-play-scraper Python library for scraping.

Cleaned data by removing duplicates and handling missing values.

Normalized dates to YYYY-MM-DD format.

Saved cleaned data to bank_reviews_cleaned.csv.

Task 2: Sentiment and Thematic Analysis (In Progress)
Performed sentiment analysis using distilbert-base-uncased-finetuned-sst-2-english model.

Extracted keywords and significant phrases from reviews.

Saved sentiment scores and keyword data to CSV files.

Next step: Group extracted keywords into 3–5 meaningful themes per bank for thematic analysis.