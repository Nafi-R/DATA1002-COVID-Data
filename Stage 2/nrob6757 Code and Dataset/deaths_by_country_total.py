import pandas as pd
import os
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv( folder + '/integrate_dataset.csv')

countries = df["Country"].unique() #get country names
country_grouped = df.groupby("Country") #group each country
sum_data = [country_grouped.get_group(country)["New Deaths"].aggregate("sum") for country in countries] #Add all country deaths sums to a list

print(country_grouped["New Deaths"].describe()) #Produce a grouped aggregate summary

plt.bar(countries, sum_data,color=["black","green","blue","red"]) #add countries and data to bar graph
plt.xlabel("Countries")
plt.ylabel("Total Deaths")
plt.title("Deaths from COVID-19")


for x,y in zip(countries,sum_data):
    plt.annotate("{:,}".format(y) + " Deaths", # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.show()


