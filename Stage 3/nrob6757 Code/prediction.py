import pandas as pd
import os
from math import sqrt
from sklearn import metrics
from sklearn import neighbors
from sklearn.model_selection import train_test_split

folder = os.path.dirname(os.path.realpath(__file__))


df = pd.read_csv(folder + '/integrate_dataset.csv')
X = df[["Containment Index", "New Cases"]]     # slice dataFrame for input variables
y = df['New Deaths']        # slice dataFrame for target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
neigh = neighbors.KNeighborsRegressor(n_neighbors=4).fit(X_train, y_train)

# Let's create one sample and predict the number of comments
sample = [200, 200]        # a sample with 1000 likes and 100 dislikes
sample_pred = neigh.predict([sample])
print('----- Sample case -----')
print("likes:",sample[0])
print("dislikes:",sample[1])
print('Predicted number of comments:', int(sample_pred))
print('-----------------------')

# Use the model to predict X_test
y_pred = neigh.predict(X_test)
# Root mean squared error
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
# R-squared score: 1 is perfect prediction
print('R-squared score:', metrics.r2_score(y_test, y_pred))
