import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict(data):
    arr = np.array([[
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.pedigree,
        data.age
    ]])

    prediction = model.predict(arr)[0]
    probability = model.predict_proba(arr)[0][1]  # diabetic probability

    return int(prediction), float(probability)
    