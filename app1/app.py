import streamlit as st
import os 
st.title("Hello Streamlit!")
st.write({"key":"value"})
3+2
"hello world "

pressed = st.button("press me ")
if pressed:
    st.write("Pressed!")
    
st.title("this is the title!")
st.header("this is the header")
st.caption("this is the capttion")
st.subheader("this is the subheader")

code_example = """
def greet(name)
    print("hello",name)
"""
st.code(code_example)
st.divider()
st.image(os.path.join(os.getcwd(),"static","image.jpg"))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Generate sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Area Chart Section
st.subheader("📈 Area Chart")
st.area_chart(chart_data)

# Bar Chart Section
st.subheader("📊 Bar Chart")
st.bar_chart(chart_data)

# Line Chart Section
st.subheader("📉 Line Chart")
st.line_chart(chart_data)

# Scatter Chart Section (Custom using Matplotlib)
st.subheader("🟣 Scatter Chart (Matplotlib)")
fig, ax = plt.subplots()
ax.scatter(chart_data['A'], chart_data['B'], color='purple', alpha=0.6)
ax.set_xlabel('A')
ax.set_ylabel('B')
st.pyplot(fig)

df = pd.DataFrame({
    'Name':['tanishq', 'svetlana', 'rohit '],
    'Age':[20,19,29],
    'Occupation':['engineer', 'doctor','painter']
})
st.dataframe(df)
goa_coords = pd.DataFrame({
    'lat': [15.5402],
    'lon': [73.8353]
})

st.subheader("🗺️ Map of Goa")
st.map(goa_coords, zoom=10)
import streamlit as st

st.title('User Information System')

form_values = {
    "Name": None,
    "Height": None,
    "Weight": None
}

with st.form(key='user-form'):
    form_values['Name'] = st.text_input('Enter your name')
    form_values['Height'] = st.text_input('Enter your height')
    form_values['Weight'] = st.text_input('Enter your weight')

    submit_button = st.form_submit_button(label="Submit")

    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all details!")
        else:
            st.balloons() 
            st.write('### Info')
            for key, value in form_values.items():
                st.write(f"{key}: {value}")


import streamlit as st
import time

@st.cache_data(ttl=120)  # Cache this data for 60 seconds
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3)  # Delay to mimic an API call
    return {"data": "This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)
