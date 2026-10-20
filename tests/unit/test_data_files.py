from pathlib import Path

DATA_DIR = Path("data/fixtures/bronze_phase")

EXPECTED_FILES = [
    "DimBusiness_Unit.csv",
    "DimDate.csv",
    "DimEthnic_Group.csv",
    "DimForeign_Indicator.csv",
    "DimGender.csv",
    "DimJob_Grade.csv",
    "DimLocation.csv",
    "DimStaff.csv",
    "FactStaff_Monthly.csv",
]

def test_expected_csv_files_exist():
    """Verify that all expected bronze-phase CSV files exist."""
    missing_files = [
        filename
        for filename in EXPECTED_FILES
        if not (DATA_DIR / filename).is_file()
    ]

    assert not missing_files, (
        f"Missing expected CSV files: {missing_files}"
    )