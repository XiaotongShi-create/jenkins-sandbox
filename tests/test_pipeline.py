def test_csv_exists():
    import os
    assert os.path.exists("Electric_Vehicle_Population_Data.csv"), "CSV file not found!"