import sqlite3

def save_to_db(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql("runs", conn, if_exists="replace", index=False)
    conn.close()
    print("Daten gespeichert.")

def query_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("\nAlle Laeufe:")
    cursor.execute("SELECT * FROM runs")
    for row in cursor.fetchall():
        print(row)

    print("\nSchnellster Lauf:")
    cursor.execute("""
        SELECT date, distance_km, pace_min_per_km 
        FROM runs 
        ORDER BY pace_min_per_km ASC 
        LIMIT 1
    """)
    print(cursor.fetchone())

    print("\nLaeufe ueber 5km:")
    cursor.execute("""
        SELECT date, distance_km 
        FROM runs 
        WHERE distance_km > 5
    """)
    for row in cursor.fetchall():
        print(row)

    conn.close()