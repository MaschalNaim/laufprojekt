import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def create_report(df):
    fig = plt.figure(figsize=(10, 12))
    fig.suptitle("Lauf-Auswertung", fontsize=16, fontweight="bold")

    gs = gridspec.GridSpec(3, 1, figure=fig, hspace=0.5)

    ax1 = fig.add_subplot(gs[0])
    ax1.bar(df["date"], df["distance_km"], color="steelblue")
    ax1.set_title("Distanz pro Lauf")
    ax1.set_ylabel("Kilometer")
    ax1.tick_params(axis="x", rotation=45)

    ax2 = fig.add_subplot(gs[1])
    ax2.plot(df["date"], df["pace_min_per_km"], marker="o", color="tomato")
    ax2.set_title("Tempo pro Lauf")
    ax2.set_ylabel("min/km")
    ax2.tick_params(axis="x", rotation=45)

    ax3 = fig.add_subplot(gs[2])
    ax3.axis("off")
    summary = (
        f"Anzahl Laeufe:      {len(df)}\n"
        f"Gesamtdistanz:      {df['distance_km'].sum()} km\n"
        f"Laengster Lauf:     {df['distance_km'].max()} km\n"
        f"Schnellstes Tempo:  {df['pace_min_per_km'].min():.2f} min/km\n"
        f"Durchschnittstempo: {df['pace_min_per_km'].mean():.2f} min/km"
    )
    ax3.text(0.1, 0.5, summary, fontsize=12, verticalalignment="center",
             fontfamily="monospace")

    plt.savefig("lauf_report.pdf", format="pdf", bbox_inches="tight")
    print("PDF gespeichert.")