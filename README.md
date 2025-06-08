# Fintech App Reviews Scraping

## Task 1: Data Collection & Preprocessing

- Scraped 400 latest user reviews from Google Play Store for each bank:
  - CBE: `com.combanketh.mobilebanking`
  - BOA: `com.boa.boaMobileBanking`
  - Dashen: `com.dashen.dashensuperapp`
- Used `google-play-scraper` python library.
- Cleaned data by removing duplicates and missing values.
- Normalized dates to `YYYY-MM-DD` format.
- Saved data to `bank_reviews_cleaned.csv`.
