import matplotlib.pyplot as plt

def plot_runs(df):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.bar(df["date"], df["distance_km"], color="steelblue")
    ax1.set_title("Distanz pro Lauf")
    ax1.set_ylabel("Kilometer")
    ax1.tick_params(axis="x", rotation=45)

    ax2.plot(df["date"], df["pace_min_per_km"], marker="o", color="tomato")
    ax2.set_title("Tempo pro Lauf")
    ax2.set_ylabel("min/km")
    ax2.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("lauf_auswertung.png")
    plt.show()