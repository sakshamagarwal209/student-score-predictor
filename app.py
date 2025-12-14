import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Student Score Predictor")
st.write("A simple ML app that predicts exam scores based on hours studied.")

HISTORY_FILE = "history.csv"

if "history" not in st.session_state:
    if os.path.exists(HISTORY_FILE):
        st.session_state.history = pd.read_csv(HISTORY_FILE).to_dict("records")
    else:
        st.session_state.history = []

hours = st.slider("Hours studied (Slider)", 0, 12, 5)
hours2 = st.number_input("Hours studied (Number Box):", 0.0, 11.0, 5.0, 0.5)

if st.button("Predict Score (Slider)"):
    prediction = model.predict([[hours]])[0]
    st.success(f"Predicted Score (Slider Input): {prediction:.2f}")

    st.session_state.history.append({
        "Hours": hours,
        "Predicted Score": round(float(prediction), 2),
        "Input Type": "Slider"
    })

if st.button("Predict Score (Number)"):
    prediction2 = model.predict([[hours2]])[0]
    st.info(f"Predicted Score (Box Input): {prediction2:.2f}")

    st.session_state.history.append({
        "Hours": hours2,
        "Predicted Score": round(float(prediction2), 2),
        "Input Type": "Number Box"
    })

if st.button("Clear History"):
    st.session_state.history = []
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    st.warning("History cleared!")

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    df.to_csv(HISTORY_FILE, index = False)
    
    st.subheader("Prediction History")
    st.dataframe(df)

    st.download_button(
        label = "Download History as CSV",
        data = df.to_csv(index = False),
        file_name = "prediction_history.csv",
        mime = "text/csv"
    )

    st.subheader("Prediction Thread")
    st.line_chart(df[["Hours", "Predicted Score"]])