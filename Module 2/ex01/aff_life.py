import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def ft_display(data: pd.DataFrame):
    '''Takes the data loaded from the csv file and displays the information
    of the country of the 42 campus (Malaysia)'''

    country = 'Malaysia'
    target = data.loc[data['country'] == country]
    # print(target)
    if target.empty:
        raise AssertionError("Country must exist in the csv file.")
    data = target.iloc[:, 1:].reset_index(drop=True).squeeze()
    data.plot()
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.savefig(f'{country}_expectancy.jpg')
    # plt.show()


def main():
    '''Main driver function'''

    try:
        data = load('life_expectancy_years.csv')
        if data is None:
            raise AssertionError("load function must be given a valid file.")
        ft_display(data)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
