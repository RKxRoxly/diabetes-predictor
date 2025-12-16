import streamlit as st
import pickle
import numpy as np

# Load the "brain"
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# --- SIDEBAR CODE STARTS HERE ---
# This puts a menu on the left side of the screen
st.sidebar.header("About the Project")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=100) # Adds a medical icon
st.sidebar.write("""
**Diabetes Prediction AI**
This tool uses a Random Forest Machine Learning model to assess diabetes risk.
""")
st.sidebar.write("---") # A divider line
st.sidebar.write("**Created by:**")
st.sidebar.write("Santanu Das") # <--- PUT YOUR NAME HERE
st.sidebar.write("B.Tech CSE 4th Sem ")
# --- SIDEBAR CODE ENDS HERE ---

# Main TitleC
st.title("Diabetes Prediction System 🏥")
st.write("Enter the patient's details below to generate a risk assessment.")

# Columns for inputs
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20)
    glucose = st.number_input("Glucose Level", 0, 200, 110) # Added default value 110
    bp = st.number_input("Blood Pressure", 0, 150, 70)      # Added default value 70
    skin = st.number_input("Skin Thickness", 0, 100, 20)    # Added default value 20

with col2:
    insulin = st.number_input("Insulin Level", 0, 900, 79)
    bmi = st.number_input("BMI", 0.0, 70.0, 32.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.number_input("Age", 0, 100, 33)

# The Button
if st.button("Predict Results"):
    features = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("Result: High Risk of Diabetes")
        st.warning("Recommendation: Please consult a specialist.")
    else:
        st.success("Result: Low Risk of Diabetes")