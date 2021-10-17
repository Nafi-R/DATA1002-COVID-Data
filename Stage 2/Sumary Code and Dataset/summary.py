import csv
import pandas as pd
import os
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv( folder + '/integrate_dataset.csv')

dates = df["Date"].unique() #get country names
countries = df["Country"].unique() #get country

for country in countries:
    date_group = df.groupby("Country").get_group(country).groupby("Date")
    case_data = [date_group.get_group(date)["New Cases"].aggregate(sum) for date in dates] #Add all country deaths sums to a list
    death_data = [date_group.get_group(date)["New Deaths"].aggregate(sum) for date in dates]
    vacc_data = [date_group.get_group(date)["People Fully Vaccinated per 100"].aggregate(sum) for date in dates]
    policy_data = [date_group.get_group(date)["Containment Index"].aggregate(sum) for date in dates]

    fig, ax = plt.subplots()

    plt.title(f"Summary COVID-19 Statistics for " + country)

    fig.subplots_adjust(right=0.7)

    case_plot = ax.twinx()
    death_plot = ax.twinx()
    policy_plot = ax.twinx()

    case_plot.spines.right.set_position(("axes", 1.1))
    death_plot.spines.right.set_position(("axes", 1.2))

    formatted_date = [i for i in range(0, len(dates))]
    cases, = case_plot.plot(formatted_date, case_data,"red", label="New Cases") #add countries and data to bar graph
    deaths, = death_plot.plot(formatted_date, death_data, "green", label="New Deaths")
    vacc, = ax.plot(formatted_date, vacc_data, "blue", label="People Vaccinated per 100")
    policy, = policy_plot.plot(formatted_date, policy_data, "orange", label="Containment Index")

    case_plot.set_ylabel("New Cases")
    death_plot.set_ylabel("New Deaths")
    policy_plot.set_ylabel("Containment Index")
    ax.set_ylabel("People Vaccinated per 100")
    ax.set_xlabel("Days since January 22nd 2020")

    ax.set_xlim(0, len(dates))
    ax.set_ylim(0, 100)
    case_plot.set_ylim(0, max(case_data))
    death_plot.set_ylim(0, max(death_data))
    policy_plot.set_ylim(0, 100)

    ax.legend(handles=[cases, deaths, vacc, policy],loc=2)


plt.show()


