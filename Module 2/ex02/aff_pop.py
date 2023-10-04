from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def filter_data(data: pd.DataFrame, country: str):
    '''Filters the dataset to obtain the data of the targeted
    country in the time period of 1800-2050'''

    # Target the row that has the country of interest
    filtered_row = data.loc[data['country'] == country]
    if filtered_row.empty:
        raise AssertionError(f"{country} does not exist in the csv file.")

    # Replace the strings in the data with the float equivalent
    mp = {'k': '* 10**3', 'M': '* 10**6'}
    filtered_year = filtered_row.loc[:, "1800":"2050"].replace(mp, regex=True)

    # Use squeeze() to convert the data into a plottable Series
    res = pd.DataFrame(filtered_year.apply(pd.eval)).squeeze()
    return (res)


def process_data(data: pd.DataFrame):
    '''Process the csv file and displays the population of two countries
    on the same plot.'''

    # What countries to look for
    home_country = "Malaysia"
    away_country = "France"

    # Filter out the data to the two intended countries
    home_data = filter_data(data, home_country)
    away_data = filter_data(data, away_country)

    # Plotting
    home_data.plot(label=home_country)
    away_data.plot(label=away_country)
    plt.legend()
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.savefig(f"Population_{home_country}_v_{away_country}.jpg")
    # plt.show()


def main():
    '''Main Driver Function'''

    try:
        data = load('population_total.csv')
        if data is None:
            raise AssertionError("load function must be given a valid file.")
        process_data(data)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
