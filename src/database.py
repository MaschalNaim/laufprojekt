import sqlite3

def save_to_db(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql("runs", conn, if_exists="replace", index=False)
    conn.close()
    print("✅ Daten in Datenbank gespeichert!")

def query_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("\n=== SQL Abfragen ===")

    # Alle Läufe
    cursor.execute("SELECT * FROM runs")
    print("\nAlle Läufe:")
    for row in cursor.fetchall():
        print(row)

    # Schnellster Lauf
    cursor.execute("""
        SELECT date, distance_km, pace_min_per_km 
        FROM runs 
        ORDER BY pace_min_per_km ASC 
        LIMIT 1
    """)
    print("\nSchnellster Lauf:")
    print(cursor.fetchone())

    # Läufe über 5km
    cursor.execute("""
        SELECT date, distance_km 
        FROM runs 
        WHERE distance_km > 5
    """)
    print("\nLäufe über 5km:")
    for row in cursor.fetchall():
        print(row)

    conn.close()