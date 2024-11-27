import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load the model
@st.cache_resource
def load_trained_model(model_path):
    return load_model(model_path)

model = load_trained_model("model.h5")

# Define the app layout
st.title("Model Deployment with Streamlit")
st.write("This app demonstrates deploying a trained model.")

# Collect user input for prediction
st.header("Input Features")
# Update the following based on your model's expected input shape
feature_1 = st.number_input("Feature 1", value=0.0)
feature_2 = st.number_input("Feature 2", value=0.0)
feature_3 = st.number_input("Feature 3", value=0.0)

# Combine inputs into a feature array
input_data = np.array([[feature_1, feature_2, feature_3]])

# Make a prediction
if st.button("Predict"):
    try:
        prediction = model.predict(input_data)
        st.subheader("Prediction")
        st.write(prediction)
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

st.caption("Ensure the inputs match the model's training features.")
