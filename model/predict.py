import pickle
import pandas as pd

with open("logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

features = ['cloud', 'humidity', 'sunshine', 'windspeed', 'dewpoint']

def predict_rain(input_values):
    df = pd.DataFrame([input_values], columns=features)
    df_scaled = scaler.transform(df)

    pred = model.predict(df_scaled)
    prob = model.predict_proba(df_scaled)

    return pred[0], prob[0][1]

if __name__ == "__main__":
    # Example usage
    result, probability = predict_rain([9.0, 90.0, 8.0, 20.0, 18.0])

    print("Prediction:", result)
    print("Probability of Rain:", round(probability, 2))

from google.colab import files
files.download("predict.py")
