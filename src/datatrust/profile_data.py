import csv
from pathlib import Path

DATA_DIR = Path("data/fixtures/bronze_phase")

def profile_csv(file_path: Path) -> None:
    """Print a CSV file's row count and column names."""
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        headers = next(reader, [])
        row_count = sum(1 for _ in reader)

    print(f"\nFile: {file_path.name}")
    print(f"Rows: {row_count}")
    print(f"Columns ({len(headers)}): {', '.join(headers)}")

def main() -> None:
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {DATA_DIR}")

    for file_path in csv_files:
        profile_csv(file_path)

if __name__ == "__main__":
    main()