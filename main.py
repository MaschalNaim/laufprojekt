from src.load_data import load_data
from src.process_data import process_data, summarize
from src.visualize import plot_runs
from src.database import save_to_db, query_db
from src.report import create_report
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "data", "raw_runs.csv")
db_path = os.path.join(base_dir, "data", "runs.db")

df = load_data(path)
df = process_data(df)

summarize(df)
plot_runs(df)
save_to_db(df, db_path)
query_db(db_path)
create_report(df)