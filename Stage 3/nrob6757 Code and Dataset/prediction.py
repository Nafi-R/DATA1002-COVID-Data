import pandas as pd
import os
from math import sqrt
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

folder = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(folder + '/integrate_dataset.csv')

country_list = df["Country"].unique()
country_group = df.groupby("Country")


for country_str in country_list:
    predictive_value = ["New Deaths"]
    predictor_values = [
        "People Vaccinated per 100",
        "People Fully Vaccinated per 100",
        "New Cases",
        "Stringency Index"	
        ]
    country_df = country_group.get_group(country_str)
    country_df = country_df.drop(columns=["Date","Country"])
    X_df = country_df[predictor_values]

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(X_df)

    pca = PCA(n_components=1)

    X = pca.fit_transform(scaled_data)
    Y = country_df[predictive_value]

    plt.scatter(X,Y)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    regr = linear_model.LinearRegression().fit(X_train, y_train)
    sample = [3] 
    sample_pred = regr.predict([sample])
    print(f"===== {country_str} Statistics ====")
    print(f"Standard Deviation Prediction: {sample}")
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