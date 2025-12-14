import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("data/student_scores.csv")

X = data[['Hours']]
y = data['Score']

model = LinearRegression()
model.fit(X, y)

with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved")