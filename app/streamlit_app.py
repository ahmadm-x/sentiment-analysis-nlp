import streamlit as st
import joblib

st.title("Sentiment Analysis App")
text = st.text_area("Enter text:")
model = joblib.load("app/sentiment_model.pkl")

if st.button("Predict"):
    pred = model.predict([text])
    st.write("Sentiment: Positive" if pred[0]==1 else "Sentiment: Negative")
