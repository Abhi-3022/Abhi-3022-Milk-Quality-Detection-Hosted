import pickle
import streamlit as st

def predict(taste, odor, ph, fat, turbidity, color, temp):
    model = pickle.load(open('model.pkl','rb'))
    result = model.predict([[ph,temp,taste, odor, fat, turbidity, color]])
    return result

# Title of the web app
st.title('Milk Quality Prediction App')

st.sidebar.title('Visualization')

# Creating 7 text input fields
taste = st.radio('Taste',['Good','Bad'])
if taste == 'Good':
  taste = 1
else:
  taste = 0
ph = st.number_input('pH', format="%f",placeholder = "Enter pH of the Milk in range 0 to 14")
odor = st.radio('Odor',['Good','Bad'])
if odor == 'Good':
  odor = 1
else:
  odor = 0
temp = st.number_input('Temperature', format="%f",placeholder = "Enter Temperature of the Milk in degree celsius.")
fat = st.radio('Fat',['Good','Bad'])
if fat == 'Good':
  fat = 1
else:
  fat = 0
color = st.number_input('Color', format="%f",placeholder = "Enter color of the Milk in grey shades from 0 to 255(255 means pure white)")
turbidity = st.radio('Turbidity',['Good','Bad'])
if turbidity == 'Good':
    turbidity = 1
else:
    turbidity = 0

# Predict button
if st.button('Predict'):
    # Call the predict function with the form data
    result = predict(taste, odor, fat, turbidity, ph, temp, color)

    if(result == 0):
      result = "High Quality Milk"
    elif(result == 2):
      result = "Medium Quality Milk"
    else:
      result = "Low Quality Milk"
    
    # Display the result
    st.markdown(f"**Prediction Result:** {result}")
