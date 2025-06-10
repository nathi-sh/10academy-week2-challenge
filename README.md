Bank App Review Analysis: CBE, BOA, and Dashen
This project scrapes, processes, analyzes, and stores user reviews for the mobile banking applications of three major Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank. The goal is to derive actionable insights into user satisfaction, identify common issues, and recommend improvements.

Task 1: Data Collection & Preprocessing
Scraping: Scraped the 400 most recent user reviews from the Google Play Store for each of the following apps:

CBE: com.combanketh.mobilebanking

BOA: com.boa.boaMobileBanking

Dashen: com.dashen.dashensuperapp

Method: Utilized the google-play-scraper Python library.

Cleaning: The collected raw data was cleaned by removing duplicate reviews, handling missing values, and normalizing all dates to a standard YYYY-MM-DD format.

Output: The final cleaned dataset was saved to bank_reviews_cleaned.csv.

Task 2: Sentiment Analysis and Theme Tagging
This task analyzed customer feedback for the bank apps using NLP techniques.

Scripts Used:

task2_sentiment.py: Performed sentiment analysis using a pre-trained DistilBERT model to classify reviews as positive, negative, or neutral.

task2_keywords_themes.py: Extracted the most relevant keywords from the review text using the TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer.

task2_theme_tagging.py: Tagged each review with a thematic label (e.g., "UI/UX", "App Stability") based on keyword matches.

Key Findings:

Most common themes: "Account Access Issues", "UI/UX", and "Transaction Performance" were frequently discussed.

Frequent sentiments: Negative sentiment was high for reviews related to "App Stability & Bugs," while positive sentiment dominated in "General Feedback."

115 reviews had no specific theme match.

Outputs:

bank_reviews_with_sentiment.csv

bank_reviews_with_sentiment_and_themes.csv

top_keywords.csv

Task 3: Store Cleaned Data in Oracle
To ensure data persistence and simulate a real-world enterprise environment, the processed data was stored in a relational database.

Database: Oracle XE (Express Edition) was set up to host the data.

Schema Design: A relational schema was designed with two primary tables:

Banks: Stores information about each bank (e.g., bank_id, bank_name).

Reviews: Stores all processed review data, linked to the Banks table via a foreign key.

Data Insertion: A Python script (insert_reviews.py) using the oracledb library was created to connect to the database and populate the tables from the bank_reviews_with_sentiment_and_themes.csv file.

Outcome: All 1181 processed reviews were successfully stored in the Oracle database. A full database dump (bank_reviews_dump.dmp) was created to ensure reproducibility.

Task 4: Insights and Recommendations
The final task involved querying the database to derive insights, visualize the findings, and formulate actionable recommendations.

Analysis:

A Python script (analyze_reviews.py) was used to fetch the complete dataset from Oracle into a pandas DataFrame.

Key Drivers & Pain Points: Analysis of themes confirmed that "User Interface & Experience" and "Transaction Performance" are critical areas influencing user satisfaction. App stability and bugs are major sources of user frustration.

Bank Comparison: Dashen Bank (average rating ~4.4) significantly outperforms both CBE (~2.9) and BOA (~2.0) in user satisfaction.

Visualizations:

Generated and saved several plots using Matplotlib and Seaborn to illustrate key findings, including:

sentiment_distribution.png: A bar chart showing the overall sentiment across all reviews.

all_reviews_wordcloud.png: A word cloud highlighting the most frequently used terms in reviews.

Recommendations:

For CBE & BOA: Prioritize a complete overhaul of the app's User Interface & Experience (UI/UX) to improve usability and match user expectations set by competitors like Dashen.

For All Banks: Invest in rigorous Quality Assurance (QA) to address and reduce the high number of complaints related to app crashes and bugs.

Ethical Considerations: Noted that review platforms often have a negative skew, as dissatisfied customers are typically more motivated to leave feedback.