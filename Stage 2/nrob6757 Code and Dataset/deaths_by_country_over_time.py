import pandas as pd
import os
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv( folder + '/integrate_dataset.csv')

dates = df["Date"].unique()
countries = df["Country"].unique().tolist() #get country names
colours = ["blue", "green", "red","orange"]
linestyles = ["dotted", "dashed", "solid","dashdot"]
formatted_date = [i for i in range(0, len(dates))]
handles = []
for country in countries:
    country_group = df.groupby("Country").get_group(country)
    country_date_group = country_group.groupby("Date")
    data = [country_date_group.get_group(date)["New Deaths"].aggregate("sum") for date in dates]
    h, = plt.plot(formatted_date, data, colours[countries.index(country)], label=country,linestyle=linestyles[countries.index(country)])
    handles.append(h)
plt.xlabel("Days since January 22nd 2020")
plt.ylabel("New Deaths")
plt.title("Daily New Deaths since January 22nd 2020")
plt.legend(handles=handles)
plt.show()