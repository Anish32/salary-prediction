
import streamlit as st
import pickle

# Load the saved model
loaded_model = pickle.load(open('triained_model.sav', 'rb'))

# Create the Streamlit app
st.title("Salary Prediction App")
experience = st.number_input("Enter Years of Experience:", min_value=0.0, step=0.1)
if st.button("Predict Salary"):
    salary_prediction = loaded_model.predict([[experience]])
    st.success(f"Predicted Salary: {salary_prediction[0]:.2f} Rupees")
    