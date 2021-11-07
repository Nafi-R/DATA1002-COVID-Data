import pandas as pd
from math import sqrt
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('integrate_dataset.csv')

countries = ['Australia','India','US','United Kingdom']
group_by_country = df.groupby("Country")

for country in countries:
    country_df = group_by_country.get_group(country)
    X = country_df['New Cases'].values.reshape(-1,1)
    y = country_df['New Deaths'].values.reshape(-1,1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    regr = linear_model.LinearRegression().fit(X_train, y_train)
    sample  = [100]
    sample_pred = regr.predict([sample])
    print("\n----------{} Predictive Modeling Data---------\n".format(country))
    print('Predicted value:{}\n'.format(sample_pred))
    print('Coefficient:{}\n'.format(regr.coef_))
    y_pred = regr.predict(X_test)# Use the model to predict y from X_test
    mse = metrics.mean_squared_error(y_test, y_pred)# Root mean squared error
    print('Root mean squared error (RMSE):', sqrt(mse))
    print("")
    print('R-squared score:', metrics.r2_score(y_test, y_pred))
    print('-------------------------------------------------\n')










