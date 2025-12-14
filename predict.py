import pickle

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

hours = [[1.5]]

predicted_score = model.predict(hours)

print(f"Predicted score for studying {hours[0][0]} hours: {predicted_score[0]:.2f}")