import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

#make a dataframe (table) that shows people fully vaccinated and total
#number of cases from 22-January-2020 until 10-September-2021 across 4 countries


##### Bar plot of Total number of cases in 4 countries
##
df = pd.read_csv('integrate_dataset.csv',index_col = 'Country')
total_cases = df.groupby(['Country'])['New Cases'].sum().reset_index()#making the dataframe
total_cases2 = total_cases.rename({'New Cases':'Total Number of Cases'},axis=1)#
print(tabulate(total_cases2,headers = 'keys',tablefmt = 'fancy_grid'))

plt.figure(figsize=(9,8)) #denoting figure size
plot = sns.barplot(x='Country',y='New Cases',data=total_cases) #plotting barplot with seaborn
plt.xlabel("Country",size=14) #x axis label and size
plt.ylabel('Number of Cases',size=14) #y axis label and size
plt.bar_label(plot.containers[0],fmt='%.0f') #labelling the bars with the number of cases
plt.ticklabel_format(useOffset=False, style='plain', axis='y')#suppress numbers inscientific format
plt.savefig("Bar_plot_Cases.png")
plt.title("Total Number of Cases",size=18)
plt.show()
##
#####Horizontal compund bar chart showing each countries stats on cases and vaccinations
##
cases_and_vaccine =  {'Cases':[68045,33174954,40330381,7132076],
                       'Vaccinated':[8422627,171150008,17789945,43895440]}

index = ['Australia','India','US','United Kingdom']
dataFrame = pd.DataFrame(data = cases_and_vaccine)
dataFrame.index = index
s=dataFrame.plot.barh(rot=15, title = "Number of Cases vs Number of People Fully Vaccinated")
plt.ticklabel_format(useOffset=False, style='plain', axis='x')
plt.bar_label(s.containers[0],fmt='%.0f')
plt.bar_label(s.containers[1],fmt='%.0f',padding= -30)
plt.show(block=True)


#Average Number of cases in 2021 vs 2020
cases_2020 = {}
cases_2021 = {}
is_first_line = True
for row in open("integrate_dataset.csv"):
    if is_first_line:
        is_first_line = False
    else:
        values = row.split(",")
        date = values[0]
        year = date.split('/')[2]
        country = values[1]
        cases =  int(values[6])
        if year == '2020':
            if country in cases_2020:
                cases_2020[country] += cases
            else:
                cases_2020[country] = cases
        elif year == "2021":
            if country in cases_2021:
                cases_2021[country] += cases
            else:
                    cases_2021[country] = cases

dict_2020= {x:cases_2020[x]/345 for x in cases_2020}
dict_2021={x:cases_2021[x]/253 for x in cases_2021}
k = 2
daily_average_2020 = {key : round(dict_2020[key], k) for key in dict_2020}
daily_average_2021 = {key : round(dict_2021[key], k) for key in dict_2021}

df2020 = pd.DataFrame(daily_average_2020.items(),columns=['Country','Average cases per day in 2020'])
df2021 = pd.DataFrame(daily_average_2021.items(),columns=['Country','Average cases per day in 2021'])

df = pd.merge(df2020,df2021,on='Country')
print(tabulate(df,headers= 'keys',tablefmt='fancy_grid'))

s=df.plot(rot=0,x="Country",y=['Average cases per day in 2020','Average cases per day in 2021'],
kind='bar',figsize=(10,8))
plt.ylabel('Cases',size=10)
plt.bar_label(s.containers[0],fmt='%.0f') #labelling the bars with the number of cases
plt.bar_label(s.containers[1],fmt='%.0f') #labelling the bars with the number of cases
plt.title("Daily Average number of cases in 2020 and 2021",size=18)
plt.savefig("Bar_plot_Average.png")
plt.show(block=True)