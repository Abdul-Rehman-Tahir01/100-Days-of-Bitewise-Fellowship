import streamlit as st
import pandas as pd
import joblib as jb
import statistics as stat


# Importing the models
lr_model = jb.load('Models/logistic_regression.pkl')
dtc_model = jb.load('Models/decision_tree.pkl')
rfc_model = jb.load('Models/random_forest.pkl')
gbc_model = jb.load('Models/gradient_boosting.pkl')
svc_model = jb.load('Models/svc.pkl')


# Title of the webpage
st.title("Rainfall Prediction Using Machine Learning")

# Create two columns
col1, col2 = st.columns(2)

# Initialize input features and data preview variables
input_features = {}
data_preview = None
prediction_made = False
prediction = [None]*5

# Column 1: Feature Input or File Upload
with col1:
    st.write("")
    st.write("")
    st.subheader('Input Numerical Values')

    # Input fields for 13 features arranged in pairs (side by side)
    col1_1, col1_2, col1_3= st.columns(3)
    with col1_1:
        pressure = st.number_input("Pressure", step=None)
        mintemp = st.number_input("Min Temperature", step=None)
        cloud = st.number_input("Cloud", step=None)
        cloud_sun_interaction = st.number_input("Cloud Sun Interaction", step=None)

    with col1_2:
        maxtemp = st.number_input("Max Temperature", step=None)
        dewpoint = st.number_input("Dew Point", step=None)
        sunshine = st.number_input("Sunshine", step=None)
        temp_gradient = st.number_input("Temperature Gradient", step=None)
        
    with col1_3:
        temperature = st.number_input("Temperature", step=None)
        humidity = st.number_input("Humidity", step=None)
        windspeed = st.number_input("Wind Speed", step=None)
        temp_humidity_press_interaction = st.number_input("T - H - P Interaction", step=None)
    
    st.write('* T - H - P Interaction = Temperature - Humidity - Pressure Interaction')
        
    # Create a dictionary with the input values
    input_features = {
        "pressure": pressure,
        "maxtemp": maxtemp,
        "temperature": temperature,
        "mintemp": mintemp,
        "dewpoint": dewpoint,
        "humidity": humidity,
        "cloud": cloud,
        "sunshine": sunshine,
        "windspeed": windspeed,
        "cloud_sun_interaction": cloud_sun_interaction,
        "temp_gradient": temp_gradient,
        "temp_humidity_press_interaction": temp_humidity_press_interaction,
    }

# Column 2: Model Selection and Parameter Adjustment
with col2:
    st.write("")
    st.write("")

    st.subheader("\t\tInput Features")
    st.write("")
    st.write("")
    st.write(input_features)


for i in range(0, 2):
    st.write("")

if st.button("Make Prediction"):
    # Creating a dataframe for the input features
    input_features_df = pd.DataFrame([input_features])

    # Making the predictions
    prediction[0] = lr_model.predict(input_features_df)[0]
    prediction[1] = dtc_model.predict(input_features_df)[0]
    prediction[2] = rfc_model.predict(input_features_df)[0]
    prediction[3] = gbc_model.predict(input_features_df)[0]
    prediction[4] = svc_model.predict(input_features_df)[0]
    final_prediction = stat.mode(prediction)

    prediction_made = True

# Showing the prediction
if prediction_made:

    col3_1, col3_2 = st.columns(2)
    
    with col3_1:
        for i in range(0, 4):
            st.write("")
        st.subheader("Prediction")

        if final_prediction:
            prediction_text = "It will Rain"
            color = 'green'
        else:
            prediction_text = "It will not Rain"
            color = 'red'

        st.markdown(f"""
            <div style="font-size: 24px; font-weight: bold; color: {color};">
                {prediction_text}
            </div>
        """, unsafe_allow_html=True)
    
    with col3_2:
        for i in range(0, 3):
            st.write("")
        if final_prediction:
            st.image("Images/rain.png", width=250)
        else:
            st.image("Images/no rain.png", width=250)

        
   