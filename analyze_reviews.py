import oracledb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# --- Step 1: Load Data from Oracle ---
try:
    conn = oracledb.connect(
        user="bank_reviews",
        password="0902", # Use your actual password
        dsn="localhost:1521/XEPDB1"
    )
    print("Successfully connected to Oracle Database.")

    # Use a JOIN to get the bank names along with the reviews
    sql_query = """
        SELECT r.review_text, r.rating, r.review_date, r.source, 
               r.sentiment_label, r.sentiment_score, r.themes, b.bank_name
        FROM Reviews r
        JOIN Banks b ON r.bank_id = b.bank_id
    """
    df = pd.read_sql(sql_query, conn)
    print(f"Successfully loaded {len(df)} reviews into a DataFrame.")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("Database connection closed.")

# --- Step 2: Analyze and Find Insights (Example) ---

# Find most common themes (pain points/drivers)
print("\nMost common themes mentioned in reviews:")
print(df['THEMES'].value_counts().head(10))

# Compare average ratings between banks
print("\nAverage rating per bank:")
print(df.groupby('BANK_NAME')['RATING'].mean().sort_values(ascending=False))


# --- Step 3: Create Visualizations (Example) ---

# Set plot style
sns.set_style("whitegrid")

# a. Sentiment Distribution Bar Chart (Corrected to avoid warning)
plt.figure(figsize=(8, 6))
sns.countplot(x='SENTIMENT_LABEL', data=df, palette='viridis', order=df['SENTIMENT_LABEL'].value_counts().index, hue='SENTIMENT_LABEL', legend=False)
plt.title('Overall Sentiment Distribution of Bank Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.savefig('sentiment_distribution.png') # Saves the plot as an image
plt.show()


# b. Keyword Cloud for a specific theme
# Create a word cloud from all review text for demonstration
all_reviews_text = ' '.join(df['REVIEW_TEXT'].dropna())

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_reviews_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for All Reviews')
plt.savefig('all_reviews_wordcloud.png')
plt.show()