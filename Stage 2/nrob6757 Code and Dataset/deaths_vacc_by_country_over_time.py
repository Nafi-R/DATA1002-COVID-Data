import pandas as pd
import os
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv( folder + '/integrate_dataset.csv')

dates = df["Date"].unique() #get country names
countries = df["Country"].unique() #get country

for country in countries:
    date_group = df.groupby("Country").get_group(country).groupby("Date")
    death_data = [date_group.get_group(date)["New Deaths"].aggregate(sum) for date in dates]
    vacc_data = [date_group.get_group(date)["People Fully Vaccinated per 100"].aggregate(sum) for date in dates]

    fig, ax = plt.subplots()

    plt.title(f" COVID-19 Deaths & Vaccination Rate for " + country)

    fig.subplots_adjust(right=0.7)

    death_plot = ax.twinx()

    death_plot.spines.right.set_position(("axes", 1.1))

    formatted_date = [i for i in range(0, len(dates))]
    deaths, = death_plot.plot(formatted_date, death_data, "red", label="New Deaths")
    vacc, = ax.plot(formatted_date, vacc_data, "blue", label="People Vaccinated per 100")

    death_plot.set_ylabel("New Deaths")
    ax.set_ylabel("People Vaccinated per 100")
    ax.set_xlabel("Days since January 22nd 2020")

    ax.set_xlim(0, len(dates))
    ax.set_ylim(0, 100)
    death_plot.set_ylim(0, max(death_data))

    ax.legend(handles=[deaths, vacc],loc=2)


plt.show()
