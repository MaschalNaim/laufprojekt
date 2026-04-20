from src.load_data import load_data
from src.process_data import process_data, summarize
from src.visualize import plot_runs
from src.database import save_to_db, query_db
from src.report import create_report

df = load_data("data/raw_runs.csv")
df = process_data(df)

summarize(df)
plot_runs(df)
save_to_db(df, "data/runs.db")
query_db("data/runs.db")
create_report(df)