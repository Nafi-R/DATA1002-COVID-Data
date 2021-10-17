import pandas as pd
import os
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv( folder + '/integrate_dataset.csv')

date_group = df.groupby('Date')
dates = df["Date"].unique().tolist() #Get all unique dates
countries = df['Country'].unique().tolist() #Get all unique countries (e.g. Australia, India, US, United Kingdom)
vaccine_dict = {}
for i in range(0, 100, +10): #Creates bins in increments of 10
    vaccine_dict[i] = 0
country_grouped = df.groupby("Country") #group each country
vacc_bin = [f"{key} - {key + 9}" for key in vaccine_dict] #List of vaccination percentage bins (e.g 10,20,30, etc)
for country in countries:
    for date in dates:
       date_country_df =  date_group.get_group(date).groupby("Country").get_group(country)
       vaccination_per_100 = date_country_df["People Fully Vaccinated per 100"].aggregate(sum)
       deaths = date_country_df["New Deaths"].aggregate(sum)
       vaccine_dict[(vaccination_per_100//10)*10] += deaths


#Print out summary
print("Percentage fully vaccinated (%)", "Deaths")
for vaccine_percentage in vaccine_dict:
    vacc_string = f"{vaccine_percentage} - {vaccine_percentage + 9}%:"
    print(vacc_string," " * (30 - len(vacc_string)) ,f"{vaccine_dict[vaccine_percentage]}")

vacc_deaths = [vaccine_dict[key] for key in vaccine_dict] #Convert vaccine deaths to a list

plt.bar(vacc_bin, vacc_deaths,color=["black","green","blue","red","pink","orange","yellow"]) #add countries and data to bar graph
plt.xlabel("Percentage of Population Fully Vaccinated (%)")
plt.ylabel("Total Deaths")
max_deaths = max(vacc_deaths) 
plt.ylim(0,(max_deaths + max_deaths/10))
plt.title("Deaths from COVID-19 for percentage of Population fully Vaccinated")
plt.xticks(vacc_bin)
plt.yticks([])


for x,y in zip(vacc_bin,vacc_deaths):
    plt.annotate("{:,}".format(y) + " Deaths", # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.show()


