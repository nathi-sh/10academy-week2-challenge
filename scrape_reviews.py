from google_play_scraper import reviews, Sort
import pandas as pd
from time import sleep
import traceback

# Define the apps dictionary BEFORE you use it
apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}

# Initialize lists to store reviews and track failures
all_reviews = []
failed_apps = []

# Now the loop to scrape reviews
for bank, app_id in apps.items():
    print(f"\nScraping {bank} ({app_id})...")
    
    try:
        for attempt in range(3):
            try:
                result, _ = reviews(
                    app_id,
                    lang='en',
                    country='et',
                    sort=Sort.MOST_RELEVANT,
                    count=400  # Limit to 400 reviews per bank
                )
                
                if result:
                    print(f"Success! Found {len(result)} reviews")
                    all_reviews.extend([{
                        'bank': bank,
                        'review': r['content'],
                        'rating': r['score'],
                        'date': r['at'].strftime('%Y-%m-%d'),
                        'source': 'Google Play'
                    } for r in result])
                    break
                else:
                    print(f"Attempt {attempt+1}: Got 0 reviews, retrying...")
                    sleep(5)
            except Exception as e:
                print(f"Attempt {attempt+1} failed: {str(e)}")
                sleep(10)
                if attempt == 2:
                    raise
    except Exception as e:
        print(f"Failed to scrape {bank}: {traceback.format_exc()}")
        failed_apps.append(bank)

# After scraping, you can save the data or print summary, e.g.:
if all_reviews:
    df = pd.DataFrame(all_reviews)
    print("\nData Summary:")
    print(f"Total reviews collected: {len(df)}")
    print("Reviews per bank:")
    print(df['bank'].value_counts())
    
    df.to_csv('bank_reviews.csv', index=False)
    print("\nSaved reviews to bank_reviews.csv")
else:
    print("\nWarning: No reviews were collected!")

if failed_apps:
    print("\nFailed to scrape these banks:", ", ".join(failed_apps))
