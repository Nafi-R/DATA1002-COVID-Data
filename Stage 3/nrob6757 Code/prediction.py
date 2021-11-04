import pandas as pd
import os
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split

folder = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(folder + '/integrate_dataset.csv')

country_list = df["Country"].unique()
country_group = df.groupby("Country")

for country_str in country_list:
    country_df = country_group.get_group(country_str)
    x = country_df.iloc[:,-2:-1]
    y = country_df.iloc[:,8]
    plt.scatter(x,y)



for country_str in country_list:
    country_df = country_group.get_group(country_str)
    X = country_df.iloc[:,-2:-1]
    Y = country_df.iloc[:,8]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    regr = linear_model.LinearRegression().fit(X_train, y_train)
    sample = [80] 
    sample_pred = regr.predict([sample])
    print(f"===== {country_str} Statistics ====")
    print(f"Predicted value : {sample_pred}")
    print('Coefficients:')
    print(regr.coef_)
    # Use the model to predict y from X_test
    y_pred = regr.predict(X_test)
    # Root mean squared error
    mse = metrics.mean_squared_error(y_test, y_pred)
    print('Root mean squared error (RMSE):', sqrt(mse))
    # R-squared score: 1 is perfect prediction
    print('R-squared score:', metrics.r2_score(y_test, y_pred))

plt.show()