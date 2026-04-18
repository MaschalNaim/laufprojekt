def process_data(df):
    df["pace_min_per_km"] = df["time_min"] / df["distance_km"]
    return df

def summarize(df):
    print("=== Zusammenfassung ===")
    print(f"Anzahl Läufe:        {len(df)}")
    print(f"Gesamtdistanz:       {df['distance_km'].sum()} km")
    print(f"Längster Lauf:       {df['distance_km'].max()} km")
    print(f"Schnellstes Tempo:   {df['pace_min_per_km'].min():.2f} min/km")
    print(f"Durchschnittstempo:  {df['pace_min_per_km'].mean():.2f} min/km")