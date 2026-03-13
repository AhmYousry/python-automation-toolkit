from tools.file_renamer import rename_files
from tools.csv_cleaner import clean_csv
from tools.report_generator import generate_report

rename_files("data")
clean_csv("data/input.csv")
generate_report("data/clean_data.csv")