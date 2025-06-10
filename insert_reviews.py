import oracledb
import pandas as pd
from datetime import datetime

# Load cleaned data
try:
    # --- CORRECTED FILENAME ---
    df = pd.read_csv('bank_reviews_with_sentiment_and_themes.csv')
    print(f"Loaded {len(df)} reviews from CSV")
    print("Columns in file:", df.columns)

except FileNotFoundError:
    print("Error: bank_reviews_with_sentiment_and_themes.csv not found")
    exit(1)

# Oracle DB connection
try:
    conn = oracledb.connect(
        user="bank_reviews",
        password="0902",
        dsn="localhost:1521/XEPDB1"
    )
    cursor = conn.cursor()
    print("Successfully connected to Oracle Database")

    # Insert banks and map names to IDs
    bank_ids = {}
    for bank in df['bank'].unique():
        cursor.execute("SELECT bank_id FROM Banks WHERE bank_name = :1", [bank])
        row = cursor.fetchone()
        if row:
            bank_ids[bank] = row[0]
        else:
            bank_id_var = cursor.var(oracledb.NUMBER)
            cursor.execute("""
                INSERT INTO Banks (bank_name)
                VALUES (:1)
                RETURNING bank_id INTO :2
            """, [bank, bank_id_var])
            bank_ids[bank] = int(bank_id_var.getvalue()[0])
    
    conn.commit()
    print("Bank names processed and committed.")

    # Prepare review data for batch insert
    review_data = []
    for _, row in df.iterrows():
        try:
            # Prepare data from all columns
            review_data.append((
                bank_ids[row['bank']],
                row['review'][:4000] if pd.notna(row['review']) else None,
                float(row['rating']) if pd.notna(row['rating']) else None,
                pd.to_datetime(row['date']) if pd.notna(row['date']) else None,
                row['source'] if pd.notna(row['source']) else 'Unknown',
                row['sentiment_label'] if pd.notna(row['sentiment_label']) else None,
                float(row['sentiment_score']) if pd.notna(row['sentiment_score']) else None,
                row['identified_theme(s)'] if pd.notna(row['identified_theme(s)']) else None
            ))
        except Exception as e:
            print(f"Error processing review row: {e}")
            continue

    # Batch insert reviews
    if review_data:
        cursor.executemany("""
            INSERT INTO Reviews (bank_id, review_text, rating, review_date, source, sentiment_label, sentiment_score, themes)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
        """, review_data)
        
        conn.commit()
        print(f"Successfully inserted {len(review_data)} reviews")
    else:
        print("No valid review data was found to insert.")

except oracledb.DatabaseError as e:
    print(f"Oracle Database Error: {e}")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn:
        conn.close()
    print("Database connection closed")