import streamlit as st
import joblib
model = joblib.load('sales_ml')
st.header("Lemonade Sales Prediction")
st.image("lemon.jpg", caption="Lemonade")
temp = st.number_input("Insert temperature value",value=30)
flyers = st.slider("No of flyers distributed", 0, 50, 25)
op = model.predict([[temp,flyers]])
if st.button("Sales"):
    st.subheader(f"Sales Predicted :{round(op[0],2)}")
else:
    st.subheader("Give input values and click on Sales button")
