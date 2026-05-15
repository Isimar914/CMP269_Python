import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_crypto_data():
    """Helper function to load mock crypto data."""
    return pd.DataFrame({
        "Day": [1, 2, 3, 4, 5, 6, 7],
        "Bitcoin": [40000, 42000, 41000, 45000, 44000, 46000, 48000],
        "Ethereum": [2500, 2600, 2550, 2800, 2750, 2900, 3100]
    })

def task_1_trend_line():
    print("--- Task 1: Building a Trend Line ---")
    df = get_crypto_data()

    plt.plot(df["Day"], df["Bitcoin"], marker = 'o')

    plt.title("Bitcoin Price Over 7 Days")
    plt.xlabel('Day')
    plt.ylabel('Bitcoin Price ($)')

    plt.show()

def task_2_seaborn_comparison():
    print("--- Task 2: Seaborn Comparison ---")

    data = {
        "Portfolio": ["Portfolio A", "Portfolio B", "Portfolio C"],
        "Value": [10000, 15000, 8000]
    }
    df = pd.DataFrame(data)

    sns.barplot(x="Portfolio", y="Value", data=df)
    plt.title("Portfolio Value Comparison")
    plt.show()

if __name__ == "__main__":
    # Uncomment to test visuals during development
     task_1_trend_line()
     task_2_seaborn_comparison()

