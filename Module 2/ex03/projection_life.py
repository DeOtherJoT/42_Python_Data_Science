from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def process_data(gdp_data: pd.DataFrame, life_data: pd.DataFrame):
	'''Takes the dataframes and presents it as tasked'''

	# Data retrieval
	year = '1900'
	filtered_gdp = gdp_data.loc[:, year]
	filtered_gdp = filtered_gdp.rename('Gross Domestic Product')
	filtered_life = life_data.loc[:, year]
	filtered_life = filtered_life.rename('Life Expectancy')

	# Error Checks
	if filtered_gdp is None or filtered_life is None:
		raise AssertionError(f"Datasets are missing the year {year}.")
	if filtered_gdp.size != filtered_life.size:
		raise AssertionError("Datasets are of not equal size")

	# Combine DataFrames
	combined_data = pd.concat([filtered_gdp, filtered_life], axis=1)

	# Plot it like how I should have done two exercises ago
	combined_data.plot(
		kind = 'scatter',
		x = 'Gross Domestic Product',
		y = 'Life Expectancy',
		logx = True,
		title = year
	)
	plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
	plt.savefig("result.jpg")
	# plt.show()


def main():
	'''Main Driver Function'''

	gdp_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
	life_file = "life_expectancy_years.csv"

	try:
		gdp_data = load(gdp_file)
		life_data = load(life_file)
		if (gdp_data is None or life_data is None):
			raise AssertionError("The csv files are invalid.")
		process_data(gdp_data, life_data)
	except Exception as e:
		print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
	main()