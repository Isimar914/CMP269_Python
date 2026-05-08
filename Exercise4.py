import pandas as pd

def task_1_series_creation():
    print("--- Task 1: Building Series ---")

    buildings = {
        "Gillet": 4,
        "Carmen": 3,
        "Music": 3,
        "Library": 4
    }

    series = pd.Series(buildings)
    print(series)

def task_2_dataframe_creation():
    print("\n--- Task 2: Course DataFrame ---")

    courses = {
        "CourseCode": ["CMP168", "CMP269", "CMP338"],
        "Credits": [4, 4, 4],
        "Enrolled": [25, 30,20]
    }

    df = pd.DataFrame(courses)
    print(df)

def task_3_data_manipulation():
    print("\n--- Task 3: Filtering and Math ---")

    courses = {
        "CourseCode": ["CMP168", "CMP269", "CMP338"],
        "Credits": [4, 4, 4],
        "Enrolled": [25, 30, 20]
    }

    df = pd.DataFrame(courses)

    filtered_df = df[df["Enrolled"] > 20]
    print(filtered_df)

    total_students = df["Enrolled"].sum()
    print("\nTotal Students: ", total_students)

def task_4_csv_integration():
    print("\n--- Task 4: Easy CSV I/O ---")

    stocks = {
        "Symbol": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
        "Price": [839, 854, 129, 267, 854]
    }

    df = pd.DataFrame(stocks)
    df.to_csv("stocks.csv", index=False)
    df_loaded = pd.read_csv("stocks.csv")
    print(df_loaded)

if __name__ == "__main__":
    # Uncomment these as you work through the assignment
     task_1_series_creation()
     task_2_dataframe_creation()
     task_3_data_manipulation()
     task_4_csv_integration()
